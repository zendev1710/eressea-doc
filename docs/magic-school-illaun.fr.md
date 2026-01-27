---
# cSpell:locale fr
alias: sorts-illaun
---
# Sorts Illaun

Les sorts de l'École de magie **Illaun** sont décrits ci-dessous par ordre de niveau croissant.

## Niveau 1

### Chevaliers de l'Ombre

<!-- TODO: checkif it is Schattenritter or Schattenritteren for German CAST -->
<!-- cspell:disable -->
*Shadow Knights (EN), Schattenritteren (DE)*.
<!-- cspell:enable -->

:   Ce sort peut donner à l'ennemi une image légèrement différente de ses propres troupes.  
    Les Chevaliers de l'Ombre n'ont aucune attaque efficace et être blessés au combat les détruira instantanément.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|  N auras   |  1   | Pré-c. |  4   |   |   |

`COMBATSPELL [LEVEL n] "Shadow Knights"`  

### Rêve

<!-- cspell:disable -->
*Dream (EN), Traum (DE)*.
<!-- cspell:enable -->

:   Le mage envoie un rêve à la cible du sort.

| Composants | Niv. |  Type  | Rang |         B          | D |
|:----------:|:----:|:------:|:----:|:------------------:|:-:|
|  N auras   |  1   | Normal |  5   | :heavy_check_mark: |   |

`CAST [LEVEL n] Dream <unit-id>`  

### Divination

<!-- TODO: check if it is Wahrsagen or Weissagung in CAST german order -->
<!-- cspell:disable -->
*Divination (EN), Weissagung (DE)*.
<!-- cspell:enable -->

:   Nul ne sait interpréter les rêves aussi bien qu'un mage Illaun.  
    Il maîtrise également l'art de la divination, de la cartomancie et de la chiromancie.  
    Pour cela, les paysans lui versent 50 silver par niveau.

| Composants | Niv. |  Type  | Rang |         B          | D |
|:----------:|:----:|:------:|:----:|:------------------:|:-:|
|  N auras   |  1   | Normal |  5   | :heavy_check_mark: |   |

`CAST [LEVEL n] Divination`  

## Niveau 2

### Horreurs indicibles

<!-- cspell:disable -->
*Unspeakable Horrors (EN), Grauen der Schlacht (DE)*.
<!-- cspell:enable -->

:   Avant le combat, le tisserand de rêves évoque des illusions terrifiantes qui font paniquer de nombreux adversaires.  
    Les personnes touchées tenteront d’échapper aux mirages.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|  N auras   |  2   | Pré-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] "Unspeakable Horrors"`  

### Repos éternel

<!-- cspell:disable -->
*Eternal Rest (EN), Seelenfrieden (DE)*.
<!-- cspell:enable -->

:   Ce rituel magique apaise les âmes tourmentées de ceux qui sont morts violemment, leur permettant d'entamer leur dernier voyage vers les Autres Terres.  
    Environ 50 âmes trouveront la paix par niveau de sort.  
    Le sort ne peut pas racheter les morts-vivants déjà ressuscités car leurs liens avec ce monde sont trop forts.

|         Composants          | Niv. |  Type  | Rang | B | D |
|:---------------------------:|:----:|:------:|:----:|:-:|:-:|
| 3 x N auras, 1 [eau de vie] |  2   | Normal |  5   |   |   |

`CAST [LEVEL n] "Eternal Rest"`  

## Niveau 3

### Changement de forme

<!-- cspell:disable -->
*Shapeshift (EN), Gestaltwandlung (DE)*.
<!-- cspell:enable -->

:   Avec l’aide de ce rituel mystérieux, le tisserand de rêves est capable de dissimuler la véritable forme d’un groupe.  
    Pour les observateurs inexpérimentés, elle semble alors appartenir à une race différente.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|  N auras   |  3   | Normal |  5   |   |   |

`CAST [LEVEL n] Shapeshift <unit-id> <race>`  

### Rêve de magie

<!-- cspell:disable -->
*Dream of Magic (EN), Traum der Magie (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le tisserand de rêves peut transférer sa propre aura à un autre tisserand de rêves dans un rapport de 2:1.

| Composants | Niv. |  Type  | Rang |         B          | D |
|:----------:|:----:|:------:|:----:|:------------------:|:-:|
|  2 auras   |  3   | Normal |  1   | :heavy_check_mark: |   |

`CAST "Dream of Magic" <unit-id> <Aura>`  

### Château d'Illusion

<!-- cspell:disable -->
*Castle of Illusion (EN), Traumschlößchen (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le tisserand de rêves peut créer l'illusion de n'importe quel bâtiment.  
    L'illusion peut être saisie, mais elle est par ailleurs non fonctionnelle et ne nécessite aucun entretien.
    Cela durera quelques semaines.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|  3 auras   |  3   | Normal |  5   |   |   |

`CAST "Castle of Illusion" <building-type>`  

## Niveau 4

### Affaiblissement

<!-- cspell:disable -->
*Tiredness (EN), Schwere Glieder (DE)*.
<!-- cspell:enable -->

:   Ce sort de combat provoque une fatigue intense chez certains ennemis pendant le combat.  
    Les soldats tardent parfois à attaquer et se défendent mal.

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 4 x N auras |  4   | Pré-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] Tiredness`  

