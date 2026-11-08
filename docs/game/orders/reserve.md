---
# cSpell:locale en
alias: cmd-reserve
---
# `RESERVE`

**`RESERVE`**` `*`number`*` `*`Item`*  
**`RESERVE`**` ALL `*`Item`*  
**`RESERVE`**` EACH `*`number`*` `*`Item`*  

This allows a unit to take and “save” items or silver from other units in the region.  
It should be noted that the unit takes its goods from any unit (usually from top to bottom according to the order in the NR), unless this unit has reserved this item (see [[items-pool]]!).  

With `RESERVE ALL`` `*`Item`*, a unit reserves everything it owns from the specified item.  

With `RESERVE EACH`` `*`number`*` `*`Item`*, *`number`* items **per person** are reserved.  

```text
RESERVE EACH 100 Silver
```

reserved for a unit with 10 people i.e. 1000 Silver.  

## Sources of error

- `TEMP` unit cannot reserve! Silver like items must be given to them using [`GIVE`][cmd-give]
- `RESERVE` occurs before [`GIVE`][cmd-give] and [`RECRUIT`][cmd-recruit] in the [[orders-sequence]]. So related `EACH` apply on the number of people **before** handover and recruitment
- If a faction's units reserve more of an item than is available in the region (in the material pool) as a whole, the outcome is difficult to predict. For further details see [[items-pool]]
- If the same item is reserved by a unit several times, only the last entry is valid

## Examples

With:

```text
RESERVE EACH 1 Sword
RESERVE EACH 1 Shield
GIVE depo ALL
```

A unit can keep one weapon and one shield per person, even after a losing battle, and give everything else (loot) to a depot unit.  

With:

```text
@RESERVE 100 Silver
RESERVE 1 Sword
RESERVE 50 Silver
```

The unit will reserve a sword and 50 silver.  

## See also

- [[items-pool]]
- [`GIVE`][cmd-give]

<!-- From [https://wiki.eressea.de/index.php?title=RESERVE&oldid=14809] -->

[cmd-give]: [[cmd-give]]
[cmd-recruit]: [[cmd-recruit]]
