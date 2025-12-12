# Alliances

Les alliances constituent l'épine dorsale du monde, que ce soit en temps de guerre, de commerce ou de simple coopération pacifique.
Tu peux nouer des alliances avec d'autes factions non seulement « en esprit », mais aussi les formaliser grâce à l'ordre [`HELP`].

Lorsqu'une faction en aide une autre, cela ne signifie pas automatiquement que l'entraide est réciproque. Seule l'expérience permet de le savoir. Il existe de bonnes raisons pour lesquelles les droits correspondants ne sont pas accordés d'office : sinon, on pourrait affaiblir les unités ennemies avec des pierres, affaiblir leurs guerriers d'élite avec des paysans ou encore s'accaparer tous les impôts du seigneur local.

Les ordres qui suivent permettent de nouer des alliances de différents types.

## `HELP GIVE`

Tes unités accepteront tous les objets et l'argent de l'autre faction. Cela équivaut à un [`CONTACT`] permanent pour [`GIVE`].

!!! warning "Attention !"
    Pour transférer des personnes ou* des unités à une autre faction avec les ordres [`GIVE <leur-unité> <nombre> MEN`][`GIVE`] ou [`GIVE <leur-unité> UNIT`][`GIVE`], la faction destinataire doit utiliser l’ordre [`CONTACT`] ! L’ordre `CONTACT` est également nécessaire pour les sorts ciblés.

## `HELP COMBAT`

Tes propres unités prêtes au combat (à l'exception de celles ayant `COMBAT FLEE` ou `COMBAT NOT`) [rejoindront un combat] si la faction alliée est attaquée.

## `HELP SILVER`

Aide la faction alliée en [soutenant] ses unités s'il te reste de l'argent après avoir payé ton propre soutien. Si les unités de la faction alliée n'ont pas assez d'argent pour se nourrir, tes unités leur en fourniront. La faction bénéficiaire n'a pas besoin de faire de don pour ce type de transfert.

## `HELP GUARD`

Lève toutes les restrictions de [`GUARD`] et étend certaines fonctions utiles à la faction ciblée : normalement, les factions de garde empêchent les autres factions de [lever des impôts], de [recruter] ou de [produire] des ressources limitées, et il arrive que certaines unités soient empêchées de [traverser][`GUARD`] ta région. Si ce statut d'assistance est activé, les unités des autres factions sont autorisées à faire tout cela ; elles peuvent donc voyager, exploiter des ressources ou recruter librement.

De plus, la faction alliée peut recevoir des ordres de longue durée [après les combats] si tu défends la région.

Enfin, les unités de la faction alliée peuvent [entrer] dans tes bâtiments et sur tes bateaux.

## `HELP FACTIONSTEALTH`

Si tu déguises tes unités avec [`HIDE FACTION NUMBER <faction>`] comme appartenant à une autre faction, les factions auxquelles tu as donné ce statut d'aide peuvent voir que ces unités camouflées appartiennent en réalité à ta faction.

## `HELP ALL`

Cela englobe dans un seul ordre tous les types d'alliance qui peuvent être nouées décrites ci-dessus.

## Voir aussi

- [`HELP`]
- [`GUARD`]
- [`CONTACT`]

Poursuivre la lecture : [magic].

<!-- From [https://wiki.eressea.de/index.php?title=Allianz/en&oldid=16781] -->

<!-- -->
[magic]: ./magic.md "Magie"  
[`HELP`]: ./cmd-help.md "HELP"
[`CONTACT`]: ./cmd-contact.md "CONTACT"
[`GIVE`]: ./cmd-give.md "GIVE"
[rejoindront un combat]: ./war.md "La guerre"
[soutenant]: ./silver.md#frais-dentretien "Argent"
[`GUARD`]: ./cmd-guard.md "GUARD"
[lever des impôts]: ./silver.md "Argent"
[recruter]: ./silver.md#recruiting "RECRUIT"
[produire]: ./resources.md "Ressources"
[après les combats]: ./war.md#kampfende "La guerre"
[entrer]: ./cmd-enter.md "ENTER"
[`HIDE FACTION NUMBER <faction>`]: ./cmd-hide.md "HIDE"
<!-- -->
