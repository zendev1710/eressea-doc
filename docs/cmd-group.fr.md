---
# cSpell:locale fr
alias: cmd-group-fr
---
# `GROUP`

**`GROUP`**`["`*`name`*`"]`  

Avec l4ORDRE `GROUP`, vous pouvez diviser la faction en sous-groupes qui ont un statut [[cmd-help|`HELP`]] différent du reste de la faction.  
Cela vous permet par exemple de mettre en place une armée de mercenaires qui vous aideront sur une île en cours de prospection alors que le reste de la faction ne le fera pas.  

De même, vous pouvez supprimer tous les statuts `HELP COMBAT` des participants à un tournoi pour éviter d'interférer dans un duel.  
Les attaques contre les alliés avec une escouade d'unités camouflées par une faction sont également possibles? sans avoir à détacher le statut `HELP COMBAT` au niveau de la faction.  
Et si vous souhaitez protéger vos forêts des alliés, par exemple, vous pouvez constituer une troupe de gardes forestiers qui n'en parleront à personne. et passer l'ordre `HELP GUARD`.
Vous pouvez également définir votre propre [[cmd-prefix|préfixe]] pour chaque groupe.

Par exemple, une unité donne l'ordre `GROUP "Corsaires des Mers"` pour rejoindre un groupe.  
S'il n'existe pas encore de groupe portant ce nom, il en sera créé un qui portera initialement toujours le même nom. avec statut `HELP` identique à celui de la faction, même si l'unité était auparavant dans un groupe différent.  
Avec le simple ordre `GROUP` sans nom, vous quittez le groupe auquel vous appartenez.  
Si toutes les unités quittent un groupe, celui-ci est dissous.  
Cependant, si toutes les unités d'un groupe meurent, le groupe reste et peut être rejoint.  

Chaque unité ne peut appartenir qu'à un seul groupe.  
Une unité qui émet un ordre `HELP` change le statut de son groupe s'il est affecté à un groupe, ou le statut de sa faction s'il n'appartient pas à un groupe.  

Dans une bataille, chaque groupe devient une armée distincte, comme cela se produit lorsque les unités sont camouflées par une faction.  

<!-- From [https://wiki.eressea.de/index.php?title=GROUP&oldid=6657] -->
