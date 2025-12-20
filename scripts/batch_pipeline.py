#!/usr/bin/env python3
import argparse
import subprocess
from pathlib import Path

PIPELINE_SCRIPT = "./translate_pipeline.sh"

def find_pairs(src_dir: Path, tgt_dir: Path):
    pairs = []
    for src_file in src_dir.rglob("*.md"):
        rel = src_file.relative_to(src_dir)
        tgt_file = tgt_dir / rel
        if tgt_file.exists():
            pairs.append((src_file, tgt_file))
    return pairs

def main():
    parser = argparse.ArgumentParser(description="Pipeline multi-fichiers pour un dossier Markdown.")
    parser.add_argument("src_dir", help="Dossier source (ex: docs/de)")
    parser.add_argument("tgt_dir", help="Dossier cible (ex: docs/fr)")
    parser.add_argument("src_lang", choices=["de", "fr", "en"])
    parser.add_argument("tgt_lang", choices=["de", "fr", "en"])
    args = parser.parse_args()

    src_dir = Path(args.src_dir).resolve()
    tgt_dir = Path(args.tgt_dir).resolve()

    pairs = find_pairs(src_dir, tgt_dir)

    if not pairs:
        print("Aucune paire de fichiers trouvée.")
        return

    print(f"{len(pairs)} paires trouvées.")

    for src, tgt in pairs:
        print(f"\n=== Traitement ===\nSRC: {src}\nTGT: {tgt}")
        cmd = [PIPELINE_SCRIPT, str(src), str(tgt), args.src_lang, args.tgt_lang]
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"⚠️ Pipeline échoué pour {src} / {tgt} (code {result.returncode})")

if __name__ == "__main__":
    main()
