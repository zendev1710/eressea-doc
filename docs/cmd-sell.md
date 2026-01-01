---
# cSpell:locale en
alias: cmd-sell
---
# SELL

**`SELL`**[<sup>`(l)`</sup>]` `*`number`*` `*`Luxury item`*  
**`SELL`**[<sup>`(l)`</sup>]` ALL `*`Luxury item`*  

The unit skilled in [trading] can use this order to sell luxury goods that it owns to the farmers.
This is only possible if, firstly, there is a trading post or larger [[castles|castle type]] in the region near which the market can be held, and secondly, if there is any demand for the product at all.
In order to sell something, no contact with the lord of the castle is necessary; Nevertheless, it is of course more diplomatic to ask beforehand...

With `SELL ALL` is sold as much as the demand in the region.
This also works if the trading volume drops in the same week (e.g. due to recruitment).
However, the order should not be given to more than one unit per region or even by several factions: as soon as several units in the region have SELL orders, it is no longer guaranteed what will happen `SELL ALL` happened.

[<sup>(l)</sup>][<sup>`(l)`</sup>] `SELL` is, like [[cmd-buy]], a [[orders|"pseudo-long" order]].

You can choose a total skill level (acting) x sell and buy 10 luxury goods, but do not give any other long orders.
BUY orders have priority over sales. `BUY` orders are generally given `SELL` executed, so you cannot use the earnings from sales directly in the same round for new purchases.
It also means that units without enough skill to execute all `BUY` - and `SELL` orders first buy as much as possible and if there are no skill points left for selling.

Only one order appears in the normal report.
But this is only so that there is not a large list of orders there.
In the computer report and the [[orders|move template]] are all`BUY` - and `SELL` - orders listed.

## See also

- [trading]
- [[cmd-buy]]

<!-- From [https://wiki.eressea.de/index.php?title=SELL&oldid=16784] -->

[<sup>`(l)`</sup>]: ./commands.md#short-and-long-orders
[trading]: ./silver.md#trade
