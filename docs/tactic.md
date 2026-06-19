---
# cSpell:locale en
alias: tactics
---

# Tactics

Before the battle, the best tactician of all participating units is determined.  
The side with the best tactician wins the so-called "tactician round": in a skilful maneuver, he lures the enemy into an ambush and his allies can strike unexpectedly with a certain chance before the first round of battle, without the enemy being able to attack in this round. If two or more tacticians from different sides are equally good, all of them can strike in the tactician round. The chance of making this strike is 10% for every skill point difference between your best tactician and the best tactician on the other side, including bonuses or penalties.  
From a skill difference of 10, all allies strike once. The tactician round also counts for reloading, so a crossbow that has fired in the tactician round shoots a second time in round 3 instead of round 4. The tactician round also allows an additional escape attempt.

## Tactical bonuses depending on the situation

A Tactician who is [fighting] in the first row receives a +1 bonus to his Tactics skill. If he is in the 3rd or 4th row, his skill is reduced by 1.

There are also some racial bonuses to the Tactics skill that depend on the terrain:

| Race   | Terrain           | Bonus/Malus |
|--------|-------------------|:-----------:|
| Elf    | Forest            | +2          |
| Dwarf  | Mountain, Glacier | +1          |
| Insect | Swamps, Desert    | +1          |
|        | Mountain, Glacier | -1          |

Insects also receive an additional bonus to the Tactics skill when they appear en masse. An insect tactician receives a bonus of log10(number of fighters in his army)-1 to Tactics. This can also result in a penalty if there are very few fighters! Important: Only the fighters in your army really count. Different groups should therefore be avoided and the troops of alliance partners do not count either.

|                    |     |       |         |            |               |                 |     |
|--------------------|-----|-------|---------|------------|---------------|-----------------|-----|
| Number of fighters | 1-9 | 10-99 | 100-999 | 1000-9.999 | 10.000-99.999 | 100.000-999.999 | ... |
| bonus              | -1  | 0     | +1      | +2         | +3            | +4              | ... |

## Inspiration

To allow for a little "inspiration" and luck, each tactician receives a random bonus that starts at 0 and can become very large, with the probability of this becoming smaller and smaller the larger the bonus is. If a tactician unit consists of several people, the dice are rolled once for each person.

| Probability | Bonus | Other      |
|------------:|:-----:|------------|
|         40% |  +0   |            |
|         30% |  +1   |            |
|         20% |  +2   |            |
|          7% |  +3   |            |
|          3% |  +3   | roll again |

Depending on the number of tacticians, this results in the following average inspiration bonuses:

|                     |      |      |      |      |      |      |      |
|---------------------|------|------|------|------|------|------|------|
| Number of tactician | 1    | 3    | 12   | 44   | 129  | 410  | 1480 |
| Average Bonus       | 1.03 | 1.96 | 3.05 | 4.03 | 5.03 | 6.03 | 7.03 |

This means that 12 Tacticians level X reach the same level on average as one Tactician level X+2.
You can therefore (also) replace a lack of class in Tacticians with mass, but it becomes very expensive relatively quickly.

## See also

- [The war][tacticians-round]

<!-- From [https://wiki.eressea.de/index.php?title=Taktik/en&oldid=9952] -->

[fighting]: [[cmd-combat]]
