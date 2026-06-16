---
# cSpell:locale fr
alias: cmd-option-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# OPTION

**OPTION**&nbsp;ADDRESSES|COMPUTER|PLAINTEXT|SCORE|SHOWSKCHANGE|STATISTICS|TEMPLATE&nbsp;&#91;NOT&#93;  
**OPTION**&nbsp;ZIPPED|BZIP2  

Ces options peuvent être activées ou désactivées avec l'opérateur `NOT` (à l'exception de `ZIPPED` et `BZIP2`).
Avec elles, vous contrôlez exactement à quoi ressemble l’évaluation.  

!!! info "Information"
    Les options et leur statut sont renseignés en allemand dans le rapport informatique (`.cr`) de l'évaluation :
    ```text
    OPTIONEN
    1;AUSWERTUNG
    1;COMPUTER
    1;ZUGVORLAGE
    1;STATISTIK
    1;ZIPPED
    1;ADRESSEN
    0;BZIP2
    1;PUNKTE
    0;SHOWSKCHANGE
    ```

Les options disponibles sont décrites ci-dessous.

## `OPTION ADDRESSES`

**OPTION**&nbsp;ADDRESSES &#91;NOT&#93;  

Si cette option est activée, la liste des adresses email des factions visibles lors du tour est ajoutée au rapport.

## `OPTION COMPUTER`

**OPTION**&nbsp;COMPUTER &#91;NOT&#93;  

Si cette option est activée, l'évaluation informatique (fichier d'extension `.cr`) est incluse à l'email renvoyé par le serveur au joueur.  
L'évaluation informatique est plus facile à lire pour les programmes.  
Elle peut être utilisée pour alimenter tout type de programme tiers développé, par exemple les outils auxiliaires ou visionneuse de cartes.

## `OPTION PLAINTEXT`

**OPTION**&nbsp;PLAINTEXT &#91;NOT&#93;  

Si cette option est activée, l'évaluation normale en texte brut (fichier d'extension `.nr`) est incluse dans l'email renvoyé par le serveur au joueur.  
Si vous utilisez uniquement l'évaluation informatique (fichier d'extension `.cr`), vous pouvez désactiver l'option; l'évaluation normale ne sera alors pas envoyée.

## `OPTION SCORE`

**OPTION**&nbsp;SCORE &#91;NOT&#93;  

Si cette option est activée, **à partir du 13ème tour**, un score est émis pour votre faction.  
Ce score est un premier élément de comparaison de votre progression dans le jeu relativement aux autres factions.

## `OPTION SHOWSKCHANGE`

**OPTION**&nbsp;SHOWSKCHANGE &#91;NOT&#93;  

Si cette option est activée, des informations relatives aux compétences des unités sont ajoutées dans le rapport standard NR.  
Après chaque compétence, il est indiqué si elle a changé au cours du tour.

## `OPTION STATISTICS`

**OPTION**&nbsp;STATISTICS &#91;NOT&#93;  

Si cette option est activée, un résumé statistique est affiché après chaque région dans l'évaluation normale (fichier d'extension `.nr`).

## `OPTION TEMPLATE`

**OPTION**&nbsp;TEMPLATE &#91;NOT&#93;  

Si cette option est activée, un fichier séparé contiendra un [modèle d'ordres du prochain tour][ordres].  
Si vous n'en avez pas besoin, par exemple parce que vous utilisez un outil pour renseigner les ordres, il est recommandé de désactiver cette option.  

## `OPTION ZIPPED|BZIP2`

**OPTION**&nbsp;ZIPPED  
**OPTION**&nbsp;BZIP2  

Avant d'être envoyé par email par le serveur au joueur, le fichier correspondant à l'évaluation sera **compressé** à un format défini par l'une des deux options suivantes :

- `OPTION ZIPPED` : compression au format `zip`
- `OPTION BZIP2` : compression avec `bzip2`

## Options dépréciées

**À partir de l'évaluation 559**, les options  `ITEMPOOL` et  `SILVERPOOL` ont été activées par défaut et **ne sont plus désactivables**.  

La [réserve d'objets][reserve-d-objets-id] et la [réserve d'argent][reserve-dargent] sont donc toujours actives.  

!!! note "rappel"
    Les unités peuvent utiliser l'ordre [`RESERVE`][cmd-reserve-fr] pour sécuriser des objets, empêchant ainsi d'autres unités de les prendre et de les consommer.  

<!-- From [https://wiki.eressea.de/index.php?title=OPTION&oldid=16703] -->

[cmd-reserve-fr]: [[cmd-reserve-fr]]
