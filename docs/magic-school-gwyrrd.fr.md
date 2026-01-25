---
# cSpell:locale fr
alias: sorts-gwyrrd
---
# Sorts Gwyrrd

Les sorts de l'École de magie **Gwyrrd** sont décrits ci-dessous par ordre de niveau croissant.

## Sorts de niveau 1

### Créer des [[stone-golem]]

<!-- cspell:disable -->
*Create Stone Golems (EN), Erschaffe Steingolems (DE)*.
<!-- cspell:enable -->

:   "Humidifiez un bloc de fine roche cristalline sans interstice avec une fiole d’eau de vie jusqu’à ce qu’elle soit complètement absorbée par la roche.  
    Ensuite, vous dirigez votre force vers la fine aura de vie qui se forme et formez un logement pour la force non liée."  
    Plus le mage investit de puissance, plus de golems peuvent être créés avant que l'aura ne se dissipe.  
    Chaque golem a 10 pour cent de chances de se transformer en poussière à chaque tour.  
    Si vous donnez aux golems l'ordre `MAKE CASTLE` ou `MAKE STREET`, 4 pierres sont utilisées par golem et le golem se dissout.

| Composants                                       | Niv. |   Type | Rang | B | D |
|--------------------------------------------------|-----:|-------:|:----:|:--|:--|
| 2 x N auras, N [pierres][pierre], 1 [eau de vie] |    1 | Normal |  4   |   |   |

`CAST [LEVEL n] "Create Stone Golems"`  

### Bénédiction de la terre

<!-- cspell:disable -->
*Blessed Harvest (EN), Segen der Erde (DE)*.
<!-- cspell:enable -->

<!-- TODO: check description -->
:   Ce rituel de récolte améliore les rendements des agriculteurs qui travaillent dans la région pour un silver de plus.  
    Plus le druide investit de puissance, plus le sort dure longtemps.

| Composants | Niv. |   Type | Rang | B                  | D                  |
|------------|-----:|-------:|:----:|:-------------------|:-------------------|
| N auras    |    1 | Normal |  5   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Blessed Harvest"`  

### Guérison du bétail

<!-- cspell:disable -->
*Cattle Healing (EN), Viehheilung (DE)*.
<!-- cspell:enable -->

:   Les compétences d'élevage et de guérison des mages Gwyrrd sont très recherchées par les agriculteurs.  
    Leurs services sont souvent très demandés, notamment sur les marchés.  
    Certaines personnes peuvent également utiliser leur compétence pour vendre un animal à un meilleur prix.  
    Le mage peut gagner 50 silver par niveau.

| Composants | Niv. |   Type | Rang | B                  | D |
|------------|-----:|-------:|:----:|:-------------------|:--|
| N auras    |    1 | Normal |  5   | :heavy_check_mark: |   |

`CAST [LEVEL n] "Cattle Healing"`  

## Sorts de niveau 2

### Créer des [[golem-de-fer]]

<!-- cspell:disable -->
*Create Iron Golems (EN), Erschaffe Eisengolems (DE)*.
<!-- cspell:enable -->
<!-- TODO: fix MAKE orders -->
:   Plus le mage investit de puissance, plus de golems peuvent être créés.  
    Chaque golem a 15 % de chances de se transformer en poussière à chaque tour.  
    Si vous donnez aux golems l'ordre `MAKE Sword | Claymore` ou `MAKE Shield | CHAIN ​​​​MAIL | PLATE ARMOR`, 4 fer sont consommés par golem et le golem se dissout.

| Composants                            | Niv. |   Type | Rang | B | D |
|---------------------------------------|-----:|-------:|:----:|:--|:--|
| 2 x N auras, N [fers], 1 [eau de vie] |    2 | Normal |  4   |   |   |

`CAST [LEVEL n] "Create Iron Golems"`  

### Magie du bosquet de chêne

<!-- cspell:disable -->
*Grove of Oak Trees (EN), Hainzauber (DE)*.
<!-- cspell:enable -->

:   Alors qu'auparavant seul un arbre pouvait germer à partir d'un bâton, chaque branche produit désormais des racines.

