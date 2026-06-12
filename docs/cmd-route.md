---
# cSpell:locale en
alias: cmd-route
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# ROUTE

*[long order][short-and-long-orders].*  

**`ROUTE`**` `*`direction`*`[`*`direction`*`...]`  

With this order, the unit moves through the world of Eressea in the same way as with the [[cmd-move]] order.  

With that `ROUTE` order you can, however, create a chain of movement so that a unit always travels between two or more points or completes a long route until it reaches its destination.  
All movements that have been processed are returned to the back `ROUTE` order attached.  

To cancel a movement prematurely (e.g. for ships that are not supposed to sail as far as they can), you can use a `PAUSE` (can be abbreviated with `P`).  
Once a unit has completed its movement, next comes a `PAUSE`, this is added at the end even though the unit is already stopping.  
Two in a row `PAUSE` orders, on the other hand, ensure that the unit stops and no longer moves without the player's intervention.  

A rider can travel three regions by road. He gets the following `ROUTE` order:

```text
ROUTE NE East Pause East East SE West West Pause SW West NW
```

Next round the command looks like this:

```text
ROUTE East East SE West West Pause SW West NW NE East Pause
```

And in the round after that:

```text
ROUTE West West Pause SW West NW NE East Pause East East SE
```

And in the round after that:

```text
ROUTE SW West NW NE East Pause East East SE West West Pause
```

And finally again like at the beginning.

## See also

- [[movement]]
- [[cmd-move]]
- [[cmd-follow]]

<!-- From [https://wiki.eressea.de/index.php?title=ROUTE&oldid=16732] -->
