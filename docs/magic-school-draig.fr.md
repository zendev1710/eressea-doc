---
# cSpell:locale fr
alias: sorts-draig
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Sorts Draig

Les sorts de l'École de magie **Draig** sont décrits ci-dessous par ordre de niveau croissant.  

*Note : Dans les descriptions ci-dessous N représente le niveau spécifié sur les ordres [[cmd-cast-fr]] ou [[cmd-combatspell-fr]] lancés.*

## Niveau 1

### Petites malédictions

<!-- cspell:disable -->
*Minor Curses (EN), Kleine Flüche (DE)*.
<!-- cspell:enable -->

:   Dans les ruelles les plus sombres, ils existent, les malédictions et les sortilèges sont faits sur commande.  
    Mais bien entendu le disciple de Draig propose aussi des contre-sorts.  
    Que le fils du voisin soit entraîné dans un sortilège d'amour ou que le rival ait des boutons et des verrues, personne n'aime admettre qu'il a eu recours à de telles mesures.  
    Pour ce service, le mage gagne 50 silver par niveau.

| Composants | Niv. |  Type  | Rang |              B               | D |
|:----------:|:----:|:------:|:----:|:----------------------------:|:-:|
|   N aura   |  1   | Normal |  5   | :material-check:{ .success } |   |

`CAST [LEVEL n] "Minor Curses"`  

### Imprécation

<!-- cspell:disable -->
*Hex (EN), Verwünschung (DE)*.
<!-- cspell:enable -->

:   La cible du mage est frappée par une malédiction inoffensive.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|   N aura   |  1   | Normal |  5   |   |   |

`CAST [LEVEL n] Hex <unit-id>`  

## Niveau 2

### Boule de feu

<!-- cspell:disable -->
*Fireball (EN), Feuerball (DE)*.
<!-- cspell:enable -->

:   Le sorcier lance un chaos ciblé dans les rangs ennemis. Le chaos en forme de boule blessera tous ceux qu'il touchera.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|   N aura   |  2   | Combat |  5   |   |   |

`COMBATSPELL [LEVEL n] "Fireball"`  

## Niveau 3

### Don du Chaos

<!-- cspell:disable -->
*Chaos Gift (EN), Gabe des Chaos (DE)*.
<!-- cspell:enable -->

:   Le mage ouvre son esprit aux sphères du Chaos et disposera ainsi de plus de pouvoir magique pendant un certain temps.  
    Mais l’aide des Seigneurs des Sphères a un prix, et la phase de pouvoir est donc remplacée par une phase de faiblesse.

| Composants | Niv. |  Type  | Rang |              B               | D |
|:----------:|:----:|:------:|:----:|:----------------------------:|:-:|
|   6 aura   |  3   | Normal |  3   | :material-check:{ .success } |   |

`CAST "Chaos Gift"`  

## Niveau 4

### Petit sacrifice de sang

<!-- cspell:disable -->
*Lesser Sacrifice (EN), Kleines Blutopfer (DE)*.
<!-- cspell:enable -->

:   Avec ce rituel, le mage peut sacrifier une partie de son énergie vitale afin d'acquérir un pouvoir magique.  
    Les mages rituels expérimentés rapportent que le rituel, une fois lancé, est difficile à contrôler et que la quantité de pouvoir gagnée varie considérablement.  
    Ainsi est-il écrit dans le « Livre du Sang » : « Qu'Il établisse donc le signe des quatre éléments dans le cercle de la création et de la décomposition et consacre chacun d'entre eux avec une goutte de sang.  
    Alors laissez-le aller au milieu des Quatre Éternels et laissez la vie passer pour que la force puisse naître. »

| Composants | Niv. |  Type  | Rang |              B               | D |
|:----------:|:----:|:------:|:----:|:----------------------------:|:-:|
|   16 PV    |  4   | Normal |  1   | :material-check:{ .success } |   |

`CAST "Lesser Sacrifice"`  

## Niveau 5

### Soif de sang

<!-- cspell:disable -->
*Blood Frenzy (EN), Blutrausch (DE)*.
<!-- cspell:enable -->

