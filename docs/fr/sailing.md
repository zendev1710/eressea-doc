# Naviguer

Seuls les [bateaux] permettent de quitter son île et ainsi, par exemple, d'ouvrir de nouveaux marchés ou d'établir un contact direct avec d'autres factions. Avec un bateau, on peut naviguer jusqu'à 7 régions, et même plus loin avec des capitaines aquariens ou de la magie.

Tous les bateaux plus grands qu'un boat (et cela inclut les longboats) ne peuvent accoster que dans les plaines et les forêts. Tous les autres types de régions (par exemple les montagnes, les highlands, les marais, etc.) ont besoin d'un [**Port**] pour que les bateaux puissent accoster. Si un bateau tente d'accoster dans une région inappropriée, il subit des [dommages]. Les bateaux peuvent cependant appareiller n'importe où, on peut donc construire des bateaux dans toutes les régions côtières et les mettre à l'eau.

Les bateaux ne peuvent pas passer directement d'une côte à une région côtière voisine sans naviguer d'abord sur une région océanique. De même, ils ne peuvent pas partir dans toutes les directions, mais seulement dans la direction d'où ils sont venus et dans les directions voisines. Un bateau venant de l'est (le rapport indique alors "côte est") peut donc partir vers l'est, le nord-est et le sud-est. Cependant, si une région dispose d'un port, les bateaux du propriétaire du port et des factions amies (voir [HELP]) peuvent aller dans d'autres directions à condition qu'il s'agisse de régions océaniques.

En haute mer - cad des régions océaniques qui ne sont pas bordées par une région terrestre - les bateaux peuvent dériver vers une région voisine et subir des dommages à cause de tempêtes. Cela ne s'applique pas aux bateaux qui ordonnent des [FOLLOW] ou [Piraterie].

Pour pouvoir naviguer sur un bateau, il faut un équipage formé, c'est-à-dire des unités qui ont appris la compétence sailing. Dans le tableau suivant, le niveau de compétence en sailing du capitaine (la première unité sur le bateau dans le rapport) est indiqué sous "Capitaine". De plus, il faut un certain niveau global en sailing pour piloter le bateau. Pour cela, les niveaux de compétence sailing de toutes les personnes à bord sont additionnés, y compris ceux de l'unité du capitaine et des unités de factions "étrangères". La valeur requise est indiquée dans le tableau sous "Équipage". La portée indiquée dans le tableau est valable par tour, c'est-à-dire qu'un bateau peut naviguer au maximum de cette distance par tour. Les bateaux pilotés par une unité d'aquariens d'une faction d'aquariens (les aquariens migrants d'une faction d'humains ne comptent donc pas) peuvent naviguer d'une case de plus.

**Exemple:**

- Une trirème peut être pilotée par une unité de 30 personnes avec sailing 4 ou par une unité d'une personne de niveau 4 et une unité de 58 personnes de niveau 2. Dans tous les cas, elle navigue sur 7 régions par tour (8 pour les aquariens) et peut emporter 2000 GE, dont le poids de l'équipage est bien sûr déduit.
- Un dragonship avec une unité de 25 personnes de niveau 2 se déplace 5 régions. Cependant, avec 3 personnes de niveau 20, il peut se déplacer de 7 régions.

Bateau - Portée, Capacité, Compétence

|            |        |          |                    |                     |                  |
|------------|--------|----------|--------------------|---------------------|------------------|
| Type       | Portée | Capacité | Capitaine/Equipage | Niveau en Shipcraft | Quantité de bois |
| Boat       | 2      | 50       | 1/2                | 1                   | 5                |
| Longboat   | 3      | 500      | 1/10               | 1                   | 50               |
| Dragonship | 5\*    | 1000     | 2/50               | 2                   | 100              |
| Caravel    | 5      | 3000     | 3/30               | 3                   | 250              |
| Trireme    | 7      | 2000     | 4/120              | 4                   | 200              |
| Galleon    | 5      | 20000    | 5/250\*\*          | 5                   | 2000             |

\* La portée d'un Dragonship dépend du niveau du capitaine.

\*\* Lorsque l'on calcule le niveau total de l'équipage d'un Galleon, seuls les marins min. T2 comptent.

Portée d'un Dragonship

|           |   |   |    |    |     |
|-----------|---|---|----|----|-----|
| Capitaine | 2 | 6 | 18 | 54 | 162 |
| Portée    | 5 | 6 | 7  | 8  | 9   |

