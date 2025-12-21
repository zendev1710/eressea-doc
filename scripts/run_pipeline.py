#!/usr/bin/env python3
import subprocess
import sys
import os

def run(cmd, input_file=None, output_file=None):
    if input_file:
        with open(input_file, "r", encoding="utf-8") as f:
            data = f.read()
        result = subprocess.run(cmd, input=data.encode("utf-8"), capture_output=True)
    else:
        result = subprocess.run(cmd, capture_output=True)

    if result.returncode != 0:
        print(f"❌ Error running: {' '.join(cmd)}", file=sys.stderr)
        print(result.stderr.decode(), file=sys.stderr)
        return False

    if output_file:
        with open(output_file, "wb") as f:
            f.write(result.stdout)

    return True


def pipeline(src, trg):
    src_norm = f"{src}.norm.md"
    trg_norm = f"{trg}.norm.md"
    trg_fixed = f"{trg}.fixed.md"
    src_sent = f"{src}.sentences.md"
    trg_sent = f"{trg}.sentences.md"
    aligned = f"{trg}.aligned.tsv"

    print("=== Normalisation stricte ===")
    run(["./mdnormalize_strict.py"], input_file=src, output_file=src_norm)
    run(["./mdnormalize_strict.py"], input_file=trg, output_file=trg_norm)

    print("=== Correction structurelle ===")
    run(["./mdstructdiff.py", src_norm, trg_norm, "--fix", "--output", trg_fixed, "--batch"])

    print("=== Segmentation ===")
    run(["./split_sentences.py"], input_file=src_norm, output_file=src_sent)
    run(["./split_sentences.py"], input_file=trg_fixed, output_file=trg_sent)

    print("=== Alignement avancé ===")
    run([
        "./aligner_advanced.py",
        src_sent,
        trg_sent,
        "--dict-source", "dictionaries/source.cspell.json",
        "--dict-target", "dictionaries/target.cspell.json",
        "--output", aligned
    ])

    print("=== Terminé ===")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: run_pipeline.py source.md target.md")
        sys.exit(1)

    pipeline(sys.argv[1], sys.argv[2])
