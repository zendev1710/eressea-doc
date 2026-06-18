---
# cSpell:locale en
alias: draig-spells
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD042 MD052 -->
# Draig spells

*Note : in the documentation below, T represents the magic skill level.*

## Level 1

### Minor Curses

:   In the darker alleys they exist, the curses and hexes made to order.  
    But of course the disciple of Draig also offers counter spells.  
    Whether the neighbor"s son is to be drawn into a love spell or the rival is to get pimples and warts, no one likes to admit that they have resorted to such measures.  
    For this service, the magician earns 50 silver per level.

| Components | Lvl |  Type  | Rank |             Ship             | Dist. |
|:----------:|:---:|:------:|:----:|:----------------------------:|:-----:|
|   T aura   |  1  | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Minor Curses"`  

### Hex

:   The magician"s target is afflicted by a harmless curse.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|   T aura   |  1  | Normal |  5   |      |       |

`CAST [LEVEL n] Hex <unit-id>`  

### Fireball

:   The sorcerer hurls focused chaos into the enemy"s ranks.  
    The ball-shaped chaos will wound anyone it hits.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|   T aura   |  2  | Combat |  5   |      |       |

`COMBATSPELL [LEVEL n] Fireball`  

### Chaos Gift

:   The magician opens his mind to the spheres of chaos and will thus have more magical power for some time.  
    But the help of the Lords of the Spheres comes at a price, and so the phase of power is replaced by a phase of weakness.

| Components | Lvl |  Type  | Rank |             Ship             | Dist. |
|:----------:|:---:|:------:|:----:|:----------------------------:|:-----:|
|   6 aura   |  3  | Normal |  3   | :material-check:{ .success } |       |

`CAST "Chaos Gift"`  

### Lesser Sacrifice

:   With this ritual the magician can sacrifice part of his life energy in order to gain magical power.  
    Experienced ritual magicians report that the ritual, once initiated, is difficult to control and the amount of power gained varies greatly.  
    So it is written in the "Book of Blood": "So let He establish the sign of the four elements in the circle of creation and decay and consecrate each one with a drop of blood.  
    Then let He go into the midst of the Eternal Four and let life pass away so that strength can be born."

| Components | Lvl |  Type  | Rank |             Ship             | Dist. |
|:----------:|:---:|:------:|:----:|:----------------------------:|:-----:|
|   16 PV    |  4  | Normal |  1   | :material-check:{ .success } |       |

`CAST "Lesser Sacrifice"`  

### Blood Frenzy

:   In this bloody ritual, the magician sacrifices a newborn baby in front of his army before battle.  
    The blood spirits summoned in this way will take possession of the soldiers and send them into a bloodlust.

|      Components      | Lvl |  Type  | Rank | Ship | Dist. |
|:--------------------:|:---:|:------:|:----:|:----:|:-----:|
| 5 x T aura, 1 paysan |  5  | Pre-c. |  4   |      |       |

`COMBATSPELL [LEVEL n] "Blood Frenzy"`  

