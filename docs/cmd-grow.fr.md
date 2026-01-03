---
# cSpell:locale fr, en
alias: cmd-grow-fr
---
# GROW

**`GROW`**`HORSES`  
**`GROW`**`[`*`quantité`*`] HERBS`  

**`GROW`** est un ordre long avec lequel les unités essaient de replanter des plantes dans une région, ou d'élever des chevaux dans une [haras].

Avec `GROW HORSES` une unité peut élever un cheval par personne et par niveau dans la compétence [Taming] avec une probabilité de *\[Taming skill level\]*%.
3 personnes niveau 5 auraient donc 3 x 5 = 15 tentatives à 5% d'obtenir un cheval en plus.

Pour pouvoir élever des chevaux, il faut qu'il y ait au moins deux chevaux dans l'[écurie].
En outre, il doit y avoir un cheval par "opportunité d'élevage" (c'est-à-dire 15 chevaux dans l'exemple ci-dessus).
L'unité doit avoir elle-même les chevaux, le pool de matériel n'est pas utilisé ici.

Pour `GROW HERBS` vous devez avoir au moins [Herbalism][Taming] 6.
L'unité essaie de planter le nombre de plantes spécifié, mais pas plus d'une plante par niveau de compétence;
elle a besoin du nombre approprié de plantes du type correspondant ainsi que d'une potion de "Water of Life".
Il n'est pas possible de changer les types d'herbes d'une région, l'unité essaie toujours de replanter le type trouvé auparavant.

## Voir aussi

- [[cmd-plant]] Herbs/Trees/Seeds

<!-- From [https://wiki.eressea.de/index.php?title=GROW/fr&oldid=14489] -->

[Taming]: ./skills-list.md#equitation
[haras]: ./buildings-others.md#haras
