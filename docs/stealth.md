---
# cSpell:locale en
alias: stealth
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD041 MD042 MD052 -->
[](){ #stealth-id }

# Stealth

The **Stealth** [[skills|skill]] allows you to camouflage yourself from other units.  
However, if a unit [is guarding][cmd-guard] the region, or is on a ship or in a building, it is always visible.  

## Countermeasures

Camouflaged units can be detected using the **Perception** skill.  
If your faction's highest Perception skill in the region is lower than the Camouflage skill of an opposing unit, the camouflaged unit will not appear in the report — it will be invisible.  
If the Perception and Camouflage skills are equal, the camouflaged unit will appear in the report.  
This is the starting situation when you begin the game, as all new units have Stealth and Perception at level 0.  

## Counter the guard

For successfully disguised units, the restrictions of [[cmd-guard]] do not apply.  
They can therefore collect taxes, mine resources, destroy roads, and recruit farmers.  

## Increase chance of escape

The standard [escape][fleeing] chance of a unit in combat is 25% (halflings 50%).  
Each level of camouflage increases the unit's escape chance by 5%.  
A horse increases a person's escape chance by 10% once (so 5 horses do NOT give a person +50%, but only +10%), regardless of whether the unit can ride.  
The maximum escape chance is 75% (halflings 90%).  

## Theft of Silver

Successful stealers can steal silver from other units using the [[cmd-steal]] command.  
The highest Perception skill of the targeted party in the region determines the amount stolen.  
For each skill level difference, each thief steals 50 silver.  
The silver is **always** stolen from the entire silver pool of the targeted party in the region.  
The targeted party receives a notification that they have been robbed, but not by whom.  
If the stealth skill is only equal to the Perception skill, the theft fails, and the targeted party receives an anonymous notification of the attempt.  
If the stealth is too poor, the targeted party receives a notification with the names of the thieves.  

Goblins, provided they have learned at least level 4 of stealth, always steal at least 50 silver, even if their stealth skill is lower than their Perception skill.  
Such theft is, of course, noticeable and therefore only makes sense under certain circumstances.  
It is said that goblin armies have even dealt the enemy a decisive blow by depriving them of food.  

If you expect to be successfully robbed, the only solution is to bring silver into the affected region, as even income from entertainment, tax collection, work and trade can be stolen by the thieves.  

Theft occasionally presents an effective way to bring down spies who are themselves well disguised, as their high level of camouflage gives them a high chance of escape during attacks.  

[](){ #espionage-id }

## Espionage

If a unit with the [Espionage][skill-espionage-id] skill issues the [`SPY`*`unit id`*][cmd-spy] order, its espionage skill is compared to the target unit's camouflage value.  
The base chance for a successful espionage attempt is 10%.  
For each skill level by which the espionage skill exceeds the target's camouflage skill, the latter increases by 5%.  
A high camouflage skill thus helps the unit to make a successful espionage attempt more difficult.  
To achieve a 50% success rate, the spy must be 8 levels higher.  

If the spy learns at least camouflage level 2, it takes disproportionately longer to reach those 8 levels.  

If the espionage attempt is successful, the spy learns the unit's combat status, the items it possesses, and its skills.  
Faction affiliation can also be determined if the spy's espionage skill is at least six levels higher than the unit's stealth skill.  
Therefore, a high stealth skill is advantageous for successful faction concealment.  

Then, regardless of success, a die is rolled to determine whether the espionage attempt was detected.  
The probability of this is (100 − Espionage * Spy 5 + Perception Victim 2)%.  

## Remarks

Many factions store their goods with a highly camouflaged unit per region ([combat status][cmd-combat]: `COMBAT NOT` or `COMBAT FLEE`).  
The goods are thus protected from a multitude of dangers, as long as no enemy observer detects the camouflage.  

In addition to these passive applications of camouflage, one can of course use well-trained camouflaged individuals to gather information or take advantage of the possibility of theft.  

## See also

- [[cmd-guard]]
- [revenue][stealing-the-dishonest-way]

Continue reading: [[travel]].

<!-- From [https://wiki.eressea.de/index.php?title=Tarnung&oldid=17029] -->
