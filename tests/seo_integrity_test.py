#!/usr/bin/env python3
"""Small, dependency-free checks for the site's search-critical invariants."""

import json
from html import unescape
import re
import unittest
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]


class SeoIntegrityTests(unittest.TestCase):
    def test_redirect_file_has_valid_three_column_rules(self):
        rules = []
        for number, raw in enumerate((ROOT / "_redirects").read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            self.assertEqual(3, len(parts), f"_redirects:{number} is malformed: {raw}")
            rules.append(tuple(parts))
        self.assertIn(("/index.html", "/", "301!"), rules)

    def test_every_page_redirects_its_extensionless_form(self):
        """Search Console indexed /page and /page.html as two URLs for pages
        missing a rule. Every top-level page needs one, not just the hub's."""
        redirects = (ROOT / "_redirects").read_text(encoding="utf-8")
        for file in sorted(ROOT.glob("*.html")):
            if file.name in ("index.html", "404.html"):
                continue
            stem = re.escape(file.stem)
            self.assertRegex(redirects, rf"(?m)^/{stem}\s+/{stem}\.html\s+301!",
                             f"{file.name} has no extensionless redirect")

    def test_sitemap_urls_exist_and_self_canonicalize(self):
        tree = ElementTree.parse(ROOT / "sitemap.xml")
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        for node in tree.findall("sm:url/sm:loc", ns):
            url = node.text.strip()
            path = urlparse(url).path
            file = ROOT / ("index.html" if path == "/" else path.lstrip("/"))
            self.assertTrue(file.exists(), f"Sitemap URL has no source file: {url}")
            html = file.read_text(encoding="utf-8", errors="replace")
            match = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', html)
            self.assertIsNotNone(match, f"Missing canonical: {file.name}")
            self.assertEqual(url, match.group(1), f"Canonical mismatch: {file.name}")

    def test_cre_case_study_has_article_and_breadcrumb_schema(self):
        html = (ROOT / "impact-real-estate-property-intelligence.html").read_text(encoding="utf-8")
        blocks = re.findall(
            r'<script\s+type="application/ld\+json">(.*?)</script>', html, re.S
        )
        types = set()

        def walk(value):
            if isinstance(value, dict):
                item_type = value.get("@type")
                if isinstance(item_type, str):
                    types.add(item_type)
                elif isinstance(item_type, list):
                    types.update(item_type)
                for child in value.values():
                    walk(child)
            elif isinstance(value, list):
                for child in value:
                    walk(child)

        for block in blocks:
            walk(json.loads(block))
        self.assertIn("Article", types)
        self.assertIn("BreadcrumbList", types)

    def test_primary_forms_emit_generate_lead_events(self):
        self.assertIn("generate_lead", (ROOT / "start-a-conversation.html").read_text(encoding="utf-8"))
        self.assertIn("generate_lead", (ROOT / "lead-magnet-form.js").read_text(encoding="utf-8"))

    def test_field_guide_form_has_capture_and_download_fallbacks(self):
        html = (ROOT / "ai-in-real-estate-guide.html").read_text(encoding="utf-8")
        script = (ROOT / "lead-magnet-form.js").read_text(encoding="utf-8")

        self.assertIn('name="subject"', html)
        self.assertIn('data-remove-prefix', html)
        self.assertIn('id="lead-form-status"', html)
        self.assertIn("fetch('/',", script)
        self.assertIn("output/pdf/ai-in-real-estate-field-guide.pdf", script)

    def test_field_guide_pdf_is_forced_to_download(self):
        headers = (ROOT / "_headers").read_text(encoding="utf-8")
        self.assertIn("/output/pdf/ai-in-real-estate-field-guide.pdf", headers)
        self.assertIn('Content-Disposition: attachment; filename="AI-in-Real-Estate-Field-Guide.pdf"', headers)

    def test_content_card_images_have_alt_text(self):
        for name in ("learn.html", "case-studies.html"):
            html = (ROOT / name).read_text(encoding="utf-8")
            empty = re.findall(r'<img\b[^>]*\balt=""[^>]*>', html)
            self.assertFalse(empty, f"{name} contains empty image alt text")

    def test_commercial_real_estate_hub_has_pillar_structure(self):
        html = (ROOT / "real-estate.html").read_text(encoding="utf-8")
        visible = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", html, flags=re.S)
        visible = re.sub(r"<[^>]+>", " ", visible)
        words = re.findall(r"\b[\w'-]+\b", visible)

        title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S).group(1)
        self.assertIn("Commercial Real Estate", title)
        self.assertIn("commercial real estate", re.sub(r"<[^>]+>", "", h1).lower())
        self.assertGreaterEqual(len(words), 900)

        required_spokes = {
            "claude-cre-skills.html",
            "claude-cre-connectors.html",
            "claude-cre-cowork.html",
            "claude-cre-scheduled-tasks.html",
            "can-claude-connect-to-costar.html",
            "impact-real-estate-property-intelligence.html",
            "ai-in-real-estate-guide.html",
            "mortr.html",
        }
        links = set(re.findall(r'href="([^"]+)"', html))
        self.assertTrue(required_spokes.issubset(links))

        blocks = re.findall(
            r'<script\s+type="application/ld\+json">(.*?)</script>', html, re.S
        )
        schema = [json.loads(block) for block in blocks]
        schema_text = json.dumps(schema)
        self.assertIn('"FAQPage"', schema_text)
        self.assertEqual(6, schema_text.count('"Question"'))

    def test_mortr_page_describes_current_crm_and_bov_product(self):
        html = (ROOT / "mortr.html").read_text(encoding="utf-8")
        visible = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", html, flags=re.S)
        visible = re.sub(r"<[^>]+>", " ", visible)
        title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)
        h1 = re.sub(r"<[^>]+>", "", re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S).group(1))
        description = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html).group(1)

        self.assertIn("crm", title.lower())
        self.assertIn("bovs", title.lower())
        self.assertIn("crm", h1.lower())
        self.assertIn("bovs", h1.lower())
        self.assertIn("property owner", description.lower())
        self.assertIn("dated public records", visible.lower())
        self.assertIn("dated servicer", visible.lower())
        self.assertNotIn("polk", html.lower())
        self.assertIn("Pinellas", visible)
        self.assertIn("Hillsborough", visible)
        self.assertIn("Pasco", visible)

        links = set(re.findall(r'href="([^"]+)"', html))
        self.assertTrue(
            {
                "real-estate.html",
                "claude-cre-connectors.html",
                "ai-in-real-estate-guide.html",
                "start-a-conversation.html",
            }.issubset(links)
        )
        self.assertIn("assets/mortr/mortr-chat-demo.gif", html)
        self.assertIn("assets/mortr/mortr-securitized-loans.jpg", html)
        for src in (
            "assets/mortr/mortr-chat-demo.gif",
            "assets/mortr/mortr-securitized-loans.jpg",
            "assets/mortr/mortr-bov-branding.png",
        ):
            match = re.search(rf'<img\b[^>]*\bsrc="{re.escape(src)}"[^>]*>', html)
            self.assertIsNotNone(match, f"missing img for {src}")
            self.assertRegex(match.group(0), r'\balt="[^"]+"')

    def test_cre_spokes_link_back_to_hub(self):
        spokes = (
            "claude-cre-skills.html",
            "claude-cre-connectors.html",
            "claude-cre-cowork.html",
            "claude-cre-scheduled-tasks.html",
            "can-claude-connect-to-costar.html",
            "impact-real-estate-property-intelligence.html",
            "ai-in-real-estate-guide.html",
            "mortr.html",
        )
        for name in spokes:
            html = (ROOT / name).read_text(encoding="utf-8")
            self.assertRegex(html, r'href="real-estate\.html"', name)

    def test_primary_positioning_matches_supported_services(self):
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        # the nav is static markup now, so read it from a page
        navigation = re.search(
            r'<header class="nav">.*?</header>', homepage, re.S
        ).group(0)
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        law_page = (ROOT / "law-firms.html").read_text(encoding="utf-8")

        # law-firms.html is published: it is the only industry page with a
        # real differentiator (the Florida Bar opinion section), so it is
        # indexed, in the sitemap and in the nav rather than orphaned
        self.assertIn('href="law-firms.html"', homepage)
        self.assertIn('href="law-firms.html"', navigation)
        self.assertIn("law-firms.html", sitemap)
        self.assertNotIn("noindex", law_page)

        self.assertIn("Commercial Real Estate", homepage)
        self.assertIn("Commercial Real Estate", navigation)
        self.assertIn('href="ai-transformation.html"', navigation)
        self.assertIn('href="ai-engineering.html"', navigation)

    def test_homepage_explains_the_engagement_method(self):
        # assert against rendered text, not raw source: headlines carry inline
        # <b>/<em> for the two-tone treatment, which a raw substring test breaks
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        visible = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", homepage))
        # The three approach lanes lead to two service paths.
        for phrase in (
            "AI services company",
            "win the AI renaissance",
            "Our approach",
            "Strategy",
            "Transformation",
            "Engineering",
            "customer-facing products",
        ):
            self.assertIn(phrase, visible)
        section = re.search(r'<section class="ph-section" id="what-we-do".*?</section>', homepage, re.S).group(0)
        self.assertNotIn("About us", section)
        self.assertNotIn("We altr how you work with AI.", section)
        self.assertEqual(2, section.count('class="ph-slip" href="ai-transformation.html"'))
        self.assertEqual(1, section.count('class="ph-slip" href="ai-engineering.html"'))
        self.assertEqual(3, section.count('class="ph-slip-figure ph-slip-figure--'))
        for image in (
            "approach-strategy-dividers.webp",
            "approach-transformation-mallet.webp",
            "approach-engineering-gear.webp",
        ):
            self.assertIn(f'assets/plates/{image}', section)
            self.assertTrue((ROOT / "assets" / "plates" / image).is_file())
        self.assertNotIn("ph-chisel-block", section)
        self.assertNotIn("ph-gear-axle", section)
        self.assertNotIn("Three services.", visible)
        for retired in ("Zero to one", "One to ten", "in the order they earn"):
            self.assertNotIn(retired, visible)

    def test_faq_schema_answers_appear_on_the_page(self):
        """Google drops FAQ rich results when the schema text is not on the page.

        Edits to a visible answer must land in the JSON-LD too, and an anchor
        that closes right before a period leaves a stray space once tags are
        stripped, which is enough to break the match.
        """
        for file in sorted(ROOT.glob("*.html")):
            html = file.read_text(encoding="utf-8")
            for raw in re.findall(
                r'<script type="application/ld\+json">(.*?)</script>', html, re.S
            ):
                graph = json.loads(raw)
                nodes = graph.get("@graph", [graph])
                for node in nodes:
                    if node.get("@type") != "FAQPage":
                        continue
                    # The JSON-LD lives in a <script>, so stripping tags over
                    # the whole file leaves the schema text in the haystack and
                    # every answer trivially matches itself. Drop scripts and
                    # styles first, or this test asserts nothing.
                    body = re.sub(
                        r"<script[^>]*>.*?</script>|<style[^>]*>.*?</style>",
                        " ", html, flags=re.S,
                    )
                    visible = re.sub(
                        r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", body))
                    )
                    for entry in node["mainEntity"]:
                        answer = re.sub(
                            r"\s+", " ",
                            unescape(re.sub(r"<[^>]+>", " ", entry["acceptedAnswer"]["text"])),
                        ).strip()
                        self.assertIn(
                            answer, visible,
                            f"{file.name}: FAQ answer missing from page text for "
                            f"{entry['name']!r}",
                        )


    def test_navigation_is_static_html_on_every_page(self):
        """The nav used to be rebuilt by JavaScript, so crawlers that do not
        execute JS saw different internal links than users did. It is static
        markup now: every page must carry the same links to the two
        service paths and the three industries."""
        required = (
            'href="ai-transformation.html"',
            'href="ai-engineering.html"',
            'href="real-estate.html"',
            'href="nonprofits.html"',
            'href="ecommerce.html"',
            'href="case-studies.html"',
            'href="learn.html"',
        )
        for file in sorted(ROOT.glob("*.html")):
            html = file.read_text(encoding="utf-8")
            match = re.search(r'<header class="nav">.*?</header>', html, re.S)
            self.assertIsNotNone(match, f"{file.name}: no nav")
            nav = match.group(0)
            for link in required:
                self.assertIn(link, nav, f"{file.name}: nav missing {link}")

    def test_workflow_automation_tampa_page_does_not_cannibalize_ai_consulting(self):
        automation = (ROOT / "workflow-automation-consultant-tampa.html").read_text(encoding="utf-8")
        consulting = (ROOT / "ai-consulting-tampa.html").read_text(encoding="utf-8")

        def title_of(html):
            return re.search(r"<title>(.*?)</title>", html, re.S).group(1).strip()

        def h1_of(html):
            raw = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S).group(1)
            text = re.sub(r"<[^>]+>", " ", raw)
            return re.sub(r"\s+", " ", text).strip()

        auto_title = title_of(automation)
        auto_h1 = h1_of(automation)
        consult_title = title_of(consulting)
        consult_h1 = h1_of(consulting)

        self.assertNotEqual(auto_title, consult_title)
        self.assertNotEqual(auto_h1.lower(), consult_h1.lower())
        self.assertIn("workflow automation consultant", auto_title.lower())
        self.assertIn("workflow automation consultant", auto_h1.lower())
        self.assertNotIn("ai consultant", auto_title.lower())
        self.assertIn("ai consulting", consult_title.lower())
        self.assertIn('href="ai-consulting-tampa.html"', automation)
        self.assertIn('href="workflow-automation-consultant-tampa.html"', consulting)
        self.assertIn("workflow-automation-consultant-tampa.html", (ROOT / "llms.txt").read_text(encoding="utf-8"))
        self.assertIn("workflow-automation-consultant-tampa.html", (ROOT / "sitemap.xml").read_text(encoding="utf-8"))
        self.assertIn(
            "/workflow-automation-consultant-tampa",
            (ROOT / "_redirects").read_text(encoding="utf-8"),
        )

    def test_homepage_and_about_do_not_cannibalize_tampa_consulting(self):
        """GSC, last 7 days Sep 21 to 27: 'ai consulting company' is the
        homepage at 236 impressions, avg position 4.8, 0 clicks. 'ai consulting
        tampa' is the homepage at 17 impressions, position 2.3, versus
        ai-consulting-tampa.html at 2 impressions, position 25. 'ai consultant
        tampa' is the homepage at 7 impressions, position 3.9, versus the
        dedicated page at 6 impressions, position 23.2.

        The homepage may say it is an AI consulting company for ops teams, but
        its title and meta must not use the local head phrases. The dedicated
        page owns 'AI consulting in Tampa' and 'AI consultant in Tampa'. About
        stays a studio page, and the homepage hands the local query off with
        a visible anchor."""
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        about = (ROOT / "about.html").read_text(encoding="utf-8")
        consulting = (ROOT / "ai-consulting-tampa.html").read_text(encoding="utf-8")

        def title_of(html):
            return re.search(r"<title>(.*?)</title>", html, re.S).group(1).strip()

        def meta_of(html):
            return re.search(
                r'<meta\s+name="description"\s+content="([^"]+)"', html
            ).group(1)

        home_title = title_of(homepage)
        home_meta = meta_of(homepage)
        about_title = title_of(about)
        about_meta = meta_of(about)
        consult_title = title_of(consulting)
        consult_meta = meta_of(consulting)
        local_heads = (
            "ai consulting tampa",
            "ai consultant tampa",
            "ai consulting in tampa",
            "ai consultant in tampa",
        )

        self.assertEqual("AI Consulting Company | AI Transformation and AI Engineering | altr", home_title)
        self.assertIn("ai engineering", home_title.lower())
        self.assertIn("ai transformation", home_title.lower())
        self.assertEqual(2, homepage.count(f'content="{home_title}"'))
        self.assertEqual(3, homepage.count(f'content="{home_meta}"'))
        self.assertGreaterEqual(len(home_meta), 140)
        self.assertLessEqual(len(home_meta), 160)
        self.assertIn("ai services company", home_meta.lower())
        self.assertIn("customer-facing products", home_meta.lower())
        for phrase in local_heads:
            self.assertNotIn(phrase, home_title.lower())
            self.assertNotIn(phrase, home_meta.lower())
        self.assertNotIn("consultant", home_title.lower())

        self.assertEqual(
            "AI Consulting in Tampa | AI Consultant for Tampa Bay Businesses | altr",
            consult_title,
        )
        self.assertIn("ai consulting", consult_title.lower())
        self.assertIn("ai consultant", consult_title.lower())
        self.assertEqual(2, consulting.count(f'content="{consult_title}"'))
        self.assertEqual(3, consulting.count(f'content="{consult_meta}"'))
        self.assertIn(f'"name": "{consult_title}"', consulting)
        self.assertIn(f'"description": "{consult_meta}"', consulting)
        self.assertIn("ai consultant in tampa", consult_meta.lower())
        self.assertIn("ai consulting", consult_meta.lower())
        h1 = re.sub(
            r"\s+", " ",
            re.sub(r"<[^>]+>", " ", re.search(r"<h1[^>]*>(.*?)</h1>", consulting, re.S).group(1)),
        ).lower()
        self.assertIn("ai consulting in tampa", h1)
        self.assertIn("altr is an AI consulting firm in Tampa, run by founders Alex Britton and Jarred Robidoux.", consulting)

        self.assertEqual("About altr | Studio and team in Tampa Bay", about_title)
        self.assertNotIn("consulting", about_title.lower())
        self.assertNotIn("consultant", about_title.lower())
        self.assertNotIn("tampa ai automation", about_title.lower())
        self.assertNotIn("consulting", about_meta.lower())
        self.assertNotIn("consultant", about_meta.lower())
        self.assertEqual(2, about.count(f'content="{about_title}"'))
        self.assertEqual(3, about.count(f'content="{about_meta}"'))

        hero = re.search(
            r'class="pp-hero[^"]*".*?</section>',
            homepage,
            re.S,
        ).group(0)
        self.assertNotIn('href="ai-consulting-tampa.html"', hero)
        self.assertNotIn("Based in Tampa", hero)
        self.assertIn(">Tampa, FL</a>", homepage)
        self.assertGreaterEqual(about.count('href="ai-consulting-tampa.html"'), 2)

    def test_ai_strategy_page_sells_what_the_rest_of_the_site_sells(self):
        """The page used to sell a 7-day audit, two named deliverables and an
        embedded engineering team, none of which altr does. It also carried
        two animated fake demos. Keep it aligned and keep it honest."""
        html = (ROOT / "how-we-altr-work.html").read_text(encoding="utf-8")

        self.assertIn("AI Strategy", re.search(r"<title>(.*?)</title>", html, re.S).group(1))
        self.assertIn("AI strategy", html)
        # the audit is a standalone service now, not the first of three phases
        for step in ("Map", "Rank", "Recommend"):
            self.assertIn(f"<h3>{step}</h3>", html)
        for retired in ("7-day", "seven-day", "priced up front",
                        "embedded engineering", "30-day Roadmap", "Opportunity Map"):
            self.assertNotIn(retired, html, f"retired claim back on the page: {retired}")
        self.assertNotRegex(html, r"Days? \d", "published day counts are back")

    def test_retired_claims_are_gone_from_every_page(self):
        """The 7-day audit, up-front pricing and the embedded engineering team
        were removed from the strategy page but survived on four others and in
        llms.txt, because the original guard only checked one file. Check the
        whole site. about.html keeps 'forward deployed engineer' as a person's
        job title in their bio, which is a description of someone rather than
        a service being sold."""
        retired = ("7-day", "seven-day", "priced up front", "embedded engineering",
                   "embedded headcount", "30-day Roadmap", "Opportunity Map",
                   "forward deployed engineering", "forward-deployed engineering")
        targets = sorted(ROOT.glob("*.html")) + [ROOT / "llms.txt"]
        for path in targets:
            text = path.read_text(encoding="utf-8")
            for claim in retired:
                if path.name == "about.html" and claim.startswith("forward"):
                    continue
                self.assertNotIn(
                    claim.lower(), text.lower(),
                    f"retired claim back on {path.name}: {claim}",
                )

    def test_workshops_are_still_offered(self):
        """Workshops remain accessible beneath the AI Transformation path."""
        for name in ("ai-enablement-workshop.html", "ai-workshop.html"):
            self.assertTrue((ROOT / name).exists(), f"{name} is missing")
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        transformation = (ROOT / "ai-transformation.html").read_text(encoding="utf-8")
        self.assertIn('href="ai-transformation.html"', homepage)
        self.assertIn('href="ai-enablement-workshop.html"', transformation)


    def test_learning_center_pages_are_wired_everywhere(self):
        """A learning page nobody can reach is not in any engine's index.
        Every page the hub links must exist, be in the sitemap and llms.txt,
        and have its extensionless form redirected to the canonical .html."""
        hub = (ROOT / "learn.html").read_text(encoding="utf-8")
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
        redirects = (ROOT / "_redirects").read_text(encoding="utf-8")
        links = re.findall(r'<h3><a href="([^"]+\.html)">', hub)
        self.assertGreaterEqual(len(links), 30)
        for href in links + ["learn.html"]:
            self.assertTrue((ROOT / href).exists(), f"learn.html links a missing page: {href}")
            self.assertIn(f"https://altrwork.com/{href}", sitemap, f"{href} not in sitemap")
            self.assertIn(f"https://altrwork.com/{href}", llms, f"{href} not in llms.txt")
            self.assertRegex(redirects, rf"(?m)^/{re.escape(href[:-5])}\s+/{re.escape(href)}\s+301!",
                             f"{href} has no extensionless redirect")

    def test_the_blog_index_is_folded_into_the_learning_center(self):
        """One index, not two listing the same articles. The old blog URL and
        its aliases must land on the hub so inbound links keep their value."""
        self.assertFalse((ROOT / "tutorials.html").exists())
        redirects = (ROOT / "_redirects").read_text(encoding="utf-8")
        for old in ("/tutorials", "/tutorials.html", "/resources", "/resources.html"):
            self.assertRegex(redirects, rf"(?m)^{re.escape(old)}\s+/learn\.html\s+301!")
        for file in sorted(ROOT.glob("*.html")):
            self.assertNotIn('href="tutorials.html"', file.read_text(encoding="utf-8"), file.name)

    def test_every_page_links_the_learning_center(self):
        for file in sorted(ROOT.glob("*.html")):
            html = file.read_text(encoding="utf-8")
            nav = re.search(r'<header class="nav">.*?</header>', html, re.S).group(0)
            self.assertIn('href="learn.html"', nav, f"{file.name}: nav missing learn.html")

    def test_answer_engine_simulation_finds_an_answer_for_every_query(self):
        """tests/answer_engine_sim.py is a proxy for whether an engine could
        lift an answer from this site. Every query in the set must land on a
        page that answers it; a new query with no page fails here until the
        page exists."""
        import importlib.util
        spec = importlib.util.spec_from_file_location("sim", ROOT / "tests" / "answer_engine_sim.py")
        sim = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sim)
        results = sim.run()
        weak = [f"{r['query']} -> {r['page']} ({r['score']})" for r in results if r["verdict"] != "strong"]
        self.assertEqual([], weak, "queries without a strong answer page")


    def test_news_months_are_catalogued_and_chained(self):
        """Monthly digests live behind one archive page, not in the hub grid.
        Every month must be in the archive, the sitemap, llms.txt and the
        redirects, and link back to the archive."""
        archive = (ROOT / "ai-news-archive.html").read_text(encoding="utf-8")
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
        redirects = (ROOT / "_redirects").read_text(encoding="utf-8")
        months = sorted(ROOT.glob("ai-news-for-business-*-2026.html"))
        self.assertGreaterEqual(len(months), 6)
        for file in months:
            name = file.name
            self.assertIn(f'href="{name}"', archive, f"{name} missing from the archive")
            self.assertIn(f"https://altrwork.com/{name}", sitemap)
            self.assertIn(f"https://altrwork.com/{name}", llms)
            self.assertRegex(redirects, rf"(?m)^/{re.escape(name[:-5])}\s+/{re.escape(name)}\s+301!")
            self.assertIn('href="ai-news-archive.html"', file.read_text(encoding="utf-8"), name)
        self.assertIn('href="ai-news-archive.html"', (ROOT / "learn.html").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
