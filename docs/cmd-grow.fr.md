---
# cSpell:locale fr
alias: cmd-grow-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# GROW

*Ordre [long][ordres-courts-et-longs].*  

**`GROW HORSES`  
**`GROW [<quantité>] HERBS`  

Avec l'ordre **`GROW`**, une unité essaie de replanter des plantes dans une région, ou d'élever des chevaux dans un [haras][haras]{title="Stable"}.  

Avec `GROW HORSES` une unité peut élever un cheval par personne et par niveau en [apprivoisement de chevaux][apprivoisement]{title="Taming"} avec une probabilité de ***\[Niveau Apprivoisement\]* %**.  
3 personnes niveau 5 auraient donc 3 x 5 = 15 tentatives à 5 % d'obtenir un cheval en plus.  

Pour pouvoir élever des chevaux, il faut qu'il y ait au moins 2 chevaux dans le [haras][haras]{title="Stable"}.  
En outre, il doit y avoir un cheval par "opportunité d'élevage" (c'est-à-dire 15 chevaux dans l'exemple ci-dessus).  
L'unité doit avoir elle-même les chevaux, la [réserve d'objets][reserve-d-objets-id] n'est pas utilisée ici.  

Pour pouvoir utiliser l'ordre `GROW HERBS`, **il faut être T6** en [herboristerie][herboristerie]{title="Herbalism"}.

L'unité essaie de planter le nombre de plantes spécifié, mais pas plus d'une plante par niveau de compétence;  
elle a besoin du nombre approprié de plantes du type correspondant, ainsi qu'une potion "Water of Life".  
Il n'est pas possible de changer le type de plante d'une région, l'unité ne peut replanter que le type de plante trouvé précédemment dans la région.  

## Voir aussi

- [`PLANT`][cmd-plant-fr] (pour les plantes, les arbres ou les graines)

<!-- From [https://wiki.eressea.de/index.php?title=GROW/fr&oldid=14489] -->

[cmd-plant-fr]: [[cmd-plant-fr]]
