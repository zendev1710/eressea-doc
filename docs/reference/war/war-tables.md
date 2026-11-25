---
# cSpell:locale en-GB
alias: war-tables
---

# War tables

Aggregate combat values only. Rules and formulas are in [War][war].

## Weapons - Summary table

<div class="sortable" markdown="1">

| Weapon               | Dam./foot |    ⌀ | Dam./horse |    ⌀ |  OB |  DB | Total |
| -------------------- | --------- | ---: | ---------: | ---: | --: | --: | ----: |
| Adamantium axe       | 3d4+15    | 22.5 |     3d4+15 | 22.5 |  +2 |  -2 |     0 |
| Axe                  | 2d6+4     |   11 |      2d6+4 |   11 |  +1 |  -2 |    -1 |
| Bow                  | 1d11+1    |    7 |     1d11+1 |    7 |  -2 |   0 |    -2 |
| Catapult[^1]         | 3d10+5    | 21.5 |     3d10+5 | 21.5 |  -4 |   0 |    -4 |
| Claymore             | 2d8+3     |   12 |      2d8+3 |   12 |  -1 |  -2 |    -3 |
| Crossbow[^2]         | 3d3+5     |   11 |      3d3+5 |   11 |   0 |   0 |     0 |
| Elven bow            | 2d6+4     |   11 |      2d6+4 |   11 |  -2 |   0 |    -2 |
| [[flaming-sword]]    | 3d6+10    | 20.5 |     3d6+10 | 20.5 |  +1 |  +1 |    +2 |
| Halberd              | 2d6+3     |   10 |      2d6+3 |   10 |  -1 |  +2 |    +1 |
| Laen sword           | 3d6+10    | 20.5 |     3d6+10 | 20.5 |  +1 |  +1 |    +2 |
| Lance                | 1d5       |    3 |      2d6+5 |   12 |   0 |  -2 |    -2 |
| Mallorn bow          | 1d11+2    |    8 |     1d11+2 |    8 |  -2 |   0 |    -2 |
| Mallorn crossbow[^2] | 3d3+6     |   12 |      3d3+6 |   12 |   0 |   0 |     0 |
| Mallorn lance        | 1d5+1     |    4 |      2d6+6 |   13 |   0 |  -2 |    -2 |
| Mallorn spear        | 1d10+1    |  6.5 |     1d12+3 |  9.5 |   0 |   0 |     0 |
| Rusty axe            | 2d6       |    7 |        2d6 |    7 |   0 |  -3 |    -3 |
| Rusty halberd        | 2d6       |    7 |        2d6 |    7 |  -2 |  +1 |    -1 |
| Rusty sword          | 1d9       |    5 |        1d9 |    5 |  -1 |  -1 |    -2 |
| Rusty claymore       | 2d8       |    9 |        2d8 |    9 |  -2 |  -3 |    -5 |
| Spear                | 1d10      |  5.5 |     1d12+2 |  8.5 |   0 |   0 |     0 |
| Sword                | 1d9+2     |    7 |      1d9+2 |    7 |   0 |   0 |     0 |
| Unarmed[^3]          | 1d5       |    3 |        1d6 |  3.5 |  -2 |  -2 |    -4 |
| Unarmed Goblins      | 1d5       |    3 |        1d6 |  3.5 |  -2 |   0 |    -2 |
| Unarmed Trolls       | 1d5+1     |    4 |          - |    - |  -2 |  -2 |    -4 |

</div>

[^1]: catapults only fire in the first round of the battle, but **hit 6 targets** there.
[^2]: crossbows only fire in the 1st and 4th rounds. A crossbow hit halves the opponent's armour protection.
[^3]: specific features depending on the race:

- [Goblins][goblins-id] do not have the -2 penalty to defence when unarmed
- [Trolls][trolls-id] deal more damage unarmed but cannot fight on horseback
- [Orcs][orcs-id] fight with their best Melee skill at -3
- [Cats][cats] receive their usual bonus, so they have -1 to Defence when unarmed
- Some races (generally only monsters and familiars) can learn the *Unarmed combat* skill and then have no penalty when fighting without a weapon

*Legend:* `d` = dice (`1d11+1` = 2 to 12 damage). `⌀` is the average damage.  
`OB`/`DB` are the offensive/defensive bonuses. Damage on horseback only applies with the [horse bonus][bonuses-and-mali].

