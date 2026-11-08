---
# cSpell:locale en
alias: cmd-message
---
# `MESSAGE`

**`MESSAGE`**` UNIT `*`unit id`*`"`*`text`*`"`  
**`MESSAGE`**` FACTION `*`faction-id`*`"`*`text`*`"`  
**`MESSAGE`**` SHIP `*`ship-id`*`"`*`text`*`"`  
**`MESSAGE`**` BUILDING `*`building-id`*`"`*`text`*`"`  
**`MESSAGE`**`REGION "`*`text`*`"`  

This can be used to send messages to other units, to other factions, or to all factions in a region.  

The sender and recipient must be in the same region.  
If you send a message to a unit, the message is anonymized if the recipient cannot see the sending unit.  

With `MESSAGE BUILDING` and `MESSAGE SHIP` the message goes to all units in the building or on the ship, but for only one unit per faction.  

Like all other texts, `\` (backslash) can be used in the message !  

```text
MESSAGE UNIT z14 "Immediately pay Johan the tax collector (9i6) 100 Silver each, \
otherwise our guards will be\
take care of you!"
```

<!-- From [https://wiki.eressea.de/index.php?title=MESSAGE&oldid=5960] -->