[](){ #d-chaos-curse-id }

### Chaos Curse

:   This insidious curse significantly impairs the victim"s magical abilities.  
    A chaos magic zone around the victim reduces his ability to concentrate and makes it very difficult for him to cast spells.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 4 x T aura |  5  | Normal |  4   |      |       |

`CAST [LEVEL n] "Chaos Curse" <unit-id>`  

### Create an [Amulet of True Sight][amulet-of-true-sight-id]

:   The spell allows a magician to create an [Amulet of True Sight][amulet-of-true-sight-id].  
    The amulet allows the wearer to see all units protected by a [Ring of Invisibility][ring-of-invisibility-id].  
    However, units that use their [stealth][skill-stealth-id] skill to hide still remain undetected.

|               Components                | Lvl |  Type  | Rank |             Ship             | Dist. |
|:---------------------------------------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 50 aura, 3 000 silver, 1 permanent aura |  6  | Normal |  5   | :material-check:{ .success } |       |

### Create a [Ring of Invisibility][ring-of-invisibility-id]

:   With this spell the wizard can create a [Ring of Invisibility][ring-of-invisibility-id].  
    The bearer of the ring becomes invisible to all units of other parties, no matter how good their perception may be.  
    In an invisible unit, each person must wear a ring.

|               Components                | Lvl |  Type  | Rank |             Ship             | Dist. |
|:---------------------------------------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 50 aura, 3 000 silver, 1 permanent aura |  6  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Ring of Invisibility"`  

### Animate Dead

:   The black magician has to spend nights wandering through the cemeteries and burial grounds of the region in order to be able to revive the unearthed corpses.  
    The undead will be at his service, but the uninformed be warned that summoning the forces of death can be a double-edged sword.

| Components | Lvl |  Type  | Rank |             Ship             |            Dist.             |
|:----------:|:---:|:------:|:----:|:----------------------------:|:----------------------------:|
| 5 x T aura |  6  | Normal |  5   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Animate Dead"`  

### Winds of Rust

:   This ritual conjures up a dark storm front that towers ominously over the region.  
    The magical rain will cause all ore to rust, destroying many of the enemy's weapons.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 2 x T aura |  6  | Combat |  5   |      |       |

`COMBATSPELL [LEVEL n] "Winds of Rust"`  

### Firewall

:   The wizard creates a wall of fire in the specified direction.
    It hurts everyone who walks through it.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 6 x T aura |  7  | Normal |  4   |      |       |

`CAST [LEVEL n] Firewall <direction>`  

### Curse of Pestilence

:   In an elaborate ritual, the black magician sacrifices some peasants and then magically distributes the corpses into the region"s wells.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 4 x T aura |  5  | Normal |  4   |      |       |

`CAST [REGION x y] "Curse of Pestilence"`  

### Transfer Power

With the help of this spell, the magician can transfer his own aura at a ratio of 2:1 to another magician of the same magic area.

| Components | Lvl |  Type  | Rank |             Ship             | Dist. |
|:----------:|:---:|:------:|:----:|:----------------------------:|:-----:|
|   2 aura   |  7  | Normal |  1   | :material-check:{ .success } |       |

`CAST "Transfer Power" <unit-id> <Aura>`  

### Summon Shadowdemons

:   Using dark rituals, the magician summons demons from the sphere of shadows.  
    These feared creatures can move almost invisibly among the living, but their dark aura can be felt by everyone.  
    Shadow demons are feared opponents in battle.  
    They are difficult to hit and drain their opponent"s power.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 3 x T aura |  8  | Normal |  5   |      |       |

### Madness of War

:   In front of the enemy soldiers, the black magician sacrifices the ten pawns in a bloody, cruel ritual and in this way summons spirits of madness over the enemy troops.  
    They will react confusedly in battle and be unable to follow the orders of their officers.

|      Components       | Lvl |  Type  | Rank | Ship | Dist. |
|:---------------------:|:---:|:------:|:----:|:----:|:-----:|
| 3 x T aura, 10 Bauern |  8  | Pre-c. |  5   |      |       |

`COMBATSPELL [LEVEL n] "Madness of War"`  

### Astral Leak

:   With this dark ritual, the black magician can cause a rift in the fabric of magic, which will tear all magical power from the region.  
    All magically gifted people in the region will lose much of their aura.

|              Components               | Lvl |  Type  | Rank | Ship | Dist. |
|:-------------------------------------:|:---:|:------:|:----:|:----:|:-----:|
| 35 aura, 1 [dragonblood][dragonblood] |  9  | Normal |  3   |      |       |

`CAST "Astral Leak"`  

### Astral Chaos

:   This ritual, performed before battle, swirls the Astral energies on the battlefield, making it more difficult for enemy magicians to cast their spells.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 6 x T aura |  9  | Pre-c. |  2   |      |       |

`COMBATSPELL [LEVEL n] "Astral Chaos"`  

### Create a [[belt-of-troll-strength]]

:   This magical artifact grants the wearer the strength of a full-grown cave troll.  
    Its carrying capacity increases 50 times and the increased strength and troll-tough skin will also have a positive effect in combat.

|        Components         | Lvl |  Type  | Rank |             Ship             | Dist. |
|:-------------------------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 20 aura, 1 permanent aura |  9  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Belt of Troll Strength"`  

### Undead Heroes

:   This ritual binds the already escaping souls of some battle victims to their dead bodies, resurrecting them to undead life.  
    Whether they previously fought on the enemy"s side or their own is irrelevant to the ritual.

| Components | Lvl |  Type   | Rank | Ship | Dist. |
|:----------:|:---:|:-------:|:----:|:----:|:-----:|
|   T aura   |  9  | Post-c. |  5   |      |       |

`COMBATSPELL [LEVEL n] "Undead Heroes"`  

### Fire Fiend

:   This elemental summoning calls a fire fiend, a creature from the deepest hell.  
    The demon will eagerly rush into the forests of a region and set them ablaze.

|     Components     | Lvl |  Type  | Rank | Ship |            Dist.             |
|:------------------:|:---:|:------:|:----:|:----:|:----------------------------:|
| 50 aura, 1 [huile] | 10  | Normal |  5   |      | :material-check:{ .success } |

`CAST [REGION x y] "Fire Fiend"`  

### Pentagram

:   Exactly at midnight, when the powers of darkness are at their greatest, a black magician can also use his powers to remove enchantments.  
    To do this, he draws a pentagram on the enchanted object and begins with an invocation to the lords of darkness.  
    The gentlemen will help him, but whether he succeeds in solving the spell depends solely on his own strength.

| Components  | Lvl |  Type  | Rank |             Ship             |            Dist.             |
|:-----------:|:---:|:------:|:----:|:----------------------------:|:----------------------------:|
| 10 x T aura | 10  | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Pentagram" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

[](){ #d-dragon-call-id }

### Dragon Call

:   With this dark ritual, the magician creates a lure that smells irresistible to [dragons][known-dragons].  
    It has not yet been possible to research whether the dragons come from the surrounding area or from the sphere of chaos.  
    Both are said to have already happened.  
    The bait lasts about 6 weeks, but must be placed in kite-friendly terrain.

|             Components              | Lvl |  Type  | Rank | Ship |            Dist.             |
|:-----------------------------------:|:---:|:------:|:----:|:----:|:----------------------------:|
| 80 aura, 1 [dragonhead][dragonhead] | 11  | Normal |  5   |      | :material-check:{ .success } |

`CAST [REGION x y] *Dragon Call`  

### Death Cloud

:   By performing a gruesome ritual and sacrificing his own blood the Sorcerer conjurs up a spirit from the Elemental Plane of Poison.  
    It will take the form of a green cloud of toxic gases that envelops a whole region and that will harm anyone within.

|   Components   | Lvl |  Type  | Rank | Ship |            Dist.             |
|:--------------:|:---:|:------:|:----:|:----:|:----------------------------:|
| 40 aura, 15 PV | 11  | Normal |  5   |      | :material-check:{ .success } |

`CAST [REGION x y] "Death Cloud"`  

### Summon Shadowmasters

:   Using dark rituals, the magician summons demons from the sphere of shadows.  
    These feared creatures can move almost invisibly among the living, but their dark aura can be felt by everyone.  
    In battle, shadow masters are feared opponents.  
    They are difficult to hit and drain their opponent"s strength and life.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 7 x T aura | 12  | Normal |  5   |      |       |

`CAST [LEVEL n] "Summon Shadowmasters"`  

### Create a [[flaming-sword]]

:   "And so rub the blood of a fierce fighter into the steel of the blade and begin the invocation of the Spheres of Chaos.  
    And if you have done everything to please them, they will send one of their own to imbue the sword with his power..."

|                         Components                          | Lvl |  Type  | Rank |             Ship             | Dist. |
|:-----------------------------------------------------------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 100 aura, 1 [berserkers blood], 1 [sword], 1 permanent aura | 12  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Flaming Sword"`  

### Summon Familiar

:   At some point in his wanderings, an experienced magician will encounter an unusual specimen of a species that will join the magician.

|         Components         | Lvl |  Type  | Rank | Ship | Dist. |
|:--------------------------:|:---:|:------:|:----:|:----:|:-----:|
| 100 aura, 5 permanent aura | 13  | Normal |  5   |      |       |

`CAST "Summon Familiar"`  

### Chaos Gate

:   By sacrificing the lives of 200 peasants, the chaossorcerer is able to open a planar gate.  
    This gate can be used during the following week to transfer units to the astral plane.  
    It dissipates at the end of the following week.

|      Components       | Lvl |  Type  | Rank | Ship | Dist. |
|:---------------------:|:---:|:------:|:----:|:----:|:-----:|
| 150 aura, 200 paysans | 14  | Normal |  5   |      |       |

`CAST "Chaos Gate"`  

### Unholy Strength

:   Only whispered the knowledge of performing this ritual is passed to the adepts of the dark academies, for it is one of the darkest that has ever been written down.  
    By calling unholy demons the strength of the living dead is greatly increased and they are turned into undead monsters of immense power.

|         Components         | Lvl |  Type  | Rank | Ship | Dist. |
|:--------------------------:|:---:|:------:|:----:|:----:|:-----:|
| 10 x T aura, 5 x N paysans | 14  | Normal |  5   |      |       |

`CAST [LEVEL n] "Unholy Strength" <unit-id> [<unit-id> ...]`  

<!-- From [https://wiki.eressea.de/index.php?title=Draigzauber&oldid=6510] -->
