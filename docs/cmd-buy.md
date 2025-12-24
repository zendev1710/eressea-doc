---
# cSpell:locale en
alias: cmd-buy
---
# BUY

**`BUY`**[<sup>`(l)`</sup>]` `*`number`*` `*`luxury goods`*  

If the unit has the [trade] skill, it will attempt to purchase that number of luxury goods.
This is only possible if, firstly, there is a trading post or a larger type of castle in the region near which the market can be held, and secondly, if the product is actually produced in the region.
In order to buy something, no contact with the lord of the castle is necessary; Nevertheless, it is of course more diplomatic to ask beforehand...

[<sup>(l)</sup>][<sup>`(l)`</sup>] `BUY` is like [[cmd-sell]] a ["pseudo-long" command]. You can implement a total of skill level (trading) x 10 luxury goods, but you cannot give any other long orders.
BUY orders have priority over sales.
`BUY` orders are generally given `SELL` executed, so you cannot use the earnings from sales directly in the same round for new purchases.
It also means that units without enough talent to execute all `BUY` and `SELL` orders first buy as much as possible and if there are no skill points left for selling.

Example:

    ```text
    UNIT hndl;     Barker [1, $1000]
        ; Trade 3 [180]
        SELL 15 Jewel
        SELL 15 Oil
        BUY 10 Incense
    ```

This merchant will buy 10 incense and sell a total of 20 jewels and oil.
So randomly between 5 and 15 per trade item if he has it.

Only one order appears in the normal report.
But this is only so that there is not a large list of orders there.
In the computer report and the [[orders|orders template]] are all `BUY` and `SELL` orders listed.

## See also

- [trade]
- [[cmd-sell]]

<!-- From [https://wiki.eressea.de/index.php?title=BUY&oldid=16746] -->

[<sup>`(l)`</sup>]: ./commands.md#short-and-long-orders
[trade]: ./silver.md#trade
