#!/usr/bin/env python3
import sys
import argparse
import difflib
import json
import re

# -------------------------
# Chargement des phrases
# -------------------------

def load_sentences_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]

def split_sentences_auto(text: str):
    """
    Segmentation simple, cohérente avec split_sentences.py :
    - coupe sur . ; !
    - ne coupe pas sur ...
    """
    out = []
    buf = []
    i = 0
    n = len(text)

    while i < n:
        if text.startswith("...", i):
            buf.append("...")
            i += 3
            continue

        ch = text[i]
        if ch in ".;!":
            buf.append(ch)
            sentence = "".join(buf).strip()
            if sentence:
                out.append(sentence)
            buf = []
            i += 1
            continue

        buf.append(ch)
        i += 1

    tail = "".join(buf).strip()
    if tail:
        out.append(tail)

    return out

def load_raw(path: str):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return split_sentences_auto(text)


# -------------------------
# Alignement simple
# -------------------------

def align_simple(fr_sentences, en_sentences):
    """
    Alignement basé sur difflib.SequenceMatcher.
    Gère :
    - égalités
    - remplacements (fusion/scission simple)
    - suppressions
    - insertions
    """
    sm = difflib.SequenceMatcher(a=fr_sentences, b=en_sentences)
    pairs = []

    for tag, i1, i2, j1, j2 in sm.get_opcodes():

        if tag == "equal":
            for k in range(i2 - i1):
                pairs.append((fr_sentences[i1 + k], en_sentences[j1 + k]))

        elif tag == "replace":
            fr_block = " ".join(fr_sentences[i1:i2])
            en_block = " ".join(en_sentences[j1:j2])
            pairs.append((fr_block, en_block))

        elif tag == "delete":
            for k in range(i1, i2):
                pairs.append((fr_sentences[k], "<!-- MISSING -->"))

        elif tag == "insert":
            for k in range(j1, j2):
                pairs.append(("<!-- EXTRA -->", en_sentences[k]))

    return pairs


# -------------------------
# Main
# -------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Alignement simple phrase par phrase (difflib)."
    )
    parser.add_argument("source", help="Fichier source (texte ou phrases)")
    parser.add_argument("target", help="Fichier cible (texte ou phrases)")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--raw", action="store_true", help="Entrées brutes (Markdown/texte) à segmenter")
    mode.add_argument("--sentences", action="store_true", help="Entrées déjà segmentées (1 phrase par ligne)")
    parser.add_argument("--json", action="store_true", help="Sortie JSON")

    args = parser.parse_args()

    # Chargement phrases
    if args.raw:
        src_sentences = load_raw(args.source)
        tgt_sentences = load_raw(args.target)
    else:
        src_sentences = load_sentences_file(args.source)
        tgt_sentences = load_sentences_file(args.target)

    pairs = align_simple(src_sentences, tgt_sentences)

    if args.json:
        print(json.dumps(
            [{"src": s, "tgt": t} for s, t in pairs],
            ensure_ascii=False,
            indent=2,
        ))
        return

    # Sortie lisible
    for idx, (s, t) in enumerate(pairs, 1):
        print(f"=== PAIR {idx} ===")
        print(f"SRC: {s}")
        print(f"TGT: {t}")
        print()


if __name__ == "__main__":
    main()
