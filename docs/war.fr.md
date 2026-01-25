---
# cSpell:locale fr
alias: guerre
---
# Guerre

Les conflits sont inévitables dans Eressea.  
Il y aura des disputes pour l'argent, pour les régions, pour les droits de taxes, pour les routes commerciales et ainsi de suite.  
C'est pourquoi il faut toujours chercher des amis et des alliés, car "les amis vont et viennent, les ennemis se multiplient".  

## Les camps dans une bataille

L'ordre [[cmd-attack]]{title="ATTAQUER"}  permet de lancer l'attaque contre l'adversaire.  
Les ordres `ATTACK` sont exécutés dans un ordre aléatoire.  
Lors d'une attaque, les unités de tous les camps se rassemblent dans la région et se battent entre elles individuellement (personne par personne).  
Une bataille dure au maximum six tours : cinq tours de combat réguliers et éventuellement encore le tour 0 (zéro), le [tour de tactique].  

Le camp attaquant est constitué de toutes les unités qui ont donné des ordres `ATTACK` contre une ou plusieurs unités des défenseurs.  

Le camp des défenseurs est composé des unités qui ont été attaquées, sur qui l'adversaire a donc donné l'ordre `ATTACK`*`unité-id`*, et de toutes les unités de la faction agressée qui sont prêtes à combattre (donc celles en [[cmd-combat]]`,`[[cmd-combat|`COMBAT AGGRESSIVE`]]`,`[[cmd-combat|`COMBAT REAR`]] ou [[cmd-combat|`COMBAT DEFENSIVE`]]).  
De plus, toutes les unités prêtes au combat des factions alliées aux factions attaquées, c'est-à-dire celles qui ont mis [[cmd-help|`HELP COMBAT`]] avec la faction attaquée, apportent leur aide.

Il y a donc différentes raisons pour lesquelles une unité participe au combat.  
Celles-ci sont classées par ordre de priorité :

1. L'unité prête à combattre attaque une autre unité. Dans ce cas, elle participe au combat dans tous les cas.
2. L'unité est attaquée par une autre unité. Elle rejoint alors les [Lignes de combat] en fonction de son statut de combat.
3. Une unité dont la faction est attaquée. L'unité participe alors au combat si elle n'a pas mis `COMBAT NOT` ou `COMBAT FLEE`.
   Dans ce dernier cas, elle n'a pas l'idée de [fuir] puisqu'elle n'est pas directement menacée.
4. Une unité d'une faction alliée (donc une faction à laquelle on a mis `HELP COMBAT`) est attaquée par quelqu'un.
   L'unité participe alors au combat, à moins qu'elle n'ait mis `COMBAT NOT` ou `COMBAT FLEE`.
   Encore une fois, une unité avec `COMBAT FLEE` ne [s'enfuira] pas, car elle n'est pas exposée à une menace directe.

Les alliés n'aident donc automatiquement que les défenseurs et ***seulement si le défenseur n'a pas lui-même attaqué**.  
Les unités attaquées se défendent avec toutes les unités de la faction, à moins que celles-ci ne se tiennent explicitement à l'écart du combat.  
Pour l'attaquant, le statut de combat n'a pas d'importance : à part pour les défenseurs, seules les unités qui ont donné un ordre [[cmd-attack]] sont engagées dans le combat.  
Cependant, les unités qui ont mis [[cmd-combat|`COMBAT NOT`]] ou [[cmd-combat|`COMBAT FLEE`]] ne peuvent pas attaquer.

Ainsi, pour attaquer conjointement un ennemi, chaque faction attaquante doit attaquer au moins une unité de l'ennemi.  
Pour se défendre ensemble contre des assaillants, il suffit que les factions qui se défendent s'entraident (`HELP`).  

<!-- TODO: clarify -->
En théorie, toute unité à laquelle [`HELP COMBAT`] a été attribuée est considérée comme alliée.  
Est aussi considérée comme alliée une unité qui n'a attaqué aucune autre unité à qui [[cmd-help|`HELP COMBAT`]] a également été attribué.  

**Exemple 1 :**

A aide B et C.  
C attaque B, c'est pourquoi A intervient dans la bataille : B est allié.  
La faction C n'est pas considérée comme alliée parce qu'elle attaque un allié.  

Qui se bat contre qui maintenant ? Je me bats contre mes ennemis.  
Mes ennemis sont des factions qui m'attaquent, que j'attaque, ou qui attaquent un allié.

**Exemple 2:**

A aide B et C. B et C s'attaquent mutuellement.  
Dans ce cas, A n'aide ni B ni C, car aucun d'entre eux n'est considéré comme allié et aucun n'est un ennemi de A.  

**Exemple 3:**

A attaque B et C.  
Si B et C ne sont pas alliés, ils s'entraident quand même contre A, car A est un ennemi commun.  
Ainsi, si B a encore des troupes de front et que C n'a plus que des archers, les troupes de B se placent devant C pour le protéger.  
Exception : si B et C sont ennemis, parce que par exemple B combat un allié supplémentaire D de C, alors ils ne s'aident pas entre eux, même pas contre A.  

**Exemple 4:**

A et B attaquent C.  
Dans ce cas, ils s'entraident contre C (même s'ils ne sont pas alliés), puisqu'ils ont un ennemi commun.  

