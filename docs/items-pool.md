---
# cSpell:locale en
alias: items-pool
---
# Items pool

Particularly with larger factions, players lose track in some regions, especially since "distributing money" is rather boring, hard work and does not add much to the fun of the game.

## The silver pool

The silver pool takes over the distribution of money when playing, so that for example with [[cmd-recruit]] the unit automatically gets enough money (if available in the region) or the learning of expensive skills is provided.  
Nevertheless, it is stated throughout the instructions that units must have enough money with them.  
This is just to avoid forgetting it.

Likewise, [[buildings]] are supplied from the pool if the silver is present in the region at the start of the round.  
If the entity that owns the building cannot pay for it out of their own pocket or from the pool, the building cannot function.  
At the end of the round, the unit will try again to pay for the building from its own silver reserves or from its own faction's pool.  

**`TEMP` units cannot reserve**.  
They cover the recruitment costs from the silver pool, if necessary, but should receive silver and items that they should take with them to another region or process immediately with [[cmd-give]].

!!! warning "Attention"
    when `TEMP` units get silver, they also use it to recruit!  
    So if you want them to take silver with themselves to another region, the recruitment silver must also be handed over.

Special rules apply to the maintenance of units: all silver in the region is used here, regardless of previous reservations.  
Units do not give silver they need for their own upkeep to units (to pay for their upkeep).

## The material pool

The material pool is the logical continuation of the silver pool: every unit that needs something, e.g. stones and wood for building buildings, automatically gets this from other units in the region.  

The pools are only valid for your own faction.  
Objects must be explicitly handed over to foreign units.  

The pools not only work in production (essentially for the [[cmd-make]] order), but basically for everything, and especially for [[cmd-reserve]], [[cmd-give]], [[cmd-use]], [[cmd-cast]] and [[cmd-recruit]] orders.  
If the unit does not have an item, it takes it from the material pool in order to process it, hand it over or reserve it.  
However, if a unit needs weapons for an attack or to collect taxes, these must be explicitly handed over or reserved, as the material pool does not apply here.

Inexperienced factions should plan the material pool thoroughly, as it is easy to "steal" resources from units that were not expected;  
thus "stealed" units cannot produce or not produce enough, while the other unit used more resources and produced more than intended.  

### Example 1

```text
UNIT a ; miner, has 30 iron
    MAKE 20 iron
    @GIVE c ALL iron
;
UNIT b ; weaponsmither, has no iron
    RESERVE 10 iron
    MAKE 10 sword
;
UNIT c ; for storage, has no iron
    LEARN Stealth
```

**Result:**

- Unit b first gets 10 iron from a's material pool
- Unit a gives the remaining 20 iron to c
- Unit b makes 10 swords out of 10 iron
- Unit a makes 20 iron
- So unit b has 10 swords
- Unit a has 20 iron
- Unit c has 20 iron

## RESERVE and GIVE

There are a few special things to note about [[cmd-reserve]] and [[cmd-give]], which come before most other orders in the [[orders-sequence]].
These apply equally to the silver and material pools:

Firstly, items that have been handed over or reserved are no longer available in the pool.  
<!-- TODO: clarify -->
So she can only use the unit that she has reserved or received.  

With `RESERVE` orders, the unit proceeds as follows: In a first pass, each unit first reserves its own items.  
From then on, everything that has been reserved will no longer be available for the pool.  
Only then do the units try to get the items from the pool that they did not have in the first step from other units.  
Both the processing of the `RESERVE` orders and the retrieval of items are carried out in the order in which the units appear in the report -strictly speaking this is not guaranteed, but it has been the practice for a long time.  

If a unit has multiple `RESERVE` orders for an item, this is not additive.
Instead, all orders are executed in sequence.  
However, this behavior is not guaranteed at the moment, so it is better for a unit to only have one `RESERVE` order per item.  

When `GIVE` is subsequently executed, items are also removed from the pool if necessary.
Here too, the report order is followed.  
Items reserved by any unit (including the unit with the `GIVE` order) are not passed on.
Items that have been handed over are no longer in the pool.  

!!! note
    `GIVE xyz ALL` order only hands over unreserved items to the unit itself.

All other orders first use your own, reserved or transferred items and only then use unreserved items from the pool.  

### Example 2

```text
UNIT a ; has 10 Silver
    LEARN Melee
    RESERVE 20 Silver
;
UNIT b ; has 0 Silver
    LEARN Melee
    RESERVE 10 Silver
;
UNIT c ; has 10 Silver
    LEARN Melee
    RESERVE 10 Silver
```

**Result:**

- Unit a reserves its own 10 silver
- Unit c reserves its own 10 silver
- Since there were only 20 silver in the region, the remaining `RESERVE` orders expire
- Unit a consumes its own 10 silver upkeep
- Unit c consumes its own 10 silver upkeep
- Unit b is starving because there is no silver left

If any unit had 10 more silver to begin with, unit b would not have starved.

### Example 3

```text
UNIT a ; hat 20 Silver
    RESERVE 20 Silver
    GIVE c 20 Silver
;
UNIT b ; has 20 Silver
    MOVE EAST
;
UNIT c ; has 0 Silver
    MOVE WEST
```

**Result:**

- Unit a reserves its own 20 silver
- Unit a gives 20 silver from the material pool to c.
  Her own 20 silver is reserved, so she takes the 20 silver from b
- Unit b goes east and will starve if there is no other unit there with silver
- Unit c takes the 20 silver west

### Example 4

```text
UNIT a ; has 10 Silver, 20 Wood, 10 Iron
    LEARN Melee
    RESERVE 5 Iron; (1)
    GIVE d ALL Iron; (6)
;
UNIT b ; has 10 Silver, 10 Iron
    RESERVE 100 Silver ; (2), (4)
    RESERVE 10 Wood ; (5)
    GIVE c 100 Silver ; (7)
    GIVE d 9 Wood ; (8)
    LEARN Melee
;
UNIT c ; Melee 10, has 100 Silver
    RESERVE 100 Silver ; (3)
    MAKE 10 Spear ; (9)
;
UNIT d ; has 200 Silver
    LEARN Forestry
```

 **Version:**

- (1), (2), (3): Units a, b, and c initially reserve their own 5 iron, 10 silver, and 100 silver, respectively
- (4): Only then does b get the remaining 90 silver from the pool, namely 10 from unit a and 80 from unit d, since these are the only ones that have not yet been reserved
- (5): Unit b takes 10 wood from unit a's pool
- (6): Unit a gives the remaining 5 irons that were not reserved to unit d
- (7): Unit b tries to give 100 silver to c; the only silver that is not yet reserved has unit d (120), so 100 of it is given to c
- (8): Unit b gives 9 wood from unit a to unit d
- (9): Unit c takes 1 wood from unit a from the pool that has not yet been reserved for production.
  So she can only build one spear
- (10): All units pay maintenance (we assume 10 silver per person)

**Result:**

- Unit a has 0 silver, 0 wood, 5 iron
- Unit b has 10 wood, 80 silver (20 used for maintenance of a and b), 10 iron
- Unit c has 190 silver (10 consumed) and 1 spear
- Unit d has 9 wood and 10 silver (10 consumed), 5 iron

## Historical note

In older versions, the material pool was an optional setting that each player could turn on or off.
There were separate settings for silver and other items.
The silver and material pools are now automatically active for all factions and can no longer be deactivated.

## See also

- [[cmd-give]]
- [[cmd-reserve]]
- [[orders-sequence]]

Continue reading: [[war]].

<!-- From [https://wiki.eressea.de/index.php?title=Materialpool&oldid=17006] -->
