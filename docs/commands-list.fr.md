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
| [[cmd-combat]]                                                             | Définit le comportement au combat                    | C      |
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
| [[cmd-end]]                                                                | Termine l'ordre `MAKE TEMP`                          | C      |
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
| [HIDE race]                                                                | Démons : déguisés en une autre race                  | C      |
| [LANGUAGE en/de]                                                           | change la langue de la faction                       | C      |
| [LEARN &lt;skill&gt;]                                                      | Apprend une compétence                               | L      |
| [LEARN AUTO &lt;skill&gt;]                                                 | Apprentissage ou enseignement d'une compétence       | L      |
| [[cmd-leave]]                                                              | Schiff oder Gebäude verlassen                        | C      |
| [LOCALE en/de]                                                             | Affiche la langue des ordres                         | C      |
| [[cmd-make]]                                                               | Fabrique un objet ou exploite une ressource          | L      |
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
| [[cmd-next]]                                                               | Termine les ordres                                   | C      |
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
| [PREFIX &#91;prefix&#93;]                                                  | Donne un préfixe au nom de la race                   | C      |
| [[cmd-promote]]                                                            | Transforme l'unité en héros                          | C      |
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
| [SHOW "&lt;race&gt;"]                                                      | Affiche la description d'une potion                  | C      |
| [SHOW "&lt;spell&gt;"]                                                     | Affiche la description de la race de l'unité         | C      |
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
| [[cmd-work]]                                                               | Gagne 10 silver ou plus                              | L      |

[^1]: l'ordre n'est pas toujours long, voir [Fin de la bataille][fin-du-combat]
[^2]: si l'unité suivie ne bouge pas, un autre ordre long peut être exécuté à la place
[^3]: un ordre `BUY` et plusieurs ordres `SELL` peuvent être combinés
[^4]: une unité peut lancer plusieurs sorts

## Voir aussi

- [[ordres]]
- [[sequence-des-ordres]]

Poursuivre la lecture : [[premier-tour]].

<!-- [THIS IS GIVE][give-link]
[give-link]: [[cmd-give]] -->

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[//]: [[cmd-comment-fr]]

[ATTACK &lt;unit id&gt;]: [[cmd-attack]]
[BANNER "&lt;text&gt;"]: [[cmd-banner]]
[BUY &lt;number&gt; &lt;luxury item&gt;]: [[cmd-buy]]
[CARRY &lt;unit id&gt;]: [[cmd-carry]]
[CAST &#91;REGION x y&#93; &#91;LEVEL n&#93; "&lt;spell&gt;"...]: [[cmd-cast]]
[CLAIM &lt;number&gt; &lt;item&gt;]: [[cmd-claim]]
[COMBAT AGGRESSIVE]: [[cmd-combat]]
[COMBAT DEFENSIVE]: [[cmd-combat]]
[COMBAT FLEE]: [[cmd-combat]]
[COMBAT HELP &#91;NOT&#93;]: [[cmd-combat]]
[COMBAT NOT]: [[cmd-combat]]
[COMBAT REAR]: [[cmd-combat]]
[COMBATSPELL &#91;LEVEL n&#93; "zauberspruch" &#91;NOT&#93;]: [[cmd-combatspell]]
[CONTACT &lt;unit id&gt;]: [[cmd-contact]]
[DEFAULT "Orders"]: [[cmd-default]]
[DESCRIBE BUILDING "&lt;text&gt;"]: [[cmd-describe]]
[DESCRIBE PRIVATE "&lt;text&gt;"]: [[cmd-describe]]
[DESCRIBE REGION "&lt;text&gt;"]: [[cmd-describe]]
[DESCRIBE SHIP "&lt;text&gt;"]: [[cmd-describe]]
[DESCRIBE UNIT "&lt;text&gt;"]: [[cmd-describe]]
[DESTROY &#91;level&#93;]: [[cmd-destroy]]
[DESTROY &#91;level&#93; STREET direction]: [[cmd-destroy]]
[EMAIL email@adresse]: [[cmd-email]]
[ENTER BUILDING &lt;building id&gt;]: [[cmd-enter]]
[ENTER SHIP &lt;ship id&gt;]: [[cmd-enter]]
[ENTERTAIN &#91;amount&#93;]: [[cmd-entertain]]
[ERESSEA &lt;faction id&gt; "password"]: [[cmd-eressea]]
[FOLLOW SHIP &lt;ship id&gt;]: [[cmd-follow]]
[FOLLOW UNIT &lt;unit id&gt;]: [[cmd-follow]]
[FORGET &lt;skill&gt;]: [[cmd-forget]]
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; &lt;item&gt;]: [[cmd-give]]
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; MEN]: [[cmd-give]]
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; SHIP]: [[cmd-give]]
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; SILVER]: [[cmd-give]]
[GIVE &lt;unit id&gt; COMMAND]: [[cmd-give]]
[GIVE &lt;unit id&gt; UNIT]: [[cmd-give]]
[GIVE &lt;unit id&gt; herb]: [[cmd-give]]
[GIVE 0 &lt;number&gt; &lt;item&gt;]: [[cmd-give]]
[GIVE 0 &lt;number&gt; MEN]: [[cmd-give]]
[GIVE 0 &lt;number&gt; SILVER]: [[cmd-give]]
[GROUP &#91;"&lt;name&gt;"&#93;]: [[cmd-group]]
[GROW HORSES]: [[cmd-grow]]
[GUARD &#91;NOT&#93;]: [[cmd-guard]]
[HELP &lt;faction id&gt; ALL &#91;NOT&#93;]: [[cmd-help]]
[HELP &lt;faction id&gt; COMBAT &#91;NOT&#93;]: [[cmd-help]]
[HELP &lt;faction id&gt; GIVE &#91;NOT&#93;]: [[cmd-help]]
[HELP &lt;faction id&gt; GUARD &#91;NOT&#93;]: [[cmd-help]]
[HELP &lt;faction id&gt; PARTEITARNUNG &#91;NOT&#93;]: [[cmd-help]]
[HELP &lt;faction id&gt; SILVER &#91;NOT&#93;]: [[cmd-help]]
[HIDE &#91;level&#93;]: [[cmd-hide]]
[HIDE FACTION &#91;NOT&#93;]: [[cmd-hide]]
[HIDE FACTION NUMBER &lt;faction id&gt;]: [[cmd-hide]]
[HIDE race]: [[cmd-hide]]
[LANGUAGE en/de]: [[cmd-language]]
[LEARN &lt;skill&gt;]: [[cmd-learn]]
[LEARN AUTO &lt;skill&gt;]: [[cmd-learn-auto]]
[LOCALE en/de]: [[cmd-locale]]
[MAKE &#91;&lt;amount&gt;&#93; &lt;HERBS&gt;]: [[cmd-make]]
[MAKE &#91;&lt;amount&gt;&#93; &lt;item&gt;]: [[cmd-make]]
[MAKE &#91;&lt;amount&gt;&#93; Potion]: [[cmd-make]]
[MAKE &#91;level&#93; &lt;building type&gt; &#91;&lt;building id&gt;&#93;]: [[cmd-make]]
[MAKE &#91;level&#93; &lt;ship-type&gt;]: [[cmd-make]]
[MAKE &#91;level&#93; SHIP &#91;&lt;ship id&gt;&#93;]: [[cmd-make]]
[MAKE &#91;level&#93; STREET direction]: [[cmd-make]]
[MAKE TEMP unit-alias-id &#91;"&lt;name&gt;"&#93;]: [[cmd-make]]
[MESSAGE BUILDING &lt;building id&gt; "&lt;text&gt;"]: [[cmd-message]]
[MESSAGE FACTION &lt;faction id&gt; "&lt;text&gt;"]: [[cmd-message]]
[MESSAGE REGION "&lt;text&gt;"]: [[cmd-message]]
[MESSAGE SHIP &lt;ship id&gt; "&lt;text&gt;"]: [[cmd-message]]
[MESSAGE UNIT &lt;unit id&gt; "&lt;text&gt;"]: [[cmd-message]]
[MOVE direction &#91;direction&#93;...]: [[cmd-move]]
[NAME BUILDING "&lt;name&gt;"]: [[cmd-name]]
[NAME FACTION "&lt;name&gt;"]: [[cmd-name]]
[NAME REGION "&lt;name&gt;"]: [[cmd-name]]
[NAME SHIP "&lt;name&gt;"]: [[cmd-name]]
[NAME FOREIGN BUILDING building "&lt;name&gt;"]: [[cmd-name]]
[NAME FOREIGN SHIP &lt;ship id&gt; "&lt;name&gt;"]: [[cmd-name]]
[NAME FOREIGN FACTION &lt;faction id&gt; "&lt;name&gt;"]: [[cmd-name]]
[NAME FOREIGN UNIT &lt;unit id&gt; "&lt;name&gt;"]: [[cmd-name]]
[NAME UNIT "&lt;name&gt;"]: [[cmd-name]]
[NUMBER BUILDING &#91;neue-nr&#93;]: [[cmd-number]]
[NUMBER FACTION &#91;neue-nr&#93;]: [[cmd-number]]
[NUMBER SHIP &#91;neue-nr&#93;]: [[cmd-number]]
[NUMBER UNIT &#91;neue-nr&#93;]: [[cmd-number]]
[OPTION ADRESSEN &#91;NOT&#93;]: [[cmd-option]]
[OPTION AUSWERTUNG &#91;NOT&#93;]: [[cmd-option]]
[OPTION BZIP2 &#91;NOT&#93;]: [[cmd-option]]
[OPTION COMPUTER &#91;NOT&#93;]: [[cmd-option]]
[OPTION MATERIALPOOL &#91;NOT&#93;]: [[cmd-option]]
[OPTION PUNKTE &#91;NOT&#93;]: [[cmd-option]]
[OPTION SILBERPOOL &#91;NOT&#93;]: [[cmd-option]]
[OPTION STATISTIK &#91;NOT&#93;]: [[cmd-option]]
[OPTION TALENTVERSCHIEBUNG &#91;NOT&#93;]: [[cmd-option]]
[OPTION ZIPPED &#91;NOT&#93;]: [[cmd-option]]
[OPTION ZUGVORLAGE &#91;NOT&#93;]: [[cmd-option]]
[ORIGIN x y]: [[cmd-origin]]
[PASSWORD "neues-password"]: [[cmd-password]]
[PAY NOT &#91;&lt;building id&gt;&#93;]: [[cmd-pay-not]]
[PIRACY &#91;faction 1&#93; &#91;faction 2&#93;...]: [[cmd-piracy]]
[PLANT &#91;&lt;number&gt;&#93; MALLORNSEEDS]: [[cmd-plant]]
[PLANT &#91;&lt;number&gt;&#93; SEEDS]: [[cmd-plant]]
[PLANT &#91;&lt;number&gt;&#93; TREES]: [[cmd-plant]]
[PLANT &#91;&lt;number&gt;&#93; herb]: [[cmd-plant]]
[PREFIX &#91;prefix&#93;]: [[cmd-prefix]]
[QUIT "&lt;password&gt;" &#91;FACTION &lt;faction id&gt;&#93;]: [[cmd-quit]]
[REGION x,y]: [[cmd-region]]
[RESEARCH HERBS]: [[cmd-research]]
[RESERVE &lt;number&gt; "&lt;item&gt;"]: [[cmd-reserve]]
[RESERVE &lt;number&gt; SILVER]: [[cmd-reserve]]
[RIDE &lt;unit id&gt;]: [[cmd-ride]]
[ROUTE direction &#91;direction&#93;...]: [[cmd-route]]
[SELL &lt;amount&gt; &lt;luxury item&gt;]: [[cmd-sell]]
[SELL ALL &lt;luxury item&gt;]: [[cmd-sell]]
[SHOW "&lt;item&gt;"]: [[cmd-show]]
[SHOW "&lt;potion&gt;"]: [[cmd-show]]
[SHOW "&lt;race&gt;"]: [[cmd-show]]
[SHOW "&lt;spell&gt;"]: [[cmd-show]]
[SHOW ALL POTIONS]: [[cmd-show]]
[SHOW ALL SPELLS]: [[cmd-show]]
[SORT AFTER &lt;unit id&gt;]: [[cmd-sort]]
[SORT BEFORE &lt;unit id&gt;]: [[cmd-sort]]
[SPY &lt;unit id&gt;]: [[cmd-spy]]
[TAX &#91;amount&#93;]: [[cmd-tax]]
[TEACH &lt;unit id&gt; &#91;&lt;unit id&gt;&#93;...]: [[cmd-teach]]
[UNIT &lt;unit id&gt;]: [[cmd-unit]]
[USE &#91;&lt;number&gt;&#93; potion]: [[cmd-use]]
