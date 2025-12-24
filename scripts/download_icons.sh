#!/bin/bash

# Dossier cible
TARGET_DIR="docs/assets/icons"
mkdir -p "$TARGET_DIR"

# Liste des icônes à télécharger
icons=(
  "alchemy"
  "crossbow"
  "muscle-up"
  "mining"
  "bowman"
  "bricks"
  "trade"
  "crossed-swords"
  "forest"
  "catapult"
  "herbs"
  "magic-swirl"
  "beast-call"
  "horse-head"
  "breastplate"
  "ship-wheel"
  "sailboat"
  "spy"
  "halberd"
  "stone-block"
  "receive-money"
  "road"
  "battle-plan"
  "hood"
  "drama-masks"
  "anvil"
  "punch"
  "cart"
  "awareness"
)

# Téléchargement
for icon in "${icons[@]}"; do
  url="https://raw.githubusercontent.com/game-icons/icons/master/src/icons/delapouite/${icon}.svg"
  echo "Téléchargement : $icon.svg"
  curl -s -L "$url" -o "$TARGET_DIR/${icon}.svg"
done

echo "✔ Tous les fichiers SVG ont été téléchargés dans $TARGET_DIR"
