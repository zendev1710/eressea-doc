---
# cSpell:locale fr
alias: cmd-move-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# MOVE

*Ordre [long][ordres-courts-et-longs].*  

**`MOVE`**` `*`direction`*`[`*`direction`*`]...`  

Avec l'ordre `MOVE` l'unité se déplace dans le monde d'Eressea.  

Les directions cardinales dans Eressea sont : le nord-est, le nord-ouest, l'est, l'ouest, le sud-est et le sud-ouest.  

| Direction   | Abréviations   |
|-------------|----------------|
| `East`      | `E`            |
| `Northeast` | `NE`, `NorthE` |
| `Northwest` | `NW`, `NorthW` |
| `Southeast` | `SE`, `SouthE` |
| `Southwest` | `SW`, `SouthW` |
| `West`      | `W`            |

!!! note
    Les coordonnées (abscisse X et ordonnée Y) ne sont pas utilisées pour cet ordre.

L'ordre a un comportement particulier en ce qui concerne les [ordres par défaut], c'est-à-dire les ordres que l'unité reçoit dans le [[ordres|modèle d'ordres]] la semaine suivante.  
L'ordre `MOVE` n'est pas inclus dans le modèle d'ordres.
Au lieu de cela, les ordres longs que l'unité avait dans le modèle la semaine précédente sont adoptés.  

Modèle :

```text
LEARN Ride
@GIVE x 100 Silver
```

Ordres envoyés :

```text
MOVE w
```

Modèle pour la semaine suivante :

```text
LEARN Ride
```

## Voir aussi

- [[travel]]
- [[cmd-route]]
- [[cmd-follow]]
- [[cmd-default]]

<!-- From [https://wiki.eressea.de/index.php?title=MOVE&oldid=16729] -->
