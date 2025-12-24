#!/bin/bash

TARGET_DIR="docs/assets/icons"

# Vérifie que svgo est installé
if ! command -v svgo &> /dev/null; then
  echo "❌ svgo n'est pas installé. Installe-le avec : npm install -g svgo"
  exit 1
fi

echo "✨ Optimisation des SVG dans $TARGET_DIR"
echo

for file in "$TARGET_DIR"/*.svg; do
  echo "Optimisation : $(basename "$file")"
  svgo "$file" --quiet
done

echo
echo "✔ Tous les SVG ont été optimisés."
