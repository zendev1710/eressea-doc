---
# cSpell:locale en
alias: gwyrrd-spells
---
# Gwyrrd spells

## Level 1

### Create [[stone-golem|Stone Golems]]

:   Moisten a gap-free block of fine crystalline rock with a vial of the water of life until it has been completely absorbed into the rock.  
    Then you direct your strength towards the fine aura of life that is forming and form a housing for the unbound strength.  
    The more power the magician invests, the more golems can be created before the aura dissipates.  
    Each golem has a 10 percent chance of turning to dust each round.  
    If you give the golems the `MAKE CASTLE` or `MAKE STREET` orders, 4 stones are placed per golem and the golem dissolves.

| Components                                        | Lvl |   Type | Rank | Ship | Dist. |
|---------------------------------------------------|----:|-------:|:----:|:-----|:------|
| 2 x T auras, T [stones][stone], 1 [water of life] |   1 | Normal |  4   |      |       |

`CAST [LEVEL n] "Create Stone Golems"`  

### Blessed Harvest

:   This harvest ritual improves the yields of working farmers in the region by one piece of silver.  
    The more power the druid invests, the longer the spell lasts.

| Components | Lvl |   Type | Rank | Ship               | Dist.              |
|------------|----:|-------:|:----:|:-------------------|:-------------------|
| T auras    |   1 | Normal |  5   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Blessed Harvest"`  

### Cattle Healing

:   The Gwyrrd mages" livestock and healing skills are highly sought after by farmers.  
    Their services are often in high demand, especially in markets.  
    Some people may also use their talent to sell an animal for a better price.  
    The magician can earn 50 silver per level.

| Components | Lvl |    Type | Rank | Ship | Dist. |
|------------|----:|--------:|:----:|:-----|:------|
| T auras    |   5 | Post-c. |  5   |      |       |

`CAST [LEVEL n] "Cattle Healing"`  

## Level 2

### Create [[iron-golem|Iron Golems]]

<!-- TODO: fix MAKE orders -->
:   The more power the magician invests, the more golems can be created.  
    Each golem has a 15 percent chance of turning to dust each round.  
    If you give the golems the order `MAKE  Sword | Claymore` or `MAKE Shield | CHAIN ​​​​MAIL | PLATE ARMOR`, 4 iron bars are installed per golem and the golem dissolves.

| Components                                | Lvl |   Type | Rank | Ship | Dist. |
|-------------------------------------------|----:|-------:|:----:|:-----|:------|
| 2 x T auras, T [irons], 1 [water of life] |   2 | Normal |  4   |      |       |

`CAST [LEVEL n] "Create Iron Golems"`  

### Grove of Oak Trees

:   Where previously only a tree could sprout from a stick, every branch now sprouts roots.

| Components                               | Lvl |   Type | Rank | Ship | Dist.              |
|------------------------------------------|----:|-------:|:----:|:-----|:-------------------|
| 4 x T auras, T [wood], 1 [water of life] |   2 | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Grove of Oak Trees"`  

## Level 3

### [[mountain-guard|Mountain Guardian]]

:   Creates a guardian spirit that prevents iron and metal mining in glaciers and mountains by non-allied factions (`HELP GUARD`) as long as it guards the region.  
    The mountain guardian is bound to the location of the summoning.

| Components  | Lvl |   Type | Rank | Ship | Dist.              |
|-------------|----:|-------:|:----:|:-----|:-------------------|
| 3 x T auras |   3 | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] Mountain Guardian`  

### Firun's Coat

:   This spell allows the magician to magically protect insects from the crippling cold of the glaciers.  
    You can enter glaciers and act normally there.  
    The saying works on a level*10 insects.  
    A Ring of Power increases the number of enchantable insects by an additional 10.

| Components  | Lvl |   Type | Rank | Ship               | Dist. |
|-------------|----:|-------:|:----:|:-------------------|:------|
| 2 x T auras |   3 | Normal |  5   | :heavy_check_mark: |       |

`CAST [LEVEL n] "Firun's Coat" <unit-id> [<unit-id> ...]`  

### Hail

:   In battle, the magician calls upon the elemental spirits of cold and binds them to himself.  
    He can then order them to attack the enemy with hailstones and chunks of ice.

| Components | Lvl |   Type | Rank | Ship | Dist. |
|------------|----:|-------:|:----:|:-----|:------|
| T auras    |   3 | Combat |  5   |      |       |

`COMBATSPELL [LEVEL n] Hail`  

### Rain of Rust

:   This ritual conjures up a dark storm front that towers ominously over the region.  
    The magical rain will cause all ore to rust.  
    Iron weapons and armor become chipped and rusty.  
    The destructive power of the rain depends on the power invested by the magician.  
    Up to 10 iron weapons can be affected for each level.  
    A ring of power increases the effect like an additional level.

| Components  | Lvl |   Type | Rank | Ship | Dist.              |
|-------------|----:|-------:|:----:|:-----|:-------------------|
| 2 x T auras |   3 | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Rain of Rust" <unit-id> [<unit-id> ...]`  

