---
alias:
	name: cmd-sort
	text: SORT
---
# SORT

**`SORT`**` BEFORE `*`unit-id`*  
**`SORT`**` AFTER `*`unit-id`*

This order modifies the order of your units **in the report** and the [Zugvorlage].
This allows, for example, the display of *students* (units executing the `LEARN` order) and *teachers* (units executing the `TEACH` order) one below the other.

!!! info
    The sorting order of units [has an impact] in case of famine

The following limitations apply:

- *`unit-id`* must be a separate unit from the one executing the order
- Both units involved in the order must be either in the same building or ship, or both outside
- It is not possible to place a unit in front of a building owner or ship captain. Use the [`GIVE `*`unit-id`*` COMMAND`] order for this purpose
- A building owner or ship captain cannot use this order

Sorting takes place at the very end of the round, after movement.
Thus, units that entered a region using [MOVE] or [RIDE] can be sorted immediately.

[Zugvorlage]: ./commands.md "Orders"
[`GIVE `*`unit-id`*` COMMAND`]: ./cmd-give.md "GIVE"
[MOVE]: ./cmd-move.md "MOVE"
[RIDE]: ./cmd-ride.md "RIDE"
[has an impact]: ./tips-and-tricks#
