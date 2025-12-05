# Races

En plus des humains, il y a beaucoup d'autres races (types de faction) à Eressea. Tu dois en choisir une pour ta faction. Chaque race a des avantages et des inconvénients qui se traduisent par des [Bonus et Malus] dans certaines compétences et parfois des capacités spéciales ; Chaque race a des [coûts de recrutement][Bonus et Malus] différents. En règle générale, une personne pèse 10 unités de poids (GE) et peut porter 5,4 GE. Les trolls, les gobelins et divers monstres constituent des exceptions.

Au début du jeu, tu dois choisir la race que tu veux jouer. Cette race est choisie lors de l'inscription et ne peut plus être modifiée par la suite. Il convient donc de bien réfléchir avant de faire son choix.

Pour un aperçu rapide, consultez le [Tableau des modificateurs raciaux][Bonus et Malus].

## Démons

Les démons (demons) sont cruels et imprévisibles. Ils dévorent les paysans des environs et surprennent toujours par l'acquisition de nouvelles capacités ou la perte de celles-ci.

**Attention !** Les démons ne sont pas conseillés aux joueurs inexpérimentés au jeu Eressea !

- Volatilité : Toutes les compétences ayant au moins un point de compétence (avant malus racial) ont 25 % de chances de changer de niveau. La compétence peut perdre jusqu'à 3 semaines d'apprentissage (40%) ou augmenter jusqu'à 3 semaines d'apprentissage (60%). Il n'en résulte pas de valeurs négatives; aucune compétence ne peut descendre en dessous du niveau 0.
- Les démons mangent des paysans à chaque tour. Un paysan nourrit dix démons.Les démons qui ne reçoivent pas de nourriture (pas assez de paysans) perdent des points de vie et sont soumis à la réduction de compétences selon la règle de normale de la [famine]. Les unités se nourrissent des paysans dans l'ordre où ils apparaissent dans le rapport (voir rapport nr).
- Les démons [recrutés] ne sont pas déduits de la réserve de paysans. Cependant, pour des raisons techniques de jeu, la limite de recrutement par région s'applique quand même.
- Si on rend des démons aux paysansavec l'ordre [`GIVE 0`], ils retournent dans leur sphère d'origine et ne s'ajoutent pas à la quantité de paysans de la région.
- Les démons peuvent se [camoufler] en une autre race .
- Au corps à corps, chaque coup porté par un démon à un adversaire provoque une "panique sur 1 personne" : la personne touchée a -1 à ses compétences de combat (pas l'unité).
- Les démons blessés se régénèrent à hauteur de 7,5% de leurs points de vie.

## Elfes

Le peuple magique du royaume des fées n'est pas fait pour le travail pénible, mais ses archers sont presque aussi redoutés que ses magiciens.

- Chaque elfe (jusqu'à 1/8 du [max. workers] de la region, par exemple 250 dans un marais) augmente les chances qu'un arbre (y compris les mallorn) sème une graine au cours d'une semaine d'été ou d'automne. Cela peut faire une grande différence en fonction du nombre d'elfes sur la région.
- Dans les forêts, les elfes ont un bonus de compétence de +1 en stealth et perception et +2 en tactics.
- Les elfes peuvent avoir 6 [mages] (au lieu de 5).
- Les mages elfes régénèrent leur aura beaucoup plus rapidement.
- Les elfes font 1 point de dégâts supplémentaire avec les arcs.
- Seuls les elfes peuvent construire des [elven bows].

## Goblins

Les goblins sont petits et faibles lorsqu'ils sont seuls ; ils préfèrent compter sur la ruse ou le surnombre. Chez eux, la règle est "la masse plutôt que la classe".

- Lorsque leur nombre est dix fois supérieur à celui de l'adversaire, les gobelins bénéficient d'un bonus de +1 à l'attaque.
- Les goblins ne pèsent que 6 GE, mais leur capacité de transport (4,4 GE) est également moindre.
- Si des goblins ayant un niveau d'au moins 4 en stealth [volent], ils dérobent toujours au moins 50 Silver, même s'ils se font prendre.
- Les goblins non armés ont un bonus de +2 à leur défense.
- Les gobelins blessés se régénèrent à hauteur de 10% de leurs points de vie.

## Halflings

Les halflings sont de petits compagnons aux pieds poilus. Ils sont de bons commerçants et savent divertir les paysans. Ce sont de bons bâtisseurs, mais ils préfèrent laisser les chevaux et les [bateaux] aux autres. Le maniement des armes n'est pas leur point fort.

- Les halflings qui essaient de [fuir] un combat, ont une chance de base de 50% (25% pour les autres races). Leur chance maximale est de 90% (75% pour les autres, voir [`COMBAT FLEE`]).
- Les halflings ont un bonus de +5 en attaque et dégâts lorsqu'ils affrontent des [dragons].
- Les halflings sont bien plus sensibles que les autres à la famine. Ils perdent entre 8 and 17 points de vie (1d10+7).

## Insectes

Les insectes (insects) vivent dans un état strictement organisé. Ils détestent le froid et se sentent le mieux dans les régions humides ou chaudes. Leur carapace dure les protège de bien des agressions. Leur compétence et leur discipline font d'eux d'excellent enseignants.

**Attention !** Les insectes ne sont pas conseillés aux joueurs inexpérimentés au jeu Eressea !

- Les insectes aiment la chaleur et l'humidité et détestent le froid : dans les déserts et les marais, ils ont +1 aux compétences dans lesquelles ils ont au moins 1, dans les montagnes et les glaciers -1.
- Les insectes ne peuvent pas entrer dans les glaciers et ne peuvent pas y être recrutés, il y fait trop froid. Les insectes qui pénètrent malgré tout dans un glacier perdent des points de vie et voient leur compétence réduite de moitié selon la règle normale de la [famine].
- Les insectes ne peuvent recruter que dans les déserts durant les mois d'hiver (Hearth fire, Icewind and Snowbane). Il est cependant possible avec la compétence [alchemy] de créer une [potion] de "nest warmth" qui permet de recruter dans d'autres types de région.
- Les insectes sont automatiquement protégés par leur armure naturelle de chitine. Cette armure naturelle sera réduite de moitié si les insectes portent une armure additionnelle (voir [hier]).
- Les insectes obtiennent un bonus sur la compétence [tactics] lorsqu'ils sont en nombre. Un tacticien insecte obtient (log<sub>10</sub> (nombre de combattants dans son groupe))-1 à sa compétence tactics. Cela peut également entraîner un malus s'il y a très peu de combattants ! Attention, les unités dans différents [groupes] sont gérées dans des armées différentes !
- Les insectes n'ont besoin d'aucune construction pour [commercer] dans les déserts et les marais.

## Chats

Connus pour leurs sens développés, les chats (cats) font des espions excellents et des gardes hors-pairs . Mais, comme les elfes, ils n’aiment pas les travaux pénibles.

- « Sept vies » : les chats ont 1/7 chance de survivre à un coup mortel ; ils ont dans ce cas leurs points de vie maximum.
- Les chats ne peuvent porter de Platemail.
- Leur Agilité confère aux chats un bonus de +1 en Défense

## Aquariens

Les aquariens (Aquarians) sont chez eux dans l’eau, mais sont plutôt mal à l’aise en montagne. Ils construisent et dirigent des navires de main de maître, alors que d'autres tâches leur sont plus compliquées.

- Tous les navires commandés par un capitaine aquarien appartenant à une faction d'aquariens se [déplacent] d'une région supplémentaire chaque semaine.
- Les aquariens peuvent exécuter des [ordres longs] sur les bateaux. Attention, cela a quelques conséquences implicites : Les aquariens peuvent par exemple se déplacer d'une région océanique adjacente à une région terrestre vers la région terrestre, voir [nager].
- Sur une case d'océan (type de région océan) jusqu'à 100 aquariens embarqués peuvent gagner 10 Silver chacun avec l'ordre [`WORK`].

## Humains

Les humains (humans) peuvent tout faire un peu. Ils n'ont aucune compétence vraiment mauvaise mais aucune de vraiment bonne non plus. Ils peuvent donc assez facilement combler les faiblesses d'autres races alliées, bien qu'ils n'aient aucune spécialisation.

- Immigrants : les factions d'humains sont les seules à être autorisées à avoir des personnes d'une autre race dans leurs rangs, bien que mélanger différentes races dans une même unité ne soit pas possible. Cependant, ils ne peuvent pas les recruter eux-mêmes, mais doivent se les [faire donner][`GIVE 0`] par d'autres factions. Il n'y a pas d'immigrants avec des [compétences payantes], c'est-à-dire magie, alchimie, herboristerie, espionnage et tactique.

Le nombre d'immigrants se calcule comme suit : 20 × log<sub>10</sub> (taille de la faction ÷ 50). Si l'on a soudainement trop d'immigrants à cause d'une catastrophe ou d'un combat, ceux-ci ne sont pas supprimés, on ne peut juste plus en accueillir de nouveaux. Le nombre maximum d'immigrants est indiqué dans le rapport et, pour les grandes factions, il est presque identique au nombre de [Héros]. Le tableau suivant contient quelques exemples :

Immigrants

|                           |   |    |    |    |    |    |    |     |     |      |      |       |        |         |
|---------------------------|---|----|----|----|----|----|----|-----|-----|------|------|-------|--------|---------|
| personnes dans la faction | 1 | 56 | 57 | 63 | 71 | 80 | 89 | 159 | 500 | 1000 | 5000 | 50000 | 500000 | 5000000 |
| immigrants                | 0 | 0  | 1  | 2  | 3  | 4  | 5  | 10  | 20  | 26   | 40   | 60    | 80     | 100     |

## Orcs

Les Orcs commencent leur vie en tant que combattants et la terminent généralement en tant que combattants. Leur force réside dans le nombre, mais ils manquent de jugeote.

- Combattants nés : Toutes les nouvelles recrues orcs commencent au niveau 1 dans les compétences Melee and Polearm.
- Paresse : les orcs gagnent moins de silver que les autres races avec l'ordre [`WORK`].
- Recrues faciles : Pour deux orcs recrutés, un seul paysan est soustrait du pool de paysans de la région. Ainsi vous pouvez recruter deux fois la limite de recrutement d'une région. La soustraction est arrondie au supérieur.
- De même : si vous donnez des orcs aux paysans avec l'ordre [`GIVE 0`], seule la moitié d'entre eux est ajoutée aux paysans. Cela est arrondi à l'inférieur.
- Les orcs non armés ne combattent pas au corps à corps avec malus de -2 comme les autres races, mais avec ("meilleure compétence de combat corps à corps" -3). Ils ont toutefois besoin d’armes pour collecter les impôts.
- Les orcs ont le cerveau lent et apprennent généralement toutes les compétences un peu plus lentement que les autres races, hors celles de combat (cad celles pour maîtriser une arme).

## Trolls

Ces rochers ambulants font partie des créatures les plus puissantes d'Eressea. Ils adorent travailler les pierres. Mais ils effraient les chevaux et la natation n'a jamais été considérée comme leur passe-temps favori.

- Les trolls sont forts et peuvent porter deux fois plus que les autres (10,8 GE), mais ils pèsent aussi deux fois plus (20 GE).
- Il n'y a pas de cavalerie troll, ce qui signifie que les trolls ne reçoivent pas de bonus de cheval. Cela n'a aucun effet sur le transport de marchandises et la vitesse de déplacement des trolls montés.
- Les pierres extraites par les trolls ne sont déduites qu'à 75% de la "réserve de la région". Cet effet est cumulatif avec une quarry (carrière) (voir [ici] et [ici][1]).
- Contre les trolls, la cavalerie ennemie n'a qu'un bonus de +1 au lieu du +2 habituel.
- Les trolls sont la seule race capable d'utiliser des chariots sans chevaux. Les trolls peuvent tirer un chariot par quatre, mais ils ne peuvent se déplacer que d'une seule région (sauf route). Cela est expliqué plus en détail dans l'ordre [RIDE].
- Les trolls non armés infligent de 2 à 6 points de dégâts.
- Les trolls blessés se régénèrent à hauteur de 7,5% de leurs points de vie.

## Nains

Les nains (dwarves) vivent dans les montagnes, leurs armes sont réputées et leurs forteresses sont connues pour leur solidité. En revanche, ils sont tout aussi sceptiques à l'égard de la magie que des chevaux, et leurs compétences en matière de navigation sont parmi les plus mauvaises du monde.

- Le fer extrait par les nains n'est déduit qu'à 60% de la "réserve de la région". Cet effet est cumulatif avec une mine (voir [ici][2] et [ici][1]).
- Dans les montagnes et les glaciers, les nains obtiennent +1 à leur compétence [tactics].
- Les [mages] nains régénèrent leur aura beaucoup plus lentement que les autres.

|--------------|--------------------------------|
| En savoir plus : | [Modificateurs de compétences] |

[Modificateurs de compétences]: ./skills-modifiers.md "Talentmodifikatoren"

<!-- From [https://wiki.eressea.de/index.php?title=Rassen/fr&oldid=16646] -->

[Bonus et Malus]: ./skills-modifiers.md "Talentmodifikatoren"
[famine]: ./silver.md#famine "Famine"
[recrutés]: ./silver.md#recruter "Recrutement"
[`GIVE 0`]: ./cmd-give.md "GIVE"
[camoufler]: ./cmd-hide.md "HIDE"
[max. workers]: ./world.md "Welt"
[mages]: ./magic.md "Magie"
[elven bows]: ./war-tables.md#waffeneigenschaften "Guerrestabellen"
[volent]: ./cmd-steal.md "STEAL"
[bateaux]: ./ships.md "Bateaux"
[fuir]: ./war.md#la-fuite "Guerre"
[`COMBAT FLEE`]: ./cmd-combat.md "COMBAT"
[dragons]: ./monsters.md#drachen "Drachen"
[alchemy]: ./skills-list.md "Liste des compétences"
[potion]: ./alchemy.md "Tränke"
[hier]: ./war-tables.md#rasseneigenschaften "Guerrestabellen"
[tactics]: ./tactic.md "Tactique"
[groupes]: ./cmd-group.md "GROUP"
[commercer]: ./silver.md#commerce "Argent"
[déplacent]: ./travel.md "Reisen"
[ordres longs]: ./commands.md "Befehl"
[nager]: ./sailing.md#nager "Schiffsreisen"
[`WORK`]: ./cmd-work.md "WORK"
[compétences payantes]: ./skills.md "Talente"
[Héros]: ./cmd-promote.md "PROMOTE"
[ici]: ./buildings-others.md#steinbruch "Andere Gebäude"
[1]: ./resources.md#ressources-minières "Ressources"
[RIDE]: ./cmd-ride.md "RIDE"
[2]: ./buildings-others.md#bergwerk "Andere Gebäude"
