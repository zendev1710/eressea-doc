---
# cSpell:locale en
alias: castles
---

# Castles

Castles increase the peasants' income, enable trade luxury goods and, finally, offer their occupants protection in the event of an attack.  
They also reduce the likelihood of [[plague]].

Castles are built from stone using the [MAKE CASTLE][cmd-make] order and the [masonry][masonry] skill.  
The size at which a castle enters a new category is shown in the table below:

| Size |     1      |     2     |      10       |  50   |    250     |   1250   |  6250+  |
|:----:|:----------:|:---------:|:-------------:|:-----:|:----------:|:--------:|:-------:|
| Type | Foundation | Tradepost | Fortification | Tower | Stronghold | Fortress | Citadel |

The larger the castle, the more difficult it is to expand it further.  
To continue building a castle, you need the masonry skill at the required level.  
Each week, the unit will extend the building by (total skill) / (skill level required) using the same amount of stones.  
You can easily build a tower in a week with a sufficiently large and skilled unit and enough stones.  

Castles also have numbers (IDs), which are used for orders.  

Here is a first example of a castle:

```text
Large Temple of the Golden-Eyed Cat (58), size 58, tower;
The temple shines white in the sun, framed by the delicate green of the park's trees.
The slender tower, which rises high above the city, can be seen from afar.
To the north of the temple, the city of Xontormia stretches along the Whyren, which is spanned by a gigantic, long bridge near the harbour.
```

Units in a castle are protected by its walls, namely one person is protected per size unit of the castle.  
Only the protected persons benefit from the bonus that a castle gives its occupants in the event of a raid (for more information, see the [[war]] chapter, in particular the list of [bonuses and penalties][bonuses-and-mali]).  
Each size unit of the castle requires a stone.  

A larger castle improves the population's income: all workers and peasants receive a bonus when they work, which depends on the size of the largest castle in a region (see also the [summary table][castles-overview-id]), and the owner of the largest castle receives a share of the profit when other players sell trade goods.  

## Foundation

## Tradepost

## Fortification

## Tower

## Stronghold

## Fortress

## Citadel

## Examples

The unit "Thor's Builders" has 20 persons with masonry level 1 and 100 stones.  
Due to its skill level and the number of people in the unit, it has 20 production points (PP).  
It allows it to increase a castle's size by a number dependent on the required level for the castle.  

When this unit starts to build a new castle, it can build 10 size units on the first turn: for the foundations and the tradepost, the required level in masonry is 1;  
to build 1 size unit, 1 production point is required, so the unit first builds the tradepost up to size 10, which makes this building a fortification.  
There are then 10 production points left, but they are lost because the minimum masonry level required for fortifications is 2.  

If the unit has a level 2 in masonry, it starts with 40 skill points; 10 are needed for the fortification.  
It will then use the remaining 30 points to improve the fortification in the same turn.  
However, a minimum skill of 2 also means that 2 production points must be spent per stone.  
So, the fortification is increased by 15 stones and a size 25 fortification will have been built at the end of the week.  

With skill level 2, builders will, in 2 additional weeks, enlarge the fortification to size 50, creating a tower.  
They will not be able to enlarge the tower, though, due to the new required minimum level of 3.  

[](){ #castles-overview-id }

## Overview

Building castles - building material, minimum Masonry skill level, wage bonus (in silvers), trade share and defense bonus.  

| Type          | Lvl | Wage bonus | Trade share | Def. bonus |
|---------------|----:|-----------:|------------:|-----------:|
| Foundation    |   1 |         -- |          -- |          0 |
| Tradepost     |   1 |         -- |          6% |          0 |
| Fortification |   2 |   1 silver |         12% |         +1 |
| Tower         |   3 |   2 silver |         18% |         +2 |
| Stronghold    |   4 |   3 silver |         24% |         +3 |
| Fortress      |   5 |   4 silver |         30% |         +4 |
| Citadel       |   6 |   5 silver |         36% |         +5 |

## See also

- [[other-buildings]]
- [[buildings]]
- [Bonuses and penalties][bonuses-and-mali]
- [Income][income]

Continue reading: [[other-buildings]].

<!-- From [https://wiki.eressea.de/index.php?title=Burg/en&oldid=14408] -->

[cmd-make]: [[cmd-make]]
