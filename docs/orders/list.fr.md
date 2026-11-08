---
# cSpell:locale fr
alias: tableau-recapitulatif-des-ordres
---

# Tableau récapitulatif des ordres

`C`/`L`indique si l'[ordre][ordres] est un ordre Court ou Long.  
Une unité ne peut exécuter qu’un seul ordre long par tour, mais peut exécuter n’importe quel nombre d’ordres courts.

`PL` désigne un [ordre Pseudo-Long][ordres], qui peut être donné plusieurs fois à une unité.  
Toutefois, aucun autre ordre long ne peut être exécuté.  

Plus d'information : [ordres][ordres].

| Ordre                                                               | Description                                          | C/L    |
|---------------------------------------------------------------------|------------------------------------------------------|--------|
| [//]                                                                | Commentaire durable                                  | C      |
| [`ATTACK <unit-id>`][cmd-attack-fr]                                 | Attaque l'unité                                      | PL[^1] |
| [`BANNER "<texte>"`][cmd-banner-fr]                                 | Définit le texte pour la liste d'adresses            | C      |
| [`BUY <quantité> <bien de luxe>`][cmd-buy-fr]                       | Acheter des produits de luxe                         | PL[^3] |
| [`CARRY <unit-id>`][cmd-carry-fr]                                   | Emportez d'autres unités avec vous                   | C      |
| [`CAST [REGION <x> <y>] [LEVEL <n>] "<sort>" ...`][cmd-cast-fr]     | Magie                                                | PL[^4] |
| [`CLAIM <quantité> <item>`][cmd-claim-fr]                           | Récupère les objets du pool de faction               | C      |
| [`COMBAT`][cmd-combat-fr]                                           | Définit le comportement au combat                    | C      |
| [`COMBAT AGGRESSIVE`][cmd-combat-fr]                                |                                                      | C      |
| [`COMBAT DEFENSIVE`][cmd-combat-fr]                                 |                                                      | C      |
| [`COMBAT FLEE`][cmd-combat-fr]                                      |                                                      | C      |
| [`COMBAT HELP [NOT]`][cmd-combat-fr]                                | L'unité n'est pas aidée au combat                    | C      |
| [`COMBAT NOT`][cmd-combat-fr]                                       |                                                      | C      |
| [`COMBAT REAR`][cmd-combat-fr]                                      |                                                      | C      |
| [`COMBATSPELL [LEVEL <niveau>] "<sort>" [NOT]`][cmd-combatspell-fr] | Définit des sorts pour les combats                   | C      |
| [`CONTACT <unit-id>`][cmd-contact-fr]                               | Contacter les unités étrangères                      | C      |
| [`DEFAULT "<ordres>"`][cmd-default-fr]                              | Définit l'ordre par défaut pour le prochain tour     | C      |
| [`DESCRIBE BUILDING "<texte>"`][cmd-describe-fr]                    |                                                      | C      |
| [`DESCRIBE PRIVATE "<texte>"`][cmd-describe-fr]                     |                                                      | C      |
| [`DESCRIBE REGION "<texte>"`][cmd-describe-fr]                      |                                                      | C      |
| [`DESCRIBE SHIP "<texte>"`][cmd-describe-fr]                        |                                                      | C      |
| [`DESCRIBE UNIT "<texte>"`][cmd-describe-fr]                        | Décrit des objets                                    | C      |
| [`DESTROY [<niveau>]`][cmd-destroy-fr]                              | Réduire la taille d'un bâtiment ou d'un bateau       | L      |
| [`DESTROY [<niveau>] STREET <direction>`][cmd-destroy-fr]           | Démolir la route                                     | L      |
| [`EMAIL <email@adresse>`][cmd-email-fr]                             | Définit l'adresse e-mail                             | C      |
| [`END`][cmd-end-fr]                                                 | Termine l'ordre `MAKE TEMP`                          | C      |
| [`ENTER BUILDING <building-id>`][cmd-enter-fr]                      | Entre dans un bâtiment                               | C      |
| [`ENTER SHIP <ship-id>`][cmd-enter-fr]                              | Entre dans un bateau                                 | C      |
| [`ENTERTAIN [<somme>]`][cmd-entertain-fr]                           | Gagne 20 silver ou plus                              | L      |
| [`ERESSEA <faction-id> "<mot de passe>"`][cmd-eressea-fr]           | Commence les ordres pour la faction                  | C      |
| [`FOLLOW SHIP <ship-id>`][cmd-follow-fr]                            | Suit un bateau                                       | PL[^2] |
| [`FOLLOW UNIT <unit-id>`][cmd-follow-fr]                            | Suit une unité                                       | PL[^2] |
| [`FORGET <compétence>`][cmd-forget-fr]                              | Oublie la compétence                                 | C      |
| [`GIVE <unit-id> [EACH] <quantité> "<item>"`][cmd-give-fr]          | Remet des objets                                     | C      |
| [`GIVE <unit-id> [EACH] <quantité> MEN`][cmd-give-fr]               | Remet des personnes                                  | C      |
| [`GIVE <unit-id> [EACH] <quantité> SHIP`][cmd-give-fr]              | Passe le bateau pour former des convois              | C      |
| [`GIVE <unit-id> [EACH] <quantité> silver`][cmd-give-fr]            | Remet de l’argent                                    | C      |
| [`GIVE <unit-id> HERB`][cmd-give-fr]                                | Donne à une unité toutes les plantes                 | C      |
| [`GIVE <unit-id> COMMAND`][cmd-give-fr]                             | Remet le commandement du bateau ou bâtiment          | C      |
| [`GIVE <unit-id> UNIT`][cmd-give-fr]                                | Transfers unit to foreign faction                    | C      |
| [`GIVE 0 <quantité> <item>`][cmd-give-fr]                           |                                                      | C      |
| [`GIVE 0 <quantité> MEN`][cmd-give-fr]                              |                                                      | C      |
| [`GIVE 0 <quantité> silver`][cmd-give-fr]                           | Donne des objets aux agriculteurs                    | C      |
| [`GROUP ["<nom>"]`][cmd-group-fr]                                   | Regroupe des unités                                  | C      |
| [`GROW HORSES`][cmd-grow-fr]                                        | Élève des chevaux - Seulement dans un haras          | L      |
| [`GUARD [NOT]`][cmd-guard-fr]                                       | Garde la région                                      | C      |
| [`HELP <faction-id> ALL [NOT]`][cmd-help-fr]                        | Définit ou supprime une alliance unilatérale         | C      |
| [`HELP <faction-id> COMBAT [NOT]`][cmd-help-fr]                     |                                                      | C      |
| [`HELP <faction-id> GIVE [NOT]`][cmd-help-fr]                       |                                                      | C      |
| [`HELP <faction-id> GUARD [NOT]`][cmd-help-fr]                      |                                                      | C      |
| [`HELP <faction-id> PARTEITARNUNG [NOT]`][cmd-help-fr]              |                                                      | C      |
| [`HELP <faction-id> SILVER [NOT]`][cmd-help-fr]                     |                                                      | C      |
| [`HIDE [<niveau>]`][cmd-hide-fr]                                    | Définir le niveau de camouflage                      | C      |
| [`HIDE FACTION [NOT]`][cmd-hide-fr]                                 | Déguise la faction en anonyme                        | C      |
| [`HIDE FACTION NUMBER <faction-id>`][cmd-hide-fr]                   | Déguise une faction en une autre faction             | C      |
| [`HIDE <peuple>`][cmd-hide-fr]                                      | Démons : déguisés en un autre peuple                 | C      |
| [`LANGUAGE en\|de`][cmd-language-fr]                                | change la langue de la faction                       | C      |
| [`LEARN <compétence>`][cmd-learn-fr]                                | Apprend une compétence                               | L      |
| [`LEARN AUTO <compétence>`][cmd-learn-fr]                           | Apprentissage ou enseignement d'une compétence       | L      |
| [`LEAVE`][cmd-leave-fr][cmd-leave-fr]                               | Schiff oder Gebäude verlassen                        | C      |
| [`LOCALE en\|de`][cmd-locale-fr]                                    | Affiche la langue des ordres                         | C      |
| [`MAKE`][cmd-make-fr]                                               | Fabrique un objet ou exploite une ressource          | L      |
| [`MAKE [<quantité>] <item>`][cmd-make-fr]                           |                                                      | L      |
| [`MAKE [<quantité>] <HERBS>`][cmd-make-fr]                          | Récolte la plante locale                             | L      |
| [`MAKE [<quantité>] <potion>`][cmd-make-fr]                         | Produit une potion alchimique                        | L      |
| [`MAKE [<niveau>] <building type> [<building-id>]`][cmd-make-fr]    | Agrandit ou construit un nouveau bâtiment            | L      |
| [`MAKE [<niveau>] <ship-type>`][cmd-make-fr]                        | Construit un nouveau bateau                          | L      |
| [`MAKE [<niveau>] SHIP [<ship-id>]`][cmd-make-fr]                   | Continue à construire le bateau                      | L      |
| [`MAKE [<niveau>] STREET direction`][cmd-make-fr]                   | Construit une routes                                 | L      |
| [`MAKE TEMP unit-alias-id ["<nom>"]`][cmd-make-fr]                  | Crée une nouvelle unité                              | C      |
| [`MESSAGE BUILDING <building-id> "<texte>"`][cmd-message-fr]        | Envoie un message                                    | C      |
| [`MESSAGE FACTION <faction-id> "<texte>"`][cmd-message-fr]          |                                                      | C      |
| [`MESSAGE REGION "<texte>"`][cmd-message-fr]                        | Envoie un message                                    | C      |
| [`MESSAGE SHIP <ship-id> "<texte>"`][cmd-message-fr]                | Envoie un message                                    | C      |
| [`MESSAGE UNIT <unit-id> "<texte>"`][cmd-message-fr]                |                                                      | C      |
| [`MOVE <direction> [<direction>]...`][cmd-move-fr]                  | Se déplace                                           | L      |
| [`NAME BUILDING "<nom>"`][cmd-name-fr]                              |                                                      | C      |
| [`NAME FACTION "<nom>"`][cmd-name-fr]                               |                                                      | C      |
| [`NAME FOREIGN FACTION <faction-id> "<nom>"`][cmd-name-fr]          |                                                      | C      |
| [`NAME FOREIGN UNIT <unit-id> "<nom>"`][cmd-name-fr]                | Nomme des objets étrangers et sans nom               | C      |
| [`NAME FOREIGN BUILDING building "<nom>"`][cmd-name-fr]             |                                                      | C      |
| [`NAME FOREIGN SHIP <ship-id> "<nom>"`][cmd-name-fr]                |                                                      | C      |
| [`NAME REGION "<nom>"`][cmd-name-fr]                                |                                                      | C      |
| [`NAME SHIP "<nom>"`][cmd-name-fr]                                  |                                                      | C      |
| [`NAME UNIT "<nom>"`][cmd-name-fr]                                  | Nomme des objets                                     | C      |
| [`NEXT`][cmd-next-fr]                                               | Termine les ordres                                   | C      |
| [`NUMBER BUILDING [<nouvel-id>]`][cmd-number-fr]                    |                                                      | C      |
| [`NUMBER FACTION [<nouvel-id>]`][cmd-number-fr]                     |                                                      | C      |
| [`NUMBER SHIP [<nouvel-id>]`][cmd-number-fr]                        |                                                      | C      |
| [`NUMBER UNIT [<nouvel-id>]`][cmd-number-fr]                        | Attribue un nouvel identifiant                       | C      |
| [`OPTION ADRESSEN [NOT]`][cmd-option-fr]                            |                                                      | C      |
| [`OPTION AUSWERTUNG [NOT]`][cmd-option-fr]                          | Différents paramètres                                | C      |
| [`OPTION BZIP2 [NOT]`][cmd-option-fr]                               |                                                      | C      |
| [`OPTION COMPUTER [NOT]`][cmd-option-fr]                            |                                                      | C      |
| [`OPTION MATERIALPOOL [NOT]`][cmd-option-fr]                        |                                                      | C      |
| [`OPTION PUNKTE [NOT]`][cmd-option-fr]                              |                                                      | C      |
| [`OPTION SILBERPOOL [NOT]`][cmd-option-fr]                          |                                                      | C      |
| [`OPTION STATISTIK [NOT]`][cmd-option-fr]                           |                                                      | C      |
| [`OPTION TALENTVERSCHIEBUNG [NOT]`][cmd-option-fr]                  |                                                      | C      |
| [`OPTION ZIPPED [NOT]`][cmd-option-fr]                              |                                                      | C      |
| [`OPTION ZUGVORLAGE [NOT]`][cmd-option-fr]                          |                                                      | C      |
| [`ORIGIN <x> <y>`][cmd-origin-fr]                                   | Définit l'origine des coordonnées                    | C      |
| [`PASSWORD "neues-password"`][cmd-password-fr]                      | Définit un nouveau mot de passe                      | C      |
| [`PAY NOT [<building-id>]`][cmd-pay-not-fr]                         | Ne paie pas l'entretien d'un bâtiment                | C      |
| [`PIRACY [faction 1] [faction 2]...`][cmd-piracy-fr]                | Définit le piratage                                  | L      |
| [`PLANT [<quantité>] TREES`][cmd-plant-fr]                          | Sème des graines                                     | L      |
| [`PLANT [<quantité>] HERB`][cmd-plant-fr]                           | Sème des plantes                                     | L      |
| [`PLANT [<quantité>] MALLORNSEEDS`][cmd-plant-fr]                   | Sème des graines                                     | L      |
| [`PLANT [<quantité>] SEEDS`][cmd-plant-fr]                          | Sème des graines                                     | L      |
| [`PREFIX [<préfixe>]`][cmd-prefix-fr]                               | Donne un préfixe au nom du peuple                    | C      |
| [`PROMOTE`][cmd-promote-fr]                                         | Transforme l'unité en héros                          | C      |
| [`QUIT "<password>" [FACTION <faction-id>]`][cmd-quit-fr]           | Quitte le jeu                                        | C      |
| [`RECRUIT <quantité>`][cmd-recruit-fr]                              | Recrute plus de personnes                            | C      |
| [`REGION <x>,<y>`][cmd-region-fr]                                   | Aucune fonction (uniquement pour les outils)         | C      |
| [`RESEARCH HERBS`][cmd-research-fr]                                 | Recherche des plantes                                | L      |
| [`RESERVE <quantité> "<item>"`][cmd-reserve-fr]                     | Gegenstände reservieren                              | C      |
| [`RESERVE <quantité> silver`][cmd-reserve-fr]                       | Reserve silver                                       | C      |
| [`RIDE <unit-id>`][cmd-ride-fr]                                     | Peut être transporté                                 | L      |
| [`ROUTE <direction1> [PAUSE] [<direction2>] ...`][cmd-route-fr]     | Se déplace                                           | L      |
| [`SELL ALL "<bien de luxe>"`][cmd-sell-fr]                          |                                                      |        |
| [`SELL <quantité> "<bien de luxe>"`][cmd-sell-fr]                   | Vend des produits de luxe                            | PL[^3] |
| [`SHOW "<potion>"`][cmd-show-fr]                                    | Affiche la description d'un objet                    | C      |
| [`SHOW "<peuple>"`][cmd-show-fr]                                    | Affiche la description d'une potion                  | C      |
| [`SHOW "<sort>"`][cmd-show-fr]                                      | Affiche la description du peuple de l'unité          | C      |
| [`SHOW "<item>"`][cmd-show-fr]                                      | Affiche la description d'un sort                     | C      |
| [`SHOW ALL POTIONS`][cmd-show-fr]                                   | Affiche la description de toutes les potions connues | C      |
| [`SHOW ALL SPELLS`][cmd-show-fr]                                    | Affiche la description de tous les sorts connus      | C      |
| [`SORT AFTER <unit-id>`][cmd-sort-fr]                               |                                                      | C      |
| [`SORT BEFORE <unit-id>`][cmd-sort-fr]                              | Tri l'unité dans le rapport                          | C      |
| [`SPY <unit-id>`][cmd-spy-fr]                                       | Espionne une unité                                   | L      |
| [`STEAL <unit-id>`][cmd-steal-fr]                                   | Vole 50 silver ou plus                               | L      |
| [`TAX [<somme>]`][cmd-tax-fr]                                       | Collecte les impôts                                  | L      |
| [`TEACH <unit1-id> [<unit2-id>]...`][cmd-teach-fr]                  | Enseigne à des unités                                | L      |
| [`UNIT <unit-id>`][cmd-unit-fr]                                     | Commence les ordres d'une unité                      | C      |
| [`USE  [<quantité>] "<potion>"`][cmd-use-fr]                        | Utilise une potion alchimique                        | C      |
| [`WORK`][cmd-work-fr]                                               | Gagne 10 silver ou plus                              | L      |

[^1]: l'ordre n'est pas toujours long, voir [Fin de la bataille][fin-du-combat]
[^2]: si l'unité suivie ne bouge pas, un autre ordre long peut être exécuté à la place
[^3]: un ordre `BUY` et plusieurs ordres `SELL` peuvent être combinés
[^4]: une unité peut lancer plusieurs sorts

## Voir aussi

- [Ordres][ordres]
- [Séquence des ordres][sequence-des-ordres]

Poursuivre la lecture : [premier tour][premier-tour].

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[//]: [[cmd-comment-fr]]

[cmd-attack-fr]: [[cmd-attack-fr]]
[cmd-banner-fr]: [[cmd-banner-fr]]
[cmd-buy-fr]: [[cmd-buy-fr]]
[cmd-carry-fr]: [[cmd-carry-fr]]
[cmd-cast-fr]: [[cmd-cast-fr]]
[cmd-claim-fr]: [[cmd-claim-fr]]
[cmd-combat-fr]: [[cmd-combat-fr]]
[cmd-combatspell-fr]: [[cmd-combatspell-fr]]
[cmd-contact-fr]: [[cmd-contact-fr]]
[cmd-default-fr]: [[cmd-default-fr]]
[cmd-describe-fr]: [[cmd-describe-fr]]
[cmd-destroy-fr]: [[cmd-destroy-fr]]
[cmd-email-fr]: [[cmd-email-fr]]
[cmd-end-fr]: [[cmd-end-fr]]
[cmd-enter-fr]: [[cmd-enter-fr]]
[cmd-entertain-fr]: [[cmd-entertain-fr]]
[cmd-eressea-fr]: [[cmd-eressea-fr]]
[cmd-follow-fr]: [[cmd-follow-fr]]
[cmd-forget-fr]: [[cmd-forget-fr]]
[cmd-give-fr]: [[cmd-give-fr]]
[cmd-group-fr]: [[cmd-group-fr]]
[cmd-grow-fr]: [[cmd-grow-fr]]
[cmd-guard-fr]: [[cmd-guard-fr]]
[cmd-help-fr]: [[cmd-help-fr]]
[cmd-hide-fr]: [[cmd-hide-fr]]
[cmd-language-fr]: [[cmd-language-fr]]
[cmd-learn-fr]: [[cmd-learn-fr]]
[cmd-leave-fr]: [[cmd-leave-fr]]
[cmd-locale-fr]: [[cmd-locale-fr]]
[cmd-make-fr]: [[cmd-make-fr]]
[cmd-message-fr]: [[cmd-message-fr]]
[cmd-move-fr]: [[cmd-move-fr]]
[cmd-name-fr]: [[cmd-name-fr]]
[cmd-next-fr]: [[cmd-next-fr]]
[cmd-number-fr]: [[cmd-number-fr]]
[cmd-option-fr]: [[cmd-option-fr]]
[cmd-origin-fr]: [[cmd-origin-fr]]
[cmd-password-fr]: [[cmd-password-fr]]
[cmd-pay-not-fr]: [[cmd-pay-not-fr]]
[cmd-piracy-fr]: [[cmd-piracy-fr]]
[cmd-plant-fr]: [[cmd-plant-fr]]
[cmd-prefix-fr]: [[cmd-prefix-fr]]
[cmd-promote-fr]: [[cmd-promote-fr]]
[cmd-quit-fr]: [[cmd-quit-fr]]
[cmd-recruit-fr]: [[cmd-recruit-fr]]
[cmd-region-fr]: [[cmd-region-fr]]
[cmd-research-fr]: [[cmd-research-fr]]
[cmd-reserve-fr]: [[cmd-reserve-fr]]
[cmd-ride-fr]: [[cmd-ride-fr]]
[cmd-route-fr]: [[cmd-route-fr]]
[cmd-sell-fr]: [[cmd-sell-fr]]
[cmd-show-fr]: [[cmd-show-fr]]
[cmd-sort-fr]: [[cmd-sort-fr]]
[cmd-spy-fr]: [[cmd-spy-fr]]
[cmd-steal-fr]: [[cmd-steal-fr]]
[cmd-tax-fr]: [[cmd-tax-fr]]
[cmd-teach-fr]: [[cmd-teach-fr]]
[cmd-unit-fr]: [[cmd-unit-fr]]
[cmd-use-fr]: [[cmd-use-fr]]
[cmd-work-fr]: [[cmd-work-fr]]