## Level 4

### Magic Path

:   By performing these rituals, the magician is able to summon a powerful earth elemental.  
    As long as this is banished into the ground, no rain will soften the paths and no river will be able to destroy bridges.  
    This means that all travelers receive the same advantages that would otherwise only be offered by a developed paved road network.  
    Even swamps and glaciers can be enchanted this way.  
    The more power the magician puts into the spell, the longer the road lasts.

| Components                 | Lvl |   Type | Rank | Ship               | Dist.              |
|----------------------------|----:|-------:|:----:|:-------------------|:-------------------|
| T auras, 1 [stone], 1 bois |   4 | Normal |  5   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Magic Path"`  

### Mallorn quarterstaff
<!-- TODO: check if it's really mallorn quarterstaff -->

:   This ritual increases the effect of the magical potion many times over.  
    Where previously only a tree could sprout from a stick, every branch now sprouts roots.

| Components                                    | Lvl |   Type | Rank | Ship | Dist.              |
|-----------------------------------------------|----:|-------:|:----:|:-----|:-------------------|
| 6 x T auras, T [[mallorn]], 1 [water of life] |   4 | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Mallorn quarterstaff"`  

### Summon Water Elemental

:   With this ritual, the magician forces the elemental spirits of the water into his service and gets them to carry the specified ship through the water more quickly.  
    In addition, the ship is not affected by unfavorable winds or currents.

| Components | Lvl |   Type | Rank | Ship               | Dist. |
|------------|----:|-------:|:----:|:-------------------|:------|
| T auras    |   4 | Normal |  5   | :heavy_check_mark: |       |

`CAST [LEVEL n] Summon Water Elemental <ship-id>`  

### Air Shield

:   Invoking the Elemental Spirits of Wind conjures up sudden gusts of wind, small gusts of wind, and vents that will hinder opposing archers.

| Components  | Lvl |   Type | Rank | Ship               | Dist. |
|-------------|----:|-------:|:----:|:-------------------|:------|
| 2 x T auras |   4 | Pre-c. |  5   | :heavy_check_mark: |       |

`COMBATSPELL [LEVEL n] "Air Shield"`  

## Level 5

### Astral Guardian Spirits

:   This ritual summons some elemental spirits of magic and sends them into the ranks of the enemy mages.  
    These will find it much more difficult to cast spells for the duration of the fight.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 5 x T auras |   5 | Pre-c. |  2   |      |       |

`COMBATSPELL [LEVEL n] "Astral Guardian Spirits"`  

### Create a [[magical-herb-pouch]]

:   The Druid takes some prepared leather, which he cleanses of all unclean spirits in a great ritual of purification, and then binds some small spirits of air and water into the material.  
    He now uses the leather prepared in this way to make a small bag that can better preserve the herbs stored in it.

| Components                                    | Lvl |   Type | Rank | Ship               | Dist. |
|-----------------------------------------------|----:|-------:|:----:|:-------------------|:------|
| 30 auras, 1 permanent aura, 1 [water of life] |   5 | Normal |  5   | :heavy_check_mark: |       |

`CAST "Create A magical Herb Pouch"`

### Heal

:   It"s not just the medic who can help the wounded in battle.  
    Druids are able to close wounds, set broken bones and regenerate even severed limbs by summoning the elemental spirits of life.

| Components | Lvl |    Type | Rank | Ship | Dist. |
|------------|----:|--------:|:----:|:-----|:------|
| T auras    |   5 | Post-c. |  5   |      |       |

`COMBATSPELL [LEVEL n] Heal`  

### Whirlwind

:   This incantation opens a gate into the plane of the elemental spirits of the wind.  
    Strong winds or even storms immediately arise in the area around the gate and hinder all archers in a battle.

| Components | Lvl |   Type | Rank | Ship | Dist. |
|------------|----:|-------:|:----:|:-----|:------|
| 15 auras   |   5 | Pre-c. |  5   |      |       |

`COMBATSPELL [LEVEL n] Whirlwind`  

## Level 6

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

### Meditate

:   With the help of this spell, the magician can transfer his own aura at a ratio of 2:1 to another magician of the same magic area.

