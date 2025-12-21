#!/usr/bin/env python
import subprocess
import sys
import os

def run(cmd, stdin_file=None, stdout_file=None):
    stdin_data = None
    if stdin_file:
        with open(stdin_file, "rb") as f:
            stdin_data = f.read()

    result = subprocess.run(
        cmd,
        input=stdin_data,
        capture_output=True
    )

    if result.returncode != 0:
        print("❌ Error:", " ".join(cmd))
        print(result.stderr.decode())
        return False

    if stdout_file:
        with open(stdout_file, "wb") as f:
            f.write(result.stdout)

    return True


def pipeline(src_de):
    if not src_de.endswith(".de.md"):
        print(f"Skipping non-German source file: {src_de}")
        return

    base = src_de[:-6]
    trg_en = base + ".md"
    trg_fr = base + ".fr.md"

    has_en = os.path.exists(trg_en)
    has_fr = os.path.exists(trg_fr)

    if not has_en and not has_fr:
        print(f"No target files for {src_de}")
        return

    print("=== Normalisation stricte (DE source) ===")
    run(["python", "scripts/mdnormalize_strict.py"], stdin_file=src_de, stdout_file=f"{src_de}.norm.md")

    # EN
    if has_en:
        print(f"=== Processing EN: {src_de} → {trg_en} ===")

        run(["python", "scripts/mdnormalize_strict.py"], stdin_file=trg_en, stdout_file=f"{trg_en}.norm.md")

        run(["python", "scripts/mdstructdiff.py", f"{src_de}.norm.md", f"{trg_en}.norm.md"])
        run(["python", "scripts/mdstructdiff.py", f"{src_de}.norm.md", f"{trg_en}.norm.md",
             "--fix", "--output", f"{trg_en}.fixed.md", "--batch"])

        run(["python", "scripts/split_sentences.py"], stdin_file=f"{src_de}.norm.md", stdout_file=f"{src_de}.sentences.md")
        run(["python", "scripts/split_sentences.py"], stdin_file=f"{trg_en}.fixed.md", stdout_file=f"{trg_en}.sentences.md")

        run([
            "python", "scripts/aligner_advanced.py",
            f"{src_de}.sentences.md",
            f"{trg_en}.sentences.md",
            "--dict-source", "dictionaries/de.cspell.json",
            "--dict-target", "dictionaries/en.cspell.json",
            "--output", f"{trg_en}.aligned.tsv"
        ])

    # FR
    if has_fr:
        print(f"=== Processing FR: {src_de} → {trg_fr} ===")

        run(["python", "scripts/mdnormalize_strict.py"], stdin_file=trg_fr, stdout_file=f"{trg_fr}.norm.md")

        if has_en:
            source_for_fr = f"{trg_en}.fixed.md"
            dict_source = "dictionaries/en.cspell.json"
            print("FR aligned against EN")
        else:
            source_for_fr = f"{src_de}.norm.md"
            dict_source = "dictionaries/de.cspell.json"
            print("FR aligned against DE")

        run(["python", "scripts/mdstructdiff.py", source_for_fr, f"{trg_fr}.norm.md"])
        run(["python", "scripts/mdstructdiff.py", source_for_fr, f"{trg_fr}.norm.md",
             "--fix", "--output", f"{trg_fr}.fixed.md", "--batch"])

        run(["python", "scripts/split_sentences.py"], stdin_file=source_for_fr, stdout_file=f"{source_for_fr}.sentences.md")
        run(["python", "scripts/split_sentences.py"], stdin_file=f"{trg_fr}.fixed.md", stdout_file=f"{trg_fr}.sentences.md")

        run([
            "python", "scripts/aligner_advanced.py",
            f"{source_for_fr}.sentences.md",
            f"{trg_fr}.sentences.md",
            "--dict-source", dict_source,
            "--dict-target", "dictionaries/fr.cspell.json",
            "--output", f"{trg_fr}.aligned.tsv"
        ])

    print(f"=== Done for {src_de} ===")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: run_pipeline.py path/to/file.de.md")
        sys.exit(1)

    pipeline(sys.argv[1])
