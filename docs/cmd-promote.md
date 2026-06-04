---
# cSpell:locale en
alias: cmd-promote
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# PROMOTE

**`PROMOTE`**  

Promotes a unit of your own faction race to **Hero** status.  

Heroes are particularly strong in [[war|combat]].  
**They attack 5 times in each combat round**.  
That's why it's worth promoting units with combat skills to hero status.  

!!! note
    Heroes **do not attack more often** with magic, crossbows or catapults.

If a unit is to be promoted, it requires Silver per person (the faction's total number of people).  
As usual, missing Silver is taken from the [silver pool][the-silver-pool] when there is enough.  

The maximum number of heroes is limited, but increases with faction size.  
The formula for this is: log10((faction size-500)÷50)×20.  

Only people of your own race can be promoted, i.e. neither monsters nor migrants.  
Transport takes place according to `RECRUIT`.  
The number of people after recruiting in the current week is used for both the number of possible heroes and the costs of promotions.  

Units that have been promoted cannot recruit additional people and cannot be merged with other non-hero units.  
There is no order to demote Heroes.  

For those who are lazy about math, here is a table showing how many heroes are available in the faction.  

| People | 557 | 563 | 571 | 580 | 589 | 600 | 612 | 626 | 641 | 659 | 678 | 700 | 724 | 751 | 782 | 816 | 854 | 898 | 946 | 1000 |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:----:|
| Heroes |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  |  20  |

| People | 1062 | 1130 | 1207 | 1293 | 1390 | 1498 | 1620 | 1756 | 1910 | 2082 | 3312 | 5500 | 9392 | 16312 | 28618 | 50500 | 89414 | 158614 | 281671 | 500500 | ... |
|--------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:-----:|:-----:|:-----:|:-----:|:------:|:------:|:------:|:---:|
| Heroes |  21  |  22  |  23  |  24  |  25  |  26  |  27  |  28  |  29  |  30  |  35  |  40  |  45  |  50   |  55   |  60   |  65   |   70   |   75   |   80   | ... |

<!-- From [https://wiki.eressea.de/index.php?title=PROMOTE&oldid=16056] -->
