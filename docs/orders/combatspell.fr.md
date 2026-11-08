---
# cSpell:locale fr
alias: cmd-combatspell-fr
---

# `COMBATSPELL`

**`COMBATSPELL`**` [LEVEL `*`n`*`] "<sort>"`  
**`COMBATSPELL`**`["<sort>"] NOT`  

Le sort mentionné est choisi et activé - en fonction du sort - comme sort de pré-combat, sort de post-combat ou sort de combat standard.  

En option, un niveau peut être spécifié, ce qui peut être utile, par exemple pour conserver l'aura pour un sort d'après-combat.  
Les sorts choisis sont automatiquement utilisés par l'unité si elle entre en combat.

Avec `COMBATSPELL <sort> NOT` ou `COMBATSPELL NOT`, le réglage d'un ou de tous les sorts de combat est désactivé.  

Tous les sorts ne sont pas des sorts de combat : consultez la description des sorts que vous recevez dans le jeu.  
La description d'un sort peut être à nouveau affichée en utilisant l'ordre [`SHOW`][cmd-show-fr].  

## Voir aussi

- [La magie][magie-fr-id]
- [`CAST`][cmd-cast-fr]

<!-- From [https://wiki.eressea.de/index.php?title=COMBATSPELL&oldid=16818] -->

[cmd-cast-fr]: [[cmd-cast-fr]]
[cmd-show-fr]: [[cmd-show-fr]]
