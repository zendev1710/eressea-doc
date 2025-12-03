#!/usr/bin/env python3
"""
Normalise les ancres (#...) dans les URLs des fichiers Markdown.

Règles appliquées:
- Pour chaque apparition de `#yyy` dans un lien (définitions ou liens inline),
  on transforme `yyy` en minuscules et on remplace les `_` par `-`.
- Parcourt tous les fichiers `*.md` du dépôt (sauf dossier `site`).
- N'écrase un fichier que s'il y a des remplacements.

Affiche un résumé des fichiers modifiés et le nombre de remplacements.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

# Pattern pour trouver une ancre #... (arrête avant espace, quote, ) ou ] )
anchor_re = re.compile(r"#([^\s\"')\]]+)")

modified = {}

for md in sorted(ROOT.rglob('*.md')):
    # Skip README? user asked all .md files; include README. Skip generated site directory.
    if 'site' in md.parts:
        continue
    text = md.read_text(encoding='utf-8')

    def repl(m):
        anchor = m.group(1)
        normalized = anchor.lower().replace('_', '-')
        if normalized != anchor:
            return '#' + normalized
        return m.group(0)

    new_text, nsub = anchor_re.subn(repl, text)
    if nsub:
        md.write_text(new_text, encoding='utf-8')
        modified[str(md.relative_to(ROOT))] = nsub

if modified:
    print('Fichiers modifiés (ancres normalisées):')
    for p, n in modified.items():
        print(f'- {p}: {n} changement(s)')
else:
    print('Aucune ancre à normaliser trouvée.')
