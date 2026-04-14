---
# cSpell:locale fr
alias: cmd-message-fr
---
# MESSAGE

**`MESSAGE`**` UNIT `*`unit id`*`"`*`text`*`"`  
**`MESSAGE`**` FACTION `*`faction-id`*`"`*`text`*`"`  
**`MESSAGE`**` SHIP `*`ship-id`*`"`*`text`*`"`  
**`MESSAGE`**` BUILDING `*`building-id`*`"`*`text`*`"`  
**`MESSAGE`**`REGION "`*`text`*`"`  

Cela peut être utilisé pour envoyer des messages à d'autres unités, à d'autres factions ou à toutes les factions d'une région.  

L'expéditeur et le destinataire doivent être dans la même région.  
Si vous envoyez un message à une unité, le message est anonymisé si le destinataire ne peut pas voir l'unité émettrice.  

Avec `MESSAGE BUILDING` et `MESSAGE SHIP`, le message est envoyé à toutes les unités du bâtiment ou du bateau, mais pour une seule unité par faction.  

Comme tous les autres textes, le caractère `\` (barre oblique inversée) peut être utilisé dans le message !  

```text
MESSAGE UNIT z14 "Payez immédiatement Johan le collecteur d'impôts (9i6) 100 Silver chacun, \
sinon nos gardes \
prendront soin de vous !"
```

<!-- From [https://wiki.eressea.de/index.php?title=MESSAGE&oldid=5960] -->
