#!/usr/bin/env python3
"""A stdlib-only proxy for how an AI answer engine picks what to cite.

ChatGPT search, Perplexity, Gemini and Google's AI Overviews all do roughly
the same thing: retrieve PASSAGES (not pages) that match the question, prefer
a page whose title and headings say it is about that question, and lift a
short self-contained answer. This script scores every query in
answer_engine_queries.json against the site on those three things:

  coverage  - share of the query's terms found in the best passage (BM25 ranks)
  intent    - share of the query's terms in that page's <title>/<h1>/<h2>s
  shape     - is the passage liftable: a summary box or FAQ answer of 20-120
              words scores 1.0, a section opening that size 0.7, else 0.4

It is a proxy, not a measurement. It says whether the site has a page that
answers the question in a form an engine can lift. It cannot say whether an
engine trusts the domain, which is off-site signal (directories, reviews,
mentions) and is measured by actually asking the engines.

    python3 tests/answer_engine_sim.py          # table + summary
    python3 tests/answer_engine_sim.py --json   # machine-readable
"""

import json
import math
import re
import sys
from collections import Counter
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"404.html", "privacy.html", "terms.html", "website-terms.html"}
STOP = set("""a an and are as at be by can do does for from how i in is it its of on or
our the to vs what when which who why with you your my me we us this that there""".split())
STRONG, WEAK = 0.75, 0.5


def stem(word):
    for suf in ("ing", "ers", "ies", "ed", "es", "er", "s"):
        if len(word) > len(suf) + 3 and word.endswith(suf):
            return word[: -len(suf)] + ("y" if suf == "ies" else "")
    return word


def terms(text):
    return [stem(w) for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP]


def text_of(fragment):
    fragment = re.sub(r"<script[^>]*>.*?</script>|<style[^>]*>.*?</style>", " ", fragment, flags=re.S)
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def passages_of(name, html):
    """Split a page into the units an engine retrieves."""
    out = []
    main = re.search(r"<main.*?</main>", html, re.S)
    body = main.group(0) if main else html
    for m in re.finditer(r'<div class="article-summary">(.*?)</div>', body, re.S):
        out.append(("summary", text_of(m.group(1))))
    # FAQ answers come from the FAQPage schema, which engines read directly.
    # seo_integrity_test.py guarantees every schema answer is visible text,
    # so this also covers FAQs laid out as panels rather than an #faq block.
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        graph = json.loads(raw)
        for node in graph.get("@graph", [graph]):
            if node.get("@type") == "FAQPage":
                for entry in node["mainEntity"]:
                    out.append(("faq", entry["name"] + " " + text_of(entry["acceptedAnswer"]["text"])))
    # sections: an h2 and everything up to the next h2
    parts = re.split(r"(?=<h2[\s>])", body)
    for part in parts:
        h = re.match(r"<h2[^>]*>(.*?)</h2>(.*)", part, re.S)
        if not h:
            continue
        first_p = re.search(r"<p[^>]*>(.*?)</p>", h.group(2), re.S)
        opening = text_of(first_p.group(1)) if first_p else ""
        out.append(("section", text_of(h.group(1)) + " " + text_of(h.group(2))[:1500], opening))
    lede = re.search(r'<p class="page-lede"[^>]*>(.*?)</p>', body, re.S)
    if lede:
        out.append(("lede", text_of(lede.group(1))))
    return out


def load_site():
    pages = {}
    for file in sorted(ROOT.glob("*.html")):
        if file.name in SKIP or "thank-you" in file.name:
            continue
        html = file.read_text(encoding="utf-8", errors="replace")
        title = text_of(re.search(r"<title>(.*?)</title>", html, re.S).group(1))
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
        heads = [title, text_of(h1.group(1)) if h1 else ""]
        heads += [text_of(h) for h in re.findall(r"<h2[^>]*>(.*?)</h2>", html, re.S)]
        types = set(re.findall(r'"@type":\s*"(\w+)"', html))
        pages[file.name] = {
            "title": title,
            "heads_title": terms(" ".join(heads[:2])),
            "heads_all": terms(" ".join(heads)),
            "passages": passages_of(file.name, html),
            "types": types,
        }
    return pages


