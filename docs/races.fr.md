---
# cSpell:locale fr
alias: peuples-fr
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD042 MD052 -->
# Peuples

En plus des [Humains][humains]title={"Humans"}, il existe beaucoup d'autres peuples (types de faction, ou peuples) dans Eressea.  
Vous devrez en choisir une pour votre [faction][faction].  

Chaque peuple a des avantages et des inconvénients qui se traduisent par des [bonus et malus][modificateurs-de-competences-id] dans certaines compétences, et parfois des capacités spéciales.  

Chaque peuple a des [coûts de recrutement][modificateurs-de-competences-id] différents.  

En règle générale, une personne (un membre d'unité) **pèse 10** unités de poids (lbs) et **peut porter jusqu'à 5,4 lbs**.  
Les [Trolls][trolls-fr-id]{title="Trolls"}, les [Gobelins][gobelins]title={"Goblins"} et divers monstres constituent des exceptions.

Au début du jeu, lors de l'inscription, tu dois choisir le peuple que tu veux jouer.  
**Elle ne pourra plus être modifiée par la suite**.  
Il convient donc de bien réfléchir avant de faire son choix.

Pour un aperçu rapide, consultez le [tableau des modificateurs de compétences][modificateurs-de-competences-id].

[](){ #demons-fr-id }

## Démons

<!-- cspell:disable -->
*Demons (EN), Dämonen (DE).*
<!-- cspell:enable -->

| PV | Armure naturelle | Résistance à la magie | Régénération | Recrutement |
|:--:|:----------------:|:---------------------:|:------------:|:-----------:|
| 50 |        2         |          15           |    7,5 %     | 150 silver  |

| Poids  | Capacité |
|:------:|:--------:|
| 10 lbs | 5,4 lbs  |

Les démons sont cruels et imprévisibles.  
Ils dévorent les paysans des environs et surprennent toujours par l'acquisition de nouvelles capacités ou la perte de celles-ci.  

!!! note "Attention"
    Les démons ne sont pas conseillés aux joueurs inexpérimentés !

- Volatilité : toutes les compétences ayant au moins un point de compétence (avant malus racial) ont 25 % de chances de changer de niveau.
  La compétence peut perdre jusqu'à 3 semaines d'apprentissage (40 %) ou augmenter jusqu'à 3 semaines d'apprentissage (60 %).
  Il n'en résulte pas de valeurs négatives; aucune compétence ne peut descendre en dessous du niveau 0.
- Les démons mangent des paysans à chaque tour.
  Un paysan nourrit 10 démons. Les démons qui ne reçoivent pas de nourriture (pas assez de paysans) perdent des points de vie et sont soumis à la réduction de compétences selon la règle normale de la [famine][famine].
  Les unités se nourrissent des paysans dans l'ordre où ils apparaissent dans le [rapport][cr-fr-id].
- Les démons [recrutés][recruter] ne sont pas déduits de la réserve de paysans.
  Cependant, pour des raisons techniques de jeu, la limite de recrutement par région s'applique quand même.
- Si on rend des démons aux paysans avec l'ordre [`GIVE 0`][cmd-give-fr], ils retournent dans leur sphère d'origine et ne s'ajoutent pas à la quantité de paysans de la région.
- Les démons peuvent [se camoufler][cmd-hide-fr] en un autre peuple.
- Au corps à corps, chaque coup porté par un démon à un adversaire provoque une "panique sur 1 personne" : la personne touchée uniquement (pas l'unité) a -1 à ses compétences de combat.
- Les démons blessés se régénèrent à hauteur de 7,5 % de leurs points de vie (PV).

## Elfes

<!-- cspell:disable -->
*Elves (EN), Elfen (DE).*
<!-- cspell:enable -->

| PV | Armure naturelle | Résistance à la magie | Régénération | Recrutement |
|:--:|:----------------:|:---------------------:|:------------:|:-----------:|
| 18 |        0         |          10           |     5 %      | 130 silver  |

*Compétences de combat.*

| [Magie][magie]{title="Magie"} | [Discrétion][skill-discretion-id]{title="Stealth"} | [Espionnage][skill-espionnage-id]{title="Espionage"} | [Perception][skill-perception-fr-id]{title="Perception"} | [Arme d'hast] | [Endurance][skill-endurance-fr-id]{title="Endurance"} | [Mêlée][skill-melee-fr-id]{title="Melee"} | [Tactique][tactique]{title="Tactics"} | [Tir arbalète][tir-a-larbalete]{title="Crossbow"} | [Tir arc][tir-a-larc]{title="Bow"} | [Tir catapulte][tir-a-la-catapulte]{title="Catapult"} |
|:-----------------------------:|:--------------------------------------------------:|:----------------------------------------------------:|:--------------------------------------------------------:|:-------------:|:-----------------------------------------------------:|:-----------------------------------------:|:-------------------------------------:|:-------------------------------------------------:|:----------------------------------:|:-----------------------------------------------------:|
|              +1               |                         +1                         |                          0                           |                            +1                            |       0       |                           0                           |                     0                     |                   0                   |                         0                         |                 +2                 |                          -2                           |

*Compétences de production.*

| [Apprivoisement][apprivoisement]{title="Taming"} | [Construction routes][construction-de-routes]{title="Roadwork"} | [Construction navale] | [Extraction pierres][extraction-de-pierres]{title="Quarrying"} | [Extraction minière][extraction-miniere]{title="Mining"} | [Fab. armes][fabrication-darmes]{title="Weaponsmithing"} | [Fab. armures][fabrication-darmures]{title="Armoursmithing"} | [Fab. chariots][fabrication-de-chariots]{title="Cartmaking"} | [Maçonnerie][maconnerie]{title="Masonry"} | [Sylviculture][sylviculture]{title="Forestry"} |
|:------------------------------------------------:|:---------------------------------------------------------------:|:---------------------:|:--------------------------------------------------------------:|:--------------------------------------------------------:|:--------------------------------------------------------:|:------------------------------------------------------------:|:------------------------------------------------------------:|:-----------------------------------------:|:----------------------------------------------:|
|                        +1                        |                               -1                                |          -1           |                               -1                               |                            -2                            |                            0                             |                              -1                              |                              0                               |                    -1                     |                       0                        |

*Autres compétences.*

| [Équitation][equitation]{title="Riding"} | [Voile][voile]{title="Sailing"} | [Commerce][commerce]{title="Trade"} | [Divertissement][skill-divertissement-id]{title="Entertainment"} | [Taxation][skill-taxation-fr-id]{title="Taxation"} | [Alchimie] | [Herboristerie] |
|:----------------------------------------:|:-------------------------------:|:-----------------------------------:|:----------------------------------------------------------------:|:--------------------------------------------------:|:----------:|:---------------:|
|                    0                     |               -1                |                  0                  |                                0                                 |                         0                          |     -1     |       +2        |

| Poids  | Capacité |
|:------:|:--------:|
| 10 lbs | 5,4 lbs  |

Le peuple magique du Royaume des Fées n'est pas fait pour le travail pénible, mais ses archers sont presque aussi redoutés que ses mages.

- Chaque elfe (jusqu'à 1/8 du [nombre maximal de travailleurs][geographie] de la région, par exemple 250 dans un marais) augmente les chances qu'un arbre (y compris les mallorn) sème une graine au cours d'une semaine d'été ou d'automne.
  Cela peut faire une grande différence en fonction du nombre d'elfes sur la région.
- Dans les forêts, les Elfes ont un bonus de compétence de +1 en [discrétion][skill-discretion-id]{title="Stealth"} et [perception][skill-perception-fr-id]{title="Perception"}, et +2 en [tactique][tactique]{title="Tactics"}.
- Les elfes peuvent avoir 6 [mages][magie] (au lieu de 5).
- Les mages elfes régénèrent leur aura beaucoup plus rapidement.
- Les elfes font 1 point de dégâts supplémentaire avec les arcs.
- Seuls les elfes peuvent fabriquer des [arcs elfiques][arc-elfique]{title="Elven bow"}.

## Gobelins

<!-- cspell:disable -->
*Goblins (EN), Goblins (DE).*
<!-- cspell:enable -->

| PV | Armure naturelle | Résistance à la magie | Régénération | Recrutement |
|:--:|:----------------:|:---------------------:|:------------:|:-----------:|
| 16 |        0         |          -5           |     10 %     |  40 silver  |

| Poids | Capacité |
|:-----:|:--------:|
| 6 lbs | 4,4 lbs  |

Les gobelins sont petits et faibles lorsqu'ils sont seuls ; ils préfèrent compter sur la ruse ou le surnombre. Chez eux, la règle est "la masse plutôt que la classe".

- Lorsque leur nombre est dix fois supérieur à celui de l'adversaire, les gobelins bénéficient d'un bonus de +1 à l'attaque.
- Les gobelins ne pèsent que 6 lbs, mais leur capacité de transport (4,4 lbs) est également moindre.
- Un gobelin au moins T4 en [discrétion][skill-discretion-id]{title="Stealth"} [dérobera][cmd-steal-fr-id] toujours au moins 50 Silver, même s'il est détecté.
- Les gobelins non armés ont un bonus de +2 à leur défense.
- Les gobelins blessés se régénèrent à hauteur de 10% de leurs points de vie.

## Halfelins

<!-- cspell:disable -->
*Halflings (EN), Halblinge (DE).*
<!-- cspell:enable -->

| PV | Armure naturelle | Résistance à la magie | Régénération | Recrutement |
|:--:|:----------------:|:---------------------:|:------------:|:-----------:|
| 18 |        0         |           5           |     5 %      |  80 silver  |

| Poids  | Capacité |
|:------:|:--------:|
| 10 lbs | 5,4 lbs  |

Les halfelins sont de petits compagnons aux pieds poilus. Ils sont de bons commerçants et savent divertir les paysans. Ce sont de bons bâtisseurs, mais ils préfèrent laisser les chevaux et les [bateaux][bateaux-id] aux autres. Le maniement des armes n'est pas leur point fort.

- Les halfelins qui essaient de [fuir][la-fuite] un combat, ont une chance de base de 50% (25% pour les autres peuples). Leur chance maximale est de 90% (75% pour les autres, voir [`COMBAT FLEE`][cmd-combat-fr]).
- Les halfelins ont un bonus de +5 en attaque et dégâts lorsqu'ils affrontent des [dragons][dragons-connus].
- Les halfelins sont bien plus sensibles que les autres à la famine. Ils perdent entre 8 and 17 points de vie (1d10+7).

## Insectes

<!-- cspell:disable -->
*Insects (EN), Insekten (DE).*
<!-- cspell:enable -->

| PV | Armure naturelle | Résistance à la magie | Régénération | Recrutement |
|:--:|:----------------:|:---------------------:|:------------:|:-----------:|
| 24 |        2         |           5           |     5 %      |  80 silver  |

| Poids  | Capacité |
|:------:|:--------:|
| 10 lbs | 5,4 lbs  |

!!! warning **Attention**
    Les insectes ne sont pas conseillés aux joueurs inexpérimentés !

Les insectes vivent dans un état strictement organisé.  
Ils détestent le froid, et au contraire aiment la chaleur et l'humidité.  
Leur carapace dure les protège de bien des agressions.  
Leur compétence et leur discipline font d'eux d'excellents enseignants.  

Les insectes aiment la chaleur et l'humidité et détestent le froid.  
Dans les déserts et les marais, régions qu'ils affectionnent, ils bénéficient d'un **bonus de +1** sur les compétences dans lesquelles ils sont **au moins T1**.  
Dans les montagnes et les glaciers, ils reçoivent un malus de **-1**.  

Les insectes ne peuvent normalement pas entrer dans les glaciers, et ne peuvent pas y être recrutés, il y fait trop froid.  
Ceux qui pénètrent malgré tout dans un glacier perdent des points de vie et voient leur compétence réduite de moitié selon la règle normale de la [famine][famine].

Durant les **mois d'hiver** ([Feu du Foyer][feu-du-foyer]{title="Hearth Fire"}, [Vent des Glaces][vent-des-glaces]{title="Icewind"} et [Neiges Envoûtantes][neiges-envoutantes]{title="Snowbane"}), les insectes peuvent **recruter uniquement dans les déserts**.  
Il est cependant possible grâce à l'[alchimie][alchimie]{title="Alchemy"} de [créer][make-potions-fr-id] une [potion de chaleur du nid][chaleur-du-nid]{title="Potion of nest warmth"} qui permet de recruter dans d'autres types de région.

Les insectes sont automatiquement protégés par leur armure naturelle de chitine.  
Cette armure naturelle sera réduite de moitié si les insectes portent une armure additionnelle (voir [ici][peuples-et-leurs-caracteristiques]).  

Les insectes obtiennent un bonus de [[tactique]] lorsqu'ils sont en nombre.  
Un tacticien insecte obtient (log<sub>10</sub> (nombre de combattants dans son groupe))-1 en tactique.  
Cela peut également entraîner un malus s'il y a très peu de combattants ! Attention, les unités dans différents [groupes][cmd-group-fr-id] sont gérées dans des armées différentes !  

Les insectes n'ont besoin d'aucune construction pour [commercer][le-commerce] dans les déserts et les marais.  

## Chats

<!-- cspell:disable -->
*Cats (EN), Katzen (DE).*
<!-- cspell:enable -->

| PV | Armure naturelle | Résistance à la magie | Régénération | Recrutement |
|:--:|:----------------:|:---------------------:|:------------:|:-----------:|
| 20 |        0         |           0           |     5 %      |  90 silver  |

| Poids  | Capacité |
|:------:|:--------:|
| 10 lbs | 5,4 lbs  |

Connus pour leurs sens développés, les chats font des espions excellents et des gardes hors-pairs . Mais, comme les elfes, ils n’aiment pas les travaux pénibles.

- « Sept vies » : les chats ont 1/7 chance de survivre à un coup mortel ; ils ont dans ce cas leurs points de vie maximum.
- Les chats ne peuvent porter d'[armure de plaque][armure-de-plaque]{title="Platemail"}.
- Leur Agilité confère aux chats un bonus de +1 en Défense

## Aquariens

<!-- cspell:disable -->
*Aquarians (EN), Meermenschen (DE).*
<!-- cspell:enable -->

| PV | Armure naturelle | Résistance à la magie | Régénération | Recrutement |
|:--:|:----------------:|:---------------------:|:------------:|:-----------:|
| 20 |        0         |           0           |     5 %      |  80 silver  |

| Poids  | Capacité |
|:------:|:--------:|
| 10 lbs | 5,4 lbs  |

Les Aquariens sont chez eux dans l’eau, mais sont plutôt mal à l’aise en montagne. Ils construisent et dirigent des bateaux de main de maître, alors que d'autres tâches leur sont plus compliquées.

- Tous les bateaux commandés par un capitaine Aquarien appartenant à une faction d'aquariens se [déplacent][deplacements] d'une région supplémentaire chaque semaine.
- Les aquariens peuvent exécuter des [ordres longs][ordres-courts-et-longs] sur les bateaux. Attention, cela a quelques conséquences implicites : Les aquariens peuvent par exemple se déplacer d'une région océanique adjacente à une région terrestre vers la région terrestre, voir [nager][nager].
- Sur une case d'océan (type de région océan) jusqu'à 100 aquariens embarqués peuvent gagner 10 Silver chacun avec l'ordre [`WORK`][cmd-work-fr].

## Humains

<!-- cspell:disable -->
*Humans (EN), Menschen (DE).*
<!-- cspell:enable -->

| PV | Armure naturelle | Résistance à la magie | Régénération | Recrutement |
|:--:|:----------------:|:---------------------:|:------------:|:-----------:|
| 20 |        0         |           0           |     5 %      |  75 silver  |

| Poids  | Capacité |
|:------:|:--------:|
| 10 lbs | 5,4 lbs  |

Les humains peuvent tout faire un peu. Ils n'ont aucune compétence vraiment mauvaise mais aucune de vraiment bonne non plus. Ils peuvent donc assez facilement combler les faiblesses d'autres peuples alliés, bien qu'ils n'aient aucune spécialisation.

- Immigrants : les factions d'humains sont les seules à être autorisées à avoir des personnes d'un autre peuple dans leurs rangs, bien que mélanger différents peuples dans une même unité ne soit pas possible. Cependant, ils ne peuvent pas les recruter eux-mêmes, mais doivent les [récupérer][cmd-give-fr] depuis d'autres factions. Il n'y a pas d'immigrants avec des [compétences payantes][competences], c'est-à-dire magie, alchimie, herboristerie, espionnage et tactique.

Le nombre d'immigrants se calcule ainsi :

<!-- cspell:disable -->
:   $$
    \text{nombre d'immigrants} = 20 \times \log_{10}\!\left(\frac{\text{taille de la faction}}{50}\right)
    $$
<!-- cspell:enable -->

*Nombre d'immigrants selon la taille de la faction.*

| Taille de la faction | 1 | 60 | 80 | 160 | 500 | 1 000 | 5 000 | 50 000 | 500 000 | 5 000 000 |
|----------------------|:-:|:--:|:--:|:---:|:---:|:-----:|:-----:|:------:|:-------:|:---------:|
| Nombre d'immigrants  | 0 | 1  | 4  | 10  | 20  |  26   |  40   |   60   |   80    |    100    |

??? tip "Calcul du nombre d'immigrants"
    <div class="md-typeset" style="margin-top: 1em;">
        <label for="races-compute-migrants-input" class="md-input-label">Taille faction :</label>
        <input id="races-compute-migrants-input" type="number" class="md-input" placeholder="nombre de personnnes">
        <button id="races-compute-migrants-btn" class="md-button md-button--primary" style="margin-top: 0.5em;">Calculer</button>
        <p style="margin-top: 1em;">Nombre d'immigrants : <strong id="races-compute-migrants-result">---</strong></p>
    </div>

Si l'on a soudainement trop d'immigrants à cause d'une catastrophe ou d'un combat, ceux-ci ne sont pas supprimés, on ne pourra juste plus en accueillir de nouveaux.  
Le nombre maximum d'immigrants est indiqué dans le rapport et, pour les grandes factions, il est presque identique au nombre de [Héros][cmd-promote-fr-id].

[](){ #orcs-fr-id }

## Orcs

<!-- cspell:disable -->
*Orcs (EN), Orks (DE).*
<!-- cspell:enable -->

| PV | Armure naturelle | Résistance à la magie | Régénération | Recrutement |
|:--:|:----------------:|:---------------------:|:------------:|:-----------:|
| 24 |        0         |          -5           |     5 %      |  70 silver  |

| Poids  | Capacité |
|:------:|:--------:|
| 10 lbs | 5,4 lbs  |

Les Orcs commencent leur vie en tant que combattants et la terminent généralement en tant que combattants. Leur force réside dans le nombre, mais ils manquent de jugeote.

- Combattants nés : Toutes les nouvelles recrues orcs commencent au niveau 1 en [mêlée][skill-melee-fr-id]{title="Melee"} et [combat à l'arme d'hast][combat-a-larme-dhast]{title="Polearm"}.
- Paresse : les orcs gagnent moins de silver que les autres peuples avec l'ordre [`WORK`][cmd-work-fr].
- Recrues faciles : Pour deux orcs recrutés, un seul paysan est soustrait du pool de paysans de la région. Ainsi vous pouvez recruter deux fois la limite de recrutement d'une région. La soustraction est arrondie au supérieur.
- De même : si vous donnez des orcs aux paysans avec l'ordre [`GIVE 0`][cmd-give-fr], seule la moitié d'entre eux est ajoutée aux paysans. Cela est arrondi à l'inférieur.
- Les orcs non armés ne combattent pas au corps à corps avec malus de -2 comme les autres peuples, mais avec ("meilleure compétence de combat corps à corps" -3). Ils ont toutefois besoin d’armes pour collecter les impôts.
- Les orcs ont le cerveau lent et apprennent généralement toutes les compétences un peu plus lentement que les autres peuples, hors celles de combat (cad celles pour maîtriser une arme).

[](){ #trolls-fr-id }

## Trolls

<!-- cspell:disable -->
*Trolls (EN), Trolle (DE).*
<!-- cspell:enable -->

| PV | Armure naturelle | Résistance à la magie | Régénération | Recrutement |
|:--:|:----------------:|:---------------------:|:------------:|:-----------:|
| 30 |        1         |          10           |    7,5 %     |  90 silver  |

| Poids  | Capacité |
|:------:|:--------:|
| 20 lbs | 10,8 lbs |

Ces rochers ambulants font partie des créatures les plus puissantes d'Eressea. Ils adorent travailler les pierres. Mais ils effraient les chevaux et la natation n'a jamais été considérée comme leur passe-temps favori.

- Les trolls sont forts et peuvent porter deux fois plus que les autres (10,8 lbs), mais ils pèsent aussi deux fois plus (20 lbs).
- Il n'y a pas de cavalerie troll, ce qui signifie que les trolls ne reçoivent pas de bonus de cheval. Cela n'a aucun effet sur le transport de marchandises et la vitesse de déplacement des trolls montés.
- Les pierres extraites par les trolls ne sont déduites qu'à 75% de la "réserve de la région". Cet effet est cumulatif avec une carrière (voir [ici][cercle-de-pierres] et [ici][ressources-minieres]).
- Contre les trolls, la cavalerie ennemie n'a qu'un bonus de +1 au lieu du +2 habituel.
- Les trolls sont le seul peuple capable d'utiliser des chariots sans chevaux. Les trolls peuvent tirer un chariot par quatre, mais ils ne peuvent se déplacer que d'une seule région (sauf route). Cela est expliqué plus en détail dans l'ordre [`RIDE`][cmd-ride-fr].
- Les trolls non armés infligent de 2 à 6 points de dégâts.
- Les trolls blessés se régénèrent à hauteur de 7,5% de leurs points de vie.

## Nains

<!-- cspell:disable -->
*Dwarves (EN), Zwerge (DE).*
<!-- cspell:enable -->

| PV | Armure naturelle | Résistance à la magie | Régénération | Recrutement |
|:--:|:----------------:|:---------------------:|:------------:|:-----------:|
| 24 |        0         |           5           |     5 %      | 110 silver  |

| Poids  | Capacité |
|:------:|:--------:|
| 10 lbs | 5,4 lbs  |

Les Nains vivent dans les montagnes, leurs armes sont réputées et leurs forteresses sont connues pour leur solidité. En revanche, ils sont tout aussi sceptiques à l'égard de la magie que des chevaux, et leurs compétences en matière de navigation sont parmi les plus mauvaises du monde.

- Le fer extrait par les nains n'est déduit qu'à 60% de la "réserve de la région". Cet effet est cumulatif avec une mine (voir [ici][mine-fr-id]{title="Mine"} et [ici][ressources-minieres]).
- Dans les montagnes et les glaciers, les nains obtiennent un bonus de +1en [tactique][tactique]{title="Tactics"}.
- Les [mages][magie] nains régénèrent leur aura beaucoup plus lentement que les autres.

Poursuivre la lecture : [Modificateurs de compétences][modificateurs-de-competences-id].

<!-- From [https://wiki.eressea.de/index.php?title=Rassen/fr&oldid=16646] -->

[cmd-combat-fr]: [[cmd-combat-fr]]
[cmd-give-fr]: [[cmd-give-fr]]
[cmd-hide-fr]: [[cmd-hide-fr]]
[cmd-work-fr]: [[cmd-work-fr]]
[cmd-ride-fr]: [[cmd-ride-fr]]
