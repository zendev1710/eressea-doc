---
# cSpell:locale en
alias: cmd-destroy
---

# `DESTROY`

*[long order][short-and-long-orders].*

**`DESTROY [<level>]`**  
**`DESTROY [<level>] STREET <direction>`**  

A unit in command of a [ship][ships-id] or [building][buildings-id] can shrink or destroy it at any time using this order.  
She doesn't need any skill for that.  

For **buildings**, the *level* parameter denotes the **size points** by which the building should be reduced in size.  
For **ships**, it denotes the **percentage** points.  

If no parameter is specified, the structure is completely destroyed.  

However, ships can only be reduced in size or sunk in coastal areas.  
The crew refuses to damage the ship on the high seas!

With `DESTROY [`*`level`*`] STREET`*`direction`* you can demolish or damage a [road][roads-id].  
<!-- TODO: check if the sentence below is related to DESTROY -->
No faction is allowed to guard the region that has not set `HELP GUARD` as its own faction.  
To damage or destroy a road, a unit requires the [roadwork][roadwork] skill.
You can destroy one size point per skill point.  

A unit can only destroy one structure (building, ship or road) per week.

<!-- From [https://wiki.eressea.de/index.php?title=DESTROY&oldid=16738] -->
