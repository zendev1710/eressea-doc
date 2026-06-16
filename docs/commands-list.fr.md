---
# cSpell:locale fr
alias: tableau-recapitulatif-des-ordres
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Tableau récapitulatif des ordres

`C`/`L`indique si l'[ordre][ordres] est un ordre Court ou Long.  
Une unité ne peut exécuter qu’un seul ordre long par tour, mais peut exécuter n’importe quel nombre d’ordres courts.

`PL` désigne un [ordre Pseudo-Long][ordres], qui peut être donné plusieurs fois à une unité.  
Toutefois, aucun autre ordre long ne peut être exécuté.  

Plus d'information : [[ordres]].

| Ordre                                                                      | Description                                          | C/L    |
|----------------------------------------------------------------------------|------------------------------------------------------|--------|
| [//]                                                                       | Commentaire durable                                  | C      |
| [ATTACK &lt;unit id&gt;]                                                   | Attaque l'unité                                      | PL[^1] |
| [BANNER "&lt;text&gt;"]                                                    | Définit le texte pour la liste d'adresses            | C      |
| [BUY &lt;number&gt; &lt;luxury item&gt;]                                   | Acheter des produits de luxe                         | PL[^3] |
| [CARRY &lt;unit id&gt;]                                                    | Emportez d'autres unités avec vous                   | C      |
| [CAST &#91;REGION x y&#93; &#91;LEVEL n&#93; "&lt;spell&gt;"...]           | Magie                                                | PL[^4] |
| [CLAIM &lt;number&gt; &lt;item&gt;]                                        | Récupère les objets du pool de faction               | C      |
| [`COMBAT`][cmd-combat-fr]                                                  | Définit le comportement au combat                    | C      |
| [COMBAT AGGRESSIVE]                                                        |                                                      | C      |
| [COMBAT DEFENSIVE]                                                         |                                                      | C      |
| [COMBAT FLEE]                                                              |                                                      | C      |
| [COMBAT HELP &#91;NOT&#93;]                                                | L'unité n'est pas aidée au combat                    | C      |
| [COMBAT NOT]                                                               |                                                      | C      |
| [COMBAT REAR]                                                              |                                                      | C      |
| [COMBATSPELL &#91;LEVEL n&#93; "zauberspruch" &#91;NOT&#93;]               | Définit des sorts pour les combats                   | C      |
| [CONTACT &lt;unit id&gt;]                                                  | Contacter les unités étrangères                      | C      |
| [DEFAULT "Orders"]                                                         | Définit l'ordre par défaut pour le prochain tour     | C      |
| [DESCRIBE BUILDING "&lt;text&gt;"]                                         |                                                      | C      |
| [DESCRIBE PRIVATE "&lt;text&gt;"]                                          |                                                      | C      |
| [DESCRIBE REGION "&lt;text&gt;"]                                           |                                                      | C      |
| [DESCRIBE SHIP "&lt;text&gt;"]                                             |                                                      | C      |
| [DESCRIBE UNIT "&lt;text&gt;"]                                             | Décrit des objets                                    | C      |
| [DESTROY &#91;level&#93;]                                                  | Réduire la taille d'un bâtiment ou d'un bateau       | L      |
| [DESTROY &#91;level&#93; STREET direction]                                 | Démolir la route                                     | L      |
| [EMAIL email@adresse]                                                      | Définit l'adresse e-mail                             | C      |
| [`END`][cmd-end-fr]                                                        | Termine l'ordre `MAKE TEMP`                          | C      |
| [ENTER BUILDING &lt;building id&gt;]                                       | Entre dans un bâtiment                               | C      |
| [ENTER SHIP &lt;ship id&gt;]                                               | Entre dans un bateau                                 | C      |
| [ENTERTAIN &#91;amount&#93;]                                               | Gagne 20 silver ou plus                              | L      |
| [ERESSEA &lt;faction id&gt; "password"]                                    | Commence les ordres pour la faction                  | C      |
| [FOLLOW SHIP &lt;ship id&gt;]                                              | Suit un bateau                                       | PL[^2] |
| [FOLLOW UNIT &lt;unit id&gt;]                                              | Suit une unité                                       | PL[^2] |
| [FORGET &lt;skill&gt;]                                                     | Oublie la compétence                                 | C      |
| [GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; &lt;item&gt;]          | Remet des objets                                     | C      |
| [GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; MEN]                   | Remet des personnes                                  | C      |
| [GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; SHIP]                  | Passe le bateau pour former des convois              | C      |
| [GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; SILVER]                | Remet de l’argent                                    | C      |
| [GIVE &lt;unit id&gt; herb]                                                | Donne à une unité toutes les plantes                 | C      |
| [GIVE &lt;unit id&gt; COMMAND]                                             | Remet le commandement du bateau ou bâtiment          | C      |
| [GIVE &lt;unit id&gt; UNIT]                                                | Transfers unit to foreign faction                    | C      |
| [GIVE 0 &lt;number&gt; &lt;item&gt;]                                       |                                                      | C      |
| [GIVE 0 &lt;number&gt; MEN]                                                |                                                      | C      |
| [GIVE 0 &lt;number&gt; SILVER]                                             | Donne des objets aux agriculteurs                    | C      |
| [GROUP &#91;"&lt;name&gt;"&#93;]                                           | Regroupe des unités                                  | C      |
| [GROW HORSES]                                                              | Élève des chevaux - Seulement dans un haras          | L      |
| [GUARD &#91;NOT&#93;]                                                      | Garde la région                                      | C      |
| [HELP &lt;faction id&gt; ALL &#91;NOT&#93;]                                | Définit ou supprime une alliance unilatérale         | C      |
| [HELP &lt;faction id&gt; COMBAT &#91;NOT&#93;]                             |                                                      | C      |
| [HELP &lt;faction id&gt; GIVE &#91;NOT&#93;]                               |                                                      | C      |
| [HELP &lt;faction id&gt; GUARD &#91;NOT&#93;]                              |                                                      | C      |
| [HELP &lt;faction id&gt; PARTEITARNUNG &#91;NOT&#93;]                      |                                                      | C      |
| [HELP &lt;faction id&gt; SILVER &#91;NOT&#93;]                             |                                                      | C      |
| [HIDE &#91;level&#93;]                                                     | Définir le niveau de camouflage                      | C      |
| [HIDE FACTION &#91;NOT&#93;]                                               | Déguise la faction en anonyme                        | C      |
| [HIDE FACTION NUMBER &lt;faction id&gt;]                                   | Déguise une faction en une autre faction             | C      |
| [HIDE &lt;peuple&gt;]                                                      | Démons : déguisés en un autre peuple                 | C      |
| [LANGUAGE en/de]                                                           | change la langue de la faction                       | C      |
| [LEARN &lt;skill&gt;]                                                      | Apprend une compétence                               | L      |
| [LEARN AUTO &lt;skill&gt;]                                                 | Apprentissage ou enseignement d'une compétence       | L      |
| [`LEAVE`][cmd-leave-fr]                                                    | Schiff oder Gebäude verlassen                        | C      |
| [LOCALE en/de]                                                             | Affiche la langue des ordres                         | C      |
| [`MAKE`][cmd-make-fr]                                                      | Fabrique un objet ou exploite une ressource          | L      |
| [MAKE &#91;&lt;amount&gt;&#93; &lt;item&gt;]                               |                                                      | L      |
| [MAKE &#91;&lt;amount&gt;&#93; &lt;HERBS&gt;]                              | Récolte la plante locale                             | L      |
| [MAKE &#91;&lt;amount&gt;&#93; potion]                                     | Produit une potion alchimique                        | L      |
| [MAKE &#91;level&#93; &lt;building type&gt; &#91;&lt;building id&gt;&#93;] | Agrandit ou construit un nouveau bâtiment            | L      |
| [MAKE &#91;level&#93; &lt;ship-type&gt;]                                   | Construit un nouveau bateau                          | L      |
| [MAKE &#91;level&#93; SHIP &#91;&lt;ship id&gt;&#93;]                      | Continue à construire le bateau                      | L      |
| [MAKE &#91;level&#93; STREET direction]                                    | Construit une routes                                 | L      |
| [MAKE TEMP unit-alias-id &#91;"&lt;name&gt;"&#93;]                         | Crée une nouvelle unité                              | C      |
| [MESSAGE BUILDING &lt;building id&gt; "&lt;text&gt;"]                      | Envoie un message                                    | C      |
| [MESSAGE FACTION &lt;faction id&gt; "&lt;text&gt;"]                        |                                                      | C      |
| [MESSAGE REGION "&lt;text&gt;"]                                            | Envoie un message                                    | C      |
| [MESSAGE SHIP &lt;ship id&gt; "&lt;text&gt;"]                              | Envoie un message                                    | C      |
| [MESSAGE UNIT &lt;unit id&gt; "&lt;text&gt;"]                              |                                                      | C      |
| [MOVE direction &#91;direction&#93;...]                                    | Se déplace                                           | L      |
| [NAME BUILDING "&lt;name&gt;"]                                             |                                                      | C      |
| [NAME FACTION "&lt;name&gt;"]                                              |                                                      | C      |
| [NAME FOREIGN FACTION &lt;faction id&gt; "&lt;name&gt;"]                   |                                                      | C      |
| [NAME FOREIGN UNIT &lt;unit id&gt; "&lt;name&gt;"]                         | Nomme des objets étrangers et sans nom               | C      |
| [NAME FOREIGN BUILDING building "&lt;name&gt;"]                            |                                                      | C      |
| [NAME FOREIGN SHIP &lt;ship id&gt; "&lt;name&gt;"]                         |                                                      | C      |
| [NAME REGION "&lt;name&gt;"]                                               |                                                      | C      |
| [NAME SHIP "&lt;name&gt;"]                                                 |                                                      | C      |
| [NAME UNIT "&lt;name&gt;"]                                                 | Nomme des objets                                     | C      |
| [`NEXT`][cmd-next-fr]                                                      | Termine les ordres                                   | C      |
| [NUMBER BUILDING &#91;neue-nr&#93;]                                        |                                                      | C      |
| [NUMBER FACTION &#91;neue-nr&#93;]                                         |                                                      | C      |
| [NUMBER SHIP &#91;neue-nr&#93;]                                            |                                                      | C      |
| [NUMBER UNIT &#91;neue-nr&#93;]                                            | Attribue un nouvel identifiant                       | C      |
| [OPTION ADRESSEN &#91;NOT&#93;]                                            |                                                      | C      |
| [OPTION AUSWERTUNG &#91;NOT&#93;]                                          | Différents paramètres                                | C      |
| [OPTION BZIP2 &#91;NOT&#93;]                                               |                                                      | C      |
| [OPTION COMPUTER &#91;NOT&#93;]                                            |                                                      | C      |
| [OPTION MATERIALPOOL &#91;NOT&#93;]                                        |                                                      | C      |
| [OPTION PUNKTE &#91;NOT&#93;]                                              |                                                      | C      |
| [OPTION SILBERPOOL &#91;NOT&#93;]                                          |                                                      | C      |
| [OPTION STATISTIK &#91;NOT&#93;]                                           |                                                      | C      |
| [OPTION TALENTVERSCHIEBUNG &#91;NOT&#93;]                                  |                                                      | C      |
| [OPTION ZIPPED &#91;NOT&#93;]                                              |                                                      | C      |
| [OPTION ZUGVORLAGE &#91;NOT&#93;]                                          |                                                      | C      |
| [ORIGIN x y]                                                               | Définit l'origine des coordonnées                    | C      |
| [PASSWORD "neues-password"]                                                | Définit un nouveau mot de passe                      | C      |
| [PAY NOT &#91;&lt;building id&gt;&#93;]                                    | Ne paie pas l'entretien d'un bâtiment                | C      |
| [PIRACY &#91;faction 1&#93; &#91;faction 2&#93;...]                        | Définit le piratage                                  | L      |
| [PLANT &#91;&lt;number&gt;&#93; TREES]                                     | Plante des graines                                   | L      |
| [PLANT &#91;&lt;number&gt;&#93; herb]                                      | Plante des herbes                                    | L      |
| [PLANT &#91;&lt;number&gt;&#93; MALLORNSEEDS]                              | Plante des graines                                   | L      |
| [PLANT &#91;&lt;number&gt;&#93; SEEDS]                                     | Plante des graines                                   | L      |
| [PREFIX &#91;prefix&#93;]                                                  | Donne un préfixe au nom du peuple                    | C      |
| [`PROMOTE`][cmd-promote-fr]                                                | Transforme l'unité en héros                          | C      |
| [QUIT "&lt;password&gt;" &#91;FACTION &lt;faction id&gt;&#93;]             | Quitte le jeu                                        | C      |
| [RECRUIT &lt;number&gt;][recruter]                                         | Recrute plus de personnes                            | C      |
| [REGION x,y]                                                               | Aucune fonction (uniquement pour les outils)         | C      |
| [RESEARCH HERBS]                                                           | Recherche des plantes                                | L      |
| [RESERVE &lt;number&gt; "&lt;item&gt;"]                                    | Gegenstände reservieren                              | C      |
| [RESERVE &lt;number&gt; SILVER]                                            | Reserve silver                                       | C      |
| [RIDE &lt;unit id&gt;]                                                     | Peut être transporté                                 | L      |
| [ROUTE direction &#91;direction&#93;...]                                   | Se déplace                                           | L      |
| [SELL ALL &lt;luxury item&gt;]                                             |                                                      |        |
| [SELL &lt;amount&gt; &lt;luxury item&gt;]                                  | Vend des produits de luxe                            | PL[^3] |
| [SHOW "&lt;potion&gt;"]                                                    | Affiche la description d'un objet                    | C      |
| [SHOW "&lt;peuple&gt;"]                                                    | Affiche la description d'une potion                  | C      |
| [SHOW "&lt;spell&gt;"]                                                     | Affiche la description du peuple de l'unité          | C      |
| [SHOW "&lt;item&gt;"]                                                      | Affiche la description d'un sort                     | C      |
| [SHOW ALL POTIONS]                                                         | Affiche la description de toutes les potions connues | C      |
| [SHOW ALL SPELLS]                                                          | Affiche la description de tous les sorts connus      | C      |
| [SORT AFTER &lt;unit id&gt;]                           "                   |                                                      | C      |
| [SORT BEFORE &lt;unit id&gt;]                                              | Tri l'unité dans le rapport                          | C      |
| [SPY &lt;unit id&gt;]                                                      | Espionne une unité                                   | L      |
| [STEAL &lt;unit id&gt;][discretion]{title="Stealth"}                       | Vole 50 silver ou plus                               | L      |
| [TAX &#91;amount&#93;]                                                     | Collecte les impôts                                  | L      |
| [TEACH &lt;unit id&gt; &#91;&lt;unit id&gt;&#93;...]                       | Enseigne à des unités                                | L      |
| [UNIT &lt;unit id&gt;]                                                     | Commence les ordres d'une unité                      | C      |
| [USE  &#91;&lt;number&gt;&#93; potion]                                     | Utilise une potion alchimique                        | C      |
| [`WORK`][cmd-work-fr]                                                      | Gagne 10 silver ou plus                              | L      |

[^1]: l'ordre n'est pas toujours long, voir [Fin de la bataille][fin-du-combat]
[^2]: si l'unité suivie ne bouge pas, un autre ordre long peut être exécuté à la place
[^3]: un ordre `BUY` et plusieurs ordres `SELL` peuvent être combinés
[^4]: une unité peut lancer plusieurs sorts

## Voir aussi

- [[ordres]]
- [[sequence-des-ordres]]

Poursuivre la lecture : [[premier-tour]].

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[//]: [[cmd-comment-fr]]
[ATTACK &lt;unit id&gt;]: [[cmd-attack-fr]]
[BANNER "&lt;text&gt;"]: [[cmd-banner-fr]]
[BUY &lt;number&gt; &lt;luxury item&gt;]: [[cmd-buy-fr]]
[CARRY &lt;unit id&gt;]: [[cmd-carry-fr]]
[CAST &#91;REGION x y&#93; &#91;LEVEL n&#93; "&lt;spell&gt;"...]: [[cmd-cast-fr]]
[CLAIM &lt;number&gt; &lt;item&gt;]: [[cmd-claim-fr]]
[COMBAT AGGRESSIVE]: [[cmd-combat-fr]]
[COMBAT DEFENSIVE]: [[cmd-combat-fr]]
[COMBAT FLEE]: [[cmd-combat-fr]]
[COMBAT HELP &#91;NOT&#93;]: [[cmd-combat-fr]]
[COMBAT NOT]: [[cmd-combat-fr]]
[COMBAT REAR]: [[cmd-combat-fr]]
[COMBATSPELL &#91;LEVEL n&#93; "zauberspruch" &#91;NOT&#93;]: [[cmd-combatspell-fr]]
[CONTACT &lt;unit id&gt;]: [[cmd-contact-fr]]
[DEFAULT "Orders"]: [[cmd-default-fr]]
[DESCRIBE BUILDING "&lt;text&gt;"]: [[cmd-describe-fr]]
[DESCRIBE PRIVATE "&lt;text&gt;"]: [[cmd-describe-fr]]
[DESCRIBE REGION "&lt;text&gt;"]: [[cmd-describe-fr]]
[DESCRIBE SHIP "&lt;text&gt;"]: [[cmd-describe-fr]]
[DESCRIBE UNIT "&lt;text&gt;"]: [[cmd-describe-fr]]
[DESTROY &#91;level&#93;]: [[cmd-destroy-fr]]
[DESTROY &#91;level&#93; STREET direction]: [[cmd-destroy-fr]]
[EMAIL email@adresse]: [[cmd-email-fr]]
[ENTER BUILDING &lt;building id&gt;]: [[cmd-enter-fr]]
[ENTER SHIP &lt;ship id&gt;]: [[cmd-enter-fr]]
[ENTERTAIN &#91;amount&#93;]: [[cmd-entertain-fr]]
[ERESSEA &lt;faction id&gt; "password"]: [[cmd-eressea-fr]]
[FOLLOW SHIP &lt;ship id&gt;]: [[cmd-follow-fr]]
[FOLLOW UNIT &lt;unit id&gt;]: [[cmd-follow-fr]]
[FORGET &lt;skill&gt;]: [[cmd-forget-fr]]
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; &lt;item&gt;]: [[cmd-give-fr]]
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; MEN]: [[cmd-give-fr]]
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; SHIP]: [[cmd-give-fr]]
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; SILVER]: [[cmd-give-fr]]
[GIVE &lt;unit id&gt; COMMAND]: [[cmd-give-fr]]
[GIVE &lt;unit id&gt; UNIT]: [[cmd-give-fr]]
[GIVE &lt;unit id&gt; herb]: [[cmd-give-fr]]
[GIVE 0 &lt;number&gt; &lt;item&gt;]: [[cmd-give-fr]]
[GIVE 0 &lt;number&gt; MEN]: [[cmd-give-fr]]
[GIVE 0 &lt;number&gt; SILVER]: [[cmd-give-fr]]
[GROUP &#91;"&lt;name&gt;"&#93;]: [[cmd-group-fr]]
[GROW HORSES]: [[cmd-grow-fr]]
[GUARD &#91;NOT&#93;]: [[cmd-guard-fr]]
[HELP &lt;faction id&gt; ALL &#91;NOT&#93;]: [[cmd-help-fr]]
[HELP &lt;faction id&gt; COMBAT &#91;NOT&#93;]: [[cmd-help-fr]]
[HELP &lt;faction id&gt; GIVE &#91;NOT&#93;]: [[cmd-help-fr]]
[HELP &lt;faction id&gt; GUARD &#91;NOT&#93;]: [[cmd-help-fr]]
[HELP &lt;faction id&gt; PARTEITARNUNG &#91;NOT&#93;]: [[cmd-help-fr]]
[HELP &lt;faction id&gt; SILVER &#91;NOT&#93;]: [[cmd-help-fr]]
[HIDE &#91;level&#93;]: [[cmd-hide-fr]]
[HIDE FACTION &#91;NOT&#93;]: [[cmd-hide-fr]]
[HIDE FACTION NUMBER &lt;faction id&gt;]: [[cmd-hide-fr]]
[HIDE &lt;peuple&gt;]: [[cmd-hide-fr]]
[LANGUAGE en/de]: [[cmd-language-fr]]
[LEARN &lt;skill&gt;]: [[cmd-learn-fr]]
[LEARN AUTO &lt;skill&gt;]: [[cmd-learn-auto-fr]]
[LOCALE en/de]: [[cmd-locale-fr]]
[MAKE &#91;&lt;amount&gt;&#93; &lt;HERBS&gt;]: [[cmd-make-fr]]
[MAKE &#91;&lt;amount&gt;&#93; &lt;item&gt;]: [[cmd-make-fr]]
[MAKE &#91;&lt;amount&gt;&#93; Potion]: [[cmd-make-fr]]
[MAKE &#91;level&#93; &lt;building type&gt; &#91;&lt;building id&gt;&#93;]: [[cmd-make-fr]]
[MAKE &#91;level&#93; &lt;ship-type&gt;]: [[cmd-make-fr]]
[MAKE &#91;level&#93; SHIP &#91;&lt;ship id&gt;&#93;]: [[cmd-make-fr]]
[MAKE &#91;level&#93; STREET direction]: [[cmd-make-fr]]
[MAKE TEMP unit-alias-id &#91;"&lt;name&gt;"&#93;]: [[cmd-make-fr]]
[MESSAGE BUILDING &lt;building id&gt; "&lt;text&gt;"]: [[cmd-message-fr]]
[MESSAGE FACTION &lt;faction id&gt; "&lt;text&gt;"]: [[cmd-message-fr]]
[MESSAGE REGION "&lt;text&gt;"]: [[cmd-message-fr]]
[MESSAGE SHIP &lt;ship id&gt; "&lt;text&gt;"]: [[cmd-message-fr]]
[MESSAGE UNIT &lt;unit id&gt; "&lt;text&gt;"]: [[cmd-message-fr]]
[MOVE direction &#91;direction&#93;...]: [[cmd-move-fr]]
[NAME BUILDING "&lt;name&gt;"]: [[cmd-name-fr]]
[NAME FACTION "&lt;name&gt;"]: [[cmd-name-fr]]
[NAME REGION "&lt;name&gt;"]: [[cmd-name-fr]]
[NAME SHIP "&lt;name&gt;"]: [[cmd-name-fr]]
[NAME FOREIGN BUILDING building "&lt;name&gt;"]: [[cmd-name-fr]]
[NAME FOREIGN SHIP &lt;ship id&gt; "&lt;name&gt;"]: [[cmd-name-fr]]
[NAME FOREIGN FACTION &lt;faction id&gt; "&lt;name&gt;"]: [[cmd-name-fr]]
[NAME FOREIGN UNIT &lt;unit id&gt; "&lt;name&gt;"]: [[cmd-name-fr]]
[NAME UNIT "&lt;name&gt;"]: [[cmd-name-fr]]
[NUMBER BUILDING &#91;neue-nr&#93;]: [[cmd-number-fr]]
[NUMBER FACTION &#91;neue-nr&#93;]: [[cmd-number-fr]]
[NUMBER SHIP &#91;neue-nr&#93;]: [[cmd-number-fr]]
[NUMBER UNIT &#91;neue-nr&#93;]: [[cmd-number-fr]]
[OPTION ADRESSEN &#91;NOT&#93;]: [[cmd-option-fr]]
[OPTION AUSWERTUNG &#91;NOT&#93;]: [[cmd-option-fr]]
[OPTION BZIP2 &#91;NOT&#93;]: [[cmd-option-fr]]
[OPTION COMPUTER &#91;NOT&#93;]: [[cmd-option-fr]]
[OPTION MATERIALPOOL &#91;NOT&#93;]: [[cmd-option-fr]]
[OPTION PUNKTE &#91;NOT&#93;]: [[cmd-option-fr]]
[OPTION SILBERPOOL &#91;NOT&#93;]: [[cmd-option-fr]]
[OPTION STATISTIK &#91;NOT&#93;]: [[cmd-option-fr]]
[OPTION TALENTVERSCHIEBUNG &#91;NOT&#93;]: [[cmd-option-fr]]
[OPTION ZIPPED &#91;NOT&#93;]: [[cmd-option-fr]]
[OPTION ZUGVORLAGE &#91;NOT&#93;]: [[cmd-option-fr]]
[ORIGIN x y]: [[cmd-origin-fr]]
[PASSWORD "neues-password"]: [[cmd-password-fr]]
[PAY NOT &#91;&lt;building id&gt;&#93;]: [[cmd-pay-not-fr]]
[PIRACY &#91;faction 1&#93; &#91;faction 2&#93;...]: [[cmd-piracy-fr]]
[PLANT &#91;&lt;number&gt;&#93; MALLORNSEEDS]: [[cmd-plant-fr]]
[PLANT &#91;&lt;number&gt;&#93; SEEDS]: [[cmd-plant-fr]]
[PLANT &#91;&lt;number&gt;&#93; TREES]: [[cmd-plant-fr]]
[PLANT &#91;&lt;number&gt;&#93; herb]: [[cmd-plant-fr]]
[PREFIX &#91;prefix&#93;]: [[cmd-prefix-fr]]
[QUIT "&lt;password&gt;" &#91;FACTION &lt;faction id&gt;&#93;]: [[cmd-quit-fr]]
[REGION x,y]: [[cmd-region-fr]]
[RESEARCH HERBS]: [[cmd-research-fr]]
[RESERVE &lt;number&gt; "&lt;item&gt;"]: [[cmd-reserve-fr]]
[RESERVE &lt;number&gt; SILVER]: [[cmd-reserve-fr]]
[RIDE &lt;unit id&gt;]: [[cmd-ride-fr]]
[ROUTE direction &#91;direction&#93;...]: [[cmd-route-fr]]
[SELL &lt;amount&gt; &lt;luxury item&gt;]: [[cmd-sell-fr]]
[SELL ALL &lt;luxury item&gt;]: [[cmd-sell-fr]]
[SHOW "&lt;item&gt;"]: [[cmd-show-fr]]
[SHOW "&lt;potion&gt;"]: [[cmd-show-fr]]
[SHOW "&lt;peuple&gt;"]: [[cmd-show-fr]]
[SHOW "&lt;spell&gt;"]: [[cmd-show-fr]]
[SHOW ALL POTIONS]: [[cmd-show-fr]]
[SHOW ALL SPELLS]: [[cmd-show-fr]]
[SORT AFTER &lt;unit id&gt;]: [[cmd-sort-fr]]
[SORT BEFORE &lt;unit id&gt;]: [[cmd-sort-fr]]
[SPY &lt;unit id&gt;]: [[cmd-spy-fr]]
[TAX &#91;amount&#93;]: [[cmd-tax-fr]]
[TEACH &lt;unit id&gt; &#91;&lt;unit id&gt;&#93;...]: [[cmd-teach-fr]]
[UNIT &lt;unit id&gt;]: [[cmd-unit-fr]]
[USE &#91;&lt;number&gt;&#93; potion]: [[cmd-use-fr]]
