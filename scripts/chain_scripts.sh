#!/bin/bash

SRC="$1"
TRG="$2"

echo "Normalisation stricte..."
cat "$SRC" | ./mdnormalize_strict.py > "${SRC}.norm.md"
cat "$TRG" | ./mdnormalize_strict.py > "${TRG}.norm.md"

echo "Comparaison structurelle..."
./mdstructdiff.py "${SRC}.norm.md" "${TRG}.norm.md"

echo "Correction automatique..."
./mdstructdiff.py "${SRC}.norm.md" "${TRG}.norm.md" --fix --output "${TRG}.fixed.md"

echo "Segmentation en phrases..."
cat "${TRG}.fixed.md" | ./split_sentences.py > "${TRG}.sentences.md"

echo "Terminé."
