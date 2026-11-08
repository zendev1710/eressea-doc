---
# cSpell:locale fr
alias: cmd-sell-fr
---

# `SELL`

*`SELL` est, comme [`BUY`][cmd-buy-fr], un ordre [pseudo-long][ordres-courts-et-longs][^1].*  

**`SELL`**` `*`nombre`*` `*`produit de luxe`*  
**`SELL`**` ALL `*`produit de luxe`*  

L'unité compétente en [commerce][commerce]{title="Trade"} peut utiliser cet ordre pour vendre aux agriculteurs les produits de luxe qu'elle possède.  
Cela n'est possible que si, premièrement, il y a un poste de commerce ou un [château de plus grande taille][chateaux]{title="Castle"} dans la région à proximité duquel le marché peut avoir lieu, et deuxièmement, s'il existe une demande pour le produit.  
Pour vendre quelque chose, aucun contact avec le seigneur du château n'est nécessaire;  
Néanmoins, il est bien sûr plus diplomatique de demander au préalable...  

Avec l'ordre `SELL ALL`, la quantité maximale du produit de luxe spécifié est vendue, **en fonction de la demande** dans la région.  
Cela fonctionne également si le volume des transactions diminue au cours de la même semaine (par exemple en raison d'un recrutement).  
Cependant, l'ordre ne doit pas être donné à plus d'une unité par région ni même par plusieurs factions;  
dès que plusieurs unités de la région passent des ordres `SELL`, le résultat de l'ordre `SELL ALL` n'est plus garanti.  

Les ordres `BUY` sont généralement accompagnés d'ordres `SELL`.  
Les achats priment sur les ventes.  
Ainsi, vous ne pouvez pas utiliser directement les revenus des ventes au cours du même tour pour de nouveaux achats.  
Cela signifie également que les unités qui n'ont pas suffisamment de compétences pour exécuter tous les ordres `BUY` et `SELL` achètent d'abord autant que possible, et s'il reste des points de compétence, vendent.  

Un seul ordre apparaît dans le rapport standard (NR).  
Mais c'est uniquement pour qu'il n'y ait pas une longue liste d'ordres.  
Dans le rapport informatique (CR) et le [modèle d'ordres][ordres] tous les ordres `BUY` et `SELL` sont répertoriés.  

[^1]: Vous pouvez choisir un niveau de compétence total (acteur) x vente et acheter 10 produits de luxe, mais vous ne pouvez plus donner d'autres ordres longs.

## Voir aussi

- [Le commerce][le-commerce]
- [`BUY`][cmd-buy-fr]

<!-- From [https://wiki.eressea.de/index.php?title=SELL&oldid=16784] -->

[cmd-buy-fr]: [[cmd-buy-fr]]