Expérience de jeu :

En fait, c'est encore un peu plus compliqué.  

**Attention :**
Des statuts d'aide ou des ordres `ATTACK` mal définis ont déjà donné lieu à des combats dont l'issue n'était pas celle attendue.  
Des alliés sont restés sans rien faire ou se sont même battus entre eux.  
Quelques astuces permettent d'éviter les plus grosses bourdes :

- Tu devrais régulièrement vérifier les statuts d'aide pour tous tes alliés.
  `HELP ALL` est préférable de pour tous ceux avec qui tu "pourrais" combattre.
  La méfiance fait souvent des dégâts à ce niveau.
- Si possible, il ne devrait y avoir qu'un seul [[cmd-group|groupe]].
- Dans ta faction, il faudrait que soit toutes les unités de combattants aient l'ordre `ATTACK`, soit aucune.
  Si seule une partie de tes unités attaque, il se peut que le reste ne participe pas au combat si un allié est attaqué.
- Il est conseillé d'attaquer toutes les unités ennemies.
  Tu devrais au moins attaquer une unité de chaque faction ennemie.
- Notez également que le camouflage des factions ne permet pas toujours de savoir qui appartient vraiment à quelle faction.
  Une autre stratégie pourrait consister à n'attaquer qu'une seule unité ennemie à la fois, en espérant que les statuts `HELP` de l'adversaire créent une certaine confusion.
  Nous ne jugerons pas ici si cette approche est honorable.

## Le combat

Une bataille dure cinq tours de combat, plus un éventuel tour de tactique.  
À chaque tour de combat, les combattants frappent dans un ordre aléatoire.  

Notez que les personnes participant à un combat ( les personnes listées dans le rapport de combat c'est-à-dire attaquées ou attaquantes) ne peuvent en principe pas exécuter d'autres ordres longs.  
Les exceptions sont [combat en mer] et les combats dans des régions qui, *au début du combat*, sont gardées par au moins une unité de sa propre faction ou qui a mis [`HELP GUARD`][`HELP COMBAT`] avec celle du combattant.  
Dans ce cas, d'autres ordres longs sont possibles.

### Lignes de combat

Durant la bataille, il y a quatre lignes de combat.  
Celles-ci ne sont composées que des unités qui participent réellement au combat (voir ci-dessus).  
Pour plus d'informations sur les statuts de combat, voir [[cmd-combat]][`COMBAT`].

1. ligne: Ici se trouvent toutes les unités qui ont mis [[cmd-combat]] ou [[cmd-combat|`COMBAT AGGRESSIVE`]].
2. ligne : Ici se trouvent toutes les unités qui ont mis [[cmd-combat|`COMBAT REAR`]] ou [[cmd-combat|`COMBAT DEFENSIVE`]].
3. ligne : Ici se trouvent toutes les unités qui ont mis [[cmd-combat|`COMBAT NOT`]].
4. ligne : C'est ici que se trouvent toutes les unités qui cherchent simplement à s'échapper.
   Donc celles qui ont mis [[cmd-combat|`COMBAT FLEE`]] et celles qui ont perdu un nombre approprié de Points de Vie (voir aussi [la fuite]).

Seules les deux premières lignes de combat participent activement au combat, c'est-à-dire qu'elles peuvent frapper, tirer et être touchées.  
Les unités qui ne sont pas combattantes et qui sont directement attaquées ne participent au combat que si la première ligne est débordée.  
Les unités en fuite tentent naturellement de s'échapper (voir [ici][la fuite]).  

Les unités qui combattent en 2eme ligne ne peuvent être attaquées directement au corps à corps que lorsqu'elles arrivent en première ligne (cela peut arriver par exemple lorsque la 1re ligne est débordée, voir ci-dessous).  
Contre les attaques à distance adverses, elles se défendent avec leur meilleure compétence de combat.

Les sorts de combat des mages peuvent être lancés de l'arrière et de la ligne de front ; cela mis à part, ils s'armeront et se battront comme tout le monde.

### Débordement

Si une faction et ses alliés ont plus de trois fois plus de personnes en première ligne que leurs adversaires, la 1ère rangée est débordée.  
Toutes les unités adverses de 2e ligne sont obligées de monter en première ligne.  
La 3e ligne remonte alors en 2e ligne et participe au combat.  
S'il n'y a toujours pas assez de personnes en 1ère ligne, les lignes suivantes remontent jusqu'à ce qu'il y ait suffisamment de personnes en 1ère ligne.  
Cette répartition est vérifiée avant chaque tour de combat.

## Aux armes (Éresséens)

Maintenant, les unités s'arment.  
Chaque personne d'une unité s'équipe en fonction de ses compétences d'une arme de corps à corps, d'une arme à distance et d'une armure.  
Elle privilégie les armes qui lui permettent d'obtenir le plus haut score en Attaque et Parade.  
Les mages qui ont choisi un sort de combat l'utilisent pour attaquer.  
Cependant, pour la défense, ils auront besoin d'une arme (et d'une compétence de combat appropriée), sinon ils seront considérés comme [non armés].  

