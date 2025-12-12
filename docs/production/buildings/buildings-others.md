---
alias:
    name: other-buildings
    text: Other Buildings
---
# Other Buildings

Buildings are built with the [MAKE "building type"] order and can be enlarged with [MAKE "building type" ID-building][MAKE "building type"]. Examples: MAKE [Lighthouse] or MAKE [Harbour] xyz. These buildings require a minimum level in Masonry skill, which is indicated in the table. Some buildings are of a specific size.

Here is a summarised table, more detailed explanations follow below.

Building; see also table on [building castles]  

The capacity refers only to the persons who can benefit from the building.  
\*: also 2 Mallorn and 2 Laen per size point

| Buildings      | Building costs |      |      |        | Skill | Upkeep  |          | Max. | Capacity   |
|----------------|----------------|------|------|--------|-------|---------|----------|------|------------|
|                | Stone          | Wood | Iron | Silver |       | Silver  | Resource |      |            |
| [Lighthouse]   | 2              | 1    | 1    | 100    | 3     | 100     | \-/-     | none | 4 persons  |
| [Mine]         | 5              | 10   | 1    | 250    | 4     | 500     | \-/-     | none | size       |
| [Quarry]       | 1              | 5    | 1    | 250    | 2     | 250     | \-/-     | none | size       |
| [Sawmill]      | 5              | 5    | 3    | 200    | 3     | 250     | \-/-     | none | size       |
| [Smithy]       | 5              | 5    | 2    | 200    | 3     | 300     | 1 wood   | none | size       |
| [Stable]       | 2              | 4    | 1    | 100    | 2     | 150     | \-/-     | none | size       |
| [Harbour]      | 5              | 5    | \-/- | 250    | 3     | 250     | \-/-     | 25   | size       |
| [Caravanserai] | 1              | 5    | 1    | 500    | 2     | 3000    | 2 horses | 10   | size       |
| [Academy]      | 5              | 5    | 1    | 500    | 3     | 1000    | \-/-     | 25   | size       |
| [Mage Tower]\* | 5              | 3    | 3    | 500    | 5     | 1000    | \-/-     | 50   | 2 Personen |
| [Dam]          | 5              | 10   | 1    | 500    | 4     | 1000    | 3 wood   | 50   | size       |
| [Tunnel]       | 10             | 5    | 1    | 300    | 6     | 100     | 2 stones | 100  | size       |
| [Inn]          | 4              | 3    | 1    | 200    | 2     | 5\*size | \-/-     | none | size       |
| [Monument]     | 1              | 1    | 1    | 400    | 4     | \-/-    | \-/-     | none | size       |
| [Stonecircle]  | 5              | 5    | \-/- | \-/-   | 2     | \-/-    | \-/-     | 100  | 3 Persons  |

## Lighthouse

|                          |                                      |
|--------------------------|--------------------------------------|
| Costs per point of size: | 2 stones, 1 wood, 1 iron, 100 Silver |
| Skill required:          | 3                                    |
| Maintenance per turn:    | 100 Silver                           |
| Maximum size:            | none                                 |
| Capacity:                | 4 units                              |

|      |            |            |
|------|------------|------------|
| Size | Perception | Visibility |
| 10   | 3          | 1          |
| 10   | 6          | 2          |
| 100  | 9          | 3          |
| 1000 | 12         | 4          |
| etc  |            |            |

- Beginning from size 10, a lighthouse reduces the possibility that a ship drifts off. This effect extends 1+ log10(size of the lighthouse) regions around the building.
- The lighthouse gives the occupants (only up to 4 units) information about ship sightings in all ocean regions within a radius of 1 + log10(lighthouse size) regions. The unit must have a perception of at least distance \* 3. A report from an ocean region three hexes away can only be obtained if the lighthouse is at least size 100 and the unit has at least perception 9.

## Mine

|                          |                                       |
|--------------------------|---------------------------------------|
| Costs per point of size: | 5 stones, 10 wood, 1 iron, 250 Silver |
| Skill required:          | 4                                     |
| Maintenance per turn:    | 500 Silver                            |
| Maximum size:            | none                                  |
| Capacity:                | 1 person per 1 size                   |

- Only half of the iron mined by units inside the mine is deducted from the region's supply. This effect works cumulatively together with any corresponding racial advantages.
- Units inside a mine extract as they have +1 on their mining skill, but it doesn’t apply to the mining level needed to reach a deeper layer.
- To produce laen you must be inside a mine.

**Examples:**

- A human with mining 2 can mine 3 iron from layers 1 or 2 if they are in a mine. Because of rounding, 2 iron are deducted from the region deposit. Two humans may mine 6 iron and only 3 are deducted.
- 10 dwarves mine 60 iron in a region. Because of their racial benefit, only 36 are deducted from the region deposit. If they are in a mine, only 18 iron will be deducted. If there are only 9 iron left in the region, they can of course online mine 15, or 30 iron, respectively.

