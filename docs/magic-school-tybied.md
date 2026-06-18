---
# cSpell:locale en
alias: tybied-spells
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD042 MD052 -->
# Tybied spells

## Level 1

### Analyze Magic

:   This spell allows the magician to attempt to detect the enchantments of a single specified object.  
    He will be able to get an impression of their effectiveness from all spells that do not exceed his own abilities.  
    With stronger spells he needs a little luck for a successful analysis.

| Components | Lvl |  Type  | Rank |             Ship             | Dist. |
|:----------:|:---:|:------:|:----:|:----------------------------:|:-----:|
|   T aura   |  1  | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Analyze Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Concealing Aura

:   This spell will obscure all of the target unit"s equipment from view for a period of time.

| Components | Lvl |  Type  | Rank |             Ship             | Dist. |
|:----------:|:---:|:------:|:----:|:----------------------------:|:-----:|
|   T aura   |  1  | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Concealing Aura" <unit-id>`  

### Miracle Doctor

:   If the alchemist cannot help you, you go to the learned Tybied magician.  
    His potions and tinctures help against everything you can"t get otherwise.  
    Whether the cryptic formula under the wooden shoe of the unfaithful husband really helped -well, the farmer who doesn't know how to read will never know.  
    It definitely helps the magician...fill his wallet.  
    You can earn 50 silver per level in a week.

| Components | Lvl |  Type  | Rank |             Ship             | Dist. |
|:----------:|:---:|:------:|:----:|:----------------------------:|:-----:|
|   T aura   |  1  | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Miracle Doctor"`  

### Protection from Magic

:   This spell places an antimagic field around enemy mages, significantly hindering their spell casting.  
    Only a few will have the strength to penetrate the field and aid their troops in battle.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 3 x T aura |  2  | Pre-c. |  2   |      |       |

`COMBATSPELL [LEVEL n] "Protection from Magic"`  

### Save Spoils

:   This spell prevents some of the objects that would otherwise be destroyed in battle from being damaged.  
    Losses are reduced by 5% per level of the spell, up to a minimum of 25%.

| Components | Lvl |  Type   | Rank | Ship | Dist. |
|:----------:|:---:|:-------:|:----:|:----:|:-----:|
|   T aura   |  3  | Post-c. |  5   |      |       |

### Resist Magic

:   This spell increases your natural resistance to magic.  
    A unit protected in this way is also less vulnerable to combat magic.  
    Per level, the magician"s power is enough to protect 5 people.

| Components | Lvl |  Type  | Rank |             Ship             | Dist. |
|:----------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 5 x T aura |  3  | Normal |  2   | :material-check:{ .success } |       |

`CAST [LEVEL n] Resist Magic <unit-id> [<unit-id> ...]`  

### Astral Exit

:   The magician concentrates on the structure of reality and can thus leave the Astral plane.  
    He can overall (Level-3)*Send 15 lbs through the briefly created gate.  
    If the magician is experienced enough to cast the spell at levels 11 or more, he can force other units to the other level even against their will.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 2 x T aura |  4  | Normal |  7   |      |       |

`CAST [LEVEL n] "Astral Exit" <x> <y> <unit-id> [<unit-id> ...]`  

### Astral Path

:   Ancient arcane formulas allow the magician to send himself and others into the Astral plane.  
    The magician can (level 3)*Send 15 lbs through the briefly created gate.  
    If the magician is experienced enough to cast the spell at levels 11 or more, he can force other units to the other level even against their will.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 2 x T aura |  4  | Normal |  7   |      |       |

`CAST [LEVEL n] "Astral Path" <unit-id> [<unit-id> ...]`  

### Antimagic

:   With this spell the magician can create a zone of Astral weakening, a local imbalance in the Astral field.  
    This zone will strive to return to equilibrium.  
    To do this, it will remove part of the strength of every spell cast in this region and even completely absorb the weaker ones.

| Components | Lvl |  Type  | Rank | Ship |            Dist.             |
|:----------:|:---:|:------:|:----:|:----:|:----------------------------:|
| 3 x T aura |  5  | Normal |  2   |      | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Antimagic"`  

### Transfer Aura

:   With the help of this spell, the magician can transfer his own aura to another magician of the same magic area at a ratio of 2:1 or to a magician of another magic area at a ratio of 3:1.

| Components | Lvl |  Type  | Rank |             Ship             | Dist. |
|:----------:|:---:|:------:|:----:|:----------------------------:|:-----:|
|   1 aura   |  5  | Normal |  1   | :material-check:{ .success } |       |

`CAST "Transfer aura" <unit-id> <Aura>`  

### Destroy Magic

:   This spell allows the magician to dispel enchantments on a unit, ship, building, or even region.

| Components | Lvl |  Type  | Rank |             Ship             |            Dist.             |
|:----------:|:---:|:------:|:----:|:----------------------------:|:----------------------------:|
| 4 x T aura |  5  | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Destroy Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Shockwave