def score(pages, query):
    q = list(dict.fromkeys(terms(query)))
    flat = [(name, p) for name, page in pages.items() for p in page["passages"]]
    docs = [Counter(terms(p[1])) for _, p in flat]
    n = len(docs)
    avg = sum(sum(d.values()) for d in docs) / max(n, 1)
    df = {t: sum(1 for d in docs if t in d) for t in q}
    best = []
    for (name, p), d in zip(flat, docs):
        length = sum(d.values()) or 1
        bm25 = 0.0
        for t in q:
            if t not in d:
                continue
            idf = math.log(1 + (n - df[t] + 0.5) / (df[t] + 0.5))
            bm25 += idf * d[t] * 2.2 / (d[t] + 1.2 * (0.25 + 0.75 * length / avg))
        page = pages[name]
        title_hit = sum(t in page["heads_title"] for t in q) / len(q)
        any_hit = sum(t in page["heads_all"] for t in q) / len(q)
        intent = 0.7 * title_hit + 0.3 * any_hit
        coverage = sum(t in d for t in q) / len(q)
        kind = p[0]
        words = len(p[1].split())
        if kind in ("summary", "faq") and 20 <= words <= 120:
            shape = 1.0
        elif kind == "section" and 20 <= len(p[2].split()) <= 120:
            shape = 0.7
        elif kind == "lede":
            shape = 0.6
        else:
            shape = 0.4
        total = 0.45 * coverage + 0.35 * intent + 0.2 * shape
        best.append((bm25, total, name, kind, coverage, intent, shape))
    # the engine retrieves by relevance, then judges what it retrieved
    best.sort(key=lambda r: (-r[0], -r[1]))
    top = best[:8]
    # engines index titles too: a page whose title and H1 carry nearly all of
    # the query is a candidate even when its body passages rank lower
    seen = {r[2] for r in top}
    for r in best:
        if r[2] not in seen and sum(t in pages[r[2]]["heads_title"] for t in q) >= 0.8 * len(q):
            top.append(r)
            seen.add(r[2])
    top.sort(key=lambda r: -r[1])
    winner = top[0]
    rivals = sorted({r[2] for r in top if r[2] != winner[2] and r[1] >= winner[1] - 0.05})
    return {
        "query": query,
        "page": winner[2],
        "passage": winner[3],
        "coverage": round(winner[4], 2),
        "intent": round(winner[5], 2),
        "shape": round(winner[6], 2),
        "score": round(winner[1], 2),
        "verdict": "strong" if winner[1] >= STRONG else "weak" if winner[1] >= WEAK else "missing",
        "rivals": rivals,
    }


def run():
    pages = load_site()
    queries = json.loads((ROOT / "tests" / "answer_engine_queries.json").read_text())
    out = []
    for item in queries:
        r = dict(score(pages, item["q"]), group=item["group"])
        # a query may name the page that should own it; landing anywhere else
        # is a miss however well the other page scores
        if item.get("expect") and r["page"] != item["expect"]:
            r["verdict"] = "wrong-page"
            r["expected"] = item["expect"]
        out.append(r)
    return out


def main():
    results = run()
    if "--json" in sys.argv:
        print(json.dumps(results, indent=2))
        return
    width = max(len(r["query"]) for r in results)
    for r in results:
        rivals = f"  (close: {', '.join(r['rivals'])})" if r["rivals"] else ""
        print(f"{r['verdict']:<8} {r['score']:.2f}  {r['query']:<{width}}  -> {r['page']} [{r['passage']}]{rivals}")
    counts = Counter(r["verdict"] for r in results)
    print(f"\n{counts['strong']} strong, {counts['weak']} weak, {counts['missing']} missing, {counts['wrong-page']} wrong page, of {len(results)} queries")


if __name__ == "__main__":
    main()
