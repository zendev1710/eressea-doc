---
# cSpell:locale fr
alias: cmd-follow-fr
---
# FOLLOW

**`FOLLOW`**` UNIT `*`unit-ID`*  
**`FOLLOW`**` SHIP `*`ship-ID`*`[`*`vitesse`*`]`  

Peut être utilisé pour suivre une unité ou un bateau.  

Avec `FOLLOW UNIT`*`unit-id`*, votre propre unité "surveillera" l'unité spécifiée et la suivra lorsqu'elle se déplacera.  
Cependant, si l’unité poursuivie est plus rapide que l’unité poursuivante, elle échappe à la poursuite.  
Les poursuivants suivent l'unité poursuivie aussi loin que possible.  
Les unités voyageant par bateau ne peuvent pas être suivies avec `FOLLOW UNIT`.  
Les capitaines ne peuvent pas non plus l'utiliser pour déplacer leur bateau.  
Au lieu de cela, ils abandonneraient le bateau et suivraient l'unité à pied si possible.  

Si l'unité poursuivie n'a pas émis d'ordre de mouvement (cela inclut `MOVE, ROUTE, RIDE, FOLLOW`, mais pas `PIRACY`), l'unité poursuivante peut exécuter son ordre long.  

Avec `FOLLOW SHIP`*`ship-id`* vous pouvez suivre les bateaux qui ont traversé la région au cours du tour en cours ou précédent.  
Si le capitaine a donné l'ordre `FOLLOW SHIP`*`ship-id`*, le bateau suivra alors la route du bateau spécifié jusqu'à ce qu'il soit rattrapé - si votre propre bateau est suffisamment rapide.  
Si le paramètre optionnel « Vitesse » est spécifié, le bateau poursuivant naviguera au maximum dans ce nombre de régions.  

!!! warning "Attention"
    Vous ne pouvez pas suivre les bateaux qui ont comme ordre `FOLLOW SHIP` ou `PIRACY`.

`FOLLOW SHIP`, comme `FOLLOW UNIT`, n'est un ordre long que si la cible a un ordre de déplacement et remplace ensuite toutes les autres ordres longs.  

`FOLLOW` ne dure que pendant le tour au cours duquel l'ordre est donné.  
Si l'ordre doit durer plus longtemps, il doit être précédé d'un `@`.  

```text
UNIT 87b6
    @FOLLOW UNIT hz7
    ENTERTAIN
```

L'unité *87b6* surveillera l'unité *hz7* et la suivra dans ses mouvements.  
Si le déplacement échoue, elle gagnera de l'argent grâce au divertissement.  
Avec le `@` les deux ordres sont conservés pour les tours suivants.  

Expérience de jeu (Solthar) :  

Il est possible d’utiliser une unité A pour suivre une unité B, qui à son tour suit une troisième unité C.  
Cependant, cela signifie que A n'exécute plus d'ordre long, car à ce stade, le serveur suppose que l'unité B se déplace également, que l'unité C se déplace ou non.

Il n'est pas possible d'émettre explicitement plusieurs ordres `FOLLOW`.  
Seul le premier est toujours exécuté.  

## Voir aussi

- [[deplacements]]
- [`MOVE`][cmd-move-fr]
- [`ROUTE`][cmd-route-fr]
- [`RIDE`][cmd-ride-fr]
- [`CARRY`][cmd-carry-fr]
- [`PIRACY`][cmd-piracy-fr]

<!-- From [https://wiki.eressea.de/index.php?title=FOLLOW/fr&oldid=8283] -->

[cmd-carry-fr]: [[cmd-carry-fr]]
[cmd-move-fr]: [[cmd-move-fr]]
[cmd-piracy-fr]: [[cmd-piracy-fr]]
[cmd-route-fr]: [[cmd-route-fr]]
[cmd-ride-fr]: [[cmd-ride-fr]]
