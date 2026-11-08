---
# cSpell:locale en
alias: skills
---

# Skills
<!-- TODO: translate page in english -->

Skills are an essential element that defines a [unit][cmd-unit] in Eressea.  
All people in a unit have the same skills. They have to learn them first.
To be precise, with the [`LEARN`][cmd-learn] order, a unit can make one attempt per turn to gain a new level.

## Progression by use

Some skills also improve by using them. If the unit uses the skill, there is a 1/3 chance it will gain experience (2/3 chance it will not gain experience).  
So by exercising a skill a unit progresses statistically at around 1/3 of the learning speed (by `LEARN`).  

Skills that **do not improve** by **practicing** include the following:

- All weapon skills
- [Endurance][skill-endurance-id]
- [Perception][skill-perception-id]
- [Tactics][skill-tactics-id]
- [Taxation][skill-taxation-id]

In most cases, the skill value displayed in the report is the one to use.  
It includes racial bonuses, regional bonuses and elements like famine or magic, which modify the value of the skill.  
But sometimes the "raw" skill value without bonus is also needed, especially for calculating magic learning costs and learning times.

## Learn skills

Reaching a new skill level becomes more and more difficult with each level.  
On average, progressing to a new skill level with the [`LEARN`][cmd-learn] order takes approximately a number of weeks equal to the targeted skill level, regardless of changes made by [race][races] or terrain.
The minimum learning time is 1 week. The maximum learning time does not exceed (2 x new level − 1).
Extreme values ​​are less frequent than the average value. So moving from level 3 to level 4 can take up to 7 weeks, but will take an average of 4 weeks.  
It takes an average of two weeks for a [dwarf][dwarves] to go from level 3 to level 4 in the Mining skill, as dwarves have a +2 modifier for this skill (4-2=2).

**Examples:**

Moving up from Level 3 to Level 4 takes an average of 4 weeks, but sometimes as little as a week and sometimes up to 7 weeks.  
A [dwarven unit][dwarves] with mining 3 in the report is actually level 1 "raw", since dwarves have a modifier of +2 on mining.  
It takes an average of two weeks to advance in the mining skill from level 3 to level 4.

To reduce the time required to learn a skill, a second unit, more experienced than the first, can [teach][cmd-teach] the skill.  
This unit must be at least 2 levels higher than the student in the skill.  
The student unit learns twice as fast as if it learned without a teacher. The teaching unit does not gain any experience from it.  
Learning in an [academy][academy] allows you to learn more quickly.

A teacher can have up to 10 students. A teaching unit can contain as many people as desired.  
If the "student unit" has too many people, this will be taken into account in the learning chances.  
A unit can teach several units, just as a unit of students can learn from several units of teachers, each student of course only being able to benefit from a single teaching.

**Example:**

```text
Unit l1; 1 Person, Endurance 3
TEACH s1
Unit l2; 1 Person, Melee 3, Endurance 3
TEACH s1 s2
Unit s1; 15 Persons, Endurance 1
LEARN Endurance
Unit s2; 10 Persons, Melee 1
LEARN Melee
```

Result: Unit l1 teaches 10 people from unit s1 in endurance.  
Unit l2 teaches the remaining 5 people from s1 in endurance and 5 people from unit s2 in cutting weapons.  
Unit s1 is taught by l1 and l2 and learns twice as fast as normal.  
Unit s2 is only half taught in endurance and therefore only learns 50% faster.  

!!! warning "Attention"
    If multiple units of teachers teach multiple units of students in different skills or skill levels, some students may not have a teacher or receive the wrong teacher.  
    IIt is not possible to do otherwise due to the internal organization of Eressea.  
    In this case, you need to create “clear relationships” by restructuring the teaching units.  
    With the [`LEARN-AUTO`][cmd-learn-auto] command, the server attempts to automate learning and teaching in a region.  
    However, as this is due to a simple heuristic, it is not guaranteed that an optimal (long-term) learning chain is created.  

[magic][skill-magic-id], [alchemy][skill-alchemy-id], [herbalism][herbalism], [espionage][skill-espionage-id] and [tactics][skill-tactics-id] are particularly difficult and expensive.  
Learning espionage costs 100 Silver per person per turn; 200 Silver per person per week for Alchemy, Herbalism and Tactics.  
Learning magic easily costs several thousand Silver at high levels (see [this table][magic]).  
The unit that learns one of these skills must have this amount in its possession.  
Whether or not the unit receives instruction has no bearing on the cost.  
If the unit is in an [academy][academy], the cost of learning paid skills is doubled.  

If the unit being trained does not have enough at the time of payment, it will learn in proportion to the amount of Silver it has;  
for example if she only has 500 Silver out of 550, her chances of learning will decrease by around 10%.

