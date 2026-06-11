---
# cSpell:locale fr
alias: cmd-promote-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD041 MD042 MD052 -->

[](){ #cmd-promote-fr-id }

# PROMOTE

**`PROMOTE`**  

Promeut une unité de votre propre race de faction au statut de **Héros**.  

Les héros sont particulièrement forts en [combat][guerre].  
**Ils attaquent 5 fois à chaque round de combat**.  
C'est pourquoi il vaut la peine de promouvoir les unités dotées de compétences de combat au statut de héros.  

!!! note
    Un Héros **n'attaque pas plus souvent** avec de la magie, des arbalètes ou des catapultes.

<!-- TODO: which cost exactly ? -->
Le coût de la promotion en tant que Héros d'une unité dépend du nombre total de personnes de la faction.  
Comme d'habitude, l'argent manquant sera retiré de la [réserve d'argent][reserve-dargent] lorsqu'il y en a suffisamment.  

Le nombre maximum de héros est limité, mais augmente avec la taille de la faction.  
La formule pour cela est : log10((taille de la faction-500)÷50)×20.  

Seules les personnes de votre propre race peuvent être promues (donc ni les monstres ni les migrants).  
Le transport s'effectue selon `RECRUIT`.  
Le nombre de personnes après recrutement dans la semaine en cours est utilisé à la fois pour déterminer le nombre de héros possibles et les coûts de promotions.  

Les unités qui ont été promues ne peuvent pas recruter de personnes supplémentaires et ne peuvent pas être fusionnées avec d'autres unités non-héros.  
Il n’y a aucun ordre pour rétrograder un Héros.  

Pour ceux qui sont paresseux en maths, voici un tableau indiquant combien de Héros sont disponibles dans la faction.  

| Personnes | 557 | 563 | 571 | 580 | 589 | 600 | 612 | 626 | 641 | 659 | 678 | 700 | 724 | 751 | 782 | 816 | 854 | 898 | 946 | 1000 |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:----:|
| Héros     |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  |  20  |

| Personnes | 1062 | 1130 | 1207 | 1293 | 1390 | 1498 | 1620 | 1756 | 1910 | 2082 | 3312 | 5500 | 9392 | 16312 | 28618 | 50500 | 89414 | 158614 | 281671 | 500500 | ... |
|-----------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:-----:|:-----:|:-----:|:-----:|:------:|:------:|:------:|:---:|
| Héros     |  21  |  22  |  23  |  24  |  25  |  26  |  27  |  28  |  29  |  30  |  35  |  40  |  45  |  50   |  55   |  60   |  65   |   70   |   75   |   80   | ... |

<!-- From [https://wiki.eressea.de/index.php?title=PROMOTE&oldid=16056] -->
