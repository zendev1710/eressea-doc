# Script to migrate from folder structure to suffix structure for i18n
# docs/en/file.md -> docs/file.md
# docs/fr/file.md -> docs/file.fr.md
# docs/de/file.md -> docs/file.de.md

$docsRoot = "c:\Users\cyril\Documents\dev\ext\eressea-doc\docs"

# Create backup
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupDir = "$docsRoot/../docs_backup_$timestamp"
Copy-Item $docsRoot -Destination $backupDir -Recurse
Write-Host "Backup created at: $backupDir"

# Get all files from en/ folder (these are the base files)
$enFiles = Get-ChildItem -Path "$docsRoot/en" -Recurse -File

foreach ($file in $enFiles) {
    $relativePath = $file.FullName.Substring("$docsRoot/en/".Length)
    $destPath = Join-Path $docsRoot $relativePath
    
    # Create directory if needed
    $destDir = Split-Path $destPath
    if (-not (Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }
    
    # Copy English file (no suffix)
    Copy-Item $file.FullName -Destination $destPath -Force
    Write-Host "Copied (EN): $relativePath"
}

# Copy French files with .fr suffix
$frFiles = Get-ChildItem -Path "$docsRoot/fr" -Recurse -File
foreach ($file in $frFiles) {
    $relativePath = $file.FullName.Substring("$docsRoot/fr/".Length)
    $destPath = Join-Path $docsRoot $relativePath
    
    # Insert .fr before extension
    $destPath = $destPath -replace '\.md$', '.fr.md'
    $destDir = Split-Path $destPath
    
    if (-not (Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }
    
    Copy-Item $file.FullName -Destination $destPath -Force
    Write-Host "Copied (FR): $relativePath -> $(Split-Path $destPath -Leaf)"
}

# Copy German files with .de suffix
$deFiles = Get-ChildItem -Path "$docsRoot/de" -Recurse -File
foreach ($file in $deFiles) {
    $relativePath = $file.FullName.Substring("$docsRoot/de/".Length)
    $destPath = Join-Path $docsRoot $relativePath
    
    # Insert .de before extension
    $destPath = $destPath -replace '\.md$', '.de.md'
    $destDir = Split-Path $destPath
    
    if (-not (Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }
    
    Copy-Item $file.FullName -Destination $destPath -Force
    Write-Host "Copied (DE): $relativePath -> $(Split-Path $destPath -Leaf)"
}

# Remove old language folders
Remove-Item "$docsRoot/en" -Recurse -Force
Remove-Item "$docsRoot/fr" -Recurse -Force
Remove-Item "$docsRoot/de" -Recurse -Force

Write-Host "Migration complete!"
Write-Host "Old language folders deleted."
Write-Host "New structure: docs/file.md, docs/file.fr.md, docs/file.de.md"
