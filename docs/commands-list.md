---
# cSpell:locale en
alias: orders-list
---
# List of orders

Under `S`/`L` it is noted whether the [[orders|order]] is a Short or Long order.  
A unit can only execute one long order per round, but can execute any number of short ones.  

`PL` denotes one [[orders|Pseudo-Long order]], which can be given multiple times to a unit.  
However, no other long order can be executed.  

More information: [[orders]].  

<!-- A link containing brackets (e.g. [BEWACHE  &#91;NICHT&#93;) cannot be used as a reference link -->
<!-- instead, replace by HTML escape codes (e.g. [BEWACHE &#91;[NICHT&#93;) or use inline link [...](<link>) -->

| Order                                                                      | Description                                | S/L    |
|----------------------------------------------------------------------------|--------------------------------------------|--------|
| [//]                                                                       | Lasting comment                            | S      |
| [ATTACK &lt;unit id&gt;]                                                   | Attacks the unit                           | PL[^1] |
| [BANNER "&lt;text&gt;"]                                                    | Sets text for address list                 | S      |
| [BUY &lt;number&gt; &lt;luxury item&gt;]                                   | Buy luxury goods                           | PL[^3] |
| [CARRY &lt;unit id&gt;]                                                    | Take other units with you                  | S      |
| [CAST &#91;REGION x y&#93; &#91;LEVEL n&#93; "&lt;spell&gt;"...]           | Magic                                      | PL[^4] |
| [CLAIM &lt;number&gt; &lt;item&gt;]                                        | Retrieves items from faction pool          | S      |
| [[cmd-combat]]                                                             | Sets behavior in combat                    | S      |
| [COMBAT AGGRESSIVE]                                                        |                                            | S      |
| [COMBAT DEFENSIVE]                                                         |                                            | S      |
| [COMBAT FLEE]                                                              |                                            | S      |
| [COMBAT HELP &#91;NOT&#93;]                                                | The unit is not helped in battle           | S      |
| [COMBAT NOT]                                                               |                                            | S      |
| [COMBAT REAR]                                                              |                                            | S      |
| [COMBATSPELL &#91;LEVEL n&#93; "zauberspruch" &#91;NOT&#93;]               | Sets spells for fights                     | S      |
| [CONTACT &lt;unit id&gt;]                                                  | Contact foreign units                      | S      |
| [DEFAULT "Orders"]                                                         | Sets default order for the next round      | S      |
| [DESCRIBE BUILDING "&lt;text&gt;"]                                         |                                            | S      |
| [DESCRIBE PRIVATE "&lt;text&gt;"]                                          |                                            | S      |
| [DESCRIBE REGION "&lt;text&gt;"]                                           |                                            | S      |
| [DESCRIBE SHIP "&lt;text&gt;"]                                             |                                            | S      |
| [DESCRIBE UNIT "&lt;text&gt;"]                                             | Describes objects                          | S      |
| [DESTROY &#91;level&#93;]                                                  | Reduce the size of a building or ship      | L      |
| [DESTROY &#91;level&#93; STREET direction]                                 | Tear down the road                         | L      |
| [EMAIL email@adresse]                                                      | Sets the email address                     | S      |
| [[cmd-end]]                                                                | Completed MAKE TEMP                        | S      |
| [ENTER BUILDING &lt;building id&gt;]                                       | Enters building                            | S      |
| [ENTER SHIP &lt;ship id&gt;]                                               | Enters ships                               | S      |
| [ENTERTAIN &#91;amount&#93;]                                               | Earned 20 or more silver                   | L      |
| [ERESSEA &lt;faction id&gt; "password"]                                    | Begins orders for faction                  | S      |
| [FOLLOW SHIP &lt;ship id&gt;]                                              | Follows a ship                             | PL[^2] |
| [FOLLOW UNIT &lt;unit id&gt;]                                              | Follows a unit                             | PL[^2] |
| [FORGET &lt;skill&gt;]                                                     | Forgets the skill                          | S      |
| [GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; &lt;item&gt;]          | Hands over items                           | S      |
| [GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; MEN]                   | Hands over people                          | S      |
| [GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; SHIP]                  | Passes SHIP to form convoys                | S      |
| [GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; SILVER]                | Hands over silver                          | S      |
| [GIVE &lt;unit id&gt; herb]                                                | Gives a unit all herbs                     | S      |
| [GIVE &lt;unit id&gt; COMMAND]                                             | Hands over command of ship/building        | S      |
| [GIVE &lt;unit id&gt; UNIT]                                                | Transfers unit to foreign faction          | S      |
| [GIVE 0 &lt;number&gt; &lt;item&gt;]                                       |                                            | S      |
| [GIVE 0 &lt;number&gt; MEN]                                                |                                            | S      |
| [GIVE 0 &lt;number&gt; SILVER]                                             | Gives items to the farmers                 | S      |
| [GROUP &#91;"&lt;name&gt;"&#93;]                                           | Grouping units                             | S      |
| [GROW HORSES]                                                              | Breed horses - only in horse breeding      | L      |
| [GUARD &#91;NOT&#93;]                                                      | Guards the region                          | S      |
| [HELP &lt;faction id&gt; ALL &#91;NOT&#93;]                                | Sets/deletes one-sided alliance            | S      |
| [HELP &lt;faction id&gt; COMBAT &#91;NOT&#93;]                             |                                            | S      |
| [HELP &lt;faction id&gt; GIVE &#91;NOT&#93;]                               |                                            | S      |
| [HELP &lt;faction id&gt; GUARD &#91;NOT&#93;]                              |                                            | S      |
| [HELP &lt;faction id&gt; PARTEITARNUNG &#91;NOT&#93;]                      |                                            | S      |
| [HELP &lt;faction id&gt; SILVER &#91;NOT&#93;]                             |                                            | S      |
| [HIDE &#91;level&#93;]                                                     | Set camouflage level                       | S      |
| [HIDE FACTION &#91;NOT&#93;]                                               | Disguise faction as anonymous              | S      |
| [HIDE FACTION NUMBER &lt;faction id&gt;]                                   | Disguise faction as another faction        | S      |
| [HIDE race]                                                                | Demons: disguise as another race           | S      |
| [LANGUAGE en/de]                                                           | changes the language of the faction        | S      |
| [LEARN &lt;skill&gt;]                                                      | Learn skill                                | L      |
| [LEARN AUTO &lt;skill&gt;]                                                 | Learning or teaching skill                 | L      |
| [[cmd-leave]]                                                              | Schiff oder Gebäude verlassen              | S      |
| [LOCALE en/de]                                                             | displays the language of the orders        | S      |
| [[cmd-make]]                                                               | Continue to build buildings/ships          | L      |
| [MAKE &#91;&lt;amount&gt;&#93; &lt;item&gt;]                               | MAKE an item or mine resources             | L      |
| [MAKE &#91;&lt;amount&gt;&#93; &lt;HERBS&gt;]                              | Look for local herbs                       | L      |
| [MAKE &#91;&lt;amount&gt;&#93; potion]                                     | MAKE an alchemical potion                  | L      |
| [MAKE &#91;level&#93; &lt;building type&gt; &#91;&lt;building id&gt;&#93;] | Expand or build new building               | L      |
| [MAKE &#91;level&#93; &lt;ship-type&gt;]                                   | Build new ships                            | L      |
| [MAKE &#91;level&#93; SHIP &#91;&lt;ship id&gt;&#93;]                      | Continue building the ship                 | L      |
| [MAKE &#91;level&#93; STREET direction]                                    | Build roads                                | L      |
| [MAKE TEMP unit-alias-id &#91;"&lt;name&gt;"&#93;]                         | Create new unity                           | S      |
| [MESSAGE BUILDING &lt;building id&gt; "&lt;text&gt;"]                      | Sends messages                             | S      |
| [MESSAGE FACTION &lt;faction id&gt; "&lt;text&gt;"]                        |                                            | S      |
| [MESSAGE REGION "&lt;text&gt;"]                                            | Sends messages                             | S      |
| [MESSAGE SHIP &lt;ship id&gt; "&lt;text&gt;"]                              | Sends messages                             | S      |
| [MESSAGE UNIT &lt;unit id&gt; "&lt;text&gt;"]                              |                                            | S      |
| [MOVE direction &#91;direction&#93;...]                                    | Travel                                     | L      |
| [NAME BUILDING "&lt;name&gt;"]                                             |                                            | S      |
| [NAME FACTION "&lt;name&gt;"]                                              |                                            | S      |
| [NAME STRANGERS FACTION &lt;faction id&gt; "&lt;name&gt;"]                 |                                            | S      |
| [NAME STRANGERS UNIT &lt;unit id&gt; "&lt;name&gt;"]                       | Names foreign and unnamed objects          | S      |
| [NAME STRANGER BUILDING building "&lt;name&gt;"]                           |                                            | S      |
| [NAME STRANGER SHIP &lt;ship id&gt; "&lt;name&gt;"]                        |                                            | S      |
| [NAME REGION "&lt;name&gt;"]                                               |                                            | S      |
| [NAME SHIP "&lt;name&gt;"]                                                 |                                            | S      |
| [NAME UNIT "&lt;name&gt;"]                                                 | Names objects                              | S      |
| [[cmd-next]]                                                               | Terminates orders                          | S      |
| [NUMBER BUILDING &#91;neue-nr&#93;]                                        |                                            | S      |
| [NUMBER FACTION &#91;neue-nr&#93;]                                         |                                            | S      |
| [NUMBER SHIP &#91;neue-nr&#93;]                                            |                                            | S      |
| [NUMBER UNIT &#91;neue-nr&#93;]                                            | Assigns new id                             | S      |
| [OPTION ADRESSEN &#91;NOT&#93;]                                            |                                            | S      |
| [OPTION AUSWERTUNG &#91;NOT&#93;]                                          | Different settings                         | S      |
| [OPTION BZIP2 &#91;NOT&#93;]                                               |                                            | S      |
| [OPTION COMPUTER &#91;NOT&#93;]                                            |                                            | S      |
| [OPTION MATERIALPOOL &#91;NOT&#93;]                                        |                                            | S      |
| [OPTION PUNKTE &#91;NOT&#93;]                                              |                                            | S      |
| [OPTION SILBERPOOL &#91;NOT&#93;]                                          |                                            | S      |
| [OPTION STATISTIK &#91;NOT&#93;]                                           |                                            | S      |
| [OPTION TALENTVERSCHIEBUNG &#91;NOT&#93;]                                  |                                            | S      |
| [OPTION ZIPPED &#91;NOT&#93;]                                              |                                            | S      |
| [OPTION ZUGVORLAGE &#91;NOT&#93;]                                          |                                            | S      |
| [ORIGIN x y]                                                               | Sets the coordinate origin                 | S      |
| [PASSWORD "neues-password"]                                                | Sets new password                          | S      |
| [PAY NOT &#91;&lt;building id&gt;&#93;]                                    | Does not pay the maintenance of a building | S      |
| [PIRACY &#91;faction 1&#93; &#91;faction 2&#93;...]                        | Set piracy                                 | L      |
| [PLANT &#91;&lt;number&gt;&#93; TREES]                                     | Plants seeds                               | L      |
| [PLANT &#91;&lt;number&gt;&#93; herb]                                      | Plants herbs                               | L      |
| [PLANT &#91;&lt;number&gt;&#93; MALLORNSEEDS]                              | Plants seeds                               | L      |
| [PLANT &#91;&lt;number&gt;&#93; SEEDS]                                     | Plants seeds                               | L      |
| [PREFIX &#91;prefix&#93;]                                                  | Gives the breed name a prefix              | S      |
| [[cmd-promote]]                                                            | Turns unity into heroes                    | S      |
| [QUIT "&lt;password&gt;" &#91;FACTION &lt;faction id&gt;&#93;]             | Leave the game                             | S      |
| [RECRUIT &lt;number&gt;]                                                   | Recruits more people                       | S      |
| [REGION x,y]                                                               | No function (only for tools)               | S      |
| [RESEARCH HERBS]                                                           | Looking for herbs                          | L      |
| [RESERVE &lt;number&gt; "&lt;item&gt;"]                                    | Gegenstände reservieren                    | S      |
| [RESERVE &lt;number&gt; SILVER]                                            | Reserve silver                             | S      |
| [RIDE &lt;unit id&gt;]                                                     | Can be transported                         | L      |
| [ROUTE direction &#91;direction&#93;...]                                   | Travel                                     | L      |
| [SELL ALL &lt;luxury item&gt;]                                             |                                            |        |
| [SELL &lt;amount&gt; &lt;luxury item&gt;]                                  | Sells luxury goods                         | PL[^3] |
| [SHOW "&lt;potion&gt;"]                                                    | Shows description of the potion            | S      |
| [SHOW "&lt;race&gt;"]                                                      | Shows description of the unit's race       | S      |
| [SHOW "&lt;spell&gt;"]                                                     | Shows description of the spell             | S      |
| [SHOW "&lt;item&gt;"]                                                      | Shows description of an item               | S      |
| [SHOW ALL POTIONS]                                                         | Shows description of all known potions     | S      |
| [SHOW ALL SPELLS]                                                          | Shows description of all known spells      | S      |
| [SORT AFTER &lt;unit id&gt;]                                               |                                            | S      |
| [SORT BEFORE &lt;unit id&gt;]                                              | Sort unit in report                        | S      |
| [SPY &lt;unit id&gt;]                                                      | Spy unit                                   | L      |
| [STEAL &lt;unit id&gt;]                                                    | Steals 50 silver or more                   | L      |
| [TAX &#91;amount&#93;]                                                     | Collect taxes                              | L      |
| [TEACH &lt;unit id&gt; &#91;&lt;unit id&gt;&#93;...]                       | Teach units                                | L      |
| [UNIT &lt;unit id&gt;]                                                     | Begins orders for a unit                   | S      |
| [USE  &#91;&lt;number&gt;&#93; potion]                                     | Uses alchemical potion                     | S      |
| [[cmd-work]]                                                               | Earns 10 silver or more                    | L      |

[^1]: the order is not always long, see [The end of the battle]
[^2]: if the tracked unit does not move, another long order can be executed instead
[^3]: a `BUY` and several `SELL` orders can be combined
[^4]: a unit can cast multiple spells

## See also

- [[orders]]
- [[orders-sequence]]

Continue reading: [[first-round]].

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[//]: ./cmd-comment-slash.md

[ATTACK &lt;unit id&gt;]: ./cmd-attack.md
[BANNER "&lt;text&gt;"]: ./cmd-banner.md
[BUY &lt;number&gt; &lt;luxury item&gt;]: ./cmd-buy.md
[CARRY &lt;unit id&gt;]: ./cmd-carry.md
[CAST &#91;REGION x y&#93; &#91;LEVEL n&#93; "&lt;spell&gt;"...]: ./cmd-cast.md
[CLAIM &lt;number&gt; &lt;item&gt;]: ./cmd-claim.md
[COMBAT AGGRESSIVE]: ./cmd-combat.md
[COMBAT DEFENSIVE]: ./cmd-combat.md
[COMBAT FLEE]: ./cmd-combat.md
[COMBAT HELP &#91;NOT&#93;]: ./cmd-combat.md
[COMBAT NOT]: ./cmd-combat.md
[COMBAT REAR]: ./cmd-combat.md
[COMBATSPELL &#91;LEVEL n&#93; "zauberspruch" &#91;NOT&#93;]: ./cmd-combatspell.md
[CONTACT &lt;unit id&gt;]: ./cmd-contact.md
[DEFAULT "Orders"]: ./cmd-default.md
[DESCRIBE BUILDING "&lt;text&gt;"]: ./cmd-describe.md
[DESCRIBE PRIVATE "&lt;text&gt;"]: ./cmd-describe.md
[DESCRIBE REGION "&lt;text&gt;"]: ./cmd-describe.md
[DESCRIBE SHIP "&lt;text&gt;"]: ./cmd-describe.md
[DESCRIBE UNIT "&lt;text&gt;"]: ./cmd-describe.md
[DESTROY &#91;level&#93;]: ./cmd-destroy.md
[DESTROY &#91;level&#93; STREET direction]: ./cmd-destroy.md
[EMAIL email@adresse]: ./cmd-email.md
[ENTER BUILDING &lt;building id&gt;]: ./cmd-enter.md
[ENTER SHIP &lt;ship id&gt;]: ./cmd-enter.md
[ENTERTAIN &#91;amount&#93;]: ./cmd-entertain.md
[ERESSEA &lt;faction id&gt; "password"]: ./cmd-eressea.md
[FOLLOW SHIP &lt;ship id&gt;]: ./cmd-follow.md
[FOLLOW UNIT &lt;unit id&gt;]: ./cmd-follow.md
[FORGET &lt;skill&gt;]: ./cmd-forget.md
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; &lt;item&gt;]: ./cmd-give.md
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; MEN]: ./cmd-give.md
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; SHIP]: ./cmd-give.md
[GIVE &lt;unit id&gt; &#91;EACH&#93; &lt;number&gt; SILVER]: ./cmd-give.md
[GIVE &lt;unit id&gt; COMMAND]: ./cmd-give.md
[GIVE &lt;unit id&gt; UNIT]: ./cmd-give.md
[GIVE &lt;unit id&gt; herb]: ./cmd-give.md
[GIVE 0 &lt;number&gt; &lt;item&gt;]: ./cmd-give.md
[GIVE 0 &lt;number&gt; MEN]: ./cmd-give.md
[GIVE 0 &lt;number&gt; SILVER]: ./cmd-give.md
[GROUP &#91;"&lt;name&gt;"&#93;]: ./cmd-group.md
[GROW HORSES]: ./cmd-grow.md
[GUARD &#91;NOT&#93;]: ./cmd-guard.md
[HELP &lt;faction id&gt; ALL &#91;NOT&#93;]: ./cmd-help.md
[HELP &lt;faction id&gt; COMBAT &#91;NOT&#93;]: ./cmd-help.md
[HELP &lt;faction id&gt; GIVE &#91;NOT&#93;]: ./cmd-help.md
[HELP &lt;faction id&gt; GUARD &#91;NOT&#93;]: ./cmd-help.md
[HELP &lt;faction id&gt; PARTEITARNUNG &#91;NOT&#93;]: ./cmd-help.md
[HELP &lt;faction id&gt; SILVER &#91;NOT&#93;]: ./cmd-help.md
[HIDE &#91;level&#93;]: ./cmd-hide.md
[HIDE FACTION &#91;NOT&#93;]: ./cmd-hide.md
[HIDE FACTION NUMBER &lt;faction id&gt;]: ./cmd-hide.md
[HIDE race]: ./cmd-hide.md
[LANGUAGE en/de]: ./cmd-language.md
[LEARN &lt;skill&gt;]: ./cmd-learn.md
[LEARN AUTO &lt;skill&gt;]: ./cmd-learn-auto.md
[LOCALE en/de]: ./cmd-locale.md
[MAKE &#91;&lt;amount&gt;&#93; &lt;HERBS&gt;]: ./cmd-make.md
[MAKE &#91;&lt;amount&gt;&#93; &lt;item&gt;]: ./cmd-make.md
[MAKE &#91;&lt;amount&gt;&#93; Potion]: ./cmd-make.md
[MAKE &#91;level&#93; &lt;building type&gt; &#91;&lt;building id&gt;&#93;]: ./cmd-make.md
[MAKE &#91;level&#93; &lt;ship-type&gt;]: ./cmd-make.md
[MAKE &#91;level&#93; SHIP &#91;&lt;ship id&gt;&#93;]: ./cmd-make.md
[MAKE &#91;level&#93; STREET direction]: ./cmd-make.md
[MAKE TEMP unit-alias-id &#91;"&lt;name&gt;"&#93;]: ./cmd-make.md
[MESSAGE BUILDING &lt;building id&gt; "&lt;text&gt;"]: ./cmd-message.md
[MESSAGE FACTION &lt;faction id&gt; "&lt;text&gt;"]: ./cmd-message.md
[MESSAGE REGION "&lt;text&gt;"]: ./cmd-message.md
[MESSAGE SHIP &lt;ship id&gt; "&lt;text&gt;"]: ./cmd-message.md
[MESSAGE UNIT &lt;unit id&gt; "&lt;text&gt;"]: ./cmd-message.md
[MOVE direction &#91;direction&#93;...]: ./cmd-move.md
[NAME BUILDING "&lt;name&gt;"]: ./cmd-name.md
[NAME FACTION "&lt;name&gt;"]: ./cmd-name.md
[NAME REGION "&lt;name&gt;"]: ./cmd-name.md
[NAME SHIP "&lt;name&gt;"]: ./cmd-name.md
[NAME STRANGER BUILDING building "&lt;name&gt;"]: ./cmd-name.md
[NAME STRANGER SHIP &lt;ship id&gt; "&lt;name&gt;"]: ./cmd-name.md
[NAME STRANGERS FACTION &lt;faction id&gt; "&lt;name&gt;"]: ./cmd-name.md
[NAME STRANGERS UNIT &lt;unit id&gt; "&lt;name&gt;"]: ./cmd-name.md
[NAME UNIT "&lt;name&gt;"]: ./cmd-name.md
[NUMBER BUILDING &#91;neue-nr&#93;]: ./cmd-number.md
[NUMBER FACTION &#91;neue-nr&#93;]: ./cmd-number.md
[NUMBER SHIP &#91;neue-nr&#93;]: ./cmd-number.md
[NUMBER UNIT &#91;neue-nr&#93;]: ./cmd-number.md
[OPTION ADRESSEN &#91;NOT&#93;]: ./cmd-option.md
[OPTION AUSWERTUNG &#91;NOT&#93;]: ./cmd-option.md
[OPTION BZIP2 &#91;NOT&#93;]: ./cmd-option.md
[OPTION COMPUTER &#91;NOT&#93;]: ./cmd-option.md
[OPTION MATERIALPOOL &#91;NOT&#93;]: ./cmd-option.md
[OPTION PUNKTE &#91;NOT&#93;]: ./cmd-option.md
[OPTION SILBERPOOL &#91;NOT&#93;]: ./cmd-option.md
[OPTION STATISTIK &#91;NOT&#93;]: ./cmd-option.md
[OPTION TALENTVERSCHIEBUNG &#91;NOT&#93;]: ./cmd-option.md
[OPTION ZIPPED &#91;NOT&#93;]: ./cmd-option.md
[OPTION ZUGVORLAGE &#91;NOT&#93;]: ./cmd-option.md
[ORIGIN x y]: ./cmd-origin.md
[PASSWORD "neues-password"]: ./cmd-password.md
[PAY NOT &#91;&lt;building id&gt;&#93;]: ./cmd-pay-not.md
[PIRACY &#91;faction 1&#93; &#91;faction 2&#93;...]: ./cmd-piracy.md
[PLANT &#91;&lt;number&gt;&#93; MALLORNSEEDS]: ./cmd-plant.md
[PLANT &#91;&lt;number&gt;&#93; SEEDS]: ./cmd-plant.md
[PLANT &#91;&lt;number&gt;&#93; TREES]: ./cmd-plant.md
[PLANT &#91;&lt;number&gt;&#93; herb]: ./cmd-plant.md
[PREFIX &#91;prefix&#93;]: ./cmd-prefix.md
[QUIT "&lt;password&gt;" &#91;FACTION &lt;faction id&gt;&#93;]: ./cmd-quit.md
[RECRUIT &lt;number&gt;]: ./silver.md#recruiting
[REGION x,y]: ./cmd-region.md
[RESEARCH HERBS]: ./cmd-research.md
[RESERVE &lt;number&gt; "&lt;item&gt;"]: ./cmd-reserve.md
[RESERVE &lt;number&gt; SILVER]: ./cmd-reserve.md
[RIDE &lt;unit id&gt;]: ./cmd-ride.md
[ROUTE direction &#91;direction&#93;...]: ./cmd-route.md
[SELL &lt;amount&gt; &lt;luxury item&gt;]: ./cmd-sell.md
[SELL ALL &lt;luxury item&gt;]: ./cmd-sell.md
[SHOW "&lt;item&gt;"]: ./cmd-show.md
[SHOW "&lt;potion&gt;"]: ./cmd-show.md
[SHOW "&lt;race&gt;"]: ./cmd-show.md
[SHOW "&lt;spell&gt;"]: ./cmd-show.md
[SHOW ALL POTIONS]: ./cmd-show.md
[SHOW ALL SPELLS]: ./cmd-show.md
[SORT AFTER &lt;unit id&gt;]: ./cmd-sort.md
[SORT BEFORE &lt;unit id&gt;]: ./cmd-sort.md
[SPY &lt;unit id&gt;]: ./cmd-spy.md
[STEAL &lt;unit id&gt;]: ./camouflage.md
[TAX &#91;amount&#93;]: ./cmd-tax.md
[TEACH &lt;unit id&gt; &#91;&lt;unit id&gt;&#93;...]: ./cmd-teach.md
[UNIT &lt;unit id&gt;]: ./cmd-unit.md
[USE &#91;&lt;number&gt;&#93; potion]: ./cmd-use.md
[The end of the battle]: ./war.md#the-end
