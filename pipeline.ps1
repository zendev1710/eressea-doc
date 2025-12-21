param(
    [Parameter(Mandatory=$true)]
    [string]$SourceDe
)

if ($SourceDe -notlike "*.de.md") {
    Write-Host "Skipping non-German source file: $SourceDe"
    exit 0
}

$Base = $SourceDe -replace "\.de\.md$", ""
$TrgEn = "$Base.md"
$TrgFr = "$Base.fr.md"

$HasEn = Test-Path $TrgEn
$HasFr = Test-Path $TrgFr

if (-not $HasEn -and -not $HasFr) {
    Write-Host "No target files (EN/FR) for German source: $SourceDe"
    exit 0
}

Write-Host "=== Normalisation stricte (DE source) ==="
python ./scripts/mdnormalize_strict.py < $SourceDe > "$SourceDe.norm.md"

# EN
if ($HasEn) {
    Write-Host "=== Processing EN: $SourceDe → $TrgEn ==="

    python ./scripts/mdnormalize_strict.py < $TrgEn > "$TrgEn.norm.md"

    python ./scripts/mdstructdiff.py "$SourceDe.norm.md" "$TrgEn.norm.md"
    python ./scripts/mdstructdiff.py "$SourceDe.norm.md" "$TrgEn.norm.md" --fix --output "$TrgEn.fixed.md" --batch

    python ./scripts/split_sentences.py < "$SourceDe.norm.md" > "$SourceDe.sentences.md"
    python ./scripts/split_sentences.py < "$TrgEn.fixed.md" > "$TrgEn.sentences.md"

    python ./scripts/aligner_advanced.py `
        "$SourceDe.sentences.md" `
        "$TrgEn.sentences.md" `
        --dict-source dictionaries/de.cspell.json `
        --dict-target dictionaries/en.cspell.json `
        --output "$TrgEn.aligned.tsv"
}

# FR
if ($HasFr) {
    Write-Host "=== Processing FR: $SourceDe → $TrgFr ==="

    python ./scripts/mdnormalize_strict.py < $TrgFr > "$TrgFr.norm.md"

    if ($HasEn) {
        $SourceForFr = "$TrgEn.fixed.md"
        $DictSource = "dictionaries/en.cspell.json"
        Write-Host "FR aligned against EN"
    } else {
        $SourceForFr = "$SourceDe.norm.md"
        $DictSource = "dictionaries/de.cspell.json"
        Write-Host "FR aligned against DE"
    }

    python ./scripts/mdstructdiff.py "$SourceForFr" "$TrgFr.norm.md"
    python ./scripts/mdstructdiff.py "$SourceForFr" "$TrgFr.norm.md" --fix --output "$TrgFr.fixed.md" --batch

    python ./scripts/split_sentences.py < "$SourceForFr" > "$SourceForFr.sentences.md"
    python ./scripts/split_sentences.py < "$TrgFr.fixed.md" > "$TrgFr.sentences.md"

    python ./scripts/aligner_advanced.py `
        "$SourceForFr.sentences.md" `
        "$TrgFr.sentences.md" `
        --dict-source $DictSource `
        --dict-target dictionaries/fr.cspell.json `
        --output "$TrgFr.aligned.tsv"
}

Write-Host "=== Done for $SourceDe ==="
