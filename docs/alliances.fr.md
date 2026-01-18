---
# cSpell:locale fr
alias: alliances-fr
---
# Alliances

Les alliances constituent l'épine dorsale du monde, que ce soit en temps de guerre, de commerce ou de simple coopération pacifique.
Tu peux nouer des alliances avec d'autres factions non seulement « en esprit », mais aussi les formaliser grâce à l'ordre [[cmd-help]].

Lorsqu'une faction en aide une autre, cela ne signifie pas automatiquement que l'entraide est réciproque.
Seule l'expérience permet de le savoir.
Il existe de bonnes raisons pour lesquelles les droits correspondants ne sont pas accordés d'office : sinon, on pourrait affaiblir les unités ennemies avec des pierres, affaiblir leurs guerriers d'élite avec des paysans ou encore s'accaparer tous les impôts du seigneur local.

Les ordres qui suivent permettent de nouer des alliances de différents types.

## `HELP GIVE`

Tes unités accepteront tous les objets et l'argent de l'autre faction.
Cela équivaut à un [[cmd-contact]] permanent pour [[cmd-give]].

!!! warning "Attention !"
    Pour transférer des personnes ou* des unités à une autre faction avec les ordres [[cmd-give|`GIVE <leur-unité> <nombre> MEN`]] ou [[cmd-give|`GIVE <leur-unité> UNIT`]], la faction destinataire doit utiliser l’ordre [[cmd-contact]] !
    L’ordre `CONTACT` est également nécessaire pour les sorts ciblés.

## `HELP COMBAT`

Tes propres unités prêtes au combat (à l'exception de celles ayant `COMBAT FLEE` ou `COMBAT NOT`) [[guerre|rejoindront un combat]] si la faction alliée est attaquée.

## `HELP SILVER`

Aide la faction alliée en [soutenant] ses unités s'il te reste de l'argent après avoir payé ton propre soutien.
Si les unités de la faction alliée n'ont pas assez d'argent pour se nourrir, tes unités leur en fourniront.
La faction bénéficiaire n'a pas besoin de faire de don pour ce type de transfert.

## `HELP GUARD`

Lève toutes les restrictions de [[cmd-guard]] et étend certaines fonctions utiles à la faction ciblée : normalement, les factions de garde empêchent les autres factions de [[argent|lever des impôts]], de [recruter] ou de [[ressources|produire]] des ressources limitées, et il arrive que certaines unités soient empêchées de [[cmd-guard|traverser]] ta région.
Si ce statut d'assistance est activé, les unités des autres factions sont autorisées à faire tout cela ; elles peuvent donc voyager, exploiter des ressources ou recruter librement.

De plus, la faction alliée peut recevoir des ordres de longue durée [après les combats] si tu défends la région.

Enfin, les unités de la faction alliée peuvent [[cmd-enter|entrer]] dans tes bâtiments et sur tes bateaux.

## `HELP FACTIONSTEALTH`

Si tu déguises tes unités avec [[cmd-hide|`HIDE FACTION NUMBER <faction>`]] en temps qu'autre faction, les factions auxquelles tu as donné ce statut d'aide pourront voir que ces unités camouflées appartiennent en réalité à ta faction.

## `HELP ALL`

Cela englobe dans un seul ordre tous les types d'alliance qui peuvent être nouées décrites ci-dessus.

## Voir aussi

- [[cmd-help]]
- [[cmd-guard]]
- [[cmd-contact]]

Poursuivre la lecture : [[magie]].

<!-- From [https://wiki.eressea.de/index.php?title=Allianz/en&oldid=16781] -->

[soutenant]: ./silver.md#frais-dentretien
[recruter]: ./silver.md#recruter
[après les combats]: ./war.md#fin-du-combat
