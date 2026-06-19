---
# cSpell:locale en
alias: cmd-grow
---

# GROW

*[long order][short-and-long-orders].*  

**`GROW`**`HORSES`  
**`GROW`**`[`*`amount`*`] HERBS`  

With **`GROW`**, a unit tries to plant herbs in a region, or breed horses if in a [stable][stable].  

With `GROW HORSES` a unit can breed one horse per person and skill level in [taming][taming], with a probability of ***\[Taming skill level\]***%.  
e.g. 3 persons level 5 would therefore have `3 x 5 = 15` attempts at 5% each to get a horse.  

You need at least 2 horses in the stable to be able to breed horses.  
In addition, there must be 1 horse per "breeding opportunity" (i.e. 15 horses in the above example).  
The unit itself must have these horses; the material pool is not used here.  

For `GROW HERBS` you need at least [Herbalism][herbalism] **level 6**.  
The unit tries to plant the specified number of herbs, but no more than one herb per skill level;  
it needs the appropriate number of herbs of the corresponding type as well as a potion of "Water of Life".  
It is not possible to change herb types of a region, the unit always tries to plant the type found before.  

## See also

- [`PLANT`][cmd-plant] (for herbs, trees or seeds).

<!-- From [https://wiki.eressea.de/index.php?title=GROW/en&oldid=14482] -->

[cmd-plant]: [[cmd-plant]]