**Attention:** les armes ou armures non utilisées ne sont pas automatiquement redistribuées aux unités non armées ou non équipées.

Pendant le combat, on ne change plus d'arme, sauf s'il est possible de prendre une meilleure arme à une personne de la même unité qui est déjà morte (les combattants survivants utilisent chacun les meilleurs sets d'armes disponibles).

Un combattant à distance qui soudain se retrouve en première ligne doit s'il est attaqué se saisir d'une arme de corps à corps (s'il en possède une et s'il a la compétence correspondante au moins au niveau 1), sinon il se défend [sans arme][non armés].

**Exemple :**

Une unité de 20 personnes dispose de 15 épées, 10 boucliers et 5 cottes de mailles.  
Alors 5 personnes se battront avec une épée, un bouclier et une cotte de mailles, 5 autres avec une épée et un bouclier, 5 avec une épée seulement et les 5 derniers combattants resteront sans armes.  
Une unité de 10 personnes avec 10 épées et 10 haches de guerre se battra avec des épées, car elles ont un meilleur bonus, même si elles infligent probablement moins de dégâts !

## Tour du tacticien

Avant la bataille, le meilleur [[tactique|Tacticien]] de toutes les unités participantes est désigné.  
Un tacticien qui se bat en première ligne reçoit un bonus de +1 à son niveau de compétence [Tactique].  
S'il se trouve en 3e ou 4e ligne, son niveau est réduit de 1.  
Afin de laisser une part de "forme du jour" et de chance, chaque tacticien reçoit également un bonus aléatoire qui commence à 0 et qui, en théorie pure, peut devenir très important, la probabilité étant de plus en plus faible à mesure que le bonus augmente.  

Le camp avec la meilleure valeur de tactique peut attaquer au tour 0 (appelé "tour du tacticien") sans que l'ennemi ne puisse attaquer.  
Le nombre de coups portés dépend de la différence entre la meilleure valeur de tactique du camp gagnant et celle du camp perdant : pour chaque point de différence, chaque personne a 10 % de chances d'attaquer lors du tour du tacticien.

**Exemple :**

Le camp A a une personne avec Tactique 4 en première ligne.  
Le camp B a 10 personnes avec Tactique 4 en troisième ligne.  
Donc, le camp A a effectivement 5 et le camp B 3.  
Sans le bonus aléatoire, chaque personne du camp A aurait 20% de chances d'attaquer lors du tour du tacticien.  
Si la personne du camp A obtient un 0 en bonus, il faut qu'au moins une personne du camp B obtienne un 2.  
Sinon, le camp A a le tour du tacticien.  
Supposons que le meilleur résultat obtenu au jet par le camp B soit un 5 (c'est peu probable, mais tout à fait possible).  
La différence pour le camp B est donc de (3 + 5) - (5 + 0) = 3.  
Chaque personne du camp B a alors 30% de chances de frapper au tour 0.  
Pour un groupe de 10, cela peut aller de 0 à 10 personnes, mais la moyenne est d'environ 3 attaques.  

## Héros

Les héros sont des combattants particulièrement puissants.  
Ils doivent avoir été préalablement promus avec l'ordre [[cmd-promote]].  
**Les héros peuvent attaquer 5 fois à chaque tour de combat**.

!!! warning "Attention"
    Cela ne s'applique pas aux attaques magiques ni aux arbalètes ni aux catapultes.

Pour plus d'informations, voir [[cmd-promote]].

## Le combat entre deux personnes

Dans chaque bataille, les armées s'affrontent personne par personne, quel que soit leur nombre.La procédure est la suivante :

- L'attaque de l'attaquant et la parade du défenseur sont (au départ) aussi élevées que leur niveau de compétence en armes.
- Ajouter des bonus/malus : A l'attaque de l'attaquant et à la parade du défenseur, on ajoute les éventuels [bonus et malus][non armés].
- Si l'attaquant est un combattant à distance, la valeur de parade de son adversaire ainsi modifiée est divisée par deux.
- Les probabilités de base de toucher (BT) d'un attaquant sont de 30%.
- Soustraire les valeurs les unes des autres : Pour chaque point de différence entre l'attaque de l'attaquant et la parade du défenseur, le BT est maintenant augmenté ou diminué de 5%.
  La probabilité réelle de toucher se calcule donc comme suit : (Attaque(attaquant)-Parade(défenseur)) \* 5% + 30%.
- Chance du débutant : si l'attaque échoue, l'attaquant a en plus 10% de chances de transformer son attaque : Il peut frapper une deuxième fois, avec une chance de toucher augmentée de 90 à 99% (hasard).
  Les combattants fortement désavantagés ont ainsi la possibilité d'obtenir au moins quelques coups aléatoires.

Chaque personne attaque une fois par tour de combat (sauf les [Héros] et certains monstres).

Lorsqu'un combattant réussit à toucher son adversaire, il lui inflige des dégâts.  
Les différentes armes infligent des dégâts différents (points de dégâts, voir [Caractéristiques des armes]).  
Par ailleurs, il vaut la peine d'avoir des niveaux de compétences élevés en maîtrise des armes : si l'on a plus de niveaux de compétence que l'adversaire, les dégâts infligés lors d'un coup augmentent d'un point par différence de deux niveaux de compétence.  
Seuls les niveaux de compétences sont pris en compte, les bonus apportés par les chevaux, les châteaux, etc. ne comptent pas.  
Cela vaut aussi bien pour le combat à distance que pour le combat rapproché.  
En outre, il y a une certaine chance, dépendant de la différence de niveau, de recevoir un coup critique qui peut causer jusqu'à cinq fois plus de dégâts.

Si une personne a subi plus de points de dégâts qu'elle ne peut "en encaisser", elle meurt (voir [Modificateurs de compétences] les différents coups portés pendant le combat s'additionnent).

Lorsqu'un combattant porte une armure, celle-ci peut absorber une partie (voire la totalité) des points de dégâts.  
Cependant, l'armure rend le combattant moins mobile et augmente ses chances d'être touché (voir [le tableau des armures]).  
Contre les arbalètes, une armure n'est qu'à moitié efficace (arrondi à l'inférieur).

Certaines créatures ou armes peuvent également infliger des dégâts magiques.  
Une armure normale est inefficace contre les dégâts magiques.  
Seule compte la [Résistance à la magie], qui peut être augmentée par certains équipements et sorts.  

Il y a également la compétence Endurance, qui permet d'endurcir son corps et de supporter plus de points de dégats avant de mourir (voir [ce tableau]).

### Combat à distance

Les armes à distance et les catapultes peuvent être utilisées efficacement en deuxième ligne.  
Là, elles seront protégées des combattants au corps à corps de l'adversaire par votre première ligne.

Les combattants à distance peuvent également tirer dans la deuxième ligne adverse.  
Ils choisissent une cible au hasard parmi tous les ennemis en première ou deuxième ligne.

Les arbalètes peuvent également transpercer les armures : Contre un tir d'arbalète, l'armure ne fait effet que pour moitié (arrondi inférieur).

Le tableau ci-dessous montre les différences entre les armes à distance.  
Il est très difficile d'utiliser un arc (Offensive Bonus -2), mais on peut tirer tous les rounds de combat.  
Les arbalètes sont beaucoup plus faciles à utiliser (OB 0), mais ne peuvent tirer qu'un round de combat sur trois.  
Les catapultes tirent toujours au premier tour (cela peut être le tour tactique ou le tour 1) et causent de lourds dégâts.

Contre les armes à distance, les personnes attaquées ne se défendent qu'avec la moitié de leur niveau de compétence.  
Cependant les unités en première ligne se défendent avec leur niveau de compétence si le combattant à distance se trouve également en première ligne.

*Attention !'* Si un combattant à distance se retrouve au premier rang (par exemple, parce qu'il a été [débordé]), il doit se défendre avec une arme de mêlée.  
S'il n'en possède pas ou ne peut pas l'utiliser (c'est-à-dire si la compétence correspondante est inférieure à 1), il se défend [à mains nues] !

