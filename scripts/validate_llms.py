#!/usr/bin/env python3
"""Compare the Git-managed LLM indexes with the published ReadMe sitemap."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parent.parent
BASE = "https://api.basiq.io"
SITEMAP = f"{BASE}/sitemap.xml"
SECTIONS = ("docs", "reference", "changelog")
INDEXES = {section: f"{BASE}/{section}/llms.txt" for section in SECTIONS}
LINK = re.compile(r"\[(?:\\.|[^\]\\])*\]\(([^)\s]+)\)")
USER_AGENT = "Basiq-docs-llms-validation/1.0"


class CanonicalLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonical = attrs.get("href")


def fetch(url):
    for attempt in range(4):
        try:
            request = Request(url, headers={"User-Agent": USER_AGENT})
            with urlopen(request, timeout=30) as response:
                return response.read(), response.headers.get_content_type(), response.url
        except HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 3:
                raise
        except (URLError, TimeoutError):
            if attempt == 3:
                raise
        time.sleep(2 ** (attempt + 1))


def parse_sitemap(data):
    root = ET.fromstring(data)
    if root.tag != "{http://www.sitemaps.org/schemas/sitemap/0.9}urlset":
        raise ValueError("Expected a sitemap urlset, not a sitemap index or other XML")
    urls = [element.findtext("{*}loc") for element in root.findall("{*}url")]
    if not urls or any(not url for url in urls):
        raise ValueError("Sitemap is empty or contains an empty URL")
    return urls


def page_url(url):
    """Return a canonical sitemap URL for a page link, or None."""
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.netloc != "api.basiq.io":
        return None
    if parsed.query or parsed.fragment or not re.fullmatch(
        r"/(?:docs|reference|changelog)/[^/]+", parsed.path
    ):
        return None
    if parsed.path.endswith("/llms.txt"):
        return None
    return BASE + parsed.path.removesuffix(".md")


def validate(sitemap_urls, indexes):
    errors = []
    expected = {section: set() for section in SECTIONS}
    excluded = []
    for url in sitemap_urls:
        page = page_url(url)
        if page and page == url:
            expected[urlsplit(url).path.split("/")[1]].add(url)
        elif url == f"{BASE}/changelog":
            excluded.append((url, "section landing page, not a changelog entry"))
        elif any(url.startswith(f"{BASE}/{section}/") for section in SECTIONS):
            errors.append(f"Unsupported documentation sitemap URL: {url}")
        else:
            excluded.append((url, "outside the indexed documentation page paths"))

    duplicates = [url for url, count in Counter(sitemap_urls).items() if count > 1]
    errors.extend(f"Duplicate sitemap URL: {url}" for url in sorted(duplicates))
    for section in SECTIONS:
        if not expected[section]:
            errors.append(f"Sitemap has no {section} pages; refusing to report coverage")

    root_links = LINK.findall(indexes["root"])
    root_counts = Counter(root_links)
    for url in INDEXES.values():
        if root_counts[url] != 1:
            errors.append(f"Root index must link exactly once to {url} (found {root_counts[url]})")
    for url in root_links:
        if url not in INDEXES.values():
            errors.append(f"Unexpected root index link: {url}")

    indexed = {section: set() for section in SECTIONS}
    links_to_check = {}
    seen = Counter()
    for section in SECTIONS:
        for link in LINK.findall(indexes[section]):
            if link == f"{BASE}/llms.txt":
                continue
            page = page_url(link)
            if not page:
                errors.append(f"Invalid or non-canonical link in {section}/llms.txt: {link}")
                continue
            actual_section = urlsplit(page).path.split("/")[1]
            if actual_section != section:
                errors.append(f"Wrong section in {section}/llms.txt: {link}")
                continue
            seen[page] += 1
            indexed[section].add(page)
            links_to_check[page] = link

    for page, count in sorted(seen.items()):
        if count > 1:
            errors.append(f"Duplicate page entry ({count}): {page}")
    for section in SECTIONS:
        for page in sorted(expected[section] - indexed[section]):
            errors.append(f"Missing {section} page: {page}")
        for page in sorted(indexed[section] - expected[section]):
            errors.append(f"Stale {section} link (not in sitemap): {page}")

    return expected, indexed, links_to_check, excluded, errors


def check_link(item):
    page, link = item
    try:
        data, content_type, final_url = fetch(link)
    except (HTTPError, URLError, TimeoutError, OSError) as error:
        return f"Inaccessible link {link}: {error}"
    if final_url != link:
        return f"Redirected link {link} -> {final_url}; verify its canonical URL"
    if link.endswith(".md"):
        if content_type not in ("text/markdown", "text/x-markdown"):
            return f"Invalid Markdown response {link}: Content-Type {content_type}"
        if not re.search(rb"(?m)^#\s+\S", data):
            return f"Invalid Markdown response {link}: no page title heading"
    elif content_type not in ("text/html", "text/markdown", "text/x-markdown"):
        return f"Invalid page response {link}: Content-Type {content_type}"
    elif content_type == "text/html":
        parser = CanonicalLinkParser()
        parser.feed(data.decode("utf-8", errors="replace"))
        if parser.canonical != page:
            return f"Invalid HTML response {link}: canonical link is {parser.canonical!r}, expected {page}"
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sitemap-file", type=Path, help="Use a saved sitemap instead of fetching the live sitemap")
    parser.add_argument("--check-live", action="store_true", help="Fetch every indexed page and validate its response")
    args = parser.parse_args()
    try:
        data = args.sitemap_file.read_bytes() if args.sitemap_file else fetch(SITEMAP)[0]
        sitemap_urls = parse_sitemap(data)
        indexes = {"root": (ROOT / "llms.txt").read_text(encoding="utf-8")}
        indexes.update({section: (ROOT / section / "llms.txt").read_text(encoding="utf-8") for section in SECTIONS})
    except (OSError, ValueError, ET.ParseError, URLError, TimeoutError) as error:
        print(f"Unable to load sitemap or indexes: {error}", file=sys.stderr)
        return 1

    expected, indexed, links, excluded, errors = validate(sitemap_urls, indexes)
    print("# llms.txt sitemap coverage\n")
    print("| Section | Sitemap pages | Indexed pages | Missing | Coverage |")
    print("| --- | ---: | ---: | ---: | ---: |")
    for section in SECTIONS:
        total = len(expected[section])
        covered = len(expected[section] & indexed[section])
        coverage = f"{100 * covered / total:.1f}%" if total else "n/a"
        print(f"| {section} | {total} | {len(indexed[section])} | {total - covered} | {coverage} |")
    print(f"\nNested indexes: {', '.join(INDEXES.values())}")
    print(f"\nSitemap entries excluded: {len(excluded)}")
    for url, reason in excluded:
        print(f"- {url}: {reason}")

    if args.check_live:
        print(f"\nChecking {len(links)} indexed page responses...")
        with ThreadPoolExecutor(max_workers=3) as executor:
            errors.extend(error for error in executor.map(check_link, sorted(links.items())) if error)
            fallbacks = [(page, page + ".md") for page, link in sorted(links.items()) if link == page]
            markdown_results = list(executor.map(check_link, fallbacks))
        if fallbacks:
            print("\n## HTML fallback pages")
            for (page, _), result in zip(fallbacks, markdown_results):
                print(f"- {page}: {result or 'Markdown now works; consider switching the index link'}")
    if errors:
        print(f"\n## Issues ({len(errors)})")
        for error in errors:
            print(f"- {error}")
        return 1
    print("\nNo missing pages, stale links, duplicates, or invalid index links found.")
    if args.check_live:
        print("All indexed page responses passed the live checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
