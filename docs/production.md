---
# cSpell:locale en
alias: production
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD041 MD042 MD052 -->
[](){ #production-id }

# Production

Various things can be produced in Eressea.  

There are [resources][resources] (e.g. iron, stones, wood, horses) and [[items|finished products]]: various weapons and armor, [ships][ships-id] and chariots, [[buildings]] and [[roads]] and alchemical [[alchemy|potions]].  
In order to be able to produce things, you need the appropriate skill.  

Most things are done with the order [`MAKE`*`<number>`*` `*`item`*][cmd-make], for example `MAKE Iron`, `MAKE Sword` or `MAKE 15 Elvenbow`.  

Depending on the item, a different level of skill is required in order to be able to produce it.  
Most [resources][resources] only require basic knowledge of the corresponding skills (Level 1), while most [[items]] require higher skill levels.  
For items with high minimum skill values, you can only craft a few of them.
In any case, **per unit per round**, you can only produce one type of item or resource and work on one building or ship.  

With the exception of [laen][laen-id] and [adamantium][adamantium-id], two particularly valuable and rare metals, and [mallorn][mallorn-id] (a magical wood), all raw materials can be produced with a skill value of 1, as can horses and herbs.
To obtain laen and adamantium you need a [mine][mine-id] and a [mining][mining] skill of **7 for laen**, **8 for adamantium**, and **[forestry][forestry] level 2 for Mallorn**.

For items as well as buildings and ships, the skill levels of all people in the unit are added together and divided by the minimum construction skill.  
For each point calculated in this way, a building or ship can be built or expanded by one point in size or an object can be produced.

Once a building or ship has been started, you can continue to build on it with as many units as you want.  
However, it is not possible to build multiple buildings or ships at the same time with one unit, even if skill levels and resources are sufficient.

## Example 1

`MAKE 10 Shield`  

Lets the unit produce 10 shields, assuming :

- it has 10 iron,
- at least [armoursmithing][armoursmithing] T2,
- a total of 20 skill levels (10 shields x minimum skill 2 = 20).

## Example 2

`MAKE 3 Boat`  

Does not allow the unit to build three separate boats.  
but it defines only the appropriate amount of wood for the ship mentioned (here 3 out of 5 for one boat)

## Example 3

A unit with 4 people and [weaponsmithing][weaponsmithing] T5 has a total of 20 skill levels.
For example, she can use it to create :

- 6 swords (minimum weaponsmithing skill T3), or
- 4 elven bows (if they are elves; requires weaponsmithing T5, or
- 10 spears (weaponsmithing 2)

## Example 4

With a [smithy][smithy], people could halve their iron consumption for swords, shields, etc.
for example they could produce 10 shields from 5 iron.

They also have a **+1 skill bonus** on the weaponsmithing and armoursmithing skills

!!! note "important"
    The skill levels only count together if the people are in a unit!  
    However, the unit must always have the minimum skill value

Especially for larger factions, “collecting” all the items, e.g. for buildings, can be annoying.
To simplify this, there is an [[items-pool]].

## See also

- [Resources][resources]
- [[items|Goods]]
- [Roads][roads-id]
- [[ships]]
- [[buildings]]
- [[faction-pool]]

Continue reading: [resources][resources].

<!-- From [https://wiki.eressea.de/index.php?title=Produktion&oldid=16875] -->
