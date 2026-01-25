---
# cSpell:locale en
alias: alchemy
---
# Alchemy

## Potions

Alchemical **potions** are prepared using [[herbs]] and other ingredients, and can then be used by any unit.
To make a potion, you need units with the skill [Alchemy], and to find the required herbs, you need units with the skill [Herbalism].

Potions are make with the order [[cmd-make|`MAKE "<potion name>"`]].
Each potion requires several ingredients.
Recipes are given each time you reach the level required to concoct them.
Later, you can find them using the [[cmd-show]] order.
To be able to make a potion, the alchemist's level must be twice as high as the potion's level.
Each turn, an alchemist can make (skill level)/(potion level\*2) potions.
A level 6 alchemist can therefore make a maximum of one level 3 potion, one level 2 potion or three level 1 potions.

If you want to use a potion, you do so with [[cmd-use|&#91;amount&#93; "&lt;potion name&gt;" &#91;unit ID&#93;]] order.  
*Unit ID* is required **only** for **[Duncebun]** potion.

A potion cannot be divided between several units.
However, a large unit can be divided into several smaller units after the potion has been used, retaining its effects.

Most potions give their benefits to the unit giving the order.
Exceptions are potions which affect a region -then the region where the unit was at the beginning of turn is affected- or those that affect other units (Duncebun potion).

Usually a potion affects 10 people or 10 goods during the turn it is used, as mentioned in its recipe.
Potions that affect a unit's items expire if they cannot be used because the unit no longer has these items.
Many potions work in such a way that too many people in the unit make no difference, i.e. with 12 people and a potion (works for 10) the effect only affects 10 of the 12 people.
This is not possible with "berserks blood" potion, as the persons do not act as a unit in battle.
Here it is necessary that all persons in the unit have the effect of the potion before the fight, otherwise it will not work!

The "residual effect" of potions does not expire with all potions, so that, for example, a person can benefit from the effect of a “Brain wax” or “busybeers” for ten weeks after using it.

### Berserkers blood

:   10 men receive a **+1 attack** modifier in combat.

**Level**: 3.  
**Target**: unit.  

To be made, this potion requires the following herbs:

- 1 [flatroot]
- 1 [mandrake]
- 1 [sand reeker]
- 1 [white hemlocks]

### Brain wax

:   Increases the chances for up to **10 men** of **learning a skill**.

**Level**: 3.  
**Target**: unit.  

To be made, this potion requires the following herbs:

- 1 [bugleweed]
- 1 [rock weed]
- 1 [waterfinder]
- 1 [windbag]

### Busybeer

:   **Doubles the productivity of 10 men** when using **`MAKE`** order.

**Level**: 2.  
**Target**: unit.  

To be made, this potion requires the following herbs:

- 1 [gapgrowth]
- 1 [mandrake]
- 1 [tangy temerity]

### Duncebun

:   for 10 people: no learning or teacher brings nothing or forget 1 week of the best skill.

**Level**: 3.  
**Target**: \[foreign\] unit.  

To be made, this potion requires the following herbs:

- 1 [cave lichen]
- 1 [fjord fungus]
- 1 [owlsgaze]
- 1 [spider ivy]

!!! note
    You can apply it to a unit with the order `USE "Duncebun"`&nbsp;&lt;`unit−id`&gt;.  
    The application of the potion fails if the `Stealth` skill of the acting unit is less or equal to the victim's `Perception` level **+ 2**.  
    In this case, you get an error message and the Duncebun is not used up (thus it remains to the unit).

### Elixir of power

:   10 men get **5 times their normal hit points**.

**Level**: 4.  
**Target**: unit.  

To be made, this potion requires the following herbs:

- 1 [[dragonblood]]
- 1 [bubblemorel]
- 1 [elvendear]
- 1 [spider ivy]
- 1 [waterfinder]
- 1 [windbag]

### Goliath water

:   10 men can carry as much as 10 horses.

**Level**: 1.  
**Target**: unit.  

To be made, this potion requires the following herbs:

- 1 [bugleweed]
- 1 [fjord fungus]

### Healing potion

:   one person survives otherwise fatal damage; only possible once per person per week.

**Level**: 4.  
**Target**: unit.  

To be made, this potion requires the following herbs:

- 1 [bugleweed]
- 1 [elvendear]
- 1 [gapgrowth]
- 1 [ice begonia]
- 1 [windbag]

### Horsepower potion

:   50 horses give birth to up to **4 foals**.

**Level**: 3.  
**Target**: region.  

To be made, this potion requires the following herbs:

- 1 [cobalt fungus]
- 1 [knotroot]
- 1 [peyote],
- 1 [sand reeker]

### Ointment

:   Heals up to 400 hit points.

**Level**: 2.  
**Target**: unit.  

To be made, this potion requires the following herbs:

- 1 [cobalt fungus]
- 1 [tangy temerity]
- 1 [white hemlocks]

### Peasant blood

:   Up to 100 demons can do without killing peasants.

**Level**: 2.  
**Target**: unit.  

To be made, this potion requires the following **ingredients**:

- 1 [cave lichen]
- 1 [cobalt fungus]
- 1 [fjord fungus]
- 1 **peasant**

!!! note
    A peasant blood acts on the unit, but all the faction's demons in the region use it if there are any left.  
    So you only need to equip one unit (per region), as long as it drinks enough peasant blood for all the demons.  

### Peasant love potion

:   1000 peasants grow twice as fast as usual.

**Level**: 4.  
**Target**: region.  

To be made, this potion requires the following herbs:

- 1 [bubblemorel]
- 1 [elvendear]
- 1 [mandrake]
- 1 [rock weed]
- 1 [snowcrystal petal]

### Potion of nest warmth

:   Allows **[Insects]** to recruit men **even in winter**.

**Level**: 3.  
**Target**: region.  

To be made, this potion requires the following herbs:

- 1 [gapgrowth]
- 1 [ice begonia]
- 1 [peyote]
- 1 [spider ivy]

### Potion of truth

:   *This potion hasn't had a function for a long time*.

**Level**: 1.  
**Target**: region.  

To be made, this potion requires the following herbs:

- 1 [fjord fungus]
- 1 [flatroot]

### Seven mile tea

:   10 men on foot can travel as fast as if mounted.

**Level**: 1.  
**Target**: unit.  

To be made, this potion requires the following herbs:

- 1 [cobalt fungus]
- 1 [windbag]

### Water of life

:   Transforms 10 pieces of wood or Mallorn into 10 mallorn/saplings.

**Level**: 1.  
**Target**: region.  

To be made, this potion requires the following herbs:

- 1 [elvendear]
- 1 [knotroot]

## Summary table

Potions list.

| Name                  | Abbr | Level | Target               |
|-----------------------|:----:|:-----:|----------------------|
| Elixir of power       |  EP  |   4   | Unit                 |
| Healing potion        |  HL  |   4   | Unit                 |
| Peasant love potion   |  PL  |   4   | Region               |
| Berserkers blood      |  BK  |   3   | Unit                 |
| Brain wax             |  BW  |   3   | Unit                 |
| Duncebun              |  DB  |   3   | \[Foreign\] unit[^2] |
| Horsepower potion     |  HP  |   3   | Region               |
| Potion of nest warmth |  NW  |   3   | Region               |
| Busybeer              |  BZ  |   2   | Unit                 |
| Ointment              |  OM  |   2   | Unit                 |
| Peasant blood         |  PB  |   2   | Unit[^1]             |
| Goliath water         |  GW  |   1   | Unit                 |
| Potion of truth       |  PT  |   1   | Region               |
| Seven mile tea        |  SM  |   1   | Unit                 |
| Water of life         |  WL  |   1   | Region               |

[^1]: Acts on the unit, but all the faction's demons in the region use it if there are any left.  
So you only need to equip one unit (per region), as long as it drinks enough peasant blood for all the demons.  

[^2]: You can apply it to a unit with the order `USE "Duncebun"`&nbsp;&lt;`unit−id`&gt;.  
The application of the potion fails if the STEALTH skill of the acting unit is less or equal to the victim's PERCEPTION+2.
In this case, you get an error message and the Duncebun is not used up (thus it remains to the unit).

## Herbs table

<!-- TODO: not possible to disp^lay this table without horizontal scrooll bar !? min column width is too high -->
| Herb              |        PT        |        SM        |        GW        |        WL        |        PB        |        BZ        |        OM        |        BK        |        DB        |        BW        |        HP        |        NW        |        PL        |        EP        |        HL        |
|-------------------|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|
| bubblemorel       |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: | :material-check: |                  |
| bugleweed         |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  | :material-check: |
| cave lichen       |                  |                  |                  |                  | :material-check: |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |
| cobalt fungus     |                  | :material-check: |                  |                  | :material-check: |                  | :material-check: |                  |                  |                  | :material-check: |                  |                  |                  |                  |
| elvendear         |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: | :material-check: | :material-check: |
| fjord fungus      | :material-check: |                  | :material-check: |                  | :material-check: |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |
| flatroot          | :material-check: |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |                  |
| gapgrowth         |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |
| ice begonia       |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |
| knotroot          |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |
| mandrake          |                  |                  |                  |                  |                  | :material-check: |                  | :material-check: |                  |                  |                  |                  | :material-check: |                  |                  |
| owlsgaze          |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |
| peyote            |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: | :material-check: |                  |                  |                  |
| rock weed         |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |                  |                  |
| sand reeker       |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |                  |                  |                  |                  |
| snowcrystal petal |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |
| spider ivy        |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |                  | :material-check: |                  |
| tangy temerity    |                  |                  |                  |                  |                  | :material-check: | :material-check: |                  |                  |                  |                  |                  |                  |                  |                  |
| waterfinder       |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  | :material-check: |                  |
| white hemlocks    |                  |                  |                  |                  |                  |                  | :material-check: | :material-check: |                  |                  |                  |                  |                  |                  |                  |
| windbag           |                  | :material-check: |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  | :material-check: | :material-check: |

Continue reading: [[herbs]].

<!-- From [https://wiki.eressea.de/index.php?title=Tränke/en&oldid=16929] -->

[Alchemy]: ./skills-list.md#alchemy
[Herbalism]: ./skills-list.md#herbalism
[Insects]: ./races.md#insects

[Duncebun]: #duncebun

[bubblemorel]: ./herbs.md#bubblemorel
[bugleweed]: ./herbs.md#bugleweed
[cave lichen]: ./herbs.md#cave-lichen
[cobalt fungus]: ./herbs.md#cobalt-fungus
[elvendear]: ./herbs.md#elvendear
[fjord fungus]: ./herbs.md#fjord-fungus
[flatroot]: ./herbs.md#flatroot
[gapgrowth]: ./herbs.md#gapgrowth
[ice begonia]: ./herbs.md#ice-begonia
[knotroot]: ./herbs.md#knotroot
[mandrake]: ./herbs.md#mandrake
[owlsgaze]: ./herbs.md#owlsgaze
[rock weed]: ./herbs.md#rock-weed
[sand reeker]: ./herbs.md#sand-reeker
[snowcrystal petal]: ./herbs.md#snowcrystal-petal
[spider ivy]: ./herbs.md#spider-ivy
[tangy temerity]: ./herbs.md#tangy-temerity
[waterfinder]: ./herbs.md#waterfinder
[white hemlocks]: ./herbs.md#white-hemlocks
[windbag]: ./herbs.md#windbag