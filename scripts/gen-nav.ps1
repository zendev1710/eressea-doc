$yaml = @"
nav:
  - Home: index.md
  - Getting Started: introduction.md
  - Production: production.md
  - Money: silver.md
  - War: war.md
  - Rules: rules.md
  - Hints: hints.md
  - FAQ: faq.md
  - World:
"@

$files = Get-ChildItem -Path "docs/world" -Name "*.md" | Where-Object { $_ -notmatch '\.(fr|de)\.md$' } | Sort-Object
foreach ($file in $files) {
    $title = $file -replace '\.md$', ''
    $yaml += "`n      - $title`: world/$file"
}

$yaml += "`n  - Gameplay:"
$files = Get-ChildItem -Path "docs/gameplay" -Name "*.md" | Where-Object { $_ -notmatch '\.(fr|de)\.md$' } | Sort-Object
foreach ($file in $files) {
    $title = $file -replace '\.md$', ''
    $yaml += "`n      - $title`: gameplay/$file"
}

$yaml += "`n  - Gameplay Misc:"
$files = Get-ChildItem -Path "docs/gameplay-misc" -Name "*.md" | Where-Object { $_ -notmatch '\.(fr|de)\.md$' } | Sort-Object
foreach ($file in $files) {
    $title = $file -replace '\.md$', ''
    $yaml += "`n      - $title`: gameplay-misc/$file"
}

$yaml += "`n  - Magic:"
$files = Get-ChildItem -Path "docs/magic" -Name "*.md" | Where-Object { $_ -notmatch '\.(fr|de)\.md$' } | Sort-Object
foreach ($file in $files) {
    $title = $file -replace '\.md$', ''
    $yaml += "`n      - $title`: magic/$file"
}

$yaml += "`n  - Orders:"
$files = Get-ChildItem -Path "docs/commands" -Name "*.md" | Where-Object { $_ -notmatch '\.(fr|de)\.md$' } | Sort-Object
foreach ($file in $files) {
    $title = $file -replace '\.md$', ''
    $yaml += "`n      - $title`: commands/$file"
}

$yaml += "`n  - Items:"
$files = Get-ChildItem -Path "docs/items" -Name "*.md" | Where-Object { $_ -notmatch '\.(fr|de)\.md$' } | Sort-Object
foreach ($file in $files) {
    $title = $file -replace '\.md$', ''
    $yaml += "`n      - $title`: items/$file"
}

$yaml += "`n  - Special Items:"
$files = Get-ChildItem -Path "docs/special-items" -Name "*.md" | Where-Object { $_ -notmatch '\.(fr|de)\.md$' } | Sort-Object
foreach ($file in $files) {
    $title = $file -replace '\.md$', ''
    $yaml += "`n      - $title`: special-items/$file"
}

$yaml += "`n  - Appendices:"
$files = Get-ChildItem -Path "docs/appendices" -Name "*.md" | Where-Object { $_ -notmatch '\.(fr|de)\.md$' } | Sort-Object
foreach ($file in $files) {
    $title = $file -replace '\.md$', ''
    $yaml += "`n      - $title`: appendices/$file"
}

Set-Content -Path "nav.yaml" -Value $yaml
Write-Host "Generated nav.yaml - first 100 lines:"
(Get-Content nav.yaml | Select-Object -First 100) | Out-Host
