---
# cSpell:locale en
alias: alchemy
---
# Alchemy

In Eressea, alchemy is the art of transforming natural substances (herbs) into potions.

## Potions

Alchemical **potions** are prepared using [[herbs]] and other ingredients, and can then be used by any unit.  

A potion weighs nothing.

### Making

To make a potion, you need units with the [alchemy] skill, and to find the required herbs, you need units with the [herbalism] skill.

!!! warning "Remark"
    A faction has at most **3 alchemists**.

Potions are make with the order [[cmd-make|`MAKE "<potion name>"`]].  

Each potion requires several ingredients.  
Recipes are given each time you reach the level required to concoct them.  

!!! tip "Astuce"
    Later, you can find them using the [[cmd-show|`SHOW "<nom potion>"`]] order.

To be able to make a potion, the alchemist's level must be **twice** as high as the potion's level.  
Each turn, an alchemist can make N potions, calculated as follows:
$$
N = \frac{T_{\text{unit}}}{Level_{\text{potion}}*2}
$$

*For example, a T6 alchemist can therefore make a maximum of 1 L3 potion ($6\,/\,(3\,\times\,2)=1$), 1 L2 potion ($6\,/\,(2\,\times\,2)=1$) or 3 L1 potions ($6\,/\,(1\,\times\,2)=3$).*

!!! note "Note"
    Herbs can be [[cmd-research|discovered]] in a region and then [[cmd-make|harvested]] by a competent unit in [herbalism].

### Using

If you want to use a potion, you do so with [[cmd-use|`USE [<amount>] "<potion name>" [<unit-id>]`]] order.  

Remark: *Unit ID* is required **only** for **[duncebun]** potion.  

A potion cannot be divided between several units.  
However, a large unit can be divided into several smaller units after the potion has been used, retaining its effects.  

All the potions have a positive effect, with the exception of [duncebun].  

Most potions give their benefits to the unit giving the order.  
Exceptions are potions which affect a region -then the region where the unit was at the beginning of turn is affected- or those that affect other units (duncebun potion).  

Usually a potion affects 10 people or 10 goods during the turn it is used, as mentioned in its recipe.  
Potions that affect a unit's items expire if they cannot be used because the unit no longer has these items.  
Many potions work in such a way that too many people in the unit make no difference, i.e. with 12 people and a potion (works for 10) the effect only affects 10 of the 12 people.  

This is not possible with [berserkers blood] potion, as the persons do not act as a unit in battle.  
Here it is necessary that all persons in the unit have the effect of the potion before the fight, otherwise it will not work!  

The "residual effect" of potions does not expire with all potions.  
For example, a person can benefit from the effect of a [brain wax] or [busybeer] for ten weeks after using it.  

## List of potions

Below you will find the list of potions in ascending order of level.

### Level 1

#### Goliath water

:   10 men can carry as much as 10 horses.

*Goal:* to increase transport capacity.  
*Level:* **1**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [bugleweed]
- [fjord fungus]

#### Potion of truth

:   *This potion hasn't had a function for a long time*.

*Level:* **1**.  
*Target:* **region**.  

To prepare this potion, you will need the following herbs:

- [fjord fungus]
- [flatroot]

#### Seven mile tea

:   10 men on foot can travel as fast as if mounted.

*Goal:* to increase the speed of movement.  
*Level:* **1**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [cobalt fungus]
- [windbag]

#### Water of life

:   Transforms 10 pieces of wood or Mallorn into 10 mallorn/saplings.

*Goal:* to increase the resources of a region (trees and mallorns).  
*Level:* **1**.  
*Target:* **region**.  

To prepare this potion, you will need the following herbs:

- [elvendear]
- [knotroot]

### Level 2

#### Busybeer

:   **Doubles the productivity of 10 men** when using **`MAKE`** order.

*Goal:* to increase productivity.  
*Level:* **2**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [gapgrowth]
- [mandrake]
- [tangy temerity]

#### Ointment

:   Heals up to 400 hit points.

*Goal:* heal a unit.  
*Level:* **2**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [cobalt fungus]
- [tangy temerity]
- [white hemlocks]

#### Peasant blood

:   Up to 100 demons can do without killing peasants.

*Goal:* to increase the resources of a region (peasants) where demons are present.  
*Level:* **2**.  
*Target:* **unit**.  

To prepare this potion, you will need the following ingredients:

- [cave lichen]
- [cobalt fungus]
- [fjord fungus]
- peasant

