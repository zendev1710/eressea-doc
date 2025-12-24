$targetDir = "docs/assets/icons"
New-Item -ItemType Directory -Force -Path $targetDir | Out-Null

$icons = @(
  "alchemy",
  "crossbow",
  "muscle-up",
  "mining",
  "bowman",
  "bricks",
  "trade",
  "crossed-swords",
  "forest",
  "catapult",
  "herbs",
  "magic-swirl",
  "beast-call",
  "horse-head",
  "breastplate",
  "ship-wheel",
  "sailboat",
  "spy",
  "halberd",
  "stone-block",
  "receive-money",
  "road",
  "battle-plan",
  "hood",
  "drama-masks",
  "anvil",
  "punch",
  "cart",
  "awareness"
)

foreach ($icon in $icons) {
    $url = "https://raw.githubusercontent.com/game-icons/icons/master/svg/delapouite/$icon.svg"
    $dest = "$targetDir\$icon.svg"
    Write-Host "Téléchargement : $icon.svg"
    Invoke-WebRequest -Uri $url -OutFile $dest -UseBasicParsing
}

Write-Host "✔ Tous les fichiers SVG ont été téléchargés dans $targetDir"
