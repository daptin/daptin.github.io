#!/usr/bin/env python3
"""Apply shared navigation, metadata, breadcrumb, and relationship UI.

The repository intentionally commits deployable HTML. This script keeps the
repeated static fragments synchronized without adding a runtime framework.
"""

from __future__ import annotations

from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urlparse
import unicodedata


ROOT = Path(__file__).resolve().parent.parent
RELATIONSHIPS = json.loads((ROOT / "site-relationships.json").read_text())

DOC_GROUPS = {
    "Start": ["getting-started", "data-modeling", "apis"],
    "Identity and access": [
        "authentication",
        "permissions",
        "two-factor-auth",
        "oauth-provider",
    ],
    "Files and publishing": [
        "files",
        "cloud-storage",
        "sites",
        "protocols",
        "webdav",
    ],
    "Application behavior": [
        "actions",
        "scheduled-work",
        "state-tracking",
        "email-actions",
    ],
    "Connections": [
        "integrations",
        "ai-routing",
        "realtime",
        "collaboration",
        "mail",
        "metering",
    ],
    "Operate": [
        "server-configuration",
        "database-setup",
        "production-deployment",
        "tls-certificates",
        "monitoring",
        "clustering",
        "operations",
    ],
    "Focused interfaces": ["graphql"],
}

LABELS = {
    "": "Home",
    "product": "Product",
    "features": "Features",
    "engineering": "Engineering",
    "use-cases": "Use cases",
    "deploy": "Deploy",
    "examples": "Examples",
    "docs": "Docs",
    "getting-started": "Getting started",
    "data-modeling": "Data modeling",
    "apis": "APIs and discovery",
    "authentication": "Authentication",
    "permissions": "Permissions and tenancy",
    "oauth-provider": "OAuth and OIDC provider",
    "files": "Files and assets",
    "cloud-storage": "Cloud storage",
    "sites": "Sites and publishing",
    "actions": "Backend actions",
    "scheduled-work": "Scheduled work",
    "state-tracking": "State tracking",
    "integrations": "External integrations",
    "ai-routing": "AI model gateway",
    "realtime": "Realtime events",
    "collaboration": "Collaborative documents",
    "mail": "Mail server",
    "protocols": "File and feed protocols",
    "metering": "Metering and quotas",
    "operations": "Operations",
    "feature-guides": "Feature guides",
    "server-configuration": "Server configuration",
    "database-setup": "Database setup",
    "production-deployment": "Production deployment",
    "monitoring": "Monitoring",
    "clustering": "Clustering",
    "graphql": "GraphQL",
    "two-factor-auth": "Two-factor authentication",
    "tls-certificates": "TLS certificates",
    "email-actions": "Email actions",
    "webdav": "WebDAV-style access",
}

CURRENT_NAV = {
    "product": "/product/",
    "features": "/product/",
    "engineering": "/engineering/",
    "use-cases": "/use-cases/",
    "deploy": "/engineering/",
    "examples": "/use-cases/",
    "docs": "/docs/",
}

PRIMARY_NAV_LINKS = '''
        <a href="/product/">Product</a>
        <a href="/use-cases/">Solutions</a>
        <a href="/engineering/">Developers</a>
        <a href="/docs/">Docs</a>
        <a class="nav-run" href="/docs/getting-started/">Run Daptin →</a>
      '''

