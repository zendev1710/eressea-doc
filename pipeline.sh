#!/bin/bash
set -e

SRC_DE="$1"

if [[ "$SRC_DE" != *.de.md ]]; then
    echo "Skipping non-German source file: $SRC_DE"
    exit 0
fi

BASE="${SRC_DE%.de.md}"

TRG_EN="${BASE}.md"
TRG_FR="${BASE}.fr.md"

HAS_EN=false
HAS_FR=false

GEN_DIR="generated"

mkdir -p "$GEN_DIR"
mkdir -p "$GEN_DIR/$(dirname "$SRC_DE")"

[ -f "$TRG_EN" ] && HAS_EN=true
[ -f "$TRG_FR" ] && HAS_FR=true

if ! $HAS_EN && ! $HAS_FR; then
    echo "No target files (EN/FR) for German source: $SRC_DE"
    exit 0
fi

echo "=== Normalisation stricte (DE source) ==="

SRC_DE_NORM="$GEN_DIR/${SRC_DE%.md}.norm.md"
SRC_DE_SENT="$GEN_DIR/${SRC_DE%.md}.sentences.md"

python ./scripts/mdnormalize_strict.py < "$SRC_DE" > "$SRC_DE_NORM"

########################################
# TRAITEMENT EN (DE → EN)
########################################
if $HAS_EN; then
    echo "=== Processing EN: $SRC_DE → $TRG_EN ==="

    mkdir -p "$GEN_DIR/$(dirname "$TRG_EN")"

    TRG_EN_NORM="$GEN_DIR/${TRG_EN%.md}.norm.md"
    TRG_EN_SENT="${TRG_EN%.md}.sentences.md"
    TRG_EN_ALIGNED="$GEN_DIR/${TRG_EN%.md}.aligned.tsv"
    TRG_EN_FIXED="$GEN_DIR/${TRG_EN%.md}.fixed.md"

    python ./scripts/mdnormalize_strict.py < "$TRG_EN" > "$TRG_EN_NORM"

    # 1) Split sentences AVANT mdstructdiff
    python ./scripts/split_sentences.py < "$SRC_DE_NORM" > "$SRC_DE_SENT"
    python ./scripts/split_sentences.py < "$TRG_EN_NORM" > "$TRG_EN_SENT"

    # 2) Alignement AVANT mdstructdiff
    python ./scripts/aligner_advanced.py \
        "$SRC_DE_SENT" \
        "$TRG_EN_SENT" \
        --dict-source .cspell/custom-dictionary-de.txt \
        --dict-target .cspell/custom-dictionary-en.txt \
        --output "$TRG_EN_ALIGNED"

    # 3) mdstructdiff lit le .aligned.tsv
    python ./scripts/mdstructdiff.py "$SRC_DE_NORM" "$TRG_EN_NORM" \
        --fix --aligned "$TRG_EN_ALIGNED" --output "$TRG_EN_FIXED"
fi


########################################
# TRAITEMENT FR (DE → FR ou EN → FR)
########################################
if $HAS_FR; then
    echo "=== Processing FR: $SRC_DE → $TRG_FR ==="

    mkdir -p "$GEN_DIR/$(dirname "$TRG_FR")"

    TRG_FR_NORM="$GEN_DIR/${TRG_FR%.md}.norm.md"
    TRG_FR_FIXED="$GEN_DIR/${TRG_FR%.md}.fixed.md"
    TRG_FR_SENT="$GEN_DIR/${TRG_FR%.md}.sentences.md"
    TRG_FR_ALIGNED="$GEN_DIR/${TRG_FR%.md}.aligned.tsv"

    python ./scripts/mdnormalize_strict.py < "$TRG_FR" > "$TRG_FR_NORM"

    if $HAS_EN; then
        SOURCE_FOR_FR="$TRG_EN_NORM"   # ⚠️ important : on aligne sur le NORM, pas le FIXED
        SOURCE_FOR_FR_SENT="${TRG_EN%.md}.norm.sentences.md"
        DICT_SOURCE=".cspell/custom-dictionary-en.txt"
        echo "FR will be aligned against EN (not DE)"
    else
        SOURCE_FOR_FR="$SRC_DE_NORM"
        SOURCE_FOR_FR_SENT="${SRC_DE%.md}.sentences.md"
        DICT_SOURCE=".cspell/custom-dictionary-de.txt"
        echo "FR will be aligned against DE"
    fi

    # 1) Split sentences AVANT mdstructdiff
    python ./scripts/split_sentences.py < "$SOURCE_FOR_FR" > "$SOURCE_FOR_FR_SENT"
    python ./scripts/split_sentences.py < "$TRG_FR_NORM" > "$TRG_FR_SENT"

    # 2) Alignement AVANT mdstructdiff
    python ./scripts/aligner_advanced.py \
        "$SOURCE_FOR_FR_SENT" \
        "$TRG_FR_SENT" \
        --dict-source "$DICT_SOURCE" \
        --dict-target .cspell/custom-dictionary-fr.txt \
        --output "$TRG_FR_ALIGNED"

    # 3) mdstructdiff lit le .aligned.tsv
    python ./scripts/mdstructdiff.py "$SOURCE_FOR_FR" "$TRG_FR_NORM" \
        --fix --aligned "$TRG_FR_ALIGNED" --output "$TRG_FR_FIXED"
fi


echo "=== Done for $SRC_DE ==="