[](){ #table-endurance-id }

## Endurance

*HP bonus per [endurance][skill-endurance-id] level. See [War][war] for the formula and calculator.*

<div class="sortable" markdown="1">

| Level      |   0 |   1 |    2 |    3 |    4 |    5 |     6 |     7 |     8 |     9 |    10 |    15 |    20 |    25 |     30 |     35 |     40 |
| ---------- | --: | --: | ---: | ---: | ---: | ---: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | -----: | -----: | -----: |
| Hit points | +0% | +7% | +20% | +37% | +57% | +79% | +104% | +131% | +160% | +191% | +224% | +410% | +632% | +883% | +1161% | +1464% | +1788% |
| Aquarians  |  20 |  21 |   24 |   27 |   31 |   35 |    40 |    46 |    52 |    58 |    64 |   102 |   146 |   196 |    252 |    312 |    377 |
| Cats       |  20 |  21 |   24 |   27 |   31 |   35 |    40 |    46 |    52 |    58 |    64 |   102 |   146 |   196 |    252 |    312 |    377 |
| Demons     |  50 |  53 |   60 |   68 |   78 |   89 |   101 |   115 |   130 |   145 |   161 |   255 |   366 |   491 |    630 |    782 |    944 |
| Dwarves    |  24 |  25 |   28 |   32 |   37 |   42 |    48 |    55 |    62 |    69 |    77 |   122 |   175 |   236 |    302 |    375 |    453 |
| Elves      |  18 |  19 |   21 |   24 |   28 |   32 |    36 |    41 |    46 |    52 |    58 |    91 |   131 |   177 |    227 |    281 |    339 |
| Goblins    |  16 |  17 |   19 |   21 |   25 |   28 |    32 |    36 |    41 |    46 |    51 |    81 |   117 |   157 |    201 |    250 |    302 |
| Halflings  |  18 |  19 |   21 |   24 |   28 |   32 |    36 |    41 |    46 |    52 |    58 |    91 |   131 |   177 |    227 |    281 |    339 |
| Humans     |  20 |  21 |   24 |   27 |   31 |   35 |    40 |    46 |    52 |    58 |    64 |   102 |   146 |   196 |    252 |    312 |    377 |
| Insects    |  24 |  25 |   28 |   32 |   37 |   42 |    48 |    55 |    62 |    69 |    77 |   122 |   175 |   236 |    302 |    375 |    453 |
| Orcs       |  24 |  25 |   28 |   32 |   37 |   42 |    48 |    55 |    62 |    69 |    77 |   122 |   175 |   236 |    302 |    375 |    453 |
| Trolls     |  30 |  32 |   36 |   41 |   46 |   53 |    61 |    69 |    78 |    87 |    97 |   153 |   219 |   295 |    378 |    469 |    566 |

</div>

## Health status

<div class="sortable" markdown="1">

| Status           | Threshold |
| ---------------- | --------: |
| Exhausted        |  < 99% HP |
| Wounded          |  < 75% HP |
| Severely wounded |  < 50% HP |
| Strong           | > 150% HP |
| Very strong      | > 200% HP |

</div>

## Armour - Summary table

*Relative, multiplicative changes. See [War][war] for the formula.*

<div class="sortable" markdown="1">

| Armour           | Protection | Change in chance to be hit |
| ---------------- | ---------: | -------------------------: |
| Shield           |          1 |                       −15% |
| Rusty shield     |          1 |                         0% |
| Laen shield      |          2 |                       −25% |
| Rusty chainmail  |          2 |                       +30% |
| Chainmail        |          3 |                       +15% |
| Rusty platemail  |          3 |                       +45% |
| Platemail        |          5 |                       +30% |
| Laen chainmail   |          6 |                         0% |
| Adamantium plate |          7 |                       +10% |

</div>

## Races and their characteristics

*See [War][war] for the natural armour rules.*

<div class="sortable" markdown="1">

| Race      |  HP |  R. |  NA |
| --------- | --: | --: | --: |
| Aquarians |  20 |   0 |   0 |
| Cats      |  20 |   0 |   0 |
| Demons    |  50 |  15 |   2 |
| Dwarves   |  24 |   5 |   0 |
| Elves     |  18 |  10 |   0 |
| Goblins   |  16 |  -5 |   0 |
| Halflings |  18 |   5 |   0 |
| Humans    |  20 |   0 |   0 |
| Insects   |  24 |   5 |   2 |
| Orcs      |  24 |  -5 |   0 |
| Trolls    |  30 |  10 |   1 |

</div>

<!-- From [https://wiki.eressea.de/index.php?title=Kriegstabellen&oldid=16872] -->
