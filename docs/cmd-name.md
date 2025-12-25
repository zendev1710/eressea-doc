---
# cSpell:locale en
alias: cmd-name
---
# NAME

**`NAME UNIT`**` `*`"name"`*  
**`NAME STRANGERS UNIT`**` `*`unit-id "name"`*  
**`NAME FACTION`**` `* `"name"`*  
**`NAME STRANGERS FACTION`**` `*`faction-id "name"`*  
**`NAME BUILDIN?G`**` `*`"name"`*  
**`NAME STRANGERS GEBÄUDE`**` `*`building-id "name"`*  
**`NAME SHIP`**` `*`"name"`*  
**`NAME STRANGERS SHIP`**` `*`ship-id "name"`*  
**`NAME REGION`**` `*`"name"`*  
**`NAME GROUP`**` `*`"name"`*  

Rename the listed item.
Ships and buildings can only be renamed if the unit also has command of the building or ship - so it must be the first unit under the building or ship in the evaluation.
A region can only be renamed by the lord of the most powerful castle in a region.
Groups can only be renamed by group members and the new group name cannot already exist.

The new name can be up to 127 characters long. Longer descriptions can be added using the [[cmd-describe]] command.

Through the addition `STRANGERS` (or `STRANGER`) and specifying the number, you can name units, ships and even buildings (not just castles) of other parties if they do not yet have a name (i.e. units are named as "unit abc").
You can even name a foreign faction as long as it is older than ten rounds.

The naming of the faction must also be carried out by a unit.

```text
ERESSEA 7 "Seven"
    NAME FACTION "Incorrect" ; no effect
    UNIT 89
        NAME FACTION "Correct"
```

<!-- From [https://wiki.eressea.de/index.php?title=NAME&oldid=16968] -->
