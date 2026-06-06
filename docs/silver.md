---
# cSpell:locale en
alias: money
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD042 MD052 -->
# Money

!!! note "Note"
    In Eressea, the basic unit of the monetary system is the **silver**.

Money makes the world go round; even in Eressea. Many different ways to earn money exist in Eressea: You can earn money by: [working], [entertaining] the peasants, [collecting taxes], or [trading].

Working is more of a type of stopgap, units working will earn barely enough to feed themselves. You can make quite a lot of money with entertainment and taxation. Especially at the beginning of your ventures, trading might be the biggest source of income, profits of some thousands of silver are possible, provided the regions have the appropriate luxury goods.

Silver has a weight: each 100 pieces of silver equal one unit of weight (UW/lbs). There is no rounding: even one piece of silver above your carrying limit can overload.

Because persons (of most [[races]]) can carry 5.4 UW/lbs, they can carry up to 540 silver with them; when carrying 541 silver a single person is overloaded. A boat (50 UW/lbs capacity), for example, can carry one person (10 lbs for most [[races]]) with 4000 Silver; even 4001 silver would be too much.

## Expenses

### Recruiting

If you want to [recruit] people, all you need is enough small change, because those willing to be recruited are often particularly thirsty. Depending on the race, you have to spend between 40 and 150 silver as recruitment costs for each person you recruit. The amount of the recruitment costs depends on the race and can be found in the [[races|modifiers table]].

Recruitment is prevented by guarding.

### Upkeep costs

Every person of a faction and each peasant require 10 silver each turn to buy themselves the supplies needed to survive.
Units of a faction help each other with silver when staying in the same region, i.e. it is basically enough if one unit has enough silver for all persons present (which can lead to catastrophes when done wrong and nobody else has any silver!). If your own faction does not have enough silver, other factions that have set [[cmd-help|HELP SILVER]] to your own faction will also help (see [[alliances]]).
Units that move must be supplied where they arrive. Silver, which was previously [reserved], is also used for unit maintenance.
Without enough silver, people will starve (see below).

Some buildings also require a weekly maintenance cost in order to function. These maintenance costs are incurred at the start of the round, i.e. they must be collected in the preliminary round and are due as soon as the building has been started (i.e. even for half-finished buildings). If there is not enough silver available, the function of the building cannot be used. More details can be found in the chapter on [buildings].

## Starvation

### Starvation for player units

Starving units take damage, i.e., they lose hit points. The hungry Halflings proportionally more than others. The health status of the unit can be seen in the report. Here, the unit is displayed as exhausted, wounded or badly wounded. However, a fully rested unit will not die of starvation in the first week.

A starving unit cannot give people to other units. In addition, the skill levels of starving units are reduced by half, they do not regenerate health points and they learn much more slowly than normal. Starving or wounded units can, however, still execute orders.

Over time, wounded units recover. Units normally regenerate 5% (some races more) of their maximum hit points per round, but at least one point per person in the unit. Undead units do not regenerate.

The sailing skill is only reduced by one level when units are starving. Nevertheless, starvation at sea is a critical situation. On the one hand, nobody can work there except [aquarians][aquarians], so you are dependent on silver from outside. Secondly, due to the reduction in skill, you may not be able to gather enough sailing levels to maneuver the ship, causing it to take [damage] and drift away.

Hunger is almost fatal if you come into contact with the enemy, e.g. due to theft or poor planning. Units lose hit points and will be much weaker in any subsequent battle. If units survive such a battle anyway, there is still a risk that they will continue to starve because they were unable to work due to the battle (see [combat end][the-end]).

If units master the [endurance][skill-endurance-id] skill at a high level, they may experience the strange effect that a unit is "very strong" according to the report (i.e. it has more hit points than it should normally have) after starving.

### Starvation for peasants

Peasants also need sustenance, which they normally earn themselves and take from the regional supply. If the regional supply is exhausted, the peasants starve and die. This can have various causes:

- The region is overpopulated. In a plain without trees, where each peasant earns 12 silver, only 12000 peasants can survive in the long term, because only 10000 peasants work, earning 120000 silver, which is only enough for 12000 peasants. In the short term, the number of peasants can be higher as long as there is still enough silver in the region's supply.
- The region is not overpopulated, but [working] player units occupy some of the jobs.
- The peasants earn enough silver, but player units collect [taxes][collecting taxes] before the peasants can provide for themselves.
- There are also rumors of special events that can temporarily or permanently reduce the fertility of a region, which means that the peasants can no longer earn their own living.

Starved peasants can later be resurrected as [undead][undead].

## Income

### Work

