$targetDir = "docs/assets/icons"
$tempDir = "tmp_icons_update"

# Liste des icônes Game-Icons
$icons = @(
  "alchemy","crossbow","muscle-up","mining","bowman","bricks","trade",
  "crossed-swords","forest","catapult","herbs","magic-swirl","beast-call",
  "horse-head","breastplate","ship-wheel","sailboat","spy","halberd",
  "stone-block","receive-money","road","battle-plan","hood","drama-masks",
  "anvil","punch","cart","awareness"
)

# Renommage FR
$renameMap = @{
  "alchemy"="alchimie"
  "crossbow"="arbalete"
  "muscle-up"="endurance"
  "mining"="minage"
  "bowman"="tir-arc"
  "bricks"="maconnerie"
  "trade"="commerce"
  "crossed-swords"="melee"
  "forest"="sylviculture"
  "catapult"="catapulte"
  "herbs"="herboristerie"
  "magic-swirl"="magie"
  "beast-call"="dressage"
  "horse-head"="equitation"
  "breastplate"="forge-armures"
  "ship-wheel"="construction-navale"
  "sailboat"="navigation"
  "spy"="espionnage"
  "halberd"="arme-hast"
  "stone-block"="extraction-pierre"
  "receive-money"="taxation"
  "road"="travaux-routiers"
  "battle-plan"="tactiques"
  "hood"="furtivite"
  "drama-masks"="divertissement"
  "anvil"="forge-armes"
  "punch"="combat-mains-nues"
  "cart"="charroi"
  "awareness"="perception"
}

Write-Host "🔄 Mise à jour des icônes Game-Icons…"

New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
Remove-Item -Recurse -Force $tempDir -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force -Path $tempDir | Out-Null

foreach ($icon in $icons) {
    $url = "https://raw.githubusercontent.com/game-icons/icons/master/svg/delapouite/$icon.svg"
    $tempFile = "$tempDir\$icon.svg"

    Write-Host "⬇️ Téléchargement : $icon.svg"
    Invoke-WebRequest -Uri $url -OutFile $tempFile -UseBasicParsing

    $finalName = $renameMap[$icon]
    if (-not $finalName) { $finalName = $icon }
    $finalPath = "$targetDir\$finalName.svg"

    if (-not (Test-Path $finalPath)) {
        Write-Host "➕ Nouveau fichier : $finalName.svg"
        Copy-Item $tempFile $finalPath
        continue
    }

    if (-not (Compare-Object (Get-Content $tempFile) (Get-Content $finalPath))) {
        Write-Host "✔ À jour : $finalName.svg"
    } else {
        Write-Host "♻️ Mise à jour : $finalName.svg"
        Copy-Item $tempFile $finalPath -Force
    }
}

# Optimisation si svgo est installé
if (Get-Command svgo -ErrorAction SilentlyContinue) {
    Write-Host "✨ Optimisation des SVG…"
    Get-ChildItem "$targetDir\*.svg" | ForEach-Object {
        svgo $_.FullName --quiet
    }
}

Write-Host "🎉 Mise à jour terminée !"
