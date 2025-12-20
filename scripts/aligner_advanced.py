#!/usr/bin/env python3
import sys
import argparse
import difflib
import json
import re
from pathlib import Path

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
    - ne regarde pas le Markdown ni le code (version simplifiée)
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
# Dictionnaires cspell
# -------------------------

def load_dict(path: str):
    if not path:
        return set()
    p = Path(path)
    if not p.is_file():
        return set()
    words = set()
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if not w or w.startswith("#"):
                continue
            words.add(w)
    return words

def tokenize_words(text: str):
    # mots alphabétiques de longueur >= 2
    return re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]{2,}", text)


# -------------------------
# Heuristiques linguistiques
# -------------------------

def score_length(a: str, b: str) -> float:
    la, lb = len(a), len(b)
    if la == 0 or lb == 0:
        return 0.0
    return 1.0 - abs(la - lb) / max(la, lb)

def score_numbers(a: str, b: str) -> float:
    nums_a = re.findall(r"\d+", a)
    nums_b = re.findall(r"\d+", b)
    if not nums_a and not nums_b:
        return 0.5
    inter = set(nums_a) & set(nums_b)
    return len(inter) / max(len(nums_a), len(nums_b), 1)

def score_proper_nouns(a: str, b: str) -> float:
    pa = set(re.findall(r"\b[A-Z][a-zÀ-ÖØ-öø-ÿ]+\b", a))
    pb = set(re.findall(r"\b[A-Z][a-zÀ-ÖØ-öø-ÿ]+\b", b))
    if not pa and not pb:
        return 0.5
    inter = pa & pb
    return len(inter) / max(len(pa), len(pb), 1)

def score_difflib(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a, b).ratio()

def score_dict_overlap(a: str, b: str, dict_src: set, dict_tgt: set) -> float:
    """
    Utilise les dictionnaires cspell pour repérer les mots "stables" :
    - mots présents dans les deux dicos → très bon signe
    - si pas de mots dictionnaire → 0.5 neutre
    """
    wa = set(tokenize_words(a))
    wb = set(tokenize_words(b))

    if not wa and not wb:
        return 0.5

    # mots qui existent dans AU MOINS un des deux dicos
    wa_dict = {w for w in wa if w in dict_src or w in dict_tgt}
    wb_dict = {w for w in wb if w in dict_src or w in dict_tgt}

    if not wa_dict and not wb_dict:
        return 0.5

    inter = wa_dict & wb_dict
    return len(inter) / max(len(wa_dict), len(wb_dict), 1)


# -------------------------
# Pondération selon la paire de langues
# -------------------------

def get_weights(src_lang: str, tgt_lang: str):
    """
    Retourne les poids pour chaque sous-score selon la combinaison de langues.
    Tous les poids sont normalisés pour approximer 1.0 au total.
    """
    pair = (src_lang, tgt_lang)

    # base: difflib, length, numbers, proper, dict
    if pair in {("fr", "en"), ("en", "fr")}:
        return {
            "difflib": 0.25,
            "length": 0.15,
            "numbers": 0.20,
            "proper": 0.15,
            "dict": 0.25,
        }
    if pair in {("de", "en"), ("en", "de")}:
        return {
            "difflib": 0.15,
            "length": 0.20,
            "numbers": 0.25,
            "proper": 0.15,
            "dict": 0.25,
        }
    if pair in {("de", "fr"), ("fr", "de")}:
        return {
            "difflib": 0.15,
            "length": 0.20,
            "numbers": 0.25,
            "proper": 0.15,
            "dict": 0.25,
        }

    # fallback neutre
    return {
        "difflib": 0.2,
        "length": 0.2,
        "numbers": 0.2,
        "proper": 0.2,
        "dict": 0.2,
    }

def global_score(a: str, b: str, dict_src: set, dict_tgt: set, weights: dict) -> float:
    s_dif = score_difflib(a, b)
    s_len = score_length(a, b)
    s_num = score_numbers(a, b)
    s_prop = score_proper_nouns(a, b)
    s_dict = score_dict_overlap(a, b, dict_src, dict_tgt)

    return (
        weights["difflib"] * s_dif +
        weights["length"] * s_len +
        weights["numbers"] * s_num +
        weights["proper"] * s_prop +
        weights["dict"] * s_dict
    )


# -------------------------
# Alignement avancé
# -------------------------

