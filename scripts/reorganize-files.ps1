# Déplacer les fichiers des commandes
$langs = @('en', 'fr', 'de')
$cmdFiles = @(
    'cmd-attack', 'cmd-banner', 'cmd-buy', 'cmd-carry', 'cmd-cast', 'cmd-claim',
    'cmd-combat', 'cmd-combatspell', 'cmd-comment', 'cmd-contact', 'cmd-default',
    'cmd-describe', 'cmd-destroy', 'cmd-email', 'cmd-end', 'cmd-enter', 'cmd-entertain',
    'cmd-follow', 'cmd-forget', 'cmd-give', 'cmd-group', 'cmd-grow', 'cmd-guard',
    'cmd-help', 'cmd-hide', 'cmd-language', 'cmd-learn', 'cmd-learn-auto', 'cmd-leave',
    'cmd-make', 'cmd-message', 'cmd-move', 'cmd-name', 'cmd-next', 'cmd-number',
    'cmd-option', 'cmd-origin', 'cmd-password', 'cmd-pay-not', 'cmd-piracy', 'cmd-plant',
    'cmd-prefix', 'cmd-promote', 'cmd-quit', 'cmd-recruit', 'cmd-region', 'cmd-research',
    'cmd-reserve', 'cmd-ride', 'cmd-route', 'cmd-sell', 'cmd-semicolon', 'cmd-show',
    'cmd-sort', 'cmd-spy', 'cmd-steal', 'cmd-tax', 'cmd-teach', 'cmd-unit', 'cmd-use', 'cmd-work'
)

$magicFiles = @(
    'magic-school-cerddor', 'magic-school-draig', 'magic-school-gwyrrd', 'magic-school-illaun',
    'magic-school-tybied', 'spells-list', 'spells-descriptions'
)

$gameplayFiles = @(
    'combat', 'tactic', 'factions', 'races', 'skills', 'skills-list', 'skills-modifiers',
    'buildings', 'buildings-others', 'castles', 'ships', 'sailing', 'familiars'
)

$itemsFiles = @(
    'potions-and-herbs', 'herbs', 'amulet-of-true-vision', 'antimagic-crystal',
    'belt-of-troll-strength', 'dream-eye', 'flaming-sword', 'iron-golem',
    'magical-herb-bag', 'mountain-guard', 'negative-weight-bag', 'ring-of-invisibility',
    'ring-of-power', 'sphere-of-invisibility', 'stardust', 'stone-golem', 'sun-sail', 'alchemy'
)

$worldFiles = @(
    'travel', 'terrains', 'roads', 'resources', 'faction-pool', 'items-pool', 'monsters'
)

$docsPath = 'C:\Users\cyril\Documents\dev\ext\eressea-doc\docs'

foreach ($lang in $langs) {
    Write-Host "Processing $lang..."
    
    # Déplacer fichiers de commandes
    foreach ($file in $cmdFiles) {
        $src = "$docsPath\$lang\$file.md"
        $dst = "$docsPath\$lang\commands\$file.md"
        if (Test-Path $src) {
            Move-Item $src $dst -Force -ErrorAction SilentlyContinue
            Write-Host "✓ Moved $file to commands"
        }
    }
    
    # Déplacer fichiers de magie
    foreach ($file in $magicFiles) {
        $src = "$docsPath\$lang\$file.md"
        $dst = "$docsPath\$lang\magic\$file.md"
        if (Test-Path $src) {
            Move-Item $src $dst -Force -ErrorAction SilentlyContinue
            Write-Host "✓ Moved $file to magic"
        }
    }
    
    # Déplacer fichiers de gameplay
    foreach ($file in $gameplayFiles) {
        $src = "$docsPath\$lang\$file.md"
        $dst = "$docsPath\$lang\gameplay\$file.md"
        if (Test-Path $src) {
            Move-Item $src $dst -Force -ErrorAction SilentlyContinue
            Write-Host "✓ Moved $file to gameplay"
        }
    }
    
    # Déplacer fichiers d'objets
    foreach ($file in $itemsFiles) {
        $src = "$docsPath\$lang\$file.md"
        $dst = "$docsPath\$lang\items\$file.md"
        if (Test-Path $src) {
            Move-Item $src $dst -Force -ErrorAction SilentlyContinue
            Write-Host "✓ Moved $file to items"
        }
    }
    
    # Déplacer fichiers du monde
    foreach ($file in $worldFiles) {
        $src = "$docsPath\$lang\$file.md"
        $dst = "$docsPath\$lang\world\$file.md"
        if (Test-Path $src) {
            Move-Item $src $dst -Force -ErrorAction SilentlyContinue
            Write-Host "✓ Moved $file to world"
        }
    }
}

Write-Host "`n✓ Reorganisation complète!"
