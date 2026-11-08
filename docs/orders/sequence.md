---
# cSpell:locale en
alias: orders-sequence
---

# Orders sequence

Eressea's orders are evaluated in a fixed sequence. Orders with the same number are executed at the same time or the exact sequence is irrelevant.

1. new default orders are set
2. [`GROUP`][cmd-group], [`MAKE TEMP`][cmd-make]
3. [`NAME`][cmd-name], [`DESCRIBE`][cmd-describe], [`GUARD NOT`][cmd-guard], [`HELP`][cmd-help], [`COMBAT`][cmd-combat], [`COMBATSPELL`][cmd-combatspell], [`HIDE`][cmd-hide], [`ORIGIN`][cmd-origin], [`SHOW`][cmd-show]
4. [`BANNER`][cmd-banner], [`EMAIL`][cmd-email], [`OPTION`][cmd-option], [`PASSWORD`][cmd-password]
5. [`CONTACT`][cmd-contact]
6. [`MESSAGE`][cmd-message]
7. [`ENTER`][cmd-enter]; 1st attempt
8. [`USE`][cmd-use]
9. [`LEAVE`][cmd-leave]
10. [`ENTER`][cmd-enter]; 2nd attempt
11. [`ATTACK`][cmd-attack]
12. [`RESERVE`][cmd-reserve], [`CLAIM`][cmd-claim]
13. [`ENTER`][cmd-enter]; 3rd attempt
14. [`GIVE CONTROL`][cmd-give]
15. [`FORGET`][cmd-forget]
16. [`GIVE`][cmd-give]
17. [`RECRUIT`][cmd-recruit][^1]
18. [`DESTROY`][cmd-destroy]
19. [`FOLLOW`][cmd-follow] is set
20. [`PROMOTE`][cmd-promote]
21. [`PAY NOT`][cmd-pay-not]; stops operation and maintenance costs for the corresponding building.
22. maintenance costs for buildings are accounted for. If they cannot be raised, the building has no effect for that turn!
23. [`QUIT`][cmd-quit]
24. [`CAST`][cmd-cast]
25. [`TEACH`][cmd-teach]
26. [`LEARN`][cmd-learn]
27. [`MAKE TEMP`][cmd-make][^1]
28. [`RESEARCH`][cmd-research], [`PLANT`][cmd-plant], [`SPY`][cmd-spy], [`GROW`][cmd-grow]
29. [`ENTERTAIN`][cmd-entertain][^1]
30. [`WORK`][cmd-work][^1]
31. [`TAX`][cmd-tax][^1]
32. [`BUY`][cmd-buy][^1]
33. [`SELL`][cmd-sell][^1]
34. [`STEAL`][cmd-steal][^1]
35. ships with insufficient crew suffer damage
36. ENTER; 4th attempt
37. [`MOVE`][cmd-move] and [`ROUTE`][cmd-route], including [`RIDE`][cmd-ride] and [`CARRY`][cmd-carry] are executed, and units ordered to FOLLOW other units do so
38. [`GUARD`][cmd-guard]; this only works if the unit has not moved.
39. ships drift on the high seas
40. [`DEFAULT`][cmd-default]
41. empty units are removed
42. peasants, horses and trees grow, if possible; the remaining peasants move into other regions
43. silver for units maintenance is subtracted
44. [`SORT`][cmd-sort]
45. [`NUMBER`][cmd-number]

[^1]: Orders marked like this are divided "fairly"; see [notes][notes] below.

However, the orders do not necessarily have to be entered in this order.  
It is perfectly permissible to enter the following:

```text
GIVE TEMP 5300 Silver
MAKE TEMP 5
    RECRUIT 1
    COMBAT NOT
    LEARN FORESTRY
END
```

Here the orders sequence is: The new unit is first created, no longer joins combats, receives 300 silver, recruits 1, and finally learns forestry - although this is not the sequence in which the orders were written.

## Notes

