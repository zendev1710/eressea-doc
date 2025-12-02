# GROW

**`GROW`**`Horses`  
**`GROW`**`[`*`amount`*`] HERBS`

**`GROW`** is a long order with which units try to plant herbs in a region or breed horses if in a [Stable].

With `GROW HORSES` a unit can breed one horse per person and skill level in [Taming] with a probability of \[Taming skill\]%. 3 persons level 5 would therefore have 3 \* 5 = 15 attempts at 5% each to get a horse.

You need at least two horses in the stable to be able to breed horses. In addition, there must be one horse per "breeding opportunity" (i.e. 15 horses in the above example). The unit itself must have these horses; the material pool is not used here.

For `GROW HERBS` you need at least [Herbalism][Taming] 6. The unit tries to plant the specified number of herbs, but no more than one herb per skill level; it needs the appropriate number of herbs of the corresponding type as well as a potion of "Water of Life". It is not possible to change herb types of a region, the unit always tries to plant the type found before.

## See also

- [PLANT] Herbs/Trees/Seeds

<!-- From [https://wiki.eressea.de/index.php?title=ZÜCHTE/en&oldid=14482] -->

  [Stable]: ./buildings-others.md#Pferdezucht "Andere Gebäude"
  [Taming]: ./skills-list.md "Liste der Talente"
  [PLANT]: ./cmd-plant.md "PFLANZE"