| Composants                            | Niv. |   Type | Rang | B | D                  |
|---------------------------------------|-----:|-------:|:----:|:--|:-------------------|
| 4 x N auras, N [bois], 1 [eau de vie] |    2 | Normal |  5   |   | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Grove of Oak Trees"`  

## Sorts de niveau 3

### Gardien de la Montagne

<!-- cspell:disable -->
*Mountain Guardian (EN), Bergwächter (DE)*.
<!-- cspell:enable -->

:   Crée un esprit gardien qui empêche l'exploitation du fer et des métaux dans les glaciers et les montagnes par des factions non alliées (`HELP GUARD`) tant qu'il garde la région.  
    Le [Gardien de la Montagne] est lié au lieu de l'invocation.

| Composants  | Niv. |   Type | Rang | B | D                  |
|-------------|-----:|-------:|:----:|:--|:-------------------|
| 3 x N auras |    3 | Normal |  5   |   | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] Mountain Guardian`  

### Le manteau de Firun

<!-- cspell:disable -->
*Firun's Coat (EN), Firuns Fell (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au mage de protéger comme par magie les insectes du froid paralysant des glaciers.  
    Vous pouvez entrer dans les glaciers et y agir normalement. Le dicton fonctionne au niveau*10 insectes.  
    Un anneau de pouvoir augmente le nombre d'insectes enchantables de 10 supplémentaires.

| Composants  | Niv. |   Type | Rang | B                  | D |
|-------------|-----:|-------:|:----:|:-------------------|:--|
| 2 x N auras |    3 | Normal |  5   | :heavy_check_mark: |   |

`CAST [LEVEL n] "Firun's Coat" <unit-id> [<unit-id> ...]`  

### Grêle

<!-- cspell:disable -->
*Hail (EN), Hagel (DE)*.
<!-- cspell:enable -->

:   Au combat, le mage fait appel aux esprits élémentaires du froid et les lie à lui-même.  
    Il peut alors leur ordonner d'attaquer l'ennemi avec des grêlons et des morceaux de glace.

| Composants | Niv. |   Type | Rang | B | D |
|------------|-----:|-------:|:----:|:--|:--|
| N auras    |    3 | Combat |  5   |   |   |

`COMBATSPELL [LEVEL n] Hail`  

### Pluie de rouille

<!-- cspell:disable -->
*Rain of Rust (EN), Rostregen (DE)*.
<!-- cspell:enable -->

:   Ce rituel évoque un sombre front de tempête qui domine de façon menaçante la région.  
    La pluie magique fera rouiller tout le minerai.  
    Les armes et armures en fer deviennent ébréchées et rouillées.  
    Le pouvoir destructeur de la pluie dépend de la puissance investie par le mage.  
    Jusqu'à 10 armes de fer peuvent être affectées pour chaque niveau.  
    Un anneau de pouvoir augmente l'effet comme un niveau supplémentaire.

| Composants  | Niv. |   Type | Rang | B | D                  |
|-------------|-----:|-------:|:----:|:--|:-------------------|
| 2 x N auras |    3 | Normal |  5   |   | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Rain of Rust" <unit-id> [<unit-id> ...]`  

## Sorts de niveau 4

### Voie magique

<!-- cspell:disable -->
*Magic Path (EN), Magischer Pfad (DE)*.
<!-- cspell:enable -->

:   En accomplissant ces rituels, le mage est capable d'invoquer un puissant élémentaire de terre.  
    Tant que celle-ci sera bannie dans le sol, aucune pluie ne adoucira les sentiers et aucune rivière ne pourra détruire les ponts.  
    Cela signifie que tous les voyageurs bénéficient des mêmes avantages qui, autrement, ne seraient offerts que par un réseau routier asphalté développé.  
    Même les marécages et les glaciers peuvent être enchantés de cette façon. Plus le mage met de puissance dans le sort, plus le chemin dure longtemps.

| Composants                  | Niv. |   Type | Rang | B                  | D                  |
|-----------------------------|-----:|-------:|:----:|:-------------------|:-------------------|
| N auras, 1 [pierre], 1 bois |    4 | Normal |  5   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Magic Path"`  