Les catapultes nécessitent des munitions.  
Celles-ci peuvent être fabriquées à partir de pierres avec l'ordre [[cmd-make|`MAKE ammunition`]], passé par des maçons T3 en [extraction de pierres].  
Elles pèsent 10 kg.  
Une unité de munitions correspond à une salve (6 cibles).

*Armes de tir à distance - bonus et temps de rechargement.*

| Arme                               | Compétence         | Bonus d'attaque | Rechargement |
|------------------------------------|--------------------|:---------------:|:------------:|
| Arc / Arc en mallorn / Arc elfique | Tir à l'arc        |       -2        |      0       |
| Catapulte                          | Tir à la catapulte |       -4        |      5       |
| Arbalète / Arbalète en mallorn     | Tir à l'arbalète   |        0        |      2       |

Le « Rechargement » indique le temps nécessaire pour que l'arme soit à nouveau prête à tirer.  
Une catapulte ne peut donc être utilisée qu'une fois par combat.  
Une arbalète peut tirer tous les trois rounds, et un arc peut tirer à chaque round.  

### Bonus et malus

Divers facteurs peuvent modifier les chances de toucher quelqu'un (attaquer) ou de dévier un coup (parer).  
Tous les bonus et malus ont un effet direct sur la compétence et sont pris en compte avant toute réduction de moitié par les combattants à distance.  
Les points de dégâts qu'une personne inflige ne sont pas modifiés par les bonus et les pénalités;  
les valeurs de compétence non modifiées comptent ici.

