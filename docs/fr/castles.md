# Château

Les châteaux augmentent les revenus des paysans, permettent d'échanger des produits de luxe et, enfin, offrent à leurs occupants une protection en cas d'attaque. Ils réduisent également la probabilité de [peste]. Les châteaux sont construits en pierre à l'aide de la commande [MAKE CASTLE] et de la compétence Masonry. La taille à partir de laquelle un château entre dans une nouvelle catégorie est indiquée dans le tableau ci-dessous. Plus le château est grand, plus il est difficile de l'agrandir. Pour continuer à construire un château, vous devez avoir au moins la compétence Maçonnerie au niveau requis. Chaque unité dispose de points de production (PP) à chaque tour : (niveau de compétence) x (nombre de personnes). Chaque semaine, l'unité agrandit le bâtiment de PP/(niveau de compétence requis) pierres. Les pierres nécessaires doivent également être disponibles. Vous pouvez facilement construire une tour en une semaine avec une unité suffisamment grande et compétente et suffisamment de pierres.

Les châteaux ont aussi des numéros (ID), utilisés pour les ordres. Voici un exemple de château :

Grand temple du chat aux yeux d'or (58), taille 58, tour ; Le temple brille d'un blanc éclatant au soleil, encadré par le vert délicat des arbres du parc. La tour élancée, qui s'élève au-dessus de la ville, est visible de loin. Au nord du temple, la ville de Xontormia s'étend le long du Whyren, enjambée un gigantesque pont près du port.

Les unités dans châteaux sont protégées, à savoir qu'une personne est protégée par unité de taille du château. Seules les personnes protégées bénéficient du bonus qu'un château donne à ses occupants en cas de raid (pour plus d'informations, voir le chapitre [guerre], en particulier la liste des [bonus et malus]). Chaque unité de taille du château nécessite une pierre.

Un plus grand château améliore le revenu de la population : tous les ouvriers et paysans bénéficient d'un bonus lorsqu'ils travaillent, qui dépend de la taille du plus grand château dans une région (voir aussi [tableau du bas]), de plus le propriétaire du plus grand château reçoit une part du produit des ventes des autres joueurs.

## Exemple

- L'unité "Thors Baumeister" est composée de 20 personnes ayant Masonry niveau 1 et dispose de 100 pierres. En raison de son niveau de compétence et du nombre de personnes de l'unité, elle dispose de 20 points de production (PP). Cela lui permet de construire PP/(niveau requis) unités de taille du chateau chaque semaine.

- Lorsque cette unité commence à construire un nouveau château, elle peut construire 10 unités de taille au premier tour : pour les fondations et le tradepost, le niveau minimal en masonry est de 1 ; pour construire une unité de taille, il faut un point de production, donc l'unité construit d'abord le tradepost jusqu'à la taille 10, ce qui fait de ce bâtiment une fortification. Il reste alors 10 points de production, mais ils sont perdus parce que le niveau minimum requis en masonry pour les fortifications est de 2.

- Si l'unité a un niveau 2 en masonry, elle commence avec 40 points de production, dont 10 sont nécessaires pour une fortification. Elle peut ensuite utiliser les 30 points de production restants pour améliorer la fortification dans le même tour. Cependant, un talent minimum de 2 signifie également que 2 points de production doivent être dépensés par pierre. Ainsi, la fortification augmente de 15 pierres et une fortification de taille 25 est construite à la fin de la semaine.

- Avec le niveau de compétence 2, les bâtisseurs vont, en l'espace de 2 tours supplémentaires, agrandir la fortification jusqu'à la taille 50, créant ainsi une tour (Tower) qu'ils ne pourront pas agrandir en raison du niveau minimal de 3 requis.

## Aperçu

Construction de châteaux - matériaux, minimum skill, bonus salaire, part du commerce et défense

| Type          | Taille min | Masonry min | Bonus salaire | Part commerce | Bonus Défense |
|---------------|------------|-------------|---------------|---------------|---------------|
| Foundation    | 1          | 1           | 0 Silber      | rien          | 0             |
| Tradepost     | 2          | 1           | 0 Silber      | 6%            | 0             |
| Fortification | 10         | 2           | 1 Silber      | 12%           | +1            |
| Tower         | 50         | 3           | 2 Silver      | 18%           | +2            |
| Stronghold    | 250        | 4           | 3 Silber      | 24%           | +3            |
| Fortress      | 1250       | 5           | 4 Silber      | 30%           | +4            |
| Citadel       | 6250       | 6           | 5 Silber      | 36%           | +5            |

## Voir aussi

- [bâtiments spéciaux]
- [bâtiments]
- [bonus et malus]
- [revenus]

|--------------|--------------------------------------------------------------|
| En savoir plus : | [bâtiments spéciaux](./buildings-others.md "Andere Gebäude") |

<!-- From [https://wiki.eressea.de/index.php?title=Burg/fr&oldid=14498] -->

[peste]: ./pest.md "Pest (Seite nicht vorhanden)"
[MAKE CASTLE]: ./cmd-make.md "MAKE"
[guerre]: ./war.md "Guerre"
[bonus et malus]: ./war.md#boni-und-mali "Boni und Mali"
[tableau du bas]: #aperçu
[bâtiments spéciaux]: ./buildings-others.md "Andere Gebäude"
[bâtiments]: ./buildings.md "Gebäude"
[revenus]: ./silver.md#einnahmen "Einnahmen"
