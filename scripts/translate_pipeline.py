#!/bin/bash

set -e

# -----------------------------
# CONFIGURATION
# -----------------------------
SRC="$1"
TGT="$2"
SRC_LANG="$3"   # de | fr | en
TGT_LANG="$4"   # de | fr | en

DICT_DE="custom-dictionary-de.txt"
DICT_FR="custom-dictionary-fr.txt"
DICT_EN="custom-dictionary-en.txt"

# Choix de l'aligneur : simple ou avancé
ALIGNER="advanced"   # "simple" ou "advanced"

# -----------------------------
# Vérification des arguments
# -----------------------------
if [ -z "$SRC" ] || [ -z "$TGT" ] || [ -z "$SRC_LANG" ] || [ -z "$TGT_LANG" ]; then
    echo "Usage: $0 source.md target.md src_lang tgt_lang"
    echo "Exemple: $0 original.md traduction.md de fr"
    exit 1
fi

# -----------------------------
# Étape 1 : Normalisation stricte
# -----------------------------
echo "🔧 Normalisation stricte..."
cat "$SRC" | ./mdnormalize_strict.py > "${SRC}.norm.md"
cat "$TGT" | ./mdnormalize_strict.py > "${TGT}.norm.md"

# -----------------------------
# Étape 2 : Diff structurel
# -----------------------------
echo "🔍 Comparaison structurelle..."
./mdstructdiff.py "${SRC}.norm.md" "${TGT}.norm.md"

# -----------------------------
# Étape 3 : Correction automatique
# -----------------------------
echo "🛠️ Correction automatique..."
./mdstructdiff.py "${SRC}.norm.md" "${TGT}.norm.md" --fix --output "${TGT}.fixed.md"

# -----------------------------
# Étape 4 : Normalisation tolérante
# -----------------------------
echo "🌿 Normalisation tolérante..."
cat "${TGT}.fixed.md" | ./mdnormalize_tolerant.py > "${TGT}.clean.md"

# -----------------------------
# Étape 5 : Segmentation
# -----------------------------
echo "✂️ Segmentation en phrases..."
cat "${SRC}.norm.md" | ./split_sentences.py > "${SRC}.sentences.md"
cat "${TGT}.clean.md" | ./split_sentences.py > "${TGT}.sentences.md"

# -----------------------------
# Étape 6 : Alignement
# -----------------------------
echo "🤝 Alignement phrase par phrase..."

if [ "$ALIGNER" = "simple" ]; then
    ./aligner_simple.py --sentences "${SRC}.sentences.md" "${TGT}.sentences.md" > alignment.txt
else
    ./aligner_advanced.py \
        --sentences \
        --src-lang "$SRC_LANG" \
        --tgt-lang "$TGT_LANG" \
        --dict-de "$DICT_DE" \
        --dict-fr "$DICT_FR" \
        --dict-en "$DICT_EN" \
        "${SRC}.sentences.md" "${TGT}.sentences.md" > alignment.txt
fi

echo "🎉 Alignement terminé → alignment.txt"
