#!/usr/bin/env python3
import sys
import argparse
import difflib
import json

def load_sentences(path):
    with open(path, "r", encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]

def split_sentences_auto(text):
    # Very simple splitter: uses your rules
    out = []
    buf = ""
    i = 0
    while i < len(text):
        ch = text[i]

        # ellipsis
        if text.startswith("...", i):
            buf += "..."
            i += 3
            continue

        if ch in ".;!":
            buf += ch
            out.append(buf.strip())
            buf = ""
            i += 1
            continue

        buf += ch
        i += 1

    if buf.strip():
        out.append(buf.strip())

    return out

def load_raw(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return split_sentences_auto(text)

def align(fr, en):
    sm = difflib.SequenceMatcher(a=fr, b=en)
    pairs = []

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                pairs.append((fr[i1+k], en[j1+k]))

        elif tag == "replace":
            # naive fusion/scission handling
            fr_block = " ".join(fr[i1:i2])
            en_block = " ".join(en[j1:j2])
            pairs.append((fr_block, en_block))

        elif tag == "delete":
            for k in range(i1, i2):
                pairs.append((fr[k], "<!-- MISSING -->"))

        elif tag == "insert":
            for k in range(j1, j2):
                pairs.append(("<!-- EXTRA -->", en[k]))

    return pairs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fr")
    parser.add_argument("en")
    parser.add_argument("--raw", action="store_true")
    parser.add_argument("--sentences", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.raw:
        fr = load_raw(args.fr)
        en = load_raw(args.en)
    else:
        fr = load_sentences(args.fr)
        en = load_sentences(args.en)

    pairs = align(fr, en)

    if args.json:
        print(json.dumps(
            [{"fr": f, "en": e} for f, e in pairs],
            ensure_ascii=False,
            indent=2
        ))
        return

    # human-readable
    for idx, (f, e) in enumerate(pairs, 1):
        print(f"=== PAIR {idx} ===")
        print(f"FR: {f}")
        print(f"EN: {e}")
        print()

if __name__ == "__main__":
    main()
