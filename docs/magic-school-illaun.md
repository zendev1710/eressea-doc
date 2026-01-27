---
# cSpell:locale en
alias: illaun-spells
---
# Illaun spells

## Level 1

### Shadow Knights

:   This spell can give the enemy a slightly different image of their own troops.  
    The Shadow Knights have no effective attack and being wounded in battle will destroy them instantly.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|  T auras   |  1  | Pre-c. |  4   |      |       |

`COMBATSPELL [LEVEL n] "Shadow Knights"`  

### Dream

:   The magician sends the target of the spell a dream.

| Components | Lvl |  Type  | Rank |        Ship        | Dist. |
|:----------:|:---:|:------:|:----:|:------------------:|:-----:|
|  T auras   |  1  | Normal |  5   | :heavy_check_mark: |       |

`CAST [LEVEL n] Dream <unit-id>`  

### Divination

:   No one can interpret dreams as well as an Illaun magician.  
    He is also familiar with the art of fortune telling, card reading and palm reading.  
    In return, the farmers pay him 50 silver per level.

| Components | Lvl |  Type  | Rank |        Ship        | Dist. |
|:----------:|:---:|:------:|:----:|:------------------:|:-----:|
|  T auras   |  1  | Normal |  5   | :heavy_check_mark: |       |

`CAST [LEVEL n] Divination`  

## Level 2

### Unspeakable Horrors

:   Before battle, the dream weaver conjures up terrifying illusions that cause many opponents to panic.  
    Those affected will try to escape from the mirages.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|  T auras   |  2  | Pre-c. |  5   |      |       |

`COMBATSPELL [LEVEL n] "Unspeakable Horrors"`  

### Eternal Rest

:   This magical ritual soothes the tormented souls of those who died violently, allowing them to begin their final journey to the other lands.  
    Approximately 50 souls will find peace per level of the spell.  
    The spell cannot redeem the living dead who have already been resurrected because their ties to this world are too strong.

| Components  | Lvl |  Type  | Rank |        Ship        | Dist. |
|:-----------:|:---:|:------:|:----:|:------------------:|:-----:|
| 5 x T auras |  3  | Normal |  2   | :heavy_check_mark: |       |

`CAST [LEVEL n] "Eternal Rest"`  

## Level 3

### Shapeshift

:   With the help of this arcane ritual, the dream weaver is able to disguise the true form of a group.  
    To inexperienced observers, she then appears to belong to a different race.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|  T auras   |  3  | Normal |  5   |      |       |

`CAST [LEVEL n] Shapeshift <unit-id> <race>`  

### Dream of Magic

:   With the help of this spell, the dream weaver can transfer his own aura to another dream weaver at a ratio of 2:1.

| Components | Lvl |  Type  | Rank |        Ship        | Dist. |
|:----------:|:---:|:------:|:----:|:------------------:|:-----:|
|  2 auras   |  3  | Normal |  1   | :heavy_check_mark: |       |

`CAST "Dream of Magic" <unit-id> <Aura>`  

### Castle of Illusion

:   With the help of this spell, the dream weaver can create the illusion of any building.  
    The illusion can be entered, but is otherwise non-functional and requires no maintenance.
    It will last for a few weeks.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|  3 auras   |  3  | Normal |  5   |      |       |

`CAST "Castle of Illusion" <Gebäudetyp>`  

## Level 4

### Tiredness

:   This combat spell causes some enemies to suffer severe fatigue during combat.  
    The soldiers sometimes oversleep their attack and defend themselves poorly.

| Components  | Lvl |  Type  | Rank | Ship | Dist. |
|:-----------:|:---:|:------:|:----:|:----:|:-----:|
| 4 x T auras |  4  | Pre-c. |  5   |      |       |

`COMBATSPELL [LEVEL n] Tiredness`  

### Read Dreams

:   This spell allows the Dreamweaver to enter a unit"s dreams to obtain a report on the surrounding area.

