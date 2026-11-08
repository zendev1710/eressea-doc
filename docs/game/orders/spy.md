---
# cSpell:locale en
alias: cmd-spy
---

# `SPY`

*[long prder][short-and-long-orders].*

**`SPY`**` `*`unit-id`*

Espionage allows you to spy on units of another faction.  
The spy's espionage skill is compared with the target unit's [stealth][skill-stealth-id]] skill.  

The basic chance of a successful espionage attempt is 10%.  
For each skill level that the espionage skill exceeds the victim's stealth skill, this increases by 5%.  

If the espionage attempt is successful, the spy learns the combat status, the items in the unit's possession, the skills and also the true faction affiliation.  

Faction affiliation can only be determined if the espionage skill is at least 6 skill levels above the unit's stealth skill.  
All other information can be determined with a simple success.  

Then - regardless of success - a dice is rolled to see whether the espionage attempt was noticed.  
The probability of this is :

`(100 - SpySpy x 5 + (Perception Sacrifice x 2)%`

## Player experience (Ralf D.)

Spies are always 1-person units, since apparently one espionage attempt is **NOT** carried out per person in the spy unit, but only once for the entire unit.  
Like all activities that depend on probabilities, you can also increase the success of espionage by spying on the same target unit with many 1-person units.  

### Example

Spies with Espionage 10 spy on a combat unit with Stealth 1.  

- 1 unit has a chance of 10% + (10 -1)*5% = 55% to spy on the target unit
- 5 units therefore have a chance of 100% -(100% -55%)^5 = 98.2%

The following is also interesting (always against camouflage 1 of the target unit):

- 5 units with Espionage 2 also have a 55% chance of success
- 8 units with Espionage 1 have a 57% chance of success
- 22 units with Espionage 1 have a 90% chance of success

The cost considerations are then interesting:

- 1 unit of espionage 10 -> 55 rounds (without teacher) -> 5500 Silver + other training and recruiting
- 5 units of espionage 2 -> 3 rounds*5 people -> 1500 Silver + ...
- 8 units of espionage 1 -> 1 round*8 people -> 800 Silver + ...

### Conclusion

High espionage skills are only worthwhile if the unit(s) have also received other training or if you cannot split up the units due to the unit limit even in the situations in which you need espionage.  

As a countermeasure, basic training in camouflage helps against many bad spies. However, more effort must always be put into camouflage than the spies have to put into espionage.  

It is clear that espionage attempts with many bad units will be noticed with almost 100% certainty.  

!!! warning "Caution"
    If the game mechanics are changed so that the target unit only calculates a random limit once per round, then the same result applies to all equally good spies, which makes this consideration incorrect.  
    At the moment there are different results for the same spies.

<!-- From [https://wiki.eressea.de/index.php?title=SPY&oldid=16733] -->
