---
# cSpell:locale en
alias: alliances
---
# Alliances

Alliances form the backbone of the world, be it in war, trade or just peaceful cooperation.
There are areas of Eressea where you can do this not just "in spirit" but also with respect to the game rules, which is achieved with the [[cmd-help]] order.

When a faction helps another faction, it does not automatically mean that this is mutual.
The only way to find out is the hard way, by trying it.
There are good reasons that the corresponding rights are not granted automatically: if so, you could weigh down enemy units with stones or dilute their elite warriors with peasants, or take alle the taxes from the local lord.

These are the areas of support:

## `HELP GIVE`

Your units will accept all items and silver from the other faction.
It is similar to a permanent [[cmd-contact]] for [[cmd-give]].

!!! warning "Attention !"
    For giving persons or units to another faction with the orders [[cmd-give|`GIVE <their-unit> <number> MEN`]] or [[cmd-give|`GIVE <their-unit> UNIT`]], the receiving faction must use the [[cmd-contact]] order!  
    Also for targeted spells, `CONTACT` is necessary.

## `HELP COMBAT`

Your own combat-ready units (except those with `COMBAT FLEE` or `COMBAT NOT`) will [[war|join a fight]] if the allied faction is being attacked.

## `HELP SILVER`

Help the allied faction [supporting] their units if you have silver left after paying for your own support.
If the units of the allied faction do not have enough silver to feed themselves, your units will give them silver.
No HELP GIVE is required by the receiving faction for this kind of transfer.

## `HELP GUARD`

Lifts all the restrictions of [[cmd-guard]] and extends some useful functions to the target faction: Normally guarding factions do not let other factions [[money|raise taxes]], [recruit], or [[resources|produce]] finite resources and sometimes other units are prevented from [[cmd-guard|traveling through]] your region.
If this help status is set, units of the other factions are allowed to do all that, so they can travel, mine, or recruit freely.

Additionally, allied factions are allowed long orders [after battles] if you guard the region.

Finally, the other faction's units are allowed to [[cmd-enter|enter]] your buildings and ships.

## `HELP FACTIONSTEALTH`

If you disguise your units with [[cmd-hide|`HIDE FACTION NUMBER <faction>`]] as belonging to another faction, factions you have given this help status can see that they really belong to your faction.

## `HELP ALL`

this covers all the above areas in one order.

## See also

- [[cmd-help]]
- [[cmd-guard]]
- [[cmd-contact]]

Continue reading: [[magic]].

<!-- From [https://wiki.eressea.de/index.php?title=Allianz/en&oldid=16781] -->

[supporting]: ./silver.md#upkeep-costs
[recruit]: ./silver.md#recruiting
[after battles]: ./war.md#the-end
