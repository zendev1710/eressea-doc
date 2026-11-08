---
# cSpell:locale en
alias: cmd-locale
---
# `LOCALE`

**`LOCALE`**`en`  
**`LOCALE`**`de`  

The order has no real function.
It can be used at the beginning of orders file, outside of units, to display the language of the orders.  

It can be used by tools to correctly interpret the orders.  
However, the server doesn't care, it always tries to interpret the orders in the currently set language!

On the other hand, if it is given **by a unit**, it is a synonym of [`LANGUAGE`][cmd-language].  
Preferably that order should be given.

<!-- From [https://wiki.eressea.de/index.php?title=LOCALE&oldid=6692] -->

[cmd-language]: [[cmd-language]]
