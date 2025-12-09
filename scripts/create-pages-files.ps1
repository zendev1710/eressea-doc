# Générer tous les fichiers .pages pour chaque catégorie et langue
$langs = @('en', 'fr', 'de')

$categories = @{
    'commands' = @('commands', 'commands-list', 'commands-send', 'commands-sequence', 'commands-extended', 'commands-send-from-magellan', 'commands-short-descriptions')
    'magic' = @('magic', 'magic-schools', 'magic-school-cerddor', 'magic-school-draig', 'magic-school-gwyrrd', 'magic-school-illaun', 'magic-school-tybied', 'spells-list', 'spells-descriptions')
    'gameplay' = @('alliances', 'armed', 'buildings', 'buildings-others', 'camouflage', 'castles', 'combat', 'familiars', 'factions', 'races', 'sailing', 'ships', 'skills', 'skills-list', 'skills-modifiers', 'tactic')
    'items' = @('adamantium', 'adamantium-armor', 'alchemy', 'herbs', 'potions-and-herbs', 'amulet-of-true-vision', 'antimagic-crystal', 'belt-of-troll-strength', 'dream-eye', 'flaming-sword', 'iron-golem', 'magical-herb-bag', 'mountain-guard', 'negative-weight-bag', 'ring-of-invisibility', 'ring-of-power', 'sphere-of-invisibility', 'stardust', 'stone-golem', 'sun-sail')
    'world' = @('world', 'faction-pool', 'items-pool', 'monsters', 'resources', 'roads', 'terrains', 'travel')
    'gameplay-misc' = @('auto-event-response', 'auto-learning-chains', 'auto-trading', 'auto-transport', 'auto-way-finding', 'atlantis', 'basics', 'eressea', 'optimize-learning-chains', 'optimize-production', 'optimize-transport', 'optimize-way-finding')
    'special-items' = @('birthday-cake', 'christmas', 'christmas-tree', 'contributors', 'cr-format', 'csmapfx', 'development', 'echeck', 'ehmv', 'eressea-join', 'eressea-story', 'farmers-hike', 'farmers-proliferation', 'fftools', 'magellan', 'mistletoe', 'pentagram-and-tirawon', 'plague', 'play-too-much-if', 'player-pages', 'puppy-protection', 'shell', 'snowman', 'the-third-age', 'tips-and-tricks', 'toad', 'vorlage')
    'appendices' = @('getting-started-tips', 'reports', 'round-first', 'war-tables')
}

$docsPath = 'C:\Users\cyril\Documents\dev\ext\eressea-doc\docs'

foreach ($lang in $langs) {
    foreach ($category in $categories.Keys) {
        $categoryPath = "$docsPath\$lang\$category"
        $pagesFile = "$categoryPath\.pages"
        
        # Créer le contenu du .pages
        $navContent = "nav:`n"
        foreach ($file in $categories[$category]) {
            $label = $file -replace '-', ' ' | ForEach-Object { (Get-Culture).TextInfo.ToTitleCase($_) }
            $navContent += "  - $label`: $file.md`n"
        }
        
        # Écrire le fichier
        Set-Content -Path $pagesFile -Value $navContent -Encoding UTF8
        Write-Host "✓ Created $lang/$category/.pages"
    }
}

Write-Host "`n✓ Tous les .pages ont été créés!"