:   Dans ce rituel sanglant, le mage sacrifie un nouveau-né devant son armée avant le combat.  
    Les esprits du sang ainsi invoqués prendront possession des soldats et les plongeront dans une soif de sang.

|      Composants      | Niv. |  Type  | Rang | B | D |
|:--------------------:|:----:|:------:|:----:|:-:|:-:|
| 5 x N aura, 1 paysan |  5   | Pré-c. |  4   |   |   |

`COMBATSPELL [LEVEL n] "Blood Frenzy"`  

### Malédiction du Chaos

<!-- cspell:disable -->
*Chaos Curse (EN), Chaosfluch (DE)*.
<!-- cspell:enable -->

:   Cette malédiction insidieuse altère considérablement les capacités magiques de la victime.  
    Une zone magique de chaos autour de la victime réduit sa capacité de concentration et rend très difficile le lancement de sorts.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 4 x N aura |  5   | Normal |  4   |   |   |

`CAST [LEVEL n] "Chaos Curse" <unit-id>`  

## Niveau 6

### Créer une [[amulette-de-vision-decuplee]]

<!-- cspell:disable -->
*Create An Amulet of True Sight (EN), Erschaffe ein Amulett des wahren Sehens (DE)*.
<!-- cspell:enable -->

:   Le sort permet à un mage de créer une [amulette de vision décuplée][amulette-de-vision-decuplee]{title="Amulet of True Sight"}.  
    L'amulette permet au porteur de voir toutes les unités protégées par un [anneau d'Invisibilité][anneau-dinvisibilite]{title="Ring of Invisibility"}.  
    Cependant, les unités qui utilisent leur compétence de [discrétion][skill-discretion-id]{title="Stealth"} pour se cacher ne sont toujours pas détectées.

|               Composants                | Niv. |  Type  | Rang |              B               | D |
|:---------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-:|
| 50 aura, 3 000 silver, 1 aura permanent |  6   | Normal |  5   | :material-check:{ .success } |   |

`CAST "Create An Amulet of True Sight"`  

### Créer un [anneau d'Invisibilité][anneau-dinvisibilite]{title="Ring of Invisibility"}

