---
# cSpell:locale fr
alias: cmd-help-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# HELP

<!-- TODO: replace PARTEITARNUNG -->
**`HELP`**` `*`faction-id`*`GIVE [NOT]`  
**`HELP`**` `*`faction-id`*`COMBAT [NOT]`  
**`HELP`**` `*`faction-id`*`SILVER [NOT]`  
**`HELP`**` `*`faction-id`*`GUARD [NOT]`  
**`HELP`**` `*`faction-id`*`PARTEITARNUNG [NOT]`  
**`HELP`**` `*`faction-id`*`ALL [NOT]`  

Cet ordre permet à une faction d'attribuer différents niveaux de soutien à une autre faction.
Cette dernière ne sera pas informée de ce changement de statut et n'est pas tenue d'avoir le même statut.

Plus d'information sur les différents modes : [les alliances][alliances].

Exemple :

```text
HELP 7 GIVE NOT
```

Expérience de jeu (Solthar) :

- `HELP`` `*`faction-id`* sans paramètres a le même effet que `HELP`` `*`faction-id`*` ``ALL`
- `HELP`` `*`faction-id`*` ``NOT` a le même effet que `HELP`` `*`faction-id`*` ``ALL NOT`

<!-- From [https://wiki.eressea.de/index.php?title=HELP&oldid=7439] -->
