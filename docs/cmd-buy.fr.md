---
# cSpell:locale fr
alias: cmd-buy-fr
---

# BUY

*`BUY` est, comme [`SELL`][cmd-sell-fr], un ordre [pseudo-long][ordres-courts-et-longs] [^1].*  

**`BUY <nombre> "produit de luxe"`**  

Si l'unité maîtrise le [commerce][commerce]{title="Trade"}, elle tentera d'acheter le nombre de produits de luxe renseigné.  
Cela n'est possible que si, d'une part, il existe dans la région un poste de commerce ou un château de plus grande taille à proximité duquel le marché peut avoir lieu, et d'autre part, si le produit est effectivement fabriqué dans la région.  
Pour acheter quelque chose, aucun contact avec le seigneur du château n'est nécessaire;  
Néanmoins, il est bien sûr plus diplomatique de demander au préalable...  

Les ordres `BUY` sont généralement accompagnés d'ordres `SELL`.  
Les ordres `BUY` sont prioritaires sur les ventes.  
Ainsi, vous ne pouvez pas utiliser directement les revenus des ventes au cours du même tour pour de nouveaux achats.  
Cela signifie également que les unités qui n'ont pas suffisamment de compétences pour exécuter tous les ordres `BUY` et `SELL` achètent d'abord autant que possible, et s'il reste des points de compétence, vendent.  

Exemple :

```text
UNIT hndl;     Barker [1, $1000]
    ; Trade 3 [180]
    SELL 15 jewel
    SELL 15 Oil
    BUY 10 Incense
```

Ce marchand achètera 10 [encens][encens]{title="Incense"} et vendra un total de 20 bijoux et de l'huile.  
Donc aléatoirement entre 5 et 15 par objet d'échange s'il en a.  

Un seul ordre apparaît dans le rapport standard (NR).  
Mais c'est uniquement pour qu'il n'y ait pas une longue liste d'ordres.  
Dans le rapport informatique (CR) et le [modèle d'ordres][ordres] tous les ordres `BUY` et `SELL` sont répertoriés.  

[^1]: Vous pouvez mettre en œuvre un total de niveau de compétence (commerce) x 10 produits de luxe, mais vous ne pouvez pas passer d'autres ordres longs.

## Voir aussi

- [Le commerce][le-commerce]
- [`SELL`][cmd-sell-fr]

<!-- From [https://wiki.eressea.de/index.php?title=BUY&oldid=16746] -->

[cmd-sell-fr]: [[cmd-sell-fr]]
