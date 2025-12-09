# Mapping complet des fichiers à leurs catégories
$langs = @('en', 'fr', 'de')
$mapping = @{
    'commands' = @(
        'commands-list', 'commands-send', 'commands-sequence', 'commands-extended',
        'commands-send-from-magellan', 'commands-short-descriptions', 'commands'
    )
    'magic' = @(
        'magic-school-cerddor', 'magic-school-draig', 'magic-school-gwyrrd', 'magic-school-illaun',
        'magic-school-tybied', 'spells-list', 'spells-descriptions', 'magic', 'magic-schools'
    )
    'gameplay' = @(
        'combat', 'tactic', 'factions', 'races', 'skills', 'skills-list', 'skills-modifiers',
        'buildings', 'buildings-others', 'castles', 'ships', 'sailing', 'familiars',
        'alliances', 'armed', 'camouflage'
    )
    'items' = @(
        'potions-and-herbs', 'herbs', 'amulet-of-true-vision', 'antimagic-crystal',
        'belt-of-troll-strength', 'dream-eye', 'flaming-sword', 'iron-golem',
        'magical-herb-bag', 'mountain-guard', 'negative-weight-bag', 'ring-of-invisibility',
        'ring-of-power', 'sphere-of-invisibility', 'stardust', 'stone-golem', 'sun-sail', 
        'alchemy', 'adamantium-armor', 'adamantium', 'armed'
    )
    'world' = @(
        'travel', 'terrains', 'roads', 'resources', 'faction-pool', 'items-pool', 'monsters',
        'world'
    )
    'gameplay-misc' = @(
        'auto-event-response', 'auto-learning-chains', 'auto-trading', 'auto-transport',
        'auto-way-finding', 'optimize-learning-chains', 'optimize-production',
        'optimize-transport', 'optimize-way-finding', 'atlantis', 'basics', 'eressea'
    )
    'appendices' = @(
        'round-first', 'getting-started-tips', 'reports', 'war-tables'
    )
    'special-items' = @(
        'birthday-cake', 'christmas', 'christmas-tree', 'echeck', 'ehmv', 'eressea-join',
        'eressea-story', 'farmers-hike', 'farmers-proliferation', 'fftools', 'flaming-sword',
        'magellan', 'mistletoe', 'pentagram-and-tirawon', 'plague', 'play-too-much-if',
        'player-pages', 'puppy-protection', 'shell', 'snowman', 'the-third-age', 'tips-and-tricks',
        'toad', 'vorlage', 'development', 'contributors', 'cr-format', 'csmapfx'
    )
}

$docsPath = 'C:\Users\cyril\Documents\dev\ext\eressea-doc\docs'

foreach ($lang in $langs) {
    Write-Host "Processing $lang..."
    
    foreach ($category in $mapping.Keys) {
        $dstDir = "$docsPath\$lang\$category"
        
        foreach ($file in $mapping[$category]) {
            $src = "$docsPath\$lang\$file.md"
            $dst = "$dstDir\$file.md"
            
            if (Test-Path $src) {
                # Créer le dossier s'il n'existe pas
                if (-not (Test-Path $dstDir)) {
                    New-Item -ItemType Directory -Path $dstDir | Out-Null
                }
                
                Move-Item $src $dst -Force -ErrorAction SilentlyContinue
                Write-Host "  ✓ $file → $category/"
            }
        }
    }
}

Write-Host "`n✓ Tous les fichiers ont été déplacés!"