### Bâton de Mallorn

<!-- TODO: check if it's really mallorn quarterstaff -->
<!-- cspell:disable -->
*Mallorn quarterstaff (EN), Segne Mallornstecken (DE)*.
<!-- cspell:enable -->

:   Ce rituel augmente plusieurs fois l'effet de la potion magique.  
    Alors qu’auparavant seul un arbre pouvait germer à partir d’un bâton, chaque branche produit désormais des racines.

| Composants                                | Niv. |   Type | Rang | B | D                  |
|-------------------------------------------|-----:|-------:|:----:|:--|:-------------------|
| 6 x N auras, N [mallorns], 1 [eau de vie] |    4 | Normal |  5   |   | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Mallorn Quarterstaff "`  

### Invocation de l'Eau

<!-- cspell:disable -->
*Summon Water Elemental (EN), Beschwörung eines Wasserelementares (DE)*.
<!-- cspell:enable -->

:   Avec ce rituel, le mage force les esprits élémentaires de l'eau à son service et les amène à transporter plus rapidement le bateau spécifié sur l'eau.  
    De plus, le bateau n’est pas affecté par des vents ou des courants défavorables.

| Composants | Niv. |   Type | Rang | B                  | D |
|------------|-----:|-------:|:----:|:-------------------|:--|
| N auras    |    4 | Normal |  5   | :heavy_check_mark: |   |

`CAST [LEVEL n] "Summon Water Elemental" <ship-id>`  

### Bouclier aérien

<!-- cspell:disable -->
*Air Shield (EN), Windschild (DE)*.
<!-- cspell:enable -->

:   Invoque les esprits élémentaires du vent.  
    Invoque des rafales de vent soudaines, de petites rafales de vent et des évents qui gêneront les archers adverses.

| Composants  | Niv. |   Type | Rang | B                  | D |
|-------------|-----:|-------:|:----:|:-------------------|:--|
| 2 x N auras |    4 | Pré-c. |  5   | :heavy_check_mark: |   |

`COMBATSPELL [LEVEL n] "Windschild"`  

## Sorts de niveau 5

### Esprits du Gardien de l'Astral

<!-- cspell:disable -->
*Astral Guardian Spirits (EN), Astralschutzgeister (DE)*.
<!-- cspell:enable -->

:   Ce rituel invoque des esprits élémentaires de magie et les envoie dans les rangs des mages ennemis.  
    Ces derniers auront bien plus de mal à lancer des sorts pendant toute la durée du combat.

| Composants  | Niv. |   Type | Rang | B | D |
|-------------|-----:|-------:|:----:|:--|:--|
| 5 x N auras |    5 | Pré-c. |  2   |   |   |

`COMBATSPELL [LEVEL n] "Astral Guardian Spirits"`  

### Créer un [[sac-a-herbes-magique]]

<!-- cspell:disable -->
*Create A magical Herb Pouch (EN), Erschaffe einen magischen Kräuterbeutel (DE)*.
<!-- cspell:enable -->

:   Le druide prend du cuir préparé, qu'il nettoie de tous les esprits impurs lors d'un grand rituel de purification, puis lie quelques petits esprits de l'air et de l'eau au matériau.  
    Il utilise désormais le cuir ainsi préparé pour fabriquer un petit sac qui permet de mieux conserver les herbes qui y sont stockées.

| Composants                                 | Niv. |   Type | Rang | B                  | D |
|--------------------------------------------|-----:|-------:|:----:|:-------------------|:--|
| 30 auras, 1 aura permanent, 1 [eau de vie] |    5 | Normal |  5   | :heavy_check_mark: |   |

`CAST "Create A magical Herb Pouch"`

### Guérison

<!-- cspell:disable -->
*Heal (EN), Heilung (DE)*.
<!-- cspell:enable -->

:   Il n'y a pas que le médecin qui peut aider les blessés au combat.  
    Les druides sont capables de refermer les blessures, de réparer les os brisés et de régénérer même les membres sectionnés en invoquant les esprits élémentaires de la vie.

