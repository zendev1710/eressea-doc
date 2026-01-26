---
# cSpell:locale en
alias: tybied-spells
---
# Tybied spells

## Level 1

### Analyze Magic

:   This spell allows the magician to attempt to detect the enchantments of a single specified object.  
    He will be able to get an impression of their effectiveness from all spells that do not exceed his own abilities.  
    With stronger spells he needs a little luck for a successful analysis.

| Components | Lvl |   Type | Rank | Ship               | Dist. |
|------------|----:|-------:|:----:|:-------------------|:------|
| T auras    |   1 | Normal |  5   | :heavy_check_mark: |       |

`CAST [LEVEL n] "Analyze Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Concealing Aura

:   This spell will obscure all of the target unit"s equipment from view for a period of time.

| Components | Lvl |   Type | Rank | Ship               | Dist. |
|------------|----:|-------:|:----:|:-------------------|:------|
| T auras    |   1 | Normal |  5   | :heavy_check_mark: |       |

`CAST [LEVEL n] "Concealing Aura" <unit-id>`  

### Miracle Doctor

:   If the alchemist cannot help you, you go to the learned Tybied magician.  
    His potions and tinctures help against everything you can"t get otherwise.  
    Whether the cryptic formula under the wooden shoe of the unfaithful husband really helped -well, the farmer who doesn't know how to read will never know.  
    It definitely helps the magician...fill his wallet.  
    You can earn 50 silver per level in a week.

| Components | Lvl |   Type | Rank | Ship               | Dist. |
|------------|----:|-------:|:----:|:-------------------|:------|
| T auras    |   1 | Normal |  5   | :heavy_check_mark: |       |

`CAST [LEVEL n] "Miracle Doctor"`  

### Protection from Magic

:   This spell places an antimagic field around enemy mages, significantly hindering their spell casting.  
    Only a few will have the strength to penetrate the field and aid their troops in battle.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 3 x T auras |   2 | Pre-c. |  2   |      |       |

`COMBATSPELL [LEVEL n] "Protection from Magic"`  

### Save Spoils

:   This spell prevents some of the objects that would otherwise be destroyed in battle from being damaged.  
    Losses are reduced by 5% per level of the spell, up to a minimum of 25%.

| Components | Lvl |    Type | Rank | Ship | Dist. |
|------------|----:|--------:|:----:|:-----|:------|
| T auras    |   3 | Post-c. |  5   |      |       |

### Resist Magic

:   This spell increases your natural resistance to magic.  
    A unit protected in this way is also less vulnerable to combat magic.  
    Per level, the magician"s power is enough to protect 5 people.

| Components  | Lvl |   Type | Rank | Ship               | Dist. |
|-------------|----:|-------:|:----:|:-------------------|:------|
| 5 x T auras |   3 | Normal |  2   | :heavy_check_mark: |       |

`CAST [LEVEL n] Resist Magic <unit-id> [<unit-id> ...]`  

### Astral Exit

:   The magician concentrates on the structure of reality and can thus leave the Astral plane.  
    He can overall (Level-3)*Send 15 kg through the briefly created gate.  
    If the magician is experienced enough to cast the spell at levels 11 or more, he can force other units to the other level even against their will.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 2 x T auras |   4 | Normal |  7   |      |       |

`CAST [LEVEL n] "Astral Exit" <x> <y> <unit-id> [<unit-id> ...]`  

### Astral Path

:   Ancient arcane formulas allow the magician to send himself and others into the Astral plane.  
    The magician can (level 3)*Send 15 kg through the briefly created gate.  
    If the magician is experienced enough to cast the spell at levels 11 or more, he can force other units to the other level even against their will.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 2 x T auras |   4 | Normal |  7   |      |       |

`CAST [LEVEL n] "Astral Path" <unit-id> [<unit-id> ...]`  

### Antimagic

:   With this spell the magician can create a zone of Astral weakening, a local imbalance in the Astral field.  
    This zone will strive to return to equilibrium.  
    To do this, it will remove part of the strength of every spell cast in this region and even completely absorb the weaker ones.

| Components  | Lvl |   Type | Rank | Ship | Dist.              |
|-------------|----:|-------:|:----:|:-----|:-------------------|
| 3 x T auras |   5 | Normal |  2   |      | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Antimagic"`  

