---
# cSpell:locale en
alias: cmd-give
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# GIVE

` `**`GIVE`**` `*`unit_ID amount item`*  
**`GIVE`**` `*`unit_ID`*` EACH `*`amount`*` `*`item`*  
**`GIVE`**` `*`unit_ID`*`ALL`  
**`GIVE`**` `*`unit_ID`*` ALL `*`item`*  
**`GIVE`**` `*`unit_ID`*`HERBS`  
**`GIVE`**` `*`unit_ID amount`*`MEN`  
**`GIVE`**` `*`unit_ID`*`ALL MEN`  
**`GIVE`**` `*`unit_ID`*`UNIT`  
**`GIVE`**` `*`unit_ID`*`KOMMANDO`  
**`GIVE`**` `*`unit_ID amount SHIP`*  
**`GIVE`**` 0 `*`amount item`*  
**`GIVE`**` 0 `*`amount`*`MEN`  
**`GIVE`**` 0 `*`amount`*`SHIP`  

The unit transfers items, command of ships or buildings, persons, ships or even itself to other units.

## Items

With `GIVE` units can give all the goods they own to other units.
The condition is that the indicated unit accepts things.  
This is the case if it belongs to the same faction or an allied faction (`HELP GIVE`), or if it has given this turn the [[cmd-contact]] order for the giving unit.  
Monster units and certain player units with monster races also accept nothing.  
Those who simply want to throw away objects can also give them to peasants or throw them into the ocean (`GIVE 0 "amount" "item"'`).  
Persons, Silver and horses respectively increase the supply of peasants, Silver and horses in a (land) region.  
All other items disappear.  

The sending and receiving units must, of course, be in the same region.
The transfer also works on the high seas, between ships and from ships to shore and vice versa.  

Instead of a number you can also use the parameter `ALL`.  
`GIVE`*`unit-id`*`ALL Swords`, for example, hand over all the swords that the unit has at the time.  
`GIVE`*`unit-id`*`ALL` hands over all items, herbs, potions and silver, but not the people in the unit.  
With`GIVE`*`unit-id`*`herb` all herbs that the unit has are handed over.  

When you explicitly give the `GIVE`*`unit-id`*`ALL MEN` order, all people are handed over and the unit is dissolved.  

!!! warning "Caution"
    All items and silver that come with `GIVE` have been handed over, are automatically reserved and can no longer be passed on from the material pool!  
    Also `GIVE` uses the [[items-pool]], except in the context of `GIVE ALL`, where the unit only gives its own, unreserved items.

The variant `GIVE xyz EACH` hands over *number* items per person in the target unit.
For example, if the unit xyz has 10 people, with `GIVE xyz EACH 20 Silver` order, it transfers her 200 Silver.

!!! tip
    With `@GIVE` you can set up automatic transfers.  
    For example, a unit with `@GIVE abc ALL Iron` hand over all the iron to the *abc* unit every week.

```text
GIVE k3f 300 Silver
; Gives the unit k3f 300 Silver.

GIVE 0 5 Stone
; Discard 5 stones.

GIVE TEMP 3 7 MEN
; Gives 7 people to the newly created unit TEMP 3.
```

!!! warning "Caution"
    Between `MAKE TEMP` and `END` there are orders for the new unit - and it has no money.

So the following **doesn't work**:

```text
MAKE TEMP 1
    GIVE TEMP 1 200 Silver  ;  Pointless!
    RECRUIT 2
    MOVE WEST
END
```

Instead, it needs to be written like this:

```text
GIVE TEMP 1 200 Silver
MAKE TEMP 1
    RECRUIT 2
    MOVE WEST
END
; GIVE TEMP 1 200 Silver  ;  or here!
```

## People and units

If you want to bring people from different units together, this is done with `GIVE`*`unit-id`*`anzahl MEN`.  
**The [[skills]] are then mixed up**, and you **shouldn't forget the items**, as they may go to the farmers if the unit runs out of people.

Player experience (Solthar):

If you want to hand over people to a unit of another faction, a simple [[cmd-help|`HELP GIVE`]] is not enough!  
The receiving unit must [[cmd-contact]] the transferring unit.  
In addition, if the receiving unit is a [migrant unit][humans], it must not have any people at the time of transfer.
Ideally it should be an empty TEMP unit.
Example:

```text
UNIT a; Faction X
    GIVE TEMP x ALL MEN
UNIT b; Faction Y
    MAKE TEMP x
        CONTACT UNIT a
    END
```
<!-- TODO clarify -->
With `GIVE`*`unit-id`*`UNIT` the complete unit with all items is given to another faciton, i.e. it switches to the faction of the recipient unit and is not added to the recipient unit!  
The unit does not carry out any further orders during the turn!  

## Command

If the unit also has a ship or building under its command - i.e. if it is the first listed unit in the ship or building - it can also pass command to another unit.  
The unit in command determines which other units are allowed to enter the ship or building.  

`GIVE unit COMMAND` should always be used, even if the unit with the command leaves the ship or building and the following unit is to receive the command.  
The order of the units during the evaluation is not always that of the report.  
New owners of a building are placed in the first position in the building at the end of the round and may therefore only benefit from the building in the following round (e.g. mining bonus).  
The command cannot be given to units without people (e.g. after a battle, or to "empty" `TEMP` units).

## Convoy

With `GIVE`*`unit-id`*` `*`number`*`SHIP` the owner of a ship or [convoy][convoy] hands over the number of ships.  
The transferring and receiving units must belong to the same faction; `HELP ALL` or `CONTACT` is not sufficient.  
If the other unit also owns a ship, a [convoy][convoy] is formed.  
Convoys always consist of ships of the same type.  
Boats cannot form convoys and the ships must be on the same coast.  

## See also

- [[cmd-reserve]]
- [[items-pool]]
- [[ships]]
- [[buildings]]

<!-- From [https://wiki.eressea.de/index.php?title=GIVE/en&oldid=15995] -->
