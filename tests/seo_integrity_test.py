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


if __name__ == "__main__":
    unittest.main()
