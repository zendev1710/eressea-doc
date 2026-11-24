---
# cSpell:locale de
alias: kriegstabellen
---

[](){ #tabellen-kampf-id }

# Kriegstabellen

Nur aggregierte Kampfwerte. Regeln und Formeln stehen unter [Krieg][krieg].

[](){ #tabelle-waffen-id }

## Waffeneigenschaften

<div class="sortable" markdown="1">

| Waffe               | Schaden/Fuß |    ⌀ | Schaden/Pferd |    ⌀ |  OB |  DB | Talent | Summe |
| ------------------- | ----------- | ---: | ------------: | ---: | --: | --: | :----: | ----: |
| Katapult[^1]        | 3d10+5      | 21,5 |        3d10+5 | 21,5 |  -4 |   0 |   K    |    -4 |
| Armbrust[^2]        | 3d3+5       |   11 |         3d3+5 |   11 |   0 |   0 |   A    |     0 |
| Mallornarmbrust[^2] | 3d3+6       |   12 |         3d3+6 |   12 |   0 |   0 |   A    |     0 |
| Bogen               | 1d11+1      |    7 |        1d11+1 |    7 |  -2 |   0 |   B    |    -2 |
| Mallornbogen        | 1d11+2      |    8 |        1d11+2 |    8 |  -2 |   0 |   B    |    -2 |
| Elfenbogen          | 2d6+4       |   11 |         2d6+4 |   11 |  -2 |   0 |   B    |    -2 |
| Speer               | 1d10        |  5,5 |        1d12+2 |  8,5 |   0 |   0 |   S    |     0 |
| Mallornspeer        | 1d10+1      |  6,5 |        1d12+3 |  9,5 |   0 |   0 |   S    |     0 |
| Hellebarde          | 2d6+3       |   10 |         2d6+3 |   10 |  -1 |  +2 |   S    |    +1 |
| Lanze               | 1d5         |    3 |         2d6+5 |   12 |   0 |  -2 |   S    |    -2 |
| Mallornlanze        | 1d5+1       |    4 |         2d6+6 |   13 |   0 |  -2 |   S    |    -2 |
| Schwert             | 1d9+2       |    7 |         1d9+2 |    7 |   0 |   0 |   H    |     0 |
| Bihänder            | 2d8+3       |   12 |         2d8+3 |   12 |  -1 |  -2 |   H    |    -3 |
| Kriegsaxt           | 2d6+4       |   11 |         2d6+4 |   11 |  +1 |  -2 |   H    |    -1 |
| Laenschwert         | 3d6+10      | 20,5 |        3d6+10 | 20,5 |  +1 |  +1 |   H    |    +2 |
| Adamantiumaxt       | 3d4+15      | 22,5 |        3d4+15 | 22,5 |  +2 |  -2 |   H    |     0 |
| Flammenschwert      | 3d6+10      | 20,5 |        3d6+10 | 20,5 |  +1 |  +1 |   H    |    +2 |
| Rostige Hellebarde  | 2d6         |    7 |           2d6 |    7 |  -2 |  +1 |   S    |    -1 |
| Schartiges Schwert  | 1d9         |    5 |           1d9 |    5 |  -1 |  -1 |   H    |    -2 |
| Rostiger Zweihänder | 2d8         |    9 |           2d8 |    9 |  -2 |  -3 |   H    |    -5 |
| Rostige Kriegsaxt   | 2d6         |    7 |           2d6 |    7 |   0 |  -3 |   H    |    -3 |
| Unbewaffnete[^3]    | 1d5         |    3 |           1d6 |  3,5 |  -2 |  -2 |        |    -4 |
| " Goblins           | 1d5         |    3 |           1d6 |  3,5 |  -2 |   0 |        |    -2 |
| " Trolle            | 1d5+1       |    4 |             - |    - |  -2 |  -2 |        |    -4 |

</div>

[^1]: Katapulte schießen nur in der 1. Runde des Kampfes, treffen dort aber 6 Ziele.
[^2]: Armbrüste schießen nur in der 1. und 4. Runde. Bei einem Armbrusttreffer wird der Rüstungsschutz des Gegners halbiert und abgerundet.
[^3]: Besonderheiten je nach Rasse:

- [Goblins][goblins-de-id] haben unbewaffnet nicht den Abzug von -2 auf Defensive
- [Trolle][trolle] machen unbewaffnet mehr Schaden, können aber nicht zu Pferd kämpfen
- [Orks][orks] kämpfen mit bestem Nahkampftalent -3
- [Katzen][katzen] bekommen ihren üblichen Bonus, haben also unbewaffnet -1 auf Defensive
- Manche Rassen (i.A. nur Monster und [[vertraute]]) können das Talent *Unbewaffneter Kampf* lernen und haben dann keinen Abzug, wenn sie ohne Waffe kämpfen

*Legende:* `d` = Würfel (`1d11+1` = 2 bis 12 Schadenspunkte). `⌀` ist der Durchschnittsschaden.  
`OB`/`DB` sind Offensiv-/Defensivbonus. Der Schaden zu Pferd gilt nur mit dem [Pferdebonus][boni-und-mali].  
Talente: K = Katapultbedienung, A = Armbrustschießen, B = Bogenschießen, H = Hiebwaffen, S = Stangenwaffen.

[](){ #table-ausdauer-id }

## Ausdauer

*HP-Bonus je [Ausdauer][skill-ausdauer-id]-Stufe. Formel und Rechner stehen unter [Krieg][krieg].*

<div class="sortable" markdown="1">

| Talent        |    0 |    1 |     2 |     3 |     4 |     5 |      6 |      7 |      8 |      9 |     10 |     15 |     20 |     25 |      30 |      35 |      40 |
| ------------- | ---: | ---: | ----: | ----: | ----: | ----: | -----: | -----: | -----: | -----: | -----: | -----: | -----: | -----: | ------: | ------: | ------: |
| Trefferpunkte | +0 % | +7 % | +20 % | +37 % | +57 % | +79 % | +104 % | +131 % | +160 % | +191 % | +224 % | +410 % | +632 % | +883 % | +1161 % | +1464 % | +1788 % |
| Dämonen       |   50 |   53 |    60 |    68 |    78 |    89 |    101 |    115 |    130 |    145 |    161 |    255 |    366 |    491 |     630 |     782 |     944 |
| Elfen         |   18 |   19 |    21 |    24 |    28 |    32 |     36 |     41 |     46 |     52 |     58 |     91 |    131 |    177 |     227 |     281 |     339 |
| Goblins       |   16 |   17 |    19 |    21 |    25 |    28 |     32 |     36 |     41 |     46 |     51 |     81 |    117 |    157 |     201 |     250 |     302 |
| Halblinge     |   18 |   19 |    21 |    24 |    28 |    32 |     36 |     41 |     46 |     52 |     58 |     91 |    131 |    177 |     227 |     281 |     339 |
| Insekten      |   24 |   25 |    28 |    32 |    37 |    42 |     48 |     55 |     62 |     69 |     77 |    122 |    175 |    236 |     302 |     375 |     453 |
| Katzen        |   20 |   21 |    24 |    27 |    31 |    35 |     40 |     46 |     52 |     58 |     64 |    102 |    146 |    196 |     252 |     312 |     377 |
| Meermenschen  |   20 |   21 |    24 |    27 |    31 |    35 |     40 |     46 |     52 |     58 |     64 |    102 |    146 |    196 |     252 |     312 |     377 |
| Menschen      |   20 |   21 |    24 |    27 |    31 |    35 |     40 |     46 |     52 |     58 |     64 |    102 |    146 |    196 |     252 |     312 |     377 |
| [Orks][orks]  |   24 |   25 |    28 |    32 |    37 |    42 |     48 |     55 |     62 |     69 |     77 |    122 |    175 |    236 |     302 |     375 |     453 |
| Trolle        |   30 |   32 |    36 |    41 |    46 |    53 |     61 |     69 |     78 |     87 |     97 |    153 |    219 |    295 |     378 |     469 |     566 |
| Zwerge/       |   24 |   25 |    28 |    32 |    37 |    42 |     48 |     55 |     62 |     69 |     77 |    122 |    175 |    236 |     302 |     375 |     453 |

</div>

[](){ #tabelle-verwundungsstatus-id }

## Verwundungsstatus

<div class="sortable" markdown="1">

| Status           |   Schwelle |
| ---------------- | ---------: |
| Sehr stark       | > 200 % HP |
| Stark            | > 150 % HP |
| Erschöpft        |  < 99 % HP |
| Verwundet        |  < 75 % HP |
| Schwer verwundet |  < 50 % HP |

</div>

[](){ #tabelle-rustung-und-schield-id }

## Rüstungen und Schilde

*Relative, multiplikative Änderungen. Formel und Beispiel stehen unter [Krieg][krieg].*

<div class="sortable" markdown="1">

| Rüstung                | Panzerung | Änderung der Chance, getroffen zu werden |
| ---------------------- | --------: | ---------------------------------------: |
| Schild                 |         1 |                                    −15 % |
| Rostiger Schild        |         1 |                                      0 % |
| Laenschild             |         2 |                                    −25 % |
| Rostiges Kettenhemd    |         2 |                                    +30 % |
| Kettenhemd             |         3 |                                    +15 % |
| Rostiger Plattenpanzer |         3 |                                    +45 % |
| Plattenpanzer          |         5 |                                    +30 % |
| Laenkettenhemd         |         6 |                                      0 % |
| Adamantiumrüstung      |         7 |                                    +10 % |

</div>

## Rasseneigenschaften

*Natürliche Rüstung: Regeln stehen unter [Krieg][krieg].*

<div class="sortable" markdown="1">

| Rasse        |  HP |  R. |  NR |
| ------------ | --: | --: | --: |
| Menschen     |  20 |   0 |   0 |
| Meermenschen |  20 |   0 |   0 |
| Zwerge       |  24 |   5 |   0 |
| [Orks][orks] |  24 |  -5 |   0 |
| Elfen        |  18 |  10 |   0 |
| Halblinge    |  18 |   5 |   0 |
| Goblins      |  16 |  -5 |   0 |
| Trolle       |  30 |  10 |   1 |
| Dämonen      |  50 |  15 |   2 |
| Insekten     |  24 |   5 |   2 |
| Katzen       |  20 |   0 |   0 |

</div>

<!-- From [https://wiki.eressea.de/index.php?title=Kriegstabellen&oldid=16872] -->
