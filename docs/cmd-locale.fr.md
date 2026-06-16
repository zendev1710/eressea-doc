---
# cSpell:locale fr
alias: cmd-locale-fr
---
# LOCALE

**`LOCALE`**`en`  
**`LOCALE`**`de`  

L'ordre n'a pas de véritable fonction.
Il peut être utilisé en début du fichier d'ordres, en dehors des unités, pour afficher la langue dans laquelle les ordres sont donnés.  

Il peut être utilisé par des outils pour interpréter correctement les ordres.  
Cependant, le serveur ignore cet ordre, il essaie toujours d'interpréter les ordres dans la langue configurée !

En revanche, s'il est donné **par une unité**, c'est un synonyme de [`LANGUAGE`][language].  
Il est préférable que cet ordre soit passé.

<!-- From [https://wiki.eressea.de/index.php?title=LOCALE&oldid=6692] -->

[language]: [[cmd-language-fr]]
