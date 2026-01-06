---
# cSpell:locale fr, en
alias: discussion-rapide-description
---
# Discussion : rapide description

Sous "C/L", il est indiqué s'il s'agit d'un [[ordres|ordre]] court ou long, c'est-à-dire s'il est exécuté immédiatement (et d'autres ordres sont possibles par la suite) ou s'il prend un tour entier pour être exécuté.
"C" est un ordre court, "L" est un ordre long.

`PL` indique un [[ordres|ordre]] pseudo-long qui peut être donné à une unité plusieurs fois.  
Cependant, aucun autre ordre long ne peut être exécuté ensuite.

brief description of orders

| Ordre                                                                   | Description                                       | C/L    |
|-------------------------------------------------------------------------|---------------------------------------------------|--------|
| [//](./cmd-comment-slash.md)                                            | commentaire permanent                             | C      |
| [[cmd-work]]                                                            | gagne 10 silver ou plus                           | L      |
| [ATTACK unit-id](./cmd-attack.md)                                       | attaque l'unité                                   | PL[^1] |
| [BANNER "text"](./cmd-banner.md)                                        | Définit le texte pour la liste d'adresses         | C      |
| [CLAIM amount item](./cmd-claim.md)                                     | Fetches items from faction pool                   | C      |
| [[cmd-promote]]                                                         | Promote a unit to heroe                           | C      |
| [STEAL unit-id](./cmd-steal.md)                                         | steal 50 Silver or more                           | L      |
| [NAME UNIT "name"](./cmd-name.md)                                       | names the specified object                        | C      |
| [NAME FACTION "name"](./cmd-name.md)                                    |                                                   | C      |
| [NAME BUILDING "name"](./cmd-name.md)                                   |                                                   | C      |
| [NAME SHIP "name"](./cmd-name.md)                                       |                                                   | C      |
| [NAME REGION "name"](./cmd-name.md)                                     |                                                   | C      |
| [NAME STRANGERS UNIT unit-id "name"](./cmd-name.md)                     | names the specified foreign object                | C      |
| [NAME STRANGER SHIP ship-id "name"](./cmd-name.md)                      |                                                   | C      |
| [NAME STRANGER BUILDING building-id "name"](./cmd-name.md)              |                                                   | C      |
| [NAME STRANGERS FACTION faction-id "name"](./cmd-name.md)               |                                                   | C      |
| [USE \[amount\] potion](./cmd-use.md)                                   | uses alchemical potion                            | C      |
| [DESCRIBE UNIT "text"](./cmd-describe.md)                               | describes object                                  | C      |
| [DESCRIBE PRIVATE "text"](./cmd-describe.md)                            | unit description for the owner                    | C      |
| [DESCRIBE BUILDING "text"](./cmd-describe.md)                           |                                                   | C      |
| [DESCRIBE SHIP "text"](./cmd-describe.md)                               |                                                   | C      |
| [DESCRIBE REGION "text"](./cmd-describe.md)                             |                                                   | C      |
| [ENTER BUILDING building-id](./cmd-enter.md)                            | Entre dans un bâtiment                            | C      |
| [ENTER SHIP ship-id](./cmd-enter.md)                                    | Monte à bord d'un bateau                          | C      |
| [GUARD \[NOT\]](./cmd-guard.md)                                         | garde une région                                  | C      |
| [BEZAHLE NOT \[building-id\]](./cmd-pay-not.md)                         | do not pay a maintenance                          | C      |
| [MESSAGE REGION "text"](./cmd-message.md)                               | Envoyer un message                                    | C      |
| [MESSAGE SHIP ship-id "text"](./cmd-message.md)                         | Envoyer un message                                    | C      |
| [MESSAGE BUILDING building-id "text"](./cmd-message.md)                 | Envoyer un message                                    | C      |
| [MESSAGE UNIT unit id "text"](./cmd-message.md)                         | Envoyer un message                                    | C      |
| [MESSAGE FACTION faction-id "text"](./cmd-message.md)                   | Envoyer un message                                    | C      |
| [DEFAULT order](./cmd-default.md)                                       | sets the default order for the next turn          | C      |
| [UNIT unit-id](./cmd-unit.md)                                           | beginning of a unit's orders                      | C      |
| [EMAIL email@adresse](./cmd-email.md)                                   | sets the e−mail the report is sent to             | C      |
| [[cmd-end]]                                                             | ends a MAKE TEMP block                            | C      |
| [ERESSEA faction-id "passwort"](./cmd-eressea.md)                       | beginning of faction's orders                     | C      |
| [RIDE unit-id](./cmd-ride.md)                                           | be transported by unit−id                         | L      |
| [FOLLOW UNIT unit-id](./cmd-follow.md)                                  | follows a unit                                    | PL[^2] |
| [FOLLOW SHIP ship-id](./cmd-follow.md)                                  | follows a ship                                    | PL[^2] |
| [RESEARCH HERB](./cmd-research.md)                                      | search for herbs                                  | L      |
| [GIVE unit-id HERB](./cmd-give.md)                                      | give a unit all herbs                             | C      |
| [GIVE unit-id COMMAND](./cmd-give.md)                                   | give a unit ship/ building control                | C      |
| [GIVE unit-id UNIT](./cmd-give.md)                                      | give unit to a foreign faction                    | C      |
| [GIVE unit-id \[EACH\] amount MEN](./cmd-give.md)                       | give a unit men                                   | C      |
| [GIVE unit-id \[EACH\] amount SHIP](./cmd-give.md)                      | give SHIP to form convoys                         | C      |
| [GIVE unit-id \[EACH\] amount SILBER](./cmd-give.md)                    | give silver                                       | C      |
| [GIVE unit-id \[EACH\] amount gegenstand](./cmd-give.md)                | give item                                         | C      |
| [GIVE 0 amount SILBER](./cmd-give.md)                                   | throwing away objects                             | C      |
| [GIVE 0 amount MEN](./cmd-give.md)                                      |                                                   | C      |
| [GIVE 0 amount gegenstand](./cmd-give.md)                               |                                                   | C      |
| [GROUP \["name"\]](./cmd-group.md)                                      | forms groups of units                             | C      |
| [HELP faction-id ALL \[NOT\]](./cmd-help.md)                            | set up/revoke an unilateral alliance              | C      |
| [HELP faction-id GIVE \[NOT\]](./cmd-help.md)                           |                                                   | C      |
| [HELP faction-id COMBAT \[NOT\]](./cmd-help.md)                         |                                                   | C      |
| [HELP faction-id GUARD \[NOT\]](./cmd-help.md)                          |                                                   | C      |
| [HELP faction-id SILBER \[NOT\]](./cmd-help.md)                         |                                                   | C      |
| [HELP faction-id PARTEITARNUNG \[NOT\]](./cmd-help.md)                  |                                                   | C      |
| [[cmd-combat]]                                                          | set the combat behaviour                          | C      |
| [COMBAT AGGRESSIV](./cmd-combat.md)                                     |                                                   | C      |
| [COMBAT DEFENSIV](./cmd-combat.md)                                      |                                                   | C      |
| [COMBAT FLIEHE](./cmd-combat.md)                                        |                                                   | C      |
| [COMBAT HELP \[NOT\]](./cmd-combat.md)                                  | the unit is \[not\] helped in the fight           | C      |
| [COMBAT REAR](./cmd-combat.md)                                          |                                                   | C      |
| [COMBAT NOT](./cmd-combat.md)                                           |                                                   | C      |
| [COMBATSPELL \[LEVEL n\] "spell" \[NOT\]](./cmd-combatspell.md)         | set spell for combat                              | C      |
| [BUY amount luxusgut](./cmd-buy.md)                                     | buy luxury item                                   | L[^3]  |
| [CONTACT unit-id](./cmd-contact.md)                                     | contact foreign unit                              | C      |
| [TEACH unit-id \[unit-id etc.\]](./cmd-teach.md)                        | teach units                                       | L      |
| [LEARN talent](./cmd-learn.md)                                          | learn a skill                                     | L      |
| [LEARN AUTO talent](./cmd-learn-auto.md)                                | learn or teach a skill                            | L      |
| [LOCALE en/de](./cmd-locale.md)                                         | no function (only for tools)                      | C      |
| [MAKE TEMP unit-alias-nr \["name"\]](./cmd-make.md)                     | creates a new unit                                | C      |
| [MAKE \[level\] gebäude-typ \[building-id\]](./cmd-make.md)             | erect or extend a building                        | L      |
| [MAKE \[level\] SHIP \[ship-id\]](./cmd-make.md)                        | extend a ship                                     | L      |
| [[cmd-make]]                                                            | baue weiter an Gebäude/Schiff ??                  | L      |
| [MAKE \[level\] BOOT](./cmd-make.md)                                    | build a boat                                      | L      |
| [MAKE \[level\] LANGBOOT](./cmd-make.md)                                | build a longboat                                  | L      |
| [MAKE \[level\] DRACHENSCHIFF](./cmd-make.md)                           | build a dragonship                                | L      |
| [MAKE \[level\] KARAVELLE](./cmd-make.md)                               |                                                   | L      |
| [MAKE \[level\] TRIREME](./cmd-make.md)                                 |                                                   | L      |
| [MAKE \[level\] GALEONE](./cmd-make.md)                                 |                                                   | L      |
| [MAKE \[level\] STRASSE richtung](./cmd-make.md)                        | build road                                        | L      |
| [MAKE \[amount\] HERB](./cmd-make.md)                                   | pick herbs in a region                            | L      |
| [MAKE \[amount\] trank](./cmd-make.md)                                  | make a potion                                     | L      |
| [MAKE \[amount\] gegenstand](./cmd-make.md)                             | make an item                                      | L      |
| [MOVE richtung \[richtung etc.\]](./cmd-move.md)                        | move unit                                         | L      |
| [[cmd-next]]                                                            | ends the orders of a faction                      | C      |
| [NUMBER UNIT \[neue\_nr\]](./cmd-number.md)                             | gives a new id                                    | C      |
| [NUMBER BUILDING \[neue\_nr\]](./cmd-number.md)                         |                                                   | C      |
| [NUMBER FACTION \[neue\_nr\]](./cmd-number.md)                          |                                                   | C      |
| [NUMBER SHIP \[neue\_nr\]](./cmd-number.md)                             |                                                   | C      |
| [OPTION AUSWERTUNG \[NOT\]](./cmd-option.md)                            | Set / Revoke Options                              | C      |
| [OPTION COMPUTER \[NOT\]](./cmd-option.md)                              |                                                   | C      |
| [OPTION ZIPPED \[NOT\]](./cmd-option.md)                                |                                                   | C      |
| [OPTION BZIP2 \[NOT\]](./cmd-option.md)                                 |                                                   | C      |
| [OPTION SILBERPOOL \[NOT\]](./cmd-option.md)                            |                                                   | C      |
| [OPTION MATERIALPOOL \[NOT\]](./cmd-option.md)                          |                                                   | C      |
| [OPTION ADRESSEN \[NOT\]](./cmd-option.md)                              |                                                   | C      |
| [OPTION ZUGVORLAGE \[NOT\]](./cmd-option.md)                            |                                                   | C      |
| [OPTION STATISTIK \[NOT\]](./cmd-option.md)                             |                                                   | C      |
| [OPTION TALENTVERSCHIEBUNG \[NOT\]](./cmd-option.md)                    |                                                   | C      |
| [OPTION PUNKTE \[NOT\]](./cmd-option.md)                                |                                                   | C      |
| [PASSWORD "neues-passwort"](./cmd-password.md)                          | set new password                                  | C      |
| [PLANT \[amount\] HERB](./cmd-plant.md)                                 | Plant herbs                                       | L      |
| [PLANT \[amount\] BÄUME](./cmd-plant.md)                                | Plant seeds                                       | L      |
| [PLANT \[amount\] MALLORNSAMEN](./cmd-plant.md)                         | Plant mallorn seeds                               | L      |
| [PLANT \[amount\] SAMEN](./cmd-plant.md)                                | Plant seeds                                       | L      |
| [PIRACY \[partei\_1\] \[partei\_2\] \[...\]](./cmd-piracy.md)           | Set Piracy                                        | L      |
| [PREFIX \[präfix\]](./cmd-prefix.md)                                    | prepend the race name with a prefix               | C      |
| [REGION x,y](./cmd-region.md)                                           | no function (only for tools)                      | C      |
| [RECRUIT amount](./cmd-recruit.md)                                      | recruit men (persons of your race)                | C      |
| [RESERVE amount "gegenstand"](./cmd-reserve.md)                         | reserve item                                      | C      |
| [RESERVE amount SILBER](./cmd-reserve.md)                               | reserve silver                                    | C      |
| [ROUTE richtung \[richtung etc.\]](./cmd-route.md)                      | Travel                                            | L      |
| [SORT BEFORE unit-id](./cmd-sort.md)                                    | sort unit in report                               | C      |
| [SORT AFTER unit-id](./cmd-sort.md)                                     |                                                   | C      |
| [SPY unit-id](./cmd-spy.md)                                             | spy a unit                                        | L      |
| [LANGUAGE en/de](./cmd-language.md)                                     | Change Language for orders                        | C      |
| [QUIT "passwort" \[FACTION faction-id\]](./cmd-quit.md)                 | quit the game (merge with another faction)        | C      |
| [HIDE \[level\]](./cmd-tax.md)                                          | set hide level                                    | C      |
| [HIDE rasse](./cmd-tax.md)                                              | Demon: disguise as another race                   | C      |
| [HIDE FACTION \[NOT\]](./cmd-tax.md)                                    |                                                   | C      |
| [HIDE FACTION NUMBER nummer](./cmd-tax.md)                              | disguised as another faction                      | C      |
| [CARRY unit-id](./cmd-carry.md)                                         | transport another unit                            | C      |
| [TAX \[betrag\]](./cmd-tax.md)                                          | tax peasants (max. 20 silver/skill lvl)           | L      |
| [ENTERTAIN \[betrag\]](./cmd-entertain.md)                              | earn 20 or more silver (max. 20 silver/skill lvl) | L      |
| [ORIGIN \[x y\]](./cmd-origin.md)                                       | Sets the origin to x,y                            | C      |
| [FORGET talent](./cmd-forget.md)                                        | forget a skill                                    | C      |
| [SELL amount luxusgut](./cmd-sell.md)                                   | sell luxury goods                                 | PL[^4] |
| [[cmd-leave]]                                                           | leave ship or building                            | C      |
| [CAST \[REGION x y\] \[LEVEL n\] "zauberspruch" \[...\]](./cmd-cast.md) | Cast spells                                       | PL     |
| [SHOW "zauberspruch"](./cmd-show.md)                                    | retrieve spell description                        | C      |
| [[cmd-destroy]]                                                         | building, ship, or road                           | L      |
| [GROW PFERDE](./cmd-grow.md)                                            | breed horses, needs a stable                      | L      |
| [GROW HERB](./cmd-grow.md)                                              |                                                   | L      |
| [GROW BÄUME](./cmd-grow.md)                                             |                                                   | L      |

## Voir aussi

- [[ordres]]
- [[sequence-des-ordres]]

Poursuivre la lecture : [[premier-tour]].

[^1]: Voir [Les conséquences de la bataille];
[^2]: Si l'unité suivie ne se déplace pas, un autre ordre long peut être exécuté à la place
[^3]: peut être combiné avec `SELL`
[^4]: peut être combiné avec l'ordre `BUY`

<!-- From [https://wiki.eressea.de/index.php?title=Diskussion:Kurzbeschreibung/fr&oldid=13471] -->

[Les conséquences de la bataille]: ./war.md#fin-du-combat
