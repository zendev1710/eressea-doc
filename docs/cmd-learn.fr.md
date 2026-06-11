---
# cSpell:locale fr
alias: cmd-learn-fr
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# LEARN

*Ordre [long][ordres-courts-et-longs]*.

**`LEARN`**` `*`<compétence>`*  
**`LEARN`**`Magic "`*`<École de Magie>`*`"`  

Avec cet ordre, l'unité passe un tour à [apprendre][apprendre-des-competences] une [[competences|compétence]] donnée (voir aussi : [[liste-des-competences]]).  

En moyenne, accéder à un nouveau niveau de compétence par apprentissage pur prend environ un nombre de semaines correspondant au niveau de compétence visé, sans tenir compte des modifications dues à la race ou au terrain.  

Par exemple, passer du niveau 2 au niveau 3 prend environ 3 semaines.  

Généralement, un niveau de compétence de 2 est deux fois plus efficace qu'un niveau de compétence de 1;  
un niveau de compétence de 3 est trois fois plus efficace, et ainsi de suite.  

Avec un ordre de la forme `LEARN <Compétence> 200`, vous pouvez indiquer à des outils tiers (comme [ECheck][echeck-id]) les [[competences|coûts d'apprentissage]] de la compétence (ici 200 silver).  
Ce type d'ordre ne sera pas pris en compte par le serveur lors de la phase d'évaluation (d'exécution des ordres).

## Apprentissage accéléré

Une unité peut bénéficier de [l'enseignement d'un Maître][cmd-teach] pour **réduire de moitié** les temps d'apprentissage habituellement nécessaires.

## Apprentissage automatique

Avec l'ordre [[cmd-learn-auto]], le serveur **tentera d'automatiser** l'apprentissage et l'enseignement dans une région au sein d'une faction.

!!! warning "Attention"
    L'utilisation simultanée d'ordres `TEACH` et `LEARN AUTO` par les unités d'une même faction dans une région n'est pas autorisée.

## École de Magie

L'ordre `LEARN Magic "<Magic School>"` détermine [[magie|l'École de Magie]] pour une faction qui n'en a pas déjà une.

## Voir aussi

- [apprendre][apprendre-des-competences]
- [enseigner][cmd-teach]
- [apprentissage automatisé][cmd-learn-auto]

<!-- From [https://wiki.eressea.de/index.php?title=LEARN&oldid=16727] -->