## Quarry

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 1 stone, 5 wood, 1 iron, 250 Silver |
| Skill required:          | 2                                   |
| Maintenance per turn:    | 250 Silver                          |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- Only half of the stone mined by units inside the mine is deducted from the region's supply. This effect works cumulatively together with any corresponding racial advantages.
- Units inside a quarry extract as they have +1 on their Quarrying level, but it doesn’t apply to the mining level needed to reach a deeper layer

**Example:** 10 trolls produce 40 stones in a region. Due to the special ability of the trolls the supply of the region is only reduced by 30 stones. If the trolls are inside a quarry, the supply will be reduced by 15 Stones. If there are only 7 stones left in the region, the trolls can only produce 9 stones but 18 in a quarry.

## Sawmill

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 5 stone, 5 wood, 3 iron, 200 Silver |
| Skill required:          | 3                                   |
| Maintenance per turn:    | 250 Silver                          |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- Only half of the wood/saplings/mallorn produced by units inside a sawmill is subtracted from the supply in the region. This number is rounded up (i.e. if a unit, in a sawmill, makes 11 woods, 6 trees are cut).
- Units inside a sawmill get a +1 modifier to their forestry skill.

**Example:** With [water of life] you can create wood with a sawmill. With [USE 1 water~of~life] you can create 10 saplings using 10 wood. You can then immediately cut them with a sawmill, producing 20 wood.

## Smithy

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 5 stone, 5 wood, 2 iron, 200 Silver |
| Skill required:          | 3                                   |
| Maintenance per turn:    | 300 Silver, 1 wood                  |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- Units only need half the normal amount of iron to make iron weapons and armour. Laen is not saved.
- Units inside a smithy receive a +1 modifier to their weaponsmithing and armoursmithing skills.

## Stable

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 2 stone, 4 wood, 1 iron, 100 Silver |
| Skill required:          | 2                                   |
| Maintenance per turn:    | 150 Silver                          |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- Units inside a stable can reproduce horses by using the order [GROW] HORSES. For this the unit needs the skill Taming and at least 2 horses (in its possession).
- The chance to breed horses corresponds to the unit's skill. In addition, the unit has several attempts according to his skill. If a unit is T5, he has 5 attempts at 5% each to breed a horse.
- For each breeding attempt, the unit needs one horse. If not enough horses are available, the attempts are forfeited.

## Harbour

|                          |                                            |
|--------------------------|--------------------------------------------|
| Costs per point of size: | 5 stone, 5 wood, 250 Silver                |
| Total cost:              | 125 stone, 125 wood, 6250 Silver           |
| Skill required:          | 3                                          |
| Maintenance per turn:    | 250 Silver                                 |
| Maximum size:            | 25                                         |
| Capacity:                | persons according to size, unlimited ships |

- Allows ships larger than a boat to land in regions which are not plains or forests.
- A region with a harbour can be used as a "canal region", i.e., a ship in the harbour can sail away in any direction with an ocean.
- In both cases, the prerequisite is that the harbour owner is a member of the same faction or has [HELP GUARD] set to the captain's faction.
- The owner of the harbour receives 10% of all the silver earned through trade, in addition to the possible income through castles.
- The owner also receives (2 \* trade)% of all luxury items which are on board of incoming ships. Unless the unit which carries the goods has a hiding level higher than the harbour master's perception level or the ship's captain is allied with the harbour owner.
- In a region with a harbour, the prices of goods will increase with a probability of 20% instead of the normal 10%.
- A harbour will only work if it is completely built. There can be only one harbour per region. The one who finishes a harbour first is the winner. The half-finished harbour can be destroyed with the order [DESTROY].

## Academy

|                          |                                            |
|--------------------------|--------------------------------------------|
| Costs per point of size: | 5 stone, 5 wood, 1 iron, 500 Silver        |
| Total cost:              | 125 stone, 125 wood, 25 iron, 12500 Silver |
| Skill required:          | 3                                          |
| Maintenance per turn:    | 1000 Silver                                |
| Maximum size:            | 25                                         |
| Capacity:                | persons according to size                  |

- Units in an academy can learn with a chance of 1/3 once extra in this week, if they have a teacher even with a chance of 2/3.
- Learning in an academy costs 50 silver per person for skills which can be normally learned without any costs and the double amount of silver for skills which cost something to learn them.
- Teachers who teach pupils in an academy also get a chance to learn, which is up to 1/3 depending on the number of their pupils. They do not have to be in an academy themselves for this.
- An academy will only work if it is completely built!

## Mage Tower

|                          |                                                                    |
|--------------------------|--------------------------------------------------------------------|
| Costs per point of size: | 5 stone, 3 wood, 3 iron, 2 mallorn, 2 laen, 500 Silver             |
| Total cost:              | 250 stone, 150 wood, 150 iron, 100 mallorn, 100 laen, 25000 Silver |
| Skill required:          | 5                                                                  |
| Maintenance per turn:    | 1000 Silver                                                        |
| Maximum size:            | 50                                                                 |
| Capacity:                | 2 Persons                                                          |

- In a mage tower, a mage regenerates 75% more aura.
- The power of every spell casted inside a mage tower is increased as if the spell was cast one level higher.
- Fizzles happen much less often.
- The building itself has 40% extra magic resistance.
- A mage tower will only work if it is completely built!

