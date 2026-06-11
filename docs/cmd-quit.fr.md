---
# cSpell:locale fr
alias: cmd-quit-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# QUIT

**`QUIT`**` ``"<mot de passe>"`  

Cela provoque la dissolution de la faction, avec arrêt du jeu.  
Pour des raisons de sécurité, le mot de passe de la faction doit être fourni.  
Cet ordre doit également être donné à une unité.  

Tous les objets, y compris l'argent, de la faction mourante sont donnés aux unités amies qui se trouvent dans la même région.  
La répartition sera effectuée en fonction du nombre de personnes dans la région.  
Seuls ceux qui ont reçu un [`HELP SILVER`][cmd-help] sont considérés comme des amis ici, c'est-à-dire là où il y avait déjà une confiance de la part de la faction partante.  
La faction qui reçoit doit avoir passé l'ordre `HELP GIVE` sur la faction mourante.  
Les objets vont à la première unité de la faction dans la région.  
S'il n'y a pas d'unité amie dans une région, tous les objets vont aux agriculteurs.  
Les membres de la faction sont toujours remis aux agriculteurs (des exceptions s'appliquent aux [Orcs][orcs-fr-id], [Démons][demons-fr-id] et [Monstres][monstres]).  

**`QUIT`**` "<mot de passe>" FACTION `*`faction-id`*  

Il est également possible de fusionner deux factions d'une même race en utilisant l'ordre `QUIT`.  
La deuxième variante est utilisée à cet effet : `QUIT "<mot de passe>" FACTION`` `*`faction-id`*, où l'identifiant de faction de l'autre faction doit être précisé.  

Les conditions requises pour la fusion des factions sont les suivantes :

1. La faction dissoute et la faction cible doivent être de la même race
2. La faction réceptrice doit contacter l'entité émettant l'ordre `QUIT`
3. La faction réceptrice doit bien sûr être dans la même région que l'unité émettant l'ordre `QUIT`
4. Les deux factions doivent exister depuis au moins 50 tours

Si l'une des conditions n'est pas remplie, l'ordre `QUIT` échoue et un message d'erreur apparaît.  

Grâce à la fusion, toutes les unités possédant la race de la faction sont transférées vers la faction spécifiée, et la faction est ensuite supprimée.  
Les unités n'appartenant pas à la race de faction, comme les migrants, les créatures magiques ou les familiers, sont supprimées.  

Si la faction cible possède moins que le nombre maximum autorisé d'unités dotées de compétences limitées (telles que l'alchimie et la magie), celles-ci sont distribuées au hasard.  
Les unités aux compétences limitées qui ne peuvent plus être transférées seront supprimées.  
Si vous souhaitez contrôler cela avec précision, vous devez laisser les unités indésirables oublier la compétence correspondante, au plus tard au cours de la semaine d'abandon du jeu.

Les mages ne sont remis que si les deux factions possèdent la même École de Magie.  
Les familiers sont perdus car ils n'appartiennent pas à la race de faction.  
Les héros sont rétrogradés par capitulation.  

La limite d'unités peut être dépassée lors de la fusion de factions.  
Mais la faction ciblée ne peut alors pas créer de nouvelles unités tant qu'elle n'est pas à nouveau en dessous de la limite.  
De nouvelles unités temporaires ne peuvent pas être créées même si la limite d'unités est inférieure à la limite à la fin du tour !  
Il est donc préférable de s'assurer à l'avance que la faction fusionnée respecte la limite courante.  

!!! warning "Attention"
    Si l'ordre est mal donné, une mort sans reddition peut survenir.  
    Si votre mot de passe est **secret** et que vous souhaitez fusionner avec la faction (enno), l'ordre est :  

    ```text
    QUIT "secret" FACTION enno
    ```

<!-- From [https://wiki.eressea.de/index.php?title=QUIT&oldid=16825] -->