<!-- cspell:disable -->
*Create A Ring of Invisibility (EN), Erschaffe einen Ring der Unsichtbarkeit (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le sorcier peut créer un [anneau d'Invisibilité][anneau-dinvisibilite]{title="Ring of Invisibility"}.  
    Le porteur de l'anneau devient invisible pour toutes les unités des autres partis, quelle que soit la qualité de leur perception.  
    Dans une unité invisible, chaque personne doit porter une bague.

|               Composants                | Niv. |  Type  | Rang |              B               | D |
|:---------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-:|
| 50 aura, 3 000 silver, 1 aura permanent |  6   | Normal |  5   | :material-check:{ .success } |   |

`CAST "Create A Ring of Invisibility"`  

### Pouvoirs des morts

<!-- cspell:disable -->
*Animate Dead (EN), Mächte des Todes (DE)*.
<!-- cspell:enable -->

:   Le mage noir doit passer des nuits à errer dans les cimetières et cimetières de la région afin de pouvoir faire revivre les cadavres déterrés.  
    Les morts-vivants seront à son service, mais les non-informés doivent savoir qu'invoquer les forces de la mort peut être une arme à double tranchant.

| Composants | Niv. |  Type  | Rang |              B               |              D               |
|:----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
| 5 x N aura |  6   | Normal |  5   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Animate Dead"`  

### Vents de rouille

<!-- cspell:disable -->
*Winds of Rust (EN), Rosthauch (DE)*.
<!-- cspell:enable -->

:   Ce rituel évoque un sombre front de tempête qui domine de façon menaçante la région.  
    La pluie magique fera rouiller tout le minerai, détruisant de nombreuses armes ennemies.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 2 x N aura |  6   | Combat |  5   |   |   |

`COMBATSPELL [LEVEL n] "Winds of Rust"`  

## Niveau 7

### Mur de feu

<!-- cspell:disable -->
*Firewall (EN), Feuerwand (DE)*.
<!-- cspell:enable -->

:   L'assistant crée un mur de feu dans la direction spécifiée.
    Cela fait mal à tous ceux qui le traversent.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 6 x N aura |  7   | Normal |  4   |   |   |

`CAST [LEVEL n] "Firewall" <direction>`  

### Malédiction de la peste

<!-- cspell:disable -->
*Curse of Pestilence (EN), Fluch der Pestilenz (DE)*.
<!-- cspell:enable -->

:   Dans un rituel élaboré, le mage noir sacrifie quelques paysans puis distribue comme par magie les cadavres dans les puits de la région.

|     Composants      | Niv. |  Type  | Rang | B |              D               |
|:-------------------:|:----:|:------:|:----:|:-:|:----------------------------:|
| 30 aura, 50 paysans |  7   | Normal |  5   |   | :material-check:{ .success } |

`CAST [REGION x y] "Curse of Pestilence"`  

### Transfert de pouvoir

<!-- cspell:disable -->
*Transfer Power (EN), Machtübertragung (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le mage peut transférer sa propre aura dans un rapport de 2:1 à un autre mage de la même École de Magie.

| Composants | Niv. |  Type  | Rang |              B               | D |
|:----------:|:----:|:------:|:----:|:----------------------------:|:-:|
|   2 aura   |  7   | Normal |  1   | :material-check:{ .success } |   |

`CAST "Transfer Power" <unit-id> <Aura>`  

## Niveau 8

### Invocation des Démons de l'Ombre

<!-- cspell:disable -->
*Summon Shadowdemons (EN), Beschwöre Schattendämonen (DE)*.
<!-- cspell:enable -->

:   À l’aide de rituels sombres, le mage invoque des démons depuis la sphère des ombres.  
    Ces créatures redoutées peuvent se déplacer de manière presque invisible parmi les vivants, mais leur aura sombre peut être ressentie par tout le monde.  
    Les démons de l’ombre sont des adversaires redoutés au combat.  
    Ils sont difficiles à toucher et drainent la puissance de leur adversaire.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 3 x N aura |  8   | Normal |  5   |   |   |

`CAST [LEVEL n] "Summon Shadowdemons"`  

### Folie de la guerre

<!-- cspell:disable -->
*Madness of War (EN), Wahnsinn des Krieges (DE)*.
<!-- cspell:enable -->

:   Devant les soldats ennemis, le mage noir sacrifie les dix pions dans un rituel sanglant et cruel et invoque ainsi les esprits de la folie sur les troupes ennemies.  
    Ils réagiront confusément au combat et seront incapables de suivre les ordres de leurs officiers.

|      Composants       | Niv. |  Type  | Rang | B | D |
|:---------------------:|:----:|:------:|:----:|:-:|:-:|
| 3 x N aura, 10 Bauern |  8   | Pré-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] "Madness of War"`  

## Niveau 9

### Fuite de l'Astral

<!-- cspell:disable -->
*Astral Leak (EN), Astraler Riss (DE)*.
<!-- cspell:enable -->

:   Avec ce sombre rituel, le mage noir peut provoquer une rupture dans le tissu magique, qui arrachera tout pouvoir magique de la région.  
    Toutes les personnes douées pour la magie dans la région perdront une grande partie de leur aura.

|          Composants           | Niv. |  Type  | Rang | B | D |
|:-----------------------------:|:----:|:------:|:----:|:-:|:-:|
| 35 aura, 1 [[sang-de-dragon]] |  9   | Normal |  3   |   |   |

`CAST "Astral Leak"`  

### Chaos de l'Astral

<!-- cspell:disable -->
*Astral Chaos (EN), Astrales Chaos (DE)*.
<!-- cspell:enable -->

:   Ce rituel, effectué avant la bataille, fait tourbillonner les énergies astrales sur le champ de bataille, rendant plus difficile le lancement de leurs sorts par les mages ennemis.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 6 x N aura |  9   | Pré-c. |  2   |   |   |

`COMBATSPELL [LEVEL n] "Astral Chaos"`  

### Créer une [[ceinture-de-force-de-troll]]

<!-- cspell:disable -->
*Create A Belt of Troll Strength (EN), Erschaffe einen Gürtel der Trollstärke (DE)*.
<!-- cspell:enable -->

:   Cet artefact magique confère à son porteur la force d'un Troll des Cavernes adulte.  
    Sa capacité de charge est multipliée par 50 et sa force accrue et sa peau résistante aux trolls auront également un effet positif au combat.

|        Composants         | Niv. |  Type  | Rang |              B               | D |
|:-------------------------:|:----:|:------:|:----:|:----------------------------:|:-:|
| 20 aura, 1 aura permanent |  9   | Normal |  5   | :material-check:{ .success } |   |

`CAST "Create A Belt of Troll Strength"`  

### Héros morts‑vivants

<!-- cspell:disable -->
*Undead Heroes (EN), Untote Helden (DE)*.
<!-- cspell:enable -->

:   Ce rituel lie les âmes déjà en fuite de certaines victimes de la bataille à leurs cadavres, les ressuscitant à la vie des morts-vivants.  
    Qu’ils aient déjà combattu du côté de l’ennemi ou du leur n’a aucune importance pour le rituel.

| Composants | Niv. |  Type   | Rang | B | D |
|:----------:|:----:|:-------:|:----:|:-:|:-:|
|   N aura   |  9   | Post-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] "Undead Heroes"`  

## Niveau 10

### Diable de feu

<!-- cspell:disable -->
*Fire Fiend (EN), Feuerteufel (DE)*.
<!-- cspell:enable -->

:   Cette invocation élémentaire invoque un diable de feu, une créature venue des profondeurs des enfers enflammés.  
    Le diable de feu se jettera avec impatience sur les forêts de la région et les incendiera.

|               Composants               | Niv. |  Type  | Rang | B |              D               |
|:--------------------------------------:|:----:|:------:|:----:|:-:|:----------------------------:|
| 50 aura, 1 [huile][huile]{title="Oil"} |  10  | Normal |  5   |   | :material-check:{ .success } |

`CAST [REGION x y] "Fire Fiend"`  

### Pentagramme

<!-- cspell:disable -->
*Pentagram (EN), Pentagramm (DE)*.
<!-- cspell:enable -->

:   Exactement à minuit, lorsque les pouvoirs des ténèbres sont à leur maximum, un mage noir peut également utiliser ses pouvoirs pour supprimer les enchantements.  
Pour ce faire, il dessine un pentagramme sur l'objet enchanté et commence par une invocation aux seigneurs des ténèbres.  
Les messieurs l'aideront, mais sa réussite à résoudre le sort dépend uniquement de sa propre force.

| Composants  | Niv. |  Type  | Rang |              B               |              D               |
|:-----------:|:----:|:------:|:----:|:----------------------------:|:----------------------------:|
| 10 x N aura |  10  | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] Pentagram ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

## Niveau 11

### Invocation du Dragon

<!-- cspell:disable -->
*Dragon Call (EN), Drachenruf (DE)*.
<!-- cspell:enable -->

:   Avec ce sombre rituel, le mage crée un leurre dont l'odeur est irrésistible pour les [Dragons][dragons-fr-id].  
    Il n'a pas encore été possible de déterminer si les dragons viennent des environs ou de la sphère du chaos.  
    On dit que les deux se sont déjà produits.  
    L'appât dure environ 6 semaines, mais doit être placé sur un terrain adapté aux cerfs-volants.

|          Composants           | Niv. |  Type  | Rang | B |              D               |
|:-----------------------------:|:----:|:------:|:----:|:-:|:----------------------------:|
| 80 aura, 1 [[tete-de-dragon]] |  11  | Normal |  5   |   | :material-check:{ .success } |

`CAST [REGION x y] "Dragon Call"`  

### Nuage de la Mort

<!-- cspell:disable -->
*Death Cloud (EN), Todeswolke (DE)*.
<!-- cspell:enable -->

:   Avec un sombre rituel et en sacrifiant son propre sang, le mage noir invoque un grand esprit du plan élémentaire des poisons.  
    L'esprit se manifeste sous la forme d'un nuage vert vif au-dessus de la région et nuira à tous ceux qui entreront en contact avec lui.

|   Composants   | Niv. |  Type  | Rang | B |              D               |
|:--------------:|:----:|:------:|:----:|:-:|:----------------------------:|
| 40 aura, 15 PV |  11  | Normal |  5   |   | :material-check:{ .success } |

`CAST [REGION x y] "Death Cloud"`  

## Niveau 12

### Invocation des Maîtres de l'Ombre

<!-- cspell:disable -->
*Summon Shadowmasters (EN), Beschwöre Schattenmeister (DE)*.
<!-- cspell:enable -->

:   À l’aide de rituels sombres, le mage invoque des démons depuis la sphère des ombres.  
    Ces créatures redoutées peuvent se déplacer de manière presque invisible parmi les vivants, mais leur aura sombre peut être ressentie par tout le monde.  
    Au combat, les maîtres de l’ombre sont des adversaires redoutés.  
    Ils sont difficiles à frapper et drainent la force et la vie de leur adversaire.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 7 x N aura |  12  | Normal |  5   |   |   |

`CAST [LEVEL n] "Summon Shadowmasters"`  

### Créer une [[epee-de-flammes]]

<!-- cspell:disable -->
*Create A Flaming Sword (EN), Erschaffe ein Flammenschwert (DE)*.
<!-- cspell:enable -->

:   "Et alors frottez le sang d'un féroce combattant dans l'acier de la lame et commencez l'invocation des Sphères du Chaos.  
    Et si vous avez tout fait pour leur plaire, ils enverront l'un des leurs pour imprégner l'épée de son pouvoir..."

|                                                          Composants                                                           | Niv. |  Type  | Rang |              B               | D |
|:-----------------------------------------------------------------------------------------------------------------------------:|:----:|:------:|:----:|:----------------------------:|:-:|
| 100 aura, 1 [sang de berserker][sang-de-berserker]{title="Berserkers blood"}, 1 [épée][epee]{title="Sword"}, 1 aura permanent |  12  | Normal |  5   | :material-check:{ .success } |   |

`CAST "Create A Flaming Sword"`  

## Niveau 13

### Invocation du Familier

<!-- cspell:disable -->
*Summon Familiar (EN), Vertrauten rufen (DE)*.
<!-- cspell:enable -->

:   À un moment donné de ses pérégrinations, un mage expérimenté rencontrera un spécimen inhabituel d'une espèce qui rejoindra le mage.

|         Composants          | Niv. |  Type  | Rang | B | D |
|:---------------------------:|:----:|:------:|:----:|:-:|:-:|
| 100 aura, 5 aura permanents |  13  | Normal |  5   |   |   |

`CAST "Summon Familiar"`  

## Niveau 14

### Portail du Chaos

<!-- cspell:disable -->
*Chaos Gate (EN), Chaossog (DE)*.
<!-- cspell:enable -->

:   En sacrifiant 200 paysans, le mage du chaos peut ouvrir une porte vers le monde Astral.  
    Le portail peut être utilisé la semaine suivante, il se dissout à la fin de la semaine suivante.

|      Composants       | Niv. |  Type  | Rang | B | D |
|:---------------------:|:----:|:------:|:----:|:-:|:-:|
| 150 aura, 200 paysans |  14  | Normal |  5   |   |   |

`CAST "Chaos Gate"`  

### Force impie

<!-- cspell:disable -->
*Unholy Strength (EN), Unheilige Kraft (DE)*.
<!-- cspell:enable -->

:   Ce rituel n’est transmis aux adeptes des académies obscures qu’à voix basse, car c’est l’un des plus sombres jamais écrits.  
    En invoquant des démons impies, le pouvoir des morts-vivants est amplifié et ils se transforment en monstres morts-vivants d'une grande puissance.

|         Composants         | Niv. |  Type  | Rang | B | D |
|:--------------------------:|:----:|:------:|:----:|:-:|:-:|
| 10 x N aura, 5 x N paysans |  14  | Normal |  5   |   |   |

`CAST [LEVEL n] "Unholy Strength" <unit-id> [<unit-id> ...]`  

<!-- From [https://wiki.eressea.de/index.php?title=Draigzauber&oldid=6510] -->
