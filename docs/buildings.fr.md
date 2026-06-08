---
# cSpell:locale fr
alias: batiments
---
<!-- disable some rules due to of autorefs plugin usage -->
<!-- markdownlint-disable MD041 MD042 MD052 -->

[](){ #batiments-id }

# Bâtiments

Il existe différents bâtiments à Eressea qui offrent différents avantages.  
À part les châteaux et les monuments, tous les bâtiments ont un coût de maintenance récurrent pour assurer leur fonctionnement.

## Maintenance

Ces coûts de maintenance sont généralement indépendants de la taille du bâtiment et doivent être payés au début du tour par le propriétaire du bâtiment, entre l'ordre [[cmd-give]] et les ordres longs (voir [[sequence-des-ordres]]).  
Une unité ne peut donc pas collecter des impôts et ensuite payer sa maintenance avec l'argent collecté.  
S'il n'y a pas d'argent à ce moment-là, le bâtiment ne fonctionne pas.  

La maintenance est entièrement due dès que le bâtiment est construit; mais pas au tour où il est commencé avec l'ordre [[cmd-make|`MAKE`` `*`type bâtiment`*]].  
Cela a pour conséquence que les bâtiments qui sont achevés en un seul tour ne fonctionnent pas pendant la semaine de construction, car aucune maintenance n'a été payée au début de la semaine.  

Si l'on manque de Silver, ou si l'on n'utilise pas un certain bâtiment au cours d'une semaine et que l'on souhaite économiser sa maintenance, l'unité commandant le bâtiment (voir section suivante) peut faire en sorte que la maintenance ne soit pas payée ce tour en utilisant l'ordre [[cmd-pay-not]].  
Le bâtiment n'a alors bien sûr aucune utilité pendant cette semaine.  

## Unités et bâtiments

Sous un bâtiment sont listées toutes les unités qui se trouvent à l'intérieur.  
La première unité en a le commandement du bâtiment, elle est le propriétaire.  
Elle détermine quelles autres unités peuvent y entrer, et elle peut renommer et décrire le bâtiment.  
L'unité propriétaire du plus grand château d'une région peut même renommer et décrire la région sur laquelle elle règne.  

L'effet des bâtiments (y compris les châteaux) est comptabilisé unité par unité.  
Les unités qui ne rentrent plus - même partiellement - dans la capacité encore disponible ne reçoivent donc pas de bonus grâce au bâtiment - même si elles sont la seule unité !  

S'il y a plusieurs unités dans un bâtiment, elles sont interrogées dans l'ordre, de haut en bas.  
La première unité trop grande "verrouille" alors le bâtiment pour celles qui suivent, même si les unités suivantes pourraient rentrer si la trop grande n'était pas là.  
L'ordre [[cmd-sort]] permet de remédier à cette situation.  

## Construction

Les bâtiments sont construits et améliorés (agrandis) avec l'ordre [[cmd-make|`MAKE`` `*`type bâtiment`*]].  

Comme pour les autres ordres de production, la capacité de construction dépend du niveau de compétence en [maçonnerie][maconnerie]{title="Masonry"}, de la taille de l'unité qui bâtit, et du niveau de compétence minimum requis.  

Une unité peut construire (niveau de compétence x personnes / niveau minimum) points de "taille" par tour;  

Vous pouvez donc facilement construire une tour en un tour avec une unité suffisamment compétente et des pierres en quantité suffisante.  

## Voir aussi

- [Les châteaux][chateaux]{title="Castle"}
- [[batiments-speciaux]]
- [Production][production-fr-id]
- [dépenses][depenses]

Poursuivre la lecture : [les châteaux][chateaux]{title="Castle"}.

<!-- From [https://wiki.eressea.de/index.php?title=Gebäude/fr&oldid=16680] -->
