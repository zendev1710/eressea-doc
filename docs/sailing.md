---
# cSpell:locale en
alias: sailing
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD041 MD042 MD052 -->

[](){ #sailing-id }

# Sailing

You can leave your island only with [ships][ships-id] and, for example, open up new markets or establish direct contact with other factions.
With a ship it is possible to move up to 7 regions, even more than 7 regions with the help of aquarians or with magic.

All ships larger than a boat (including longboats) can only dock in plains and forests.
All other types of region (e.g. mountains, highlands, swamps, etc.) require an [Harbour][harbour] for ships to dock.
If a ship tries to dock in an unsuitable region, it suffers [damages][damage-to-ships].
However, ships can set sail from anywhere, so you can build ships in any coastal region and launch them.

Ships cannot pass directly from one coast to a neighbouring coastal region without first sailing on an ocean region.
Similarly, they can't leave in all directions, but only in the direction from which they came and in neighbouring directions.
A ship coming from the east (report indicates then "coast east") can thus leave towards the east, the north-east and the south-east.
However, if a region has a harbour, the ships of the owner of the harbour and of friendly factions (see [[cmd-help]]) can go in any directions as long as they are oceanic regions.

On the high seas - i.e. ocean areas that are not bordered by a land region - ships can drift into a neighbouring area and suffer damage due to storms.
This does not apply to ships ordering [[cmd-follow]] or [[cmd-piracy]].

To be able to sail a ship, you need a trained crew, i.e. units that have learnt the skill of sailing.
In the following table, the sailing skill level of the captain (the first unit on the ship in the report) is indicated under "Captain".
In addition, a certain overall level of sailing is required to pilot the ship.
To achieve this, the sailing skill levels of all the persons on board are added together, including those of the captain's unit and units from "foreign" factions.
The required value is shown in the table under "Crew".
The range indicated in the table is valid per turn, i.e. a ship can sail a maximum of this distance per turn.
Ships piloted by a unit of aquarians from an aquarian faction (migrant aquarians from a human faction do not count) can sail one extra hex.

**Example:**

- A trireme can be piloted by a unit of 30 persons with sailing 4 or by a unit of one person with sailing 4 and a unit of 58 persons with sailing 2.
  In all cases, it sails over 7 regions per turn (8 for Aquarians) and can carry 2000 lbs, from which the weight of the crew is of course deducted.
- A dragonship with a level 2 unit of 25 persons moves 5 regions.
  However, with 3 level 20 persons, it can move 7 regions.

| Type       | Range | Capacity | Captain / Crew | Shipcraft lvl | Qty of wood |
|------------|:-----:|---------:|---------------:|:-------------:|------------:|
| Boat       |     2 |       50 |        1 /   2 |       1       |           5 |
| Longboat   |     3 |      500 |        1 /  10 |       1       |          50 |
| Dragonship | 5[^1] |     1000 |        2 /  50 |       2       |         100 |
| Caravel    |     5 |     3000 |        3 /  30 |       3       |         250 |
| Trireme    |     7 |     2000 |        4 / 120 |       4       |         200 |
| Galleon    |     5 |    20000 |    5 / 250[^2] |       5       |        2000 |

[^1]: Dragonship range depends on captain skill.
[^2]: When calculating the Galleons crews total skill, only min. T2 crews are counting.

Dragonship Range.

| Captain | 2 | 6 | 18 | 54 | 162 |
|---------|:-:|:-:|:--:|:--:|:---:|
| Range   | 5 | 6 | 7  | 8  |  9  |

If a ship does not have a sufficient crew, it cannot set sail.
If this happens at sea (for example due to combat or units starving for lack of money), it drifts until it reaches a coastal region.
It then suffers [damages][damage-to-ships] every turn, so that it quickly sinks.

The total weight of all units on a ship, including the weight of horses, carts, persons and of course all goods and silver of the units, must be able to be transported by the ship.
If this is not the case, or is no longer the case, the ship cannot sail.
At sea, it will not sink immediately, but will drift.
Ships capacities are shown in the table above and are always displayed in the report.
The weights of items can be found in the section on [[items]] and those of persons of different races, in the table [Weights and Capacities][travel-by-land-or-by-sea].

It is possible to group together several ships in a [convoy][convoy-id].
Details are described in the chapter on [ships][ships-id].

Units aboard a ship cannot execute long orders (with the exception of aquarians).
Only the captain can give [[cmd-move]] or [[cmd-route]] orders to navigate the ship.
Up to 100 aquarians per ocean region can earn 10 silver each per turn with the [[cmd-work]] order.
Nevertheless, all persons on the ship need the weekly upkeep, so it should always have enough silver on board.

When the ship is ashore, all the units on board can do something; they go ashore to work, so to speak.
They can do this even if the ship leaves during the same turn.
However, if the region is guarded by a non-allied faction, they cannot [earn silver][money] with WORK, ENTERTAIN or SELL.

If units want to leave a ship, they must first do so with [[cmd-leave]].
If the region is not guarded by a non-allied faction, the units can move immediately with MOVE, otherwise they can only MOVE on the turn following the LEAVE order.
This also applies to [[cmd-ride]] and [[cmd-carry]].

## Swimming

[Aquarians][aquarians] in a ship can swim from an ocean region onto a directly adjacent land region (with the MOVE order), but the reverse is not true.
Aquarians can not swim from a land region onto any ocean region.
This works only if the unit isn’t overloaded.
Swimming aquarians can carry items, but not horses.
[transporting][cmd-carry] units of other races is not possible in this way, but aquarians can transport each other.
This movement takes place before the movement of ships, so a ship can drop off units and then move on.
[[cmd-leave]] is not necessary when swimming from a ship, but is not even a mistake.

## Damage to Ships

Travelling by sea is dangerous, and ships can be damaged on the high seas by storms, natural events or even creatures from the depths (or also if no one drives them).

Damage is expressed as a percentage and reduces capacity in proportion to the damage indicated; round down.
Range, including all acceleration bonuses (aquarian, artefacts, spells), is also reduced in proportion; but in this case, always round up.

Example: A boat with an aquarian captain is 17% damaged.

- This reduces the capacity to (50)\*0.83=41.5 (round down) 41 WU.
- The range (1+2)\*0.83=2.49 (round up) therefore remains at 3.

If the damage exceeds 100%, the ship will sink with all units on board.

The following events will damage a ship :

- The ship was involved in a fight : 0%-20% damage (see [Battle on ship][combat-on-and-with-ships])
- The ship was harmed by a spell, up to 90% damage.
- A tidal wave damages the ship, 50% damage.
- if the ship hits reefs, it suffers 10% damage (hitting reefs: attempting to dock in an unsuitable region)
- A ship at sea without enough sailors, 30% damage per round.
- The ship does not have any owner, 5% damage per round
- The ship is hit by a storm and drifts off course, 2% damage

You can repair a ship with [`MAKE`&nbsp;&#91;`level`&#93;&nbsp;`SHIP`&nbsp;&#91;`ship id`&#93;][cmd-make], just as if the ship wasn't finished yet.

Player experience: Ship drifted in a storm; what happened?  

Ships travel over coasts (ocean hexes with at least one adjacent land hex) or over open sea (ocean with only adjacent water hexes).

- As long as a ship only travels in coastal regions it will never get caught in a storm and it will never drift away.
- If a ship is crossing open sea hexes (this is independent of the start and destination region), it may get caught in a storm and drift away.
  It is then pushed to the side (random) and then carries out the remaining movements.
- If a ship drifts away, it always suffers 2% damage without exception.

## See also

- [movement][travel]
- [Ships][ships-id]

Continue reading: [Production][production-id].

<!-- From [https://wiki.eressea.de/index.php?title=Schiffsreise/en&oldid=15812] -->