| Components | Lvl |  Type  | Rank | Ship |       Dist.        |
|:----------:|:---:|:------:|:----:|:----:|:------------------:|
|  8 auras   |  4  | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] "Read Dreams" <unit-id>`  

## Level 5

### Analyse Dreams

:   With this spell, the dream weaver can attempt to detect the enchantments of a single unit.  
    He will be able to get an impression of their effectiveness from all spells that do not exceed his own abilities.  
    With stronger spells he needs a little luck for a successful analysis.

| Components | Lvl |  Type  | Rank |        Ship        | Dist. |
|:----------:|:---:|:------:|:----:|:------------------:|:-----:|
|  25 auras  |  5  | Normal |  5   | :heavy_check_mark: |       |

`CAST "Analyse Dreams" <unit-id>`  

### Resurrection

:   If a warrior dies in battle, his soul begins the long journey to the stars.  
    With the help of a ritual, a dream weaver can attempt to capture the soul and return it to the body of the deceased.  
    Although the spell does not heal physical injuries, the person treated will survive the fight.

| Components | Lvl |  Type   | Rank | Ship | Dist. |
|:----------:|:---:|:-------:|:----:|:----:|:-----:|
|  T auras   |  5  | Post-c. |  4   |      |       |

`COMBATSPELL [LEVEL n] Resurrection`  

## Level 6

### Create an [[amulet-of-true-sight]]

:   The spell allows a magician to create an [[amulet-of-true-sight]].  
    The amulet allows the wearer to see all units protected by a ring of invisibility.  
    However, units that use their [[camouflage]] skill to hide still remain undetected.

|                Components                | Lvl |  Type  | Rank |        Ship        | Dist. |
|:----------------------------------------:|:---:|:------:|:----:|:------------------:|:-----:|
| 50 auras, 3 000 silver, 1 permanent aura |  6  | Normal |  5   | :heavy_check_mark: |       |

`CAST "Create An Amulet of True Sight"`  

### Create a [[ring-of-invisibility]]

:   With this spell the wizard can create a ring of invisibility.  
    The bearer of the ring becomes invisible to all units of other parties, no matter how good their perception may be.  
    In an invisible unit, each person must wear a ring.

|                Components                | Lvl |  Type  | Rank |        Ship        | Dist. |
|:----------------------------------------:|:---:|:------:|:----:|:------------------:|:-----:|
| 50 auras, 3 000 silver, 1 permanent aura |  6  | Normal |  5   | :heavy_check_mark: |       |

`CAST "Create A Ring of Invisibility"`  

### Schlechter Schlaf

### Insomnia

:   This spell causes insomnia and restlessness in the affected area for a few weeks.  
    Those affected find it much more difficult to learn.

| Components | Lvl |  Type  | Rank | Ship |       Dist.        |
|:----------:|:---:|:------:|:----:|:----:|:------------------:|
|  18 auras  |  6  | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] Insomnia`  

## Level 7

### Sleep

:   This spell causes some enemy combatants to fall asleep.  
    Sleeping fighters do not attack and have poorer defenses, but they wake up as soon as they are hit in combat.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|  T auras   |  7  | Combat |  5   |      |       |

`COMBATSPELL [LEVEL n] Sleep`  

### Mind Probe

:   With this spell, the dream weaver penetrates the thoughts and dream world of his victim and can thus spy on his most intimate secrets.  
    His abilities, possessions and faction affiliation will no longer be uncertain.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|  20 auras  |  7  | Normal |  5   |      |       |

`CAST "Mind Probe" <unit-id>`  

## Level 8

### Schöne Träume  <!-- TODO -->

:   This spell allows the Dreamweaver to affect the sleep of all allied units in the region, giving them a bonus in all skills for a period of time.

