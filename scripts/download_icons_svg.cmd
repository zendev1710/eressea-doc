@echo off
set TARGET_DIR=docs/assets/icons
mkdir %TARGET_DIR%

set ICONS=alchemy crossbow muscle-up mining bowman bricks trade crossed-swords forest catapult herbs magic-swirl beast-call horse-head breastplate ship-wheel sailboat spy halberd stone-block receive-money road battle-plan hood drama-masks anvil punch cart awareness

for %%I in (%ICONS%) do (
    echo Téléchargement : %%I.svg
    curl -s -L "https://raw.githubusercontent.com/game-icons/icons/master/svg/delapouite/%%I.svg" -o "%TARGET_DIR%/%%I.svg"
)

echo ✔ Tous les fichiers SVG ont été téléchargés dans %TARGET_DIR%