### Lecture des rêves

<!-- cspell:disable -->
*Read Dreams (EN), Traumlesen (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au Dreamweaver d'entrer dans les rêves d'une unité pour obtenir un rapport sur les environs.  

| Composants | Niv. |  Type  | Rang | B |         D          |
|:----------:|:----:|:------:|:----:|:-:|:------------------:|
|  8 auras   |  4   | Normal |  5   |   | :heavy_check_mark: |

`CAST [REGION x y] "Read Dreams" <unit-id>`  

## Niveau 5

### Analyse des rêves

<!-- cspell:disable -->
*Analyse Dreams (EN), Traumbilder analysieren (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le tisserand de rêves peut tenter de détecter les enchantements d'une seule unité.  
    Il pourra se faire une idée de leur efficacité grâce à tous les sorts qui ne dépassent pas ses propres capacités.  
    Avec des sorts plus puissants, il lui faut un peu de chance pour réussir son analyse.

| Composants | Niv. |  Type  | Rang |         B          | D |
|:----------:|:----:|:------:|:----:|:------------------:|:-:|
|  25 auras  |  5   | Normal |  5   | :heavy_check_mark: |   |

`CAST "Analyse Dreams" <unit-id>`  

### Résurrection

<!-- cspell:disable -->
*Resurrection (EN), Wiederbelebung (DE)*.
<!-- cspell:enable -->

:   Si un guerrier meurt au combat, son âme commence le long voyage vers les étoiles.  
    À l'aide d'un rituel, un tisserand de rêves peut tenter de capturer l'âme et de la restituer dans le corps du défunt.  
    Bien que le sort ne soigne pas les blessures physiques, la personne soignée survivra au combat.

| Composants | Niv. |  Type   | Rang | B | D |
|:----------:|:----:|:-------:|:----:|:-:|:-:|
|  N auras   |  5   | Post-c. |  4   |   |   |

`COMBATSPELL [LEVEL n] Resurrection`  

## Niveau 6

### Créer une [[amulette-de-vision-decuplee]]

<!-- cspell:disable -->
*Create An Amulet of True Sight (EN), Erschaffe ein Amulett des wahren Sehens (DE)*.
<!-- cspell:enable -->

:   Le sort permet à un mage de créer une [amulette de vision décuplée].  
    L'amulette permet au porteur de voir toutes les unités protégées par un [anneau d'Invisibilité].  
    Cependant, les unités qui utilisent leur compétence de [camouflage] pour se cacher ne sont toujours pas détectées.

<!-- TODO: check if it's only Cerdorr or not -->
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

### Insomnie

<!-- cspell:disable -->
*Insomnia (EN), Schlechter Schlaf (DE)*.
<!-- cspell:enable -->

:   Ce sort provoque de l'insomnie et de l'agitation dans la zone touchée pendant quelques semaines.  
    Les personnes concernées ont beaucoup plus de mal à apprendre.

| Composants | Niv. |  Type  | Rang | B |         D          |
|:----------:|:----:|:------:|:----:|:-:|:------------------:|
|  18 auras  |  6   | Normal |  5   |   | :heavy_check_mark: |

`CAST [REGION x y] Insomnia`  

## Niveau 7

### Endormissement

<!-- cspell:disable -->
*Sleep (EN), Schlaf (DE)*.
<!-- cspell:enable -->

:   Ce sort endort certains combattants ennemis.  
    Les combattants endormis n'attaquent pas et ont des défenses plus faibles, mais ils se réveillent dès qu'ils sont touchés au combat.  

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|  N auras   |  7   | Combat |  5   |   |   |

`COMBATSPELL [LEVEL n] Sleep`  

### Intrusion mentale

<!-- cspell:disable -->
*Mind Probe (EN), Traumdeuten (DE)*.
<!-- cspell:enable -->

:   Grâce à ce sort, le tisserand de rêves pénètre dans les pensées et le monde onirique de sa victime et peut ainsi espionner ses secrets les plus intimes.  
    Ses capacités, ses possessions et son affiliation à un parti ne seront plus incertaines.

| Composants | Niv. |  Type  | Rang | B | D |
|:----------:|:----:|:------:|:----:|:-:|:-:|
|  20 auras  |  7   | Normal |  5   |   |   |

`CAST "Mind Probe" <unit-id>`  

## Niveau 8

### Schöne Träume

<!-- cspell:disable -->
*(EN), Schöne Träume (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au Dreamweaver d'affecter le sommeil de toutes les unités alliées de la région, leur donnant un bonus dans toutes les compétences pendant un certain temps.

| Composants | Niv. |  Type  | Rang | B |         D          |
|:----------:|:----:|:------:|:----:|:-:|:------------------:|
|  80 auras  |  8   | Normal |  5   |   | :heavy_check_mark: |

`CAST [REGION x y] "Schöne Träume"`  

### Traumbilder entwirren

<!-- cspell:disable -->
*(EN), Traumbilder entwirren (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au tisserand de rêves de distinguer et de démêler les images oniriques naturelles et forcées d'une personne, d'un bâtiment, d'un bateau ou d'une région.

| Composants  | Niv. |  Type  | Rang |         B          |         D          |
|:-----------:|:----:|:------:|:----:|:------------------:|:------------------:|
| 6 x N auras |  8   | Normal |  2   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Traumbilder entwirren" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

## Niveau 9

### Invocation du Familier

<!-- cspell:disable -->
*Summon Familiar (EN), Vertrauten rufen (DE)*.
<!-- cspell:enable -->

:   À un moment donné de ses pérégrinations, un mage expérimenté rencontrera un spécimen inhabituel d'une espèce qui rejoindra le mage.

|          Composants           | Niv. |  Type  | Rang | B | D |
|:-----------------------------:|:----:|:------:|:----:|:-:|:-:|
| 100 auras, 5 auras permanents |  9   | Normal |  5   |   |   |

`CAST "Summon Familiar"`  

## Niveau 10

### Schlechte Träume

<!-- cspell:disable -->
*(EN), Schlechte Träume (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au Rêveur de perturber le sommeil de toutes les unités non alliées (`HELP GUARD`) de la région à tel point qu'elles perdent temporairement une partie de leurs souvenirs.

| Composants | Niv. |  Type  | Rang | B |         D          |
|:----------:|:----:|:------:|:----:|:-:|:------------------:|
|  90 auras  |  10  | Normal |  5   |   | :heavy_check_mark: |

`CAST [REGION x y] "Schlechte Träume"`  

## Niveau 11

### Tod des Geistes

<!-- cspell:disable -->
*(EN), Tod des Geistes (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le mage attaque directement l'esprit de ses adversaires.  
    Une explosion d'énergie astrale et électrique frappe les adversaires;  
    si la résistance magique est brisée, la victime perd définitivement une partie de ses souvenirs.  
    S'il est trop souvent victime de ce sort, il peut mourir.

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 2 x N auras |  11  | Pré-c. |  5   |   |   |

`COMBATSPELL [LEVEL n] "Tod des Geistes"`  

## Niveau 12

### Süße Träume

<!-- cspell:disable -->
*(EN), Süße Träume (DE)*.
<!-- cspell:enable -->

:   Ce sortilège dont l'usage est strictement interdit dans la plupart des cultures déclenche chez la victime un désir incontrôlable d'amour physique.  
    Les individus concernés se précipiteront à corps perdu dans une histoire d'amour, trop aveuglés par le désir de penser à autre chose.  
    La plupart du temps, ils le regrettent quelques semaines plus tard...

| Composants  | Niv. |  Type  | Rang | B | D |
|:-----------:|:----:|:------:|:----:|:-:|:-:|
| 5 x N auras |  12  | Normal |  5   |   |   |

`CAST [LEVEL n] "Süße Träume" <unit-id> [<unit-id> ...]`  

## Niveau 13

### Créer une [Sphère d'Invisibilité]

<!-- cspell:disable -->
*Create A Sphere of Invisibility (EN), Erschaffe eine Sphäre der Unsichtbarkeit (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le mage peut créer une [Sphère d'Invisibilité].  
    Celle-ci rend invisibles son porteur et quatre-vingt-dix-neuf autres personnes de la même unité.

|                  Composants                  | Niv. |  Type  | Rang |         B          | D |
|:--------------------------------------------:|:----:|:------:|:----:|:------------------:|:-:|
| 150 auras, 30 000 silver, 3 auras permanents |  13  | Normal |  5   | :heavy_check_mark: |   |

`CAST "Create A Sphere of Invisibility"`  

## Niveau 14

### Créer un [[dreameye]]

<!-- cspell:disable -->
*Create A DreamEye (EN), Erschaffe ein Traumauge (DE)*.
<!-- cspell:enable -->

:   Un œil de dragon lancé avec ce sort est consommé lors de la communion, ce qui permet à l'utilisateur d'entrer et de lire les rêves d'une autre personne.  
    Pendant longtemps, une telle capacité a été considérée comme inutile jusqu'à ce que l'ancien maître de la magie de combat des Elfes des bois, Liarana Sundew de l'Académie Thall, présente une application spéciale :  
    les généraux rêvent souvent sans relâche avant les batailles majeures et révèlent leurs plans dans leurs rêves.  
    Cela peut donner à l'utilisateur un énorme avantage dans la bataille à venir.  
    Mais attention : interpréter les rêves est une affaire difficile.

|                Composants                | Niv. |  Type  | Rang |         B          | D |
|:----------------------------------------:|:----:|:------:|:----:|:------------------:|:-:|
| 1 [[tete-de-dragon]], 5 auras permanents |  14  | Normal |  5   | :heavy_check_mark: |   |

`CAST "Create A DreamEye"`  

<!-- From [https://wiki.eressea.de/index.php?title=Illaunzauber&oldid=7014] -->

[eau de vie]: ./alchemy.md#eau-de-vie "Water of life"
