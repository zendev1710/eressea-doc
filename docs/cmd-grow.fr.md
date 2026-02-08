---
# cSpell:locale fr
alias: cmd-grow-fr
---
# `GROW`

*Ordre [long].*  

**`GROW HORSES`  
**`GROW [<quantité>] HERBS`  

Avec l'ordre **`GROW`**, une unité essaie de replanter des plantes dans une région, ou d'élever des chevaux dans un [Haras].  

Avec `GROW HORSES` une unité peut élever un cheval par personne et par niveau en [Apprivoisement de chevaux] avec une probabilité de ***\[Niveau Apprivoisement\]***%.  
3 personnes niveau 5 auraient donc 3 x 5 = 15 tentatives à 5% d'obtenir un cheval en plus.  

Pour pouvoir élever des chevaux, il faut qu'il y ait au moins 2 chevaux dans le [Haras].  
En outre, il doit y avoir un cheval par "opportunité d'élevage" (c'est-à-dire 15 chevaux dans l'exemple ci-dessus).  
L'unité doit avoir elle-même les chevaux, la [[reserve-d-objets]] n'est pas utilisée ici.  

Pour pouvoir utiliser l'ordre `GROW HERBS`, vous devez avoir au moins [Herboristerie] au niveau 6.  
L'unité essaie de planter le nombre de plantes spécifié, mais pas plus d'une plante par niveau de compétence;  
elle a besoin du nombre approprié de plantes du type correspondant, ainsi qu'une potion "Water of Life".  
Il n'est pas possible de changer le type de plante d'une région, l'unité ne peut replanter que le type de plante trouvé précédemment dans la région.  

## Voir aussi

- [[cmd-plant]] (pour les plantes, les arbres ou les graines)

<!-- From [https://wiki.eressea.de/index.php?title=GROW/fr&oldid=14489] -->

[long]: ./commands.md#ordres-courts-et-longs
[Haras]: ./buildings-others.md#haras
[Apprivoisement de chevaux]: ./skills-list.md#apprivoisement
[Herboristerie]: ./skills-list.md#herboristerie
