---
# cSpell:locale fr
alias: alliances-fr
---
<!-- disable some rules due to of autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Alliances

Les alliances constituent l'épine dorsale du monde, que ce soit en temps de guerre, de commerce ou de simple coopération pacifique.  
Vous pouvez nouer des alliances avec d'autres factions non seulement « en esprit », mais aussi les formaliser grâce à l'ordre [[cmd-help]].  

Lorsqu'une faction en aide une autre, cela ne signifie pas automatiquement que l'entraide est réciproque.  
Seule l'expérience permet de le savoir.  

Il existe de bonnes raisons pour lesquelles les droits correspondants ne sont pas accordés d'office;  
on pourrait sinon affaiblir les unités ennemies avec des pierres, affaiblir leurs guerriers d'élite avec des paysans ou encore s'accaparer tous les impôts du seigneur local.  

Les ordres qui suivent permettent de nouer des alliances de différents types.  

## `HELP GIVE`

Tes unités accepteront tous les objets et l'argent de l'autre faction.  
Cela équivaut à un [[cmd-contact]] permanent pour [[cmd-give]].  

!!! warning "Attention !"
    Pour transférer des personnes ou* des unités à une autre faction avec les ordres [`GIVE <leur-unité> <nombre> MEN`][cmd-give] ou [`GIVE <leur-unité> UNIT`][cmd-give], la faction destinataire doit donner l’ordre [[cmd-contact]] !  
    L’ordre `CONTACT` est également nécessaire pour les sorts ciblés.  

## `HELP COMBAT`

Tes propres unités prêtes au combat (à l'exception de celles ayant `COMBAT FLEE` ou `COMBAT NOT`) [rejoindront un combat][guerre] si la faction alliée est attaquée.  

## `HELP SILVER`

Aide la faction alliée en [soutenant][frais-dentretien] ses unités s'il te reste de l'argent après avoir payé ton propre soutien.  
Si les unités de la faction alliée n'ont pas assez d'argent pour se nourrir, tes unités leur en fourniront.  
La faction bénéficiaire n'a pas besoin de faire de don pour ce type de transfert.  

## `HELP GUARD`

Lève toutes les restrictions de [[cmd-guard]] et étend certaines fonctions utiles à la faction ciblée.  
Normalement, les factions de garde empêchent les autres factions de [lever des impôts][argent], de [recruter][recruter] ou de [produire][ressources] des ressources limitées;  
Il arrive aussi que certaines unités soient empêchées de [traverser][cmd-guard] ta région.  
Si ce statut d'aide est activé, les unités des autres factions sont autorisées à faire tout cela ; elles peuvent donc voyager, exploiter des ressources ou recruter librement.  

De plus, la faction alliée peut recevoir des ordres de longue durée [après les combats][fin-du-combat] si vous défendez la région.  

Enfin, les unités de la faction alliée peuvent [entrer][cmd-enter] dans tes bâtiments et sur tes bateaux.  

## `HELP FACTIONSTEALTH`

Si vous déguisez vos unités avec [`HIDE FACTION NUMBER <faction>`][cmd-hide] en temps qu'autre faction, les factions auxquelles vous avez donné ce statut d'aide pourront voir que ces unités camouflées appartiennent en réalité à votre faction.  

## `HELP ALL`

Cela englobe dans un seul ordre tous les types d'alliance qui peuvent être nouées décrites ci-dessus.  

## Voir aussi

- [[cmd-help]]
- [[cmd-guard]]
- [[cmd-contact]]

Poursuivre la lecture : [[magie]].

<!-- From [https://wiki.eressea.de/index.php?title=Allianz/en&oldid=16781] -->
