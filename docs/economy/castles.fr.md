---
# cSpell:locale fr
alias: chateaux
---

# Châteaux

Les châteaux augmentent les revenus des paysans, permettent d'échanger des biens de luxe et offrent à leurs occupants une protection en cas d'attaque.  
Ils réduisent également la probabilité de [peste][peste].  

Les châteaux sont construits en pierres à l'aide de l'ordre [`MAKE CASTLE`][cmd-make-fr] par des unités maîtrisant la [maçonnerie][maconnerie]{title="Masonry"}.  
Un château entre dans une nouvelle catégorie selon sa taille :

*Taille d'un château selon son type.*

| Fondation | Comptoir commercial | Fortification | Tower | Bastion | Forteresse | Citadelle |
|:---------:|:-------------------:|:-------------:|:-----:|:-------:|:----------:|:---------:|
|     1     |          2          |      10       |  50   |   250   |   1 250    |  6 250+   |

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
Au nord du temple, la ville de Xontormia s'étend le long du Whyren, enjambée par un gigantesque pont près du port.
```

Les unités dans un château sont protégées, à savoir qu'une personne est protégée par unité de taille du château.  
Seules les personnes protégées bénéficient du bonus qu'un château donne à ses occupants en cas de raid.  
Plus d'informations :

- [la guerre][guerre]
- [bonus et malus][bonus-et-malus]

Chaque unité de taille du château nécessite une pierre.  

Un plus grand château améliore le revenu de la population : tous les ouvriers et paysans bénéficient d'un bonus lorsqu'ils travaillent, qui dépend de la taille du plus grand château dans une région (voir aussi [tableau du bas][chateaux-tableau-synthese-fr-id]), de plus le propriétaire du plus grand château reçoit une part du produit des ventes des autres joueurs.  

## Construction - Exemples

L'unité "Thors Baumeister" est composée de 20 maçons T1 disposant de 100 pierres.  
En raison de son niveau de compétence et du nombre de personnes de l'unité, elle dispose de 20 points de production (PP).  
Cela lui permet de construire `PP / <niveau requis>` unités de taille du château à chaque tour.  

Lorsque cette unité commence à construire un nouveau château, elle peut construire 10 unités de taille au premier tour : pour les fondations et le comptoir commercial, le niveau minimal en maçonnerie est de 1;  
pour construire une unité de taille, il faut un point de production, donc l'unité construit d'abord le comptoir commercial jusqu'à la taille 10, ce qui fait de ce bâtiment une fortification.  
Il reste alors 10 points de production, mais ils sont perdus parce que le niveau minimum requis en maçonnerie pour les fortifications est de 2.  

Si l'unité a un niveau 2 en maçonnerie, elle commence avec 40 points de production, dont 10 sont nécessaires pour une fortification.  
Elle peut alors utiliser les 30 points de production restants pour améliorer la fortification dans le même tour.  
Cependant, un niveau minimum de 2 signifie également que 2 points de production doivent être dépensés par pierre.  
Ainsi, la fortification augmente de 15 pierres et une fortification de taille 25 est construite à la fin de la semaine.  

Avec le niveau de compétence 2, les bâtisseurs vont, en l'espace de 2 tours supplémentaires, agrandir la fortification jusqu'à la taille 50, créant ainsi une tour (Tower) qu'ils ne pourront pas agrandir en raison du niveau minimal de 3 requis.  

## Fondation

<!-- cspell:disable -->
*Foundation (EN), Grundmauern (DE)*.
<!-- cspell:enable -->

Château de taille 1.  
Il faut être maçon T1 pour débuter la construction d'une fondation.  

Une fondation ne procure aucun avantage réel. Il est conseillé d'augmenter la taille du château dès que possible.  

## Comptoir commercial

<!-- cspell:disable -->
*Tradepost (EN), Handelsposten (DE)*.
<!-- cspell:enable -->

Château de taille 2 à 9.  
Il faut être maçon T1 pour bâtir un poste de commerce.  

Les [marchands][skill-commerce-id] peuvent pratiquer le [négoce][commerce-des-biens-de-luxe-id] dans la région.  
Les marchands bénéficient d'une part de commerce de 6 %.  

## Fortification

<!-- cspell:disable -->
*Fortification (EN), Befestigung (DE)*.
<!-- cspell:enable -->

Château de taille 10 à 49.  
Il faut être maçon T2 pour bâtir une fortification.  

Les unités occupant la fortification bénéficient d'un bonus de défense de +1.  
Le salaire de base des unités et paysans de la région est augmenté d'1 silver.  
Les marchands bénéficient d'une part de commerce de 12 %.  

## Tour

<!-- cspell:disable -->
*Tower (EN), Turm (DE)*.
<!-- cspell:enable -->

Château de taille 50 à 249.  
Il faut être maçon T3 pour bâtir une tour.  

Les unités occupant la tour bénéficient d'un bonus de défense de +2.  
Le salaire de base des unités et paysans de la région est augmenté de 2 silvers.  
Les marchands bénéficient d'une part de commerce de 18 %.  

## Bastion

<!-- cspell:disable -->
*Stronghold (EN), Burg (DE)*.
<!-- cspell:enable -->

Château de taille 250 à 1249.  
Il faut être maçon T4 pour bâtir un bastion.  

Les unités occupant le bastion bénéficient d'un bonus de défense de +3.  
Le salaire de base des unités et paysans de la région est augmenté de 3 silvers.  
Les marchands bénéficient d'une part de commerce de 24 %.  

## Forteresse

<!-- cspell:disable -->
*Fortress (EN), Festung (DE)*.
<!-- cspell:enable -->

Château de taille 1250 à 6249.  
Il faut être maçon T5 pour bâtir une forteresse.  

Les unités occupant la forteresse bénéficient d'un bonus de défense de +4.  
Le salaire de base des unités et paysans de la région est augmenté de 4 silvers.  
Les marchands bénéficient d'une part de commerce de 30 %.  

## Citadelle

<!-- cspell:disable -->
*Citadel (EN), Zitadelle (DE)*.
<!-- cspell:enable -->

Château de taille 6250 ou plus.  
Il faut être maçon T6 pour bâtir une citadelle.  

Les unités occupant la citadelle bénéficient d'un bonus de défense de +5.  
Le salaire de base des unités et paysans de la région est augmenté de 5 silvers.  
Les marchands bénéficient d'une part de commerce de 36 %.  

[](){ #chateaux-tableau-synthese-fr-id }

## Châteaux - Tableau de synthèse

Le tableau ci-dessous définit pour chaque type de château :

- Le niveau minimum de compétence en maçonnerie pour le bâtir
- Le bonus de salaire
- La part du commerce
- Le bonus de défense

<div class="sortable" markdown="1">

| Type                | Niv. | Bonus salaire | Part commerce | Bonus Défense |
|---------------------|:----:|:-------------:|--------------:|:-------------:|
| Fondation           |  T1  |       -       |             - |       -       |
| Comptoir commercial |  T1  |       -       |           6 % |       -       |
| Fortification       |  T2  |  +1 silver    |          12 % |      +1       |
| Tour                |  T3  |  +2 silvers   |          18 % |      +2       |
| Bastion             |  T4  |  +3 silvers   |          24 % |      +3       |
| Forteresse          |  T5  |  +4 silvers   |          30 % |      +4       |
| Citadelle           |  T6  |  +5 silvers   |          36 % |      +5       |

</div>

## Voir aussi

- [Bâtiments spéciaux][batiments-speciaux]
- [Bâtiments][batiments-id]
- [bonus et malus][bonus-et-malus]
- [revenus][revenus]

Poursuivre la lecture : [bâtiments spéciaux][batiments-speciaux].

<!-- From [https://wiki.eressea.de/index.php?title=Burg/fr&oldid=14498] -->

[cmd-make-fr]: [[cmd-make-fr]]
