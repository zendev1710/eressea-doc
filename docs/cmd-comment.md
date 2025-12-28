---
# cSpell:locale en
alias: cmd-comment
---
# ; COMMENT

The semicolon “;” is used in Eressea orders to mark (temporary) comments.
Some of these comments are inserted "automatically".
For example, the standard [[orders|orders template]] always contains the names of regions and units, the number of people and their silver supply as a comment.
In addition, comments are also used to provide the [[echeck]] program with certain information, such as wages in a region.

```text
ERESSEA abcd "Enter password here"
; ECHECK -l -w4 -r90 -v4.01
REGION 85,-48 ; Darkland
  ; ECheck Salary 15
UNIT ub2;    Handyman [3,30$]
    LEARN forestry
    // LEARN Shipbuilding AT T2 or T3
```

If you use the [[vorlage]] program to create an orders template, a variety of information is transmitted to the player via these comments:

```text
REGION 85,-48 ; Darkland (Plain, 290 people, $4270 Silver)
; ECheck Salary 15
;  . .  |Farms: 8534 +9|Silver: 47588297 +48400|Upkeep: 2379414 +2420|
; . E w |Recruits: 213 +0|Horses: 2532 -8|Profit: 51204 +54|
;  . .  |pl. free: 1466 -9|                       |                        |
;       |Spice: 125 +0|Jewel: 175 +0|Myrrh: 125 +0|
;       |Oil: 75 +0|Silk: 150 +0|Incense: 100 +0|
; Prod.: Balm: -4 +0 max. tradeable: 85
; Street (100%) to the east
; Region income: 2660 Silver
; Food costs:    2900 Silver
; Material pool: 4270 Silver, 1 Speer
; -   -   -   -   -   -   -   -   -   -   -   -
; In an open field:
UNIT ub2;  Handyman [3,0$] flieht
; Weight: 60.00GE Walking: 32.40GE/32.40GE
; Forestry 2
    LEARN Forestry
    // LEARN Forestry On T3
```

The player himself can also insert comments after a semicolon.
However, since these comments are not included in next week's template, permanent comments after [[comment-with-slashes|`//`]] usually make more sense.

To save transmission capacity, temporary comments can be removed before sending the orders.
Some tools do this, like [[magellan]] or VPP.

## External links

- [Vorlage and VPP on Gulrak.de]

<!-- From [https://wiki.eressea.de/index.php?title=;&oldid=16702] -->

[Vorlage and VPP on Gulrak.de]: http://www.gulrak.de/eressea/tools.html
