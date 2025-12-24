$targetDir = "docs/assets/icons"

if (-not (Get-Command svgo -ErrorAction SilentlyContinue)) {
    Write-Host "❌ svgo n'est pas installé. Installe-le avec : npm install -g svgo"
    exit
}

Write-Host "✨ Optimisation des SVG dans $targetDir"
Write-Host ""

Get-ChildItem "$targetDir\*.svg" | ForEach-Object {
    Write-Host "Optimisation : $($_.Name)"
    svgo $_.FullName --quiet
}

Write-Host ""
Write-Host "✔ Tous les SVG ont été optimisés."