### Transfer Aura

:   With the help of this spell, the magician can transfer his own aura to another magician of the same magic area at a ratio of 2:1 or to a magician of another magic area at a ratio of 3:1.

| Components | Lvl |   Type | Rank | Ship               | Dist. |
|------------|----:|-------:|:----:|:-------------------|:------|
| 1 aura     |   5 | Normal |  1   | :heavy_check_mark: |       |

`CAST "Transfer aura" <unit-id> <Aura>`  

### Destroy Magic

:   This spell allows the magician to dispel enchantments on a unit, ship, building, or even region.

| Components  | Lvl |   Type | Rank | Ship               | Dist.              |
|-------------|----:|-------:|:----:|:-------------------|:-------------------|
| 4 x T auras |   5 | Normal |  2   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Destroy Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Shockwave

:   This spell causes a wave of pure power to sweep across the enemy ranks.  
    The shock will leave many fighters so dazed that they will be unable to attack for a brief moment.

| Components | Lvl |   Type | Rank | Ship | Dist. |
|------------|----:|-------:|:----:|:-----|:------|
| T auras    |   5 | Combat |  5   |      |       |

`COMBATSPELL [LEVEL n] Shockwave`  

### Astral Call

:   A magician who is in the Astral plane can use this spell to bring other units to him.  
    The magician can (level 3)*Send 15 kg through the briefly created gate.  
    If the magician is experienced enough to cast the spell at levels 13 or more, he can force other units to the other level even against their will.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 2 x T auras |   6 | Normal |  7   |      |       |

`CAST [LEVEL n] "Astral Call" <x> <y> <unit-id> [<unit-id> ...]`  

### Create an [[amulet-of-true-sight]]

:   The spell allows a magician to create an [[amulet-of-true-sight]].  
    The amulet allows the wearer to see all units protected by a ring of invisibility.  
    However, units that use their [[camouflage]] skill to hide still remain undetected.

| Components                               | Lvl |   Type | Rank | Ship               | Dist. |
|------------------------------------------|----:|-------:|:----:|:-------------------|:------|
| 50 auras, 3 000 silver, 1 permanent aura |   6 | Normal |  5   | :heavy_check_mark: |       |

`CAST "Create An Amulet of True Sight"`  

### Create a [[ring-of-invisibility]]

:   With this spell the wizard can create a ring of invisibility.  
    The bearer of the ring becomes invisible to all units of other parties, no matter how good their perception may be.  
    In an invisible unit, each person must wear a ring.

| Components                               | Lvl |   Type | Rank | Ship               | Dist. |
|------------------------------------------|----:|-------:|:----:|:-------------------|:------|
| 50 auras, 3 000 silver, 1 permanent aura |   6 | Normal |  5   | :heavy_check_mark: |       |

`CAST "Create A Ring of Invisibility"`  

### Airship

:   These magical runes make a boat or longboat fly for a week.  
This can then also be used to cross land.  
For the color of the runes, a special ink must be mixed from a cream puff and a snow crystal.

| Components                                           | Lvl |   Type | Rank | Ship               | Dist. |
|------------------------------------------------------|----:|-------:|:----:|:-------------------|:------|
| 10 auras, 1 [gousse], 1 [pétale de cristal de neige] |   6 | Normal |  5   | :heavy_check_mark: |       |

`CAST Airship <ship-id>`  

### Call of Reality

:   A magician who is in the material world can use this spell to summon units from the adjacent Astral world.  
    If the magician is experienced enough to cast the spell at levels of 13 or more, he can force other units into the material world against their will.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 2 x T auras |   6 | Normal |  7   |      |       |

`CAST [LEVEL n] "Call of Reality" <unit-id> [<unit-id> ...]`  

### Steal Aura

:   With the help of this spell, the magician can withdraw his aura from another magician against his will and supply it to himself.

