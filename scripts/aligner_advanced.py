#!/usr/bin/env python3
import sys
import argparse
import difflib
import json
import re
from pathlib import Path

def detect_language(text):
    t = text.lower()

    fr_markers = ["é", "è", "ê", "à", "ç", "le ", "la ", "les ", "des ", "une ", "un ", "que ", "qui "]
    en_markers = ["the ", "and ", "with ", "from ", "this ", "that ", "ing ", "ed "]
    de_markers = ["der ", "die ", "das ", "und ", "nicht ", "für ", "mit ", "ä", "ö", "ü", "ß"]

    score_fr = sum(m in t for m in fr_markers)
    score_en = sum(m in t for m in en_markers)
    score_de = sum(m in t for m in de_markers)

    if score_fr > max(score_en, score_de):
        return "FR"
    if score_en > max(score_fr, score_de):
        return "EN"
    if score_de > max(score_fr, score_en):
        return "DE"

    return "UNKNOWN"

def extract_yaml_front_matter(lines):
    if not lines or not lines[0].strip() == "---":
        return [], lines

    yaml = []
    content = []
    in_yaml = True

    for i, line in enumerate(lines):
        yaml.append(line)
        if i > 0 and line.strip() == "---":
            content = lines[i+1:]
            break

    return yaml, content

def is_heading(line):
    return line.lstrip().startswith("#")

def is_list_item(line):
    stripped = line.lstrip()
    return (
        stripped.startswith("- ")
        or stripped.startswith("* ")
        or stripped.startswith("+ ")
        or re.match(r"^\s*\d+\.\s+", stripped)
    )

def is_blockquote(line):
    return line.lstrip().startswith(">")

def is_table_row(line):
    return "|" in line and line.strip().startswith("|")

def is_code_fence(line):
    return line.strip().startswith("```")

def similarity(a, b, dict_source=None, dict_target=None):
    """
    Similarité + bonus dictionnaires.
    """
    base = difflib.SequenceMatcher(None, a, b).ratio()

    if dict_source is None or dict_target is None:
        return base

    bonus = 0.0

    # Bonus si mots connus dans source
    for w in a.lower().split():
        if w in dict_source:
            bonus += 0.02

    # Bonus si mots connus dans target
    for w in b.lower().split():
        if w in dict_target:
            bonus += 0.02

    return min(1.0, base + bonus)


def align_segments(src, trg, threshold=0.45, dict_source=None, dict_target=None):
    """
    Aligne les segments src et trg.
    Retourne une liste de tuples (status, src_line, trg_line).
    status ∈ {"OK", "MISSING", "EXTRA"}
    """
    result = []
    i = 0
    j = 0

    while i < len(src) or j < len(trg):

        if i >= len(src):
            result.append(("EXTRA", None, trg[j]))
            j += 1
            continue

        if j >= len(trg):
            result.append(("MISSING", src[i], None))
            i += 1
            continue

        s = src[i]
        t = trg[j]

        # --- CALCUL DU FLAG (patch 2) ---
        lang_src = detect_language(s)
        lang_trg = detect_language(t)

        if similarity(s, t, dict_source, dict_target) > 0.95:
            flag = "NOT_TRANSLATED"
        elif lang_trg == "FR":
            flag = "TRANSLATED_IN_FR"
        elif lang_trg == "EN":
            flag = "TRANSLATED_IN_EN"
        else:
            flag = "UNKNOWN"
        # --------------------------------

        # lignes structurelles → alignement direct
        if (
            is_heading(s) or is_list_item(s) or is_blockquote(s)
            or is_table_row(s) or is_code_fence(s)
        ):
            result.append(("OK", s, t, flag))
            i += 1
            j += 1
            continue

        # lignes vides
        if s.strip() == "" and t.strip() == "":
            result.append(("OK", "", "", flag))
            i += 1
            j += 1
            continue

        # similarité directe
        if similarity(s, t, dict_source, dict_target) >= threshold:
            result.append(("OK", s, t, flag))
            i += 1
            j += 1
            continue

        # sinon → chercher la meilleure correspondance dans une fenêtre
        best_j = None
        best_score = 0

        for k in range(j+1, min(j+5, len(trg))):
            score = similarity(s, trg[k], dict_source, dict_target)
            if score > best_score:
                best_score = score
                best_j = k

        if best_score >= threshold:
            # EXTRA entre j et best_j
            for x in range(j, best_j):
                result.append(("EXTRA", None, trg[x], "NONE"))
            result.append(("OK", s, trg[best_j], flag))
            i += 1
            j = best_j + 1
            continue

        # sinon → MISSING
        result.append(("MISSING", s, None, "NONE"))
        i += 1

    return result

def load_dictionary(path):
    """
    Charge un dictionnaire TXT cSpell-like :
    - ignore les lignes vides
    - ignore les commentaires (# ...)
    - retourne un set de mots en minuscules
    """
    words = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if not w:
                continue
            if w.startswith("#"):
                continue
            words.add(w.lower())
    return words


def format_alignment(alignment):
    out = []
    for status, s, t, flag in alignment:

        if status == "OK":
            out.append(f"SRC\t{s}")
            out.append(f"TRG\t{t}")
            out.append(f"STATUS\t{status}")
            out.append(f"FLAG\t{flag}")
            out.append("")

        elif status == "MISSING":
            out.append(f"SRC\t{s}")
            out.append(f"TRG\t")
            out.append(f"STATUS\t{status}")
            out.append(f"FLAG\tNONE")
            out.append("")

        elif status == "EXTRA":
            out.append(f"SRC\t")
            out.append(f"TRG\t{t}")
            out.append(f"STATUS\t{status}")
            out.append(f"FLAG\tNONE")
            out.append("")

    return out



def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("target")
    parser.add_argument("--output", default=None)
    parser.add_argument("--dict-source", default=None)
    parser.add_argument("--dict-target", default=None)
    args = parser.parse_args()

    # Charger dictionnaires
    # Charger dictionnaires TXT
    if args.dict_source:
        dict_source = load_dictionary(args.dict_source)
    else:
        dict_source = set()

    if args.dict_target:
        dict_target = load_dictionary(args.dict_target)
    else:
        dict_target = set()


    # lire fichiers
    with open(args.source, "r", encoding="utf-8") as f:
        src_raw = [line.rstrip("\n") for line in f]

    with open(args.target, "r", encoding="utf-8") as f:
        trg_raw = [line.rstrip("\n") for line in f]

    # extraire YAML
    src_yaml, src_content = extract_yaml_front_matter(src_raw)
    trg_yaml, trg_content = extract_yaml_front_matter(trg_raw)

    # aligner
    alignment = align_segments(
        src_content,
        trg_content,
        dict_source=dict_source,
        dict_target=dict_target
    )

    # formatter
    aligned = format_alignment(alignment)

    # réinsérer YAML
    final = trg_yaml + aligned

    # écrire
    with open(args.output, "w", encoding="utf-8") as f:
        for line in final:
            f.write(line + "\n")

if __name__ == "__main__":
    main()