| Components | Lvl |   Type | Rank | Ship               | Dist. |
|------------|----:|-------:|:----:|:-------------------|:------|
| 2 auras    |   6 | Normal |  1   | :heavy_check_mark: |       |

`CAST Meditate <unit-id> <Aura>`  

## Level 7

### Summon Storm Elemental

:   Summoning elemental spirits of storms is an ancient ritual.  
    The druid banishes the elementals into the sails of the ships, where they help carry the ship over the waves at high speed.  
    The more power the druid invests in the spell, the greater the number of elemental spirits that can be banished. An elemental spirit is required for each ship.

| Components  | Lvl |   Type | Rank | Ship                   | Dist. |
|-------------|----:|-------:|:----:|:-----------------------|:------|
| 6 x T auras |   6 | Normal |  5   | :heavy_check_mark:[^3] |       |

`CAST [LEVEL n] "Summon Storm Elemental" <ship-id> [<ship-id> ...]`  

### Summon Earth Elemental

:   With this ritual, the druid summons an elemental spirit of the earth and causes it to cause the earth to tremble.  
This earthquake will damage all buildings in the region.

| Components         | Lvl |   Type | Rank | Ship | Dist.              |
|--------------------|----:|-------:|:----:|:-----|:-------------------|
| 25 auras, 2 [laen] |   7 | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] "Summon Earth Elemental"`  

### Homestone

:   With this formula, the magician binds the forces of the earth forever into the walls of the castle in which he currently finds himself.  
    Walls that have been strengthened in this way cannot be destroyed either by magic or with heavy artillery, and age also affects them less.  
    The building also offers better protection against attacks with swords and magic.

| Components                 | Lvl |   Type | Rank | Ship | Dist. |
|----------------------------|----:|-------:|:----:|:-----|:------|
| 50 auras, 1 permanent aura |   7 | Normal |  5   |      |       |

`CAST Homestone`  

### Timber Wolves

:   Over the course of their lives in nature, quite a few Druids become friends with the oldest friends of the great peoples.  
    They learn to summon many of their friends to aid them in battle with a single howling call.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 2 x T auras |   7 | Pre-c. |  5   |      |       |

`COMBATSPELL [LEVEL n] "Timber Wolves"`  

## Level 8

### Gaze of the Basilisk

:   This difficult but effective combat spell uses the elemental spirits of stone to turn a number of enemies to stone for the duration of the battle.  
    The affected people will no longer fight, but they cannot be wounded either.

| Components | Lvl |   Type | Rank | Ship | Dist. |
|------------|----:|-------:|:----:|:-----|:------|
| T auras    |   8 | Combat |  5   |      |       |

`COMBATSPELL [LEVEL n] "Gaze of the Basilisk"`  

### Banish Spirits

:   According to the ancient teachings of the Druids, what ordinary beings call magic consists of elemental spirits.  
    The magician conjures and banishes these into a form to achieve the desired effect.  
    This ritual is able to drive away elemental spirits that have been summoned into this world in order to free an object from magic.

| Components  | Lvl |   Type | Rank | Ship               | Dist.              |
|-------------|----:|-------:|:----:|:-------------------|:-------------------|
| 6 x T auras |   8 | Normal |  2   | :heavy_check_mark: | :heavy_check_mark: |

`CAST [REGION x y] [LEVEL n] "Banish Spirits" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Strong Wall And Sturdy Gate

:   With this formula, at the beginning of a fight, the magician binds some elemental spirits of the rock into the walls of the building in which he is currently located.  
    The building then offers better protection against attacks with the sword and magic.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 2 x T auras |   8 | Pre-c. |  5   |      |       |

`COMBATSPELL [LEVEL n] "Strong Wall And Sturdy Gate"`  

## Level 9

### Sacred Ground

:   This ritual summons various natural spirits into the soil of the region, which guard it from then on.  
    In such a blessed region, the dead will never again leave their graves, and undead that have arisen elsewhere will avoid them whenever possible.

| Components                  | Lvl |   Type | Rank | Ship | Dist. |
|-----------------------------|----:|-------:|:----:|:-----|:------|
| 80 auras, 3 permanent auras |   9 | Normal |  5   |      |       |

`CAST "Sacred Ground"`  

### Ties of Life

:   A druid who has fallen into the world of spirits can use this spell to level up*Send 5 units of weight back to a forest on the material world.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 2 x T auras |   9 | Normal |  7   |      |       |

`CAST [LEVEL n] "Sog des Lebens" <x> <y> <unit-id> [<unit-id> ...]`  

### Path of Trees

