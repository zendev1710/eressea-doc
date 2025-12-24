#!/bin/bash

TARGET_DIR="docs/assets/icons"

declare -A rename_map=(
  ["alchemy"]="alchimie"
  ["crossbow"]="arbalete"
  ["muscle-up"]="endurance"
  ["mining"]="minage"
  ["bowman"]="tir-arc"
  ["bricks"]="maconnerie"
  ["trade"]="commerce"
  ["crossed-swords"]="melee"
  ["forest"]="sylviculture"
  ["catapult"]="catapulte"
  ["herbs"]="herboristerie"
  ["magic-swirl"]="magie"
  ["beast-call"]="dressage"
  ["horse-head"]="equitation"
  ["breastplate"]="forge-armures"
  ["ship-wheel"]="construction-navale"
  ["sailboat"]="navigation"
  ["spy"]="espionnage"
  ["halberd"]="arme-hast"
  ["stone-block"]="extraction-pierre"
  ["receive-money"]="taxation"
  ["road"]="travaux-routiers"
  ["battle-plan"]="tactiques"
  ["hood"]="furtivite"
  ["drama-masks"]="divertissement"
  ["anvil"]="forge-armes"
  ["punch"]="combat-mains-nues"
  ["cart"]="charroi"
  ["awareness"]="perception"
)

for old in "${!rename_map[@]}"; do
  new="${rename_map[$old]}"
  if [ -f "$TARGET_DIR/$old.svg" ]; then
    mv "$TARGET_DIR/$old.svg" "$TARGET_DIR/$new.svg"
    echo "✔ $old.svg → $new.svg"
  else
    echo "❌ $old.svg introuvable"
  fi
done