COMPACT_FOOTER = '''    <footer class="grand-footer compact-footer">
      <h2 class="visually-hidden">Daptin site links</h2>
      <div class="footer-intro">
        <a class="brand" href="/"><img src="/images/theme-logo.png" alt="" /><span>Daptin</span></a>
        <p>The self-hosted application server behind your product.</p>
        <a class="footer-run" href="/docs/getting-started/">Run Daptin →</a>
      </div>
      <nav class="footer-directory" aria-label="Footer">
        <div><p class="footer-heading">Product</p><ul>
          <li><a href="/product/">Overview</a></li><li><a href="/features/">Features</a></li><li><a href="/use-cases/">Use cases</a></li>
        </ul></div>
        <div><p class="footer-heading">Learn</p><ul>
          <li><a href="/docs/">Documentation</a></li><li><a href="/docs/getting-started/">Getting started</a></li><li><a href="/examples/">Examples</a></li>
        </ul></div>
        <div><p class="footer-heading">Operate</p><ul>
          <li><a href="/deploy/">Deploy</a></li><li><a href="/docs/operations/">Operations</a></li><li><a href="/engineering/">Engineering</a></li>
        </ul></div>
        <div><p class="footer-heading">Project</p><ul>
          <li><a href="https://github.com/daptin/daptin">Source code ↗</a></li><li><a href="https://github.com/daptin/daptin/releases">Releases ↗</a></li><li><a href="https://github.com/daptin/daptin/blob/master/LICENSE">LGPL-3.0 ↗</a></li>
        </ul></div>
      </nav>
      <div class="footer-bottom"><span>Daptin · Open source · Self-hosted</span><a href="/docs/">Documentation</a><a href="https://github.com/daptin/daptin">GitHub ↗</a></div>
    </footer>'''