| Components  | Lvl |   Type | Rank | Ship | Dist.              |
|-------------|----:|-------:|:----:|:-----|:-------------------|
| 2 x T auras |   6 | Normal |  3   |      | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Steal Aura" <unit-id>`  

### Create an [[antimagic-crystal|Antimagic Crystal]]

:   With the help of this spell, the magician drains a quartz crystal of all its magical energies.  
    The crystal, when ground into a fine dust and dispersed, will absorb the magical energies released during casting and reduce the power of all spells cast in the region that week.

| Components             | Lvl |   Type | Rank | Ship               | Dist. |
|------------------------|----:|-------:|:----:|:-------------------|:------|
| 50 auras, 3 000 silver |   7 | Normal |  5   | :heavy_check_mark: |       |

`CAST "Create An Antimagic Crystal"`  

### Negate Curse

:   This spell allows the magician to specifically dispel a specific enchantment on a unit, ship, building or even the region.

| Components  | Lvl |   Type | Rank | Ship               | Dist.              |
|-------------|----:|-------:|:----:|:-------------------|:-------------------|
| 3 x T auras |   7 | Normal |  3   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Negate Curse" ( REGION | UNIT <unit-id> | SHIP <ship-id> | CASTLE <building-id> ) <spell-id>`  

### Eternal Walls

:   With this formula, the magician binds the forces of the earth into the walls of the building forever.  
    A building enchanted in this way is protected against the ravages of time and no longer requires any maintenance.

| Components                 | Lvl |   Type | Rank | Ship               | Dist. |
|----------------------------|----:|-------:|:----:|:-------------------|:------|
| 50 auras, 1 permanent aura |   7 | Normal |  5   | :heavy_check_mark: |       |

`CAST [LEVEL n] "Eternal Walls" <building-id>`  

### Protective Runes

:   If you draw these runes on the walls of a building or on the planks of a ship, it will be more difficult to influence by magic.  
    Each ritual increases the building or ship"s resistance to enchantment by 20%.  
    If several protective spells are placed on top of each other, their effects are added together, but 100% protection cannot be achieved this way.  
    The spell lasts at least three weeks, but depending on the magician"s skill it can last much longer.

| Components | Lvl |   Type | Rank | Ship               | Dist. |
|------------|----:|-------:|:----:|:-------------------|:------|
| 20 auras   |   8 | Normal |  2   | :heavy_check_mark: |       |

`CAST "Protective Runes" ( SHIP <ship-id> | CASTLE <building-id> )`  

### Shield of the Fish

:   This spell can give the enemy a slightly different image of their own troops, just like the fish in the water is not where it seems to be.  
    In this way, half of the damage from each hit can be rendered harmless.  
    But the shield can only withstand a few hundred sword blows, after which it will disintegrate.  
    The stronger the magician, the more damage the shield can withstand.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 4 x T auras |   8 | Pre-c. |  2   |      |       |

`COMBATSPELL [LEVEL n] "Shield of the Fish"`  

### Acceleration

:   This spell speeds up some fighters on your side so that they can attack twice in one combat round throughout the entire combat.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 5 x T auras |   9 | Pre-c. |  5   |      |       |

`COMBATSPELL [LEVEL n] Acceleration`  

### Create a [[ring-of-power]]

:   This powerful ritual creates a ring of power.  
    A ring of power increases the power of any spell its wearer casts, as if the mage were one level better.

| Components                               | Lvl |   Type | Rank | Ship               | Dist. |
|------------------------------------------|----:|-------:|:----:|:-------------------|:------|
| 100 auras, 1 permanent aura, 4000 silver |   9 | Normal |  5   | :heavy_check_mark: |       |

`CAST "Create A Ring of Power"`  

### Blick in die Realität <!-- TODO -->

:   With the help of this spell, the magician can look from the Astral plane into the material plane and recognize the regions and units precisely.

| Components | Lvl |   Type | Rank | Ship | Dist. |
|------------|----:|-------:|:----:|:-----|:------|
| 40 auras   |  10 | Normal |  5   |      |       |

