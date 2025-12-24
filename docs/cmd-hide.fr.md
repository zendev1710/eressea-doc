---
# cSpell:locale fr, en
alias: cmd-hide-fr
---
# HIDE

**`HIDE`**`[`*`level`*`]`  
**`HIDE`**`FACTION [NOT]`  
**`HIDE`**`FACTION NUMBER [`*`number`*`]`  
**`HIDE`**` `*`race`*  

With the first variant you can adjust how “intensively” a unit tries to camouflage itself. `level` obviously cannot be higher than the unit's [[camouflage|camouflage skill]].
If no parameters are specified, the maximum is set.

With `HIDE FACTION` you can try to hide your faction affiliation.
The faction affiliation is then displayed as *anonymous* to other players.
In contrast to the normal stealth/perception mechanism, the faction affiliation of such a unit can only be recognized using [espionage].
With `HIDE FACTION NOT` this anonymization will be canceled again and other players will see the correct faction affiliation - if they have enough awareness and even see the unit in their report.

`HIDE FACTION NUMBER number` camouflages the unit with the specified faction number, so it can disguise itself as belonging to any other faction.
There is no easy way to see through this form of camouflage. In order to appear to belong to your own faction again, you have to `number` your own faction number can be used.
The specified faction must be known to the faction issuing the order, i.e. appear in their report, otherwise the order will fail. Parties that receive [[cmd-help|`[HELP xyz FACTION CAMO]`]] from the unit's faction or group can see the unit's true faction affiliation.

So far, so simple. However, this camouflage comes with a few special features, which are listed here in no particular order:

- The (apparent) race of the unit does not change as a result; a goblin remains a goblin, even if he claims to belong to the light elves faction
- The units do not change their behavior due to the camouflage. For example, they do not donate silver to the allies of the faction they disguise themselves as.
  So if you want to perfect the camouflage, you should form a group with the units and set appropriate help statuses for this group.
  Units cloaked in this way cannot suddenly enter buildings or ships that they are otherwise not allowed to enter, or collect taxes where they are normally prohibited from doing so
- In battle, such units form their own army.
  Example: There are three parties, the Wood Elves, the River Elves and the Iron Dwarves. All parties each have a unit: Wood Elf, River Elf and Iron Dwarf.
  While Wood Elf disguises itself as a River Elf, all other units retain their true identities.
  Now the iron dwarf attacks the river elf. This means that three armies appear in the battle report: the iron dwarves and two river elf armies.

However, [[cmd-group]] also has the side effect of having multiple armies.
This way you can't see whether units are posing as a foreign faction or whether the person in question just has several groups.

With `HIDE race` [demons] can disguise themselves as another race.

## Voir aussi

- [espionage]
- [[camouflage]]

<!-- From [https://wiki.eressea.de/index.php?title=HIDE&oldid=15791] -->

[espionage]: ./skills-list.md#espionnage
[demons]: ./races.md#demons
