@echo off
set SRC_DE=%1

echo %SRC_DE% | findstr /E ".de.md" >nul
if errorlevel 1 (
    echo Skipping non-German source file: %SRC_DE%
    exit /b 0
)

set BASE=%SRC_DE:.de.md=%
set TRG_EN=%BASE%.md
set TRG_FR=%BASE%.fr.md

if not exist "%TRG_EN%" (
    set HAS_EN=0
) else (
    set HAS_EN=1
)

if not exist "%TRG_FR%" (
    set HAS_FR=0
) else (
    set HAS_FR=1
)

if %HAS_EN%==0 if %HAS_FR%==0 (
    echo No target files for %SRC_DE%
    exit /b 0
)

echo === Normalisation stricte (DE source) ===
python scripts\mdnormalize_strict.py < "%SRC_DE%" > "%SRC_DE%.norm.md"

REM EN
if %HAS_EN%==1 (
    echo === Processing EN: %SRC_DE% → %TRG_EN% ===

    python scripts\mdnormalize_strict.py < "%TRG_EN%" > "%TRG_EN%.norm.md"

    python scripts\mdstructdiff.py "%SRC_DE%.norm.md" "%TRG_EN%.norm.md"
    python scripts\mdstructdiff.py "%SRC_DE%.norm.md" "%TRG_EN%.norm.md" --fix --output "%TRG_EN%.fixed.md" --batch

    python scripts\split_sentences.py < "%SRC_DE%.norm.md" > "%SRC_DE%.sentences.md"
    python scripts\split_sentences.py < "%TRG_EN%.fixed.md" > "%TRG_EN%.sentences.md"

    python scripts\aligner_advanced.py ^
        "%SRC_DE%.sentences.md" ^
        "%TRG_EN%.sentences.md" ^
        --dict-source dictionaries\de.cspell.json ^
        --dict-target dictionaries\en.cspell.json ^
        --output "%TRG_EN%.aligned.tsv"
)

REM FR
if %HAS_FR%==1 (
    echo === Processing FR: %SRC_DE% → %TRG_FR% ===

    python scripts\mdnormalize_strict.py < "%TRG_FR%" > "%TRG_FR%.norm.md"

    if %HAS_EN%==1 (
        set SOURCE_FOR_FR=%TRG_EN%.fixed.md
        set DICT_SOURCE=dictionaries\en.cspell.json
        echo FR aligned against EN
    ) else (
        set SOURCE_FOR_FR=%SRC_DE%.norm.md
        set DICT_SOURCE=dictionaries\de.cspell.json
        echo FR aligned against DE
    )

    python scripts\mdstructdiff.py "%SOURCE_FOR_FR%" "%TRG_FR%.norm.md"
    python scripts\mdstructdiff.py "%SOURCE_FOR_FR%" "%TRG_FR%.norm.md" --fix --output "%TRG_FR%.fixed.md" --batch

    python scripts\split_sentences.py < "%SOURCE_FOR_FR%" > "%SOURCE_FOR_FR%.sentences.md"
    python scripts\split_sentences.py < "%TRG_FR%.fixed.md" > "%TRG_FR%.sentences.md"

    python scripts\aligner_advanced.py ^
        "%SOURCE_FOR_FR%.sentences.md" ^
        "%TRG_FR%.sentences.md" ^
        --dict-source "%DICT_SOURCE%" ^
        --dict-target dictionaries\fr.cspell.json ^
        --output "%TRG_FR%.aligned.tsv"
)

echo === Done for %SRC_DE% ===
