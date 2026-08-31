#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "$0")/.." && pwd)"
pages=("$root_dir/index.html" "$root_dir/product/index.html" "$root_dir/use-cases/index.html" "$root_dir/deploy/index.html" "$root_dir/examples/index.html")

printf 'Marketing pages: %s\n' "${#pages[@]}"

heading_count=$(rg -o '<h[1-6][ >]' "${pages[@]}" | wc -l | tr -d ' ')
printf 'Headings: %s\n' "$heading_count"
if (( heading_count >= 80 )); then
  printf 'FAIL: expected fewer than 80 headings\n' >&2
  exit 1
fi

homepage_words=$(python3 - "$root_dir/index.html" <<'PY'
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in {"script", "style"} and self.skip:
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

parser = VisibleText()
parser.feed(Path(sys.argv[1]).read_text())
print(len(re.findall(r"[A-Za-z0-9][A-Za-z0-9:+./'-]*", " ".join(parser.parts))))
PY
)
printf 'Homepage words: %s\n' "$homepage_words"
if (( homepage_words > 700 )); then
  printf 'FAIL: expected no more than 700 homepage words\n' >&2
  exit 1
fi

banned='powerful|robust|seamless|comprehensive|modern|flexible|unlock|leverage|future-proof|not just|all-in-one|build anything|everything you need'
if rg -ni "${banned}" "${pages[@]}"; then
  printf 'FAIL: banned marketing phrase found\n' >&2
  exit 1
fi

ai_style='the model is not|it is the contract|one runtime speaks|where your data lives|hard backend rules|reliability is enforced|parts that are hard to fake|one model becomes|short list on purpose|put a complete operation'
if rg -ni "${ai_style}" "${pages[@]}"; then
  printf 'FAIL: slogan-like AI copy found\n' >&2
  exit 1
fi

python3 - "${pages[@]}" <<'PY'
from html.parser import HTMLParser
from pathlib import Path
import sys

class HeadingBreaks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.heading = None
        self.found = False
    def handle_starttag(self, tag, attrs):
        if tag in {"h1", "h2"}:
            self.heading = tag
        elif tag == "br" and self.heading:
            self.found = True
    def handle_startendtag(self, tag, attrs):
        if tag == "br" and self.heading:
            self.found = True
    def handle_endtag(self, tag):
        if tag == self.heading:
            self.heading = None

failed = False
for filename in sys.argv[1:]:
    parser = HeadingBreaks()
    parser.feed(Path(filename).read_text())
    if parser.found:
        print(f"Manual line break in a primary heading: {filename}", file=sys.stderr)
        failed = True
raise SystemExit(1 if failed else 0)
PY

if rg -n '—' "${pages[@]}"; then
  printf 'FAIL: em dash found in visible site source\n' >&2
  exit 1
fi

if rg -n 'v0\.(?!12\.36)' "${pages[@]}" --pcre2; then
  printf 'FAIL: stale Daptin version found\n' >&2
  exit 1
fi

if rg -ni '\b[0-9]+(?:%|x|×)\b|hours? saved|times faster' "${pages[@]}" --pcre2; then
  printf 'FAIL: unsupported quantified marketing claim found\n' >&2
  exit 1
fi

python3 - "${pages[@]}" <<'PY'
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

class Paragraphs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_p = False
        self.in_footer = False
        self.buffer = []
        self.items = []
    def handle_starttag(self, tag, attrs):
        if tag == "footer":
            self.in_footer = True
        if tag == "p" and not self.in_footer:
            self.in_p = True
            self.buffer = []
    def handle_data(self, data):
        if self.in_p:
            self.buffer.append(data)
    def handle_endtag(self, tag):
        if tag == "p" and self.in_p:
            value = re.sub(r"\s+", " ", "".join(self.buffer)).strip()
            if len(value) >= 45:
                self.items.append(value)
            self.in_p = False
        if tag == "footer":
            self.in_footer = False

seen = defaultdict(list)
for filename in sys.argv[1:]:
    parser = Paragraphs()
    parser.feed(Path(filename).read_text())
    for value in parser.items:
        seen[value].append(filename)

duplicates = {value: files for value, files in seen.items() if len(files) > 1}
if duplicates:
    for value, files in duplicates.items():
        print(f"Repeated paragraph in {', '.join(files)}: {value}", file=sys.stderr)
    raise SystemExit(1)
PY

printf 'Editorial audit passed.\n'