In rare cases, a unit may want to get rid of a skill. This is possible with the [`FORGET`][cmd-forget] command.

## Mixing skills

When people transfer or are recruited into an existing unit, new skill levels are calculated based on the number of weeks of training both units have had.  
It may happen that weeks of learning are "lost" due to rounding effects.  
You should therefore avoid unnecessarily merging units as much as possible.

**Example:**

A two-person unit with [melee][skill-melee-id] T5 recruits a peasant.  
The two people each studied for approximately 15 weeks (i.e. 1+2+3+4+5) before progressing to level 5.  
The farmers have no skills, so we add 0. The new unit therefore has approximately 30 weeks of training.  
This corresponds to 3 people with melee T4 (1+2+3+4=10 weeks per person).  
The new unit is therefore level 4.

For the calculation of apprenticeship weeks, just as for apprenticeship, it is the "raw" skill values ​​that count, from which all bonuses and penalties such as racial bonuses are first subtracted.

Player Experience (Solthar):

In fact, the matter is more complicated.
However, you can skip this if you are reading this guide for the first time.
Each time a unit advances a level, a dice is rolled to determine how many weeks it will take to advance to the next level.
This results in a value between 1 and (2 x new level − 1).
A unit can therefore have a skill between (6,1) -this notation means level 6 and still a week until promotion -and (6,13).
This value is taken into account when mixing.
For example, if you mix a person with (5.6) and a person with (1.2) -both of which correspond exactly to the average -they have a total of 16 weeks of learning.
However, two people with (3.4) only correspond to 12 weeks of learning.
The difference of two weeks per person will be “credited” to the new unit.
It therefore has (3.2) -a little better than average.

If you mix (5,1) and (1,1), i.e. people who have almost made it to the next climb, you would even get (4,4).
However, mixing (5,11) and (1,3) results in (3,5) as the new value. So it is not possible to accurately predict the skill value of a mixed unit.
Only a minimum and maximum value can be specified.

## Use of skills

Skills allow units to do certain things.  

Sometimes it is the unit's skill level that makes a given activity possible.  
Sometimes the total skill level (the number of people x the skill level) of the unit also plays a role.  

Skills can be divided into several groups.

### Skills for production

alchemy, mining, masonry, forestry, herbalism, taming, armoursmithing, shipcraft, quarrying, roadwork, weaponsmithing, cartmaking

This is the largest group of skills.  
These skills allow you to craft objects, buildings, boats or roads.  
The production skills are as follows :

- [Alchemy][skill-alchemy-id] (potion making)
- [Taming][taming] (obtaining horses)
- [Shipcraft][shipcraft]
- [Roadwork][roadwork]
- [Quarrying][quarrying]
- [Mining][mining] (production of iron, laen or adamantium)
- [Weaponsmithing][weaponsmithing]
- [Armoursmithing][armoursmithing]
- [Cartmaking][cartmaking]
- [Herbalism][herbalism] (harvesting plants)
- [Masonry][masonry]
- [Forestry][forestry] (wood and mallorn production)

More information:

- [Production][production-id]
- [Alchemy][alchemy-id]

### Skills for making money

[Trade][skill-trade-id], [taxation][skill-taxation-id] and [entertainment][skill-entertainment-id] allow you to earn money (silvers).

More information: [money][money].

### Concealment & Co

[espionage][skill-espionage-id], [stealth][skill-stealth-id] and [perception][skill-perception-id] are focused on concealment.

More information: [stealth][stealth-id].

### Movement skills

[Sailing][skill-sailing-id] and [riding][riding] are explained in the chapter on [movement].

Riding is also covered in the [combat][war-tables] chapter.

[](){ #skills-skill-magic-id }

### Magic

[Magic][magic-id] is a skill with particularly powerful powers that takes up an entire chapter.

### Combat skills

Weapon handling skills are as follows :

- [Bow][skill-bow-id]
- [Catapult][skill-catapult-id]
- [Crossbow][skill-crossbow-id]
- [Melee][melee]
- [Polearm][polearm]
- [Unarmed combat][unarmed-combat]

Other essential combat skills are:

- [Endurance][skill-endurance-id]
- [Riding][riding]
- [Tactics][tactics-id]

All of these skills are particularly important in [battles][war], whether against other factions or monsters.

Continue reading: [[list-of-skills]].

<!-- From [https://wiki.eressea.de/index.php?title=Talente/fr&oldid=16177] -->

[cmd-forget]: [[cmd-forget]]
[cmd-learn]: [[cmd-learn]]
[cmd-learn-auto]: [[cmd-learn-auto]]
[cmd-teach]: [[cmd-teach]]
[cmd-unit]: [[cmd-unit]]
