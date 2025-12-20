---
# cSpell:locale en
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
| [//](./cmd-comment-slash.md)                                                    | //                                           | permanent comment                                 | K           |
| [[cmd-work]](./cmd-work.md)                                                   | WORK                                         | earns 10 silver or more                           | L           |
| [ATTACK unit-id](./cmd-attack.md)                               | ATTACK unit-ID                               | attacks the unit                                  | (L)\*       |
| [BANNER "text"](./cmd-banner.md)                                               | BANNER                                       | Sets text for the address list                    | K           |
| [CLAIM anzahl gegenstand](./cmd-claim.md)                     | CLAIM                                        | Fetches items from party pool                     | K           |
| [[cmd-promote]](./cmd-promote.md)                                        | PROMOTE                                      | Promote a unit to heroe                           | K           |
| [STEAL unit-id](./cmd-steal.md)                                        | STEAL unit-ID                                | steal 50 Silver or more                           | L           |
| [NAME UNIT "name"](./cmd-name.md                             | names the specified object                        | K           |
| [NAME PARTEI "name"](./cmd-name.md                          |                                                   | K           |
| [NAME GEBÄUDE "name"](./cmd-name.md                         |                                                   | K           |
| [NAME SCHIFF "name"](./cmd-name.md                             |                                                   | K           |
| [NAME REGION "name"](./cmd-name.md                           |                                                   | K           |
| [NAME FREMDE UNIT unit-id "name"](./cmd-name.md             | names the specified foreign object                | K           |
| [NAME FREMDES SCHIFF ship-id "name"](./cmd-name.md             |                                                   | K           |
| [NAME FREMDES GEBÄUDE building-id "name"](./cmd-name.md     |                                                   | K           |
| [NAME FREMDE PARTEI faction-id "name"](./cmd-name.md       |                                                   | K           |
| [USE \[anzahl\] trank](./cmd-use.md)                                  | USE \[amount\] potion                        | uses alchemical potion                            | K           |
| [DESCRIBE UNIT "text"](./cmd-describe.md                         | describes object                                  | K           |
| [DESCRIBE PRIVAT "text"](./cmd-describe.md                      | unit description for the owner                    | K           |
| [DESCRIBE GEBÄUDE "text"](./cmd-describe.md                     |                                                   | K           |
| [DESCRIBE SCHIFF "text"](./cmd-describe.md                         |                                                   | K           |
| [DESCRIBE REGION "text"](./cmd-describe.md                       |                                                   | K           |
| [ENTER GEBÄUDE building-id](./cmd-enter.md)                                | ENTER BUILDING building-id                   | Enter a building                                  | K           |
| [ENTER SCHIFF ship-id](./cmd-enter.md)                                  | ENTER SHIP ship-id                           | Enter a ship                                      | K           |
| [GUARD \[NOT\]](./cmd-guard.md)                                         | GUARD                                        | guard the region                                  | K           |
| [BEZAHLE NOT \[building-id\]](./cmd-pay-not.md)                              | PAY \[NOT\]                                  | do not pay a maintenance                          | K           |
| [MESSAGE REGION "text"](./cmd-message.md                        | Send a message                                    | K           |
| [MESSAGE SCHIFF ship-id "text"](./cmd-message.md                  | Send a message                                    | K           |
| [MESSAGE GEBÄUDE building-id "text"](./cmd-message.md          | Send a message                                    | K           |
| [MESSAGE UNIT unit id "text"](./cmd-message.md                  | Send a message                                    | K           |
| [MESSAGE PARTEI faction-id "text"](./cmd-message.md            | Send a message                                    | K           |
| [DEFAULT befehl](./cmd-default.md)                                            | DEFAULT                                      | sets the default order for the next turn          | K           |
| [UNIT unit-id](./cmd-unit.md)                                        | UNIT unit-ID                                 | beginning of a unit's orders                      | K           |
| [EMAIL email@adresse](./cmd-email.md)                                           | EMAIL email@adresse                          | sets the e−mail the report is sent to             | K           |
| [[cmd-end]](./cmd-end.md)                                                            | END                                          | ends a MAKE TEMP block                            | K           |
| [ERESSEA faction-id "passwort"](./cmd-eressea.md                | beginning of faction's orders                     | K           |
| [RIDE unit-id](./cmd-ride.md)                                              | RIDE unit-id                                 | be transported by unit−id                         | L           |
| [FOLLOW UNIT unit-id](./cmd-follow.md)                                      | FOLLOW UNIT unit-id                          | follows a unit                                    | (L)\*\*     |
| [FOLLOW SCHIFF ship-id](./cmd-follow.md)                                        | FOLLOW SHIP ship-id                          | follows a ship                                    | (L)\*\*     |
| [RESEARCH KRÄUTER](./cmd-research.md)                                           | RESEARCH herbs                               | search for herbs                                  | L           |
| [GIVE unit-id KRÄUTER](./cmd-give.md)                                            | GIVE unit-id herbs                           | give a unit all herbs                             | K           |
| [GIVE unit-id KOMMANDO](./cmd-give.md)                                           | GIVE unit-id command                         | give a unit ship/ building control                | K           |
| [GIVE unit-id UNIT](./cmd-give.md)                                            | GIVE unit-id UNIT                            | give unit to a foreign faction                    | K           |
| [GIVE unit-id \[JE\] anzahl PERSONEN](./cmd-give.md)                             | GIVE unit-id \[each\] amount MEN             | give a unit men                                   | K           |
| [GIVE unit-id \[JE\] anzahl SCHIFF](./cmd-give.md)                               | GIVE unit-id \[each\] amount SHIP            | give SHIP to form convoys                         | K           |
| [GIVE unit-id \[JE\] anzahl SILBER](./cmd-give.md)                               | GIVE unit-id \[each\] amount SILVER          | give silver                                       | K           |
| [GIVE unit-id \[JE\] anzahl gegenstand](./cmd-give.md)                           | GIVE unit-id \[each\] amount item            | give item                                         | K           |
| [GIVE 0 anzahl SILBER](./cmd-give.md)                                               | GIVE 0 number SILVER                         | throwing away objects                             | K           |
| [GIVE 0 anzahl PERSONEN](./cmd-give.md)                                             | GIVE 0 number MEN                            |                                                   | K           |
| [GIVE 0 anzahl gegenstand](./cmd-give.md)                                           | GIVE 0 number item                           |                                                   | K           |
| [GROUP \["name"\]](./cmd-group.md\]                             | forms groups of units                             | K           |
| [HELP faction-id ALLES \[NOT\]](./cmd-help.md)                               | HELP faction-id ALL \[NOT\]                  | set up/revoke an unilateral alliance              | K           |
| [HELP faction-id GIVE \[NOT\]](./cmd-help.md)                                 | HELP faction-id GIVE \[NOT\]                 |                                                   | K           |
| [HELP faction-id COMBAT \[NOT\]](./cmd-help.md)                              | HELP faction-id COMBAT \[NOT\]               |                                                   | K           |
| [HELP faction-id GUARD \[NOT\]](./cmd-help.md)                             | HELP faction-id GUARD \[NOT\]                |                                                   | K           |
| [HELP faction-id SILBER \[NOT\]](./cmd-help.md)                              | HELP faction-id SILVER \[NOT\]               |                                                   | K           |
| [HELP faction-id PARTEITARNUNG \[NOT\]](./cmd-help.md)                       | HELP faction-id FACTIONSTEALTH \[NOT\]       |                                                   | K           |
| [[cmd-combat]](./cmd-combat.md)                                                 | COMBAT                                       | set the combat behaviour                          | K           |
| [COMBAT AGGRESSIV](./cmd-combat.md)                                       | COMBAT AGGRESSIVE                            |                                                   | K           |
| [COMBAT DEFENSIV](./cmd-combat.md)                                        | COMBAT DEFENSIVE                             |                                                   | K           |
| [COMBAT FLIEHE](./cmd-combat.md)                                          | COMBAT FLEE                                  |                                                   | K           |
| [COMBAT HELP \[NOT\]](./cmd-combat.md)                                 | COMBAT HELP \[NOT\]                          | the unit is \[not\] helped in the fight           | K           |
| [COMBAT REAR](./cmd-combat.md)                                          | COMBAT REAR                                  |                                                   | K           |
| [COMBAT NOT](./cmd-combat.md)                                           | COMBAT NOT                                   |                                                   | K           |
| [COMBATSPELL \[LEVEL n\] "zauberspruch" \[NOT\]](./cmd-combatspell.md \[NOT\]      | set spell for combat                              | K           |
| [BUY anzahl luxusgut](./cmd-buy.md)                                         | BUY amount luxurygood                        | buy luxury item                                   | L\*\*\*     |
| [CONTACT unit-id](./cmd-contact.md)                            | CONTACT unit-no                              | contact foreign unit                              | K           |
| [TEACH unit-id \[unit-id etc.\]](./cmd-teach.md)                          | TEACH unit-no                                | teach units                                       | L           |
| [LEARN talent](./cmd-learn.md)                                                  | LEARN skill                                  | learn a skill                                     | L           |
| [LEARN AUTO talent](./cmd-learn-auto.md)                                   | LEARN AUTO                                   | learn or teach a skill                            | L           |
| [LOCALE en/de](./cmd-locale.md)                                                | LOCALE en/de                                 | no function (only for tools)                      | K           |
| [MAKE TEMP unit-alias-nr \["name"\]](./cmd-make.md\]           | creates a new unit                                | K           |
| [MAKE \[stufe\] gebäude-typ \[building-id\]](./cmd-make.md)                    | MAKE \[level\] building-type \[building-ID\] | erect or extend a building                        | L           |
| [MAKE \[stufe\] SCHIFF \[ship-id\]](./cmd-make.md)                          | MAKE \[level\] SHIP \[ship-ID\]              | extend a ship                                     | L           |
| [[cmd-make]](./cmd-make.md)                                                         | MAKE ??                                      | baue weiter an Gebäude/Schiff ??                  | L           |
| [MAKE \[stufe\] BOOT](./cmd-make.md)                                          | MAKE \[level\] boat                          | build a boat                                      | L           |
| [MAKE \[stufe\] LANGBOOT](./cmd-make.md)                                      | MAKE \[level\] longboat                      | build a longboat                                  | L           |
| [MAKE \[stufe\] DRACHENSCHIFF](./cmd-make.md)                                 | MAKE \[level\] dragonship                    | build a dragonship                                | L           |
| [MAKE \[stufe\] KARAVELLE](./cmd-make.md)                                     | MAKE \[level\] caravel                       |                                                   | L           |
| [MAKE \[stufe\] TRIREME](./cmd-make.md)                                       | MAKE \[level\] trireme                       |                                                   | L           |
| [MAKE \[stufe\] GALEONE](./cmd-make.md)                                       | MAKE \[level\] galleon                       |                                                   | L           |
| [MAKE \[stufe\] STRASSE richtung](./cmd-make.md)                              | MAKE \[level\] ROAD direction                | build road                                        | L           |
| [MAKE \[anzahl\] KRÄUTER](./cmd-make.md)                                      | MAKE \[amount\] HERBS                        | pick herbs in a region                            | L           |
| [MAKE \[anzahl\] trank](./cmd-make.md)                                        | MAKE \[amount\] POTIONS                      | make a potion                                     | L           |
| [MAKE \[anzahl\] gegenstand](./cmd-make.md)                                   | MAKE \[amount\] item                         | make an item                                      | L           |
| [MOVE richtung \[richtung etc.\]](./cmd-move.md)                                 | MOVE direction \[direction\]                 | move unit                                         | L           |
| [[cmd-next]](./cmd-next.md)                                           | NEXT                                         | ends the orders of a faction                      | K           |
| [NUMBER UNIT \[neue\_nr\]](./cmd-number.md)                                 | NUMBER UNIT \[newID\]                        | gives a new id                                    | K           |
| [NUMBER GEBÄUDE \[neue\_nr\]](./cmd-number.md)                                 | NUMBER CASTLE \[newID\]                      |                                                   | K           |
| [NUMBER PARTEI \[neue\_nr\]](./cmd-number.md)                                  | NUMBER FACTION \[newID\]                     |                                                   | K           |
| [NUMBER SCHIFF \[neue\_nr\]](./cmd-number.md)                                  | NUMBER SHIP \[newID\]                        |                                                   | K           |
| [OPTION AUSWERTUNG \[NOT\]](./cmd-option.md)                                 | OPTION                                       | Set / Revoke Options                              | K           |
| [OPTION COMPUTER \[NOT\]](./cmd-option.md)                                   | OPTION                                       |                                                   | K           |
| [OPTION ZIPPED \[NOT\]](./cmd-option.md)                                     | OPTION                                       |                                                   | K           |
| [OPTION BZIP2 \[NOT\]](./cmd-option.md)                                      | OPTION                                       |                                                   | K           |
| [OPTION SILBERPOOL \[NOT\]](./cmd-option.md)                                 | OPTION                                       |                                                   | K           |
| [OPTION MATERIALPOOL \[NOT\]](./cmd-option.md)                               | OPTION                                       |                                                   | K           |
| [OPTION ADRESSEN \[NOT\]](./cmd-option.md)                                   | OPTION                                       |                                                   | K           |
| [OPTION ZUGVORLAGE \[NOT\]](./cmd-option.md)                                 | OPTION                                       |                                                   | K           |
| [OPTION STATISTIK \[NOT\]](./cmd-option.md)                                  | OPTION                                       |                                                   | K           |
| [OPTION TALENTVERSCHIEBUNG \[NOT\]](./cmd-option.md)                         | OPTION                                       |                                                   | K           |
| [OPTION PUNKTE \[NOT\]](./cmd-option.md)                                     | OPTION                                       |                                                   | K           |
| [PASSWORD "neues-passwort"](./cmd-password.md                      | set new password                                  | K           |
| [PLANT \[anzahl\] KRÄUTER](./cmd-plant.md)                                | PLANT \[amount\] HERBS                       | Plant herbs                                       | L           |
| [PLANT \[anzahl\] BÄUME](./cmd-plant.md)                                  | PLANT \[amount\] TREES                       | Plant seeds                                       | L           |
| [PLANT \[anzahl\] MALLORNSAMEN](./cmd-plant.md             | Plant mallorn seeds                               | L           |
| [PLANT \[anzahl\] SAMEN](./cmd-plant.md)                                  | PLANT \[amount\] SEEDS                       | Plant seeds                                       | L           |
| [PIRACY \[partei\_1\] \[partei\_2\] \[...\]](./cmd-piracy.md)         | PIRACY \[faction\_1\] \[faction\_2\]         | Set Piracy                                        | L           |
| [PREFIX \[präfix\]](./cmd-prefix.md)                                      | PREFIX                                       | prepend the race name with a prefix               | K           |
| [REGION x,y](./cmd-region.md)                                                  | REGION x,y                                   | no function (only for tools)                      | K           |
| [RECRUIT anzahl](./cmd-recruit.md)                                   | RECRUIT amount                               | recruit men (persons of your race)                | K           |
| [RESERVE anzahl "gegenstand"](./cmd-reserve.md)                      | RESERVE amount item                          | reserve item                                      | K           |
| [RESERVE anzahl SILBER](./cmd-reserve.md)                            | RESERVE amount silver                        | reserve silver                                    | K           |
| [ROUTE richtung \[richtung etc.\]](./cmd-route.md)                              | ROUTE direction \[direction etc.\]           | Travel                                            | L           |
| [SORT BEFORE unit-id](./cmd-sort.md)                                 | SORT BEFORE unit-id                          | sort unit in report                               | K           |
| [SORT AFTER unit-id](./cmd-sort.md)                              | SORT AFTER unit-id                           |                                                   | K           |
| [SPY unit-id](./cmd-spy.md)                                  | SPY unit-id                                  | spy a unit                                        | L           |
| [LANGUAGE en/de](./cmd-language.md)                                             | LANGUAGE en/de                               | Change Language for orders                        | K           |
| [QUIT "passwort" \[PARTEI faction-id\]](./cmd-quit.md \[FACTION Faction-id\]       | quit the game \[merge with another faction\]      | K           |
| [HIDE \[stufe\]](./cmd-tax.md)                                               | HIDE \[level\]                               | set hide level                                    | K           |
| [HIDE rasse](./cmd-tax.md)                                                   | HIDE \[race\]                                | Demon: disguise as another race                   | K           |
| [HIDE PARTEI \[NOT\]](./cmd-tax.md)         | K           |
| [HIDE PARTEI NUMBER nummer](./cmd-tax.md)                                    | HIDE FACTION faction-ID                      | disguised as another faction                      | K           |
| [CARRY unit-id](./cmd-carry.md)                      | CARRY unit-id                                | transport another unit                            | K           |
| [TAX \[betrag\]](./cmd-tax.md)                                           | TAX \[amount\]                               | tax peasants (max. 20 silver/skill lvl)           | L           |
| [ENTERTAIN \[betrag\]](./cmd-entertain.md)                               | ENTERTAIN \[amount\]                         | earn 20 or more silver (max. 20 silver/skill lvl) | L           |
| [ORIGIN \[x y\]](./cmd-origin.md)                                        | ORIGIN \[x y\]                               | Sets the origin to x,y                            | K           |
| [FORGET talent](./cmd-forget.md)                                            | FORGET skill                                 | forget a skill                                    | K           |
| [SELL anzahl luxusgut](./cmd-sell.md)                                | SELL \[amount\] \[ALL\] good                 | sell luxury goods                                 | (L)\*\*\*\* |
| [[cmd-leave]](./cmd-leave.md)                                                | LEAVE                                        | leave ship or building                            | K           |
| [CAST \[REGION x y\] \[LEVEL n\] "zauberspruch" \[...\]](./cmd-cast.md      | Cast spells                                       | (L)         |
| [SHOW "zauberspruch"](./cmd-show.md)                                          | SHOW                                         | retrieve spell description                        | K           |
| [[cmd-destroy]](./cmd-destroy.md)                                           | DESTROY                                      | building, ship, or road                           | L           |
| [GROW PFERDE](./cmd-grow.md)                                          | GROW HORSES                                  | breed horses, needs a stable                      | L           |
| [GROW KRÄUTER](./cmd-grow.md                              | L           |
| [GROW BÄUME](./cmd-grow.md                      | L           |

\* voir [The aftermath of battle]; \*\*If the tracked unit does not move, another long order can be executed instead; \*\*\*can be combined with SELL; \*\*\*\*can be combined with BUY

## See also

- [Orders]
- [Orders sequence]

Continue reading: [Der erste Zug](./first-round.md)

<!-- From [https://wiki.eressea.de/index.php?title=Diskussion:Kurzbeschreibung/en&oldid=8215] -->

  [Order]: ./commands.md
  [The aftermath of battle]: ./war.md#the-end
  [Orders]: ./commands.md
  [Orders sequence]: ./commands-sequence.md