Units can earn money by working in agriculture (see [[cmd-work]]).
However, the larger the forests in a region, the less arable land there is, and the fewer peasants (and player units) can work: eight peasants or players can no longer work per tree, each sapling occupies 4 jobs.
The maximum number of people who can work (not live) in a region, i.e. without any forest, depends on the terrain (see the table in the [[cmd-work]] order page).

A peasant normally earns 11 silver per turn. This wage can be increased by the bonus of a citadel to up to 16 silver per peasant and week (see also the [castles table][castles-overview-id]). If, for example, a citadel is built in a plain and the forest is cut down, 10000 peasants can feed themselves in one turn and another 60000 silver are added to the region silver.

However, working units of players earn less - after all, they are only auxiliaries. How much they can earn (usually 1 silver less than peasants) is specified in the report and can also be found in the table in the [WORK order page][`WORK`].

Work is prevented by guarding only for units working on ships.

### Collecting taxes

Armed and trained henchmen can use the order [[cmd-tax]][collecting taxes] to squeeze 20 silver in taxes per person and skill taxation level out of the peasants.
To do this, you will of course need the taxation skill, as well as one weapon per person (catapults don't count) and at least one level of the corresponding weapon skill.

If the peasants live close to the maximum population, almost all the silver reserves will be used up by themselves, so they will have no more silver "left" for taxes.
Taxes can then still be collected (up to the amount in the regional reserve), but the peasants who are not supplied at the end of the round will starve to death (which will not increase their earnings either ...).
This is why it makes sense to build a castle, as this increases wages: with 12 silver instead of 11 silver, 2000 peasants earn 2000 silver more per turn!

Collecting taxes is prevented by guarding.

[](){ #silver-entertainment-id }

### Entertainment

The silver that remains to peasants after paying taxes is added to the region's silver (the peasants' silver supply, so to speak).
Of this silver, 5% can be earned through entertainment. This amount is also stated in the region's statistics.
Each person can earn up to 20 silver per round and talent level in entertainment with the [[cmd-entertain]][entertaining] order if the peasants have enough money available.

### Examples of potential income

*Income and upkeep.*

| Region | Trees | Peasants | Max. workers | Wage | Income | Upkeep | Surplus | Entertain |
|--------|------:|---------:|-------------:|-----:|-------:|-------:|--------:|----------:|
| Plain  |   200 |     3742 |         8400 |   11 |  41162 |  37420 |    3742 |       187 |
| Plain  |   200 |     3742 |         8400 |   14 |  52388 |  37420 |   14968 |       748 |
| Forest |   818 |     3742 |         3456 |   11 |  38016 |  37420 |     596 |        29 |
| Forest |   818 |     3742 |         3456 |   12 |  41472 |  37420 |    4052 |       202 |

For each tree, the maximum number of peasants that may work is decreased by 8, for each sapling the number is decreased by 4.

In the last example of the table, the total income is decreased because not all the peasants can work.
This is because too many trees are preventing them from growing food.

The values in the table do not account for the peasants' savings (region silver reserve).
They will live on this reserve when overpopulation strikes.
The silver available for entertainment is also affected by the amount in the silver reserve.
As a rule, more silver can therefore be earned through entertainment, as the 5% refers to this reserve.

Entertainment is prevented by guarding only for entertaining units on ships.

### Stealing: the dishonest way

In addition to the honest ways of earning money, there is also the dishonest variant: theft. Units that with stealth can attempt to steal silver from other units using the [[cmd-steal]] order.

If the [stealth skill] of the stealing unit is higher than the [perception][skill-perception-id] of the best unit in the region of the faction they are stealing from, they earn 50 silver per skill level difference.

It is also worth reading the chapter on [stealth][stealth skill] about this topic.

[](){ #silver-trade-id }

## Trade

In every region, the peasantry produce one special luxury item.
Your units may purchase this product.
In all regions that do not produce this special luxury product, there is a continuously rising demand.
If you are not afraid of the risks involved in long distance travels, trading is a very lucrative method of earning silver.

In order to trade, a unit needs the trade skill.
For every level of trade skill, a person can [[cmd-buy]] up to 10 luxury items or sell 10 luxury items. The respective numbers of traded goods can be selected completely freely.
For example, a unit consisting of a person with skill level 4 in trading can buy 20 gems and sell 12 silk and 8 balm in one round.

Furthermore, some form of castle is required for the trade to take place. At least the size level of a tradepost is required.
It does not matter who controls the castle, the owner cannot directly prevent the trading from taking place.
However, they can indirectly prevent trading by simply attacking the trading units with their own armed units.

The unit that owns the largest castle in the region receives a percentage of the proceeds of all sales by the other factions.
This revenue share is deducted from the trader's income. If two castles in the region are the same size, no one receives this share. The amount of the "tax rate" can be found in the table in the [castles] chapter.

Trade is prevented by guarding only for trading units on ships.

Every type of trade good has a certain base price (see table below). The number of luxury goods that can be bought without raising this price is 1% of the number of peasants in the region. Every time this amount is bought (the total bought by all factions), the price is increased by the base price. A region with 2,000 peasants means that 20 luxury items can be bought without raising the price. The price drops to normal the next turn.

*Base prices of luxury goods.*

| Luxury good | Base price | Weight UW/lbs |
|-------------|------------|---------------|
| balm        | 4          | 2             |
| oil         | 3          | 3             |
| spice       | 5          | 2             |
| silk        | 6          | 3             |
| gem         | 7          | 1             |
| incense     | 4          | 2             |
| myrrh       | 5          | 2             |

The selling price of a luxury item in a region is a multiple of the basic price, and is declared in the report of the region. Each time more than 1% of the peasants has bought a certain good, the selling price drops by the basic price and rises again slowly in the following turns. Each turn, there is a 10% chance for each luxury good that its selling price is increased by its basic price. In regions with a [harbour][harbour], this chance is 20%. If the selling price is already 25 times the base price, it will not increase any further.

The prices and maximums shown are valid for all factions in the region and not per faction, but per luxury product. Without trade agreements between players, the selling prices of luxury goods can be "messed up" faster than you would like ...

All purchases and sales of luxury goods are distributed equally among the factions. The price increase or decrease therefore affects everyone who buys or sells in the turn equally.

Examples:

- Let's assume a region with 8,000 peasants that offers incense for 4 silver, and buys spice for 15 silver. 1% of the peasants is 80. If all the traders in the region sell 200 spices, the first 80 units are sold for 15 silver a piece, the next 80 units are sold for 10 silver a piece (down one base price for spice), and the last 40 spice are sold for only 5 silver a piece. The next week, spices will be sold for only 5 silver. Unless the price has already risen to 10 again (10% probability, 20% with a harbour).

- If 100 incense is bought in the same region, the first 80 are bought at 4 silver a piece, and the next 20 are bought at 8 silver a piece (an increase of one basic price). In the coming week the price for incense will be 4 silver again and you can buy the first 80 incense for this price. If the 100 incense was purchased by units from two different factions, both pay approximately 4.8 silver per luxury good (disregarding rounding effects).

The silver spent by peasants to buy the luxury goods benefits the selling traders. Nevertheless, the region does not lose any silver, because the peasants own luxury goods with which they can pay the taxes. The money is not created out of nothing - it is the value of goods produced in another region. The silver spent by BUY, on the other hand, goes into the region's supply. Clever rulers can take it back from them through entertainment and taxes.

It's worth equipping a ship and setting sail. Although it is possible to trade with the two products usually produced on an island, the profits remain relatively low. On the other hand, if you return from a foreign island with a cargo of rare goods, you can make astronomical profits, whatever the distance between the islands. Remember that a tradepost is a prerequisite for any trade, so if you equip an expedition to a new world, make sure to account for that.

### Luxury goods

#### Balm

#### Gem

#### Incense

#### Oil

#### Myrrh

#### Silk

#### Spice

## Competition between different factions

If several factions work, maintain, collect taxes or trade in a region, the possible income is divided as evenly as possible between the units. It is best to consult with your neighbors, provided that they are friendly.

If the region is guarded by a foreign faction, your own unit cannot collect taxes or recruit. Work, entertainment and trade are possible, however, unless your own unit is on a ship.

If all guarding factions have set [[cmd-help|`HELP GUARD`]] or [[cmd-help|`HELP ALL`]] to our faction or [[cmd-contact]] to our unit or our faction, then guarding has no effect. This also applies if our unit is not seen due to a sufficiently good stealth skill. For a TEMP unit (particularly relevant when recruiting), the "mother" unit counts, i.e. the unit that gives the command `MAKE TEMP`.

## See also

- [[cmd-give]]
- [[cmd-reserve]][reserved]
- [[cmd-recruit]]
- [Item pool]
- [Stealth][stealth skill]
- [[cmd-guard]]

Continue reading: [Material pool].

[Material pool]: ./items-pool.md

<!-- From [https://wiki.eressea.de/index.php?title=Geld/en&oldid=16779] -->

[collecting taxes]: ./cmd-tax.md
[working]: ./cmd-work.md
[entertaining]: ./cmd-entertain.md
[recruit]: ./cmd-recruit.md
[reserved]: ./cmd-reserve.md
[buildings]: ./buildings.md
[damage]: ./ships.md
[`WORK`]: ./cmd-work.md
[stealth skill]: ./stealth.md
[castles]: ./castles.md
[Item pool]: ./items-pool.md

[trading]: #trade
