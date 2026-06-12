---
# cSpell:locale fr
alias: cmd-name-fr
---
# NAME

**`NAME UNIT "<name>"`*  
**`NAME FOREIGN UNIT <unit-id> "<name>"`**  
**`NAME FOREIGNUNIT UNIT <unit-id> "<name>"`**  
**`NAME FACTION "<name>"`**  
**`NAME FOREIGN FACTION <faction-id> "<name>"`**  
**`NAME CASTLE "<name>"`**  
**`NAME FOREIGN CASTLE <building-id> "<name>"`**  
**`NAME BUILDING "<name>"`**  
**`NAME FOREIGN BUILDING <building-id> "<name>"`**  
**`NAME SHIP "<name>"`**  
**`NAME FOREIGN SHIP <ship-id> "<name>"`**  
**`NAME REGION "<name>"`**  
**`NAME GROUP "<name>"`**  

Renomme l'élément spécifié.  

Un bateau ou un bâtiment ne peut être renommé que si l'unité le contrôle - elle doit donc être la première unité sous le bâtiment ou le bateau dans l'évaluation.  
Une région ne peut être renommée que par le seigneur du château le plus puissant d'une région.  
Les groupes ne peuvent être renommés que par les membres du groupe et le nouveau nom de groupe ne peut pas déjà exister.  

Le nouveau nom peut contenir jusqu’à 127 caractères.  
Des descriptions plus longues peuvent être ajoutées à l'aide de l'ordre [[cmd-describe-fr]].  

Grâce à l'ajout `FOREIGN` et en spécifiant l'identifiant, vous pouvez nommer des unités, des bateaux ou même des bâtiments (pas seulement des châteaux) d'autres factions s'ils n'ont pas encore de nom (càd de libellé « unit abc »).
Vous pouvez même nommer une faction étrangère à condition qu'elle date de plus de dix tours.  

Le nommage de la faction doit également être effectuée par une unité :

```text
ERESSEA 7 "Seven"
    NAME FACTION "Incorrect" ; aucun effet
    UNIT 89
        NAME FACTION "Correct"
```

<!-- From [https://wiki.eressea.de/index.php?title=NAME&oldid=16968] -->
