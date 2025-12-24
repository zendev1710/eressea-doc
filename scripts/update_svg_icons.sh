#!/bin/bash

TARGET_DIR="docs/assets/icons"
TEMP_DIR="tmp_icons_update"

# Liste des icônes (noms Game-Icons)
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

# Si tu as renommé les icônes en FR, mappe ici :
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

echo "🔄 Mise à jour des icônes Game-Icons…"
mkdir -p "$TARGET_DIR"
rm -rf "$TEMP_DIR"
mkdir "$TEMP_DIR"

for icon in "${icons[@]}"; do
  url="https://raw.githubusercontent.com/game-icons/icons/master/svg/delapouite/${icon}.svg"
  temp_file="$TEMP_DIR/$icon.svg"

  echo "⬇️ Téléchargement : $icon.svg"
  curl -s -L "$url" -o "$temp_file"

  # Nom final (FR ou EN selon ton choix)
  final_name="${rename_map[$icon]}"
  [ -z "$final_name" ] && final_name="$icon"
  final_path="$TARGET_DIR/$final_name.svg"

  # Si le fichier n'existe pas → copie directe
  if [ ! -f "$final_path" ]; then
    echo "➕ Nouveau fichier : $final_name.svg"
    cp "$temp_file" "$final_path"
    continue
  fi

  # Compare les fichiers
  if ! diff -q "$temp_file" "$final_path" >/dev/null; then
    echo "♻️ Mise à jour : $final_name.svg"
    cp "$temp_file" "$final_path"
  else
    echo "✔ À jour : $final_name.svg"
  fi
done

# Optimisation SVG si svgo est installé
if command -v svgo &> /dev/null; then
  echo "✨ Optimisation des SVG…"
  svgo "$TARGET_DIR"/*.svg --quiet
fi

