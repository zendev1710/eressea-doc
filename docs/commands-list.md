---
# cSpell:locale en
alias: orders-list
---
# List of orders

Under "K/L" it is noted whether the [order] is a short or long order. A unit can only execute one long order per round, but can execute any number of short ones.

[<sup>(l)</sup>] denotes one [[orders|pseudo-long order]], which can be given multiple times to a unit. However, no other long order can be executed. Further information can be found on the respective orders page.

Short list of orders.

| Order                                           | Description                                | K/L     |
|-------------------------------------------------|--------------------------------------------|---------|
| [//]                                            | Lasting comment                            | [S]     |
| [[cmd-work]]                                    | Earns 10 silver or more                    | [L]     |
| [[cmd-attack|`ATTACK <unit id>`]]               | Attacks the unit                           | [(l)] 1 |
| [`BANNER "<text>"`]                             | Sets text for address list                 | [S]     |
| [`CLAIM <number> <item>`]                       | Retrieves items from faction pool          | [S]     |
| [[cmd-promote]]                                 | Turns unity into heroes                    | [S]     |
| [`STEAL <unit id>`]                             | Steals 50 silver or more                   | [L]     |
| [`NAME UNIT "<name>"`]                          | Names objects                              | [S]     |
| [`NAME FACTION "<name>"`]                       |                                            | [S]     |
| [`NAME BUILDING "<name>"`]                      |                                            | [S]     |
| [`NAME SHIP "<name>"`]                          |                                            | [S]     |
| [`NAME REGION "<name>"`]                        |                                            | [S]     |
| [`NAME FREMDE UNIT einheit "<name>"`]           | Names foreign and unnamed objects          | [S]     |
| [`NAME FREMDES SHIP schiff "<name>"`]           |                                            | [S]     |
| [`NAME FREMDES BUILDING gebäude "<name>"`]      |                                            | [S]     |
| [`NAME FREMDE FACTION partei "<name>"`]         |                                            | [S]     |
| [`USE [<number>] trank`]                        | Uses alchemical potion                     | [S]     |
| [`DESCRIBE UNIT "<text>"`]                      | Describes objects                          | [S]     |
| [`DESCRIBE PRIVAT "<text>"`]                    |                                            | [S]     |
| [`DESCRIBE BUILDING "<text>"`]                  |                                            | [S]     |
| [`DESCRIBE SHIP "<text>"`]                      |                                            | [S]     |
| [`DESCRIBE REGION "<text>"`]                    |                                            | [S]     |
| [`ENTER BUILDING <building id>`]                | Enters building                            | [S]     |
| [`ENTER SHIP <ship id>`]                        | Enters ships                               | [S]     |
| [`GUARD [NOT]`]                                 | Guards the region                          | [S]     |
| [`PAY NOT [<building id>]`]                     | Does not pay the maintenance of a building | [S]     |
| [`MESSAGE REGION "<text>"`]                     | Sends messages                             | [S]     |
| [`MESSAGE SHIP <ship id> "<text>"`]             | Sends messages                             | [S]     |
| [`MESSAGE BUILDING <building id> "<text>"`]     | Sends messages                             | [S]     |
| [`MESSAGE UNIT <unit id> "<text>"`]             |                                            | [S]     |
| [`MESSAGE FACTION <faction id> "<text>"`]       |                                            | [S]     |
| [`DEFAULT "Orders"`]                            | Sets default order for the next round      | [S]     |
| [`UNIT <unit id>`]                              | Begins commands for a unit                 | [S]     |
| [`EMAIL email@adresse`]                         | Sets the email address                     | [S]     |
| [[cmd-end]]                                     | Completed MAKE TEMP                        | [S]     |
| [`ERESSEA <faction id> "passwort"`]             | Begins orders for faction                  | [S]     |
| [`RIDE <unit id>`]                              | Can be transported                         | [L]     |
| [`FOLLOW UNIT <unit id>`]                       | Follows a unit                             | [(l)] 2 |
| [`FOLLOW SHIP <ship id>`]                       | Follows a ship                             | [(l)] 2 |
| [`RESEARCH HERBS`]                              | Looking for herbs                          | [L]     |
| [`GIVE <unit id> herb`]                         | Gives a unit all herbs                     | [S]     |
| [`GIVE <unit id> KOMMANDO`]                     | Hands over command of ship/building        | [S]     |
| [`GIVE <unit id> UNIT`]                         | Transfers unit to foreign faction          | [S]     |
| [`GIVE <unit id> [JE] <number> MEN`]        | Hands over people                          | [S]     |
| [`GIVE <unit id> [JE] <number> SHIP`]           | Passes SHIP to form convoys                | [S]     |
| [`GIVE <unit id> [JE] <number> SILVER`]         | Hands over silver                          | [S]     |
| [`GIVE <unit id> [JE] <number> <item>`]         | Hands over items                           | [S]     |
| [`GIVE 0 <number> SILVER`]                      | Gives items to the farmers                 | [S]     |
| [`GIVE 0 <number> MEN`]                     |                                            | [S]     |
| [`GIVE 0 <number> <item>`]                      |                                            | [S]     |
| [`GROUP ["<name>"]`]                            | Grouping units                             | [S]     |
| [`HELP <faction id> ALLES [NOT]`]               | Sets/deletes one-sided alliance            | [S]     |
| [`HELP <faction id> GIVE [NOT]`]                |                                            | [S]     |
| [`HELP <faction id> COMBAT [NOT]`]              |                                            | [S]     |
| [`HELP <faction id> GUARD [NOT]`]               |                                            | [S]     |
| [`HELP <faction id> SILVER [NOT]`]              |                                            | [S]     |
| [`HELP <faction id> PARTEITARNUNG [NOT]`]       |                                            | [S]     |
| [[cmd-combat]]                                  | Sets behavior in combat                    | S       |
| [`COMBAT AGGRESSIVE`]                           |                                            | [S]     |
| [`COMBAT DEFENSIVE`]                            |                                            | [S]     |
| [`COMBAT FLEE`]                                 |                                            | [S]     |
| [`COMBAT HELP [NOT]`]                           | The unit is not helped in battle           | [S]     |
| [`COMBAT REAR`]                                 |                                            | [S]     |
| [`COMBAT NOT`]                                  |                                            | [S]     |
| [`COMBATSPELL [LEVEL n] "zauberspruch" [NOT]`]  | Sets spells for fights                     | [S]     |
| [`BUY <number> luxusgut`]                       | Buy luxury goods                           | [(l)] 3 |
| [`CONTACT <unit id>`]                           | Contact foreign units                      | [S]     |
| [`TEACH <unit id> [<unit id> etc.]`]            | Teach units                                | [L]     |
| [`LEARN <skill>`]                               | Learn skill                                | [L]     |
| [`LEARN AUTO <skill>`]                          | Learning or teaching skill                 | [L]     |
| [`LOCALE en/de`]                                | displays the language of the orders        | [S]     |
| [`MAKE TEMP unit-alias-nr ["<name>"]`]          | Create new unity                           | [S]     |
| [`MAKE [stufe] gebäude-typ [<building id>]`]    | Expand or build new building               | [L]     |
| [`MAKE [stufe] schiffstyp`]                     | Build new ships                            | [L]     |
| [`MAKE [stufe] SHIP [<ship id>]`]               | Continue building the ship                 | [L]     |
| [[cmd-make]]                                    | Continue to build buildings/ships          | [L]     |
| [`MAKE [stufe] STRASSE richtung`]               | Build roads                                | [L]     |
| [`MAKE [<number>] herb`]                        | Look for local herbs                       | [L]     |
| [`MAKE [<number>] trank`]                       | MAKE an alchemical potion                  | [L]     |
| [`MAKE [<number>] <item>`]                      | MAKE an item or mine resources             | [L]     |
| [`MOVE richtung [richtung etc.]`]               | Travel                                     | [L]     |
| [`NEXT`]                                        | Terminates orders                          | [S]     |
| [`NUMBER UNIT [neue\_nr]`]                      | Assigns new id                             | [S]     |
| [`NUMBER BUILDING [neue\_nr]`]                  |                                            | [S]     |
| [`NUMBER FACTION [neue\_nr]`]                   |                                            | [S]     |
| [`NUMBER SHIP [neue\_nr]`]                      |                                            | [S]     |
| [`OPTION AUSWERTUNG [NOT]`]                     | Different settings                         | [S]     |
| [`OPTION COMPUTER [NOT]`]                       |                                            | [S]     |
| [`OPTION ZIPPED [NOT]`]                         |                                            | [S]     |
| [`OPTION BZIP2 [NOT]`]                          |                                            | [S]     |
| [`OPTION SILBERPOOL [NOT]`]                     |                                            | [S]     |
| [`OPTION MATERIALPOOL [NOT]`]                   |                                            | [S]     |
| [`OPTION ADRESSEN [NOT]`]                       |                                            | [S]     |
| [`OPTION ZUGVORLAGE [NOT]`]                     |                                            | [S]     |
| [`OPTION STATISTIK [NOT]`]                      |                                            | [S]     |
| [`OPTION TALENTVERSCHIEBUNG [NOT]`]             |                                            | [S]     |
| [`OPTION PUNKTE [NOT]`]                         |                                            | [S]     |
| [`PASSWORD "neues-passwort"`]                   | Sets new password                          | [S]     |
| [`PLANT [<number>] herb`]                       | Plants herbs                               | [L]     |
| [`PLANT [<number>] BÄUME`]                      | Plants seeds                               | [L]     |
| [`PLANT [<number>] MALLORNSAMEN`]               | Plants seeds                               | [L]     |
| [`PLANT [<number>] SAMEN`]                      | Plants seeds                               | [L]     |
| [`PIRACY [partei\_1] [partei\_2] [...]`]        | Set piracy                                 | [L]     |
| [`PREFIX [präfix]`]                             | Gives the breed name a prefix              | [S]     |
| [`REGION x,y`]                                  | No function (only for tools)               | [S]     |
| [`RECRUIT <number>`]                            | Recruits more people                       | [S]     |
| [`RESERVE <number> "<item>"`]                   | Gegenstände reservieren                    | [S]     |
| [`RESERVE <number> SILVER`]                     | Reserve silver                             | [S]     |
| [`ROUTE richtung [richtung etc.]`]              | Travel                                     | [L]     |
| [`SORT BEFORE <unit id>`]                       | Sort unit in report                        | [S]     |
| [`SORT AFTER <unit id>`]                        |                                            | [S]     |
| [`SPY <unit id>`]                               | Spy unit                                   | [L]     |
| [`LANGUAGE en/de`]                              | changes the language of the faction        | [S]     |
| [`QUIT "passwort" [FACTION <faction id>]`]      | Leave the game                             | [S]     |
| [`HIDE [stufe]`]                                | Set camouflage level                       | [S]     |
| [`HIDE rasse`]                                  | Demons: disguise as another race           | [S]     |
| [`HIDE FACTION [NOT]`]                          | Disguise faction as anonymous              | [S]     |
| [`HIDE FACTION NUMBER <faction id>>`]           | Disguise faction as another faction        | [S]     |
| [`CARRY <unit id>`]                             | Take other units with you                  | [S]     |
| [`TAX [betrag]`]                                | Collect taxes                              | [L]     |
| [`ENTERTAIN [betrag]`]                          | Earned 20 or more silver                   | [L]     |
| [`ORIGIN x y`]                                  | Sets the coordinate origin                 | [S]     |
| [`FORGET <skill>`]                              | Forgets the skill                          | [S]     |
| [`SELL anzah`l luxusgut]                        | Sells luxury goods                         | [(l)] 3 |
| [`SELL ALL luxusgut`]                           |                                            |         |
| [`LEAVE`]                                       | Schiff oder Gebäude verlassen              | [S]     |
| [`CAST [REGION x y] [LEVEL n] "<spell>" [...]`] | Magic                                      | [(l)] 4 |
| [`SHOW ALLE ZAUBER`]                            | Shows description of all known spells      | [S]     |
| [`SHOW ALLE TRÄNKE`]                            | Shows description of all known potions     | [S]     |
| [`SHOW "Gegenstand"`]                           | Shows description of an item               | [S]     |
| [`SHOW "<potion>"`]                             | Shows description of the potion            | [S]     |
| [`SHOW "<spell>"`]                              | Shows description of the spell             | [S]     |
| [`SHOW "<race>"`]                               | Shows description of the unit's race       | [S]     |
| [`DESTROY [stufen]`]                            | Reduce the size of a building or ship      | [L]     |
| [`DESTROY [stufen]`] STREET direction           | Tear down the road                         | [L]     |
| [`GROW PFERDE`]                                 | Breed horses - only in horse breeding      | L       |

<!-- [//]: ./cmd-comment-slash.md-->
[S]: ./commands.md#short-and-long-orders
[L]: ./commands.md#short-and-long-orders
<!--[`ATTACK <unit id>`]: ./cmd-attack.md-->
[(l)]: ./commands.md#short-and-long-orders
[`BANNER "<text>"`]: ./cmd-banner.md
[`CLAIM <number> <item>`]: ./cmd-claim.md
[`STEAL <unit id>`]: ./camouflage.md
[`NAME UNIT "<name>"`]: ./cmd-name.md
[`NAME FACTION "<name>"`]: ./cmd-name.md
[`NAME BUILDING "<name>"`]: ./cmd-name.md
[`NAME SHIP "<name>"`]: ./cmd-name.md
[`NAME REGION "<name>"`]: ./cmd-name.md
[`NAME FREMDE UNIT einheit "<name>"`]: ./cmd-name.md
[`NAME FREMDES SHIP schiff "<name>"`]: ./cmd-name.md
[`NAME FREMDES BUILDING gebäude "<name>"`]: ./cmd-name.md
[`NAME FREMDE FACTION partei "<name>"`]: ./cmd-name.md
[`USE [<number>] trank`]: ./cmd-use.md
[`DESCRIBE UNIT "<text>"`]: ./cmd-describe.md
[`DESCRIBE PRIVAT "<text>"`]: ./cmd-describe.md
[`DESCRIBE BUILDING "<text>"`]: ./cmd-describe.md
[`DESCRIBE SHIP "<text>"`]: ./cmd-]describe.md
[`DESCRIBE REGION "<text>"`]: ./cmd-describe.md
[`ENTER BUILDING <building id>`]: ./cmd-enter.md
[`ENTER SHIP <ship id>`]: ./cmd-enter.md
[`GUARD [NOT]`]: ./cmd-guard.md
[`PAY NOT [<building id>]`]: ./cmd-pay-not.md
[`MESSAGE REGION "<text>"`]: ./cmd-message.md
[`MESSAGE SHIP <ship id> "<text>"`]: ./cmd-message.md
[`MESSAGE BUILDING <building id> "<text>"`]: ./cmd-message.md
[`MESSAGE UNIT <unit id> "<text>"`]: ./cmd-message.md
[`MESSAGE FACTION <faction id> "<text>"`]: ./cmd-message.md
[`DEFAULT "Orders"`]: ./cmd-default.md
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
[`GIVE <unit id> [JE] <number> MEN`]: ./cmd-give.md
[`GIVE <unit id> [JE] <number> SHIP`]: ./cmd-give.md
[`GIVE <unit id> [JE] <number> SILVER`]: ./cmd-give.md
[`GIVE <unit id> [JE] <number> <item>`]: ./cmd-give.md
[`GIVE 0 <number> SILVER`]: ./cmd-give.md
[`GIVE 0 <number> MEN`]: ./cmd-give.md
[`GIVE 0 <number> <item>`]: ./cmd-give.md
[`GROUP ["<name>"]`]: ./cmd-group.md
[`HELP <faction id> ALLES [NOT]`]: ./cmd-help.md
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
[`BUY <number> luxusgut`]: ./cmd-buy.md
[`CONTACT <unit id>`]: ./cmd-contact.md
[`TEACH <unit id> [<unit id> etc.]`]: ./cmd-teach.md
[`LEARN <skill>`]: ./cmd-learn.md
[`LEARN AUTO <skill>`]: ./cmd-learn-auto.md
[`LOCALE en/de`]: ./cmd-locale.md
[`MAKE TEMP unit-alias-nr ["<name>"]`]: ./cmd-make.md
[`MAKE [stufe] gebäude-typ [<building id>]`]: ./cmd-make.md
[`MAKE [stufe] schiffstyp`]: ./cmd-make.md
[`MAKE [stufe] SHIP [<ship id>]`]: ./cmd-make.md
[`MAKE`]: ./cmd-make.md
[`MAKE [stufe] STRASSE richtung`]: ./cmd-make.md
[`MAKE [<number>] <herb>`]: ./cmd-make.md
[`MAKE [<number>] trank`]: ./cmd-make.md
[`MAKE [<number>] <item>`]: ./cmd-make.md
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
[`PLANT [<number>] herb`]: ./cmd-plant.md
[`PLANT [<number>] BÄUME`]: ./cmd-plant.md
[`PLANT [<number>] MALLORNSAMEN`]: ./cmd-plant.md
[`PLANT [<number>] SAMEN`]: ./cmd-plant.md
[`PIRACY [partei\_1] [partei\_2] [...]`]: ./cmd-piracy.md
[`PREFIX [präfix]`]: ./cmd-prefix.md
[`REGION x,y`]: ./cmd-region.md
[`RECRUIT <number>`]: ./silver.md#recruter
[`RESERVE <number> "<item>"`]: ./cmd-reserve.md
[`RESERVE <number> SILVER`]: ./cmd-reserve.md
[`ROUTE richtung [richtung etc.]`]: ./cmd-route.md
[`SORT BEFORE <unit id>`]: ./cmd-sort.md
[`SORT AFTER <unit id>`]: ./cmd-sort.md
[`SPY <unit id>`]: ./cmd-spy.md
[`LANGUAGE en/de`]: ./cmd-language.md
[`QUIT <passwort> [FACTION <faction id>]`]: ./cmd-quit.md
[`HIDE [stufe]`]: ./cmd-hide.md
[`HIDE rasse`]: ./cmd-hide.md
[`HIDE FACTION [NOT]`]: ./cmd-hide.md
[`HIDE FACTION NUMBER nummer`]: ./cmd-hide.md
[`CARRY <unit id>`]: ./cmd-carry.md
[`TAX [betrag]`]: ./cmd-tax.md
[`ENTERTAIN [betrag]`]: ./cmd-entertain.md
[`ORIGIN x y`]: ./cmd-origin.md
[`FORGET <skill>`]: ./cmd-forget.md
[`SELL <number> luxusgut`]: ./cmd-sell.md
[`SELL ALLES luxusgut`]: ./cmd-sell.md
[`LEAVE`]: ./cmd-leave.md
[`CAST [REGION x y] [LEVEL n] "zauberspruch" [...]`]: ./cmd-cast.md
[`SHOW ALLE ZAUBER`]: ./cmd-show.md
[`SHOW ALLE TRÄNKE`]: ./cmd-show.md
[`SHOW "Gegenstand"`]: ./cmd-show.md
[`SHOW "Trank"`]: ./cmd-show.md
[`SHOW "Zauberspruch"`]: ./cmd-show.md
[`SHOW "Rasse"`]: ./cmd-show.md
[`DESTROY [stufen]`]: ./cmd-destroy.md
[`GROW PFERDE`]: ./cmd-grow.md

<sup>1</sup> the order is not always long, see [The end of the battle]  
<sup>2</sup> if the tracked unit does not move, another long order can be executed instead  
<sup>3</sup> a BUY and several SELL commands can be combined  
<sup>4</sup> a unit can cast multiple spells

## See also

- [[orders]]
- [[orders-sequence]]

Continue reading: [[first-round]].

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[<sup>(l)</sup>]: ./commands.md#short-and-long-orders
[The end of the battle]: ./war.md#the-end
