#!/usr/bin/env python3
"""Small, dependency-free checks for the site's search-critical invariants."""

import json
import re
import unittest
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]


class SeoIntegrityTests(unittest.TestCase):
    def test_redirect_file_has_valid_three_column_rules(self):
        rules = []
        for number, raw in enumerate((ROOT / "_redirects").read_text().splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            self.assertEqual(3, len(parts), f"_redirects:{number} is malformed: {raw}")
            rules.append(tuple(parts))
        self.assertIn(("/index.html", "/", "301!"), rules)

    def test_sitemap_urls_exist_and_self_canonicalize(self):
        tree = ElementTree.parse(ROOT / "sitemap.xml")
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        for node in tree.findall("sm:url/sm:loc", ns):
            url = node.text.strip()
            path = urlparse(url).path
            file = ROOT / ("index.html" if path == "/" else path.lstrip("/"))
            self.assertTrue(file.exists(), f"Sitemap URL has no source file: {url}")
            html = file.read_text(errors="replace")
            match = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', html)
            self.assertIsNotNone(match, f"Missing canonical: {file.name}")
            self.assertEqual(url, match.group(1), f"Canonical mismatch: {file.name}")

    def test_cre_case_study_has_article_and_breadcrumb_schema(self):
        html = (ROOT / "impact-real-estate-property-intelligence.html").read_text()
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
        self.assertIn("generate_lead", (ROOT / "intake-modal.js").read_text())
        self.assertIn("generate_lead", (ROOT / "start-a-conversation.html").read_text())
        self.assertIn("generate_lead", (ROOT / "lead-magnet-form.js").read_text())

    def test_content_card_images_have_alt_text(self):
        for name in ("tutorials.html", "impact-studies.html"):
            html = (ROOT / name).read_text()
            empty = re.findall(r'<img\b[^>]*\balt=""[^>]*>', html)
            self.assertFalse(empty, f"{name} contains empty image alt text")

    def test_commercial_real_estate_hub_has_pillar_structure(self):
        html = (ROOT / "real-estate.html").read_text()
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

    def test_cre_spokes_link_back_to_hub(self):
        spokes = (
            "claude-cre-skills.html",
            "claude-cre-connectors.html",
            "claude-cre-cowork.html",
            "claude-cre-scheduled-tasks.html",
            "can-claude-connect-to-costar.html",
            "impact-real-estate-property-intelligence.html",
            "ai-in-real-estate-guide.html",
        )
        for name in spokes:
            html = (ROOT / name).read_text()
            self.assertRegex(html, r'href="real-estate\.html"', name)

    def test_primary_positioning_matches_supported_services(self):
        homepage = (ROOT / "index.html").read_text()
        navigation = (ROOT / "nav-dropdown.js").read_text()
        sitemap = (ROOT / "sitemap.xml").read_text()
        law_page = (ROOT / "law-firms.html").read_text()

        self.assertNotIn('href="law-firms.html"', homepage)
        self.assertNotIn('href="law-firms.html"', navigation)
        self.assertNotIn("law-firms.html", sitemap)
        self.assertRegex(
            law_page,
            r'<meta\s+name="robots"\s+content="noindex, follow"\s*/?>',
        )

        self.assertIn("Commercial Real Estate", homepage)
        self.assertIn("Commercial Real Estate", navigation)
        self.assertIn("Ways to work with us", navigation)
        for href in (
            "workflow-audit.html",
            "ai-enablement-workshop.html",
            "custom-agents.html",
        ):
            self.assertIn(f'href="{href}"', navigation)

    def test_homepage_explains_the_engagement_method(self):
        homepage = (ROOT / "index.html").read_text()
        for phrase in (
            "From one repeated workflow to a system your team can trust.",
            "Map the workflow",
            "Prove it with the team",
            "Deploy what earns a role",
        ):
            self.assertIn(phrase, homepage)


if __name__ == "__main__":
    unittest.main()
