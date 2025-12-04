# Discussion:Short description

Under "K/L" it is noted whether the [Order] is a short or long order, i.e. whether it is executed immediately (and further orders are possible afterwards) or takes a whole round to execute. K is a short order, L is a long order.

\(L\) denotes a pseudo-long [Order] that can be given to a unit multiple times. However, no other long order can be executed.

brief description of orders

| Befehl (Deutsch)                                                                | Order (English)                              | Beschreibung                                      | K/L         |
|---------------------------------------------------------------------------------|----------------------------------------------|---------------------------------------------------|-------------|
| [//](/KOMMENTAR "KOMMENTAR")                                                    | //                                           | permanent comment                                 | K           |
| [ARBEITE](/ARBEITE "ARBEITE")                                                   | WORK                                         | earns 10 silver or more                           | L           |
| [ATTACKIERE einheit-nr](/ATTACKIERE "ATTACKIERE")                               | ATTACK unit-ID                               | attacks the unit                                  | (L)\*       |
| [BANNER "text"](/BANNER "BANNER")                                               | BANNER                                       | Sets text for the address list                    | K           |
| [BEANSPRUCHE anzahl gegenstand](/BEANSPRUCHE "BEANSPRUCHE")                     | CLAIM                                        | Fetches items from party pool                     | K           |
| [BEFÖRDERE](/BEF%C3%96RDERE "BEFÖRDERE")                                        | PROMOTE                                      | Promote a unit to heroe                           | K           |
| [BEKLAUE einheit-nr](/BEKLAUE "BEKLAUE")                                        | STEAL unit-ID                                | steal 50 Silver or more                           | L           |
| [BENENNE EINHEIT "name"](/BENENNE "BENENNE")                                    | NAME UNIT "name"                             | names the specified object                        | K           |
| [BENENNE PARTEI "name"](/BENENNE "BENENNE")                                     | NAME FACTION "name"                          |                                                   | K           |
| [BENENNE GEBÄUDE "name"](/BENENNE "BENENNE")                                    | NAME BUILDING "name"                         |                                                   | K           |
| [BENENNE SCHIFF "name"](/BENENNE "BENENNE")                                     | NAME SHIP "name"                             |                                                   | K           |
| [BENENNE REGION "name"](/BENENNE "BENENNE")                                     | NAME REGION "name"                           |                                                   | K           |
| [BENENNE FREMDE EINHEIT einheit-nr "name"](/BENENNE "BENENNE")                  | NAME FOREIGN UNIT unit-no "name"             | names the specified foreign object                | K           |
| [BENENNE FREMDES SCHIFF schiff-nr "name"](/BENENNE "BENENNE")                   | NAME FOREIGN SHIP ship-no "name"             |                                                   | K           |
| [BENENNE FREMDES GEBÄUDE gebäude-nr "name"](/BENENNE "BENENNE")                 | NAME FOREIGN BUILDING building-no "name"     |                                                   | K           |
| [BENENNE FREMDE PARTEI partei-nr "name"](/BENENNE "BENENNE")                    | NAME FOREIGN FACTION faction-id "name"       |                                                   | K           |
| [BENUTZE \[anzahl\] trank](/BENUTZE "BENUTZE")                                  | USE \[amount\] potion                        | uses alchemical potion                            | K           |
| [BESCHREIBE EINHEIT "text"](/BESCHREIBE "BESCHREIBE")                           | DESCRIBE UNIT "text"                         | describes object                                  | K           |
| [BESCHREIBE PRIVAT "text"](/BESCHREIBE "BESCHREIBE")                            | DESCRIBE PRIVATE "text"                      | unit description for the owner                    | K           |
| [BESCHREIBE GEBÄUDE "text"](/BESCHREIBE "BESCHREIBE")                           | DESCRIBE BUILDING "text"                     |                                                   | K           |
| [BESCHREIBE SCHIFF "text"](/BESCHREIBE "BESCHREIBE")                            | DESCRIBE SHIP "text"                         |                                                   | K           |
| [BESCHREIBE REGION "text"](/BESCHREIBE "BESCHREIBE")                            | DESCRIBE REGION "text"                       |                                                   | K           |
| [BETRETE GEBÄUDE gebäude-nr](/BETRETE "BETRETE")                                | ENTER BUILDING building-id                   | Enter a building                                  | K           |
| [BETRETE SCHIFF schiff-nr](/BETRETE "BETRETE")                                  | ENTER SHIP ship-id                           | Enter a ship                                      | K           |
| [BEWACHE \[NICHT\]](/BEWACHE "BEWACHE")                                         | GUARD                                        | guard the region                                  | K           |
| [BEZAHLE NICHT \[gebäude-nr\]](/BEZAHLE "BEZAHLE")                              | PAY \[NOT\]                                  | do not pay a maintenance                          | K           |
| [BOTSCHAFT REGION "text"](/BOTSCHAFT "BOTSCHAFT")                               | MESSAGE REGION "text"                        | Send a message                                    | K           |
| [BOTSCHAFT SCHIFF schiff-nr "text"](/BOTSCHAFT "BOTSCHAFT")                     | MESSAGE SHIP ship-id "text"                  | Send a message                                    | K           |
| [BOTSCHAFT GEBÄUDE gebäude-nr "text"](/BOTSCHAFT "BOTSCHAFT")                   | MESSAGE BUILDING building-id "text"          | Send a message                                    | K           |
| [BOTSCHAFT EINHEIT einh-nr "text"](/BOTSCHAFT "BOTSCHAFT")                      | MESSAGE UNIT unit-id "text"                  | Send a message                                    | K           |
| [BOTSCHAFT PARTEI partei-nr "text"](/BOTSCHAFT "BOTSCHAFT")                     | MESSAGE FACTION faction-id "text"            | Send a message                                    | K           |
| [DEFAULT befehl](/DEFAULT "DEFAULT")                                            | DEFAULT                                      | sets the default order for the next turn          | K           |
| [EINHEIT einheit-nr](/EINHEIT "EINHEIT")                                        | UNIT unit-ID                                 | beginning of a unit's orders                      | K           |
| [EMAIL email@adresse](/EMAIL "EMAIL")                                           | EMAIL email@adresse                          | sets the e−mail the report is sent to             | K           |
| [ENDE](/ENDE "ENDE")                                                            | END                                          | ends a MAKE TEMP block                            | K           |
| [ERESSEA partei-nr "passwort"](/ERESSEA "ERESSEA")                              | ERESSEA faction-id "password"                | beginning of faction's orders                     | K           |
| [FAHRE einheit-nr](/FAHRE "FAHRE")                                              | RIDE unit-id                                 | be transported by unit−id                         | L           |
| [FOLGE EINHEIT einheit-nr](/FOLGE "FOLGE")                                      | FOLLOW UNIT unit-id                          | follows a unit                                    | (L)\*\*     |
| [FOLGE SCHIFF schiff-nr](/FOLGE "FOLGE")                                        | FOLLOW SHIP ship-id                          | follows a ship                                    | (L)\*\*     |
| [FORSCHE KRÄUTER](/FORSCHE "FORSCHE")                                           | RESEARCH herbs                               | search for herbs                                  | L           |
| [GIB einheit-nr KRÄUTER](/GIB "GIB")                                            | GIVE unit-id herbs                           | give a unit all herbs                             | K           |
| [GIB einheit-nr KOMMANDO](/GIB "GIB")                                           | GIVE unit-id command                         | give a unit ship/ building control                | K           |
| [GIB einheit-nr EINHEIT](/GIB "GIB")                                            | GIVE unit-id UNIT                            | give unit to a foreign faction                    | K           |
| [GIB einheit-nr \[JE\] anzahl PERSONEN](/GIB "GIB")                             | GIVE unit-id \[each\] amount MEN             | give a unit men                                   | K           |
| [GIB einheit-nr \[JE\] anzahl SCHIFF](/GIB "GIB")                               | GIVE unit-id \[each\] amount SHIP            | give SHIP to form convoys                         | K           |
| [GIB einheit-nr \[JE\] anzahl SILBER](/GIB "GIB")                               | GIVE unit-id \[each\] amount SILVER          | give silver                                       | K           |
| [GIB einheit-nr \[JE\] anzahl gegenstand](/GIB "GIB")                           | GIVE unit-id \[each\] amount item            | give item                                         | K           |
| [GIB 0 anzahl SILBER](/GIB "GIB")                                               | GIVE 0 number SILVER                         | throwing away objects                             | K           |
| [GIB 0 anzahl PERSONEN](/GIB "GIB")                                             | GIVE 0 number MEN                            |                                                   | K           |
| [GIB 0 anzahl gegenstand](/GIB "GIB")                                           | GIVE 0 number item                           |                                                   | K           |
| [GRUPPE \["name"\]](/GRUPPE "GRUPPE")                                           | GROUP \["name"\]                             | forms groups of units                             | K           |
| [HELFE partei-nr ALLES \[NICHT\]](/HELFE "HELFE")                               | HELP faction-id ALL \[NOT\]                  | set up/revoke an unilateral alliance              | K           |
| [HELFE partei-nr GIB \[NICHT\]](/HELFE "HELFE")                                 | HELP faction-id GIVE \[NOT\]                 |                                                   | K           |
| [HELFE partei-nr KÄMPFE \[NICHT\]](/HELFE "HELFE")                              | HELP faction-id COMBAT \[NOT\]               |                                                   | K           |
| [HELFE partei-nr BEWACHE \[NICHT\]](/HELFE "HELFE")                             | HELP faction-id GUARD \[NOT\]                |                                                   | K           |
| [HELFE partei-nr SILBER \[NICHT\]](/HELFE "HELFE")                              | HELP faction-id SILVER \[NOT\]               |                                                   | K           |
| [HELFE partei-nr PARTEITARNUNG \[NICHT\]](/HELFE "HELFE")                       | HELP faction-id FACTIONSTEALTH \[NOT\]       |                                                   | K           |
| [KÄMPFE](/K%C3%84MPFE "KÄMPFE")                                                 | COMBAT                                       | set the combat behaviour                          | K           |
| [KÄMPFE AGGRESSIV](/K%C3%84MPFE "KÄMPFE")                                       | COMBAT AGGRESSIVE                            |                                                   | K           |
| [KÄMPFE DEFENSIV](/K%C3%84MPFE "KÄMPFE")                                        | COMBAT DEFENSIVE                             |                                                   | K           |
| [KÄMPFE FLIEHE](/K%C3%84MPFE "KÄMPFE")                                          | COMBAT FLEE                                  |                                                   | K           |
| [KÄMPFE HELFE \[NICHT\]](/K%C3%84MPFE "KÄMPFE")                                 | COMBAT HELP \[NOT\]                          | the unit is \[not\] helped in the fight           | K           |
| [KÄMPFE HINTEN](/K%C3%84MPFE "KÄMPFE")                                          | COMBAT REAR                                  |                                                   | K           |
| [KÄMPFE NICHT](/K%C3%84MPFE "KÄMPFE")                                           | COMBAT NOT                                   |                                                   | K           |
| [KAMPFZAUBER \[STUFE n\] "zauberspruch" \[NICHT\]](/KAMPFZAUBER "KAMPFZAUBER")  | COMBATSPELL \[level n\] "spell" \[NOT\]      | set spell for combat                              | K           |
| [KAUFE anzahl luxusgut](/KAUFE "KAUFE")                                         | BUY amount luxurygood                        | buy luxury item                                   | L\*\*\*     |
| [KONTAKTIERE einheit-nr](/KONTAKTIERE "KONTAKTIERE")                            | CONTACT unit-no                              | contact foreign unit                              | K           |
| [LEHRE einheit-nr \[einheit-nr etc.\]](/LEHRE "LEHRE")                          | TEACH unit-no                                | teach units                                       | L           |
| [LERNE talent](/LERNE "LERNE")                                                  | LEARN skill                                  | learn a skill                                     | L           |
| [LERNE AUTO talent](/LERNE_AUTO "LERNE AUTO")                                   | LEARN AUTO                                   | learn or teach a skill                            | L           |
| [LOCALE en/de](/LOCALE "LOCALE")                                                | LOCALE en/de                                 | no function (only for tools)                      | K           |
| [MACHE TEMP unit-alias-nr \["name"\]](/MACHE "MACHE")                           | MAKE TEMP unit-alias-nr \["name"\]           | creates a new unit                                | K           |
| [MACHE \[stufe\] gebäude-typ \[gebäude-nr\]](/MACHE "MACHE")                    | MAKE \[level\] building-type \[building-ID\] | erect or extend a building                        | L           |
| [MACHE \[stufe\] SCHIFF \[schiff-nr\]](/MACHE "MACHE")                          | MAKE \[level\] SHIP \[ship-ID\]              | extend a ship                                     | L           |
| [MACHE](/MACHE "MACHE")                                                         | MAKE ??                                      | baue weiter an Gebäude/Schiff ??                  | L           |
| [MACHE \[stufe\] BOOT](/MACHE "MACHE")                                          | MAKE \[level\] boat                          | build a boat                                      | L           |
| [MACHE \[stufe\] LANGBOOT](/MACHE "MACHE")                                      | MAKE \[level\] longboat                      | build a longboat                                  | L           |
| [MACHE \[stufe\] DRACHENSCHIFF](/MACHE "MACHE")                                 | MAKE \[level\] dragonship                    | build a dragonship                                | L           |
| [MACHE \[stufe\] KARAVELLE](/MACHE "MACHE")                                     | MAKE \[level\] caravel                       |                                                   | L           |
| [MACHE \[stufe\] TRIREME](/MACHE "MACHE")                                       | MAKE \[level\] trireme                       |                                                   | L           |
| [MACHE \[stufe\] GALEONE](/MACHE "MACHE")                                       | MAKE \[level\] galleon                       |                                                   | L           |
| [MACHE \[stufe\] STRASSE richtung](/MACHE "MACHE")                              | MAKE \[level\] ROAD direction                | build road                                        | L           |
| [MACHE \[anzahl\] KRÄUTER](/MACHE "MACHE")                                      | MAKE \[amount\] HERBS                        | pick herbs in a region                            | L           |
| [MACHE \[anzahl\] trank](/MACHE "MACHE")                                        | MAKE \[amount\] POTIONS                      | make a potion                                     | L           |
| [MACHE \[anzahl\] gegenstand](/MACHE "MACHE")                                   | MAKE \[amount\] item                         | make an item                                      | L           |
| [NACH richtung \[richtung etc.\]](/NACH "NACH")                                 | MOVE direction \[direction\]                 | move unit                                         | L           |
| [NÄCHSTER](/N%C3%84CHSTER "NÄCHSTER")                                           | NEXT                                         | ends the orders of a faction                      | K           |
| [NUMMER EINHEIT \[neue\_nr\]](/NUMMER "NUMMER")                                 | NUMBER UNIT \[newID\]                        | gives a new id                                    | K           |
| [NUMMER GEBÄUDE \[neue\_nr\]](/NUMMER "NUMMER")                                 | NUMBER CASTLE \[newID\]                      |                                                   | K           |
| [NUMMER PARTEI \[neue\_nr\]](/NUMMER "NUMMER")                                  | NUMBER FACTION \[newID\]                     |                                                   | K           |
| [NUMMER SCHIFF \[neue\_nr\]](/NUMMER "NUMMER")                                  | NUMBER SHIP \[newID\]                        |                                                   | K           |
| [OPTION AUSWERTUNG \[NICHT\]](/OPTION "OPTION")                                 | OPTION                                       | Set / Revoke Options                              | K           |
| [OPTION COMPUTER \[NICHT\]](/OPTION "OPTION")                                   | OPTION                                       |                                                   | K           |
| [OPTION ZIPPED \[NICHT\]](/OPTION "OPTION")                                     | OPTION                                       |                                                   | K           |
| [OPTION BZIP2 \[NICHT\]](/OPTION "OPTION")                                      | OPTION                                       |                                                   | K           |
| [OPTION SILBERPOOL \[NICHT\]](/OPTION "OPTION")                                 | OPTION                                       |                                                   | K           |
| [OPTION MATERIALPOOL \[NICHT\]](/OPTION "OPTION")                               | OPTION                                       |                                                   | K           |
| [OPTION ADRESSEN \[NICHT\]](/OPTION "OPTION")                                   | OPTION                                       |                                                   | K           |
| [OPTION ZUGVORLAGE \[NICHT\]](/OPTION "OPTION")                                 | OPTION                                       |                                                   | K           |
| [OPTION STATISTIK \[NICHT\]](/OPTION "OPTION")                                  | OPTION                                       |                                                   | K           |
| [OPTION TALENTVERSCHIEBUNG \[NICHT\]](/OPTION "OPTION")                         | OPTION                                       |                                                   | K           |
| [OPTION PUNKTE \[NICHT\]](/OPTION "OPTION")                                     | OPTION                                       |                                                   | K           |
| [PASSWORT "neues-passwort"](/PASSWORT "PASSWORT")                               | PASSWORD "new-password"                      | set new password                                  | K           |
| [PFLANZE \[anzahl\] KRÄUTER](/PFLANZE "PFLANZE")                                | PLANT \[amount\] HERBS                       | Plant herbs                                       | L           |
| [PFLANZE \[anzahl\] BÄUME](/PFLANZE "PFLANZE")                                  | PLANT \[amount\] TREES                       | Plant seeds                                       | L           |
| [PFLANZE \[anzahl\] MALLORNSAMEN](/PFLANZE "PFLANZE")                           | PLANT \[amount\] "mallorn seeds"             | Plant mallorn seeds                               | L           |
| [PFLANZE \[anzahl\] SAMEN](/PFLANZE "PFLANZE")                                  | PLANT \[amount\] SEEDS                       | Plant seeds                                       | L           |
| [PIRATERIE \[partei\_1\] \[partei\_2\] \[...\]](/PIRATERIE "PIRATERIE")         | PIRACY \[faction\_1\] \[faction\_2\]         | Set Piracy                                        | L           |
| [PRÄFIX \[präfix\]](/PR%C3%84FIX "PRÄFIX")                                      | PREFIX                                       | prepend the race name with a prefix               | K           |
| [REGION x,y](/REGION "REGION")                                                  | REGION x,y                                   | no function (only for tools)                      | K           |
| [REKRUTIERE anzahl](/REKRUTIERE "REKRUTIERE")                                   | RECRUIT amount                               | recruit men (persons of your race)                | K           |
| [RESERVIERE anzahl "gegenstand"](/RESERVIERE "RESERVIERE")                      | RESERVE amount item                          | reserve item                                      | K           |
| [RESERVIERE anzahl SILBER](/RESERVIERE "RESERVIERE")                            | RESERVE amount silver                        | reserve silver                                    | K           |
| [ROUTE richtung \[richtung etc.\]](/ROUTE "ROUTE")                              | ROUTE direction \[direction etc.\]           | Travel                                            | L           |
| [SORTIERE VOR einheit-nr](/SORTIERE "SORTIERE")                                 | SORT BEFORE unit-id                          | sort unit in report                               | K           |
| [SORTIERE HINTER einheit-nr](/SORTIERE "SORTIERE")                              | SORT AFTER unit-id                           |                                                   | K           |
| [SPIONIERE einheit-nr](/SPIONIERE "SPIONIERE")                                  | SPY unit-id                                  | spy a unit                                        | L           |
| [SPRACHE en/de](/SPRACHE "SPRACHE")                                             | LANGUAGE en/de                               | Change Language for orders                        | K           |
| [STIRB "passwort" \[PARTEI partei-nr\]](/STIRB "STIRB")                         | QUIT "password" \[FACTION Faction-id\]       | quit the game \[merge with another faction\]      | K           |
| [TARNE \[stufe\]](/TARNE "TARNE")                                               | HIDE \[level\]                               | set hide level                                    | K           |
| [TARNE rasse](/TARNE "TARNE")                                                   | HIDE \[race\]                                | Demon: disguise as another race                   | K           |
| [TARNE PARTEI \[NICHT\]](/TARNE "TARNE")                                        | HIDE FACTION \[NOT\]                         | hide faction membership (hide as"anonym")         | K           |
| [TARNE PARTEI NUMMER nummer](/TARNE "TARNE")                                    | HIDE FACTION faction-ID                      | disguised as another faction                      | K           |
| [TRANSPORTIERE einheit-nr](/TRANSPORTIERE "TRANSPORTIERE")                      | CARRY unit-id                                | transport another unit                            | K           |
| [TREIBE \[betrag\]](/TREIBE "TREIBE")                                           | TAX \[amount\]                               | tax peasants (max. 20 silver/skill lvl)           | L           |
| [UNTERHALTE \[betrag\]](/UNTERHALTE "UNTERHALTE")                               | ENTERTAIN \[amount\]                         | earn 20 or more silver (max. 20 silver/skill lvl) | L           |
| [URSPRUNG \[x y\]](/URSPRUNG "URSPRUNG")                                        | ORIGIN \[x y\]                               | Sets the origin to x,y                            | K           |
| [VERGISS talent](/VERGISS "VERGISS")                                            | FORGET skill                                 | forget a skill                                    | K           |
| [VERKAUFE anzahl luxusgut](/VERKAUFE "VERKAUFE")                                | SELL \[amount\] \[ALL\] good                 | sell luxury goods                                 | (L)\*\*\*\* |
| [VERLASSE](/VERLASSE "VERLASSE")                                                | LEAVE                                        | leave ship or building                            | K           |
| [ZAUBERE \[REGION x y\] \[STUFE n\] "zauberspruch" \[...\]](/ZAUBERE "ZAUBERE") | CAST \[REGION x y\] \[level n\] "spell"      | Cast spells                                       | (L)         |
| [ZEIGE "zauberspruch"](/ZEIGE "ZEIGE")                                          | SHOW                                         | retrieve spell description                        | K           |
| [ZERSTÖRE](/ZERST%C3%96RE "ZERSTÖRE")                                           | DESTROY                                      | building, ship, or road                           | L           |
| [ZÜCHTE PFERDE](/Z%C3%9CCHTE "ZÜCHTE")                                          | GROW HORSES                                  | breed horses, needs a stable                      | L           |
| [ZÜCHTE KRÄUTER](/Z%C3%9CCHTE "ZÜCHTE")                                         | GROW HERBS                                   | need "Water of Life"                              | L           |
| [ZÜCHTE BÄUME](/Z%C3%9CCHTE "ZÜCHTE")                                           | GROW TREES                                   | works ? need "Water of Life"                      | L           |

\* voir [The aftermath of battle]; \*\*If the tracked unit does not move, another long order can be executed instead; \*\*\*can be combined with SELL; \*\*\*\*can be combined with BUY

## See also

- [Orders]
- [Orders sequence]

|-------------------|-------------------------------------------------|
| Continue reading: | [Der erste Zug](/Der_erste_Zug "Der erste Zug") |

<!-- From [https://wiki.eressea.de/index.php?title=Diskussion:Kurzbeschreibung/en&oldid=8215] -->

  [Order]: ./commands.md "Befehl"
  [The aftermath of battle]: ./war.md#kampfende "Kampfende"
  [Orders]: ./commands.md "Befehle"
  [Orders sequence]: ./commands-sequence.md "Befehlsreihenfolge"
