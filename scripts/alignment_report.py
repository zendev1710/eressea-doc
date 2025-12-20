#!/usr/bin/env python3
import argparse
import json
import subprocess
from html import escape
from pathlib import Path

ALIGNER_ADV = "./aligner_advanced.py"

def run_aligner_json(src, tgt, src_lang, tgt_lang, dict_de, dict_fr, dict_en):
    cmd = [
        ALIGNER_ADV,
        "--sentences",
        "--src-lang", src_lang,
        "--tgt-lang", tgt_lang,
        "--dict-de", dict_de or "",
        "--dict-fr", dict_fr or "",
        "--dict-en", dict_en or "",
        src,
        tgt,
        "--json",
    ]
    # filtre chaînes vides
    cmd = [c for c in cmd if c != ""]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Aligner failed: {result.stderr}")
    return json.loads(result.stdout)

def generate_html(pairs, title="Rapport d'alignement"):
    rows = []
    for i, item in enumerate(pairs, 1):
        src = item.get("src", "")
        tgt = item.get("tgt", "")
        cls_src = ""
        cls_tgt = ""

        if "<!-- MISSING" in tgt:
            cls_tgt = "missing"
        if "<!-- EXTRA" in src:
            cls_src = "extra"

        rows.append(f"""
<tr>
  <td class="index">{i}</td>
  <td class="{cls_src}">{escape(src)}</td>
  <td class="{cls_tgt}">{escape(tgt)}</td>
</tr>
""")

    html = f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>{escape(title)}</title>
  <style>
    body {{
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      margin: 20px;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
    }}
    th, td {{
      border: 1px solid #ddd;
      padding: 8px;
      vertical-align: top;
    }}
    th {{
      background-color: #f4f4f4;
    }}
    tr:nth-child(even) {{ background-color: #fafafa; }}
    .missing {{
      background-color: #ffe5e5;
    }}
    .extra {{
      background-color: #e5f0ff;
    }}
    .index {{
      width: 3rem;
      text-align: right;
      color: #666;
    }}
    pre {{
      margin: 0;
      white-space: pre-wrap;
    }}
  </style>
</head>
<body>
  <h1>{escape(title)}</h1>
  <table>
    <thead>
      <tr>
        <th>#</th>
        <th>Source</th>
        <th>Cible</th>
      </tr>
    </thead>
    <tbody>
      {''.join(rows)}
    </tbody>
  </table>
</body>
</html>
"""
    return html

def main():
    parser = argparse.ArgumentParser(description="Générer un rapport HTML d'alignement.")
    parser.add_argument("src_sentences", help="Fichier phrases source (1 par ligne)")
    parser.add_argument("tgt_sentences", help="Fichier phrases cible (1 par ligne)")
    parser.add_argument("--src-lang", choices=["de", "fr", "en"], required=True)
    parser.add_argument("--tgt-lang", choices=["de", "fr", "en"], required=True)
    parser.add_argument("--dict-de")
    parser.add_argument("--dict-fr")
    parser.add_argument("--dict-en")
    parser.add_argument("--output", default="alignment_report.html")
    args = parser.parse_args()

    pairs = run_aligner_json(
        args.src_sentences,
        args.tgt_sentences,
        args.src_lang,
        args.tgt_lang,
        args.dict_de,
        args.dict_fr,
        args.dict_en,
    )

    html = generate_html(pairs, title=f"Alignement {args.src_lang} → {args.tgt_lang}")
    out_path = Path(args.output)
    out_path.write_text(html, encoding="utf-8")
    print(f"Rapport HTML généré : {out_path}")

if __name__ == "__main__":
    main()
