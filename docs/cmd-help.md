---
# cSpell:locale en
alias: cmd-help
---
# HELP

<!-- TODO: replace PARTEITARNUNG -->
**`HELP`**` `*`faction-id`*`GIVE [NOT]`  
**`HELP`**` `*`faction-id`*`COMBAT [NOT]`  
**`HELP`**` `*`faction-id`*`SILVER [NOT]`  
**`HELP`**` `*`faction-id`*`GUARD [NOT]`  
**`HELP`**` `*`faction-id`*`PARTEITARNUNG [NOT]`  
**`HELP`**` `*`faction-id`*`ALL [NOT]`  

This order allows a faction to set different levels of support for another faction.
The counterparty does not learn about a change in status and does not have to have the same status.

The individual modes are explained in the section about [alliances][alliances-id].

Example:

```text
HELP 7 GIVE NOT
```

Player experience (Solthar):

- `HELP`` `*`faction-id`* without parameters does the same as `HELP`` `*`faction-id`* ` ALL`
- `HELP`` `*`faction-id`*` ``NOT` does the same thing as `HELP`` `*`faction-id`*` ``ALL NOT`

<!-- From [https://wiki.eressea.de/index.php?title=HELP&oldid=7439] -->
