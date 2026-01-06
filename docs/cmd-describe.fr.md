---
# cSpell:locale fr, en
alias: cmd-describe-fr
---
# DESCRIBE

**`DESCRIBE UNIT`**`"`*`text`*`"`  
**`DESCRIBE BUILDING`**`"`*`text`*`"`  
**`DESCRIBE SHIP`**`"`*`text`*`"`  
**`DESCRIBE REGION`**`"`*`text`*`"`  
**`DESCRIBE PRIVATE`**`"`*`text`*`"`  

La description de l'objet spécifiée est modifiée.
Cette description est spécifiée par objet et peut contenir jusqu'à **8 191** caractères.  

L'ordinateur n'attribue pas de descriptions lors de la création d'objets.  

Les mêmes restrictions s'appliquent aux bateaux, aux bâtiments et aux régions que lors du nommage des objets.
Un bâtiment ou un bateau ne peut être décrit que si l'unité a le commandement du bâtiment ou du bateau (c'est-à-dire qu'elle doit être la première unité sous le bâtiment ou le navire dans l'évaluation).  
Une région ne peut être décrite que par le seigneur du château le plus puissant qui y est présent.

Avec `DESCRIBE PRIVATE` vous pouvez donner à l'unité passant l'ordre une description "privée" que seul le propriétaire de l'unité peut voir.  

Les descriptions longues doivent être écrites avec le séparateur `\` (barre oblique inverse).
La nouvelle ligne après un `\` ne doit pas commencer par des espaces.

<!-- TODO: clarify text below -->
```text
DESCRIBE UNIT "Leaf-cutting ants don't need one\
Sleep and its workers are always focused on maximum efficiency\
Everything they do and think under their black cover refers to\
then it also das Kollektiv des Staates."
```

Il n'est actuellement pas possible d'insérer des paragraphes et des césures dans une description.

<!-- From [https://wiki.eressea.de/index.php?title=DESCRIBE&oldid=7442] -->
