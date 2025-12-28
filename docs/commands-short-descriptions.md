---
# cSpell:locale en
alias: discussion-short-description
---
# Discussion: Short description

Under "S/L" it is noted whether the [Order] is a short or long order, i.e. whether it is executed immediately (and further orders are possible afterwards) or takes a whole round to execute. S is a short order, L is a long order.

\(L\) denotes a pseudo-long [Order] that can be given to a unit multiple times. However, no other long order can be executed.

Brief description of orders.

<!-- [ => &#91; ] &#93; because '[' or ']' inside an overriden alias link value fails. -->
| Order (Deutsch)                                           | Beschreibung                                      | S/L         |
|-----------------------------------------------------------|---------------------------------------------------|-------------|
| [[cmd-guard|`GUARD`&nbsp;&#91;`NOT`&#93;]]                | guard the region                                  | S           |
| [[comment-with-slashes|`//`]]                             | permanent comment                                 | S           |
| [[cmd-attack|`ATTACK unit-id`]]                           | attacks the unit                                  | (L)\*       |
| [[cmd-banner|`BANNER "text"`]]                            | Sets text for the address list                    | S           |
| [[cmd-buy|`BUY number luxury-item`]]                      | buy luxury number                                 | L\*\*\*     |
| [[cmd-carry|`CARRY unit-id`]]                             | transport another unit                            | S           |
| [[cmd-cast|`CAST`&nbsp;&#91;`REGION x y`&#93;&nbsp;&#91;`LEVEL n`&#93;&nbsp;`"spell" ...`]] | Cast spells                                       | (L)         |
| [[cmd-claim|`CLAIM number item`]]                         | Fetches items from faction pool                   | S           |
| [[cmd-combat|`COMBAT AGGRESSIVE`]]                        |                                                   | S           |
| [[cmd-combat|`COMBAT DEFENSIVE`]]                         |                                                   | S           |
| [[cmd-combat|`COMBAT FLIEHE`]]                            |                                                   | S           |
| [[cmd-combat|`COMBAT HELP`&nbsp;&#91;`NOT`&#93;]]         | the unit is `[NOT]` helped in the fight           | S           |
| [[cmd-combat|`COMBAT NOT`]]                               |                                                   | S           |
| [[cmd-combat|`COMBAT REAR`]]                              |                                                   | S           |
| [[cmd-combatspell|`COMBATSPELL`&nbsp;&#91;`LEVEL n`&#93;&nbsp;`"spell"`&nbsp;&#91;`NOT`&#93;]] | set spell for combat                              | S           |
| [[cmd-contact|`CONTACT unit-id`]]                         | contact foreign unit                              | S           |
| [[cmd-default|`DEFAULT befehl`]]                          | sets the default order for the next turn          | S           |
| [[cmd-describe|`DESCRIBE BUILDING "text"`]]               |                                                   | S           |
| [[cmd-describe|`DESCRIBE PRIVATE "text"`]]                | unit description for the owner                    | S           |
| [[cmd-describe|`DESCRIBE REGION "text"`]]                 |                                                   | S           |
| [[cmd-describe|`DESCRIBE SHIP "text"`]]                   |                                                   | S           |
| [[cmd-describe|`DESCRIBE UNIT "text"`]]                   | describes object                                  | S           |
| [[cmd-email|`EMAIL email@adresse`]]                       | sets the e−mail the report is sent to             | S           |
| [[cmd-enter|`ENTER BUILDING building-id`]]                | Enter a building                                  | S           |
| [[cmd-enter|`ENTER SHIP ship-id`]]                        | Enter a ship                                      | S           |
| [[cmd-entertain|`ENTERTAIN`&nbsp;&#91;*`amount`*&#93;]]   | earn 20 or more silver (max. 20 silver/skill lvl) | L           |
| [[cmd-eressea|`ERESSEA faction-id "password"`]]           | beginning of faction's orders                     | S           |
| [[cmd-follow|`FOLLOW SHIP ship-id`]]                      | follows a ship                                    | (L)\*\*     |
| [[cmd-follow|`FOLLOW UNIT unit-id`]]                      | follows a unit                                    | (L)\*\*     |
| [[cmd-forget|`FORGET skill`]]                             | forget a skill                                    | S           |
| [[cmd-give|`GIVE 0 number item`]]                         |                                                   | S           |
| [[cmd-give|`GIVE 0 number MEN`]]                          |                                                   | S           |
| [[cmd-give|`GIVE 0 number SILVER`]]                       | throwing away objects                             | S           |
| [[cmd-give|`GIVE unit-id`&nbsp;&#91;`EACH`&#93;&nbsp;`number item`]]            | give number                                       | S           |
| [[cmd-give|`GIVE unit-id`&nbsp;&#91;`EACH`&#93;&nbsp;`number MEN`]]             | give a unit men                                   | S           |
| [[cmd-give|`GIVE unit-id`&nbsp;&#91;`EACH`&#93;&nbsp;`number SHIP`]]            | give SHIP to form convoys                         | S           |
| [[cmd-give|`GIVE unit-id`&nbsp;&#91;`EACH`&#93;&nbsp;`number SILVER`]]          | give silver                                       | S           |
| [[cmd-give|`GIVE unit-id COMMAND`]]                       | give a unit ship/ building control                | S           |
| [[cmd-give|`GIVE unit-id HERB`]]                          | give a unit all herbs                             | S           |
| [[cmd-give|`GIVE unit-id UNIT`]]                          | give unit to a foreign faction                    | S           |
| [[cmd-group|`GROUP`&nbsp;&#91;`"name"`&#93;]]                            | forms groups of units                             | S           |
| [[cmd-grow|`GROW HERB`]]                                  |                                                   | L           |
| [[cmd-grow|`GROW HORSES`]]                                | breed horses, needs a stable                      | L           |
| [[cmd-grow|`GROW TREES`]]                                 |                                                   | L           |
| [[cmd-help|`HELP faction-id ALL`&nbsp;&#91;`NOT`&#93;]]        | set up/revoke an unilateral alliance              | S           |
| [[cmd-help|`HELP faction-id COMBAT`&nbsp;&#91;`NOT`&#93;]]     |                                                   | S           |
| [[cmd-help|`HELP faction-id FACTIONSTEAL`&nbsp;&#91;`NOT`&#93;]]|                                                   | S           |
| [[cmd-help|`HELP faction-id GIVE`&nbsp;&#91;`NOT`&#93;]]       |                                                   | S           |
| [[cmd-help|`HELP faction-id GUARD`&nbsp;&#91;`NOT`&#93;]]      |                                                   | S           |
| [[cmd-help|`HELP faction-id SILVER`&nbsp;&#91;`NOT`&#93;]]     |                                                   | S           |
| [[cmd-tax|`HIDE`&nbsp;&#91;`level`&#93;]]                      | set hide level                                    | S           |
| [[cmd-tax|`HIDE FACTION`&nbsp;&#91;`NOT`&#93;]]                |                                                   | S           |
| [[cmd-tax|`HIDE FACTION NUMBER nummer`]]                  | disguised as another faction                      | S           |
| [[cmd-tax|`HIDE race`]]                                   | Demon: disguise as another race                   | S           |
| [[cmd-language|`LANGUAGE en/de`]]                         | Change Language for orders                        | S           |
| [[cmd-learn-auto|`LEARN AUTO skill`]]                     | learn or teach a skill                            | L           |
| [[cmd-learn|`LEARN skill`]]                               | learn a skill                                     | L           |
| [[cmd-locale|`LOCALE en/de`]]                             | no function (only for tools)                      | S           |
| [[cmd-make|`MAKE`&nbsp;&#91;`number`&#93;&nbsp;`HERB`]]                         | pick herbs in a region                            | L           |
| [[cmd-make|`MAKE`&nbsp;&#91;`number`&#93;&nbsp;`item`]]                         | make an number                                    | L           |
| [[cmd-make|`MAKE`&nbsp;&#91;`number`&#93;&nbsp;`trank`]]                        | make a potion                                     | L           |
| [[cmd-make|`MAKE`&nbsp;&#91;`stufe`&#93;&nbsp;`BOAT`]]                          | build a boat                                      | L           |
| [[cmd-make|`MAKE`&nbsp;&#91;`stufe`&#93;&nbsp;`building-type`&nbsp;&#91;`building-id`&#93;]] | erect or extend a building                        | L           |
| [[cmd-make|`MAKE`&nbsp;&#91;`stufe`&#93;&nbsp;`CARAVEL`]]                       |                                                   | L           |
| [[cmd-make|`MAKE`&nbsp;&#91;`stufe`&#93;&nbsp;`DRAGONSHIP`]]                    | build a dragonship                                | L           |
| [[cmd-make|`MAKE`&nbsp;&#91;`stufe`&#93;&nbsp;`GALLEON`]]                       |                                                   | L           |
| [[cmd-make|`MAKE`&nbsp;&#91;`stufe`&#93;&nbsp;`LONGBOAT`]]                      | build a longboat                                  | L           |
| [[cmd-make|`MAKE`&nbsp;&#91;`stufe`&#93;&nbsp;`ROAD direction`]]                | build road                                        | L           |
| [[cmd-make|`MAKE`&nbsp;&#91;`stufe`&#93;&nbsp;`SHIP`&nbsp;&#91;`ship-id`&#93;]] | extend a ship                                     | L           |
| [[cmd-make|`MAKE`&nbsp;&#91;`stufe`&#93;&nbsp;`TRIREME`]]                       |                                                   | L           |
| [[cmd-make|`MAKE TEMP unit-alias-nr`&nbsp;&#91;`"name"`&#93;]]           | creates a new unit                                | S           |
| [[cmd-message|`MESSAGE BUILDING building-id "text"`]]     | Send a message                                    | S           |
| [[cmd-message|`MESSAGE FACTION faction-id "text"`]]       | Send a message                                    | S           |
| [[cmd-message|`MESSAGE REGION "text"`]]                   | Send a message                                    | S           |
| [[cmd-message|`MESSAGE SHIP ship-id "text"`]]             | Send a message                                    | S           |
| [[cmd-message|`MESSAGE UNIT unit id "text"`]]             | Send a message                                    | S           |
| [[cmd-move|`MOVE direction`&nbsp;&#91;`direction`&#93;`...`]]            | move unit                                         | L           |
| [[cmd-name|`NAME BUILDING "name"`]]                       |                                                   | S           |
| [[cmd-name|`NAME FACTION "name"`]]                        |                                                   | S           |
| [[cmd-name|`NAME FOREIGN BUILDING building-id "name"`]]   |                                                   | S           |
| [[cmd-name|`NAME FOREIGN FACTION faction-id "name"`]]     |                                                   | S           |
| [[cmd-name|`NAME FOREIGN SHIP ship-id "name"`]]           |                                                   | S           |
| [[cmd-name|`NAME FOREIGN UNIT unit-id "name"`]]           | names the specified foreign object                | S           |
| [[cmd-name|`NAME REGION "name"`]]                         |                                                   | S           |
| [[cmd-name|`NAME SHIP "name"`]]                           |                                                   | S           |
| [[cmd-name|`NAME UNIT "name"`]]                           | names the specified object                        | S           |
| [[cmd-number|`NUMBER BUILDING`&nbsp;&#91;`new-id`&#93;]]  |                                                   | S           |
| [[cmd-number|`NUMBER FACTION`&nbsp;&#91;`new-id`&#93;]]                  |                                                   | S           |
| [[cmd-number|`NUMBER SHIP`&nbsp;&#91;`new-id`&#93;]]           |                                                   | S           |
| [[cmd-number|`NUMBER UNIT`&nbsp;&#91;`new-id`&#93;]]           | gives a new id                                    | S           |
| [[cmd-option|`OPTION ADRESSES`&nbsp;&#91;`NOT`&#93;]]          |                                                   | S           |
| [[cmd-option|`OPTION AUSWERTUNG`&nbsp;&#91;`NOT`&#93;]]        | Set / Revoke Options                              | S           |
| [[cmd-option|`OPTION BZIP2`&nbsp;&#91;`NOT`&#93;]]             |                                                   | S           |
| [[cmd-option|`OPTION COMPUTER`&nbsp;&#91;`NOT`&#93;]]          |                                                   | S           |
| [[cmd-option|`OPTION MATERIALPOOL`&nbsp;&#91;`NOT`&#93;]]      |                                                   | S           |
| [[cmd-option|`OPTION PUNKTE`&nbsp;&#91;`NOT`&#93;]]            |                                                   | S           |
| [[cmd-option|`OPTION SILBERPOOL`&nbsp;&#91;`NOT`&#93;]]        |                                                   | S           |
| [[cmd-option|`OPTION STATISTICS`&nbsp;&#91;`NOT`&#93;` ``]]    |                                                   | S           |
| [[cmd-option|`OPTION TALENTVERSCHIEBUNG`&nbsp;&#91;`NOT`&#93;]]|                                                   | S           |
| [[cmd-option|`OPTION ZIPPED`&nbsp;&#91;`NOT`&#93;]]            |                                                   | S           |
| [[cmd-option|`OPTION ZUGVORLAGE`&nbsp;&#91;`NOT`&#93;]]   |                                                   | S           |
| [[cmd-origin|`ORIGIN`&nbsp;&#91;`x y`&#93;]]                             | Sets the origin to x,y                            | S           |
| [[cmd-password|`PASSWORD "new-password"`]]                | set new password                                  | S           |
| [[cmd-pay-not|`PAY NOT`&nbsp;&#91;`building-id`&#93;]]                   | do not pay a maintenance                          | S           |
| [[cmd-piracy|`PIRACY`&nbsp;&#91;`faction_1`&#93;` [faction_2`&#93;`...`]]     | Set Piracy                                        | L           |
| [[cmd-plant|`PLANT`&nbsp;&#91;`number`&#93;&nbsp;`HERB`]]                       | Plant herbs                                       | L           |
| [[cmd-plant|`PLANT`&nbsp;&#91;`number`&#93;&nbsp;`MALLORNSEEDS`]]               | Plant mallorn seeds                               | L           |
| [[cmd-plant|`PLANT`&nbsp;&#91;`number`&#93;&nbsp;`SEEDS`]]                      | Plant seeds                                       | L           |
| [[cmd-plant|`PLANT`&nbsp;&#91;`number`&#93;&nbsp;`TREES`]]                      | Plant seeds                                       | L           |
| [[cmd-prefix|`PREFIX`&nbsp;&#91;`präfix`&#93;]]                          | prepend the race name with a prefix               | S           |
| [[cmd-quit|`QUIT "password"`&nbsp;&#91;`FACTION faction-id`&#93;`]]       | quit the game [merge with another faction]        | S           |
| [[cmd-recruit|`RECRUIT number`]]                          | recruit men (persons of your race)                | S           |
| [[cmd-region|`REGION x,y`]]                               | no function (only for tools)                      | S           |
| [[cmd-research|`RESEARCH HERB`]]                          | search for herbs                                  | L           |
| [[cmd-reserve|`RESERVE number "item"`]]                   | reserve number                                    | S           |
| [[cmd-reserve|`RESERVE number SILVER`]]                   | reserve silver                                    | S           |
| [[cmd-ride|`RIDE unit-id`]]                               | be transported by unit−id                         | L           |
| [[cmd-route|`ROUTE direction`&nbsp;&#91;`direction`&#93;`...`]]          | Travel                                            | L           |
| [[cmd-sell|`SELL number luxury-item`]]                    | sell luxury goods                                 | (L)\*\*\*\* |
| [[cmd-show|`SHOW "spell"`]]                               | retrieve spell description                        | S           |
| [[cmd-sort|`SORT AFTER unit-id`]]                         |                                                   | S           |
| [[cmd-sort|`SORT BEFORE unit-id`]]                        | sort unit in report                               | S           |
| [[cmd-spy|`SPY unit-id`]]                                 | spy a unit                                        | L           |
| [[cmd-steal|`STEAL unit-id`]]                             | steal 50 Silver or more                           | L           |
| [[cmd-tax|`TAX`&nbsp;&#91;*`amount`*&#93;]]                                | tax peasants (max. 20 silver/skill lvl)           | L           |
| [[cmd-teach|`TEACH unit-id`&nbsp;&#91;`unit-id`&#93;`...`]]              | teach units                                       | L           |
| [[cmd-unit|`UNIT unit-id`]]                               | beginning of a unit's orders                      | S           |
| [[cmd-use|`USE`&nbsp;&#91;*`number`*&#93;&nbsp;`trank`]]  | uses alchemical potion                            | S           |
| [[cmd-make]]                                              | baue weiter an Gebäude/Schiff ??                  | L           |
| [[cmd-destroy]]                                           | building, ship, or road                           | L           |
| [[cmd-work]]                                              | earns 10 silver or more                           | L           |
| [[cmd-end]]                                               | ends a MAKE TEMP block                            | S           |
| [[cmd-next]]                                              | ends the orders of a faction                      | S           |
| [[cmd-leave]]                                             | leave ship or building                            | S           |
| [[cmd-promote]]                                           | Promote a unit to hero                            | S           |
| [[cmd-combat]]                                            | set the combat behavior                           | S           |

\* voir [The aftermath of battle]  
\*\*If the tracked unit does not move, another long order can be executed instead  
\*\*\*can be combined with SELL  
\*\*\*\*can be combined with BUY  

## See also

- [Orders]
- [Orders sequence]

Continue reading: [Der erste Zug](./first-round.md)

<!-- From [https://wiki.eressea.de/index.php?title=Diskussion:Kurzbeschreibung/en&oldid=8215] -->

  [Order]: ./commands.md
  [The aftermath of battle]: ./war.md#the-end
  [Orders]: ./commands.md
  [Orders sequence]: ./commands-sequence.md