Voir aussi : [tables de combat].

#### Combat à mains nues

:   Les personnes ne possédant pas de compétence correspondant à leur arme sont également considérées comme désarmées.  
    Les personnes désarmées combattent avec un score de -2.  
    Les combattants à distance qui entrent en combat au corps à corps et ne peuvent accéder à une arme de corps à corps (et à la compétence correspondante) se défendent avec un score de -2.  
    Ils peuvent toujours attaquer avec leur arme à distance.  
    Les gobelins se défendent avec +/-0.  
    La compétence avec laquelle les orcs engagent le combat au corps à corps est déterminée par le niveau de leur meilleure compétence de corps à corps - 3.  
    Certaines races (généralement les familiers) peuvent apprendre le combat au corps à corps et ne subissent alors aucune pénalité lorsqu'ils combattent au corps à corps.  

#### Bonus de château

:   Les personnes se trouvant dans un château bénéficient d'une protection supplémentaire.  
    Les occupants du château bénéficient d'un bonus de parade, selon la taille du château, s'ils appartiennent au camp défenseur et que le château est suffisamment grand pour les accueillir.  
    Une fortification donne +1, une tour +2, et ainsi de suite, jusqu'à la citadelle, qui donne +5.  
    Si les occupants du château s'attaquent eux-mêmes, ils ne bénéficient d'aucun bonus de parade.  
    Le bonus du château s'applique également aux combattants à distance !  

#### Bonus de cavalerie

:   Dans les plaines, les déserts et les Highlands, les combattants en première ligne en terrain découvert peuvent utiliser un cheval.  
    Pour monter un cheval au combat, il faut être T2 en [équitation] et posséder un cheval.  
    Les cavaliers bénéficient d'un bonus de +2 à l'attaque et à la parade, car ils sont plus rapides et plus agiles.  
    Les cavaliers à l'intérieur d'un château, et bénéficiant du bonus du château, n'ont pas le bonus cavalerie si ils sont attaqués.  
    Les trolls ne peuvent pas utiliser de chevaux au combat.  

#### Bonus de lance

:   Les porteurs de lance et de javelot montés reçoivent un bonus additionnel de +1 en attaque.  

#### Bonus de piquiers

:   Les porteurs de javelot et de hallebarde qui n'utilisent pas de cheval reçoivent un bonus de +1 à la parade contre les troupes montées.  

#### Modificateurs d'armes

