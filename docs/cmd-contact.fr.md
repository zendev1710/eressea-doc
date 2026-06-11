---
# cSpell:locale fr
alias: cmd-contact-fr
---
# CONTACT

**`CONTACT`**` UNIT `*`unit-id`*  
**`CONTACT`**` PARTEI `*`faction-id`*  
**`CONTACT`**` `*`unit-id`*  

Vous n'êtes normalement pas autorisé à donner quoi que ce soit aux unités de factions étrangères, à moins que vous ne soyez un allié de cette faction.  

Pour permettre cela ponctuellement, il existe l'ordre `CONTACT`.  
Dans ce tour -et seulement dans ce tour- l'unité donnant l'ordre se comporte envers l'unité spécifiée comme si elle était alliée avec elle (voir aussi sous [[cmd-help]]), c'est-à-dire qu'elle accepte des objets, de l'argent et des personnes.  
Les factions non alliées peuvent également pénétrer dans les châteaux et les navires, recruter des personnes et extraire des ressources de cette manière.  

`CONTACT UNIT`donne les droits à une seule unité, tandis que `CONTACT FACTION` autorise toutes les unités de la faction en question dans une région.  
L' ordre `CONTACT <unit-id>` est autorisé pour des raisons historiques, mais devrait être remplacé par `CONTACT UNIT <unit-id>`.

**Exemples :**

```text
PARTEI ff "FooBar"
    UNIT a
        GIVE x 1000 Silver ; Tribut!
        [...]

PARTEI 300 "BarFoo"
    UNIT x
        CONTACT UNIT a ; autoriser le paiement
```

L'unité *a* peut donner à l'unité *x* les 1000 Silver.  
Si *x*est la seule unité de garde dans la région, *a* est également autorisé à recruter et à collecter des impôts.  

L'unité *b* de la faction *ff* n'est pas autorisée à faire quoi que ce soit de tout cela.  
Pour que cela soit possible, l'unité *x* doit donner l'ordre `CONTACT FACTION ff`.  

L'unité *x* et l'unité *y* d'une faction gardent la région.  
Pour que l'unité *a* recrute, *x* et *y* doivent tous deux passer un ordre `CONTACT` (`CONTACT UNIT a` ou `CONTACT FACTION ff`).

## Differences avec `HELP`

`CONTACT` a une fonction similaire à [`HELP GIVE + HELP GUARD`][cmd-help], mais n'est pas tout à fait identique :
<!-- TODO: compare second item in enumeration with original wiki documentation -->
- `CONTACT` est requis pour certaines actions spécifiques non prises en charge par `HELP GIVE` et `HELP GUARD`, comme [`GIVE MEN`][cmd-give] et certains sorts
- `HELP` ferme `HELP SILVER, HELP COMBAT` et `HELP PARTEITARNUNG`
- `CONTACT` s'applique uniquement au tour en cours et uniquement à l'unité émettant l'ordre
- `HELP` est permanent et s'applique à toutes les unités de la faction ou du groupe (et à toutes les unités de la faction ciblée par l'ordre)

<!-- From [https://wiki.eressea.de/index.php?title=CONTACT&oldid=13303] -->