`CAST "Blick in die Realität"`  

### Create a [[negative-weight-bag]] <!-- TODO: check -->

:   This bag encloses a small dimensional fold in which up to 200 weight units can be transported without being counted towards the carrying weight.  
    Horses and other living creatures as well as particularly bulky items (chariots and catapults) cannot be transported in the bag.  
    It is also not possible to transport one magic bag in another.  
    The bag itself weighs 1 kg.

| Components                               | Lvl |   Type | Rank | Ship               | Dist. |
|------------------------------------------|----:|-------:|:----:|:-------------------|:------|
| 30 auras, 1 permanent aura, 5 000 silver |  10 | Normal |  5   | :heavy_check_mark: |       |

`CAST "Create A Bag of Negative Weight"`   <!-- TODO: check -->

### Zeitdehnung <!-- TODO -->

:   This practical application of theoretical knowledge of space and time makes it possible to change the flow of time for some people.  
    People modified in this way get twice as many movement points and twice as many attacks per round for a few weeks.

| Components  | Lvl |   Type | Rank | Ship               | Dist. |
|-------------|----:|-------:|:----:|:-------------------|:------|
| 5 x T auras |  11 | Normal |  5   | :heavy_check_mark: |       |

`CAST [LEVEL n] Zeitdehnung <unit-id> [<unit-id> ...]`  

### Armor Shield  <!-- TODO -->
<!-- TODO: check if it is really Armor Shield -->

:   This ritual, which can be cast before battle, gives your troops an additional bonus to their armor.  
    Each hit reduces the spell"s power, so the shield will dissipate at some point in the fight.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 4 x T auras |  12 | Pre-c. |  2   |      |       |

`COMBATSPELL [LEVEL n] "Armor Shield"`  

### Summon Familiar

:   At some point in his wanderings, an experienced magician will encounter an unusual specimen of a species that will join the magician.

| Components                   | Lvl |   Type | Rank | Ship | Dist. |
|------------------------------|----:|-------:|:----:|:-----|:------|
| 100 auras, 5 permanent auras |  12 | Normal |  5   |      |       |

`CAST "Summon Familiar"`  

### Belebtes Gestein <!-- TODO -->

:   This energy-sapping ritual uses a ball of concentrated Laen to summon a massive earth elemental and banish it to a building.  
    The elemental can then be ordered to carry the building and all its inhabitants to a neighboring region.  
    The strength of the summoned elemental depends on the skill of the magician: the elemental can do maximum[Level-12]*Move 250 size units buildings.  
    The building will not survive this procedure unscathed.

| Components                               | Lvl |   Type | Rank | Ship | Dist. |
|------------------------------------------|----:|-------:|:----:|:-----|:------|
| 10 x T auras, 1 permanent aura, 5 [laen] |  13 | Normal |  5   |      |       |

`CAST [LEVEL n] "Belebtes Gestein" <building-id> <Richtung>`  

### Störe Astrale Integrität <!-- TODO -->

:   This spell causes severe disruption to the Astral space.  
    Within an Astral radius of level/5 regions, all Astral beings who cannot resist the spell are thrown out of the Astral plane.  
    Astral contact with all affected regions is disrupted for level/3 weeks.

| Components | Lvl |   Type | Rank | Ship | Dist. |
|------------|----:|-------:|:----:|:-----|:------|
| 140 auras  |  14 | Normal |  4   |      |       |

`CAST [LEVEL n] "Störe Astrale Integrität"`  

### Opfere Kraft  <!-- TODO -->

:   With the help of this spell, the magician can permanently transfer part of his magical power to another magician.  
    He can transfer half of the power used to a magician of the same magic area, and a third to other magicians.

| Components | Lvl |   Type | Rank | Ship | Dist. |
|------------|----:|-------:|:----:|:-----|:------|
| 100 auras  |  15 | Normal |  1   |      |       |

`CAST "Opfere Kraft" <unit-id> <Aura>`  

<!-- From [https://wiki.eressea.de/index.php?title=Tybiedzauber&oldid=7486] -->
