---
# cSpell:locale en
alias: cmd-quit
---

# QUIT

**`QUIT`**`"<password>"`  

This causes the faction to disband and no longer play.  
For security purposes, the faction's password must be provided.  
This order must also be given to a unit.  

All items, including Silver, from the dying faction are given to friendly units that are in the same region as units of the dying faction.  
If there are several people in the region, it will be divided according to the number of people in the region.  
Only those who have been given a [HELP SILVER][cmd-help] are considered friends here, i.e. where there was already trust on the part of the departing faction.  
The receiving faction must have put HELP GIVE on the dying faction.  
The items go to the faction's first unit in the region.  
If there is no friendly unit in a region, all items go to the farmers.  
The faction's people are always handed over to the farmers (exceptions apply to [Orcs][orcs-id], [Demons][demons-id] and [Monsters]).  

**`QUIT`**` "<password>" FACTION `*`faction-id`*  

It is also possible to merge two factions of the same race using the `QUIT` order.  
The second variant is used for this purpose `QUIT "<password>" FACTION`` `*`faction-id`*, where the faction number of the other faction must be specified.  

Requirements for the merger are:

1. Dissolving faction and target faction must be of the same race
2. The receiving faction must contact the entity issuing the `QUIT` order
3. The receiving faction must of course be in the same region as the unit issuing the `QUIT` order
4. Both factions must be at least 50 rounds old

If one of the requirements is not met, the QUIT order is not executed and an error message appears.  

Through the merger, all units that have the faction's race are transferred to the specified faction and the faction is then deleted.  
Units that do not belong to the faction race, such as migrants, magical creatures or familiars, are deleted.  

If the target faction has fewer than the maximum permitted number of units with limited skills (such as alchemy and magic), these are handed over at random.  
Units with limited skills that can no longer be transferred will be deleted.  
If you want to control this precisely, you should let the unwanted units forget about the corresponding skill in the QUIT week at the latest.  

Magicians are only handed over if both factions have the same Magic School.  
Familiars are deleted because they do not belong to the faction race.  
Heroes are demoted by surrender.  

The unit limit can be exceeded through faction merger.  
But then the target faction cannot create new units until it is below the limit again.  
New Temp units cannot be created even if the unit limit would be below the limit at the end of the round!  
It is therefore better to ensure in advance that the merged faction complies with the current limit.  

!!! warning "Caution"
    If the order is given incorrectly, a death without surrender can occur.  
    If your password is *secret* and you want to merge with the faction (enno), the order is:  

    ```text
    QUIT "secret" FACTION enno
    ```

<!-- From [https://wiki.eressea.de/index.php?title=QUIT&oldid=16825] -->

[cmd-help]: [[cmd-help]]
