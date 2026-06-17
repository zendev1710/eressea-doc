---
# cSpell:locale en
alias: cmd-attack
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# ATTACK

**`ATTACK <unit-id>`**  

Pseudo-long order [^1].

This order attacks the affected unit in the current region.  
One order must be given for each unit to be attacked.  

Units that are not [fighting][cmd-combat] at the front (`COMBAT` or `COMBAT AGGRESSIVE`) or rear (`COMBAT REAR` or `COMBAT DEFENSIVE`) cannot attack.  

In the first few weeks, a faction is [immune][puppy-protection] to attacks.  

## See also

- [[war]]
- [`COMBAT`][cmd-combat] order

[^1]: The `ATTACK` order is a [pseudo-long order][short-and-long-orders]:
It is short in the sense that are several `ATTACK` orders can be done;
it is long because it precludes further long orders if a "long" fight actually occurs.
When a “long” fight occurs is explained under [end of battle][the-end].

<!-- From [https://wiki.eressea.de/index.php?title=ATTACK&oldid=16719] -->

[cmd-combat]: [[cmd-combat]]
