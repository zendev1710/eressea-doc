---
# cSpell:locale fr, en
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

`FOLLOW SHIP`, comme `FOLLOW UNIT`, n'est un ordre longu que si la cible a un ordre de déplacement et remplace ensuite toutes les autres ordres longs.

`FOLLOW` ne dure que pendant le tour au cours duquel la commande est donnée.
Si la commande doit durer plus longtemps, elle doit être précédée d'un `@`.

```text
    UNIT 87b6
        @FOLLOW UNIT hz7
        ENTERTAIN
```

L'unité *87b6* surveillera l'unité *hz7* et la suivra dans ses mouvements.
Si le déplacement échoue, elle gagnera de l'argent grâce au divertissement.
Avec le `@` les deux commandes sont conservées pour les tours suivants.

Expérience de jeu (Solthar):

<!-- TODO: translate in french -->
It is possible to use a unit A to follow a unit B, which in turn follows a third unit C.
However, this means that A no longer executes a long command, because at this point the server assumes that unit B is also moving, regardless of whether unit C is also moving.

It is not possible to meaningfully issue multiple FOLLOW commands.
Only the first one is always executed.

## Voir aussi

- [[travel]]
- [[cmd-move]]
- [[cmd-route]]
- [[cmd-ride]]
- [[cmd-carry]]
- [[cmd-piracy]]

<!-- From [https://wiki.eressea.de/index.php?title=FOLLOW/fr&oldid=8283] -->
