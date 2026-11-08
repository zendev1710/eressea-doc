---
# cSpell:locale fr
alias: cmd-describe-fr
---
# `DESCRIBE`

**`DESCRIBE UNIT`**`"`*`text`*`"`  
**`DESCRIBE BUILDING`**`"`*`text`*`"`  
**`DESCRIBE SHIP`**`"`*`text`*`"`  
**`DESCRIBE REGION`**`"`*`text`*`"`  
**`DESCRIBE PRIVATE`**`"`*`text`*`"`  

La description de l'objet spécifiée est modifiée.
Cette description est spécifiée par objet et peut contenir jusqu'à **8 191** caractères.  

L'ordinateur n'attribue pas de descriptions lors de la création d'objets.  

Les mêmes restrictions s'appliquent aux bateaux, aux bâtiments et aux régions que lors du nommage des objets.
Un bâtiment ou un bateau ne peut être décrit que si l'unité a le commandement du bâtiment ou du bateau (c'est-à-dire qu'elle doit être la première unité sous le bâtiment ou le bateau dans l'évaluation).  
Une région ne peut être décrite que par le seigneur du château le plus puissant qui y est présent.

Avec `DESCRIBE PRIVATE` vous pouvez donner à l'unité passant l'ordre une description "privée" que seul le propriétaire de l'unité peut voir.  

Les descriptions longues doivent être écrites avec le séparateur `\` (barre oblique inverse).  
La nouvelle ligne après un `\` ne doit pas commencer par des espaces.

```text
DESCRIBE UNIT "Les fourmis coupeuses de feuilles n'ont pas besoin de\
dormir et leurs ouvrières sont constamment concentrées sur une efficacité maximal\
e. Tout ce qu'elles font et pensent sous leur exosquelette noir\
est lié au collectif de la colonie."
```

Il n'est actuellement pas possible d'insérer des paragraphes et des césures dans une description.

<!-- From [https://wiki.eressea.de/index.php?title=DESCRIBE&oldid=7442] -->