| Composants | Niv. |    Type | Rang | B | D |
|------------|-----:|--------:|:----:|:--|:--|
| N auras    |    5 | Post-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] Heal`  

### Tourbillon

<!-- cspell:disable -->
*Whirlwind (EN), Wirbelwind (DE)*.
<!-- cspell:enable -->

:   Cette incantation ouvre une porte vers le plan des esprits élémentaires du vent.  
    Des vents violents, voire des tempêtes, se lèvent immédiatement dans la zone autour de la porte et gênent tous les archers dans la bataille.

| Composants | Niv. |   Type | Rang | B | D |
|------------|-----:|-------:|:----:|:--|:--|
| 15 auras   |    5 | Pré-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] Whirlwind`  

## Sort de niveau 6

### Créer une [[amulette-de-vision-decuplee]]

<!-- cspell:disable -->
*Create An Amulet of True Sight (EN), Erschaffe ein Amulett des wahren Sehens (DE)*.
<!-- cspell:enable -->

:   Le sort permet à un mage de créer une [amulette de vision décuplée].  
    L'amulette permet au porteur de voir toutes les unités protégées par un [anneau d'Invisibilité].  
    Cependant, les unités qui utilisent leur compétence de [camouflage] pour se cacher ne sont toujours pas détectées.

<!-- TODO: check if it's only Cerdorr or not -->
| Composants                               | Niv. |   Type | Rang | B                  | D |
|------------------------------------------|-----:|-------:|:----:|:-------------------|:--|
| 50 auras, 3 000 silver, 1 aura permanent |    6 | Normal |  5   | :heavy_check_mark: |   |

`CAST "Create An Amulet of True Sight"`  

### Créer un [anneau d'Invisibilité]

