---
# cSpell:locale en
alias: cmd-buy
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# BUY

*`BUY` is like [[cmd-sell]], a [pseudo-long order][short-and-long-orders][^1].*  

**`BUY <number> <luxury-good>`**  

If the unit has the [trade skill][skill-trade-id], it will attempt to purchase that number of luxury goods.
This is only possible if, firstly, there is a trading post or a larger type of castle in the region near which the market can be held, and secondly, if the product is actually produced in the region.
In order to buy something, no contact with the lord of the castle is necessary;  
Nevertheless, it is of course more diplomatic to ask beforehand...

`BUY` orders are generally given `SELL` executed.  
`BUY` orders have priority over sales.  
So you cannot use the earnings from sales directly in the same round for new purchases.  
It also means that units without enough skill to execute all `BUY` and `SELL` orders first buy as much as possible and if there are no skill points left for selling.  

<!-- TODO:check if it's Jewel or gem  -->
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
In the computer report and the [orders template][orders] are all `BUY` and `SELL` orders listed.  

[^1]: You can implement a total of skill level (trading) x 10 luxury goods, but you cannot give any other long orders.  

## See also

- [trade][silver-trade-id]
- [[cmd-sell]]

<!-- From [https://wiki.eressea.de/index.php?title=BUY&oldid=16746] -->