:   This spell causes a wave of pure power to sweep across the enemy ranks.  
    The shock will leave many fighters so dazed that they will be unable to attack for a brief moment.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|   T aura   |  5  | Combat |  5   |      |       |

`COMBATSPELL [LEVEL n] Shockwave`  

### Astral Call

:   A magician who is in the Astral plane can use this spell to bring other units to him.  
    The magician can (level 3)*Send 15 lbs through the briefly created gate.  
    If the magician is experienced enough to cast the spell at levels 13 or more, he can force other units to the other level even against their will.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 2 x T aura |  6  | Normal |  7   |      |       |

`CAST [LEVEL n] "Astral Call" <x> <y> <unit-id> [<unit-id> ...]`  

### Create an [Amulet of True Sight][amulet-of-true-sight-id]

:   The spell allows a magician to create an [Amulet of True Sight][amulet-of-true-sight-id].  
    The amulet allows the wearer to see all units protected by a ring of invisibility.  
    However, units that use their [stealth][skill-stealth-id] skill to hide still remain undetected.

|               Components                | Lvl |  Type  | Rank |             Ship             | Dist. |
|:---------------------------------------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 50 aura, 3 000 silver, 1 permanent aura |  6  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create An Amulet of True Sight"`  

### Create a [Ring of Invisibility][ring-of-invisibility-id]

:   With this spell the wizard can create a ring of invisibility.  
    The bearer of the ring becomes invisible to all units of other parties, no matter how good their perception may be.  
    In an invisible unit, each person must wear a ring.

|               Components                | Lvl |  Type  | Rank |             Ship             | Dist. |
|:---------------------------------------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 50 aura, 3 000 silver, 1 permanent aura |  6  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Ring of Invisibility"`  

### Airship

:   These magic runes allow a boat with a capacity of up to 50 weight units to fly for a week and allow the boat to cross land.  
    The enchanted ink's components include a windbag and a snowcrystal petal.

|                     Components                      | Lvl |  Type  | Rank |             Ship             | Dist. |
|:---------------------------------------------------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 10 aura, 1 [gousse], 1 [pétale de cristal de neige] |  6  | Normal |  5   | :material-check:{ .success } |       |

`CAST Airship <ship-id>`  

### Call of Reality

:   A magician who is in the material world can use this spell to summon units from the adjacent Astral world.  
    If the magician is experienced enough to cast the spell at levels of 13 or more, he can force other units into the material world against their will.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 2 x T aura |  6  | Normal |  7   |      |       |

`CAST [LEVEL n] "Call of Reality" <unit-id> [<unit-id> ...]`  

### Steal Aura

:   With the help of this spell, the magician can withdraw his aura from another magician against his will and supply it to himself.

| Components | Lvl |  Type  | Rank | Ship |            Dist.             |
|:----------:|:---:|:------:|:----:|:----:|:----------------------------:|
| 2 x T aura |  6  | Normal |  3   |      | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Steal Aura" <unit-id>`  

