#!/usr/bin/env python3
import sys
import argparse
import difflib
import json
import re
import math

def load_sentences(path):
    with open(path, "r", encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]

def split_sentences_auto(text):
    out = []
    buf = ""
    i = 0
    while i < len(text):
        if text.startswith("...", i):
            buf += "..."
            i += 3
            continue
        ch = text[i]
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
        return split_sentences_auto(f.read())

# -------------------------
# Heuristics
# -------------------------

def score_length(a, b):
    la, lb = len(a), len(b)
    if la == 0 or lb == 0:
        return 0
    return 1 - abs(la - lb) / max(la, lb)

def score_numbers(a, b):
    nums_a = re.findall(r"\d+", a)
    nums_b = re.findall(r"\d+", b)
    if not nums_a and not nums_b:
        return 0.5
    return len(set(nums_a) & set(nums_b)) / max(len(nums_a), len(nums_b), 1)

def score_proper_nouns(a, b):
    # naive: capitalized words
    pa = set(re.findall(r"\b[A-Z][a-z]+\b", a))
    pb = set(re.findall(r"\b[A-Z][a-z]+\b", b))
    if not pa and not pb:
        return 0.5
    return len(pa & pb) / max(len(pa), len(pb), 1)

def score_lexical(a, b):
    # very light lexical similarity
    wa = set(re.findall(r"[a-zA-Z]{4,}", a.lower()))
    wb = set(re.findall(r"[a-zA-Z]{4,}", b.lower()))
    if not wa and not wb:
        return 0.5
    return len(wa & wb) / max(len(wa), len(wb), 1)

def score_difflib(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()

def global_score(a, b):
    return (
        0.30 * score_difflib(a, b) +
        0.20 * score_length(a, b) +
        0.20 * score_numbers(a, b) +
        0.15 * score_proper_nouns(a, b) +
        0.15 * score_lexical(a, b)
    )

# -------------------------
# Alignment
# -------------------------

def align_advanced(fr, en):
    pairs = []
    i = j = 0

    while i < len(fr) and j < len(en):
        s = global_score(fr[i], en[j])

        # Try fusion FR: fr[i] + fr[i+1]
        if i + 1 < len(fr):
            s2 = global_score(fr[i] + " " + fr[i+1], en[j])
        else:
            s2 = -1

        # Try fusion EN: en[j] + en[j+1]
        if j + 1 < len(en):
            s3 = global_score(fr[i], en[j] + " " + en[j+1])
        else:
            s3 = -1

        best = max(s, s2, s3)

        if best == s:
            pairs.append((fr[i], en[j]))
            i += 1
            j += 1
        elif best == s2:
            pairs.append((fr[i] + " " + fr[i+1], en[j]))
            i += 2
            j += 1
        else:
            pairs.append((fr[i], en[j] + " " + en[j+1]))
            i += 1
            j += 2

    # leftovers
    while i < len(fr):
        pairs.append((fr[i], "<!-- MISSING -->"))
        i += 1

    while j < len(en):
        pairs.append(("<!-- EXTRA -->", en[j]))
        j += 1

    return pairs

# -------------------------
# Main
# -------------------------

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

    pairs = align_advanced(fr, en)

    if args.json:
        print(json.dumps(
            [{"fr": f, "en": e} for f, e in pairs],
            ensure_ascii=False,
            indent=2
        ))
        return

    for idx, (f, e) in enumerate(pairs, 1):
        print(f"=== PAIR {idx} ===")
        print(f"FR: {f}")
        print(f"EN: {e}")
        print()

if __name__ == "__main__":
    main()
