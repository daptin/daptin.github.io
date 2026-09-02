#!/usr/bin/env python3
"""Whole-site structural, metadata, navigation, and relationship audit."""

from __future__ import annotations

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent
RELATIONSHIPS = json.loads((ROOT / "site-relationships.json").read_text())
VOID_ELEMENTS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class AuditParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.ids: set[str] = set()
        self.links: list[tuple[str, bool]] = []
        self.main_links: set[str] = set()
        self.h1 = 0
        self.main_h1 = 0
        self.current_primary: list[str] = []
        self.current_breadcrumb = 0
        self.canonical = ""
        self.og_url = ""
        self.meta_names: set[str] = set()
        self.has_breadcrumb = False
        self.has_nav_toggle = False
        self.has_site_script = False
        self.nesting_errors: list[str] = []
        self._in_primary = False
        self._in_breadcrumb = False

    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        if tag not in VOID_ELEMENTS:
            self.stack.append(tag)
        classes = set(values.get("class", "").split())
        if values.get("id"):
            self.ids.add(values["id"])
        if tag == "nav" and "desktop-nav" in classes:
            self._in_primary = True
        if tag == "nav" and "breadcrumb" in classes:
            self._in_breadcrumb = True
            self.has_breadcrumb = True
        if tag == "button" and "nav-toggle" in classes:
            self.has_nav_toggle = True
        if tag == "script" and values.get("src") == "/site.js":
            self.has_site_script = True
        if tag == "h1":
            self.h1 += 1
            if "main" in self.stack:
                self.main_h1 += 1
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href", "")
        if tag == "meta":
            if values.get("name"):
                self.meta_names.add(values["name"])
            if values.get("property") == "og:url":
                self.og_url = values.get("content", "")
        if tag == "a":
            href = values.get("href", "")
            in_main = "main" in self.stack and "footer" not in self.stack
            self.links.append((href, in_main))
            if in_main and href and not href.startswith("#"):
                self.main_links.add(href)
            if values.get("aria-current") == "page":
                if self._in_primary:
                    self.current_primary.append(href)
                if self._in_breadcrumb:
                    self.current_breadcrumb += 1
        elif values.get("aria-current") == "page" and self._in_breadcrumb:
            self.current_breadcrumb += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID_ELEMENTS:
            return
        if tag == "nav":
            if self._in_primary and self.stack and "nav" in self.stack:
                self._in_primary = False
            elif self._in_breadcrumb and self.stack and "nav" in self.stack:
                self._in_breadcrumb = False
        if not self.stack or self.stack[-1] != tag:
            self.nesting_errors.append(f"line {self.getpos()[0]} closes {tag} inside {self.stack[-1] if self.stack else 'nothing'}")
        elif tag in self.stack:
            index = len(self.stack) - 1 - self.stack[::-1].index(tag)
            self.stack = self.stack[:index]


def route_for(path: Path) -> str:
    relative = path.relative_to(ROOT)
    if relative.name == "404.html":
        return "/404.html"
    parent = relative.parent.as_posix()
    return "/" if parent == "." else f"/{parent}/"


def target_for(source: Path, href: str) -> tuple[Path | None, str]:
    parsed = urlparse(href)
    if parsed.scheme or href.startswith(("mailto:", "tel:", "javascript:")):
        return None, ""
    if parsed.path.startswith("/"):
        target = ROOT / parsed.path.lstrip("/")
    elif parsed.path:
        target = (source.parent / parsed.path).resolve()
    else:
        target = source
    if href.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target, parsed.fragment


