---
# cSpell:locale fr, en
alias: cmd-buy-fr
---
# BUY

**`BUY`**[<sup>`(l)`</sup>]` `*`number`*` `*`luxury goods`*  

Si l'unité possède la compétence [Commerce], elle tentera d'acheter le nombre de produits de luxe renseigné.
Cela n'est possible que si, d'une part, il existe dans la région un poste de commerce ou un château de plus grande taille à proximité duquel le marché peut avoir lieu, et d'autre part, si le produit est effectivement fabriqué dans la région.
In order to buy something, no contact with the lord of the castle is necessary; Nevertheless, it is of course more diplomatic to ask beforehand...

[<sup>(l)</sup>][<sup>`(l)`</sup>] `BUY` is like [[cmd-sell]] a ["pseudo-long" command].
You can implement a total of skill level (trading) x 10 luxury goods, but you cannot give any other long orders.
BUY orders have priority over sales.

Les ordres `BUY` sont généralement accompagnés d'ordres `SELL`.
Cependant, vous ne pouvez pas utiliser directement les revenus des ventes au cours du même tour pour de nouveaux achats.
Cela signifie également que les unités qui n'ont pas suffisamment de compétences pour exécuter tous les ordres `BUY` et `SELL` achètent d'abord autant que possible, et s'il reste des points de compétence, vendent.

Example:

```text
UNIT hndl;     Barker [1, $1000]
    ; Trade 3 [180]
    SELL 15 jewel
    SELL 15 Oil
    BUY 10 Incense
```

Ce marchand achètera 10 encens et vendra un total de 20 bijoux et de l'huile.
Donc aléatoirement entre 5 et 15 par objet d'échange s'il en a.

Une seule commande apparaît dans le rapport standard.
Mais c'est uniquement pour qu'il n'y ait pas une longue liste d'ordres.
Dans le rapport informatique et le [[ordres|modèle d'ordres]] tous les ordres `BUY` et `SELL` sont répertoriés.

## Voir aussi

- [trade]
- [[cmd-sell]]

<!-- From [https://wiki.eressea.de/index.php?title=BUY&oldid=16746] -->

[<sup>`(l)`</sup>]: ./commands.md#ordres-courts-et-longs
[trade]: ./silver.md#commerce