:   Great power lies in places where life pulsates.  
    The druid can collect this power and create a gateway into the world of spiritual beings.  
    The druid can then level*Send 5 units of weight through the gate.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 3 x T auras |   9 | Normal |  7   |      |       |

`CAST [LEVEL n] "Path of Trees" <unit-id> [<unit-id> ...]`  

## Level 10

### Awakening of the [Ents]

:   With the help of this spell, the druid awakens the Ents slumbering in the forests of the region from their eons-long sleep.  
    The wild tree creatures will join him and assist him, but after a while they will fall back into slumber.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 6 x T auras |  10 | Normal |  5   |      |       |

`CAST [LEVEL n] "Awakening of the Ents"`  

### Summon Familiar

:   At some point in his wanderings, an experienced magician will encounter an unusual specimen of a species that will join the magician.

| Components                   | Lvl |   Type | Rank | Ship | Dist. |
|------------------------------|----:|-------:|:----:|:-----|:------|
| 100 auras, 5 permanent auras |  10 | Normal |  5   |      |       |

`CAST "Summon Familiar"`  

## Level 11

### Segne Steinkreis <!-- TODO -->

:   This ritual blesses a stone circle that must first be built from stones and some wood.  
    The Druid"s Blessing turns the circle into a powerful site of magical activity, providing protection from magic and increased aura regeneration.  
    It is said that virgins encountered strange creatures around stone circles.

| Components                   | Lvl |   Type | Rank | Ship | Dist. |
|------------------------------|----:|-------:|:----:|:-----|:------|
| 350 auras, 5 permanent auras |  11 | Normal |  5   |      |       |

`CAST "Segne Steinkreis" <building-id>`  

## Level 12

### Rindenhaut  <!-- TODO -->

:   This ritual, cast before battle, grants your troops an additional armor bonus.  
    Each hit reduces the spell's power, so the shield will eventually dissipate during the fight.

| Components  | Lvl |   Type | Rank | Ship | Dist. |
|-------------|----:|-------:|:----:|:-----|:------|
| 4 x T auras |  12 | Pre-c. |  2   |      |       |

`COMBATSPELL [LEVEL n] Rindenhaut`  

## Level 13

### Hitzeelementar  <!-- TODO -->

:   This ritual summons angry heat elementals.  
    A drought is plaguing the country.  
    Trees wither, animals die, and the harvest fails.  
    There is hardly any work to be found in agriculture for day laborers.

| Components | Lvl |   Type | Rank | Ship | Dist.              |
|------------|----:|-------:|:----:|:-----|:-------------------|
| 600 auras  |  13 | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] Hitzeelementar`  

## Level 15

### Mahlstrom  <!-- TODO -->

:   This ritual summons a great water elemental from the depths of the ocean.  
    The elemental creates a massive whirlpool, a maelstrom, which can severely damage any ships that pass through it.

| Components                          | Lvl |   Type | Rank | Ship                   | Dist. |
|-------------------------------------|----:|-------:|:----:|:-----------------------|:------|
| 200 auras, 1 tête de serpent de mer |  15 | Normal |  5   | :heavy_check_mark:[^3] |       |

`CAST Mahlstrom`  

## Level 16

### Wurzeln der Magie <!-- TODO -->

:   With the help of this elaborate ritual, the druid allows part of his power to flow permanently into the soil and forests of the region.  
    This will change the balance of nature in the region forever, and in the future only the demanding but strong mallorns will thrive in the region.

| Components                                      | Lvl |   Type | Rank | Ship | Dist.              |
|-------------------------------------------------|----:|-------:|:----:|:-----|:-------------------|
| 250 auras, 10 permanent auras, 1 [[cream-puff]] |  16 | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] "Wurzeln der Magie"`  

## Level 17

### Tor in die Ebene der Hitze <!-- TODO -->

:   This powerful ritual opens a gateway into the elemental plane of heat.  
    A great drought is coming to the country.  
    Farmers, animals and plants in the region are fighting for survival, but only half of all living things can survive such a drought.  
    The region can be affected by the consequences of such a drought for years to come.

| Components | Lvl |   Type | Rank | Ship | Dist.              |
|------------|----:|-------:|:----:|:-----|:-------------------|
| 800 auras  |  17 | Normal |  5   |      | :heavy_check_mark: |

`CAST [REGION x y] "Tor in die Ebene der Hitze"`  

<!-- From [https://wiki.eressea.de/index.php?title=Gwyrrdzauber&oldid=7693] -->

[water of life]: ./alchemy.md#water-of-life
[wood]: ./resources.md#wood
[irons]: ./resources.md#iron
[stone]: ./resources.md#stone
[mallorn]: ./resources.md#mallorn
