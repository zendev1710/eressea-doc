---
# cSpell:locale en
alias: cmd-leave
---
# LEAVE

**`LEAVE`**  

The unit will abandon the ship or the building in which it is located.
If you use the [[cmd-enter]] or [[cmd-move]] orders, the units will sometimes automatically leave their ships and buildings.
However, this doesn't always work: if the unit is the captain of a ship and uses MOVE, it will attempt to sail in that direction, even if there is land there.
Captains must first 'LEAVE' their ship, but all other sailors can use 'MOVE' to move over land and automatically leave the ship.

If a unit leaves a building or a ship over which it has command, this does not necessarily pass to the following unit in the report.
Here you should use [[cmd-give|`GIVE unit-id COMMAND`]] let the handover of command take place in a controlled manner.
The order of the units during the evaluation is not always that of the report.
If your own units are in the building or on the ship, the order falls to them.

If the unit is on a ship and the region is guarded by a non-allied faction, it must first leave the ship if it wants to carry out certain actions.
For more information, see [[cmd-guard]].
The leave order does not work on the open sea.
One way to still let people jump overboard is "Give 0[number]People".
Another Aquarian-only solution that doesn't kill people is [swimming].

<!-- From [https://wiki.eressea.de/index.php?title=LEAVE&oldid=15184] -->

[swimming]: ./sailing.md#swimming
