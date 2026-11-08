---
# cSpell:locale en
alias: cmd-enter
---

# `ENTER`

**`ENTER`**` BUILDING `*`building-id`*  
**`ENTER`**` SHIP `*`ship-id`*  

Enter the specified [building][buildings-id] or [ship][ships-id].  

The unit [in command][units-and-buildings] of the building or ship must allow entry.
She does this if she belongs to her own faction, has set [`HELP GUARD`][cmd-help] for her own faction or gives the [`CONTACT`][cmd-contact] order for the unit this round.
Otherwise access will be denied.

An ENTER implies [`LEAVE`][cmd-leave] if the unit is on a ship or in a building.

<!-- From [https://wiki.eressea.de/index.php?title=ENTER&oldid=7174] -->

[cmd-contact]: [[cmd-contact]]
[cmd-help]: [[cmd-help]]
[cmd-leave]: [[cmd-leave]]
