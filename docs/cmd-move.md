---
# cSpell:locale en
alias: cmd-move
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# MOVE

*[long order][short-and-long-orders].*  

**`MOVE`**` `*`direction`*`[`*`direction`*`]...`  

With the `MOVE` order the unit moves through the world of Eressea.

The cardinal directions in Eressea are northeast, northwest, east, west, southeast and southwest.

| Direction   | Abbreviations  |
|-------------|----------------|
| `East`      | `E`            |
| `Northeast` | `NE`, `NorthE` |
| `Northwest` | `NW`, `NorthW` |
| `Southeast` | `SE`, `SouthE` |
| `Southwest` | `SW`, `SouthW` |
| `West`      | `W`            |

!!! note
    The coordinates (X, Y) are not used for this order.

The order has a special behavior when it comes to [default orders], i.e. orders that the unit receives in the [move template][orders] the following week.
The `MOVE` order is not included in the template.
Instead, the long orders that the unit had in the template last week are adopted.  

Template:

```text
LEARN Ride
@GIVE x 100 Silver
```

Orders sent in :

```text
MOVE w
```

Next week's template:

```text
LEARN Ride
```

## See also

- [[movement]]
- [`ROUTE`][cmd-route]
- [`FOLLOW`][cmd-follow]
- [`DEFAULT`][cmd-default]

<!-- From [https://wiki.eressea.de/index.php?title=MOVE&oldid=16729] -->

[cmd-default]: [[cmd-default]]
[cmd-follow]: [[cmd-follow]]
[cmd-route]: [[cmd-route]]
