---
# cSpell:locale fr
alias: tableau-recapitulatif-des-ordres
---
# Tableau récapitulatif des ordres

`C`/`L`indique si l'[[ordres|ordre]] est un ordre Court ou Long.  
Une unité ne peut exécuter qu’un seul ordre long par tour, mais peut exécuter n’importe quel nombre d’ordres courts.

`PL` désigne un [[ordres|ordre Pseudo-Long]], qui peut être donné plusieurs fois à une unité.  
Toutefois, aucun autre ordre long ne peut être exécuté.  

Plus d'information : [[ordres]].

<!-- A link containing brackets (e.g. [BEWACHE  &#91;NICHT&#93;) cannot be used as a reference link -->
<!-- instead, replace by HTML escape codes (e.g. [BEWACHE &#91;[NICHT&#93;) or use inline link [...](<link>) -->

| Ordre                                             | Description                                          | C/L    |
|---------------------------------------------------|------------------------------------------------------|--------|
| [//]                                              | Commentaire durable                                  | C      |
| [`ATTACK <unit id>`]                              | Attaque l'unité                                      | PL[^1] |
| [`BANNER "<texte>"`]                              | Définit le texte pour la liste d'adresses            | C      |
| [`BUY <quantité> <luxury item>`]                  | Acheter des produits de luxe                         | PL[^3] |
| [`CARRY <unit id>`]                               | Emportez d'autres unités avec vous                   | C      |
| [`CAST [REGION x y] [LEVEL n] "<sort>" [...]`]    | Magie                                                | PL[^4] |
| [`CLAIM <quantité> <item>`]                       | Récupère les objets du pool de faction               | C      |
| [[cmd-combat]]                                    | Définit le comportement au combat                    | C      |
| [`COMBAT AGGRESSIVE`]                             |                                                      | C      |
| [`COMBAT DEFENSIVE`]                              |                                                      | C      |
| [`COMBAT FLEE`]                                   |                                                      | C      |
| [`COMBAT HELP [NOT]`]                             | L'unité n'est pas aidée au combat                    | C      |
| [`COMBAT NOT`]                                    |                                                      | C      |
| [`COMBAT REAR`]                                   |                                                      | C      |
| [`COMBATSPELL [LEVEL n] "<sort>" [NOT]`]          | Définit des sorts pour les combats                   | C      |
| [`CONTACT <unit id>`]                             | Contacter les unités étrangères                      | C      |
| [`DEFAULT "Orders"`]                              | Définit l'ordre par défaut pour le prochain tour     | C      |
| [`DESCRIBE BUILDING "<texte>"`]                   |                                                      | C      |
| [`DESCRIBE PRIVATE "<texte>"`]                    |                                                      | C      |
| [`DESCRIBE REGION "<texte>"`]                     |                                                      | C      |
| [`DESCRIBE SHIP "<texte>"`]                       |                                                      | C      |
| [`DESCRIBE UNIT "<texte>"`]                       | Décrit des objets                                    | C      |
| [`DESTROY [<niveau>]`]                            | Réduire la taille d'un bâtiment ou d'un bateau       | L      |
| [`DESTROY [<niveau>] STREET <direction>`]         | Démolir la route                                     | L      |
| [`EMAIL email@adresse`]                           | Définit l'adresse e-mail                             | C      |
| [[cmd-end]]                                       | Termine l'ordre `MAKE TEMP`                          | C      |
| [`ENTER BUILDING <building id>`]                  | Entre dans un bâtiment                               | C      |
| [`ENTER SHIP <ship id>`]                          | Entre dans un bateau                                 | C      |
| [`ENTERTAIN [<montant>]`]                         | Gagne 20 silver ou plus                              | L      |
| [`ERESSEA <faction id> "<mot de passe>"`]         | Commence les ordres pour la faction                  | C      |
| [`FOLLOW SHIP <ship id>`]                         | Suit un bateau                                       | PL[^2] |
| [`FOLLOW UNIT <unit id>`]                         | Suit une unité                                       | PL[^2] |
| [`FORGET <skill>`]                                | Oublie la compétence                                 | C      |
| [`GIVE <unit id> [EACH] <quantité> <item>`]       | Remet des objets                                     | C      |
| [`GIVE <unit id> [EACH] <quantité> MEN`]          | Remet des personnes                                  | C      |
| [`GIVE <unit id> [EACH] <quantité> SHIP`]         | Passe le bateau pour former des convois              | C      |
| [`GIVE <unit id> [EACH] <quantité> SILVER`]       | Remet de l’argent                                    | C      |
| [`GIVE <unit id> herb`]                           | Donne à une unité toutes les plantes                 | C      |
| [`GIVE <unit id> COMMAND`]                        | Remet le commandement du bateau ou bâtiment          | C      |
| [`GIVE <unit id> UNIT`]                           | Transfers unit to foreign faction                    | C      |
| [`GIVE 0 <quantité> <item>`]                      |                                                      | C      |
| [`GIVE 0 <quantité> MEN`]                         |                                                      | C      |
| [`GIVE 0 <quantité> SILVER`]                      | Donne des objets aux agriculteurs                    | C      |
| [`GROUP ["<nom>"]`]                               | Regroupe des unités                                  | C      |
| [`GROW HORSES`]                                   | Élève des chevaux - Seulement dans un haras          | L      |
| [`GUARD [NOT]`]                                   | Garde la région                                      | C      |
| [`HELP <faction id> ALL [NOT]`]                   | Définit ou supprime une alliance unilatérale         | C      |
| [`HELP <faction id> COMBAT [NOT]`]                |                                                      | C      |
| [`HELP <faction id> GIVE [NOT]`]                  |                                                      | C      |
| [`HELP <faction id> GUARD [NOT]`]                 |                                                      | C      |
| [`HELP <faction id> PARTEITARNUNG [NOT]`]         |                                                      | C      |
| [`HELP <faction id> SILVER [NOT]`]                |                                                      | C      |
| [`HIDE [<niveau>]`]                               | Définir le niveau de camouflage                      | C      |
| [`HIDE FACTION [NOT]`]                            | Déguise la faction en anonyme                        | C      |
| [`HIDE FACTION NUMBER <faction id>`]              | Déguise une faction en une autre faction             | C      |
| [`HIDE race`]                                     | Démons : déguisés en une autre race                  | C      |
| [`LANGUAGE en/de`]                                | change la langue de la faction                       | C      |
| [`LEARN <compétence>`]                            | Apprend une compétence                               | L      |
| [`LEARN AUTO <compétence>`]                       | Apprentissage ou enseignement d'une compétence       | L      |
| [[cmd-leave]]                                     | Schiff oder Gebäude verlassen                        | C      |
| [`LOCALE en/de`]                                  | Affiche la langue des ordres                         | C      |
| [[cmd-make]]                                      | Fabrique un objet ou exploite une ressource          | L      |
| [`MAKE [<quantité>] <item>`]                      |                                                      | L      |
| [`MAKE [<quantité>] HERB`]                        | Récolte la plante locale                             | L      |
| [`MAKE [<quantité>] <potion>`]                    | Produit une potion alchimique                        | L      |
| [`MAKE [niveau] <building type> [<building id>]`] | Agrandit ou construit un nouveau bâtiment            | L      |
| [`MAKE [niveau] <ship type>`]                     | Construit un nouveau bateau                          | L      |
| [`MAKE [niveau] SHIP [<ship id>]`]                | Continue à construire le bateau                      | L      |
| [`MAKE [niveau] STREET richtung`]                 | Construit une routes                                 | L      |
| [`MAKE TEMP unit-alias-id ["<nom>"]`]             | Crée une nouvelle unité                              | C      |
| [`MESSAGE BUILDING <building id> "<texte>"`]      | Envoie un message                                    | C      |
| [`MESSAGE FACTION <faction id> "<texte>"`]        |                                                      | C      |
| [`MESSAGE REGION "<texte>"`]                      | Envoie un message                                    | C      |
| [`MESSAGE SHIP <ship id> "<texte>"`]              | Envoie un message                                    | C      |
| [`MESSAGE UNIT <unit id> "<texte>"`]              |                                                      | C      |
| [`MOVE <direction> [<direction>]...`]             | Se déplace                                           | L      |
| [`NAME BUILDING "<nom>"`]                         |                                                      | C      |
| [`NAME FACTION "<nom>"`]                          |                                                      | C      |
| [`NAME STRANGERS FACTION <faction id> "<nom>"`]   |                                                      | C      |
| [`NAME STRANGERS UNIT <unit id> "<nom>"`]         | Nomme des objets étrangers et sans nom               | C      |
| [`NAME STRANGER BUILDING <building id> "<nom>"`]  |                                                      | C      |
| [`NAME STRANGER SHIP <ship id> "<nom>"`]          |                                                      | C      |
| [`NAME REGION "<nom>"`]                           |                                                      | C      |
| [`NAME SHIP "<nom>"`]                             |                                                      | C      |
| [`NAME UNIT "<nom>"`]                             | Nomme des objets                                     | C      |
| [`NEXT`]                                          | Termine les ordres                                   | C      |
| [`NUMBER BUILDING [<nouvel id>]`]                 |                                                      | C      |
| [`NUMBER FACTION [<nouvel id>]`]                  |                                                      | C      |
| [`NUMBER SHIP [<nouvel id>]`]                     |                                                      | C      |
| [`NUMBER UNIT [<nouvel id>]`]                     | Attribue un nouvel identifiant                       | C      |
| [`OPTION ADRESSEN [NOT]`]                         |                                                      | C      |
| [`OPTION AUSWERTUNG [NOT]`]                       | Différents paramètres                                | C      |
| [`OPTION BZIP2 [NOT]`]                            |                                                      | C      |
| [`OPTION COMPUTER [NOT]`]                         |                                                      | C      |
| [`OPTION MATERIALPOOL [NOT]`]                     |                                                      | C      |
| [`OPTION PUNKTE [NOT]`]                           |                                                      | C      |
| [`OPTION SILBERPOOL [NOT]`]                       |                                                      | C      |
| [`OPTION STATISTIK [NOT]`]                        |                                                      | C      |
| [`OPTION TALENTVERSCHIEBUNG [NOT]`]               |                                                      | C      |
| [`OPTION ZIPPED [NOT]`]                           |                                                      | C      |
| [`OPTION ZUGVORLAGE [NOT]`]                       |                                                      | C      |
| [`ORIGIN x y`]                                    | Définit l'origine des coordonnées                    | C      |
| [`PASSWORD "<nouveau mot de passe>"`]             | Définit un nouveau mot de passe                      | C      |
| [`PAY NOT [<building id>]`]                       | Ne paie pas l'entretien d'un bâtiment                | C      |
| [`PIRACY [faction 1] [faction 2]...`]             | Définit le piratage                                  | L      |
| [`PLANT [<quantité>] TREES`]                      | Plante des graines                                   | L      |
| [`PLANT [<quantité>] HERBS`]                      | Plante des herbes                                    | L      |
| [`PLANT [<quantité>] MALLORNSEEDS`]               | Plante des graines                                   | L      |
| [`PLANT [<quantité>] SEEDS`]                      | Plante des graines                                   | L      |
| [`PREFIX [<préfixe>]`]                            | Donne un préfixe au nom de la race                   | C      |
| [[cmd-promote]]                                   | Transforme l'unité en héros                          | C      |
| [`QUIT "<mot de passe>" [FACTION <faction id>]`]  | Quitte le jeu                                        | C      |
| [`RECRUIT <quantité>`]                            | Recrute plus de personnes                            | C      |
| [`REGION x,y`]                                    | Aucune fonction (uniquement pour les outils)         | C      |
| [`RESEARCH HERBS`]                                | Recherche des plantes                                | L      |
| [`RESERVE <quantité> "<item>"`]                   | Gegenstände reservieren                              | C      |
| [`RESERVE <quantité> SILVER`]                     | Reserve silver                                       | C      |
| [`RIDE <unit id>`]                                | Peut être transporté                                 | L      |
| [`ROUTE <direction> [<direction>]...`]            | Se déplace                                           | L      |
| [`SELL ALL <bien de luxe>`]                       |                                                      |        |
| [`SELL <quantité> <bien de luxe>`]                | Vend des produits de luxe                            | PL[^3] |
| [`SHOW "<Item>"`]                                 | Affiche la description d'un objet                    | C      |
| [`SHOW "<Potion>"`]                               | Affiche la description d'une potion                  | C      |
| [`SHOW "<Race>"`]                                 | Affiche la description de la race de l'unité         | C      |
| [`SHOW "<Sort>"`]                                 | Affiche la description d'un sort                     | C      |
| [`SHOW ALL POTIONS`]                              | Affiche la description de toutes les potions connues | C      |
| [`SHOW ALL SPELLS`]                               | Affiche la description de tous les sorts connus      | C      |
| [`SORT AFTER <unit id>`]                          |                                                      | C      |
| [`SORT BEFORE <unit id>`]                         | Tri l'unité dans le rapport                          | C      |
| [`SPY <unit id>`]                                 | Espionne une unité                                   | L      |
| [`STEAL <unit id>`]                               | Vole 50 silver ou plus                               | L      |
| [`TAX [<montant>]`]                               | Collecte les impôts                                  | L      |
| [`TEACH <unit id> [<unit id>...]`]                | Enseigne à des unités                                | L      |
| [`UNIT <unit id>`]                                | Commence les ordres d'une unité                      | C      |
| [`USE [<quantité>] <potion>`]                     | Utilise une potion alchimique                        | C      |
| [[cmd-work]]                                      | Gagne 10 silver ou plus                              | L      |

[^1]: l'ordre n'est pas toujours long, voir [Fin de la bataille]
[^2]: si l'unité suivie ne bouge pas, un autre ordre long peut être exécuté à la place
[^3]: un ordre `BUY` et plusieurs ordres `SELL` peuvent être combinés
[^4]: une unité peut lancer plusieurs sorts

## Voir aussi

- [[ordres]]
- [[sequence-des-ordres]]

Poursuivre la lecture : [[premier-tour]].

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[//]: ./cmd-comment-slash.md

[`ATTACK <unit id>`]: ./cmd-attack.md
[`BANNER "<texte>"`]: ./cmd-banner.md
[`CLAIM <quantité> <item>`]: ./cmd-claim.md
[`STEAL <unit id>`]: ./camouflage.md
[`NAME UNIT "<nom>"`]: ./cmd-name.md
[`NAME FACTION "<nom>"`]: ./cmd-name.md
[`NAME BUILDING "<nom>"`]: ./cmd-name.md
[`NAME SHIP "<nom>"`]: ./cmd-name.md
[`NAME REGION "<nom>"`]: ./cmd-name.md
[`NAME STRANGERS UNIT <unit id> "<nom>"`]: ./cmd-name.md
[`NAME STRANGER SHIP <ship id> "<nom>"`]: ./cmd-name.md
[`NAME STRANGER BUILDING <building id> "<nom>"`]: ./cmd-name.md
[`NAME STRANGERS FACTION <faction id> "<nom>"`]: ./cmd-name.md
[`USE [<quantité>] <potion>`]: ./cmd-use.md
[`DESCRIBE UNIT "<texte>"`]: ./cmd-describe.md
[`DESCRIBE PRIVAT "<texte>"`]: ./cmd-describe.md
[`DESCRIBE BUILDING "<texte>"`]: ./cmd-describe.md
[`DESCRIBE SHIP "<texte>"`]: ./cmd-]describe.md
[`DESCRIBE REGION "<texte>"`]: ./cmd-describe.md
[`ENTER BUILDING <building id>`]: ./cmd-enter.md
[`ENTER SHIP <ship id>`]: ./cmd-enter.md
[`GUARD [NOT]`]: ./cmd-guard.md
[`PAY NOT [<building id>]`]: ./cmd-pay-not.md
[`MESSAGE REGION "<texte>"`]: ./cmd-message.md
[`MESSAGE SHIP <ship id> "<texte>"`]: ./cmd-message.md
[`MESSAGE BUILDING <building id> "<texte>"`]: ./cmd-message.md
[`MESSAGE UNIT <unit id> "<texte>"`]: ./cmd-message.md
[`MESSAGE FACTION <faction id> "<texte>"`]: ./cmd-message.md
[`DEFAULT "Ordres"`]: ./cmd-default.md
[`UNIT <unit id>`]: ./cmd-unit.md
[`EMAIL email@adresse`]: ./cmd-email.md
[`END`]: ./cmd-end.md
[`ERESSEA <faction id> "passwort"`]: ./cmd-eressea.md
[`RIDE <unit id>`]: ./cmd-ride.md
[`FOLLOW UNIT <unit id>`]: ./cmd-follow.md
[`FOLLOW SHIP <ship id>`]: ./cmd-follow.md
[`RESEARCH HERBS`]: ./cmd-research.md
[`GIVE <unit id> herb`]: ./cmd-give.md
[`GIVE <unit id> KOMMANDO`]: ./cmd-give.md
[`GIVE <unit id> UNIT`]: ./cmd-give.md
[`GIVE <unit id> [EACH] <quantité> MEN`]: ./cmd-give.md
[`GIVE <unit id> [EACH] <quantité> SHIP`]: ./cmd-give.md
[`GIVE <unit id> [EACH] <quantité> SILVER`]: ./cmd-give.md
[`GIVE <unit id> [EACH] <quantité> <item>`]: ./cmd-give.md
[`GIVE 0 <quantité> SILVER`]: ./cmd-give.md
[`GIVE 0 <quantité> MEN`]: ./cmd-give.md
[`GIVE 0 <quantité> <item>`]: ./cmd-give.md
[`GROUP ["<nom>"]`]: ./cmd-group.md
[`HELP <faction id> ALL [NOT]`]: ./cmd-help.md
[`HELP <faction id> GIVE [NOT]`]: ./cmd-help.md
[`HELP <faction id> COMBAT [NOT]`]: ./cmd-help.md
[`HELP <faction id> GUARD [NOT]`]: ./cmd-help.md
[`HELP <faction id> SILVER [NOT]`]: ./cmd-help.md
[`HELP <faction id> PARTEITARNUNG [NOT]`]: ./cmd-help.md
[`COMBAT`]: ./cmd-combat.md
[`COMBAT AGGRESSIVE`]: ./cmd-combat.md
[`COMBAT DEFENSIVE``]: ./cmd-combat.md
[`COMBAT FLEE`]: ./cmd-combat.md
[`COMBAT HELP [NOT]`]: ./cmd-combat.md
[`COMBAT REAR`]: ./cmd-combat.md
[`COMBAT NOT`]: ./cmd-combat.md
[`COMBATSPELL [LEVEL n] "zauberspruch" [NOT]`]: ./cmd-combatspell.md
[`BUY <quantité> luxusgut`]: ./cmd-buy.md
[`CONTACT <unit id>`]: ./cmd-contact.md
[`TEACH <unit id> [<unit id> etc.]`]: ./cmd-teach.md
[`LEARN <skill>`]: ./Learn.md
[`LEARN AUTO <skill>`]: ./Learn-auto.md
[`LOCALE en/de`]: ./Locale.md
[`MAKE TEMP unit-alias-nr ["<nom>"]`]: ./cmd-make.md
[`MAKE [niveau] gebäude-typ [<building id>]`]: ./cmd-make.md
[`MAKE [niveau] schiffstyp`]: ./cmd-make.md
[`MAKE [niveau] SHIP [<ship id>]`]: ./cmd-make.md
[`MAKE`]: ./cmd-make.md
[`MAKE [niveau] STRASSE richtung`]: ./cmd-make.md
[`MAKE [<quantité>] <herb>`]: ./cmd-make.md
[`MAKE [<quantité>] <potion>`]: ./cmd-make.md
[`MAKE [<quantité>] <item>`]: ./cmd-make.md
[`MOVE richtung [richtung etc.]`]: ./cmd-move.md
[`NEXT`]: ./cmd-next.md
[`NUMBER UNIT [neue\_nr]`]: ./cmd-number.md
[`NUMBER BUILDING [neue\_nr]`]: ./cmd-number.md
[`NUMBER FACTION [neue\_nr]`]: ./cmd-number.md
[`NUMBER SHIP [neue\_nr]`]: ./cmd-number.md
[`OPTION AUSWERTUNG [NOT]`]: ./cmd-option.md
[`OPTION COMPUTER [NOT]`]: ./cmd-option.md
[`OPTION ZIPPED [NOT]`]: ./cmd-option.md
[`OPTION BZIP2 [NOT]`]: ./cmd-option.md
[`OPTION SILBERPOOL [NOT]`]: ./cmd-option.md
[`OPTION MATERIALPOOL [NOT]`]: ./cmd-option.md
[`OPTION ADRESSEN [NOT]`]: ./cmd-option.md
[`OPTION ZUGVORLAGE [NOT]`]: ./cmd-option.md
[`OPTION STATISTIK [NOT]`]: ./cmd-option.md
[`OPTION TALENTVERSCHIEBUNG [NOT]`]: ./cmd-option.md
[`OPTION PUNKTE [NOT]`]: ./cmd-option.md
[`PASSWORD "neues-passwort"`]: ./cmd-password.md
[`PLANT [<quantité>] herb`]: ./cmd-plant.md
[`PLANT [<quantité>] BÄUME`]: ./cmd-plant.md
[`PLANT [<quantité>] MALLORNSAMEN`]: ./cmd-plant.md
[`PLANT [<quantité>] SAMEN`]: ./cmd-plant.md
[`PIRACY [partei\_1] [partei\_2] [...]`]: ./cmd-piracy.md
[`PREFIX [präfix]`]: ./cmd-prefix.md
[`REGION x,y`]: ./cmd-region.md
[`RECRUIT <quantité>`]: ./silver.md#recruter
[`RESERVE <quantité> "<item>"`]: ./cmd-reserve.md
[`RESERVE <quantité> SILVER`]: ./cmd-reserve.md
[`ROUTE richtung [richtung etc.]`]: ./cmd-route.md
[`SORT BEFORE <unit id>`]: ./cmd-sort.md
[`SORT AFTER <unit id>`]: ./cmd-sort.md
[`SPY <unit id>`]: ./cmd-spy.md
[`LANGUAGE en/de`]: ./Language.md
[`QUIT <passwort> [FACTION <faction id>]`]: ./cmd-quit.md
[`HIDE [niveau]`]: ./cmd-hide.md
[`HIDE rasse`]: ./cmd-hide.md
[`HIDE FACTION [NOT]`]: ./cmd-hide.md
[`HIDE FACTION NUMBER nummer`]: ./cmd-hide.md
[`CARRY <unit id>`]: ./cmd-carry.md
[`TAX [betrag]`]: ./cmd-tax.md
[`ENTERTAIN [betrag]`]: ./cmd-entertain.md
[`ORIGIN x y`]: ./cmd-origin.md
[`FORGET <skill>`]: ./cmd-forget.md
[`SELL <quantité> luxusgut`]: ./cmd-sell.md
[`SELL ALL luxusgut`]: ./cmd-sell.md
[`LEAVE`]: ./Leave.md
[`CAST [REGION x y] [LEVEL n] "zauberspruch" [...]`]: ./cmd-cast.md
[`SHOW ALL ZAUBER`]: ./cmd-show.md
[`SHOW ALL TRÄNKE`]: ./cmd-show.md
[`SHOW "Gegenstand"`]: ./cmd-show.md
[`SHOW "Potion"`]: ./cmd-show.md
[`SHOW "Zauberspruch"`]: ./cmd-show.md
[`SHOW "Rasse"`]: ./cmd-show.md
[`DESTROY [stufen]`]: ./cmd-destroy.md
[`GROW PFERDE`]: ./cmd-grow.md

[Fin de la bataille]: ./war.md#fin-du-combat
