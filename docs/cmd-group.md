---
# cSpell:locale en
alias: cmd-group
---
# GROUP

**`GROUP`**`["`*`name`*`"]`  

With the `GROUP` order you can divide the faction into subgroups that have a different [`HELP`][cmd-help] status than the rest of the faction.  
This allows you, for example, to set up an army of mercenaries that will help you on the client's island while the rest of the faction does not.  

Similarly, you can remove all `HELP COMBAT` assignments for participants in a tournament to avoid interfering in a duel.  
Attacks on allies with a faction-camouflaged squad of units are also possible without having to detach `HELP COMBAT` at faction level.  
And if you want to protect your forests from allies, for example, you can set up a troop of forest guards who won't tell anyone, and give `HELP GUARD` order.  
You can also set your own [[cmd-prefix]] for each group.  

For example, a unit gives the order `GROUP "Privateers of the Seas"` to join a group.  
If a group with this name does not yet exist, one will be created that initially always has the same name, with the `HELP` status like the faction has, even if the unit was previously in a different group.  
With `GROUP` without a name, you leave a group.  
If all units leave a group, it is dissolved.  
However, if all units in a group die, the group remains and can be rejoined.  

Each unit can only belong to one group.  
A unit that issues a `HELP` order changes the status of its group if it is assigned to a group, or the status of its faction if it does not belong to a group.  

In a battle, each group becomes a separate army, as happens when units are faction-camouflaged.  

<!-- From [https://wiki.eressea.de/index.php?title=GROUP&oldid=6657] -->