## Caravanserai

|                          |                                         |
|--------------------------|-----------------------------------------|
| Costs per point of size: | 1 stone, 5 wood, 1 iron, 500 Silver     |
| Total cost:              | 10 stone, 50 wood, 10 iron, 5000 Silver |
| Skill required:          | 2                                       |
| Maintenance per turn:    | 3000 Silver, 2 horses                   |
| Maximum size:            | 10                                      |
| Capacity:                | persons according to size               |

- A caravanserai allows you to build roads in deserts. If the caravanserai is destroyed, half of the roads will also be destroyed. A completed road remains if the building maintenance is not paid.
- In deserts, double the possible trade volume. The owner receives a part of the trade as in (see [castle rules table]).
- A caravanserai will only work if it is completely built!

## Dam

|                          |                                            |
|--------------------------|--------------------------------------------|
| Costs per point of size: | 5 stone, 10 wood, 1 iron, 500 Silver       |
| Total cost:              | 250 stone, 500 wood, 50 iron, 25000 Silver |
| Skill required:          | 4                                          |
| Maintenance per turn:    | 1000 Silver, 3 wood                        |
| Maximum size:            | 50                                         |
| Capacity:                | persons according to size                  |

- Dam allows you to build roads in swamps. If the dam is destroyed, half of the roads will also be destroyed. A completed road remains if the building maintenance is not paid.
- Dam will only work if it is completely built!

## Tunnel

|                          |                                              |
|--------------------------|----------------------------------------------|
| Costs per point of size: | 10 stone, 5 wood, 1 iron, 300 Silver         |
| Total cost:              | 1000 stone, 500 wood, 100 iron, 30000 Silver |
| Skill required:          | 6                                            |
| Maintenance per turn:    | 100 Silver, 2 stone                          |
| Maximum size:            | 100                                          |
| Capacity:                | persons according to size                    |

- A tunnel allows you to build roads in glacier. If the tunnel is destroyed, half of the roads will also be destroyed. A completed road remains if the building maintenance is not paid.
- Tunnel will only work if it is completely built!

## Inn

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 4 stone, 3 wood, 1 iron, 200 Silver |
| Skill required:          | 2                                   |
| Maintenance per turn:    | 5 Silver per 1 size                 |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- Units in a Inn regenerate 50% faster.
- All persons inside an Inn need 14 silver per week to live instead of the normal 10 silver.

## Monument

|                          |                                     |
|--------------------------|-------------------------------------|
| Costs per point of size: | 1 stone, 1 wood, 1 iron, 400 Silver |
| Skill required:          | 4                                   |
| Maintenance per turn:    | none                                |
| Maximum size:            | none                                |
| Capacity:                | 1 person per 1 size                 |

- The name and the description of the monument can only be entered once. This can never be changed again.
- The monument has no functionality.

## Stonecircle

|                          |                     |
|--------------------------|---------------------|
| Costs per point of size: | 5 stone, 5 wood     |
| Total cost:              | 500 stone, 500 wood |
| Skill required:          | 2                   |
| Maintenance per turn:    | none                |
| Maximum size:            | 100                 |
| Capacity:                | 3 persons           |

- A stonecircle can be blessed by a [powerful spell]. This then develops some strange effects. Among other things, it seems to attract the extremely rare elf horses. In addition, magicians in the building can interrupt the connection between the astral space and the real world.
- In a blessed stonecircle, a mage regenerates 50% more aura.
- The power of any spell cast in a blessed stonecircle increases as if the spell had been cast with one more level.
- Occupants have 30% extra magic resistance.
- Stonecircle will only work if it is completely built and blessed!

## See also

- [Buildings]
- [Castles]
- [Production]

Continue reading: [Faction Pool].

[building castles]: ./castles.md "Burgen"
[Lighthouse]: #lighthouse
[Mine]: #mine
[Quarry]: #quarry
[Sawmill]: #sawmill
[Smithy]: #smithy
[Stable]: #stable
[Harbour]: #harbour
[Caravanserai]: #caravanserai
[Academy]: #academy
[Mage Tower]: #mage-tower
[Dam]: #dam
[Tunnel]: #tunnel
[Inn]: #inn
[Monument]: #monument
[Stonecircle]: #stonecircle
[water of life]: ./alchemy.md "Tränke"
[USE 1 water~of~life]: ./cmd-use.md "USE"
[GROW]: ./cmd-grow.md "GROW"
[HELP GUARD]: ./cmd-help.md "HELP"
[DESTROY]: ./cmd-destroy.md "DESTROY"
[castle rules table]: ./castles.md#overview "Burgen"
[powerful spell]: ./spells-descriptions.md#segne-steinkreis "Zauberbeschreibungen E2"
[Buildings]: ./buildings.md "Gebäude"
[Castles]: ./castles.md "Burgen"
[Production]: ./production.md "Produktion"
[Faction Pool]: ./faction-pool.md "Parteipool"
[MAKE "building type"]: ./cmd-make.md "MAKE"
