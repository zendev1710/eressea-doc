---
# cSpell:locale en
alias: ships
title: Ships
---

<!-- markdownlint-disable MD025 -->
[](){ #ships-id }

# Ships

Ships are built using the [**`MAKE`**&#91;*`levels`*&#93;*`ship type`*][cmd-make] order.  
Existing, unfinished, or damaged ships can be further built using **`MAKE`**&#91;*`levels`*&#93;&nbsp;`SHIP`&nbsp;&#93;*`ship-id`*&#93;.  

Wood is needed for this. The more complex the ship, the harder it is to build and command.  
This is summarized in the table below.  

To start building a ship or to continue building or repairing one, the unit needs at least the specified shipbuilding skill.  
The table shows how much wood is required to build a ship.  
A unit can use per round this number of woods : `skill level X people / minimum skill`.

A ship also has an id that is used in orders.

Example:

```text
Pride of the Seven Winds (18), Longboat, (254/500). This beautiful

    ship was the first to be built by the Plötzbogen merchant family
    used. Captain Gorm stands on the quarterdeck and gives orders
    Orders to the sailors. He has everything completely under control.
```

For your own ships, the ship type indicates the load and capacity (here 254 weight units out of 500 possible).

In the report, the units that are on the ship are indented under the ship.

The first unit is a captain and has command of the ship.  
The captain determines which other units are allowed to board the ship.  
He may [rename][cmd-name] or [describe][cmd-describe] the ship, and also counts as crew.

Unlike buildings, ships cannot be expanded.  
So once you start building a [longboat][longboat], you won't be able to convert it into a [caravel][caravel] later.

Newly built ships are not located on any coast and can therefore sail to any neighboring ocean region.

## Ship types
<!-- TODO: add information  -->
### Boat

### Longboat

### Dragonship

### Caravel

[](){ #trireme-id }

### Trireme

### Galleon

### Ships - Summary table

Ships - type, range, capacity, needed sailing skill for captain/crew, needed building skill, needed wood.

| Type                     | Range | Capacity | Captain/Crew | Building skill |  Wood |
|--------------------------|:-----:|---------:|-------------:|---------------:|------:|
| [Boat][boat]             |   2   |       50 |          1/2 |              1 |     5 |
| [Longboat][longboat]     |   3   |      500 |         1/10 |              1 |    50 |
| [Dragonship][dragonship] | 5[^1] |    1 000 |         2/50 |              2 |   100 |
| [Caravel][caravel]       |   5   |    3 000 |         3/30 |              3 |   250 |
| [Trireme][trireme-id]    |   7   |    2 000 |        4/120 |              4 |   200 |
| [Galleon][galleon]       |   5   |   20 000 |    5/250[^2] |              5 | 2 000 |

[^1]: Dragonship speed depends on captain sailing skill.
[^2]: Only units from level 2 in sails are taken into account for the overall skill of the galleon.

Dragon ship speed.

| Captain | 2 | 6 | 18 | 54 | 162 |
|---------|---|---|----|----|:---:|
| Range   | 5 | 6 | 7  | 8  |  9  |

[](){ #convoy-id }

## Convoy

In the same way that you can have several people in a unit, convoys are made up of several ships **of the same type**.  
It is therefore not permitted, for example, to form a convoy made up of triremes and caravels.

To form a convoy, the unit owning a ship is given one or more ships of the same type with the [`GIVE <target-captain-id> 1 SHIP`][cmd-give] order.  
The target unit becomes the commander of a convoy.  

Source and target units **must belong to the same faction**.

The command unit can then direct all the ships in its convoy, provided that it has:

- The level of [sailing][skill-sailing-id] skill required for the type of ship
- At least as many people as ships in the convoy

The total crew sailing skill must also be a multiple corresponding to the number of ships.

The range of the convoy corresponds to that of the ship type; Maximum damage and payload increase with the number of ships.

**Example:**

A convoy of 3 caravels requires a captain of at least 3 people T3 in [sailing][skill-sailing-id], and a crew with 90 skill levels in total.  
As before, they have a range of 5 ocean regions, but a capacity of 9,000 lbs.  
The following configuration, for example, is therefore authorized and safe to navigate:

```text
Caravel (2seh), 3 Caravels, (9000/9000).
    * Kapitänsteam (k29), 3 Humans, Skill: Sailing 3.
    * Besatzung (2ztf), 9 Humans, Skill: Sailing 9.
    * Horde (770L), 888 Humans.
```

With a convoy, it then becomes possible to move large units without having to distribute them on individual ships.  
For the rest, a convoy behaves like a single ship.

For example, the entire convoy drifts together, takes damage as a whole, and command can be transferred.

!!! note
   **It is not possible** to form a convoy of [**boats**][boat].

Damaged or incomplete ships can also be transferred, their condition then being reflected proportionally on the convoy.  
If a ship with 8% damage is handed over to a convoy of 3 ships, the convoy then consists of 4 ships with 2% damage.

If only one ship under construction is handed over, the entire convoy is then under construction and cannot sail until completed.  
Thus, by forming a convoy of 2 ships, one of which is completed but the other is 50% under construction, we obtain a convoy under construction of 2 ships 75% complete.

The `GIVE <target-id> <number> SHIP` order also allows ships to be detached from a convoy.  
The ships or convoys of the giving unit and the receiving unit must be **on the same coast**or in the same ocean region.  
The receiving unit must either be captain of a ship — in which case the ship is added to its convoy — or be on the same ship as the yielding unit, or not be in a ship or building.

You can also give ships to farmers: `GIVE 0 2 SHIP` creates a new convoy with 2 ships, on which there is no one.  
On land, a convoy commander cannot hand over all his ships to the peasants, he must always keep at least one.

If, after the transfer, the transferred unit no longer has any ships, all units that previously accompanied it automatically switch to the ships of the destination unit.

Convoys cannot be enchanted, enchanted ships cannot be transferred, and no ships can be transferred to owners of enchanted ships.

Player experience (Solthar) :

An empty unit cannot hand over anything.  
This is why the order of the following orders is important:

```text
GIVE 123 1 SHIP
GIVE 123 ALL MEN
```

## See also

- [[movement]]
- [`GIVE`][cmd-give]

Continue reading: [Buildings][buildings-id].

<!-- From [https://wiki.eressea.de/index.php?title=Schiff/fr&oldid=16676] -->

[cmd-describe]: [[cmd-describe]]
[cmd-give]: [[cmd-give]]
[cmd-make]: [[cmd-make]]
[cmd-name]: [[cmd-name]]
