---
# cSpell:locale en
alias: cmd-cast
---

# CAST

*[Short order][short-and-long-orders][^1].*  

**`CAST`**` [REGION `*`x`*` `*`y`*`] [LEVEL`*`nr`*`] "`*`Spell`*`" [`*`parameter`*`] ...`

With this order, a mage unit will attempt to cast the named spell.  

Please note that the REGION and LEVEL modifiers do not apply to every spell.
REGION can only be used with [ranged spells][ranged-spells], and LEVEL only makes sense with variable [cost][components] spells.

!!! note
    Some spells have additional parameters.

The use of the spells is explained in more detail in the [[magic]] chapter, and can also be found in the spell description itself.  
You get this when you get the spell again and can use it with [`SHOW ALL SPELLS`][cmd-show] display again.  

Combat spells cannot simply be cast.  
If you want to use this against a unit, you have to set the [`COMBATSPELL`][cmd-combatspell] and then [attack][cmd-attack] a unit (or be attacked).  
However, this can lead to bigger battles!  

[^1]: although `CAST` is not a long order, it excludes other long orders. But you can cast other spells.

<!-- From [https://wiki.eressea.de/index.php?title=CAST&oldid=16737] -->

[cmd-attack]: [[cmd-attack]]
[cmd-combatspell]: [[cmd-combatspell]]
[cmd-show]: [[cmd-show]]
