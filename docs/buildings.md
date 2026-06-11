---
# cSpell:locale en
alias: buildings
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Buildings

There are a number of different buildings in Eressea that offer different benefits. Apart from castles and monuments, all buildings have a recurring maintenance cost to keep them running.

## Maintenance

These maintenance costs are generally independent of the size of the building and must be paid at the start of the turn by the building owner, between the [[cmd-give]] order and long orders (see [[orders-sequence]]).
So a unit cannot collect taxes and then pay for its maintenance with the money collected.
If there is no money at the time, the building does not function.

Maintenance is due in full as soon as the building is built; but not in the turn it is started with the [`MAKE`` `*`building type`*][cmd-make] order.
The consequence of this is that buildings that are completed in a single turn do not function during the construction week, as no maintenance was paid for at the start of the week.

If there is a shortage of Silver, or if a certain building is not used during a week and you wish to save on its maintenance, the unit controlling the building (see next section) can ensure that maintenance is not paid for that turn by using the order [`PAY NOT`][cmd-pay-not].
The building then, of course, has no use during that week.

## Units and buildings

All the units inside a building are listed underneath.
The first unit has command of the building; it is the owner.
It determines which other units can enter the building, and it can rename and describe the building.
The unit that owns the largest castle in a region can even rename and describe the region it rules.

The effect of buildings (including castles) is counted on a unit-by-unit basis.
Units that no longer fit - even partially - into the free capacity do not receive a bonus from the building - even if they are the only unit!

If there are several units in a building, they are interrogated in order, from top to bottom. The first unit that is too big "locks" the building for those that follow, even if the following units could get in if the big one wasn't there. The [[cmd-sort]] order can be used to remedy this situation.

## Building

Buildings are constructed and expanded using the [`MAKE`` `*`building type`*][cmd-make] order.
As with other production orders, the construction output depends on the skill (masonry), size of the builder unit and the minimum skill required.
A unit can build ( skill level x persons / minimum skill) size points per round, so you can easily build a tower in a week with a sufficiently skilled unit and enough stones.

## See also

- [[castles]]
- [special buildings][other-buildings]
- [Production][production-id]
- [expenses][expenses]

Continue reading: [[castles]].

<!-- From [https://wiki.eressea.de/index.php?title=Gebäude/en&oldid=16677] -->
