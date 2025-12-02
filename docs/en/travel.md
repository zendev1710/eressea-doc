# Movement

There are several modes of movement in Eressea: Walking, riding on horses, or sailing over oceans on ships. Sometimes you may even fly or swim. For alle modes the orders [`MOVE`] or [`ROUTE`] are used.

## Travel: By land or by sea

On land, it is possible to travel a distance of one region, so a unit can more from one region to the next. If the unit has enough horses and the Riding skill, it can travel one region further. If the regions are connected by road, it is possible to move up to two regions on foot or even up to three regions on horseback.

Movement is only possible in six directions: northeast, northwest, east, west, southeast and southwest. It is not possible to move straight north or south.

The order [`CARRY`]` `*`passenger-unit`* allows units to transport other units while moving. The unit that is to be carried must have the order [`RIDE`]` `*`transporting-unit`*. Units that do not have the riding skill can still be transported along on horses or carts with this combination of orders. Of course, the carrying units must have enough capacity for the passengers and their equipment. Using [`FOLLOW`]` UNIT `*`followee`* oder `FOLLOW SHIP`*`followed-ship`* is mostly equivalent to the unit using the MOVE command itself, if the the followed unit also has a movement command. The followers must carry their own weight.

Travelling units may be stopped from passing through a region by guarding units (siehe [GUARD]).

If the cargo (including any passengers) is too heavy for a unit or ship, it cannot move. The total weight of the transported units and their goods and equipment, including silver, is checked against the carrying capacity (check [this table] to find out the weight of items).

TODO: Katapulte

Weights and Capacities

|                        |        |          |
|------------------------|--------|----------|
|                        | Weight | Capacity |
| trolls                 | 20     | 10,8     |
| goblins                | 6      | 4,4      |
| all other player races | 10     | 5,4      |
| horse                  | 50     | 20       |
| cart                   | 40     | 100      |
| boat                   | \-/-   | 50       |
| longboat               | \-/-   | 500      |
| dragonship             | \-/-   | 1000     |
| caravel                | \-/-   | 3000     |
| trireme                | \-/-   | 2000     |
| galleon                | \-/-   | 20000    |

## Roads

The speed of travel can be enhanced by building [roads]. If all regions that are passed through have the appropriate road network, you can travel one region further. If, for example, a unit wants to walk two regions to the east, it needs to start in a region with a (completed) road towards the east. In addition, the middle region needs to have roads to the east and west, and the destination needs to have a road to the west - all of which must be completed, too.

## Horse and Carriage

The **movement speed** on foot without [road][roads] is one region per turn; with a road, it's two. On horseback, you can move two regions without a road, and three regions with roads. A skill level 2 per 2 horses is required to ride. The unit rides automatically if it has enough riding levels for all the horses it owns and if the unit is not overloaded. If the unit is too heavily laden to ride, but not too heavily laden to move on foot, the unit moves through a single region (without roads). The unit is considered to be leading the horses by the bridle.

**Horses'** have a capacity of 20 WU/GE.

Carts have a capacity of 100 GE/WU. They must be pulled by 2 horses (per cart). But carts can also be transported as freight, for example on a boat or if the unit does not have enough horses with it; they have a weight of 40 UW/GE.

Four trolls can also pull a cart without horses, but only to one region. Only trolls can use cart without horses.

**On foot**, each person (even without riding skills) can lead a horse through a region. In addition, each person can lead four horses per riding skill level (a person with riding 1 can therefore lead a total of 5 horses). If the trolls transport both horses and carts, the horses have priority over the carts.

**On horseback**, each person may have two horses per riding level. It should be noted that the weight of the riders must be deducted from the capacity of the horses.

If it has too many horses, the unit can no longer move.

If a unit has several horses and carts, their transport capacity is simply added together. For example, 7 stones can be transported on 3 carts, whereas only one stone can be transported on a single cart.

**Examples** (we are assuming here that there are no roads)

- A 4-person unit with riding 1 can carry a maximum of 20 horses (4 horses anyway, plus 4 \* 4 horses with riding 1) on foot. If it has no more than 8 horses with it and is not too heavy, it can move two hexes.
- If the same unit only carries 8 horses and 2 carts, it has a mounted capacity of 320GE (2 \* 100GE for carts + 8 \* 20GE for horses −4 \* 10GE for riders). The exceptions to this rule are races with a different weight, where the rider's actual weight is of course deducted.
- A unit of 5 dwarves with no riding skills can lead 5 horses through a region carrying 127GE (5.4GE per dwarf and 20GE per horse).
- If the same unit also has 3 carts, it can transport 287GE of other goods (5.4GE per dwarf, 20GE per horse and 2 \* 100GE for the carts being pulled minus 40GE for the cart to be transported, as 5 horses are only enough for 2 carts).
- A unit of 4 trolls with no riding skills and no horses can pull a cart over one region (two regions with roads) and transport 143.2GE (10.8GE per troll and 100GE on the cart).
- A unit of 4 trolls without riding skills can pull 4 horses and 3 carts (two behind the horses and one behind the 4 trolls) over a region, carrying 423.2GE (10.8GE per troll, 300GE on the cart and 20GE on each of the 4 horses).
- A unit of 4 trolls with riding 1 with 4 horses and two carts can move one region with 323.2GE (10.8GE per troll, 20GE per horse and 100GE per cart) or move two regions with 200GE (20GE per horse, 100GE per cart minus 80GE for the 4 trolls).
- A unit with riding 1, a cart and two horses can move 130 swords over two regions (the rider weighs 10 and must be deducted from the capacity when sitting on the cart). A unit with riding 1 and 4 people could move 20 horses and 10 carts over one region and 8 horses and four carts over two regions.
- If an empty cart with two horses is to be transported on a ship, the ship must have a free capacity of 140GE (40GE for the cart and 2 \* 50GE for the horses).

## See also

- [Ships]
- [Roads]

|                   |                |
|-------------------|----------------|
| Continue reading: | [Ship Voyages] |

[Ship Voyages]: ./travel.md "Schiffsreise"

<!-- From [https://wiki.eressea.de/index.php?title=Reisen/en&oldid=16637] -->

[`MOVE`]: ./cmd-move.md "MOVE"
[`ROUTE`]: ./cmd-route.md "ROUTE"
[`CARRY`]: ./cmd-carry.md "CARRY"
[`RIDE`]: ./cmd-ride.md "RIDE"
[`FOLLOW`]: ./cmd-follow.md "FOLLOW"
[GUARD]: ./cmd-guard.md "GUARD"
[this table]: ./items.md "Waren"
[roads]: ./roads.md "Straße"
[Ships]: ./ships.md "Schiff"