!!! note
    A peasant blood acts on the unit, but all the faction's demons in the region use it if there are any left.  
    So you only need to equip one unit (per region), as long as it drinks enough peasant blood for all the demons.  

### Level 3

#### Berserkers blood

:   10 men receive a **+1 attack** modifier in combat.

*Goal:* to strengthen the attack.  
*Level:* **3**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [flatroot]
- [mandrake]
- [sand reeker]
- [white hemlocks]

#### Brain wax

:   Increases the chances for up to **10 men** of **learning a skill**.

*Goal:* to accelerate learning.  
*Level:* **3**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [bugleweed]
- [rock weed]
- [waterfinder]
- [windbag]

#### Duncebun

:   for 10 people: no learning or teacher brings nothing or forget 1 week of the best skill.

*Goal:* slow down the learning of a unit.  
*Level:* **3**.  
*Target:* **foreign unit**.  

To prepare this potion, you will need the following herbs:

- [cave lichen]
- [fjord fungus]
- [owlsgaze]
- [spider ivy]

!!! note
    You can apply it to a unit with the order `USE "Duncebun"`&nbsp;&lt;`unit−id`&gt;.  
    The application of the potion fails if the `Stealth` skill of the acting unit is less or equal to the victim's `Perception` level **+ 2**.  
    In this case, you get an error message and the duncebun is not used up (thus it remains to the unit).

#### Horsepower potion

:   50 horses give birth to up to **4 foals**.

*Goal:* to increase the resources of a region (horses).  
*Level:* **3**.  
*Target:* **region**.  

To prepare this potion, you will need the following herbs:

- [cobalt fungus]
- [knotroot]
- [peyote],
- [sand reeker]

#### Potion of nest warmth

:   Allows **[Insects]** to recruit men **even in winter**.

*Goal:* to allow the recruitment of [Insects] in winter.  
*Level:* **3**.  
*Target:* **region**.  

To prepare this potion, you will need the following herbs:

- [gapgrowth]
- [ice begonia]
- [peyote]
- [spider ivy]

### Level 4

#### Elixir of power

:   10 men get **5 times their normal hit points**.

*Goal:* to increase a unit's Hit Points.  
*Level:* **4**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [bubblemorel]
- [[dragonblood]]
- [elvendear]
- [spider ivy]
- [waterfinder]
- [windbag]

#### Healing potion

:   one person survives otherwise fatal damage; only possible once per person per week.

*Goal:* to increase the chances of survival in combat.  
*Level:* **4**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [bugleweed]
- [elvendear]
- [gapgrowth]
- [ice begonia]
- [windbag]

#### Peasant love potion

:   1000 peasants grow twice as fast as usual.

*Goal:* to increase the resources of a region (farmers).  
*Level:* **4**.  
*Target:* **region**.  

To prepare this potion, you will need the following herbs:

- [bubblemorel]
- [elvendear]
- [mandrake]
- [rock weed]
- [snowcrystal petal]

## Potions - Summary table

| Name                    | Abbr | Level | Target           |
|-------------------------|:----:|:-----:|------------------|
| [Goliath water]         |  GW  |   1   | Unit             |
| [Potion of truth]       |  PT  |   1   | Region           |
| [Seven mile tea]        |  SM  |   1   | Unit             |
| [Water of life]         |  WL  |   1   | Region           |
| [Busybeer]              |  BZ  |   2   | Unit             |
| [Ointment]              |  OM  |   2   | Unit             |
| [Peasant blood]         |  PB  |   2   | Unit[^1]         |
| [Berserkers blood]      |  BK  |   3   | Unit             |
| [Brain wax]             |  BW  |   3   | Unit             |
| [Duncebun]              |  DB  |   3   | Foreign unit[^2] |
| [Horsepower potion]     |  HP  |   3   | Region           |
| [Potion of nest warmth] |  NW  |   3   | Region           |
| [Elixir of power]       |  EP  |   4   | Unit             |
| [Healing potion]        |  HL  |   4   | Unit             |
| [Peasant love potion]   |  PL  |   4   | Region           |

## Herbs table