def main() -> int:
    pages = sorted(ROOT.glob("**/index.html")) + [ROOT / "404.html"]
    failures: list[str] = []
    parsed: dict[Path, AuditParser] = {}
    incoming_main: dict[Path, set[Path]] = {path: set() for path in pages}

    if len(pages) != 63:
        failures.append(f"expected 63 HTML pages, found {len(pages)}")

    inventory = json.loads((ROOT / "site-pages.json").read_text())
    if len(inventory) != len(pages):
        failures.append("site-pages.json does not cover every HTML page")

    for path in pages:
        parser = AuditParser()
        parser.feed(path.read_text())
        parsed[path] = parser
        if parser.nesting_errors or parser.stack:
            failures.append(f"{path.relative_to(ROOT)}: invalid element nesting")

    for path, parser in parsed.items():
        route = route_for(path)
        expected_url = "https://daptin.github.io" + route
        relative = path.relative_to(ROOT)
        source = path.read_text()
        if parser.h1 != 1 or parser.main_h1 != 1:
            failures.append(f"{relative}: expected exactly one H1 inside main")
        if parser.canonical != expected_url:
            failures.append(f"{relative}: canonical {parser.canonical!r} != {expected_url!r}")
        if parser.og_url and parser.og_url != expected_url:
            failures.append(f"{relative}: og:url does not match canonical")
        for required in ("theme-color", "twitter:card", "twitter:image"):
            if required not in parser.meta_names:
                failures.append(f"{relative}: missing {required} metadata")
        if not parser.has_nav_toggle or not parser.has_site_script:
            failures.append(f"{relative}: missing shared mobile navigation")
        if 'class="grand-footer compact-footer"' not in source:
            failures.append(f"{relative}: missing compact shared footer")
        if re.search(r'</ul>\s*<a[^>]*class="[^"]*button', source, re.S):
            failures.append(f"{relative}: hero facts and action bypass the shared actions group")
        if route not in {"/", "/404.html"}:
            if not parser.has_breadcrumb or parser.current_breadcrumb != 1:
                failures.append(f"{relative}: missing one visible current breadcrumb")
            if len(parser.current_primary) != 1:
                failures.append(f"{relative}: expected one current primary navigation item")

        slug = route.strip("/").split("/")[-1] if route.strip("/") else ""
        if route.startswith("/features/") and route != "/features/" and 'class="related-content"' not in source:
            failures.append(f"{relative}: missing contextual relationship block")
        if route.startswith("/docs/") and route not in {"/docs/", "/docs/feature-guides/"}:
            if 'class="docs-context"' not in source:
                failures.append(f"{relative}: missing documentation section navigation")
            if 'class="page-toc"' not in source and 'class="guide-aside"' not in source:
                failures.append(f"{relative}: missing on-page contents navigation")
            if 'class="guide-sequence"' not in source:
                failures.append(f"{relative}: missing previous/next guide navigation")
        for item in RELATIONSHIPS.get(slug, []):
            if item["path"] == route:
                continue
            if item["path"] not in parser.main_links:
                failures.append(
                    f"{relative}: missing required {item['type'].lower()} link {item['path']}"
                )

        for href, in_main in parser.links:
            if not href:
                continue
            target, fragment = target_for(path, href)
            if target is None:
                continue
            if not target.exists():
                failures.append(f"{relative}: broken link {href}")
                continue
            if fragment and target in parsed and fragment not in parsed[target].ids:
                failures.append(f"{relative}: missing fragment in {href}")
            if in_main and target in incoming_main:
                incoming_main[target].add(path)

    for path, sources in incoming_main.items():
        route = route_for(path)
        if route in {"/404.html", "/docs/feature-guides/"}:
            continue
        if not sources and route != "/":
            failures.append(f"{path.relative_to(ROOT)}: no incoming main-content links")

    if "<lastmod>" in (ROOT / "sitemap.xml").read_text():
        failures.append("sitemap.xml: lastmod must be source-derived or omitted")
    stylesheet = (ROOT / "styles.css").read_text()
    if re.search(r'font-size:\s*(?:0\.[0-7][0-9]*|\.[0-7][0-9]*)rem|font:\s*[^;]*(?:0\.[0-7][0-9]*|\.[0-7][0-9]*)rem', stylesheet):
        failures.append("styles.css: supporting type must not be smaller than 0.8rem")

    if failures:
        print("Whole-site audit failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Whole-site audit passed for {len(pages)} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