Si un navire n'est pas doté d'un équipage suffisant, il ne peut pas appareiller. Si cela se produit en mer (par exemple à cause d'un combat ou d'unités affamées par manque d'argent), il dérive jusqu'à ce qu'il touche une région côtière. Il subit alors chaque tour des [dommages], si bien qu'il coule rapidement.

Le poids total de toutes les unités d'un bateau, y compris le poids des chevaux, des voitures, des personnes et, bien sûr, de toutes les marchandises et de l'argent des unités, doit pouvoir être supporté par le bateau. Si ce n'est pas ou plus le cas, le bateau ne peut pas naviguer. En mer, il ne coulera pas immédiatement, mais dérivera. Les capacités des bateaux sont indiquées dans le tableau ci-dessus et sont toujours affichées dans le rapport. Les poids des objets se trouvent dans la section sur [objets] et ceux des personnes des différentes races, dans le tableau [Poids et Capacités].

Il est possible de regrouper plusieurs navires en [convoi]. Les détails à ce sujet sont décrits dans le chapitre sur les [bateaux][1].

Les unités qui se trouvent à bord d'un navire ne sont peuvent exécuter d'ordres longs (à l'exception des aquariens). Seul le capitaine d'un navire peut donner des ordres de [MOVE] ou [ROUTE] pour faire naviguer le navire. Sur une case d'océan (type de région océan) jusqu'à 100 aquariens embarqués peuvent gagner 10 Silver chacun avec l'ordre [`WORK`]. Néanmoins, toutes les unités à bord du navire consomment l'entretien hebdomadaire, il faut donc toujours embarquer suffisamment de Silver.

Lorsque le bateau est à terre, toutes les unités à bord peuvent faire quelque chose ; elles vont pour ainsi dire à terre pour travailler. Elles peuvent le faire même si le navire part au cours du même tour. Mais si la région est gardée par une faction non alliée, en addition aux conséquences habituelles de l'ordre GUARD, elles ne peuvent pas non plus [gagner d'argent] avec WORK, ENTERTAIN ou SELL, comme elles pourraient le faire autrement.

Si des unités veulent quitter un navire, elles doivent d'abord le faire avec [LEAVE]. Si la région n'est pas gardée par une faction non alliée, les unités peuvent se déplacer immédiatement avec MOVE, sinon elles ne pourront le faire qu'au tour suivant l'ordre LEAVE. Cela s'applique bien sûr aussi à [RIDE] et [CARRY].

## Nager

Les [aquariens] peuvent nager jusqu'à terre à partir d'un navire qui se trouve dans une région océanique à côté de régions terrestres, mais pas l'inverse. Cela fonctionne comme un mouvement normal avec [`MOVE`][MOVE] et seulement si l'unité n'est pas surchargée. Ils peuvent emporter des objets, mais pas de chevaux, même si l'unité qui nage peut les porter. De même [transporter][CARRY] des personnes d'autres races n'est pas possible de cette manière, mais les aquariens peuvent se transporter mutuellement. Ce mouvement a lieu avant celui des navires, de sorte qu'un navire peut déposer des unités puis poursuivre sa route. [LEAVE] n'est pas nécessaire lorsque l'on nage à partir d'un navire, mais ce n'est même pas une erreur.

## Dommages aux bateaux

Un voyage maritime est dangereux et en haute mer les navires peuvent être endommagés durant leur traversée par des tempêtes, des évènements naturels ou même des créatures des profondeurs (ou aussi par manque d'équipage).

Les dégâts sont exprimés en pourcentage et réduisent la capacité en proportion des dégâts indiqués ; on arrondit vers le bas. La portée, y compris tous les bonus d'accélération (aquarien, artefacts, sorts), est également réduite en proportion ; mais dans ce cas, on arrondit toujours vers le haut.

Exemple : Un bateau avec une capitaine aquarien est endommagé à 17%.

- La capacité est donc réduite (50 \* 0,83 = 41,5 arrondir vers le bas) à 41 GE.
- La portée (1 + 2 \* 0,83 = 2,49 arrondir à l'unité supérieure) reste donc à 3.

Si un navire subit 100% de dégâts, il coule avec son équipage et ses passagers.

Lors des événements suivants, un bateau subit des dommages :

- le navire est engagé dans un combat : 0%-20% de dommages (voir [combat naval])
- le navire est endommagé par un sort puissant (jusqu'à 90%)
- le bateau subit des dommages à cause des raz-de-marée (50%)
- si le navire heurte des écueils, il subit 10% de dégâts (heurter des écueils : tenter d'accoster dans une région inadaptée)
- en mer avec un équipage insuffisant, 30% de dommages.
- si le bateau est sans propriétaire, il subit 5% de dommages
- Si le navire dérive (comme suite à une tempête), il subit 2% de dommages.

On peut réparer un bateau avec [`MAKE [`*`niveau`*`] SHIP [`*`ship-ID`*`]`][2], exactement comme si le bateau n'était pas encore terminé.

Expérience de jeu : Ship drifted in a storm; what happened?
  
Ships travel over coasts (ocean hexes with at least one adjacent land hex) or over open sea (ocean with only adjacent water hexes).

- As long as a ship only travels in coastal regions it will never get caught in a storm and it will never drift away.
- If a ship is crossing open sea hexes (this is independent of the start and destination region), it may get caught in a storm and drift away. It is then pushed to the side (random) and then carries out the remaining movements.
- If a ship drifts away, it always suffers 2% damage without exception.

## Voir aussi

- [déplacement]
- [bateaux]

|              |              |
|--------------|--------------|
| Weiterlesen: | [Produktion] |

[Produktion]: ./production.md "Produktion"

<!-- From [https://wiki.eressea.de/index.php?title=Schiffsreise/fr&oldid=15810] -->

[bateaux]: ./ships.md "Schiff"
[**Port**]: ./buildings-others.md#Hafen "Andere Gebäude"
[dommages]: #schiffsschaden
[HELP]: ./cmd-help.md "HELP"
[FOLLOW]: ./cmd-follow.md "FOLLOW"
[Piraterie]: ./war.md#Piraterie "Guerre"
[objets]: ./items.md#Getenständen "Waren"
[Poids et Capacités]: ./travel.md#Rassengewichte "Reisen"
[convoi]: ./ships.mde#Konvoi "Schiffe"
[1]: ./ships.mde "Schiffe"
[MOVE]: ./cmd-move.md "MOVE"
[ROUTE]: ./cmd-route.md "ROUTE"
[`WORK`]: ./cmd-work.md "WORK"
[gagner d'argent]: ./silver.md "Argent"
[LEAVE]: ./cmd-leave.md "LEAVE"
[RIDE]: ./cmd-ride.md "RIDE"
[CARRY]: ./cmd-carry.md "CARRY"
[aquariens]: ./races.md#meermenschen "Meermenschen"
[combat naval]: ./war.md#kampf-auf-und-von-schiffen "Kampf auf Schiffen"
[2]: ./cmd-make.md "MAKE"
[déplacement]: ./travel.md "Reisen"
