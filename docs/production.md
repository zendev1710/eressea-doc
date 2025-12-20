---
# cSpell:locale en
alias:
    name: production
    text: Production
---
# Production

Various things can be produced in Eressea.
There are [raw materials] (e.g. iron, stones, wood, horses) and [finished products] (various weapons and armor, [ships] and chariots, [buildings] and [roads] and alchemical [potions]).
In order to be able to produce things, you need the appropriate skill.
Most things are done with the command [`MAKE`*`Anzahl`*` `*`Gegenstand`*] produced, for example`MAKE Eisen, MAKE Schwert`or`MAKE 15 Elfenbogen`.

Depending on the item, a different level of skill is required in order to be able to produce it.
Most [Resources][1] only require basic knowledge of the corresponding skills (Level 1), while most [Items] require higher skill levels.
For items with high minimum skill values, you can only craft a few of them.
In any case, you can only produce one type of item or resource and work on one building or ship per unit per round.

With the exception of laen and adamantium, two particularly valuable and rare metals, and mallorn, a magical wood, all raw materials can be produced with a skill value of 1, as can horses and herbs.
To obtain Laen and Adamantium you need a [Mine] and a mining skill of 7 for Laen and 8 for Adamantium, respectively, for Mallorn Lumbering level 2.

For items as well as buildings and ships, the skill levels of all people in the unit are added together and divided by the minimum construction skill.
For each point calculated in this way, a building or ship can be built or expanded by one point in size or an object can be produced.

Once a building or ship has been started, you can continue to build on it with as many units as you want.
However, it is not possible to build multiple buildings or ships at the same time with one unit, even if skill levels and resources are sufficient.

 **Examples:**

- `MAKE 10 Schild` lets the unit produce 10 shields -assuming it has 10 iron, at least Armor Construction 2 and a total of 20 skill levels (10 shields x minimum skill 2 = 20)
- `MAKE 3 Boot` does not allow the unit to build three separate boats, but only the appropriate amount of wood for the ship mentioned (here 3 out of 5 for one boat)
- A unit with 4 people and weapon construction 5 has a total of 20 skill levels. For example, she can use it to create 6 swords (minimum weapon construction skill 3), 4 elven bows (if they are elves; requires weapon construction 5) or 10 spears (weapon construction 2) without any tools.
- With a forge, people could halve their iron consumption for swords, shields, etc., i.e. produce 10 shields from 5 iron. They also have a +1 skill bonus on the Weapon Construction and Armor Construction skills
- **Important:** The skill levels only count together if the people are in a unit! However, the unit must always have the minimum skill value

Gerade bei größeren Parteien kann das "Zusammensuchen" aller Materialien z.B. für Gebäude lästig sein.
Um dies zu vereinfachen, gibt es einen [Materialpool], dessen Funktion im betreffenden Abschnitt erklärt ist.

## See also

- [Rohstoffe]
- [Waren][Endprodukte]
- [Straßen][2]
- [Schiffe][3]
- [Gebäude]
- [Parteipool]

Continue reading: [Rohstoffe].

[Rohstoffe]: ./resources.md

<!-- From [https://wiki.eressea.de/index.php?title=Produktion&oldid=16875] -->

[Endprodukte]: ./items.md
[Schiffe]: ./ships.md
[Gebäude]: ./buildings.md
[Straßen]: ./roads.md
[Tränke]: ./alchemy.md
[1]: ./resources.md
[Gegenstände]: ./items.md
[Bergwerk]: ./buildings-others.md#mine
[Materialpool]: ./items-pool.md
[2]: ./roads.md
[3]: ./ships.md
[Parteipool]: ./faction-pool.md