[](){ #t-create-an-antimagic-crystal-id }

### Create an [Antimagic Crystal][antimagic-crystal]

:   With the help of this spell, the magician drains a quartz crystal of all its magical energies.  
    The crystal, when ground into a fine dust and dispersed, will absorb the magical energies released during casting and reduce the power of all spells cast in the region that week.

|      Components       | Lvl |  Type  | Rank |             Ship             | Dist. |
|:---------------------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 50 aura, 3 000 silver |  7  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create An Antimagic Crystal"`  

### Negate Curse

:   This spell allows the magician to specifically dispel a specific enchantment on a unit, ship, building or even the region.

| Components | Lvl |  Type  | Rank |             Ship             |            Dist.             |
|:----------:|:---:|:------:|:----:|:----------------------------:|:----------------------------:|
| 3 x T aura |  7  | Normal |  3   | :material-check:{ .success } | :material-check:{ .success } |

`CAST [REGION x y] [LEVEL n] "Negate Curse" ( REGION | UNIT <unit-id> | SHIP <ship-id> | CASTLE <building-id> ) <spell-id>`  

### Eternal Walls

:   With this formula, the magician binds the forces of the earth into the walls of the building forever.  
    A building enchanted in this way is protected against the ravages of time and no longer requires any maintenance.

|        Components         | Lvl |  Type  | Rank |             Ship             | Dist. |
|:-------------------------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 50 aura, 1 permanent aura |  7  | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Eternal Walls" <building-id>`  

### Protective Runes

:   If you draw these runes on the walls of a building or on the planks of a ship, it will be more difficult to influence by magic.  
    Each ritual increases the building or ship"s resistance to enchantment by 20%.  
    If several protective spells are placed on top of each other, their effects are added together, but 100% protection cannot be achieved this way.  
    The spell lasts at least three weeks, but depending on the magician"s skill it can last much longer.

| Components | Lvl |  Type  | Rank |             Ship             | Dist. |
|:----------:|:---:|:------:|:----:|:----------------------------:|:-----:|
|  20 aura   |  8  | Normal |  2   | :material-check:{ .success } |       |

`CAST "Protective Runes" ( SHIP <ship-id> | CASTLE <building-id> )`  

### Shield of the Fish

:   This spell can give the enemy a slightly different image of their own troops, just like the fish in the water is not where it seems to be.  
    In this way, half of the damage from each hit can be rendered harmless.  
    But the shield can only withstand a few hundred sword blows, after which it will disintegrate.  
    The stronger the magician, the more damage the shield can withstand.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 4 x T aura |  8  | Pre-c. |  2   |      |       |

`COMBATSPELL [LEVEL n] "Shield of the Fish"`  

### Acceleration

:   This spell speeds up some fighters on your side so that they can attack twice in one combat round throughout the entire combat.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 5 x T aura |  9  | Pre-c. |  5   |      |       |

`COMBATSPELL [LEVEL n] Acceleration`  

### Create a [Ring of Power][ring-of-power-id]

:   This powerful ritual creates a ring of power.  
    A ring of power increases the power of any spell its wearer casts, as if the mage were one level better.

|               Components                | Lvl |  Type  | Rank |             Ship             | Dist. |
|:---------------------------------------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 100 aura, 1 permanent aura, 4000 silver |  9  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Ring of Power"`  

### Gaze Upon Reality

:   With this spell the mage can glance from the astral to the material plane and recognize regions and units.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|  40 aura   | 10  | Normal |  5   |      |       |

`CAST "Gaze Upon Reality"`  

### Create A Bag of Holding

:   This bag encloses a dimensional rift in which up to 200 units of weight can be carries.  
    Horses and other large objects cannot be put into the bag.  
    The bag itself has a weight of 1.

|               Components                | Lvl |  Type  | Rank |             Ship             | Dist. |
|:---------------------------------------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 30 aura, 1 permanent aura, 5 000 silver | 10  | Normal |  5   | :material-check:{ .success } |       |

`CAST "Create A Bag of Holding"`

### Double Time

:   Abstract theories of space and time at last find practical application in this spell which warps the very fabric of time around a person.  
    Such a person has twice as many movement points and doubles their attacks per round for a few weeks.

| Components | Lvl |  Type  | Rank |             Ship             | Dist. |
|:----------:|:---:|:------:|:----:|:----------------------------:|:-----:|
| 5 x T aura | 11  | Normal |  5   | :material-check:{ .success } |       |

`CAST [LEVEL n] "Double Time" <unit-id> [<unit-id> ...]`  

### Shield Shine

:   This ritual, to be performed before battle, gives the own troops an added bonus to their armor.  
    Every hit reduces the strength of the spell until it dissipates during battle.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
| 4 x T aura | 12  | Pre-c. |  2   |      |       |

`COMBATSPELL [LEVEL n] "Shield Shine"`  

### Summon Familiar

:   At some point in his wanderings, an experienced magician will encounter an unusual specimen of a species that will join the magician.

|         Components         | Lvl |  Type  | Rank | Ship | Dist. |
|:--------------------------:|:---:|:------:|:----:|:----:|:-----:|
| 100 aura, 5 permanent aura | 12  | Normal |  5   |      |       |

`CAST "Summon Familiar"`  

### Living Rock

:   This draining ritual summons a gigantic earth elemental from a sphere of laen and binds it to a building.  
    The elemental can then be commanded to move the building with all its occupants to a neighbouring region.
    The strength of the elemental depends of the mage's skill: it can move up to (level-12)*250 size units of building.
    The building won't remain undamaged by the process.

|                    Components                    | Lvl |  Type  | Rank | Ship | Dist. |
|:------------------------------------------------:|:---:|:------:|:----:|:----:|:-----:|
| 10 x T aura, 1 permanent aura, 5 [laen][laen-id] | 13  | Normal |  5   |      |       |

`CAST [LEVEL n] "Living Rock" <building-id> <Richtung>`  

### Astral Disruption

:   This spell causes a severe disturbance of the astral plane.  
    Within an astral radius of level/5 regions all astral creatures not able to resist the spell will be thrown from the astral plane.  
    The astral contact with all affected regions will be disrupted for level/3 weeks.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|  140 aura  | 14  | Normal |  4   |      |       |

`CAST [LEVEL n] "Astral Disruption"`  

### Sacrifice Strength

:   This spell allows the magician to transfer part of his magical powers to another magician.  
    Magicians of the seam school will receive half the power invested, magicians of other schoolsreceive receive one third.

| Components | Lvl |  Type  | Rank | Ship | Dist. |
|:----------:|:---:|:------:|:----:|:----:|:-----:|
|  100 aura  | 15  | Normal |  1   |      |       |

`CAST "Sacrifice Strength" <unit-id> <Aura>`  

<!-- From [https://wiki.eressea.de/index.php?title=Tybiedzauber&oldid=7486] -->
