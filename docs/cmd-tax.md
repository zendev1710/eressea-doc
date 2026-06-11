---
# cSpell:locale en
alias: cmd-tax
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# TAX

*[long order][short-and-long-orders].*

**`TAX`**`[`*`Amount`*`]`  

With this order, armed and trained units collect taxes from the farmers.  
To do this, they need a weapon and the corresponding [skill][skills-list], and also the [taxation skill][skill-taxation-id].  
Up to **20 Silver** are collected from farmers per [[armed]] person (and trained in this weapon) and per taxation skill level.  

!!! note
    A catapult is not suitable as a weapon for collecting taxes.

If you specify an amount, a maximum of this amount will be collected in taxes.  
Only full 10s can be specified; everything else is rounded down to the next full 10s.  

The farmers even give away silver that they actually need to survive, which can lead to [hunger][starvation].  

If several factions want to collect taxes, the money is divided between the factions.  
If you want to prevent non-allied factions from collecting taxes, you can do this with the [[cmd-guard]] order.  

!!! note
    Taxation skill does not increase during use.

## See also

- [[money]]

<!-- From [https://wiki.eressea.de/index.php?title=TAX&oldid=16747] -->
