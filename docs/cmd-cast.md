---
# cSpell:locale en
alias: cmd-cast
---
# CAST

**`CAST`**[<sup>`(l)`</sup>]` [REGION `*`x`*` `*`y`*`] [LEVEL`*`nr`*`] "`*`Spell`*`" [`*`parameter`*`] ...`

With this order, a mage unit will attempt to cast the named spell.

[<sup>(l)</sup>][<sup>`(l)`</sup>] Although CAST is not a long order, it excludes other long orders. But you can cast other spells.

Please note that the REGION and LEVEL modifiers do not apply to every spell.
REGION can only be used with [ranged spells], and LEVEL only makes sense with variable [cost] spells.

!!! note
    Some spells have additional parameters.

The use of the spells is explained in more detail in the [[magic]] chapter, and can also be found in the spell description itself.
You get this when you get the spell again and can use it with [[cmd-show|`SHOW ALL SPELLS`]] display again.

Combat spells cannot simply be cast. If you want to use this against a unit, you have to set the [[cmd-combatspell]] and then [[cmd-attack|attack]] a unit or be attacked. However, this can lead to bigger battles!

<!-- From [https://wiki.eressea.de/index.php?title=CAST&oldid=16737] -->

[<sup>`(l)`</sup>]: ./commands.md#short-and-long-orders
[ranged spells]: ./magic.md#ranged-spells
[cost]: ./magic.md#components