<!-- cspell:disable -->
*Create A Ring of Invisibility (EN), Erschaffe einen Ring der Unsichtbarkeit (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le sorcier peut créer un [anneau d'Invisibilité].  
    Le porteur de l'anneau devient invisible pour toutes les unités des autres partis, quelle que soit la qualité de leur perception.  
    Dans une unité invisible, chaque personne doit porter une bague.

| Composants                               | Niv. |   Type | Rang | B                  | D |
|------------------------------------------|-----:|-------:|:----:|:-------------------|:--|
| 50 auras, 3 000 silver, 1 aura permanent |    6 | Normal |  5   | :heavy_check_mark: |   |

`CAST "Create A Ring of Invisibility"`  

### Méditation

<!-- cspell:disable -->
*Meditate (EN), Meditation (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le mage peut transférer sa propre aura dans un rapport de 2:1 à un autre mage de la même École de Magie.

| Composants | Niv. |   Type | Rang | B                  | D |
|------------|-----:|-------:|:----:|:-------------------|:--|
| 2 auras    |    6 | Normal |  1   | :heavy_check_mark: |   |

`CAST Meditate <unit-id> <Aura>`  

### Invocation de la Tempête

<!-- cspell:disable -->
*Summon Storm Elemental (EN), Beschwöre einen Sturmelementar (DE)*.
<!-- cspell:enable -->

:   L'invocation des esprits élémentaires des tempêtes est un rituel ancien.  
    Le druide bannit les élémentaires dans les voiles des bateaux, où ils aident à transporter le bateau sur les vagues à grande vitesse.  
    Plus le druide investit de puissance dans le sort, plus le nombre d'esprits élémentaires pouvant être bannis est grand.  
    Un esprit élémentaire est requis pour chaque vaisseau.

| Composants  | Niv. |   Type | Rang | B                      | D |
|-------------|-----:|-------:|:----:|:-----------------------|:--|
| 6 x N auras |    6 | Normal |  5   | :heavy_check_mark:[^3] |   |

`CAST [LEVEL n] "Summon Storm Elemental" <ship-id> [<ship-id> ...]`  

## Sorts de niveau 7

### Invocation de la Terre

<!-- cspell:disable -->
*Summon Earth Elemental (EN), Beschwöre einen Erdelementar (DE)*.
<!-- cspell:enable -->

:   Avec ce rituel, le druide invoque un esprit élémentaire de la terre et le fait trembler la terre.  
    Ce tremblement de terre endommagera tous les bâtiments de la région.

| Composants         | Niv. |   Type | Rang | B | D                  |
|--------------------|-----:|-------:|:----:|:--|:-------------------|
| 25 auras, 2 [laen] |    7 | Normal |  5   |   | :heavy_check_mark: |

`CAST [REGION x y] "Summon Earth Elemental"`  

### Pierre de maison

<!-- cspell:disable -->
*Homestone (EN), Heimstein (DE)*.
<!-- cspell:enable -->

:   Avec cette formule, le mage lie à jamais les forces de la terre dans les murs du château dans lequel il se trouve actuellement.  
    Les murs ainsi renforcés ne peuvent être détruits ni par magie ni par l'artillerie lourde, et l'âge les affecte également moins.  
    Le bâtiment offre également une meilleure protection contre les attaques à l’épée et à la magie.

| Composants                 | Niv. |   Type | Rang | B | D |
|----------------------------|-----:|-------:|:----:|:--|:--|
| 50 auras, 1 aura permanent |    7 | Normal |  5   |   |   |

`CAST Homestone`  

### Hurlement des Loups

<!-- cspell:disable -->
*Timber Wolves (EN), Wolfsgeheul (DE)*.
<!-- cspell:enable -->

:   Au cours de leur vie dans la nature, de nombreux druides se lient d'amitié avec les plus anciens amis des grands peuples.  
    Ils apprennent à invoquer plusieurs de leurs amis pour les aider au combat avec un seul appel hurlant.

| Composants  | Niv. |   Type | Rang | B | D |
|-------------|-----:|-------:|:----:|:--|:--|
| 2 x N auras |    7 | Pré-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] "Timber Wolves"`  

## Sorts de niveau 8

### Regard du Basilic

<!-- cspell:disable -->
*Gaze of the Basilisk (EN), Blick des Basilisken (DE)*.
<!-- cspell:enable -->

:   Ce sort de combat difficile mais efficace utilise les esprits élémentaires de pierre pour transformer un certain nombre d'ennemis en pierre pendant toute la durée de la bataille.  
    Les personnes touchées ne combattront plus, mais elles ne pourront pas non plus être blessées.

| Composants | Niv. |   Type | Rang | B | D |
|------------|-----:|-------:|:----:|:--|:--|
| N auras    |    8 | Combat |  5   |   |   |

`COMBATSPELL [LEVEL n] "Gaze of the Basilisk"`  

### Bannissement des Esprits

<!-- cspell:disable -->
*Banish Spirits (EN), Geister bannen (DE)*.
<!-- cspell:enable -->

:   Selon les anciens enseignements des druides, ce que les êtres ordinaires appellent magie est constitué d'esprits élémentaires.  
    Le mage les évoque et les bannit sous une forme permettant d'obtenir l'effet souhaité. Ce rituel est capable de chasser les esprits élémentaires invoqués dans ce monde afin de libérer un objet de la magie.

| Composants  | Niv. |   Type | Rang | B                  | D                  |
|-------------|-----:|-------:|:----:|:-------------------|:-------------------|
| 6 x N auras |    8 | Normal |  2   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Banish Spirits" (REGION | UNIT <unit-id>; [<unit-id>]... | SHIP <ship-id> | CASTLE <building-id>)`  

### Portail puissant et Mur robuste

<!-- cspell:disable -->
*Strong Wall And Sturdy Gate (EN), Starkes Tor und feste Mauer (DE)*.
<!-- cspell:enable -->

:   Avec cette formule, au début d'un combat, le mage lie des esprits élémentaires du rocher dans les murs du bâtiment dans lequel il se trouve actuellement.  
    Le bâtiment offre alors une meilleure protection contre les attaques à l'épée et à la magie.

| Composants  | Niv. |   Type | Rang | B | D |
|-------------|-----:|-------:|:----:|:--|:--|
| 2 x N auras |    8 | Pré-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] "Strong Wall And Sturdy Gate"`  

## Sorts de niveau 9

### Terre Sacrée

<!-- cspell:disable -->
*Sacred Ground (EN), Heiliger Boden (DE)*.
<!-- cspell:enable -->

:   Ce rituel convoque divers esprits de la nature dans le sol de la région, qui le gardent désormais.  
    Dans une région aussi bénie, les morts ne quitteront plus jamais leurs tombes, et les morts-vivants apparus ailleurs les éviteront autant que possible.

| Composants                   | Niv. |   Type | Rang | B | D |
|------------------------------|-----:|-------:|:----:|:--|:--|
| 80 auras, 3 auras permanents |    9 | Normal |  5   |   |   |

`CAST "Sacred Ground"`  

### Liens de Vie

<!-- cspell:disable -->
*Ties of Life (EN), Sog des Lebens (DE)*.
<!-- cspell:enable -->

:   Un druide tombé dans le monde des esprits peut utiliser ce sort pour passer au niveau supérieur x Renvoyer 5 unités de poids dans une forêt du monde matériel.

| Composants  | Niv. |   Type | Rang | B | D |
|-------------|-----:|-------:|:----:|:--|:--|
| 2 x N auras |    9 | Normal |  7   |   |   |

`CAST [LEVEL n] "Ties of Life" <x> <y> <unit-id> [<unit-id> ...]`  

### Voie des Arbres

<!-- cspell:disable -->
*Path of Trees (EN), Weg der Bäume (DE)*.
<!-- cspell:enable -->

:   Un grand pouvoir réside dans les endroits où la vie palpite.  
    Le druide peut collecter ce pouvoir et créer une passerelle vers le monde des êtres spirituels.  
    Le druide peut alors niveau*Envoyer 5 unités de poids à travers la porte.

| Composants  | Niv. |   Type | Rang | B | D |
|-------------|-----:|-------:|:----:|:--|:--|
| 3 x N auras |    9 | Normal |  7   |   |   |

`CAST [LEVEL n] "Path of Trees" <unit-id> [<unit-id> ...]`  

## Sorts de niveau 10

### Éveil des [Ents]

<!-- cspell:disable -->
*Awakening of the Ents (EN), Erwecke Ents (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le druide réveille les Ents endormis dans les forêts de la région de leur sommeil éternel.  
    Les créatures sauvages des arbres le rejoindront et l’assisteront, mais après un certain temps, elles retomberont dans le sommeil.

| Composants  | Niv. |   Type | Rang | B | D |
|-------------|-----:|-------:|:----:|:--|:--|
| 6 x N auras |   10 | Normal |  5   |   |   |

`CAST [LEVEL n] "Awakening of the Ents"`  

### Invocation du Familier

<!-- cspell:disable -->
*Summon Familiar (EN), Vertrauten rufen (DE)*.
<!-- cspell:enable -->

:   À un moment donné de ses pérégrinations, un mage expérimenté rencontrera un spécimen inhabituel d'une espèce qui rejoindra le mage.

| Composants                    | Niv. |   Type | Rang | B | D |
|-------------------------------|-----:|-------:|:----:|:--|:--|
| 100 auras, 5 auras permanents |   10 | Normal |  5   |   |   |

`CAST "Summon Familiar"`  

## Sort de niveau 11

### Segne Steinkreis <!-- TODO -->

<!-- cspell:disable -->
*(EN), Segne Steinkreis (DE)*.
<!-- cspell:enable -->

:   Ce rituel bénit un cercle de pierres qui doit d'abord être construit à partir de pierres et d'un peu de bois.  
    La bénédiction du druide transforme le cercle en un puissant site d'activité magique, offrant une protection contre la magie et une régénération accrue de l'aura.  
    On dit que les vierges rencontraient d'étranges créatures autour des cercles de pierres.

| Composants                    | Niv. |   Type | Rang | B | D |
|-------------------------------|-----:|-------:|:----:|:--|:--|
| 350 auras, 5 auras permanents |   11 | Normal |  5   |   |   |

`CAST "Segne Steinkreis" <building-id>`  

## Sort de niveau 12

### Peau d'écorce

<!-- cspell:disable -->
*(EN), Rindenhaut (DE)*.
<!-- cspell:enable -->

:   Ce rituel, lancé avant la bataille, confère à vos troupes un bonus d'armure supplémentaire.  
    Chaque coup réduit la puissance du sort, le bouclier finira donc par se dissiper au cours du combat.

| Composants  | Niv. |   Type | Rang | B | D |
|-------------|-----:|-------:|:----:|:--|:--|
| 4 x N auras |   12 | Pré-c. |  2   |   |   |

`COMBATSPELL [LEVEL n] "Rindenhaut"`  

## Sort de niveau 13

### Hitzeelementar

<!-- cspell:disable -->
*(EN), Hitzeelementar (DE)*.
<!-- cspell:enable -->

:   Ce rituel invoque des élémentaires de chaleur en colère.  
    Une sécheresse ravage le pays. Les arbres se fanent, les animaux meurent et les récoltes échouent.  
    Il n’y a pratiquement pas de travail dans l’agriculture pour les journaliers.

| Composants | Niv. |   Type | Rang | B | D                  |
|------------|-----:|-------:|:----:|:--|:-------------------|
| 600 auras  |   13 | Normal |  5   |   | :heavy_check_mark: |

<!-- TODO: chec if it's `CAST [REGION x y] "Beschwörung eines Hitzeelementar"`  -->
`CAST [REGION x y] Hitzeelementar`  

## Sort de niveau 15

### Mahlstrom

<!-- cspell:disable -->
*(EN), Mahlstrom (DE)*.
<!-- cspell:enable -->

:   Ce rituel invoque un grand élémentaire d'eau des profondeurs de l'océan.  
    L'élémentaire crée un énorme tourbillon, un maelström, qui peut gravement endommager tous les bateaux qui le traversent.

| Composants                          | Niv. |   Type | Rang | B                      | D |
|-------------------------------------|-----:|-------:|:----:|:-----------------------|:--|
| 200 auras, 1 tête de serpent de mer |   15 | Normal |  5   | :heavy_check_mark:[^3] |   |

`CAST Mahlstrom`  

## Sort de niveau 16

### Wurzeln der Magie

<!-- cspell:disable -->
*(EN), Wurzeln der Magie (DE)*.
<!-- cspell:enable -->
<!-- TODO: check 1 pot de bave de crapaud -->
:   À l'aide de ce rituel élaboré, le druide permet à une partie de son pouvoir de circuler en permanence dans les sols et les forêts de la région.  
    Cela modifiera à jamais l’équilibre naturel de la région et, à l’avenir, seules les majornas exigeantes mais fortes prospéreront dans la région.

| Composants                                               | Niv. |   Type | Rang | B | D                  |
|----------------------------------------------------------|-----:|-------:|:----:|:--|:-------------------|
| 250 auras, 10 auras permanents, 1 pot de bave de crapaud |   16 | Normal |  5   |   | :heavy_check_mark: |

`CAST [REGION x y] "Wurzeln der Magie"`  

## Sort de niveau 17

### Tor in die Ebene der Hitze

<!-- cspell:disable -->
*(EN), Tor in die Ebene der Hitze (DE)*.
<!-- cspell:enable -->

:   Ce rituel puissant ouvre une porte vers le plan élémentaire de la chaleur.  
    Une grande sécheresse s'annonce dans le pays.  
    Les agriculteurs, les animaux et les plantes de la région luttent pour leur survie, mais seulement la moitié de tous les êtres vivants peuvent survivre à une telle sécheresse.  
    La région pourrait être affectée par les conséquences d’une telle sécheresse pendant des années.

| Composants | Niv. |   Type | Rang | B | D                  |
|------------|-----:|-------:|:----:|:--|:-------------------|
| 800 auras  |   17 | Normal |  5   |   | :heavy_check_mark: |

`CAST [REGION x y] "Tor in die Ebene der Hitze"`  

<!-- From [https://wiki.eressea.de/index.php?title=Gwyrrdzauber&oldid=7693] -->

[Ents]: ./monsters.md#ents "Ents"
[eau de vie]: ./alchemy.md#eau-de-vie "Water of life"
[bois]: ./resources.md#bois "Wood"
[fers]: ./resources.md#fer "Iron"
[pierre]: ./resources.md#pierre "Stone"
