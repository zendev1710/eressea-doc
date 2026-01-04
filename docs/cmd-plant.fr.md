---
# cSpell:locale fr, en
alias: cmd-plant-fr
---
# PLANT

*Ordre [long].*  

**`PLANT`**`[`*`quantité`*`] HERBS`  
**`PLANT`**`[`*`quantité`*`] TREES`  
**`PLANT`**`[`*`quantité`*`] MALLORNSEEDS`  
**`PLANT`**`[`*`quantité`*`] SEEDS`  

Cet ordre peut être utilisé pour redonner de la verdure à une région vidée ou dévastée, ou pour contrôler la reproduction naturelle des arbres.  

L'ordre `PLANT HERBS` nécessite au moins un **niveau 6** en [Herboristerie].  
L'unité tente de planter le nombre spécifié de plantes, jusqu'à un maximum d'une plante par niveau de compétence;  
Pour ce faire, elle a besoin du nombre approprié de plantes du type correspondant et d'une et une seule fiole de la potion [[tableaux-potions-et-plantes|Water of life]].  
Il n'est possible de replanter que la plante originaire de la région.

Dans la région, les plantes nouvellement plantées se multiplient très rapidement (sauf en hiver) dès lors qu'elles ne sont pas cueillies pendant quelques semaines.

Si votre niveau de compétence est faible, les plantes peuvent être cassées lors de la plantation.  
À partir du niveau 10, cela ne devrait plus se produire.  

La culture des plantes vise surtout à réactiver des régions dont toutes les plantes ont été récoltées et où plus rien ne pousse.  

With `PLANT [`*`quantité`*`] TREES` ou `PLANT [`*`quantité`*`] SEEDS`, l'unité tente de planter le nombre spécifié de graines, jusqu'à un maximum d'une graine par niveau de compétence.  
Seules les graines de Mallorn peuvent être plantées dans les régions de Mallorn.  
Pour cela, il faut être au moins de **niveau 7** en Herboristerie.  

Pour planter des graines normales, il faut être au moins de **niveau 6** en Herboristerie.  

**Au printemps**, une unité d'au moins **niveau 12** en Herboristerie pourra directement planter une pousse (jeune arbre) toutes les 10 graines.  
Vous devez soigneusement réfléchir si cela est souhaitable ou non.  

Expérience de jeu (Solthar):

Les ordres `PLANT` et `GROW` sont des ordres interchangeables (synonymes).  

Vous pouvez faire pousser des graines et "planter" des chevaux.  
Mais ce n’est pas recommandé.  

## Voir aussi

- [[cmd-grow|`GROW HORSES`]]
- [[resources]]

<!-- From [https://wiki.eressea.de/index.php?title=PLANT&oldid=16730] -->

[long]: ./commands.md#ordres-courts-et-longs
[Herboristerie]: ./skills-list.md#herboristerie
