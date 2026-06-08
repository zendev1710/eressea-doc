---
# cSpell:locale en
alias: alchemy
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD042 MD052 -->
# Alchemy

In Eressea, alchemy is the art of transforming natural substances (herbs) into potions.

[](){ #potions-id }

## Potions

Alchemical **potions** are prepared using [[herbs]] and other ingredients, and can then be used by any unit.  

A potion weighs nothing.

### Making

To make a potion, you need units with the [alchemy][skill-alchemy-id] skill, and to find the required herbs, you need units with the [herbalism][herbalism] skill.

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
    Herbs can be [[cmd-research|discovered]] in a region and then [[cmd-make|harvested]] by a competent unit in [herbalism][herbalism].

### Using

If you want to use a potion, you do so with [`USE [<amount>] "<potion name>" [<unit-id>]`][cmd-use] order.  

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

- [bugleweed][bugleweed]
- [fjord fungus][fjord-fungus]

#### Potion of truth

:   *This potion hasn't had a function for a long time*.

*Level:* **1**.  
*Target:* **region**.  

To prepare this potion, you will need the following herbs:

- [fjord fungus][fjord-fungus]
- [flatroot][flatroot]

#### Seven mile tea

:   10 men on foot can travel as fast as if mounted.

*Goal:* to increase the speed of movement.  
*Level:* **1**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [cobalt fungus][cobalt-fungus]
- [windbag][windbag]

#### Water of life

:   Transforms 10 pieces of wood or Mallorn into 10 mallorn/saplings.

*Goal:* to increase the resources of a region (trees and mallorns).  
*Level:* **1**.  
*Target:* **region**.  

To prepare this potion, you will need the following herbs:

- [elvendear][elvendear]
- [knotroot][knotroot]

### Level 2

#### Busybeer

:   **Doubles the productivity of 10 men** when using **`MAKE`** order.

*Goal:* to increase productivity.  
*Level:* **2**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [gapgrowth][gapgrowth]
- [mandrake][mandrake]
- [tangy temerity][tangy-temerity]

#### Ointment

:   Heals up to 400 hit points.

*Goal:* heal a unit.  
*Level:* **2**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [cobalt fungus][cobalt-fungus]
- [tangy temerity][tangy-temerity]
- [white hemlocks][white-hemlocks]

#### Peasant blood

:   Up to 100 demons can do without killing peasants.

*Goal:* to increase the resources of a region (peasants) where demons are present.  
*Level:* **2**.  
*Target:* **unit**.  

To prepare this potion, you will need the following ingredients:

- [cave lichen][cave-lichen]
- [cobalt fungus][cobalt-fungus]
- [fjord fungus][fjord-fungus]
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

- [flatroot][flatroot]
- [mandrake][mandrake]
- [sand reeker][sand-reeker]
- [white hemlocks][white-hemlocks]

#### Brain wax

:   Increases the chances for up to **10 men** of **learning a skill**.

*Goal:* to accelerate learning.  
*Level:* **3**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [bugleweed][bugleweed]
- [rock weed][rock-weed]
- [waterfinder][waterfinder]
- [windbag][windbag]

#### Duncebun

:   for 10 people: no learning or teacher brings nothing or forget 1 week of the best skill.

*Goal:* slow down the learning of a unit.  
*Level:* **3**.  
*Target:* **foreign unit**.  

To prepare this potion, you will need the following herbs:

- [cave lichen][cave-lichen]
- [fjord fungus][fjord-fungus]
- [owlsgaze][owlsgaze]
- [spider ivy][spider-ivy]

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

- [cobalt fungus][cobalt-fungus]
- [knotroot][knotroot]
- [peyote][peyote-id]
- [sand reeker][sand-reeker]

#### Potion of nest warmth

:   Allows [Insects][insects] to recruit men **even in winter**.

*Goal:* to allow the recruitment of [Insects][insects] in winter.  
*Level:* **3**.  
*Target:* **region**.  

To prepare this potion, you will need the following herbs:

- [gapgrowth][gapgrowth]
- [ice begonia][ice-begonia]
- [peyote][peyote-id]
- [spider ivy][spider-ivy]

### Level 4

#### Elixir of power

:   10 men get **5 times their normal hit points**.

*Goal:* to increase a unit's Hit Points.  
*Level:* **4**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [bubblemorel][bubblemorel]
- [[dragonblood]]
- [elvendear][elvendear]
- [spider ivy][spider-ivy]
- [waterfinder][waterfinder]
- [windbag][windbag]

#### Healing potion

:   one person survives otherwise fatal damage; only possible once per person per week.

*Goal:* to increase the chances of survival in combat.  
*Level:* **4**.  
*Target:* **unit**.  

To prepare this potion, you will need the following herbs:

- [bugleweed][bugleweed]
- [elvendear][elvendear]
- [gapgrowth][gapgrowth]
- [ice begonia][ice-begonia]
- [windbag][windbag]

#### Peasant love potion

:   1000 peasants grow twice as fast as usual.

*Goal:* to increase the resources of a region (farmers).  
*Level:* **4**.  
*Target:* **region**.  

To prepare this potion, you will need the following herbs:

- [bubblemorel][bubblemorel]
- [elvendear][elvendear]
- [mandrake][mandrake]
- [rock weed][rock-weed]
- [snowcrystal petal][snowcrystal-petal]

## Potions - Summary table

| Name                                           | Abbr | Level | Target           |
|------------------------------------------------|:----:|:-----:|------------------|
| [Goliath water][goliath-water]                 |  GW  |   1   | Unit             |
| [Potion of truth][potion-of-truth]             |  PT  |   1   | Region           |
| [Seven mile tea][seven-mile-tea]               |  SM  |   1   | Unit             |
| [Water of life][water-of-life]                 |  WL  |   1   | Region           |
| [Busybeer][busybeer]                           |  BZ  |   2   | Unit             |
| [Ointment][ointment]                           |  OM  |   2   | Unit             |
| [Peasant blood][peasant-blood]                 |  PB  |   2   | Unit[^1]         |
| [Berserkers blood][berserkers-blood]           |  BK  |   3   | Unit             |
| [Brain wax][brain-wax]                         |  BW  |   3   | Unit             |
| [Duncebun][duncebun]                           |  DB  |   3   | Foreign unit[^2] |
| [Horsepower potion][horsepower-potion]         |  HP  |   3   | Region           |
| [Potion of nest warmth][potion-of-nest-warmth] |  NW  |   3   | Region           |
| [Elixir of power][elixir-of-power]             |  EP  |   4   | Unit             |
| [Healing potion][healing-potion]               |  HL  |   4   | Unit             |
| [Peasant love potion][peasant-love-potion]     |  PL  |   4   | Region           |

## Herbs table

<!-- TODO: not possible to display this table without horizontal scroll bar !? min column width is too high -->
| Herb                                   | [SM][seven-mile-tea]{title="Seven mile tea"} | [GW][goliath-water]{title="Goliath water"} | [WL][water-of-life]{title="Water of life"} | [PB][peasant-blood]{title="Peasant blood"} | [BZ][busybeer]{title="Busybeer"} | [OM][ointment]{title="Ointment"} | [BK][berserkers-blood]{title="Berserkers blood"} | [DB][duncebun]{title="Duncebun"} | [BW][brain-wax]{title="Brain wax"} | [HP][horsepower-potion]{title="Horsepower potion"} | [NW][potion-of-nest-warmth]{title="Potion of nest warmth"} | [PL][peasant-love-potion]{title="Peasant love potion"} | [EP][elixir-of-power]{title="Elixir of power"} | [HL][healing-potion]{title="Healing potion"} |
|----------------------------------------|:--------------------------------------------:|:------------------------------------------:|:------------------------------------------:|:------------------------------------------:|:--------------------------------:|:--------------------------------:|:------------------------------------------------:|:--------------------------------:|:----------------------------------:|:--------------------------------------------------:|:----------------------------------------------------------:|:------------------------------------------------------:|:----------------------------------------------:|:--------------------------------------------:|
| [bubblemorel][bubblemorel]             |                                              |                                            |                                            |                                            |                                  |                                  |                                                  |                                  |                                    |                                                    |                                                            |                    :material-check:                    |                :material-check:                |                                              |
| [bugleweed][bugleweed]                 |                                              |              :material-check:              |                                            |                                            |                                  |                                  |                                                  |                                  |          :material-check:          |                                                    |                                                            |                                                        |                                                |               :material-check:               |
| [cave lichen][cave-lichen]             |                                              |                                            |                                            |              :material-check:              |                                  |                                  |                                                  |         :material-check:         |                                    |                                                    |                                                            |                                                        |                                                |                                              |
| [cobalt fungus][cobalt-fungus]         |               :material-check:               |                                            |                                            |              :material-check:              |                                  |         :material-check:         |                                                  |                                  |                                    |                  :material-check:                  |                                                            |                                                        |                                                |                                              |
| [elvendear][elvendear]                 |                                              |                                            |              :material-check:              |                                            |                                  |                                  |                                                  |                                  |                                    |                                                    |                                                            |                    :material-check:                    |                :material-check:                |               :material-check:               |
| [fjord fungus][fjord-fungus]           |                                              |              :material-check:              |                                            |              :material-check:              |                                  |                                  |                                                  |         :material-check:         |                                    |                                                    |                                                            |                                                        |                                                |                                              |
| [flatroot][flatroot]                   |                                              |                                            |                                            |                                            |                                  |                                  |                 :material-check:                 |                                  |                                    |                                                    |                                                            |                                                        |                                                |                                              |
| [gapgrowth][gapgrowth]                 |                                              |                                            |                                            |                                            |         :material-check:         |                                  |                                                  |                                  |                                    |                                                    |                      :material-check:                      |                                                        |                                                |               :material-check:               |
| [ice begonia][ice-begonia]             |                                              |                                            |                                            |                                            |                                  |                                  |                                                  |                                  |                                    |                                                    |                      :material-check:                      |                                                        |                                                |               :material-check:               |
| [knotroot][knotroot]                   |                                              |                                            |              :material-check:              |                                            |                                  |                                  |                                                  |                                  |                                    |                  :material-check:                  |                                                            |                                                        |                                                |                                              |
| [mandrake][mandrake]                   |                                              |                                            |                                            |                                            |         :material-check:         |                                  |                 :material-check:                 |                                  |                                    |                                                    |                                                            |                    :material-check:                    |                                                |                                              |
| [owlsgaze][owlsgaze]                   |                                              |                                            |                                            |                                            |                                  |                                  |                                                  |         :material-check:         |                                    |                                                    |                                                            |                                                        |                                                |                                              |
| [peyote][peyote-id]                    |                                              |                                            |                                            |                                            |                                  |                                  |                                                  |                                  |                                    |                  :material-check:                  |                      :material-check:                      |                                                        |                                                |                                              |
| [rock weed][rock-weed]                 |                                              |                                            |                                            |                                            |                                  |                                  |                                                  |                                  |          :material-check:          |                                                    |                                                            |                    :material-check:                    |                                                |                                              |
| [sand reeker][sand-reeker]             |                                              |                                            |                                            |                                            |                                  |                                  |                 :material-check:                 |                                  |                                    |                  :material-check:                  |                                                            |                                                        |                                                |                                              |
| [snowcrystal petal][snowcrystal-petal] |                                              |                                            |                                            |                                            |                                  |                                  |                                                  |                                  |                                    |                                                    |                                                            |                    :material-check:                    |                                                |                                              |
| [spider ivy][spider-ivy]               |                                              |                                            |                                            |                                            |                                  |                                  |                                                  |         :material-check:         |                                    |                                                    |                      :material-check:                      |                                                        |                :material-check:                |                                              |
| [tangy temerity][tangy-temerity]       |                                              |                                            |                                            |                                            |         :material-check:         |         :material-check:         |                                                  |                                  |                                    |                                                    |                                                            |                                                        |                                                |                                              |
| [waterfinder][waterfinder]             |                                              |                                            |                                            |                                            |                                  |                                  |                                                  |                                  |          :material-check:          |                                                    |                                                            |                                                        |                :material-check:                |                                              |
| [white hemlocks][white-hemlocks]       |                                              |                                            |                                            |                                            |                                  |         :material-check:         |                 :material-check:                 |                                  |                                    |                                                    |                                                            |                                                        |                                                |                                              |
| [windbag][windbag]                     |               :material-check:               |                                            |                                            |                                            |                                  |                                  |                                                  |                                  |          :material-check:          |                                                    |                                                            |                                                        |                :material-check:                |               :material-check:               |

Continue reading: [[herbs]].

[^1]: Acts on the unit, but all the faction's demons in the region use it if there are any left.  
So you only need to equip one unit (per region), as long as it drinks enough peasant blood for all the demons.  
[^2]: You can apply it to a unit with the order `USE Duncebun <unit−id>`.  
The application of the potion fails if the [[stealth]] skill of the acting unit is **less or equal** to the victim's **[perception][skill-perception-id] level + 2**.
In this case, you get an error message and the [duncebun] is not used up (thus it remains to the unit).

<!-- From [https://wiki.eressea.de/index.php?title=Tränke/en&oldid=16929] -->

[cmd-use]: [[cmd-use]]
