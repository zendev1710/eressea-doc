---
# cSpell:locale en
alias: cmd-combat
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# COMBAT

**`COMBAT`**`FRONT`  
**`COMBAT`**`AGGRESSIVE`  
**`COMBAT`**`REAR`  
**`COMBAT`**`DEFENSIVE`  
**`COMBAT`**`NOT`  
**`COMBAT`**`FLEE`  
**`COMBAT`**`HELP [NOT]`  

This order determines the reaction of a unit in the event of a battle (see also the section [Battle lines][combat-rows] in the chapter [[war]]).  

## `COMBAT AGGRESSIVE`

In combat, the unit is at the front and will never flee, but will fight to the death.  
This is used to advantage when the last bit of offensive power really counts.  

## `COMBAT FRONT`

In battle, the unit is at the front.  

It will attempt to flee when it has less than or equal to 20% of its hit points.  
This is used with advantage for good swordsmen.  
Can also come with `COMBAT` be set.  

## `COMBAT REAR`

The unit fights in the second row.  
If the front is wiped out, these units will still be drawn into the melee! This is used with advantage for shooters.  
The unit attempts to flee when it has less than or equal to 20% of its hit points.  

## `COMBAT DEFENSIV`

Like `COMBAT REAR`, but the unit will flee if it still has 90% of its hit points.  
This is used with advantage for magicians.  

## `COMBAT NOT`

The unit only takes part in the fight if it is the target of an enemy [[cmd-attack]] command.  
This is used to advantage for units that stay out of combat but are not supposed to flee, e.g. to occupy a building.  
The unit attempts to flee when it still has 90% of its hit points.  

## `COMBAT FLEE`

If a unit that is ready to [flee][fleeing] is involved in combat, it will attempt to flee before each round of combat.  
<!-- TODO: find escape section and combat chapter -->
For more information about "escape behavior", see the [Escape] section in the Combat chapter.  

This combat status is used to advantage for almost all "civilians".  
If even one person in a unit successfully escapes from a fight, they automatically leave buildings or land-based ships in which they are located.  
It is therefore important to consider whether this status makes sense for building (or ship) occupants.  

Units with this combat status also cannot [attack][cmd-attack] or [guard][cmd-guard].  
If a guarding unit places `COMBAT FLEE`, the guarding is immediately canceled, with corresponding consequences.  
Units with the combat status can still move after combat (with [[cmd-move]], [[cmd-route]], [[cmd-follow]]).  

!!! warning "Caution"
    Units with `COMBAT FLEE` or `COMBAT NOT` will fight if they are attacked and the first two rows are overrun.  
    That means magicians also do magic.  
    Pre-and post-combat spells are (currently) cast even if the front lines are not overrun.  
    If you want to prevent this, you can deactivate the [combat spell status][cmd-combatspell].  

Operating [catapults][weapon-catapult-id] is a task that requires a lot of preparation, so a unit with the combat status `COMBAT NOT` or `COMBAT FLEE` will not fire ammunition, but will use any other weapon if it has one with it and knows how to use it.  

!!! warning "Caution"
    People with low hit points who have not set `COMBAT FLEE` will only flee if they have taken a hit in combat.  
    Hits whose damage points were completely stopped by the armor and failed hit attempts also count.  
    Of course, people with `COMBAT FLEE` flee beforehand.  

## `COMBAT HELP`

One unit with `COMBAT HELP NOT` will not be helped in battle, neither by units of your own faction nor by allies.  
If such a unit is attacked, no other units will be brought into battle.  
Of course, this only applies if other units without such a status are not also attacked.  

Your own faction is always involved when it attacks, or when it or a faction it helps is attacked.  
You'll find further details at [[cmd-help]] and in the chapters [[war]] and [Alliance][alliances].  

<!-- From [https://wiki.eressea.de/index.php?title=COMBAT&oldid=7216] -->
