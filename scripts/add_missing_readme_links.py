#!/usr/bin/env python3
"""
Parcourt README.md, identifie les entrées de la première et dernière colonne des tables,
et ajoute/met à jour les liens en fin de fichier.

Format:
- Première colonne: [label]: ./label.md "label"
- Dernière colonne: [label]: https://wiki.eressea.de/label "label"
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'

if not README.exists():
    print('README.md introuvable')
    raise SystemExit(1)

text = README.read_text(encoding='utf-8')
lines = text.splitlines(keepends=True)

# Separator line detection
sep_re = re.compile(r"^\s*\|(?:\s*:?-+:?\s*\|)+\s*$")

first_col_labels = set()
last_col_labels = set()

# Parse tables to extract first and last column labels
i = 0
while i < len(lines) - 1:
    line = lines[i]
    next_line = lines[i+1]
    if '|' in line and sep_re.match(next_line):
        # header + separator found
        i += 2
        while i < len(lines) and '|' in lines[i]:
            row = lines[i]
            if sep_re.match(row):
                i += 1
                continue
            parts = row.rstrip('\n').split('|')
            
            # first non-empty cell (first column)
            if parts:
                for p in parts:
                    s = p.strip()
                    if s and set(s) != set('-'):
                        # extract label if bracketed
                        if s.startswith('[') and s.endswith(']'):
                            s = s[1:-1]
                        # avoid complex labels
                        if '|' not in s and '[' not in s and ']' not in s:
                            first_col_labels.add(s)
                        break
            
            # last non-empty cell (last column)
            if parts:
                for p in reversed(parts):
                    s = p.strip()
                    if s and set(s) != set('-'):
                        # extract label if bracketed
                        if s.startswith('[') and s.endswith(']'):
                            s = s[1:-1]
                        # avoid complex labels
                        if '|' not in s and '[' not in s and ']' not in s:
                            last_col_labels.add(s)
                        break
            i += 1
        continue
    i += 1

if not first_col_labels and not last_col_labels:
    print('Aucune étiquette trouvée')
    raise SystemExit(0)

print(f'Étiquettes première colonne: {len(first_col_labels)}')
print(f'Étiquettes dernière colonne: {len(last_col_labels)}')

# Extract existing link definitions
existing_defs = {}
for match in re.finditer(r"^\s*\[([^\]]+)\]:\s*(.+?)\s+\"", text, flags=re.M):
    label, url = match.groups()
    existing_defs[label] = url.strip()

# Build new definitions
new_defs = {}

# First column: ./label.md
for label in first_col_labels:
    if label not in existing_defs:
        new_defs[label] = f'./{label}.md'
        print(f'  [AJOUTER] [{label}]: ./{label}.md')
    # else: déjà existant, ne pas modifier

# Last column: https://wiki.eressea.de/label (créer ou remplacer)
for label in last_col_labels:
    url = f'https://wiki.eressea.de/{label}'
    if label not in existing_defs or existing_defs[label] != url:
        if label in existing_defs:
            print(f'  [REMPLACER] [{label}]: {existing_defs[label]} → {url}')
        else:
            print(f'  [AJOUTER] [{label}]: {url}')
        new_defs[label] = url

if not new_defs:
    print('Aucun nouveau lien à ajouter.')
    raise SystemExit(0)

# Update file: remove old defs for labels we're updating, then add all
new_lines = list(lines)

# Remove old definitions for labels we're updating
filtered_lines = []
for ln in new_lines:
    # check if this line defines a label we're updating
    m = re.match(r"^\s*\[([^\]]+)\]:", ln)
    if m:
        label = m.group(1)
        if label in new_defs:
            # skip this line (we'll re-add it)
            continue
    filtered_lines.append(ln)

new_lines = filtered_lines

# Ensure blank line before definitions
if new_lines and not new_lines[-1].endswith('\n'):
    new_lines[-1] = new_lines[-1] + '\n'
if new_lines and new_lines[-1].strip():
    new_lines.append('\n')

# Add new definitions
for label in sorted(new_defs.keys()):
    url = new_defs[label]
    new_lines.append(f'[{label}]: {url} "{label}"\n')

# Write back
README.write_text(''.join(new_lines), encoding='utf-8')
print(f'\n✓ {len(new_defs)} lien(s) ajouté(s)/modifié(s) dans README.md')