Orders of the same rank from different units are normally processed in the sequence in which they appear in the report.  
For example, first all GIVE orders of the first unit, then all `GIVE` orders of the second unit, then all `RECRUIT` orders of the first unit, then the second and so on.  
The [items pool][items-pool] also usually works in this way: units higher up in the region are first "asked" if the can share a certain item.  
However, this sequence can be changed by certain orders.  
These include `ENTER, LEAVE, MAKE TEMP, GIVE CONTROL` and `GIVE SHIP`.  
The exact behavior is not guaranteed! Therefore, if in doubt, give orders in such a way that the unit sequence does not matter.  

For orders where the result has an upper limit, for example the maximum number of trees in the region for `MAKE wood`, the maximum number of recruits to `RECRUIT` or the region's money for `ENTERTAIN` and `TAX`, it may happen that several units are in competition.  
In this case, we try to distribute the scarce good in proportion to the quantity that each unit could produce if it were unlimited.  
In this case, there may be gaps and a unit may end up with nothing.  
The `SELL`, `BUY` and `WORK` orders are also affected.  

About `ENTER` 1st/2nd/3rd/4th attempt  
This means that you can still enter a castle before an attack.  
After the fight, a unit may try to enter again, as the former owner might be dead or has fled in the meantime.  

It does not mean that units leaving a ship can still attack in the same turn, as the server remembers who left ships and intercepts it accordingly.

## See also

- [orders][orders]
- [short description][list-of-orders]
<!-- TODO: check -->
<!-- - [short description DE/EN]-->

Continue reading: [Short Description][list-of-orders].

<!-- From [https://wiki.eressea.de/index.php?title=Befehlsreihenfolge/en&oldid=13988] -->

[cmd-attack]: [[cmd-attack]]
[cmd-banner]: [[cmd-banner]]
[cmd-buy]: [[cmd-buy]]
[cmd-carry]: [[cmd-carry]]
[cmd-cast]: [[cmd-cast]]
[cmd-claim]: [[cmd-claim]]
[cmd-combat]: [[cmd-combat]]
[cmd-combatspell]: [[cmd-combatspell]]
[cmd-contact]: [[cmd-contact]]
[cmd-default]: [[cmd-default]]
[cmd-describe]: [[cmd-describe]]
[cmd-destroy]: [[cmd-destroy]]
[cmd-email]: [[cmd-email]]
[cmd-enter]: [[cmd-enter]]
[cmd-entertain]: [[cmd-entertain]]
[cmd-follow]: [[cmd-follow]]
[cmd-forget]: [[cmd-forget]]
[cmd-give]: [[cmd-give]]
[cmd-group]: [[cmd-group]]
[cmd-grow]: [[cmd-grow]]
[cmd-guard]: [[cmd-guard]]
[cmd-help]: [[cmd-help]]
[cmd-hide]: [[cmd-hide]]
[cmd-learn]: [[cmd-learn]]
[cmd-leave]: [[cmd-leave]]
[cmd-make]: [[cmd-make]]
[cmd-message]: [[cmd-message]]
[cmd-move]: [[cmd-move]]
[cmd-name]: [[cmd-name]]
[cmd-number]: [[cmd-number]]
[cmd-option]: [[cmd-option]]
[cmd-origin]: [[cmd-origin]]
[cmd-password]: [[cmd-password]]
[cmd-pay-not]: [[cmd-pay-not]]
[cmd-plant]: [[cmd-plant]]
[cmd-promote]: [[cmd-promote]]
[cmd-quit]: [[cmd-quit]]
[cmd-recruit]: [[cmd-recruit]]
[cmd-research]: [[cmd-research]]
[cmd-reserve]: [[cmd-reserve]]
[cmd-ride]: [[cmd-ride]]
[cmd-route]: [[cmd-route]]
[cmd-sell]: [[cmd-sell]]
[cmd-show]: [[cmd-show]]
[cmd-sort]: [[cmd-sort]]
[cmd-spy]: [[cmd-spy]]
[cmd-steal]: [[cmd-steal]]
[cmd-tax]: [[cmd-tax]]
[cmd-teach]: [[cmd-teach]]
[cmd-use]: [[cmd-use]]
[cmd-work]: [[cmd-work]]
