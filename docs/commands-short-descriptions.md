---
alias:
    name: discussion-short-description
    text: "Discussion: Short description"
---
# Discussion: Short description

Under "K/L" it is noted whether the [Order] is a short or long order, i.e. whether it is executed immediately (and further orders are possible afterwards) or takes a whole round to execute. K is a short order, L is a long order.

\(L\) denotes a pseudo-long [Order] that can be given to a unit multiple times. However, no other long order can be executed.

brief description of orders

| Befehl (Deutsch)                                                                | Order (English)                              | Beschreibung                                      | K/L         |
|---------------------------------------------------------------------------------|----------------------------------------------|---------------------------------------------------|-------------|
| [//](./cmd-comment-slash.md "KOMMENTAR")                                                    | //                                           | permanent comment                                 | K           |
| [[cmd-work]](./cmd-work.md "WORK")                                                   | WORK                                         | earns 10 silver or more                           | L           |
| [ATTACK unit-id](./cmd-attack.md "ATTACK")                               | ATTACK unit-ID                               | attacks the unit                                  | (L)\*       |
| [BANNER "text"](./cmd-banner.md "BANNER")                                               | BANNER                                       | Sets text for the address list                    | K           |
| [CLAIM anzahl gegenstand](./cmd-claim.md "CLAIM")                     | CLAIM                                        | Fetches items from party pool                     | K           |
| [[cmd-promote]](./cmd-promote.md "PROMOTE")                                        | PROMOTE                                      | Promote a unit to heroe                           | K           |
| [STEAL unit-id](./cmd-steal.md "STEAL")                                        | STEAL unit-ID                                | steal 50 Silver or more                           | L           |
| [NAME UNIT "name"](./cmd-name.md "NAME")                                    | NAME UNIT "name"                             | names the specified object                        | K           |
| [NAME PARTEI "name"](./cmd-name.md "NAME")                                     | NAME FACTION "name"                          |                                                   | K           |
| [NAME GEBÄUDE "name"](./cmd-name.md "NAME")                                    | NAME BUILDING "name"                         |                                                   | K           |
| [NAME SCHIFF "name"](./cmd-name.md "NAME")                                     | NAME SHIP "name"                             |                                                   | K           |
| [NAME REGION "name"](./cmd-name.md "NAME")                                     | NAME REGION "name"                           |                                                   | K           |
| [NAME FREMDE UNIT unit-id "name"](./cmd-name.md "NAME")                  | NAME FOREIGN UNIT unit-no "name"             | names the specified foreign object                | K           |
| [NAME FREMDES SCHIFF ship-id "name"](./cmd-name.md "NAME")                   | NAME FOREIGN SHIP ship-no "name"             |                                                   | K           |
| [NAME FREMDES GEBÄUDE building-id "name"](./cmd-name.md "NAME")                 | NAME FOREIGN BUILDING building-no "name"     |                                                   | K           |
| [NAME FREMDE PARTEI faction-id "name"](./cmd-name.md "NAME")                    | NAME FOREIGN FACTION faction-id "name"       |                                                   | K           |
| [USE \[anzahl\] trank](./cmd-use.md "USE")                                  | USE \[amount\] potion                        | uses alchemical potion                            | K           |
| [DESCRIBE UNIT "text"](./cmd-describe.md "DESCRIBE")                           | DESCRIBE UNIT "text"                         | describes object                                  | K           |
| [DESCRIBE PRIVAT "text"](./cmd-describe.md "DESCRIBE")                            | DESCRIBE PRIVATE "text"                      | unit description for the owner                    | K           |
| [DESCRIBE GEBÄUDE "text"](./cmd-describe.md "DESCRIBE")                           | DESCRIBE BUILDING "text"                     |                                                   | K           |
| [DESCRIBE SCHIFF "text"](./cmd-describe.md "DESCRIBE")                            | DESCRIBE SHIP "text"                         |                                                   | K           |
| [DESCRIBE REGION "text"](./cmd-describe.md "DESCRIBE")                            | DESCRIBE REGION "text"                       |                                                   | K           |
| [ENTER GEBÄUDE building-id](./cmd-enter.md "ENTER")                                | ENTER BUILDING building-id                   | Enter a building                                  | K           |
| [ENTER SCHIFF ship-id](./cmd-enter.md "ENTER")                                  | ENTER SHIP ship-id                           | Enter a ship                                      | K           |
| [GUARD \[NOT\]](./cmd-guard.md "GUARD")                                         | GUARD                                        | guard the region                                  | K           |
| [BEZAHLE NOT \[building-id\]](./cmd-pay-not.md "BEZAHLE")                              | PAY \[NOT\]                                  | do not pay a maintenance                          | K           |
| [MESSAGE REGION "text"](./cmd-message.md "MESSAGE")                               | MESSAGE REGION "text"                        | Send a message                                    | K           |
| [MESSAGE SCHIFF ship-id "text"](./cmd-message.md "MESSAGE")                     | MESSAGE SHIP ship-id "text"                  | Send a message                                    | K           |
| [MESSAGE GEBÄUDE building-id "text"](./cmd-message.md "MESSAGE")                   | MESSAGE BUILDING building-id "text"          | Send a message                                    | K           |
| [MESSAGE UNIT unit id "text"](./cmd-message.md "MESSAGE")                      | MESSAGE UNIT unit-id "text"                  | Send a message                                    | K           |
| [MESSAGE PARTEI faction-id "text"](./cmd-message.md "MESSAGE")                     | MESSAGE FACTION faction-id "text"            | Send a message                                    | K           |
| [DEFAULT befehl](./cmd-default.md "DEFAULT")                                            | DEFAULT                                      | sets the default order for the next turn          | K           |
| [UNIT unit-id](./cmd-unit.md "UNIT")                                        | UNIT unit-ID                                 | beginning of a unit's orders                      | K           |
| [EMAIL email@adresse](./cmd-email.md "EMAIL")                                           | EMAIL email@adresse                          | sets the e−mail the report is sent to             | K           |
| [[cmd-end]](./cmd-end.md "END")                                                            | END                                          | ends a MAKE TEMP block                            | K           |
| [ERESSEA faction-id "passwort"](./cmd-eressea.md "ERESSEA")                              | ERESSEA faction-id "password"                | beginning of faction's orders                     | K           |
| [RIDE unit-id](./cmd-ride.md "RIDE")                                              | RIDE unit-id                                 | be transported by unit−id                         | L           |
| [FOLLOW UNIT unit-id](./cmd-follow.md "FOLLOW")                                      | FOLLOW UNIT unit-id                          | follows a unit                                    | (L)\*\*     |
| [FOLLOW SCHIFF ship-id](./cmd-follow.md "FOLLOW")                                        | FOLLOW SHIP ship-id                          | follows a ship                                    | (L)\*\*     |
| [RESEARCH KRÄUTER](./cmd-research.md "RESEARCH")                                           | RESEARCH herbs                               | search for herbs                                  | L           |
| [GIVE unit-id KRÄUTER](./cmd-give.md "GIVE")                                            | GIVE unit-id herbs                           | give a unit all herbs                             | K           |
| [GIVE unit-id KOMMANDO](./cmd-give.md "GIVE")                                           | GIVE unit-id command                         | give a unit ship/ building control                | K           |
| [GIVE unit-id UNIT](./cmd-give.md "GIVE")                                            | GIVE unit-id UNIT                            | give unit to a foreign faction                    | K           |
| [GIVE unit-id \[JE\] anzahl PERSONEN](./cmd-give.md "GIVE")                             | GIVE unit-id \[each\] amount MEN             | give a unit men                                   | K           |
| [GIVE unit-id \[JE\] anzahl SCHIFF](./cmd-give.md "GIVE")                               | GIVE unit-id \[each\] amount SHIP            | give SHIP to form convoys                         | K           |
| [GIVE unit-id \[JE\] anzahl SILBER](./cmd-give.md "GIVE")                               | GIVE unit-id \[each\] amount SILVER          | give silver                                       | K           |
| [GIVE unit-id \[JE\] anzahl gegenstand](./cmd-give.md "GIVE")                           | GIVE unit-id \[each\] amount item            | give item                                         | K           |
| [GIVE 0 anzahl SILBER](./cmd-give.md "GIVE")                                               | GIVE 0 number SILVER                         | throwing away objects                             | K           |
| [GIVE 0 anzahl PERSONEN](./cmd-give.md "GIVE")                                             | GIVE 0 number MEN                            |                                                   | K           |
| [GIVE 0 anzahl gegenstand](./cmd-give.md "GIVE")                                           | GIVE 0 number item                           |                                                   | K           |
| [GROUP \["name"\]](./cmd-group.md "GROUP")                                           | GROUP \["name"\]                             | forms groups of units                             | K           |
| [HELP faction-id ALLES \[NOT\]](./cmd-help.md "HELP")                               | HELP faction-id ALL \[NOT\]                  | set up/revoke an unilateral alliance              | K           |
| [HELP faction-id GIVE \[NOT\]](./cmd-help.md "HELP")                                 | HELP faction-id GIVE \[NOT\]                 |                                                   | K           |
| [HELP faction-id COMBAT \[NOT\]](./cmd-help.md "HELP")                              | HELP faction-id COMBAT \[NOT\]               |                                                   | K           |
| [HELP faction-id GUARD \[NOT\]](./cmd-help.md "HELP")                             | HELP faction-id GUARD \[NOT\]                |                                                   | K           |
| [HELP faction-id SILBER \[NOT\]](./cmd-help.md "HELP")                              | HELP faction-id SILVER \[NOT\]               |                                                   | K           |
| [HELP faction-id PARTEITARNUNG \[NOT\]](./cmd-help.md "HELP")                       | HELP faction-id FACTIONSTEALTH \[NOT\]       |                                                   | K           |
| [[cmd-combat]](./cmd-combat.md "COMBAT")                                                 | COMBAT                                       | set the combat behaviour                          | K           |
| [COMBAT AGGRESSIV](./cmd-combat.md "COMBAT")                                       | COMBAT AGGRESSIVE                            |                                                   | K           |
| [COMBAT DEFENSIV](./cmd-combat.md "COMBAT")                                        | COMBAT DEFENSIVE                             |                                                   | K           |
| [COMBAT FLIEHE](./cmd-combat.md "COMBAT")                                          | COMBAT FLEE                                  |                                                   | K           |
| [COMBAT HELP \[NOT\]](./cmd-combat.md "COMBAT")                                 | COMBAT HELP \[NOT\]                          | the unit is \[not\] helped in the fight           | K           |
| [COMBAT HINTEN](./cmd-combat.md "COMBAT")                                          | COMBAT REAR                                  |                                                   | K           |
| [COMBAT NOT](./cmd-combat.md "COMBAT")                                           | COMBAT NOT                                   |                                                   | K           |
| [COMBATSPELL \[LEVEL n\] "zauberspruch" \[NOT\]](./cmd-combatspell.md "COMBATSPELL")  | COMBATSPELL \[level n\] "spell" \[NOT\]      | set spell for combat                              | K           |
| [BUY anzahl luxusgut](./cmd-buy.md "BUY")                                         | BUY amount luxurygood                        | buy luxury item                                   | L\*\*\*     |
| [CONTACT unit-id](./cmd-contact.md "CONTACT")                            | CONTACT unit-no                              | contact foreign unit                              | K           |
| [TEACH unit-id \[unit-id etc.\]](./cmd-teach.md "TEACH")                          | TEACH unit-no                                | teach units                                       | L           |
| [LEARN talent](./cmd-learn.md "LEARN")                                                  | LEARN skill                                  | learn a skill                                     | L           |
| [LEARN AUTO talent](./cmd-learn-auto.md "LEARN AUTO")                                   | LEARN AUTO                                   | learn or teach a skill                            | L           |
| [LOCALE en/de](./cmd-locale.md "LOCALE")                                                | LOCALE en/de                                 | no function (only for tools)                      | K           |
| [MAKE TEMP unit-alias-nr \["name"\]](./cmd-make.md "MAKE")                           | MAKE TEMP unit-alias-nr \["name"\]           | creates a new unit                                | K           |
| [MAKE \[stufe\] gebäude-typ \[building-id\]](./cmd-make.md "MAKE")                    | MAKE \[level\] building-type \[building-ID\] | erect or extend a building                        | L           |
| [MAKE \[stufe\] SCHIFF \[ship-id\]](./cmd-make.md "MAKE")                          | MAKE \[level\] SHIP \[ship-ID\]              | extend a ship                                     | L           |
| [[cmd-make]](./cmd-make.md "MAKE")                                                         | MAKE ??                                      | baue weiter an Gebäude/Schiff ??                  | L           |
| [MAKE \[stufe\] BOOT](./cmd-make.md "MAKE")                                          | MAKE \[level\] boat                          | build a boat                                      | L           |
| [MAKE \[stufe\] LANGBOOT](./cmd-make.md "MAKE")                                      | MAKE \[level\] longboat                      | build a longboat                                  | L           |
| [MAKE \[stufe\] DRACHENSCHIFF](./cmd-make.md "MAKE")                                 | MAKE \[level\] dragonship                    | build a dragonship                                | L           |
| [MAKE \[stufe\] KARAVELLE](./cmd-make.md "MAKE")                                     | MAKE \[level\] caravel                       |                                                   | L           |
| [MAKE \[stufe\] TRIREME](./cmd-make.md "MAKE")                                       | MAKE \[level\] trireme                       |                                                   | L           |
| [MAKE \[stufe\] GALEONE](./cmd-make.md "MAKE")                                       | MAKE \[level\] galleon                       |                                                   | L           |
| [MAKE \[stufe\] STRASSE richtung](./cmd-make.md "MAKE")                              | MAKE \[level\] ROAD direction                | build road                                        | L           |
| [MAKE \[anzahl\] KRÄUTER](./cmd-make.md "MAKE")                                      | MAKE \[amount\] HERBS                        | pick herbs in a region                            | L           |
| [MAKE \[anzahl\] trank](./cmd-make.md "MAKE")                                        | MAKE \[amount\] POTIONS                      | make a potion                                     | L           |
| [MAKE \[anzahl\] gegenstand](./cmd-make.md "MAKE")                                   | MAKE \[amount\] item                         | make an item                                      | L           |
| [MOVE richtung \[richtung etc.\]](./cmd-move.md "MOVE")                                 | MOVE direction \[direction\]                 | move unit                                         | L           |
| [[cmd-next]](./cmd-next.md "NEXT")                                           | NEXT                                         | ends the orders of a faction                      | K           |
| [NUMBER UNIT \[neue\_nr\]](./cmd-number.md "NUMBER")                                 | NUMBER UNIT \[newID\]                        | gives a new id                                    | K           |
| [NUMBER GEBÄUDE \[neue\_nr\]](./cmd-number.md "NUMBER")                                 | NUMBER CASTLE \[newID\]                      |                                                   | K           |
| [NUMBER PARTEI \[neue\_nr\]](./cmd-number.md "NUMBER")                                  | NUMBER FACTION \[newID\]                     |                                                   | K           |
| [NUMBER SCHIFF \[neue\_nr\]](./cmd-number.md "NUMBER")                                  | NUMBER SHIP \[newID\]                        |                                                   | K           |
| [OPTION AUSWERTUNG \[NOT\]](./cmd-option.md "OPTION")                                 | OPTION                                       | Set / Revoke Options                              | K           |
| [OPTION COMPUTER \[NOT\]](./cmd-option.md "OPTION")                                   | OPTION                                       |                                                   | K           |
| [OPTION ZIPPED \[NOT\]](./cmd-option.md "OPTION")                                     | OPTION                                       |                                                   | K           |
| [OPTION BZIP2 \[NOT\]](./cmd-option.md "OPTION")                                      | OPTION                                       |                                                   | K           |
| [OPTION SILBERPOOL \[NOT\]](./cmd-option.md "OPTION")                                 | OPTION                                       |                                                   | K           |
| [OPTION MATERIALPOOL \[NOT\]](./cmd-option.md "OPTION")                               | OPTION                                       |                                                   | K           |
| [OPTION ADRESSEN \[NOT\]](./cmd-option.md "OPTION")                                   | OPTION                                       |                                                   | K           |
| [OPTION ZUGVORLAGE \[NOT\]](./cmd-option.md "OPTION")                                 | OPTION                                       |                                                   | K           |
| [OPTION STATISTIK \[NOT\]](./cmd-option.md "OPTION")                                  | OPTION                                       |                                                   | K           |
| [OPTION TALENTVERSCHIEBUNG \[NOT\]](./cmd-option.md "OPTION")                         | OPTION                                       |                                                   | K           |
| [OPTION PUNKTE \[NOT\]](./cmd-option.md "OPTION")                                     | OPTION                                       |                                                   | K           |
| [PASSWORD "neues-passwort"](./cmd-password.md "PASSWORD")                               | PASSWORD "new-password"                      | set new password                                  | K           |
| [PLANT \[anzahl\] KRÄUTER](./cmd-plant.md "PLANT")                                | PLANT \[amount\] HERBS                       | Plant herbs                                       | L           |
| [PLANT \[anzahl\] BÄUME](./cmd-plant.md "PLANT")                                  | PLANT \[amount\] TREES                       | Plant seeds                                       | L           |
| [PLANT \[anzahl\] MALLORNSAMEN](./cmd-plant.md "PLANT")                           | PLANT \[amount\] "mallorn seeds"             | Plant mallorn seeds                               | L           |
| [PLANT \[anzahl\] SAMEN](./cmd-plant.md "PLANT")                                  | PLANT \[amount\] SEEDS                       | Plant seeds                                       | L           |
| [PIRACY \[partei\_1\] \[partei\_2\] \[...\]](./cmd-piracy.md "PIRACY")         | PIRACY \[faction\_1\] \[faction\_2\]         | Set Piracy                                        | L           |
| [PREFIX \[präfix\]](./cmd-prefix.md "PREFIX")                                      | PREFIX                                       | prepend the race name with a prefix               | K           |
| [REGION x,y](./cmd-region.md "REGION")                                                  | REGION x,y                                   | no function (only for tools)                      | K           |
| [RECRUIT anzahl](./cmd-recruit.md "RECRUIT")                                   | RECRUIT amount                               | recruit men (persons of your race)                | K           |
| [RESERVE anzahl "gegenstand"](./cmd-reserve.md "RESERVE")                      | RESERVE amount item                          | reserve item                                      | K           |
| [RESERVE anzahl SILBER](./cmd-reserve.md "RESERVE")                            | RESERVE amount silver                        | reserve silver                                    | K           |
| [ROUTE richtung \[richtung etc.\]](./cmd-route.md "ROUTE")                              | ROUTE direction \[direction etc.\]           | Travel                                            | L           |
| [SORT BEFORE unit-id](./cmd-sort.md "SORT")                                 | SORT BEFORE unit-id                          | sort unit in report                               | K           |
| [SORT AFTER unit-id](./cmd-sort.md "SORT")                              | SORT AFTER unit-id                           |                                                   | K           |
| [SPY unit-id](./cmd-spy.md "SPY")                                  | SPY unit-id                                  | spy a unit                                        | L           |
| [LANGUAGE en/de](./cmd-language.md "LANGUAGE")                                             | LANGUAGE en/de                               | Change Language for orders                        | K           |
| [QUIT "passwort" \[PARTEI faction-id\]](./cmd-quit.md "QUIT")                         | QUIT "password" \[FACTION Faction-id\]       | quit the game \[merge with another faction\]      | K           |
| [HIDE \[stufe\]](./cmd-tax.md "HIDE")                                               | HIDE \[level\]                               | set hide level                                    | K           |
| [HIDE rasse](./cmd-tax.md "HIDE")                                                   | HIDE \[race\]                                | Demon: disguise as another race                   | K           |
| [HIDE PARTEI \[NOT\]](./cmd-tax.md "HIDE")                                        | HIDE FACTION \[NOT\]                         | hide faction membership (hide as"anonym")         | K           |
| [HIDE PARTEI NUMBER nummer](./cmd-tax.md "HIDE")                                    | HIDE FACTION faction-ID                      | disguised as another faction                      | K           |
| [CARRY unit-id](./cmd-carry.md "CARRY")                      | CARRY unit-id                                | transport another unit                            | K           |
| [TAX \[betrag\]](./cmd-tax.md "TAX")                                           | TAX \[amount\]                               | tax peasants (max. 20 silver/skill lvl)           | L           |
| [ENTERTAIN \[betrag\]](./cmd-entertain.md "ENTERTAIN")                               | ENTERTAIN \[amount\]                         | earn 20 or more silver (max. 20 silver/skill lvl) | L           |
| [ORIGIN \[x y\]](./cmd-origin.md "ORIGIN")                                        | ORIGIN \[x y\]                               | Sets the origin to x,y                            | K           |
| [FORGET talent](./cmd-forget.md "FORGET")                                            | FORGET skill                                 | forget a skill                                    | K           |
| [SELL anzahl luxusgut](./cmd-sell.md "SELL")                                | SELL \[amount\] \[ALL\] good                 | sell luxury goods                                 | (L)\*\*\*\* |
| [[cmd-leave]](./cmd-leave.md "LEAVE")                                                | LEAVE                                        | leave ship or building                            | K           |
| [CAST \[REGION x y\] \[LEVEL n\] "zauberspruch" \[...\]](./cmd-cast.md "CAST") | CAST \[REGION x y\] \[level n\] "spell"      | Cast spells                                       | (L)         |
| [SHOW "zauberspruch"](./cmd-show.md "SHOW")                                          | SHOW                                         | retrieve spell description                        | K           |
| [[cmd-destroy]](./cmd-destroy.md "DESTROY")                                           | DESTROY                                      | building, ship, or road                           | L           |
| [GROW PFERDE](./cmd-grow.md "GROW")                                          | GROW HORSES                                  | breed horses, needs a stable                      | L           |
| [GROW KRÄUTER](./cmd-grow.md "GROW")                                         | GROW HERBS                                   | need "Water of Life"                              | L           |
| [GROW BÄUME](./cmd-grow.md "GROW")                                           | GROW TREES                                   | works ? need "Water of Life"                      | L           |

\* voir [The aftermath of battle]; \*\*If the tracked unit does not move, another long order can be executed instead; \*\*\*can be combined with SELL; \*\*\*\*can be combined with BUY

## See also

- [Orders]
- [Orders sequence]

Continue reading: [Der erste Zug](./first-round.md "First round")

<!-- From [https://wiki.eressea.de/index.php?title=Diskussion:Kurzbeschreibung/en&oldid=8215] -->

  [Order]: ./commands.md "Orders"
  [The aftermath of battle]: ./war.md#the-end "Kampfende"
  [Orders]: ./commands.md "Befehle"
  [Orders sequence]: ./commands-sequence.md "Befehlsreihenfolge"
