"""Tell IndexNow engines (Bing, Yandex, Seznam, Naver) which pages changed.

Usage:
    python .github/indexnow.py                        # every URL in sitemap.xml
    python .github/indexnow.py learn.html ...         # just these pages
    python .github/indexnow.py --changed-since <sha>  # pages changed since a commit

The site is served by Netlify, not through Cloudflare's proxy, so Cloudflare
Crawler Hints never sees it change. The indexnow workflow runs this with
--changed-since after every push to main instead.

The key is the 32-hex-character .txt file at the site root. It must be live
at https://altrwork.com/<key>.txt before a submission is accepted.
"""
import re
import subprocess
import sys
from pathlib import Path

import requests

HOST = "altrwork.com"
ROOT = Path(__file__).resolve().parent.parent


def find_key() -> str:
    keys = [p.stem for p in ROOT.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}", p.stem)]
    if len(keys) != 1:
        sys.exit(f"Expected one IndexNow key file at the site root, found {len(keys)}")
    return keys[0]


def sitemap_urls() -> list[str]:
    return re.findall(r"<loc>(.*?)</loc>", (ROOT / "sitemap.xml").read_text(encoding="utf-8"))


def page_url(path: str) -> str:
    path = path.lstrip("/")
    return f"https://{HOST}/" if path == "index.html" else f"https://{HOST}/{path}"


def changed_since(sha: str) -> list[str]:
    """Sitemap URLs whose page changed after `sha`, plus any newly listed in the sitemap."""
    diff = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AMR", sha, "HEAD"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout.split()
    old_sitemap = subprocess.run(
        ["git", "show", f"{sha}:sitemap.xml"], cwd=ROOT, capture_output=True, text=True,
    ).stdout
    listed = sitemap_urls()
    changed = {page_url(p) for p in diff if p.endswith(".html")}
    added = set(listed) - set(re.findall(r"<loc>(.*?)</loc>", old_sitemap))
    return [u for u in listed if u in changed or u in added]


def main() -> None:
    args = sys.argv[1:]
    if args[:1] == ["--changed-since"]:
        urls = changed_since(args[1])
        if not urls:
            print("No listed pages changed; nothing to submit")
            return
    else:
        urls = [page_url(p) for p in args] or sitemap_urls()

    key = find_key()
    key_url = f"https://{HOST}/{key}.txt"
    live = requests.get(key_url, timeout=15)
    if live.status_code != 200 or live.text.strip() != key:
        sys.exit(f"Key file is not live at {key_url} (HTTP {live.status_code}); deploy it first")

    r = requests.post(
        "https://api.indexnow.org/indexnow",
        json={"host": HOST, "key": key, "keyLocation": key_url, "urlList": urls},
        timeout=30,
    )
    # 200 and 202 both mean accepted; 202 means the key is still being verified.
    print(f"HTTP {r.status_code}: submitted {len(urls)} URLs {r.text[:200]}")
    for u in urls:
        print(" ", u)
    if r.status_code not in (200, 202):
        sys.exit(1)


if __name__ == "__main__":
    main()
