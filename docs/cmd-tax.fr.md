---
# cSpell:locale fr
alias: cmd-tax-fr
---
# `TAX`

*Ordre [long]*.

**`TAX`**` ``[`*`montant`*`]`  

Avec cet ordre, une unité armée et entraînée collecte les impôts auprès des agriculteurs.  
Pour ce faire, elle a besoin d'une arme et de maîtriser la [[liste-des-competences|compétence]] correspondante, ainsi que de la compétence de [collecte des impôts].  
Jusqu'à **20 Silver** sont collectées auprès des agriculteurs par personne [[arme-et-pret-au-combat|armée et formée à l'arme portée]] et par niveau de compétence en matière de collecte des impôts.  

!!! note
    Les catapultes ne conviennent pas en tant qu'arme pour collecter des impôts.  

Si vous précisez un montant, un maximum de ce montant sera collecté en taxes.  
Seules des dizaines peuvent être spécifiées; dans le cas contraire, le montant est arrondi à la dizaine suivante.  

!!! warning "Attention"
    Les agriculteurs donnent même l’argent dont ils ont réellement besoin pour survivre, **ce qui peut conduire à la [famine]**.  

Si plusieurs factions passent l'ordre de collecte des impôts, l’argent résultant de la collecte sera réparti entre les différentes factions.  
Si vous souhaitez empêcher les factions non alliées de collecter l'impôt, vous devrez donner l'ordre [[cmd-guard]].  

!!! note
    La compétence de collecte des impôts n’augmente pas avec son utilisation.

## Voir aussi

- [[money]]

<!-- From [https://wiki.eressea.de/index.php?title=TAX&oldid=16747] -->

[long]: ./commands.md#ordres-courts-et-longs
[famine]: ./silver.md#famine
[collecte des impôts]: ./skills-list.md#taxation
