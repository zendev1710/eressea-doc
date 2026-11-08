---
# cSpell:locale en
alias: cmd-sort
---

# `SORT`

**`SORT`**` BEFORE `*`unit-id`*  
**`SORT`**` AFTER `*`unit-id`*  

This order modifies the order of your units **in the report** and the [orders evaluation][orders].  
This allows, for example, the display of *students* (units executing the `LEARN` order) and *teachers* (units executing the `TEACH` order) one below the other.  

!!! info
    The sorting order of units [has an impact][escaping-death-by-starvation] in case of famine

The following limitations apply:

- *`unit-id`* must be a separate unit from the one executing the order
- Both units involved in the order must be either in the same building or ship, or both outside
- It is not possible to place a unit in front of a building owner or ship captain. Use the [`GIVE`*`unit-id`*`COMMAND`] order for this purpose
- A building owner or ship captain cannot use this order

Sorting takes place at the very end of the round, after movement.  
Thus, units that entered a region using [`MOVE`][cmd-move] or [`RIDE`][cmd-ride] can be sorted immediately.  

[cmd-move]: [[cmd-move]]
[cmd-ride]: [[cmd-ride]]
