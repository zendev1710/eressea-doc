---
alias:
    name: alchemy
    text: Alchemy
---
# Potions

Alchemical *potions* are prepared using [[herbs]] and other ingredients, and can then be used by any unit. To make a potion, you need units with the skill [Alchemy], and to find the required herbs, you need units with the skill [Herbalism].

Potions are make with the order [[cmd-make]]`"potion_name"`. Each potion requires several ingredients. Recipes are given each time you reach the level required to concoct them. Later, you can find them using the [[cmd-show]] command. To be able to make a potion, the alchemist's level must be twice as high as the potion's level. Each turn, an alchemist can make (skill level)/(potion level\*2) potions. A level 6 alchemist can therefore make a maximum of one level 3 potion, one level 2 potion or three level 1 potions.

If you want to use a potion, you do so with order [[cmd-use]]`[amount] "potion_name" [unit ID]`. Unit ID is required only for Duncebun potion. A potion cannot be divided between several units. However, a large unit can be divided into several smaller units after the potion has been used, retaining its effects.

Most potions give their benefits to the unit giving the order. Exceptions are potions which affect a region -then the region where the unit was at the beginning of turn is affected- or those that affect other units (Duncebun potion).

Usually a potion affects 10 people or 10 goods during the turn it is used, as mentioned in its recipe. Potions that affect a unit's items expire if they cannot be used because the unit no longer has these items. Many potions work in such a way that too many people in the unit make no difference, i.e. with 12 people and a potion (works for 10) the effect only affects 10 of the 12 people. This is not possible with "berserks blood" potion, as the persons do not act as a unit in battle. Here it is necessary that all persons in the unit have the effect of the potion before the fight, otherwise it will not work!

The "residual effect" of potions does not expire with all potions, so that, for example, a person can benefit from the effect of a “Brain wax” or “busybeers” for ten weeks after using it.

## Potions list

Potions list

|       |      |                       |                                                                        |                                                                                         |                    |
|-------|------|-----------------------|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------|
| Level | Abbr | Name                  | Ingredients                                                            | Description                                                                             | Target             |
| 1     | Sm   | Seven mile tea        | cobalt fungus, windbag                                                 | 10 men on foot can travel as fast as if mounted                                         | Unit               |
| 1     | Gw   | Goliath water         | bugleweed, fjord fungus                                                | 10 men can carry as much as 10 horses                                                   | Unit               |
| 1     | WL   | Water of life         | elvendear, knotroot                                                    | Transforms 10 pieces of wood or Mallorn into 10 mallorn/saplings                        | Region             |
| 1     | TW   | Potion of truth       | flatroot, fjord fungus                                                 | This potion hasn't had a function for a long time                                       | Region             |
| 2     | St   | Busybeer              | mandrake, gapgrowth, tangy temerity                                    | Doubles the productivity of 10 men when using `MAKE` order                              | Unit               |
| 2     | Ws   | Ointment              | cobalt fungus, white hemlock, tangy temerity                           | Heals up to 400 hit points                                                              | Unit               |
| 2     | Ba   | Peasant blood         | cave lichen, fjord fungus, cobalt fungus, Peasant                      | Up to 100 demons can do without killing peasants                                        | Unit\*             |
| 3     | Gs   | Brain wax             | waterfinder, rock weed, windbag, bugleweed                             | Increases the chances for up to 10 men of learning a skill                              | Unit               |
| 3     | Db   | Duncebun              | owlsgaze, spider ivy, cave lichen, fjord fungus                        | for 10 people: no learning or teacher brings nothing or forget 1 week of the best skill | (foreign) Unit\*\* |
| 3     | Nw   | Potion of nest warmth | ice begonia, spider ivy, gapgrowth, peyote                             | Allows insects to recruit men even in winter                                            | Region             |
| 3     | Pg   | Horsepower potion     | cobalt fungus, sand reeker, peyote, knotroot                           | 50 horses give birth to up to 4 foals                                                   | Region             |
| 3     | Be   | Berserkers blood      | white hemlock, mandrake, flatroot, sand reeker                         | 10 men receive a +1 attack modifier in combat                                           | Unit               |
| 4     | Bl   | Peasant love potion   | mandrake, snowcrystal petal, rock weed, bubblemorel, elvendear         | 1000 peasants grow twice as fast as usual                                               | Region             |
| 4     | EM   | Elixir of power       | elvendear, waterfinder, windbag, spider ivy, bubblemorel, Dragon blood | 10 men get 5 times their normal hit points                                              | Unit               |
| 4     | Ht   | Healing potion        | bugleweed, windbag, ice begonia, elvendear, gapgrowth                  | one person survives otherwise fatal damage; only possible once per person per week      | Unit               |

\* Acts on the unit, but all the faction's demons in the region use it if there are any left. So you only need to equip one unit (per region), as long as it drinks enough peasant blood for all the demons.

\*\* You can apply it to a unit with the order USE "Duncebun" &lt;unit−id&gt;. The application of the potion fails if the STEALTH skill of the acting unit is less or equal to the victim's PERCEPTION+2. In this case, you get an error message and the Dumpfbackenbrot is not used up (thus it remains to the unit).

## Herbs Table

| Herb              | TW | Sm | Gw | WL | Ba | St | Ws | Be | Db | Gs | Pg | Nw | Bl | EM | Ht |
|-------------------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| flatroot          | X  |    |    |    |    |    |    | X  |    |    |    |    |    |    |    |
| tangy temerity    |    |    |    |    |    | X  | X  |    |    |    |    |    |    |    |    |
| owlsgaze          |    |    |    |    |    |    |    |    | X  |    |    |    |    |    |    |
| spider ivy        |    |    |    |    |    |    |    |    | X  |    |    | X  |    | X  |    |
| cobalt fungus     |    | X  |    |    | X  |    | X  |    |    |    | X  |    |    |    |    |
| elvendear         |    |    |    | X  |    |    |    |    |    |    |    |    | X  | X  | X  |
| bugleweed         |    |    | X  |    |    |    |    |    |    | X  |    |    |    |    | X  |
| knotroot          |    |    |    | X  |    |    |    |    |    |    | X  |    |    |    |    |
| bubblemorel       |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  |    |
| waterfinder       |    |    |    |    |    |    |    |    |    | X  |    |    |    | X  |    |
| peyote            |    |    |    |    |    |    |    |    |    |    | X  | X  |    |    |    |
| sand reeker       |    |    |    |    |    |    |    | X  |    |    | X  |    |    |    |    |
| windbag           |    | X  |    |    |    |    |    |    |    | X  |    |    |    | X  | X  |
| fjord fungus      | X  |    | X  |    | X  |    |    |    | X  |    |    |    |    |    |    |
| mandrake          |    |    |    |    |    | X  |    | X  |    |    |    |    | X  |    |    |
| rock weed         |    |    |    |    |    |    |    |    |    | X  |    |    | X  |    |    |
| gapgrowth         |    |    |    |    |    | X  |    |    |    |    |    | X  |    |    | X  |
| cave lichen       |    |    |    |    | X  |    |    |    | X  |    |    |    |    |    |    |
| ice begonia       |    |    |    |    |    |    |    |    |    |    |    | X  |    |    | X  |
| white hemlock     |    |    |    |    |    |    | X  | X  |    |    |    |    |    |    |    |
| snowcrystal petal |    |    |    |    |    |    |    |    |    |    |    |    | X  |    |    |

Continue reading: [[herbs]].

<!-- From [https://wiki.eressea.de/index.php?title=Tränke/en&oldid=16929] -->

[Alchemy]: ./skills-list.md#alchemy
[Herbalism]: ./skills-list.md#herbalism
