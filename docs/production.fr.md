---
# cSpell:locale fr
alias: production-fr
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD041 MD042 MD052 -->
[](){ #production-fr-id }

# Production

Diverses choses peuvent être produites à Eressea.  

Il existe des [[ressources]] (par exemple le fer, les pierres, le bois, les chevaux) et des [[objets|produits finis]] : diverses armes et armures, des [bateaux][bateaux-id], des chariots, des [bâtiments][batiments-id], des [[routes]] et des [[alchimie|potions]].  
Pour pouvoir produire, il faut posséder les compétences appropriées.  

La plupart des productions s"effectuent avec l'ordre [[cmd-make|`MAKE`*`<number>`*` `*`item`*]], par exemple `MAKE Iron`, `MAKE Sword` ou `MAKE 15 Elvenbow`.  

Selon l'objet, un niveau de compétence différent est requis pour pouvoir le produire.  
La majorité des [[ressources]] ne nécessitent qu'une connaissance de base des compétences correspondantes (niveau 1), tandis que la plupart des [[objets]] nécessitent des niveaux de compétence plus élevés.  
Pour les objets avec des valeurs de compétence minimales élevées, vous ne pouvez en fabriquer que quelques-uns.
Dans tous les cas, **par unité et sur un tour**, vous ne pouvez produire qu’un seul type d’objet ou de ressource et travailler sur un seul bâtiment ou bateau.  

À l'exception du [laen][laen-fr-id]{title="Laen"} et de l'[adamantium][adamantium-fr-id], deux métaux particulièrement précieux et rares, et du [mallorn][mallorn-fr-id]{title="Mallorn"} (un bois magique), toutes les matières premières peuvent être produites avec une valeur de compétence de 1, tout comme les chevaux et les plantes.  
Pour obtenir du laen et de l'adamantium, vous avez besoin d'une [mine][mine-fr-id]{title="Mine"} et d'une compétence d'[extraction minière][extraction-miniere]{title="Mining"} de **7 pour le laen**, de **8 pour l'adamantium**, et d'une compétence de niveau 2 en [sylviculture][sylviculture]{title="Forestry"} pour le mallorn.

Pour les objets ainsi que pour les bâtiments et les bateaux, les niveaux de compétence de toutes les personnes de l'unité sont additionnés et divisés par la compétence minimale requise en construction.  
Pour chaque point ainsi calculé, un bâtiment ou un beateau peut être construit ou agrandi d'un point, ou un objet peut être produit.

Une fois que la construction d'un bâtiment ou un bateau a débuté, vous pouvez continuer à le construire avec autant d'unités que vous le souhaitez.  
Cependant, il n'est pas possible de construire plusieurs bâtiments ou bateaux en même temps avec une seule unité, même si les niveaux de compétences et les ressources le permettent théoriquement.

## Exemple 1

`MAKE 10 Shield`  

Permet à une unité de produire 10 boucliers, en supposant qu'elle :

- possède 10 fer
- soit au moins T2 en [fabrication d'armures][fabrication-darmures]{title="Armoursmithing"}
- posssède un total de 20 niveaux de compétence (10 boucliers x compétence minimale 2 = 20)

## Exemple 2

`MAKE 3 Boat`  

Cet ordre ne permet pas à l'unité de construire trois bateaux séparés.  
Il définit la quantité de bois voulue pour construire le bateau du type mentionné (ici 3 sur 5 pour un bateau).

## Exemple 3

Une unité composée de 4 personnes et **T5 en [fabrication d'armes][fabrication-darmes]{title="Weaponsmithing"}** possède un total de 20 niveaux de compétence.  
Elle peut utiliser ses compétences pour créer au choix (et sans aucun outil) par exemple :

- 6 épées (compétence requise T3), ou
- 4 arcs elfiques (s'il s'agit d'elfes; nécessite une compétence requise T5), ou
- 10 lances (compétence requise T2)

## Exemple 4

Avec une **[forge][forge]{title="Smithy"}**, la consommation de fer pour les épées et les boucliers (et autres objets produits dans une forge) est **réduite de moitié**.  
Il est par exemple possible de produire 10 boucliers à partir de 5 fers.  

Les forgerons bénéficient également d'un **bonus de compétence de +1** en [fabrication d'armes][fabrication-darmes]{title="Weaponsmithing"} et [fabrication d'armures][fabrication-darmures]{title="Armoursmithing"}.  

!!! note "important"
    Les niveaux de compétence ne comptent ensemble que si les personnes sont dans une unité !  
    Cependant, l'unité doit toujours avoir la valeur de compétence minimale

En particulier pour les grandes factions, « collecter » tous les objets nécessaires à la production (par exemple de bâtiments) peut s'avérer fastidieux.  
Pour faciliter la collecte, il existe une [[reserve-d-objets]].

## Voir aussi

- [[resources]]
- [[items|Goods]]
- [[roads]]
- [[ships]]
- [[buildings]]
- [[faction-pool]]

Poursuivre la lecture : [[resources]].

<!-- From [https://wiki.eressea.de/index.php?title=Produktion&oldid=16875] -->
