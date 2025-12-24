$targetDir = "docs/assets/icons"

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

foreach ($old in $renameMap.Keys) {
    $new = $renameMap[$old]
    $oldPath = "$targetDir\$old.svg"
    $newPath = "$targetDir\$new.svg"

    if (Test-Path $oldPath) {
        Rename-Item -Path $oldPath -NewName "$new.svg"
        Write-Host "✔ $old.svg → $new.svg"
    } else {
        Write-Host "❌ $old.svg introuvable"
    }
}