| Components | Lvl |  Type  | Rank | Ship |       Dist.        |
|:----------:|:---:|:------:|:----:|:----:|:------------------:|
|  80 auras  |  8  | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] "Schöne Träume"`  

### Traumbilder entwirren

:   This spell allows the dream weaver to distinguish and unravel the natural and forced dream images of a person, building, ship, or region.

| Components  | Lvl |  Type  | Rank |        Ship        |       Dist.        |
|:-----------:|:---:|:------:|:----:|:------------------:|:------------------:|
| 6 x T auras |  8  | Normal |  2   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Traumbilder entwirren" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

## Level 9

### Summon Familiar

:   At some point in his wanderings, an experienced magician will encounter an unusual specimen of a species that will join the magician.

|          Components          | Lvl |  Type  | Rank | Ship | Dist. |
|:----------------------------:|:---:|:------:|:----:|:----:|:-----:|
| 100 auras, 5 permanent auras |  9  | Normal |  5   |      |       |

`CAST "Summon Familiar"`  

## Level 10

### Schlechte Träume  <!-- TODO -->

:   This spell allows the Dreamer to disrupt the sleep of all non-allied units (`HELP GUARD`) in the region to such an extent that they temporarily lose some of their memories.

| Components | Lvl |  Type  | Rank | Ship |       Dist.        |
|:----------:|:---:|:------:|:----:|:----:|:------------------:|
|  90 auras  | 10  | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] "Schlechte Träume"`  

## Level 11

### Tod des Geistes <!-- TODO -->

:   With this spell the magician attacks the minds of his opponents directly.  
    A blast of Astral and electrical energy hits the opponents;  
    if magic resistance is broken, a victim permanently loses part of their memories.  
    If it falls victim to this spell too often, it can die.

| Components  | Lvl |  Type  | Rank | Ship | Dist. |
|:-----------:|:---:|:------:|:----:|:----:|:-----:|
| 2 x T auras | 11  | Pre-c. |  5   |      |       |

`COMBATSPELL [LEVEL n] "Tod des Geistes"`  

## Level 12

### Süße Träume <!-- TODO -->

:   This spell -the use of which is strictly forbidden in most cultures -triggers an uncontrollable desire for physical love in the victim.  
    The affected individuals will rush headlong into a love affair, too blinded by desire to think of anything else.  
    Most of the time they regret it a few weeks later...

| Components  | Lvl |  Type  | Rank | Ship | Dist. |
|:-----------:|:---:|:------:|:----:|:----:|:-----:|
| 5 x T auras | 12  | Normal |  5   |      |       |

`CAST [LEVEL n] "Süße Träume" <unit-id> [<unit-id> ...]`  

## Level 13

### Create a [[sphere-of-invisibility]]

:   With this spell the magician can create a sphere of invisibility.  
    The sphere renders its wielder and ninety-nine other people in the same unit invisible.

|                 Components                  | Lvl |  Type  | Rank |        Ship        | Dist. |
|:-------------------------------------------:|:---:|:------:|:----:|:------------------:|:-----:|
| 150 auras, 30 000 silver, 3 permanent auras | 13  | Normal |  5   | :heavy_check_mark: |       |

`CAST "Create A Sphere of Invisibility"`  

## Level 14

### Create a [[flaming-sword]]

:   "And so rub the blood of a fierce fighter into the steel of the blade and begin the invocation of the Spheres of Chaos.  
    And if you have done everything to please them, they will send one of their own to imbue the sword with his power..."

|                          Components                          | Lvl |  Type  | Rank |        Ship        | Dist. |
|:------------------------------------------------------------:|:---:|:------:|:----:|:------------------:|:-----:|
| 100 auras, 1 [berserkers blood], 1 [sword], 1 permanent aura | 12  | Normal |  5   | :heavy_check_mark: |       |

`CAST "Create A Flaming Sword"`  

<!-- From [https://wiki.eressea.de/index.php?title=Illaunzauber&oldid=7014] -->
