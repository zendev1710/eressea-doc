# Script to fix .pages files in docs directory
# Rules:
# - Create .pages if it doesn't exist
# - Reference subdirectories and *.md files (base only, no .fr.md or .de.md)
# - Add new entries at the end
# - Remove entries that don't correspond to existing subdirectories or .md files

$docsRoot = "c:\Users\cyril\Documents\dev\ext\eressea-doc\docs"

function Fix-PagesFile {
    param(
        [string]$dirPath
    )
    
    $pagesFile = Join-Path $dirPath ".pages"
    
    # Get subdirectories and base .md files
    $subdirs = @(Get-ChildItem -Path $dirPath -Directory -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Name | Sort-Object)
    $mdFiles = @(Get-ChildItem -Path $dirPath -Filter "*.md" -File -ErrorAction SilentlyContinue | 
                Where-Object { $_.Name -notmatch '\.(fr|de)\.md$' } | 
                Select-Object -ExpandProperty Name | Sort-Object)
    
    $validEntries = @($subdirs) + @($mdFiles)
    
    # Read existing .pages file if it exists
    $existingLines = @()
    $existingNav = @()
    
    if (Test-Path $pagesFile) {
        $existingLines = @(Get-Content $pagesFile)
    }
    
    # Parse existing nav entries
    foreach ($line in $existingLines) {
        $trimmed = $line.Trim()
        if ($trimmed -match '^\- (.+?)(\:|$)') {
            $entry = $matches[1].Trim()
            $existingNav += $entry
        }
    }
    
    # Build new nav content
    $newNav = @()
    
    # Keep valid existing entries (preserve order where they appear)
    foreach ($entry in $existingNav) {
        if ($entry -in $validEntries) {
            $newNav += $entry
        }
    }
    
    # Add new entries (not in existing nav)
    foreach ($entry in $validEntries) {
        if ($entry -notin $newNav) {
            $newNav += $entry
        }
    }
    
    # Generate .pages content
    if ($newNav.Count -gt 0) {
        $content = "nav:`n"
        foreach ($entry in $newNav) {
            $content += "  - $entry`n"
        }
        
        Set-Content -Path $pagesFile -Value $content -Encoding UTF8 -NoNewline
        Write-Host "Fixed: $pagesFile ($(($newNav).Count) entries)"
    } else {
        # Remove .pages if no valid entries
        if (Test-Path $pagesFile) {
            Remove-Item $pagesFile -Force
            Write-Host "Deleted (empty): $pagesFile"
        }
    }
}

# Process root docs directory
Write-Host "Processing docs root..."
Fix-PagesFile $docsRoot

# Process all subdirectories
$allDirs = @(Get-ChildItem -Path $docsRoot -Directory -Recurse -ErrorAction SilentlyContinue)
foreach ($dir in $allDirs) {
    Write-Host "Processing $($dir.FullName)..."
    Fix-PagesFile $dir.FullName
}

Write-Host "Done!"
