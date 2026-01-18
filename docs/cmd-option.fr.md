---
# cSpell:locale fr
alias: cmd-option-fr
---
# `OPTION`

**`OPTION`**` `*`option`*`[NOT]`  

<!-- TODO: check if the following options stay in german or not for english players -->

Ces options peuvent être activées ou désactivées.
Vous contrôlez exactement à quoi ressemble l’évaluation.  

- `AUSWERTUNG` : il s'agit de l'évaluation normale en texte brut.
  Si vous utilisez uniquement l'évaluation informatique, l'évaluation normale peut être omise
- `COMPUTER` : cette évaluation est plus facile à lire pour les programmes. Il peut être utilisé pour alimenter tout type de programmes tiers développé, par ex. outils auxiliaires ou visionneuse de cartes
- `ZIPPED` : l'évaluation sera compressée au format zip avant envoi par email
- `BZIP2` : l'évaluation sera compressée avec bzip2 avant envoi par email
- `STATISTIK` : avec cette option, un résumé statistique est affichée après chaque région dans l'analyse standard
- `PUNKTE` : avec cette option, dès le 13ème tour au plus tôt, un score est émis qui permet une petite comparaison avec les autres factions
- `ZUGVORLAGE` : un fichier séparé contient un [[ordres|modèle d'ordres du prochain tour]].
  Si vous n'en avez pas besoin, par exemple parce que vous utilisez un outil pour créer un déplacement, vous devez désactiver le modèle d'ordres
- `TALENTVERSCHIEBUNG` : cela vous permet d'activer l'ajout d'informations relatives aux compétences dans le NR. Après la compétence, il est indiqué si elle a changé au cours du tour
- `ADRESSEN` : ceci ajoute au rapport la liste d'adresses des factions vues dans le groupe

## Anciennes options

À partir de l'évaluation 559, les options  `MATERIALPOOL` et  `SILVERPOOL` ont été **activées** par défaut. **Ces options ne sont plus désactivables**.

- `SILVERPOOL` : en règle générale, les unités paient les dépenses engagées « de leur poche ». Cette option peut être utilisée pour garantir que l'argent nécessaire soit collecté auprès de toutes les unités de la région
- `MATERIALPOOL` : si la [[reserve-d-objets]] est activée, tous les objets requis dans une unité sont collectés selon les besoins, comme pour l'argent avec la [réserve d'argent].
  Les unités peuvent utiliser la commande [[cmd-reserve]] pour sécuriser des objets, empêchant ainsi d'autres unités de les prendre et de les consommer.
  Cette option est à utiliser avec précaution, car vous pouvez rapidement, par exemple, utiliser tout le bois d'une région que vous aviez prévu à d'autres fins, simplement parce que vous avez oublié un `RESERVE`.

<!-- From [https://wiki.eressea.de/index.php?title=OPTION&oldid=16703] -->

[réserve d'argent]: ./items-pool.md#reserve-dargent