<!-- TODO: not possible to disp^lay this table without horizontal scrooll bar !? min column width is too high -->
| Herb                |       [SM]       |       [GW]       |       [WL]       |       [PB]       |       [BZ]       |       [OM]       |       [BK]       |       [DB]       |       [BW]       |       [HP]       |       [NW]       |       [PL]       |       [EP]       |       [HL]       |
|---------------------|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|
| [bubblemorel]       |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: | :material-check: |                  |
| [bugleweed]         |                  | :material-check: |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  | :material-check: |
| [cave lichen]       |                  |                  |                  | :material-check: |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |
| [cobalt fungus]     | :material-check: |                  |                  | :material-check: |                  | :material-check: |                  |                  |                  | :material-check: |                  |                  |                  |                  |
| [elvendear]         |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: | :material-check: | :material-check: |
| [fjord fungus]      |                  | :material-check: |                  | :material-check: |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |
| [flatroot]          |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |                  |
| [gapgrowth]         |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |
| [ice begonia]       |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |
| [knotroot]          |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |
| [mandrake]          |                  |                  |                  |                  | :material-check: |                  | :material-check: |                  |                  |                  |                  | :material-check: |                  |                  |
| [owlsgaze]          |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  |                  |                  |                  |
| [peyote]            |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: | :material-check: |                  |                  |                  |
| [rock weed]         |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |                  |                  |
| [sand reeker]       |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |                  |                  |                  |                  |
| [snowcrystal petal] |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |
| [spider ivy]        |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  | :material-check: |                  | :material-check: |                  |
| [tangy temerity]    |                  |                  |                  |                  | :material-check: | :material-check: |                  |                  |                  |                  |                  |                  |                  |                  |
| [waterfinder]       |                  |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  | :material-check: |                  |
| [white hemlocks]    |                  |                  |                  |                  |                  | :material-check: | :material-check: |                  |                  |                  |                  |                  |                  |                  |
| [windbag]           | :material-check: |                  |                  |                  |                  |                  |                  |                  | :material-check: |                  |                  |                  | :material-check: | :material-check: |

Continue reading: [[herbs]].

[^1]: Acts on the unit, but all the faction's demons in the region use it if there are any left.  
So you only need to equip one unit (per region), as long as it drinks enough peasant blood for all the demons.  
[^2]: You can apply it to a unit with the order `USE Duncebun <unit−id>`.  
The application of the potion fails if the [[camouflage]] skill of the acting unit is **less or equal** to the victim's **[perception] level + 2**.
In this case, you get an error message and the [duncebun] is not used up (thus it remains to the unit).

<!-- From [https://wiki.eressea.de/index.php?title=Tränke/en&oldid=16929] -->

[Alchemy]: ./skills-list.md#alchemy
[Herbalism]: ./skills-list.md#herbalism
[perception]: ./skills-list.md#perception
[Insects]: ./races.md#insects

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
[peyote]: ./herbs.md#peyote
[rock weed]: ./herbs.md#rock-weed
[sand reeker]: ./herbs.md#sand-reeker
[snowcrystal petal]: ./herbs.md#snowcrystal-petal
[spider ivy]: ./herbs.md#spider-ivy
[tangy temerity]: ./herbs.md#tangy-temerity
[waterfinder]: ./herbs.md#waterfinder
[white hemlocks]: ./herbs.md#white-hemlocks
[windbag]: ./herbs.md#windbag

[Goliath water]: #goliath-water
[Potion of truth]: #potion-of-truth
[Seven mile tea]: #seven-mile-tea
[Water of life]: #water-of-life
[Busybeer]: #busybeer
[Ointment]: #ointment
[Peasant blood]: #peasant-blood
[Berserkers blood]: #berserkers-blood
[Brain wax]: #brain-wax
[Duncebun]:#duncebun
[Horsepower potion]: #horsepower-potion
[Potion of nest warmth]: #potion-of-nest-warmth
[Elixir of power]: #elixir-of-power
[Healing potion]: #healing-potion
[Peasant love potion]: #peasant-love-potion

[SM]: #seven-mile-tea "Seven mile tea"
[GW]: #goliath-water "Goliath water"
[WL]:  #water-of-life "Water of life"
[PB]: #peasant-blood "Peasant blood"
[BZ]: #busybeer "Busybeer"
[OM]: #ointment "Ointment"
[BK]: #berserkers-blood "Berserkers blood"
[DB]: #duncebun "Duncebun"
[BW]: #brain-wax "Brain wax"
[HP]: #horsepower-potion "Horsepower potion"
[NW]: #potion-of-nest-warmth "Potion of nest warmth"
[PL]: #peasant-love-potion "Peasant love potion"
[EP]: #elixir-of-power "Elixir of power"
[HL]: #healing-potion "Healing potion"
