---
# cSpell:locale fr
alias: sorts-tybied
---
# Sorts Tybied

Les sorts de l'École de magie **Tybied** sont décrits ci-dessous par ordre de niveau croissant.

## Niveau 1

### Analyse de la Magie

<!-- cspell:disable -->
*Analyze Magic (EN), Magie analysieren (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au mage de tenter de détecter les enchantements d'un seul objet spécifié.  
    Il pourra se faire une idée de leur efficacité grâce à tous les sorts qui ne dépassent pas ses propres capacités.  
    Avec des sorts plus puissants, il lui faut un peu de chance pour réussir son analyse.

| Composants | Niv. |  Type  | Rang |         B          | D |
|:----------:|:----:|:------:|:----:|:------------------:|:-:|
|  N auras   |  1   | Normal |  5   | :heavy_check_mark: |   |

`CAST [LEVEL n] "Analyze Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Dissimulation d'aura

<!-- cspell:disable -->
*Concealing Aura (EN), Schleieraura (DE)*.
<!-- cspell:enable -->

:   Ce sort masquera tout l'équipement de l'unité cible pendant un certain temps.

| Composants | Niv. |  Type  | Rang |         B          | D |
|:----------:|:----:|:------:|:----:|:------------------:|:-:|
|  N auras   |  1   | Normal |  5   | :heavy_check_mark: |   |

 `CAST [LEVEL n] "Concealing Aura" <unit-id>`  

### Docteur Miracle

<!-- cspell:disable -->
*Miracle Doctor (EN), Wunderdoktor (DE)*.
<!-- cspell:enable -->

:   Si l'alchimiste ne peut pas vous aider, vous vous adressez au savant mage Tybied.  
    Ses potions et teintures aident contre tout ce que vous ne pouvez pas obtenir autrement.  
    Si la formule énigmatique sous le sabot du mari infidèle a vraiment aidé, eh bien, le fermier qui ne sait pas lire ne le saura jamais.  
    Cela aide certainement le mage... à remplir son portefeuille. Vous pouvez gagner 50 silver par niveau en une semaine.

| Composants | Niv. |  Type  | Rang |         B          | D |
|:----------:|:----:|:------:|:----:|:------------------:|:-:|
|  N auras   |  1   | Normal |  5   | :heavy_check_mark: |   |

`CAST [LEVEL n] "Miracle Doctor"`  

## Niveau 2

### Protection contre la magie

<!-- cspell:disable -->
*Protection from Magic (EN), Schutz vor Magie (DE)*.
<!-- cspell:enable -->

:   Ce sort place un champ d'antimagie autour des mages ennemis, gênant considérablement leur lancement de sorts.  
    Seuls quelques-uns auront la force de pénétrer sur le terrain et d’aider leurs troupes au combat.

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 3 x N auras |  2   | Pré-c. |  2   |   |   |

`COMBATSPELL [LEVEL n] "Protection from Magic"`  

## Niveau 3

### Préservation du butin

<!-- cspell:disable -->
*Save Spoils (EN), Beute Bewahren (DE)*.
<!-- cspell:enable -->

:   Ce sort empêche certains objets qui seraient normalement détruits au combat de subir des dommages.  
    Les pertes sont réduites de 5 % par niveau du sort, jusqu'à un minimum de 25 %.

| Composants | Niv. |  Type   | Rang | B | D |
|:----------:|:----:|:-------:|:----:|:-:|:-:|
|  N auras   |  3   | Post-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] "Save Spoils"`  

### Résistance à la magie

<!-- cspell:disable -->
*Resist Magic (EN), Schutzzauber (DE)*.
<!-- cspell:enable -->

:   Ce sort augmente votre résistance naturelle à la magie.  
    Une unité ainsi protégée est également moins vulnérable à la magie de combat.  
    Par niveau, le pouvoir du mage est suffisant pour protéger 5 personnes.

| Composants  | Niv. |  Type  | Rang |         B          | D |
|:-----------:|:----:|:------:|:----:|:------------------:|:-:|
| 5 x N auras |  3   | Normal |  2   | :heavy_check_mark: |   |

`CAST [LEVEL n] Resist Magic <unit-id> [<unit-id> ...]`  

## Niveau 4

### Sortie de l'Astral

<!-- cspell:disable -->
*Astral Exit (EN), Astraler Ausgang (DE)*.
<!-- cspell:enable -->

:   Le mage se concentre sur la structure de la réalité et peut ainsi quitter le plan Astral.  
    Il peut globalement (Niveau-3)*Envoyer 15 kg par la porte brièvement créée.  
    Si le mage est suffisamment expérimenté pour lancer le sort aux niveaux 11 ou plus, il peut forcer d'autres unités à passer à l'autre niveau, même contre leur gré.

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 2 x N auras |  4   | Normal |  7   |   |   |

`CAST [LEVEL n] "Astral Exit" <x> <y> <unit-id> [<unit-id> ...]`  

### Voie de l'Astral

<!-- cspell:disable -->
*Astral Path (EN), Astraler Weg (DE)*.
<!-- cspell:enable -->

:   D'anciennes formules arcaniques permettent au mage de s'envoyer lui-même et les autres dans le plan Astral.  
    Le mage peut envoyer 15 kg par la porte brièvement créée.  
    Si le mage est suffisamment expérimenté pour lancer le sort aux niveaux 11 ou plus, il peut forcer d'autres unités à passer à l'autre niveau, même contre leur gré.

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 2 x N auras |  4   | Normal |  7   |   |   |

`CAST [LEVEL n] "Astral Path" <unit-id> [<unit-id> ...]`  

## Niveau 5

### Antimagie

<!-- cspell:disable -->
*Antimagic (EN), Astrale Schwächezone (DE)*.
<!-- cspell:enable -->

:   Avec ce sort le mage peut créer une zone d'affaiblissement Astral, un déséquilibre local dans le champ Astral.  
    Cette zone s'efforcera de revenir à l'équilibre.  
    Pour ce faire, il supprimera une partie de la force de chaque sort lancé dans cette région et même absorbera complètement les plus faibles.

| Composants  | Niv. |  Type  | Rang | B |         D          |
|:-----------:|:----:|:------:|:----:|:-:|:------------------:|
| 3 x N auras |  5   | Normal |  2   |   | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Antimagic"`  

### Transfert d'aura

<!-- cspell:disable -->
*Transfer Aura (EN), Auratransfer (DE)*.
<!-- cspell:enable -->

:   À l'aide de ce sort, le mage peut transférer sa propre aura à un autre mage de la même École de Magie dans un rapport de 2:1 ou à un mage d'une autre École de Magie dans un rapport de 3:1.

| Composants | Niv. |  Type  | Rang |         B          | D |
|:----------:|:----:|:------:|:----:|:------------------:|:-:|
|   1 aura   |  5   | Normal |  1   | :heavy_check_mark: |   |

`CAST "Transfer aura" <unit-id> <Aura>`  

### Dévoreur de magie

<!-- cspell:disable -->
*Destroy Magic (EN), Magiefresser (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au mage de dissiper les enchantements sur une unité, un bateau, un bâtiment ou même une région.

| Composants  | Niv. |  Type  | Rang |         B          |         D          |
|:-----------:|:----:|:------:|:----:|:------------------:|:------------------:|
| 4 x N auras |  5   | Normal |  2   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Destroy Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> | CASTLE <building-id> )`  

### Onde de choc

<!-- cspell:disable -->
*Shockwave (EN), Schockwelle (DE)*.
<!-- cspell:enable -->

:   Ce sort provoque une vague de puissance pure qui déferle sur les rangs ennemis.  
    Le choc laissera de nombreux combattants tellement hébétés qu’ils seront incapables d’attaquer pendant un bref instant.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|  N auras   |  5   | Combat |  5   |   |   |

`COMBATSPELL [LEVEL n] Shockwave`  

## Niveau 6

### Invocation de l'Astral

<!-- cspell:disable -->
*Astral Call (EN), Astraler Ruf (DE)*.
<!-- cspell:enable -->

:   Un mage qui se trouve dans le plan Astral peut utiliser ce sort pour lui amener d'autres unités.  
    Le mage peut (niveau 3)*Envoyer 15 kg par la porte brièvement créée.  
    Si le mage est suffisamment expérimenté pour lancer le sort aux niveaux 13 ou plus, il peut forcer d'autres unités à passer à l'autre niveau, même contre leur gré.

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 2 x N auras |  6   | Normal |  7   |   |   |

`CAST [LEVEL n] "Astral Call" <x> <y> <unit-id> [<unit-id> ...]`  

### Créer une [[amulette-de-vision-decuplee]]

<!-- cspell:disable -->
*Create An Amulet of True Sight (EN), Erschaffe ein Amulett des wahren Sehens (DE)*.
<!-- cspell:enable -->

:   Le sort permet à un mage de créer une [amulette de vision décuplée].  
    L'amulette permet au porteur de voir toutes les unités protégées par un [anneau d'Invisibilité].  
    Cependant, les unités qui utilisent leur compétence de [camouflage] pour se cacher ne sont toujours pas détectées.

|                Composants                | Niv. |  Type  | Rang |         B          | D |
|:----------------------------------------:|:----:|:------:|:----:|:------------------:|:-:|
| 50 auras, 3 000 silver, 1 aura permanent |  6   | Normal |  5   | :heavy_check_mark: |   |

`CAST "Create An Amulet of True Sight"`  

### Créer un [anneau d'Invisibilité]

<!-- cspell:disable -->
*Create A Ring of Invisibility (EN), Erschaffe einen Ring der Unsichtbarkeit (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le sorcier peut créer un [anneau d'Invisibilité].  
    Le porteur de l'anneau devient invisible pour toutes les unités des autres partis, quelle que soit la qualité de leur perception.  
    Dans une unité invisible, chaque personne doit porter une bague.

|                Composants                | Niv. |  Type  | Rang |         B          | D |
|:----------------------------------------:|:----:|:------:|:----:|:------------------:|:-:|
| 50 auras, 3 000 silver, 1 aura permanent |  6   | Normal |  5   | :heavy_check_mark: |   |

`CAST "Create A Ring of Invisibility"`  

### Dirigeable

<!-- cspell:disable -->
*Airship (EN), Luftschiff (DE)*.
<!-- cspell:enable -->

:   Ces runes magiques font voler un bateau ou une chaloupe pendant une semaine.  
    Cela peut alors également être utilisé pour traverser des terres.  
    Pour la couleur des runes, une encre spéciale doit être mélangée à partir d'un chou à la crème et d'un cristal de neige.

|                      Composants                      | Niv. |  Type  | Rang |         B          | D |
|:----------------------------------------------------:|:----:|:------:|:----:|:------------------:|:-:|
| 10 auras, 1 [gousse], 1 [pétale de cristal de neige] |  6   | Normal |  5   | :heavy_check_mark: |   |

`CAST Airship <ship-id>`  

### Invocation de la Réalité

<!-- cspell:disable -->
*Call of Reality (EN), Ruf der Realität (DE)*.
<!-- cspell:enable -->

:   Un mage qui se trouve dans le monde matériel peut utiliser ce sort pour invoquer des unités du monde Astral adjacent.  
    Si le mage est suffisamment expérimenté pour lancer le sort à des niveaux de 13 ou plus, il peut forcer d'autres unités à entrer dans le monde matériel contre leur gré.

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 2 x N auras |  6   | Normal |  7   |   |   |

`CAST [LEVEL n] "Call of Reality" <unit-id> [<unit-id> ...]`  

### Vol d'aura

<!-- cspell:disable -->
*Steal Aura (EN), Stehle Aura (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le mage peut retirer son aura à un autre mage contre son gré et se la fournir.  

| Composants  | Niv. |  Type  | Rang | B |         D          |
|:-----------:|:----:|:------:|:----:|:-:|:------------------:|
| 2 x N auras |  6   | Normal |  3   |   | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Steal Aura" <unit-id>`  

## Niveau 7

### Créer un [Cristal d'Antimagie]

<!-- cspell:disable -->
*Create An Antimagic Crystal (EN), Erschaffe Antimagiekristall (DE)*.
<!-- cspell:enable -->

:   À l'aide de ce sort, le mage draine un cristal de quartz de toutes ses énergies magiques.  
    Le cristal, une fois broyé en une fine poussière et dispersé, absorbera les énergies magiques libérées lors du lancement et réduira la puissance de tous les sorts lancés dans la région cette semaine-là.

|       Composants       | Niv. |  Type  | Rang |         B          | D |
|:----------------------:|:----:|:------:|:----:|:------------------:|:-:|
| 50 auras, 3 000 silver |  7   | Normal |  5   | :heavy_check_mark: |   |

`CAST "Create An Antimagic Crystal"`  

### Brise‑malédiction

<!-- cspell:disable -->
*Negate Curse (EN), Fluch brechen (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au mage de dissiper spécifiquement un enchantement spécifique sur une unité, un bateau, un bâtiment ou même la région.

| Composants  | Niv. |  Type  | Rang |         B          |         D          |
|:-----------:|:----:|:------:|:----:|:------------------:|:------------------:|
| 3 x N auras |  7   | Normal |  3   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Negate Curse" ( REGION | UNIT <unit-id> | SHIP <ship-id> | CASTLE <building-id> ) <spell-id>`  

### Murs d'éternité

<!-- cspell:disable -->
*Eternal Walls (EN), Mauern der Ewigkeit (DE)*.
<!-- cspell:enable -->

:   Avec cette formule, le mage lie pour toujours les forces de la terre dans les murs du bâtiment.  
    Un bâtiment ainsi enchanté est protégé contre les agressions du temps et ne nécessite plus aucun entretien.

|         Composants         | Niv. |  Type  | Rang |         B          | D |
|:--------------------------:|:----:|:------:|:----:|:------------------:|:-:|
| 50 auras, 1 aura permanent |  7   | Normal |  5   | :heavy_check_mark: |   |

`CAST [LEVEL n] "Eternal Walls" <building-id>`  

## Niveau 8

### Runes de protection

<!-- cspell:disable -->
*Protective Runes (EN), Runen des Schutzes (DE)*.
<!-- cspell:enable -->

:   Si vous dessinez ces runes sur les murs d’un bâtiment ou sur les planches d’un bateau, il sera plus difficile de les influencer par magie.  
    Chaque rituel augmente la résistance du bâtiment ou du bateau à l'enchantement de 20 %.  
    Si plusieurs sorts de protection sont superposés, leurs effets s'additionnent, mais une protection à 100 % ne peut pas être obtenue de cette façon.  
    Le sort dure au moins trois semaines, mais selon la compétence du mage, il peut durer beaucoup plus longtemps.

| Composants | Niv. |  Type  | Rang |         B          | D |
|:----------:|:----:|:------:|:----:|:------------------:|:-:|
|  20 auras  |  8   | Normal |  2   | :heavy_check_mark: |   |

`CAST "Protective Runes" ( SHIP <ship-id> | CASTLE <building-id> )`  

### Bouclier du poisson

<!-- cspell:disable -->
*Shield of the Fish (EN), Schild des Fisches (DE)*.
<!-- cspell:enable -->

:   Ce sort peut donner à l'ennemi une image légèrement différente de ses propres troupes, tout comme le poisson dans l'eau n'est pas là où il semble être.  
    De cette façon, la moitié des dégâts de chaque coup peuvent être rendus inoffensifs.  
    Mais le bouclier ne peut résister que quelques centaines de coups d’épée, après quoi il se désintègre.  
    Plus le mage est fort, plus le bouclier peut résister aux dégâts.

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 4 x N auras |  8   | Pré-c. |  2   |   |   |

`COMBATSPELL [LEVEL n] "Shield of the Fish"`  

## Niveau 9

### Accélération

<!-- cspell:disable -->
*Acceleration (EN), Beschleunigung (DE)*.
<!-- cspell:enable -->

:   Ce sort accélère certains combattants de votre côté afin qu'ils puissent attaquer deux fois en un seul round de combat, tout au long du combat.  

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 5 x N auras |  9   | Pré-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] Acceleration`  

### Créer un [[anneau-de-pouvoir]]

<!-- cspell:disable -->
*Ring of Power (EN), Erschaffe einen Ring der Macht (DE)*.
<!-- cspell:enable -->

:   Ce rituel puissant crée un [[anneau-de-pouvoir]]. Celui-ci augmente la puissance de tout sort lancé par son porteur, comme si le mage était supérieur d'un niveau.

|                Composants                 | Niv. |  Type  | Rang |         B          | D |
|:-----------------------------------------:|:----:|:------:|:----:|:------------------:|:-:|
| 100 auras, 1 aura permanent, 4 000 silver |  9   | Normal |  5   | :heavy_check_mark: |   |

`CAST "Create A Ring of Power"`  

## Niveau 10

### Blick in die Realität <!-- TODO -->

<!-- cspell:disable -->
*(EN), Blick in die Realität (DE)*.
<!-- cspell:enable -->

:   Grâce à ce sort, le mage peut regarder du plan Astral vers le plan matériel et reconnaître avec précision les régions et les unités.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|  40 auras  |  10  | Normal |  5   |   |   |

`CAST "Blick in die Realität"`  

### Créer un [[sac-a-poids-negatif]] <!-- TODO: check -->

<!-- cspell:disable -->
*Create A Bag of Negative Weight (EN), Erschaffe einen Beutel des Negativen Gewichts (DE)*.
<!-- cspell:enable -->

:   Ce sac renferme un petit pli dimensionnel dans lequel jusqu'à 200 unités de poids peuvent être transportées sans être comptées dans le poids transporté.  
    Les chevaux et autres êtres vivants ainsi que les objets particulièrement volumineux (chars et catapultes) ne peuvent pas être transportés dans le sac.  
    Il n'est pas non plus possible de transporter un sac magique dans un autre. Le sac lui-même pèse 1 kg.

|                Composants                | Niv. |  Type  | Rang |         B          | D |
|:----------------------------------------:|:----:|:------:|:----:|:------------------:|:-:|
| 30 auras, 1 aura permanent, 5 000 silver |  10  | Normal |  5   | :heavy_check_mark: |   |

`CAST "Create A Bag of Negative Weight"`   <!-- TODO: check -->

## Niveau 11

### Zeitdehnung

<!-- cspell:disable -->
*(EN), Zeitdehnung (DE)*.
<!-- cspell:enable -->

:   Cette application pratique des connaissances théoriques sur l’espace et le temps permet de modifier l’écoulement du temps pour certaines personnes.  
    Les personnes ainsi modifiées obtiennent deux fois plus de points de mouvement et deux fois plus d'attaques par round pendant quelques semaines.

| Composants  | Niv. |  Type  | Rang |         B          | D |
|:-----------:|:----:|:------:|:----:|:------------------:|:-:|
| 5 x N auras |  11  | Normal |  5   | :heavy_check_mark: |   |

`CAST [LEVEL n] "Zeitdehnung" <unit-id> [<Unit-id> ...]`  

## Niveau 12

### Bouclier d'armure

<!-- TODO: check if it is really Armor Shield -->
<!-- cspell:disable -->
*Armor Shield (EN), Rüstschild (DE)*.
<!-- cspell:enable -->

:   Ce rituel, qui peut être lancé avant le combat, confère à vos troupes un bonus supplémentaire à leur armure.  
    Chaque coup réduit la puissance du sort, le bouclier se dissipera donc à un moment donné du combat.

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 4 x N auras |  12  | Pré-c. |  2   |   |   |

`COMBATSPELL [LEVEL n] "Armor Shield"`  

### Invocation du Familier

<!-- cspell:disable -->
*Summon Familiar (EN), Vertrauten rufen (DE)*.
<!-- cspell:enable -->

:   À un moment donné de ses pérégrinations, un mage expérimenté rencontrera un spécimen inhabituel d'une espèce qui rejoindra le mage.

|          Composants           | Niv. |  Type  | Rang | B | D |
|:-----------------------------:|:----:|:------:|:----:|:-:|:-:|
| 100 auras, 5 auras permanents |  12  | Normal |  5   |   |   |

`CAST "Summon Familiar"`  

## Niveau 13

### Belebtes Gestein

<!-- cspell:disable -->
*(EN), Belebtes Gestein (DE)*.
<!-- cspell:enable -->

:   Ce rituel énergivore utilise une boule de laen concentré pour invoquer un énorme élémentaire de terre et le bannir dans un bâtiment.  
    L'élémentaire peut alors recevoir l'ordre de transporter le bâtiment et tous ses habitants vers une région voisine.  
    La force de l'élémentaire invoqué dépend de la compétence du mage : l'élémentaire peut faire au maximum (Niveau - 12) X Déplacer des bâtiments de taille 250.  
    Le bâtiment ne sortira pas indemne de cette procédure.

|                Composants                | Niv. |  Type  | Rang | B | D |
|:----------------------------------------:|:----:|:------:|:----:|:-:|:-:|
| 10 x N auras, 1 aura permanent, 5 [laen] |  13  | Normal |  5   |   |   |

`CAST [LEVEL n] "Belebtes Gestein" <building-id> <direction>`  

## Niveau 14

### Störe Astrale Integrität

<!-- cspell:disable -->
*(EN), Störe Astrale Integrität (DE)*.
<!-- cspell:enable -->

:   Ce sort provoque de graves perturbations dans l'Astral.  
    Dans un rayon Astral de régions de niveau 5, tous les êtres astraux qui ne peuvent pas résister au sort sont expulsés du plan Astral.  
    Le contact Astral avec toutes les régions affectées est perturbé pendant le niveau/3 semaines.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 140 auras  |  14  | Normal |  4   |   |   |

`CAST [LEVEL n] "Störe Astrale Integrität"`  

## Niveau 15

### Opfere Kraft

<!-- cspell:disable -->
*(EN), Opfere Kraft (DE)*.
<!-- cspell:enable -->

:   À l'aide de ce sort, le mage peut transférer définitivement une partie de son pouvoir magique à un autre mage.  
    Il peut transférer la moitié de la puissance utilisée à un mage de la même École de Magie, et un tiers à d'autres mages.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
| 100 auras  |  15  | Normal |  1   |   |   |

`CAST "Opfere Kraft" <unit-id> <Aura>`  

<!-- From [https://wiki.eressea.de/index.php?title=Tybiedzauber&oldid=7486] -->

[amulette de vision décuplée]: ./amulet-of-true-sight.md "Amulet of True Vision"
[anneau d'Invisibilité]: ./ring-of-invisibility.md "Ring of Invisibility"
[camouflage]: ./camouflage.md

[gousse]: ./herbs.md#gousse "Windbag"
[pétale de cristal de neige]: ./herbs.md#petale-de-cristal-de-neige "Snowcrystal petal"
[laen]: ./resources.md#laen "Laen"
[Cristal d'Antimagie]: ./antimagic-crystal.md "Antimagic Crystal"
