---
# cSpell:locale en
alias: orders
---
# Orders

## Conventions

```text
GIVE unit-id [number|ALL] [item]
```

The following conventions apply in these rules:

- Keywords like `GIVE`, `MAKE`, `NOT` are in capital letters.
  This is not mandatory, but we recommend it. Placeholders are in lowercase letter.
  They should not be adopted literally, but must be replaced by concrete values, for example unit-id by the number of the desired unit.
  Sometimes we also write this as &lt;unit-id&gt;, in which case the `<` and `>` symbols are **NOT** to be included.
- Words in \[\] brackets are optional.
  So they can be omitted, but they change the meaning of the order.
  Alternatives are through `|` separated.

The example above allows `GIVE 123 EVERYTHING` or `GIVE abc 4 sword`.  

## Syntax

Except for the password and the faction id, the server is case-insensitive.  
`learN croSSBow` is completely legal (but not recommended as it is difficult for humans to read).  

Items should always be in the **singular** stand, so `GIVE xyz 100 Sword` or `MAKE 15 Stone`.  
Items often appear in the majority in the report and are mostly understood in orders, but you should be aware that the server does not understand natural language, even if the orders look almost like that.  

Many orders can be shortened, although you should not overdo it as this is prone to errors.  
For instance, `LEA` matches `LEARN` and `LEAVE`, and it is therefore noted as an error;  
So here you should use at least 4 letters.  

In addition, overly cryptic abbreviations are not particularly readable when you look through your orders later...  
It's still safest if you don't abbreviate your orders, especially since there may be orders, items and skills that are intentionally not in the instructions but start out similar to well-known orders, items and skills.  

Texts that contain spaces must be enclosed in quotation marks (""), or the spaces must be replaced by `~` (tilde):

```text
NAME Ship "Big Blue Bird"
GIVE unit 5 Water~of~life
COMBAT REAR
```

It is possible to use and combine single quotes (`'`).  
It's better to try out what exactly comes out, because the exact behavior can always change.  

```text
MESSAGE REGION 'Say "Friend" and enter'
NAME CASTLE xyz "Helm's Deep"
DEFAULT 'MAKE 1 "Water of Life"'
```

Also called masking (escaping) by the character `\` is possible, but not necessarily recommended:

```text
MESSAGE REGION "Say \"Friend\" and enter"
NAME CASTLE xyz 'Helm\'s Deep'
DEFAULT 'MAKE 1 Water\~of\~Life'
```

By the way, it is not necessary to limit yourself to the Latin alphabet.  
The full Unicode character set is possible in names and descriptions:

```text
NAME UNIT "Σωκράτης"
MESSAGE REGION "🨀 شاه مات"
```

Of course, you should make sure that you are understood by others.  

<!-- TODO: rework ZUGVORLAGE notion-->
## Orders template

The easiest way is to use the orders template at the end of the evaluation.  
All units are listed there so that you don't forget anyone.  
If you don't send in any orders, the orders in the orders template will still be executed automatically.  
Even if you only send orders for some of your units, the orders in the orders template will be executed for the remaining units.  
If your evaluation does not contain an orders template (with the `.txt` extension), you can reactivate it with the [`OPTION ZUGVORLAGE`][cmd-option] order.  

## Short and long orders

There are short and long orders in Eressea.  

The long orders are:

- [[cmd-work]],
- [[cmd-attack]],
- [[cmd-steal]],
- [[cmd-ride]],
- [[cmd-follow]],
- [[cmd-research]],
- [[cmd-buy]],
- [[cmd-teach]],
- [[cmd-learn]],
- [[cmd-make]] (exception: `MAKE TEMP`),
- [[cmd-move]],
- [[cmd-plant]],
- [[cmd-piracy]],
- [[cmd-route]],
- [[cmd-spy]],
- [[cmd-tax]],
- [[cmd-entertain]],
- [[cmd-sell]],
- [[cmd-cast]],
- [[cmd-destroy]],
- [[cmd-grow]].

All other orders are short orders ([short description] of all orders).  

You can enter as many short orders as you want per unit.  
A unit can usually only have one long order.  

There are a few exceptions, called pseudo-long orders (`ATTACK, FOLLOW, BUY, SELL, CAST`), of which several may be given under certain circumstances.  
Further information can be found in the description of the individual orders.  

If a unit is given a long order, it will adopt it as the default order, replacing the previous default order.  
The default order is always in the [orders template] as a suggestion for a long order.  
So you only need to give a horse trainer the order `MAKE Horse` once, and this order will appear in the orders template until she receives another long order (e.g. `LEARN Tazming`).  
It makes sense that not all long orders are adopted as default orders.  
This applies, for example, to `MOVE`, `ATTACK` and `FOLLOW`.  
For more information about default orders, see the [[cmd-default]] order page.  

A unit that worked one turn, moved north the next turn, and then received no more orders will settle down and work again the following turn (unless, of course, it receives another long order that turn).  

Please note that only one command per unit will be displayed in the Normal Report (NR).  
The remaining default orders are displayed in the orders template (NR) and in the Computer Report (CR).  

## Execute short orders permanently

Sometimes it makes sense to execute a short order every round, such as `GIVE`, because the miners should constantly deliver the mined iron to the forge.  

To do this, you can put an @ (at sign, spider monkey) before each short order.  
Such orders are simply copied into the orders template for the next round and - unless you delete them again - executed again.  

 **An example** :

```text
UNIT berg;               miners [5,400$,U500]
    MAKE iron
    @GIVE schm ALL Iron; always deliver to the blacksmith
UNIT schm;               wrought [3,1343$,U250]
    MAKE Sword
```

!!! note
    There is a cap on the number of orders stored for a unit.  
    This is currently 128 orders, which should easily be enough for most purposes.

## Suppress errors

It may happen that you consciously accept errors when executing a order.  
By prefixing it with an exclamation mark (!) you can suppress the server messages concerning this order.  

**An example**:

```text
UNIT berg;         Miners
    MAKE iron
    !@GIVE tran ALL iron;   The van isn't always there; we don't want an error message about this
UNIT tran;        Transporter
    ROUTE w PAUSE e PAUSE;   We commute between two regions
    !@GIVE schm ALL iron;   In the west we hand the iron over to the blacksmiths
```

Of course, this carries the risk that you will miss errors that you did not expect.  

## See also

- [[orders-sequence]]
- [[orders-list]]
- [[cmd-default]]

Continue reading: [[orders-sequence]].

<!-- From [https://wiki.eressea.de/index.php?title=Befehl&oldid=16787] -->