class PageInfo(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.description = ""
        self.h1 = ""
        self._capture = ""
        self._parts: list[str] = []
        self.stack: list[str] = []
        self.main_links: list[str] = []
        self.main_words: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        self.stack.append(tag)
        if tag in {"title", "h1"}:
            self._capture = tag
            self._parts = []
        if tag == "meta" and values.get("name") == "description":
            self.description = values.get("content", "")
        if tag == "a" and "main" in self.stack and "footer" not in self.stack:
            href = values.get("href", "")
            if href and not href.startswith("#"):
                self.main_links.append(href)

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._parts.append(data)
        if "main" in self.stack and "footer" not in self.stack and "script" not in self.stack:
            self.main_words.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == self._capture:
            value = re.sub(r"\s+", " ", "".join(self._parts)).strip()
            if tag == "title":
                self.title = value
            else:
                self.h1 = value
            self._capture = ""
            self._parts = []
        if tag in self.stack:
            index = len(self.stack) - 1 - self.stack[::-1].index(tag)
            self.stack = self.stack[:index]


def route_for(path: Path) -> str:
    relative = path.relative_to(ROOT)
    if relative.name == "404.html":
        return "/404.html"
    parent = relative.parent.as_posix()
    return "/" if parent == "." else f"/{parent}/"


def slug_for(route: str) -> str:
    parts = [part for part in route.strip("/").split("/") if part]
    return parts[-1] if parts else ""


def page_type(route: str) -> str:
    if route == "/":
        return "home"
    if route == "/404.html":
        return "utility"
    if route.startswith("/features/") and route != "/features/":
        return "feature"
    if route.startswith("/docs/") and route not in {"/docs/", "/docs/feature-guides/"}:
        return "guide"
    if route in {"/docs/", "/docs/feature-guides/", "/features/"}:
        return "directory"
    return "marketing"


def breadcrumb(route: str) -> str:
    if route in {"/", "/404.html"}:
        return ""
    parts = [part for part in route.strip("/").split("/") if part]
    items = ['<li><a href="/">Home</a></li>']
    current = ""
    for index, part in enumerate(parts):
        current += f"/{part}"
        label = LABELS.get(part, part.replace("-", " ").title())
        if index == len(parts) - 1 and parts[0] == "docs" and len(parts) > 1:
            group_name = next((name for name, slugs in DOC_GROUPS.items() if part in slugs), "")
            if group_name:
                items.append(f'<li>{escape(group_name)}</li>')
        if index == len(parts) - 1:
            items.append(f'<li aria-current="page">{escape(label)}</li>')
        else:
            items.append(f'<li><a href="{current}/">{escape(label)}</a></li>')
    return (
        '      <nav class="breadcrumb" aria-label="Breadcrumb">\n'
        "        <ol>" + "".join(items) + "</ol>\n"
        "      </nav>\n"
    )


def doc_sequence(route: str) -> str:
    if not route.startswith("/docs/") or route in {"/docs/", "/docs/feature-guides/"}:
        return ""
    slugs = [slug for group in DOC_GROUPS.values() for slug in group]
    slug = slug_for(route)
    if slug not in slugs:
        return ""
    index = slugs.index(slug)
    links = []
    if index > 0:
        previous = slugs[index - 1]
        links.append(f'<a rel="prev" href="/docs/{previous}/"><span>Previous</span><strong>{escape(LABELS[previous])}</strong></a>')
    if index < len(slugs) - 1:
        following = slugs[index + 1]
        links.append(f'<a rel="next" href="/docs/{following}/"><span>Next</span><strong>{escape(LABELS[following])}</strong></a>')
    return '<nav class="guide-sequence" aria-label="Previous and next guides">' + "".join(links) + "</nav>\n"


def ensure_page_toc(text: str, route: str) -> str:
    if not route.startswith("/docs/") or route in {"/docs/", "/docs/feature-guides/"}:
        return text
    if 'class="guide-aside"' in text or 'class="page-toc"' in text:
        return text
    main_start = text.find("<main")
    main_end = text.find('class="related-content"', main_start)
    if main_end == -1:
        main_end = text.find('class="final-cta"', main_start)
    fragment = text[main_start:main_end]
    headings = list(re.finditer(r'<h2(?:\s+id="([^"]+)")?>(.*?)</h2>', fragment, re.S))
    if len(headings) < 3:
        return text
    links = []
    used: set[str] = set()
    offset = main_start
    replacements = []
    for match in headings:
        label = re.sub(r"<[^>]+>", "", match.group(2))
        label = re.sub(r"\s+", " ", label).strip()
        identifier = match.group(1)
        if not identifier:
            value = unicodedata.normalize("NFKD", label).encode("ascii", "ignore").decode().lower()
            identifier = re.sub(r"[^a-z0-9]+", "-", value).strip("-") or "section"
            base = identifier
            number = 2
            while identifier in used:
                identifier = f"{base}-{number}"
                number += 1
            start, end = match.span()
            replacements.append((offset + start, offset + end, f'<h2 id="{identifier}">{match.group(2)}</h2>'))
        used.add(identifier)
        links.append(f'<li><a href="#{identifier}">{escape(label)}</a></li>')
    for start, end, replacement in reversed(replacements):
        text = text[:start] + replacement + text[end:]
    toc = '<details class="page-toc"><summary>On this page</summary><ul>' + "".join(links) + "</ul></details>\n        "
    return text.replace('<p class="guide-meta">', toc + '<p class="guide-meta">', 1)


def doc_context(route: str) -> str:
    if not route.startswith("/docs/") or route in {"/docs/", "/docs/feature-guides/"}:
        return ""
    slug = slug_for(route)
    group_name = next((name for name, slugs in DOC_GROUPS.items() if slug in slugs), "Guides")
    siblings = DOC_GROUPS.get(group_name, [slug])
    links = []
    for item in siblings:
        current = ' aria-current="page"' if item == slug else ""
        links.append(
            f'<li><a href="/docs/{item}/"{current}>{escape(LABELS[item])}</a></li>'
        )
    return (
        '      <aside class="docs-context" aria-label="Documentation section">\n'
        f"        <strong>{escape(group_name)}</strong>\n"
        f"        <ul>{''.join(links)}</ul>\n"
        '        <p class="guide-meta"><span>Last reviewed: 2026-09-02</span>'
        '<span>Applies to the latest release available on the review date; check your installed release</span>'
        '<a href="https://github.com/daptin/daptin">Review source ↗</a></p>\n'
        "      </aside>\n"
    )


def related(route: str) -> str:
    slug = slug_for(route)
    items = RELATIONSHIPS.get(slug)
    if not items:
        return ""
    current_path = route
    cards = []
    for item in items:
        if item["path"] == current_path:
            continue
        cards.append(
            f'          <a href="{escape(item["path"])}">'
            f'<span>{escape(item["type"])}</span>'
            f'<strong>{escape(item["title"])}</strong>'
            f'<span>{escape(item["description"])}</span></a>'
        )
    if not cards:
        return ""
    return (
        '      <section class="related-content" aria-labelledby="related-title">\n'
        '        <p class="kicker">Continue the task</p>\n'
        '        <h2 id="related-title">Understand the connections, then implement them.</h2>\n'
        "        <p>These are the prerequisites, implementation details, boundaries, and proof most relevant to this page.</p>\n"
        f'        <div class="related-links">\n{"".join(cards)}\n        </div>\n'
        "      </section>\n"
    )


def normalize_head(text: str, route: str) -> str:
    url = "https://daptin.github.io" + route
    text = re.sub(
        r'<link\s+rel="canonical"\s+href="[^"]+"\s*/>',
        f'<link rel="canonical" href="{url}" />',
        text,
        flags=re.S,
    )
    if 'rel="canonical"' not in text:
        text = text.replace("<title>", f'<link rel="canonical" href="{url}" />\n    <title>', 1)
    if 'rel="icon"' not in text:
        text = text.replace(
            '<link rel="stylesheet"',
            '<link rel="icon" href="/images/theme-favicon.png" />\n    <link rel="stylesheet"',
            1,
        )
    if 'name="theme-color"' not in text:
        text = re.sub(
            r'(<meta name="viewport"[^>]+/>)',
            r'\1\n    <meta name="theme-color" content="#17242a" />',
            text,
            count=1,
        )
    if 'name="twitter:card"' not in text:
        text = text.replace(
            '</head>',
            '    <meta name="twitter:card" content="summary_large_image" />\n  </head>',
            1,
        )
    if 'name="twitter:image"' not in text:
        marker = '<meta name="twitter:card" content="summary_large_image" />'
        text = text.replace(
            marker,
            marker + '\n    <meta name="twitter:image" content="https://daptin.github.io/images/og-card.png" />',
            1,
        )
    # Keep machine breadcrumbs aligned with the self-canonical route.
    if '"@type": "BreadcrumbList"' in text:
        matches = list(re.finditer(r'("position":\s*\d+,\s*"name":\s*"[^"]+",\s*"item":\s*)"[^"]+"', text))
        if matches:
            match = matches[-1]
            text = text[:match.start()] + match.group(1) + json.dumps(url) + text[match.end():]
    return text


def set_current_nav(text: str, route: str) -> str:
    text = re.sub(
        r'(<nav id="primary-navigation" class="desktop-nav" aria-label="Primary">).*?(</nav>)',
        lambda match: match.group(1) + PRIMARY_NAV_LINKS + match.group(2),
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(r'(<nav[^>]*class="desktop-nav"[^>]*>.*?</nav>)', lambda m: m.group(1).replace(' aria-current="page"', ''), text, count=1, flags=re.S)
    first = route.strip("/").split("/")[0] if route.strip("/") else ""
    target = CURRENT_NAV.get(first)
    if target:
        nav_pattern = re.compile(r'(<nav[^>]*class="desktop-nav"[^>]*>.*?</nav>)', re.S)
        def update(match):
            nav = match.group(1)
            return nav.replace(f'href="{target}"', f'href="{target}" aria-current="page"', 1)
        text = nav_pattern.sub(update, text, count=1)
    return text


def modernize(path: Path) -> dict:
    route = route_for(path)
    text = path.read_text()
    text = normalize_head(text, route)
    text = set_current_nav(text, route)
    text = re.sub(
        r'(</ul>\s*)(<a\s+[^>]*class="[^"]*button[^"]*".*?</a\s*>)',
        r'\1<div class="actions">\2</div>',
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r'<p class="guide-meta">.*?</p>',
        '<p class="guide-meta"><span>Last reviewed: 2026-09-02</span>'
        '<span>Applies to the latest release available on the review date; check your installed release</span>'
        '<a href="https://github.com/daptin/daptin">Review source ↗</a></p>',
        text,
        flags=re.S,
    )
    text = re.sub(r'    <footer class="grand-footer(?: compact-footer)?">.*?</footer>', COMPACT_FOOTER, text, count=1, flags=re.S)

    crumb = breadcrumb(route)
    if crumb and 'class="breadcrumb"' in text:
        text = re.sub(r'      <nav class="breadcrumb".*?</nav>\n', crumb, text, count=1, flags=re.S)

    if "site.js" not in text:
        text = text.replace("</body>", '    <script src="/site.js"></script>\n  </body>', 1)

    if "nav-toggle" not in text and 'class="desktop-nav"' in text:
        text = text.replace(
            '      <nav class="desktop-nav" aria-label="Primary">',
            '      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-navigation">Menu</button>\n'
            '      <nav id="primary-navigation" class="desktop-nav" aria-label="Primary">',
            1,
        )

    if "class=\"breadcrumb\"" not in text:
        crumb = breadcrumb(route)
        if crumb:
            text = re.sub(r'(<main\b[^>]*>\n)', lambda match: match.group(1) + crumb, text, count=1)

    if "class=\"docs-context\"" not in text:
        context = doc_context(route)
        if context:
            crumb_end = "      </nav>\n"
            crumb_pos = text.find(crumb_end, text.find('class="breadcrumb"'))
            if crumb_pos != -1:
                insert_at = crumb_pos + len(crumb_end)
                text = text[:insert_at] + context + text[insert_at:]

    text = ensure_page_toc(text, route)

    if "class=\"related-content\"" not in text:
        block = related(route)
        if block:
            text = text.replace('      <section class="final-cta">', block + '      <section class="final-cta">', 1)

    if "class=\"guide-sequence\"" not in text:
        sequence = doc_sequence(route)
        if sequence:
            text = text.replace('      <section class="final-cta">', '      ' + sequence + '      <section class="final-cta">', 1)

    # Normalize the reported hero spacing defect.
    if route == "/use-cases/" and '<div class="actions">' not in text[text.find('<main'):text.find('</main>')]:
        text = re.sub(
            r'(</ul>\s*)(<a class="button button-light" href="\.\./examples/".*?</a>)',
            r'\1<div class="actions">\2</div>',
            text,
            count=1,
            flags=re.S,
        )

    path.write_text(text)

    info = PageInfo()
    info.feed(text)
    first = route.strip("/").split("/")[0] if route.strip("/") else ""
    return {
        "route": route,
        "type": page_type(route),
        "title": info.title,
        "h1": info.h1,
        "description": info.description,
        "primaryNavigation": LABELS.get(CURRENT_NAV.get(first, "").strip("/"), "") if first else "",
        "relationshipKey": slug_for(route) if slug_for(route) in RELATIONSHIPS else None,
        "mainWordCount": len(re.findall(r"\b[\w'-]+\b", " ".join(info.main_words))),
        "mainDestinations": sorted(set(info.main_links)),
    }


def main() -> None:
    pages = sorted(ROOT.glob("**/index.html")) + [ROOT / "404.html"]
    inventory = [modernize(path) for path in pages]
    inventory.sort(key=lambda item: item["route"])
    (ROOT / "site-pages.json").write_text(json.dumps(inventory, indent=2) + "\n")
    print(f"Modernized {len(inventory)} pages and refreshed site-pages.json")


if __name__ == "__main__":
    main()
