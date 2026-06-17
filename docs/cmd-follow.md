---
# cSpell:locale en
alias: cmd-follow
---
# FOLLOW

**`FOLLOW`**` UNIT `*`unit-ID`*  
**`FOLLOW`**` SHIP `*`ship-ID`*`[`*`speed`*`]`  

This can be used to follow units or ships.  

With `FOLLOW UNIT`*`unit-ID`* your own unit will "watch" the specified unit and follow it when it moves.  
However, if the pursued unit is faster than the following unit, it escapes pursuit.  
The pursuers follow the pursued unit as far as possible.  
Units traveling by ship cannot be tracked with `FOLLOW UNIT`.  
Nor can captains use this to move their ship.  
Instead, they would abandon ship and follow the unit on foot if possible.  

If the pursued unit has not issued a movement order (this includes `MOVE, ROUTE, RIDE, FOLLOW`, but not `PIRACY`), the pursuing unit can execute its long order.  

With `FOLLOW SHIP`*`ship-id`* you can follow ships that have crossed the region in the current or previous round.  
If the captain has given the order `FOLLOW SHIP`*`ship-id`*, the ship will then follow the course of the specified ship until it is overtaken - if your own ship is fast enough.  
If the optional parameter *Speed* is specified, the pursuing ship will sail a maximum of this many regions.  

!!! warning "Attention"
    You cannot follow ships that have `FOLLOW SHIP` or `PIRACY` as their order.

`FOLLOW SHIP`, like `FOLLOW UNIT`, is only a long order if the target has a move order and then replaces all other long order.  

`FOLLOW` only lasts in the round in which the order is given.  
If the order is to last longer, it must be preceded by a `@`.  

```text
UNIT 87b6
    @FOLLOW UNIT hz7
    ENTERTAIN
```

Unit *87b6* will now watch unit *hz7* and follow it as it moves.  
Otherwise, she will make money from entertainment.  
With the `@` both orders are retained.  

Player experience (Solthar):  

It is possible to use a unit A to follow a unit B, which in turn follows a third unit C.  
However, this means that A no longer executes a long order, because at this point the server assumes that unit B is also moving, regardless of whether unit C is also moving.  

It is not possible to meaningfully issue multiple FOLLOW orders.  
Only the first one is always executed.  

## See also

- [[movement]]
- [`MOVE`][cmd-move]
- [`ROUTE`][cmd-route]
- [`RIDE`][cmd-ride]
- [`CARRY`][cmd-carry]
- [`PIRACY`][cmd-piracy]

<!-- From [https://wiki.eressea.de/index.php?title=FOLLOW/en&oldid=8282] -->

[cmd-carry]: [[cmd-carry]]
[cmd-move]: [[cmd-move]]
[cmd-piracy]: [[cmd-piracy]]
[cmd-ride]: [[cmd-ride]]
[cmd-route]: [[cmd-route]]
