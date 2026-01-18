---
# cSpell:locale fr
alias: naviguer
---
# Naviguer

Seuls les [[bateaux]] permettent de quitter son île et ainsi, par exemple, d'ouvrir de nouveaux marchés ou d'établir un contact direct avec d'autres factions.  
Avec un bateau, on peut naviguer jusqu'à 7 régions, et même plus loin avec des capitaines aquariens ou de la magie.  

Tous les bateaux plus grands qu'un boat (et cela inclut les longboats) ne peuvent accoster que dans les plaines et les forêts.  
Tous les autres types de régions (par exemple les montagnes, les highlands, les marais, etc.) ont besoin d'un [**Port**] pour que les bateaux puissent accoster.  
Si un bateau tente d'accoster dans une région inappropriée, il subit des [dommages].  
Les bateaux peuvent cependant appareiller n'importe où, on peut donc construire des bateaux dans toutes les régions côtières et les mettre à l'eau.  

Les bateaux ne peuvent pas passer directement d'une côte à une région côtière voisine sans naviguer d'abord sur une région océanique.  
De même, ils ne peuvent pas partir dans toutes les directions, mais seulement dans la direction d'où ils sont venus et dans les directions voisines.  
Un bateau venant de l'est (le rapport indique alors "côte est") peut donc partir vers l'est, le nord-est et le sud-est.  
Cependant, si une région dispose d'un port, les bateaux du propriétaire du port et des factions amies (voir [[cmd-help]]) peuvent aller dans d'autres directions à condition qu'il s'agisse de régions océaniques.  

En haute mer - cad des régions océaniques qui ne sont pas bordées par une région terrestre - les bateaux peuvent dériver vers une région voisine et subir des dommages à cause de tempêtes.  
Cela ne s'applique pas aux bateaux qui ordonnent des [[cmd-follow]] ou [Piraterie].  

Pour pouvoir naviguer sur un bateau, il faut un équipage formé, c'est-à-dire des unités qui ont appris la compétence sailing.  
Dans le tableau suivant, le niveau de compétence en sailing du capitaine (la première unité sur le bateau dans le rapport) est indiqué sous "Capitaine".  
De plus, il faut un certain niveau global en sailing pour piloter le bateau.  
Pour cela, les niveaux de compétence sailing de toutes les personnes à bord sont additionnés, y compris ceux de l'unité du capitaine et des unités de factions "étrangères".  
La valeur requise est indiquée dans le tableau sous "Équipage".  
La portée indiquée dans le tableau est valable par tour, c'est-à-dire qu'un bateau peut naviguer au maximum de cette distance par tour.  
Les bateaux pilotés par une unité d'aquariens d'une faction d'aquariens (les aquariens migrants d'une faction d'humains ne comptent donc pas) peuvent naviguer d'une case de plus.  

**Exemple :**

- Une trirème peut être pilotée par une unité de 30 personnes avec sailing 4 ou par une unité d'une personne de niveau 4 et une unité de 58 personnes de niveau 2.
  Dans tous les cas, elle navigue sur 7 régions par tour (8 pour les aquariens) et peut emporter 2000 kg, dont le poids de l'équipage est bien sûr déduit.
- Un dragonship avec une unité de 25 personnes de niveau 2 se déplace 5 régions.
  Cependant, avec 3 personnes de niveau 20, il peut se déplacer de 7 régions.

Bateau - Portée, Capacité, Compétence

| Type      | Portée | Capacité | Capitaine/Équipage | Niveau en Shipcraft | Qté de bois |
|-----------|:------:|---------:|-------------------:|:-------------------:|------------:|
| Barque    |   2    |       50 |            1 /   2 |          1          |           5 |
| Chaloupe  |   3    |      500 |            1 /  10 |          1          |          50 |
| Drakkar   | 5[^1]  |    1 000 |            2 /  50 |          2          |         100 |
| Caravelle |   5    |    3 000 |            3 /  30 |          3          |         250 |
| Trirème   |   7    |    2 000 |            4 / 120 |          4          |         200 |
| Galion    |   5    |   20 000 |        5 / 250[^2] |          5          |       2 000 |

[^1]: la portée d'un Drakkar dépend du niveau du capitaine.
[^2]: lorsque l'on calcule le niveau total de l'équipage d'un Galioon, seuls les marins min. T2 comptent.

Portée d'un drakkar.

| Capitaine | 2 | 6 | 18 | 54 | 162 |
|-----------|:-:|:-:|:--:|:--:|:---:|
| Portée    | 5 | 6 | 7  | 8  |  9  |