def align_advanced(fr_sentences, en_sentences, dict_src, dict_tgt, weights):
    """
    fr_sentences = liste phrases source
    en_sentences = liste phrases cible

    On procède séquentiellement avec gestion de fusions simplifiées :
    - FR[i] ↔ EN[j]
    - FR[i]+FR[i+1] ↔ EN[j]
    - FR[i] ↔ EN[j]+EN[j+1]
    """
    pairs = []
    i = j = 0
    n_fr = len(fr_sentences)
    n_en = len(en_sentences)

    while i < n_fr and j < n_en:
        s1 = global_score(fr_sentences[i], en_sentences[j], dict_src, dict_tgt, weights)

        if i + 1 < n_fr:
            fr_merge = fr_sentences[i] + " " + fr_sentences[i + 1]
            s2 = global_score(fr_merge, en_sentences[j], dict_src, dict_tgt, weights)
        else:
            s2 = -1.0

        if j + 1 < n_en:
            en_merge = en_sentences[j] + " " + en_sentences[j + 1]
            s3 = global_score(fr_sentences[i], en_merge, dict_src, dict_tgt, weights)
        else:
            s3 = -1.0

        best = max(s1, s2, s3)

        # seuil basique pour éviter des alignements aberrants
        # (tu pourras ajuster si besoin)
        if best < 0.15:
            # on considère qu'il y a un décalage : phrase manquante / en trop
            # ici on choisit de marquer la source comme manquante côté cible
            pairs.append((fr_sentences[i], "<!-- MISSING OR MISALIGNED -->"))
            i += 1
            continue

        if best == s1:
            pairs.append((fr_sentences[i], en_sentences[j]))
            i += 1
            j += 1
        elif best == s2:
            pairs.append((fr_merge, en_sentences[j]))
            i += 2
            j += 1
        else:  # best == s3
            pairs.append((fr_sentences[i], en_merge))
            i += 1
            j += 2

    while i < n_fr:
        pairs.append((fr_sentences[i], "<!-- MISSING -->"))
        i += 1

    while j < n_en:
        pairs.append(("<!-- EXTRA -->", en_sentences[j]))
        j += 1

    return pairs


# -------------------------
# Main
# -------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Alignement avancé phrase par phrase avec heuristiques linguistiques et dictionnaires cspell."
    )
    parser.add_argument("source", help="Fichier source (texte ou phrases)")
    parser.add_argument("target", help="Fichier cible (texte ou phrases)")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--raw", action="store_true", help="Entrées brutes (Markdown/texte) à segmenter")
    mode.add_argument("--sentences", action="store_true", help="Entrées déjà segmentées (1 phrase par ligne)")
    parser.add_argument("--json", action="store_true", help="Sortie JSON")
    parser.add_argument("--src-lang", choices=["de", "fr", "en"], required=True,
                        help="Langue source (de, fr, en)")
    parser.add_argument("--tgt-lang", choices=["de", "fr", "en"], required=True,
                        help="Langue cible (de, fr, en)")
    parser.add_argument("--dict-de", help="Dictionnaire cspell allemand", default=None)
    parser.add_argument("--dict-fr", help="Dictionnaire cspell français", default=None)
    parser.add_argument("--dict-en", help="Dictionnaire cspell anglais", default=None)

    args = parser.parse_args()

    # Chargement phrases
    if args.raw:
        src_sentences = load_raw(args.source)
        tgt_sentences = load_raw(args.target)
    else:
        src_sentences = load_sentences_file(args.source)
        tgt_sentences = load_sentences_file(args.target)

    # Chargement dictionnaires
    dict_de = load_dict(args.dict_de)
    dict_fr = load_dict(args.dict_fr)
    dict_en = load_dict(args.dict_en)

    # Sélection des dicos en fonction des langues
    lang_to_dict = {
        "de": dict_de,
        "fr": dict_fr,
        "en": dict_en,
    }
    dict_src = lang_to_dict.get(args.src_lang, set())
    dict_tgt = lang_to_dict.get(args.tgt_lang, set())

    weights = get_weights(args.src_lang, args.tgt_lang)

    pairs = align_advanced(src_sentences, tgt_sentences, dict_src, dict_tgt, weights)

    if args.json:
        print(json.dumps(
            [{"src": s, "tgt": t} for s, t in pairs],
            ensure_ascii=False,
            indent=2,
        ))
        return

    for idx, (s, t) in enumerate(pairs, 1):
        print(f"=== PAIR {idx} ===")
        print(f"SRC: {s}")
        print(f"TGT: {t}")
        print()


if __name__ == "__main__":
    main()
