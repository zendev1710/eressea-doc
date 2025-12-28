---
# cSpell:locale en
alias: cmd-default
---
# DEFAULT

**`DEFAULT`**`"`*`order`*`"`  

`DEFAULT`changes the [[orders|command]] that a unit normally issues **in the next week** would execute:

## Orders template and default orders

After I have sent in my orders and the server has created the evaluation, specific orders come for each unit zurück.
These are the default orders.
They will be executed next week if you don't send in orders *for this unit*.
You will receive the default orders with the report as a text file (also called a move template or orders template) if you do not use them with [[cmd-option|`OPTION ZUGVORLAGE NOT`]] switched off.
They are also included in the computer report (CR).
The normal report (NR) always only contains the first long default order.
So you can't see all the default orders there.

All [long orders] are normally included in a unit's default orders.
Exceptions are `ATTACK`, `FOLLOW` and `MOVE`.
In addition, all [[comment-withslashes|`//`]] and all orders beginning with `@` are adopted.
The spelling may be standardized.

Orders sent in:

```text
UNIT abc
; only 10 this week
BUY 10 Balm
SELL 100 Oil
// buy more balm next week
@GIVE xyz ALL Balm ; Transporter
GIVE abc 100 Silver
RECRUIT 1
```

Default orders for next week:

```text
UNIT abc
BUY 10 Balm
SELL 100 Oil
// buy more balm next week
@GIVE xyz ALL Balm ; Transporter
```

By the way, what happens if the unit has illegally received several long orders (for example `LEARN` and `WORK`) is not precisely defined.
The same applies to other invalid orders.

## The DEFAULT order

The `DEFAULT` order changes this behavior by changing the default orders that come back from the server.
If the unit has received a `DEFAULT` order, its **long** orders not included in the template.
[long orders] (with `//`) and short `@` orders are accepted.
The given orders are validated to a certain extent.
Invalid orders are therefore not accepted.
However, this test has limitations, it is better not to rely on it.

You can also insert short orders using the `DEFAULT` order.

Orders sent in:

```text
UNIT abc
; this week only 10
BUY 10 Balm
SELL 100 Öl
// learn next week
@GIVE xyz ALL Balm ; Transporter
GIVE abc 100 Silver
RECRUIT 1
DEFAULT "GIVE 123 50 Silver; don't forget"
DEFAULT "LEARN Trade" ; Deletes BUY und SELL
DEFAULT "XXX" ; no order, will not be accepted
```

Default orders for next week:

```text
UNIT abc
GIVE 123 50 Silver; don't forget
LEARN Trade
// learn next week
@GIVE xyz ALL Balm ; Transporter
```

If your default orders need to contain quotes, there are currently a few ways to achieve this:

```text
DEFAULT "CAST 'Create a Ring of Invisibility'"
DEFAULT 'CAST "Create a Ring of Invisibility"'
DEFAULT "NAME UNIT \"Bob's Builders\""
DEFAULT "MAKE 1 'Water of life'"
```

## The MOVE order

The `MOVE` order plays a special role: it is not included in the template.
Instead, the long orders that the unit had in the template last week are adopted, but only long orders.

Default orders:

```text
LEARN Ride
@GIVE 0 10 Silver
// no comment
```

Orders sent in:

```text
MOVE e
```

Default commands for next week:

```text
LEARN Ride
```

What happens if both `MOVE` and `DEFAULT` are in play?

Template:

```text
WORK
// now to the west
```

Orders sent in:

```text
DEFAULT "LEARN Endurance"
// now learn
MOVE w
```

Default orders for next week:

```text
LEARN Endurance
// now learn
```

`DEFAULT` deletes them here too **long** default orders (here `WORK`) and reset them.

It is possible to set `MOVE` with `DEFAULT`.

Template:

```text
WORK
@GIVE 0 1 Silver
```

Orders sent in:

```text
DEFAULT "MOVE o"
WORK
@GIVE 0 2 Silver
```

Default orders for next week:

```text
MOVE o
@GIVE 0 2 Silver
```

Default orders for the week after next if no other orders are sent in for the unit:

```text
@GIVE 0 2 Silver
```

Here too, the unit would not carry out a long order.

!!! note
    There is a cap on the number of orders stored for a unit.
    This is currently 128 orders, which should easily be enough for most purposes.

Player experience (Solthar):

`DEFAULT DEFAULT` ???

Is it possible to nest DEFAULT orders to make commands for several weeks in advance?
Well, something like `DEFAULT "DEFAULT 'LEARN Endurance'"` apparently works as you would expect, but the game management would rather not make any guarantees about it.
Please do not submit bug reports if something like this doesn't work as expected.
Scripting languages ​​such as [[vorlage]], [[extended-commands]] or [[fftools]] are better suited for such projects.

## See also

- [[orders]]
- [[sending-orders]]

<!-- From [https://wiki.eressea.de/index.php?title=DEFAULT&oldid=16788] -->

[long orders]: ./commands.md#short-and-long-orders