Si un bateau n'est pas doté d'un équipage suffisant, il ne peut pas appareiller.  
Si cela se produit en mer (par exemple à cause d'un combat ou d'unités affamées par manque d'argent), il dérive jusqu'à ce qu'il touche une région côtière.  
Il subit alors chaque tour des [dommages], si bien qu'il coule rapidement.  

Le poids total de toutes les unités d'un bateau, y compris le poids des chevaux, des voitures, des personnes et, bien sûr, de toutes les marchandises et de l'argent des unités, doit pouvoir être supporté par le bateau.  
Si ce n'est pas ou plus le cas, le bateau ne peut pas naviguer.  
En mer, il ne coulera pas immédiatement, mais dérivera.  
Les capacités des bateaux sont indiquées dans le tableau ci-dessus et sont toujours affichées dans le rapport.  
Les poids des objets se trouvent dans la section sur [[objets]] et ceux des personnes des différentes races, dans le tableau [[deplacements|Poids et Capacités]].  

Il est possible de regrouper plusieurs bateaux en [convoi].  
Les détails à ce sujet sont décrits dans le chapitre sur les [[bateaux]].  

Les unités qui se trouvent à bord d'un bateau ne sont peuvent exécuter d'ordres longs (à l'exception des aquariens).  
Seul le capitaine d'un bateau peut donner des ordres de [[cmd-move]] ou [[cmd-route]] pour faire naviguer le bateau.  
Sur une case d'océan (type de région océan) jusqu'à 100 aquariens embarqués peuvent gagner 10 Silver chacun avec l'ordre [[cmd-work]].  
Néanmoins, toutes les unités à bord du bateau consomment l'entretien hebdomadaire, il faut donc toujours embarquer suffisamment de Silver.  

Lorsque le bateau est à terre, toutes les unités à bord peuvent faire quelque chose ; elles vont pour ainsi dire à terre pour travailler.  
Elles peuvent le faire même si le bateau part au cours du même tour.  
Mais si la région est gardée par une faction non alliée, en addition aux conséquences habituelles de l'ordre GUARD, elles ne peuvent pas non plus [[argent|gagner d'argent]] avec `WORK`, `ENTERTAIN` ou `SELL`, comme elles pourraient le faire autrement.  

Si des unités veulent quitter un bateau, elles doivent d'abord le faire avec [[cmd-leave]].  
Si la région n'est pas gardée par une faction non alliée, les unités peuvent se déplacer immédiatement avec MOVE, sinon elles ne pourront le faire qu'au tour suivant l'ordre LEAVE.  
Cela s'applique bien sûr aussi à [[cmd-ride]] et [[cmd-carry]].  

## Nager

Les [aquariens] peuvent nager jusqu'à terre à partir d'un bateau qui se trouve dans une région océanique à côté de régions terrestres, mais pas l'inverse.  
Cela fonctionne comme un mouvement normal avec [[cmd-move]] et seulement si l'unité n'est pas surchargée.  
Ils peuvent emporter des objets, mais pas de chevaux, même si l'unité qui nage peut les porter.  
De même [[cmd-carry|transporter]] des personnes d'autres races n'est pas possible de cette manière, mais les aquariens peuvent se transporter mutuellement.  
Ce mouvement a lieu avant celui des bateaux, de sorte qu'un bateau peut déposer des unités puis poursuivre sa route.  
[[cmd-leave]] n'est pas nécessaire lorsque l'on nage à partir d'un bateau, mais ce n'est même pas une erreur.  

## Dommages aux bateaux

Un voyage maritime est dangereux et en haute mer les bateaux peuvent être endommagés durant leur traversée par des tempêtes, des évènements naturels ou même des créatures des profondeurs (ou aussi par manque d'équipage).  

Les dégâts sont exprimés en pourcentage et réduisent la capacité en proportion des dégâts indiqués ; on arrondit vers le bas.  
La portée, y compris tous les bonus d'accélération (aquarien, artefacts, sorts), est également réduite en proportion ; mais dans ce cas, on arrondit toujours vers le haut.  

Exemple : Un bateau avec une capitaine aquarien est endommagé à 17 %.  

- La capacité est donc réduite (50 x 0,83 = 41,5 arrondir vers le bas) à 41 kg
- La portée (1 + 2 x 0,83 = 2,49 arrondir à l'unité supérieure) reste donc à 3

Si un bateau subit 100% de dégâts, il coule avec son équipage et ses passagers.  

Lors des événements suivants, un bateau subit des dommages :

- le bateau est engagé dans un combat : 0%-20% de dommages (voir [combat naval])
- le bateau est endommagé par un sort puissant (jusqu'à 90 %)
- le bateau subit des dommages à cause des raz-de-marée (50 %)
- si le bateau heurte des écueils, il subit 10% de dégâts (heurter des écueils : tenter d'accoster dans une région inadaptée)
- en mer avec un équipage insuffisant, 30 % de dommages
- si le bateau est sans propriétaire, il subit 5% de dommages
- Si le bateau dérive (comme suite à une tempête), il subit 2 % de dommages

Un bateau peut être réparé avec l'ordre [[cmd-make|`MAKE`&nbsp;&#91;`level`&#93;&nbsp;`SHIP`&nbsp;&#91;`ship id`&#93;]], exactement comme lorsque sa construction n'était pas encore achevée.  

Expérience de jeu :

Le bateau a dérivé dans une tempête; que s'est-il passé ?

Les bateaux voyagent le long des côtes ou en pleine mer.

- Tant qu’un bateau voyage uniquement dans les régions côtières, il ne sera jamais pris dans une tempête et ne dérivera jamais
- Si un bateau traverse des régions de haute mer (indépendamment des régions de départ et de destination), il peut être pris dans une tempête et dériver.
  Il est ensuite poussé aléatoirement sur une région voisine, puis effectue les déplacements restants
- Si un bateau dérive, il subit toujours 2 % de dégâts sans exception

## Voir aussi

- [[deplacements]]
- [[bateaux]]

Poursuivre la lecture : [[production]].

<!-- From [https://wiki.eressea.de/index.php?title=Schiffsreise/fr&oldid=15810] -->

[**Port**]: ./buildings-others.md#port
[dommages]: #dommages-aux-bateaux
[Piraterie]: ./war.md#piraterie
[convoi]: ./ships.md#convoi
[aquariens]: ./races.md#aquariens
[combat naval]: ./war.md#combats-a-bord-et-depuis-les-navires
