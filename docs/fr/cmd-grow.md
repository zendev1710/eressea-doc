# GROW

**`GROW`**`Horses`  
**`GROW`**`[`*`quantité`*`] HERBS`

**`GROW`** est un ordre long avec lequel les unités essaient de replanter des plantes dans une région ou d'élever des chevaux dans une Stable (écurie).

Avec `GROW HORSES` une unité peut élever un cheval par personne et par niveau dans la compétence [Taming] avec une probabilité de \[Taming level\]%. 3 personnes niveau 5 auraient donc 3 \* 5 = 15 tentatives à 5% d'obtenir un cheval en plus.

Pour pouvoir élever des chevaux, il faut qu'il y ait au moins deux chevaux dans l'[écurie]. En outre, il doit y avoir un cheval par "opportunité d'élevage" (c'est-à-dire 15 chevaux dans l'exemple ci-dessus). L'unité doit avoir elle-même les chevaux, le pool de matériel n'est pas utilisé ici.

Pour `GROW HERBS` vous devez avoir au moins [Herbalism][Taming] 6. L'unité essaie de planter le nombre de plantes spécifié, mais pas plus d'une plante par niveau de compétence ; elle a besoin du nombre approprié de plantes du type correspondant ainsi que d'une potion de "Water of Life". Il n'est pas possible de changer les types d'herbes d'une région, l'unité essaie toujours de replanter le type trouvé auparavant.

## Voir aussi

- [PLANT] Herbs/Trees/Seeds

<!-- From [https://wiki.eressea.de/index.php?title=ZÜCHTE/fr&oldid=14489] -->

  [Taming]: ./skills-list.md "Liste der Talente"
  [écurie]: ./buildings-others.md#pferdezucht "Andere Gebäude"
  [PLANT]: ./cmd-plant.md "PFLANZE"