:   Les [Modificateurs d'armes][Caractéristiques des armes] sont également considérés comme des bonus et des malus.  
    Une unité de hallebardiers a donc (en plus de tout autre bonus ou malus éventuel) un bonus de +2 à sa parade.  
    Si elle n'est pas montée et qu'elle se bat contre un cavalier, sa valeur de parade est alors augmentée de +1.  

Voici quelques exemples de situation de combat.  

<!-- TODO: clarify the whole paragraph -->
**Exemple 1 :**

Chance de base de l'attaquant -> BC = 30 %.  
Attaquant avec compétence 3, compétence défenseur 4 -> chance de toucher = 25 %.  
Défenseur dans une citadelle -> parade +5 -> chance de toucher = 0 %.  

Ainsi, l'attaquant n'a qu'une chance de 10 % (« chance du débutant ») d'obtenir un deuxième essai, pour lequel il a 90 à 99 % de chances de réussir à toucher.  
Au total, il y a 9 à 9,9 % de chances de toucher le défenseur.  

Après tout, l'attaquant se trouve dans une très mauvaise situation car le défenseur est dans une citadelle.

**Exemple 2 :**

Supposons cette fois-ci que le défenseur n'est pas dans la citadelle.  

Chance de base de l'attaquant -> BC = 30%.  
Compétence de l'attaquant 3, compétence du défenseur 4 -> chance de toucher = 25 %.  
Attaquant avec bonus de cheval -> attaque +2 -> chance de toucher = 35 %.  

**Exemple 3 :**

Une jeune fille à l'épée en mêlée 3 contre un cavalier avec *équitation* T1 et *combat à l'arme d'hast* T2.  
Elle attaque avec 3 (compétence 3) contre une parade de 2 (compétence 2, pas de bonus de cheval, car la compétence du cavalier est trop faible).  

L'attaquant a une chance de toucher de 35 %.  

**Exemple 4 :**

Un archer T9 attaque depuis la 2ème ligne contre un cavalier avec lance avec équitation T3 et combat à l'arme d'hast T9.  
Il attaque avec 7 (malus de -2 à l'arc) contre une parade de 5 (compétence divisée par deux et arrondie à l'inférieur : compétence 9, +2 bonus cheval -> (9+2) /2 = 5).  

L'attaquant a une chance de toucher de (7 -5) * 5 % + 30 % = 40 %  

**Exemple 5 :**

Un cavalier de lance avec une monture 3 et des armes d'hast 9 attaque un archer avec la compétence 9 en première ligne.  
Il attaque avec 12 (compétence 9, bonus cheval +2, bonus lance +1) contre une parade de -2 (combattant à distance sans arme de corps à corps).

L'attaquant a une chance de toucher de 100 %, il frappera donc toujours. Aïe...  

Elle pare avec toute sa valeur de parade (compétence arme + bonus cheval = 11), car ils sont en contact direct, contre une arme à distance (malus de 2 à cause de l'arc).

Le tireur attaque efficacement avec un 7 contre le cavalier avec un 11.  
La chance de succès de toucher qui en résulte est (7 -11) * 5 % + 30 % = 10 %.

**Exemple 6 :**

Un combattant à la lance avec des armes d'hast 3 dans un château attaque un cavalier avec une monture 2 et des armes d'hast 3.  
Il attaque à 3 (compétence 3, pas de bonus de pique en attaque, pas de bonus de château non plus) contre 5 (compétence 3, +2 bonus de cheval, pas de bonus de lance en parant).  

L'attaquant a une chance de toucher de (3 -5) * 5 % + 30 % = 20 %.  

Elle parera à 4 (compétence 3, pas de bonus de château car elle a attaqué, +1 bonus de pique) contre 6 (+2 bonus de cheval et +1 bonus de lance).  

Le cavalier a une chance de toucher de (6 -4) x 5 % + 30 % = 40 %.

**Exemple 7 :**

Un cavalier avec équitation 2 et mêlée 2 contre un chasseur à la lance avec armes d'hast 3.  
Ils attaquent à 4 (compétence 2, bonus cheval +2) contre 4 (compétence 3 et bonus pique +1).  

L'attaquant a une chance de toucher de 30 %.  

Le combattant à la lance riposte à 3 contre 4 (le bonus de pique ne s'applique pas lors de l'attaque).  

Le porteur de lance a une chance de toucher de 25 %.  

**Exemple 8 :**

Un cavalier de lance avec équitation 2 et armes d'hast 3 attaque un combattant égal.  
Ils combattent à 6 (compétence 3, +2 pour l'équitation, +1 bonus de lance) contre 5 (compétence 3, +2 pour l'équitation).  

L'attaquant a donc une chance de toucher 35 %.  

Il s'ensuit que vous pouvez relativement bien tenir un château, mais que vous ne devez pas lancer d'attaques depuis un château si possible, car vous perdrez votre bonus de défense.  
Il s'ensuit également que les combattants à la lance sont légèrement plus efficaces contre les troupes montées que les combattants à l'épée.

## La fuite

Les unités qui sont au statut [[cmd-combat|`COMBAT FLEE`]] et sont [[cmd-attack|attaqués]] essaient de fuir.  
Ils le font avant chaque round de combat, ils devront donc peut-être subir (plus) de coups avant de pouvoir s'échapper.  

Les unités **touchées au combat** tentent également de fuir si :

- Elles sont au statut [[cmd-combat|`COMBAT`]] ou [[cmd-combat|`COMBAT REAR`]] et qu'**il ne leur reste que 20%** de points de vie (PV)
- Elles sont au statut [[cmd-combat|`COMBAT DEFENSIVE`]] ou [[cmd-combat|`COMBAT NOT`]] et qu'**il ne leur reste que 90%** de leurs PV

Les coups dont les points de dégâts ont été entièrement absorbés par l'armure et les tentatives de coup ratées comptent également.  
Ceci a pour but d'empêcher les unités déjà endommagées avant la bataille de fuir même si elles n'étaient pas réellement en danger.  

La chance de base de s'échapper est de 25 % (50 % pour les halflings), plus 10 % si vous possédez un cheval et 5 % par niveau de compétence furtive;  
la valeur maximale est de 75 % (ou 90 % pour les Halflings).

Les unités en fuite échappent au combat, mais restent à une distance sûre des combats dans la région.  
Si l'unité se trouvait dans un bâtiment ou sur un bateau à terre, elle le quitte dès qu'une personne de l'unité s'est enfuie pendant la bataille.

!!! note
    Il peut être utile d'ordonner aux occupants d'un château (ou d'un bateau) de réintégrer leur propre château (ou bateau), ce qu'ils pourront peut-être faire après la bataille.
    Pensez également à remettre le commandement à la bonne unité avec [[cmd-give|`GIVE COMMAND`]].

### Statut de combat `FLEE`

Des règles particulières s'appliquent aux unités qui sont au statut de combat `FLEE`.  

Ces unités **peuvent toujours se déplacer après le combat**, même si elles ne pourraient normalement pas exécuter un ordre long.  

De plus, ces unités ne **peuvent pas garder** de régions.  
Toute garde est automatiquement annulée lorsque l'unité de garde passe au statut `FLEE`.  
Cela se produit au début du tour, ce qui signifie que tous les effets de [[cmd-guard]] sont immédiatement annulés.

## Combats à bord et depuis les navires

Les batailles navales se déroulent comme des batailles terrestres : les [[bateaux]] s'abordent et les unités s'affrontent.  
Après la bataille, il est possible pour les unités d'exécuter d'autres ordres longs.

Si un bateau est impliqué dans une bataille, il subit 5 % de dégâts par round de bataille si au moins une personne qui se trouve sur le navire ou qui s'y trouvait au début du tour subit des dégâts.  
Il ne sert donc à rien de quitter le bateau avant le début de la bataille.  
Le [tour de tactique] et le premier tour ne sont pas pris en compte, les dégâts maximum possibles sont donc de 20 %.  

Des dégâts supplémentaires peuvent survenir si des serpents de mer sont impliqués dans la bataille.  
Ces monstres, comme certains familiers, ont une attaque qui peut causer des dégâts structurels aux bateaux à chaque round de combat.

Si le bateau est en sous-équipage ou vide après la bataille, il dérive sans contrôle dans l'océan et subit davantage de [dommages].

Si vous souhaitez atterrir dans une région [[cmd-guard|gardée]] par une autre faction, vous devez d'abord [[cmd-leave|quitter]] le bateau et ne pourrez attaquer ou vous déplacer que lors du tour suivant.  
Cela donne à vos ennemis le temps de se préparer.

Depuis la terre, vous pouvez attaquer un bateau immédiatement.  
Lorsque les unités à bord d'un bateau (ou ses alliés) sont attaqués, elles rejoignent les lignes de bataille normalement en fonction de leur statut de combat ([[cmd-combat]]) et de leur statut d'aide au combat ([[cmd-help|`HELP COMBAT`]]).  

## Piraterie

Chaque capitaine a la chance de gagner un prix en capturant des bateaux dans les régions adjacentes.

Le capitaine guette les bateaux qui terminent leur déplacement dans une région voisine.  
Une fois sur place, l’équipage peut agir normalement lors du tour suivant.  
Avec l'aide de [[cmd-follow|`FOLLOW SHIP`]], par exemple, vous pouvez également simplement suivre vos victimes pour le moment.

Il y a quelques points à garder à l’esprit dans toute l’histoire :

- Uniquement les factions avec lesquelles vous n'êtes pas allié de combat (`HELP FIGHT`) sont reconnus comme des cibles
- Si les numéros de faction sont spécifiés ([[cmd-piracy|`PIRACY`*`<faction-id>`*`...`]]), seuls les capitaines des factions spécifiées sont reconnus comme cibles
- Le mécanisme fonctionne également lorsque le bateau pirate est à terre
  Il offre donc un moyen efficace de protection du littoral.
- Les pirates naviguent également dans les régions terrestres, à condition que le bateau puisse y atterrir.
  S'il ne peut pas atterrir, il subit des dégâts.
- Les capitaines pirates sont aussi épais que des voleurs. <!-- TODO: better translation -->
  Ils ne peuvent pas évaluer si une cible leur est éventuellement supérieure.
  Ils se contenteront donc de faire naviguer un seul bateau dans une flotte ennemie de 100 bateaux.
  Être pirate comporte des risques.
- S'il y a plusieurs cibles potentielles parmi lesquelles choisir, le capitaine en sélectionnera une au hasard
- Les flottes pirates restent ensemble.
  Si un bateau allié (sur lequel le capitaine a défini [[cmd-help|`HELP COMBAT`]]) de votre propre région a déjà reconnu une victime, notre bateau naviguera également vers la région en question, à condition que la victime reconnue par le premier bateau soit également une victime potentielle pour nous.

## Fin du combat

Après la bataille, on compte les morts, et tout le matériel utilisable des unités anéanties est récupéré et distribué aux survivants.  

Les unités blessées au combat restent blessées.  
Ceci est indiqué dans le rapport.  
Avec le temps, elles guérissent.  
Elles régénèrent généralement 5 % (certaines races [[modificateurs-de-competences|davantage]]) de leurs points de vie maximum par tour, mais au moins un point par individu.  
Les unités mortes-vivantes ne se régénèrent pas.

Si la région où les combats ont eu lieu était [[alliances|gardée]] **au début du combat** par une unité amie ou une unité ayant activé l'ordre [[cmd-help|`HELP GUARD`]] pour les forces amies, toutes les unités participant au combat (celles figurant dans le rapport de bataille) peuvent exécuter des ordres longs.  
Ceci est valable même si des troupes ennemies gardent également la région.  
Cela fonctionne aussi si tu as attaqué toi-même (c'est-à-dire si tu as donné toi-même l'ordre `ATTACK`).

Si aucune unité amie ou alliée ne gardait la région au début du combat, les unités participantes ne pourront plus exécuter d'ordres longs après le combat.

La seule exception concerne les unités avec le statut de combat [[cmd-combat|`COMBAT FLEE`]] et les unités en mer.  
Les unités avec le statut `COMBAT FLEE` peuvent se déplacer après une bataille s'ils ont défini l'un des ordres suivants : [[cmd-move]], [[cmd-route]] ou [[cmd-follow|`FOLLOW SHIP`]].  
Après une bataille en mer, vous pouvez toujours exécuter des ordres longs.

## Voir aussi

- [[tactique]]
- [[war-tables]]

Poursuivre la lecture : [[alliances]].

<!-- From [https://wiki.eressea.de/index.php?title=Krieg/fr&oldid=16966] -->

[Caractéristiques des armes]: ./war-tables.md#armes-tableau-de-synthese
[Modificateurs de compétences]: ./war-tables.md#races-et-leurs-caracteristiques
[le tableau des armures]: ./war-tables.fr.md#armures-synthese
[Résistance à la magie]: ./war-tables.md#resistance-a-la-magie
[ce tableau]: ./war-tables.md#endurance
[dommages]: ./sailing.md#dommages-aux-bateaux
[Tactique]: ./skills-list.md#tactique "Tactics"
[extraction de pierres]: ./skills-list.md#extraction-de-pierres "Quarrying"
[équitation]: ./skills-list.md#equitation "Riding"

[tour de tactique]: #tour-du-tacticien
[Lignes de combat]: #lignes-de-combat
[débordé]: #lignes-de-combat
[la fuite]: #la-fuite
[fuir]: #la-fuite
[s'enfuira]: #la-fuite
[non armés]: #bonus-et-malus
[à mains nues]: #bonus-et-malus
[tables de combat]: #bonus-et-malus

<!-- prefixed with war.md to avoid markdown lint warning due to accents in anchors -->
[combat en mer]: ./war.md#combats-a-bord-et-depuis-les-navires
[Héros]: ./war.md#heros
