---
# cSpell:locale fr
alias: chateaux
---
<!-- disable some rules due to of autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Châteaux

Les châteaux augmentent les revenus des paysans, permettent d'échanger des produits de luxe et offrent à leurs occupants une protection en cas d'attaque.  
Ils réduisent également la probabilité de [[peste]].  

Les châteaux sont construits en pierre à l'aide de l'ordre [[cmd-make|`MAKE CASTLE`]] par des unités maîtrisant la [maçonnerie][maconnerie].  
Un château entre dans une nouvelle catégorie selon sa taille :

*Taille d'un château selon son type.*

| Fondation | Poste de commerce | Fortification | Tower | Bastion | Forteresse | Citadelle |
|:---------:|:-----------------:|:-------------:|:-----:|:-------:|:----------:|:---------:|
|     1     |         2         |      10       |  50   |   250   |   1 250    |  6 250+   |

Plus le château est grand, plus il est difficile de l'agrandir.  
Pour continuer à construire un château, vous devez avoir au moins la compétence Maçonnerie au niveau requis.  
Chaque unité dispose de points de production (PP) à chaque tour : (niveau de compétence) x (nombre de personnes).  
Chaque semaine, l'unité agrandit le bâtiment de PP/(niveau de compétence requis) pierres.  
Les pierres nécessaires doivent également être disponibles.  
Vous pouvez facilement construire une tour en une semaine avec une unité suffisamment grande et compétente et suffisamment de pierres.  

Un château a aussi un identifiant (ID), utilisé pour les ordres.  

Premier exemple de château :

```text
Grand temple du chat aux yeux d'or (58), taille 58, tour;
Le temple brille d'un blanc éclatant au soleil, encadré par le vert délicat des arbres du parc.
La tour élancée, qui s'élève au-dessus de la ville, est visible de loin.
Au nord du temple, la ville de Xontormia s'étend le long du Whyren, enjambée un gigantesque pont près du port.
```

Les unités dans un château sont protégées, à savoir qu'une personne est protégée par unité de taille du château.  
Seules les personnes protégées bénéficient du bonus qu'un château donne à ses occupants en cas de raid (pour plus d'informations, voir le chapitre [[guerre]], en particulier la liste des [bonus et malus][bonus-et-malus]).  
Chaque unité de taille du château nécessite une pierre.  

Un plus grand château améliore le revenu de la population : tous les ouvriers et paysans bénéficient d'un bonus lorsqu'ils travaillent, qui dépend de la taille du plus grand château dans une région (voir aussi [tableau du bas][apercu]), de plus le propriétaire du plus grand château reçoit une part du produit des ventes des autres joueurs.  

## Fondation

<!-- cspell:disable -->
*Foundation (EN), Grundmauern (DE)*.
<!-- cspell:enable -->

## Poste de commerce

<!-- cspell:disable -->
*Tradepost (EN), Handelsposten (DE)*.
<!-- cspell:enable -->

## Fortification

<!-- cspell:disable -->
*Fortification (EN), Befestigung (DE)*.
<!-- cspell:enable -->

## Tour

<!-- cspell:disable -->
*Tower (EN), Turm (DE)*.
<!-- cspell:enable -->

## Bastion

<!-- cspell:disable -->
*Stronghold (EN), Burg (DE)*.
<!-- cspell:enable -->

## Forteresse

<!-- cspell:disable -->
*Fortress (EN), Festung (DE)*.
<!-- cspell:enable -->

## Citadelle

<!-- cspell:disable -->
*Citadel (EN), Zitadelle (DE)*.
<!-- cspell:enable -->

## Exemples

L'unité "Thors Baumeister" est composée de 20 personnes de niveau 1 en Maçonnerie, disposant de 100 pierres.  
En raison de son niveau de compétence et du nombre de personnes de l'unité, elle dispose de 20 points de production (PP).  
Cela lui permet de construire `PP / <niveau requis>` unités de taille du chateau chaque semaine.  

Lorsque cette unité commence à construire un nouveau château, elle peut construire 10 unités de taille au premier tour : pour les fondations et le poste de commerce, le niveau minimal en maçonnerie est de 1;  
pour construire une unité de taille, il faut un point de production, donc l'unité construit d'abord le poste de commerce jusqu'à la taille 10, ce qui fait de ce bâtiment une fortification.  
Il reste alors 10 points de production, mais ils sont perdus parce que le niveau minimum requis en maçonnerie pour les fortifications est de 2.  

Si l'unité a un niveau 2 en maçonnerie, elle commence avec 40 points de production, dont 10 sont nécessaires pour une fortification.  
Elle peut ensuite utiliser les 30 points de production restants pour améliorer la fortification dans le même tour.  
Cependant, un talent minimum de 2 signifie également que 2 points de production doivent être dépensés par pierre.  
Ainsi, la fortification augmente de 15 pierres et une fortification de taille 25 est construite à la fin de la semaine.  

Avec le niveau de compétence 2, les bâtisseurs vont, en l'espace de 2 tours supplémentaires, agrandir la fortification jusqu'à la taille 50, créant ainsi une tour (Tower) qu'ils ne pourront pas agrandir en raison du niveau minimal de 3 requis.  

## Aperçu

Construction de châteaux : type, niveau minimum de compétence en maçonnerie, bonus salaire (en silvers), part du commerce et bonus de défense.  

| Type              | Niv. | Bonus salaire | Part commerce | Bonus Défense |
|-------------------|-----:|--------------:|--------------:|--------------:|
| Fondation         |    1 |            -- |            -- |             0 |
| Poste de commerce |    1 |            -- |            6% |             0 |
| Fortification     |    2 |      1 silver |           12% |            +1 |
| Tour              |    3 |      2 silver |           18% |            +2 |
| Bastion           |    4 |      3 silver |           24% |            +3 |
| Forteresse        |    5 |      4 silver |           30% |            +4 |
| Citadelle         |    6 |      5 silver |           36% |            +5 |

## Voir aussi

- [[batiments-speciaux]]
- [[batiments]]
- [bonus et malus][bonus-et-malus]
- [revenus][revenus]

Poursuivre la lecture : [[batiments-speciaux]].

<!-- From [https://wiki.eressea.de/index.php?title=Burg/fr&oldid=14498] -->
