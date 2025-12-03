#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'

if not README.exists():
    print('README.md introuvable')
    raise SystemExit(1)

text = README.read_text(encoding='utf-8')
lines = text.splitlines()

# Separator line detection similar to previous script
sep_re = re.compile(r"^\s*\|(?:\s*:?-+:?\s*\|)+\s*$")

mapping = {}  # last_label_lower -> first_name (without extension)

i = 0
while i < len(lines) - 1:
    line = lines[i]
    next_line = lines[i+1]
    if '|' in line and sep_re.match(next_line):
        # header + separator
        i += 2
        while i < len(lines) and '|' in lines[i]:
            row = lines[i]
            if sep_re.match(row):
                i += 1
                continue
            parts = row.rstrip('\n').split('|')
            # get first non-empty cell
            first_label = None
            last_label = None
            for p in parts:
                s = p.strip()
                if s and set(s) != set('-'):
                    first_label = s
                    break
            # get last non-empty cell from right
            for p in reversed(parts):
                s = p.strip()
                if s and set(s) != set('-'):
                    last_label = s
                    break
            # normalize bracketed labels
            def extract_label(s):
                if not s:
                    return None
                s = s.strip()
                if s.startswith('[') and s.endswith(']'):
                    return s[1:-1]
                return s
            f = extract_label(first_label)
            l = extract_label(last_label)
            if f and l:
                mapping[l.lower()] = f  # map last -> first name
            i += 1
        continue
    i += 1

if not mapping:
    print('Aucune correspondance trouvée dans README.md')
    raise SystemExit(0)
else:
    print(f'Correspondances trouvées: {len(mapping)}')

# Prepare regex for matching definition lines starting with '/'
def_re = re.compile(r"^(\s*)\[([^\]]+)\]:\s*/([^ \t#\"]+)(.*)$")

modified_files = {}

# iterate all .md files except README.md
for md in sorted(ROOT.rglob('*.md')):
    if md.resolve() == README.resolve():
        continue
    # skip files in .git or site directories optionally
    if 'site' in md.parts:
        continue
    orig = md.read_text(encoding='utf-8')
    out_lines = []
    changed = []
    for ln in orig.splitlines():
        m = def_re.match(ln)
        if m:
            indent, label, slash_label, rest = m.groups()
            key = label.strip().lower()
            key2 = slash_label.strip().lower()
            use = None
            if key in mapping:
                use = mapping[key]
            elif key2 in mapping:
                use = mapping[key2]
            if use:
                new_url = f'./{use}.md'
                new_line = f'{indent}[{label}]: {new_url}{rest}'
                out_lines.append(new_line)
                changed.append((ln, new_line))
                continue
        out_lines.append(ln)
    if changed:
        md.write_text('\n'.join(out_lines) + '\n', encoding='utf-8')
        modified_files[str(md.relative_to(ROOT))] = changed

if modified_files:
    print('Fichiers modifiés:')
    for p, changes in modified_files.items():
        print(f'- {p}: {len(changes)} modification(s)')
else:
    print('Aucune modification apportée aux fichiers .md')
