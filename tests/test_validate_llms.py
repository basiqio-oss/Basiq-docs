import unittest
from unittest.mock import patch

from scripts import validate_llms as llms


class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.urls = [f"{llms.BASE}/{section}/page" for section in llms.SECTIONS]
        self.indexes = {
            "root": "\n".join(f"- [{section}]({url})" for section, url in llms.INDEXES.items()),
            **{
                section: f"- [Page]({llms.BASE}/{section}/page.md)"
                for section in llms.SECTIONS
            },
        }

    def test_complete_indexes_and_landing_page(self):
        expected, indexed, _, excluded, errors = llms.validate(
            self.urls + [f"{llms.BASE}/changelog"], self.indexes
        )
        self.assertEqual(expected, indexed)
        self.assertEqual(len(excluded), 1)
        self.assertEqual(errors, [])

    def test_missing_stale_duplicate_and_wrong_section(self):
        self.indexes["docs"] = (
            f"- [Page]({self.urls[0]}.md)\n"
            f"- [Again]({self.urls[0]})\n"
            f"- [Stale]({llms.BASE}/docs/old.md)\n"
            f"- [Wrong]({self.urls[1]}.md)"
        )
        self.indexes["changelog"] = ""
        _, _, _, _, errors = llms.validate(self.urls, self.indexes)
        for message in ("Duplicate page", "Stale docs", "Wrong section", "Missing changelog"):
            self.assertTrue(any(message in error for error in errors), errors)

    def test_missing_nested_index_and_noncanonical_links(self):
        self.indexes["root"] = self.indexes["root"].replace(llms.INDEXES["docs"], "https://example.com/docs/llms.txt")
        self.indexes["docs"] += "\n- [Bad](http://api.basiq.io/docs/other.md)"
        _, _, _, _, errors = llms.validate(self.urls, self.indexes)
        for message in ("Root index must link", "Unexpected root", "non-canonical"):
            self.assertTrue(any(message in error for error in errors), errors)

    def test_unknown_nested_sitemap_path_is_not_silently_excluded(self):
        _, _, _, _, errors = llms.validate(self.urls + [f"{llms.BASE}/docs/new/nested"], self.indexes)
        self.assertTrue(any("Unsupported documentation sitemap URL" in error for error in errors))

    def test_empty_section_fails(self):
        _, _, _, _, errors = llms.validate(self.urls[:2], self.indexes)
        self.assertTrue(any("Sitemap has no changelog pages" in error for error in errors))


class LiveResponseTests(unittest.TestCase):
    def test_markdown_rejects_html_and_missing_heading(self):
        page = f"{llms.BASE}/docs/page"
        with patch.object(llms, "fetch", return_value=(b"<html>not found</html>", "text/html", page + ".md")):
            self.assertIn("Invalid Markdown", llms.check_link((page, page + ".md")))
        with patch.object(llms, "fetch", return_value=(b"not a page", "text/markdown", page + ".md")):
            self.assertIn("no page title", llms.check_link((page, page + ".md")))

    def test_rejects_redirects(self):
        page = f"{llms.BASE}/docs/page"
        with patch.object(llms, "fetch", return_value=(b"# Title", "text/markdown", page)):
            self.assertIn("Redirected", llms.check_link((page, page + ".md")))

    def test_html_fallback_requires_matching_canonical_url(self):
        page = f"{llms.BASE}/docs/page"
        with patch.object(llms, "fetch", return_value=(b"<html>not found</html>", "text/html", page)):
            self.assertIn("Invalid HTML", llms.check_link((page, page)))
        html = f'<link rel="canonical" href="{page}">'.encode()
        with patch.object(llms, "fetch", return_value=(html, "text/html", page)):
            self.assertIsNone(llms.check_link((page, page)))


if __name__ == "__main__":
    unittest.main()
