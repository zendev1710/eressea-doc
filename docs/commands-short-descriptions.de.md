---
# cSpell:locale de
alias: diskussion:kurzbeschreibung
---
# Diskussion:Kurzbeschreibung

Unter "K/L" ist vermerkt, ob der [Befehl] ein kurzer oder langer Befehl ist, d.h., ob er sofort ausgeführt wird (und danach weitere Befehle möglich sind) oder eine ganze Runde zur Ausführung braucht.

\(L\) bezeichnet einen pseudolangen [Befehl], der einer Einheit mehrfach gegeben werden kann. Allerdings kann kein weiterer anderer langer Befehl ausgeführt werden.

Kurzliste der Befehle

| Befehl (Deutsch)                                                           | Befehl (English)                             | Beschreibung                                           | K/L         |
|----------------------------------------------------------------------------|----------------------------------------------|--------------------------------------------------------|-------------|
| [//](./cmd-comment-slash.md)                                               | //                                           | bleibender Kommentar                                   | K           |
| [[bef-arbeite]](./cmd-work.md)                                             | WORK                                         | verdient 10 Silber oder mehr                           | L           |
| [ATTACKIERE einheit-nr](./cmd-attack.md)                                   | ATTACK unit-ID                               | greift die Einheit an                                  | (L)\*       |
| [BANNER "text"](./cmd-banner.md)                                           | BANNER                                       | Setzt Text für Adress-Liste                            | K           |
| [BEANSPRUCHE anzahl gegenstand](./cmd-claim.md)                            | CLAIM                                        | holt Gegenstände aus Parteipool                        | K           |
| [[bef-befoerdere]](./cmd-promote.md)                                       | PROMOTE                                      | macht Einheit zu Helden                                | K           |
| [BEKLAUE einheit-nr](./cmd-steal.md)                                       | STEAL unit-ID                                | klaut 50 Silber oder mehr                              | L           |
| [BENENNE EINHEIT "name"](./cmd-name.md)                                    | NAME UNIT "name"                             | benennt Objekte                                        | K           |
| [BENENNE PARTEI "name"](./cmd-name.md)                                     | NAME FACTION "name"                          |                                                        | K           |
| [BENENNE GEBÄUDE "name"](./cmd-name.md)                                    | NAME BUILDING "name"                         |                                                        | K           |
| [BENENNE SCHIFF "name"](./cmd-name.md)                                     | NAME SHIP "name"                             |                                                        | K           |
| [BENENNE REGION "name"](./cmd-name.md)                                     | NAME REGION "name"                           |                                                        | K           |
| [BENENNE FREMDE EINHEIT einheit-nr "name"](./cmd-name.md)                  | NAME FOREIGN UNIT unit-no "name"             | benennt fremde und unbenannte Objekte                  | K           |
| [BENENNE FREMDES SCHIFF schiff-nr "name"](./cmd-name.md)                   | NAME FOREIGN SHIP ship-no "name"             |                                                        | K           |
| [BENENNE FREMDES GEBÄUDE gebäude-nr "name"](./cmd-name.md)                 | NAME FOREIGN BUILDING building-no "name"     |                                                        | K           |
| [BENENNE FREMDE PARTEI partei-nr "name"](./cmd-name.md)                    | NAME FOREIGN FACTION?? faction??-no "name"   |                                                        | K           |
| [BENUTZE \[anzahl\] trank](./cmd-use.md)                                   | USE \[amount\] potion                        | benutzt alchemistischen Trank                          | K           |
| [BESCHREIBE EINHEIT "text"](./cmd-describe.md)                             | DESCRIBE UNIT "text"                         | beschreibt Objekte                                     | K           |
| [BESCHREIBE PRIVAT "text"](./cmd-describe.md)                              | DESCRIBE PRIVATE "text"                      |                                                        | K           |
| [BESCHREIBE GEBÄUDE "text"](./cmd-describe.md)                             | DESCRIBE BUILDING "text"                     |                                                        | K           |
| [BESCHREIBE SCHIFF "text"](./cmd-describe.md)                              | DESCRIBE SHIP "text"                         |                                                        | K           |
| [BESCHREIBE REGION "text"](./cmd-describe.md)                              | DESCRIBE REGION "text"                       |                                                        | K           |
| [BETRETE GEBÄUDE gebäude-nr](./cmd-enter.md)                               | ENTER BUILDING building-id                   | betritt Gebäude                                        | K           |
| [BETRETE SCHIFF schiff-nr](./cmd-enter.md)                                 | ENTER SHIP ship-id                           | betritt Schiffe                                        | K           |
| [BEWACHE \[NICHT\]](./cmd-guard.md)                                        | GUARD                                        | bewacht die Region                                     | K           |
| [BEZAHLE NICHT \[gebäude-nr\]](./cmd-pay-not.md)                           | PAY \[NOT\]                                  | bezahlt den Unterhalt für ein Gebäude nicht            | K           |
| [BOTSCHAFT REGION "text"](./cmd-message.md)                                | MESSAGE REGION "text"                        | versendet Botschaften                                  | K           |
| [BOTSCHAFT SCHIFF schiff-nr "text"](./cmd-message.md)                      | MESSAGE SHIP ship-id "text"                  | versendet Botschaften                                  | K           |
| [BOTSCHAFT GEBÄUDE gebäude-nr "text"](./cmd-message.md)                    | MESSAGE BUILDING building-id "text"          | versendet Botschaften                                  | K           |
| [BOTSCHAFT EINHEIT einh-nr "text"](./cmd-message.md)                       | MESSAGE UNIT unit-id "text"                  |                                                        | K           |
| [BOTSCHAFT PARTEI partei-nr "text"](./cmd-message.md)                      | MESSAGE FACTION faction-id "text"            |                                                        | K           |
| [DEFAULT befehl](./cmd-default.md)                                         | DEFAULT                                      | Setzt Default-Befehl für die nächste Runde.            | K           |
| [EINHEIT einheit-nr](./cmd-unit.md)                                        | UNIT unit-ID                                 | beginnt Befehle für eine Einheit                       | K           |
| [EMAIL email@adresse](./cmd-email.md)                                      | EMAIL email@adresse                          | setzt die eMail-Adresse                                | K           |
| [[bef-ende]](./cmd-end.md)                                                 | END                                          | beendet MACHE TEMP                                     | K           |
| [ERESSEA partei-nr "passwort"](./cmd-eressea.md)                           | ERESSEA faction-id "password"                | beginnt Befehle für Partei                             | K           |
| [FAHRE einheit-nr](./cmd-ride.md)                                          | RIDE unit-id                                 | sich transportieren lassen                             | L           |
| [FOLGE EINHEIT einheit-nr](./cmd-follow.md)                                | FOLLOW UNIT unit-id                          | folgt einer Einheit                                    | (L)\*\*     |
| [FOLGE SCHIFF schiff-nr](./cmd-follow.md)                                  | FOLLOW SHIP ship-id                          | folgt einem Schiff                                     | (L)\*\*     |
| [FORSCHE KRÄUTER](./cmd-research.md)                                       | RESEARCH herbs                               | sucht Kräuter                                          | L           |
| [GIB einheit-nr KRÄUTER](./cmd-give.md)                                    | GIVE unit-id herbs\_name                     | gibt einer Einheit alle Kräuter                        | K           |
| [GIB einheit-nr KOMMANDO](./cmd-give.md)                                   | GIVE unit-id command                         | übergibt Kommando über Schiff/Gebäude                  | K           |
| [GIB einheit-nr EINHEIT](./cmd-give.md)                                    | GIVE unit-id UNIT                            | übergibt Einheit an fremde Partei                      | K           |
| [GIB einheit-nr \[JE\] anzahl PERSONEN](./cmd-give.md)                     | GIVE unit-id \[each\] amount MEN             | übergibt Personen                                      | K           |
| [GIB einheit-nr \[JE\] anzahl SCHIFF](./cmd-give.md)                       | GIVE unit-id \[each\] amount SHIP            | übergibt SCHIFF zur Bildung von Konvois                | K           |
| [GIB einheit-nr \[JE\] anzahl SILBER](./cmd-give.md)                       | GIVE unit-id \[each\] amount SILVER          | übergibt Silber                                        | K           |
| [GIB einheit-nr \[JE\] anzahl gegenstand](./cmd-give.md)                   | GIVE unit-id \[each\] amount item            | übergibt Gegenstände                                   | K           |
| [GIB 0 anzahl SILBER](./cmd-give.md)                                       | GIVE 0 number SILVER                         | wegwerfen von Gegenständen                             | K           |
| [GIB 0 anzahl PERSONEN](./cmd-give.md)                                     | GIVE 0 number MEN                            |                                                        | K           |
| [GIB 0 anzahl gegenstand](./cmd-give.md)                                   | GIVE 0 number item                           |                                                        | K           |
| [GRUPPE \["name"\]](./cmd-group.md)                                        | GROUP \["name"\]                             | Gruppieren von Einheiten                               | K           |
| [HELFE partei-nr ALLES \[NICHT\]](./cmd-help.md)                           | HELP faction-id ALL \[NOT\]                  | setze/lösche einseitige Allianz                        | K           |
| [HELFE partei-nr GIB \[NICHT\]](./cmd-help.md)                             | HELP faction-id GIVE \[NOT\]                 |                                                        | K           |
| [HELFE partei-nr KÄMPFE \[NICHT\]](./cmd-help.md)                          | HELP faction-id COMBAT \[NOT\]               |                                                        | K           |
| [HELFE partei-nr BEWACHE \[NICHT\]](./cmd-help.md)                         | HELP faction-id GUARD \[NOT\]                |                                                        | K           |
| [HELFE partei-nr SILBER \[NICHT\]](./cmd-help.md)                          | HELP faction-id SILVER \[NOT\]               |                                                        | K           |
| [HELFE partei-nr PARTEITARNUNG \[NICHT\]](./cmd-help.md)                   | HELP faction-id FACTIONSTEALTH \[NOT\]       |                                                        | K           |
| [KÄMPFE](./cmd-combat.md)                                                  | COMBAT                                       | setzt Verhalten im Kampf                               | K           |
| [KÄMPFE AGGRESSIV](./cmd-combat.md)                                        | COMBAT AGGRESSIVE                            |                                                        | K           |
| [KÄMPFE DEFENSIV](./cmd-combat.md)                                         | COMBAT DEFENSIVE                             |                                                        | K           |
| [KÄMPFE FLIEHE](./cmd-combat.md)                                           | COMBAT FLEE                                  |                                                        | K           |
| [KÄMPFE HELFE \[NICHT\]](./cmd-combat.md)                                  | COMBAT HELP \[NOT\]                          | der Einheit wird im Kampf \[nicht\] geholfen           | K           |
| [KÄMPFE HINTEN](./cmd-combat.md)                                           | COMBAT REAR                                  |                                                        | K           |
| [KÄMPFE NICHT](./cmd-combat.md)                                            | COMBAT NOT                                   |                                                        | K           |
| [KAMPFZAUBER \[STUFE n\] "zauberspruch" \[NICHT\]](./cmd-combatspell.md)   | COMBATSPELL \[level n\] "spell" \[NOT\]      | setzt Zauber für Kämpfe                                | K           |
| [KAUFE anzahl luxusgut](./cmd-buy.md)                                      | BUY amount luxurygood                        | kaufe Luxusgüter                                       | L\*\*\*     |
| [KONTAKTIERE einheit-nr](./cmd-contact.md)                                 | CONTACT unit-no                              | kontaktiere fremde Einheiten                           | K           |
| [LEHRE einheit-nr \[einheit-nr etc.\]](./cmd-teach.md)                     | TEACH unit-no                                | lehre Einheiten                                        | L           |
| [LERNE talent](./cmd-learn.md)                                             | LEARN skill                                  | Talent lernen                                          | L           |
| [LERNE AUTO talent](./cmd-learn-auto.md)                                   | LEARN AUTO                                   | Talent lernen oder lehren                              | L           |
| [LOCALE en/de](./cmd-locale.md)                                            | LOCALE en/de??                               | Zeigt die Sprache der Befehle an                       | K           |
| [MACHE TEMP unit-alias-nr \["name"\]](./cmd-make.md)                       | MAKE TEMP unit-alias-nr \["name"\]           | erschaffe neue Einheit                                 | K           |
| [MACHE \[stufe\] gebäude-typ \[gebäude-nr\]](./cmd-make.md)                | MAKE \[level\] building-type \[building-ID\] | erweitere oder baue neues Gebäude                      | L           |
| [MACHE \[stufe\] SCHIFF \[schiff-nr\]](./cmd-make.md)                      | MAKE \[level\] SHIP \[ship-ID\]              | baue weiter am Schiff                                  | L           |
| [[bef-mache]](./cmd-make.md)                                               | MAKE                                         | baue weiter an Gebäude/Schiff                          | L           |
| [MACHE \[stufe\] BOOT](./cmd-make.md)                                      | MAKE \[level\] boat                          | baue neue Schiffe                                      | L           |
| [MACHE \[stufe\] LANGBOOT](./cmd-make.md)                                  | MAKE \[level\] longboat                      |                                                        | L           |
| [MACHE \[stufe\] DRACHENSCHIFF](./cmd-make.md)                             | MAKE \[level\] dragonship                    |                                                        | L           |
| [MACHE \[stufe\] KARAVELLE](./cmd-make.md)                                 | MAKE \[level\] caravel                       |                                                        | L           |
| [MACHE \[stufe\] TRIREME](./cmd-make.md)                                   | MAKE \[level\] trireme                       |                                                        | L           |
| [MACHE \[stufe\] GALEONE](./cmd-make.md)                                   | MAKE \[level\] galleon                       |                                                        | L           |
| [MACHE \[stufe\] STRASSE richtung](./cmd-make.md)                          | MAKE \[level\] ROAD direction                | baue Straßen                                           | L           |
| [MACHE \[anzahl\] KRÄUTER](./cmd-make.md)                                  | MAKE \[amount\] HERBS                        | suche Kräuter der Region                               | L           |
| [MACHE \[anzahl\] trank](./cmd-make.md)                                    | MAKE \[amount\] POTIONS                      | mache einen alchemistischen Trank                      | L           |
| [MACHE \[anzahl\] gegenstand](./cmd-make.md)                               | MAKE \[amount\] item                         | mache einen Gegenstand                                 | L           |
| [NACH richtung \[richtung etc.\]](./cmd-move.md)                           | MOVE direction \[direction\]                 | Reisen                                                 | L           |
| [NÄCHSTER](./cmd-next.md)                                                  | NEXT                                         | Beendet Befehle                                        | K           |
| [NUMMER EINHEIT \[neue\_nr\]](./cmd-number.md)                             | NUMBER UNIT \[newID\]                        | vergibt neue Nummer                                    | K           |
| [NUMMER GEBÄUDE \[neue\_nr\]](./cmd-number.md)                             | NUMBER CASTLE \[newID\]                      |                                                        | K           |
| [NUMMER PARTEI \[neue\_nr\]](./cmd-number.md)                              | NUMBER FACTION \[newID\]                     |                                                        | K           |
| [NUMMER SCHIFF \[neue\_nr\]](./cmd-number.md)                              | NUMBER SHIP \[newID\]                        |                                                        | K           |
| [OPTION AUSWERTUNG \[NICHT\]](./cmd-option.md)                             | OPTION                                       | verschiedene Optionen                                  | K           |
| [OPTION COMPUTER \[NICHT\]](./cmd-option.md)                               | OPTION                                       |                                                        | K           |
| [OPTION ZIPPED \[NICHT\]](./cmd-option.md)                                 | OPTION                                       |                                                        | K           |
| [OPTION BZIP2 \[NICHT\]](./cmd-option.md)                                  | OPTION                                       |                                                        | K           |
| [OPTION SILBERPOOL \[NICHT\]](./cmd-option.md)                             | OPTION                                       |                                                        | K           |
| [OPTION MATERIALPOOL \[NICHT\]](./cmd-option.md)                           | OPTION                                       |                                                        | K           |
| [OPTION ADRESSEN \[NICHT\]](./cmd-option.md)                               | OPTION                                       |                                                        | K           |
| [OPTION ZUGVORLAGE \[NICHT\]](./cmd-option.md)                             | OPTION                                       |                                                        | K           |
| [OPTION STATISTIK \[NICHT\]](./cmd-option.md)                              | OPTION                                       |                                                        | K           |
| [OPTION TALENTVERSCHIEBUNG \[NICHT\]](./cmd-option.md)                     | OPTION                                       |                                                        | K           |
| [OPTION PUNKTE \[NICHT\]](./cmd-option.md)                                 | OPTION                                       |                                                        | K           |
| [PASSWORT "neues-passwort"](./cmd-password.md)                             | PASSWORD "new-password"                      | setze neues Passwort                                   | K           |
| [PFLANZE \[anzahl\] KRÄUTER](./cmd-plant.md)                               | PLANT \[amount\] HERBS                       | pflanzt Kräuter                                        | L           |
| [PFLANZE \[anzahl\] BÄUME](./cmd-plant.md)                                 | PLANT \[amount\] TREES                       | pflanzt Samen                                          | L           |
| [PFLANZE \[anzahl\] MALLORNSAMEN](./cmd-plant.md)                          | PLANT \[amount\] "mallorn seeds"             | pflanzt Samen                                          | L           |
| [PFLANZE \[anzahl\] SAMEN](./cmd-plant.md)                                 | PLANT \[amount\] SEEDS                       | pflanzt Samen                                          | L           |
| [PIRATERIE \[partei\_1\] \[partei\_2\] \[...\]](./cmd-piracy.md)           | PIRACY \[faction\_1\] \[faction\_2\]         | Piraterie setzen                                       | L           |
| [PRÄFIX \[präfix\]](./cmd-prefix.md)                                       | PREFIX                                       | gibt der Rassenbezeichnung ein Präfix                  | K           |
| [REGION x,y](./cmd-region.md)                                              | REGION x,y                                   | keine Funktion (nur für Tools)                         | K           |
| [REKRUTIERE anzahl](./cmd-recruit.md)                                      | RECRUIT amount                               | rekrutiere weitere Personen                            | K           |
| [RESERVIERE anzahl "gegenstand"](./cmd-reserve.md)                         | RESERVE amount item                          | Gegenstände reservieren                                | K           |
| [RESERVIERE anzahl SILBER](./cmd-reserve.md)                               | RESERVE amount silver                        | Silber reservieren                                     | K           |
| [ROUTE richtung \[richtung etc.\]](./cmd-route.md)                         | ROUTE direction \[direction etc.\]           | Reisen                                                 | L           |
| [SORTIERE VOR einheit-nr](./cmd-sort.md)                                   | SORT BEFORE unit-id                          | Einheit in Report sortieren                            | K           |
| [SORTIERE HINTER einheit-nr](./cmd-sort.md)                                | SORT AFTER unit-id                           |                                                        | K           |
| [SPIONIERE einheit-nr](./cmd-spy.md)                                       | SPY unit-id                                  | Einheit ausspionieren                                  | L           |
| [SPRACHE en/de](./cmd-language.md)                                         | LANGUAGE                                     | Ändert die Sprache der Partei                          | K           |
| [STIRB "passwort" \[PARTEI partei-nr\]](./cmd-quit.md)                     | QUIT "password"                              | aus dem Spiel ausscheiden                              | K           |
| [TARNE \[stufe\]](./cmd-tax.md)                                            | HIDE \[level\]                               | Tarnstufe setzen                                       | K           |
| [TARNE rasse](./cmd-tax.md)                                                | HIDE \[race\]                                | Dämonen: als andere Rasse tarnen                       | K           |
| [TARNE PARTEI \[NICHT\]](./cmd-tax.md)                                     | HIDE FACTION \[NOT\]                         | Parteizugehörigkeit verbergen (als "anonym" getarnt)   | K           |
| [TARNE PARTEI NUMMER nummer](./cmd-tax.md)                                 | HIDE FACTION faction-ID                      | Parteizugehörigkeit tarnen (als andere Partei getarnt) | K           |
| [TRANSPORTIERE einheit-nr](./cmd-carry.md)                                 | CARRY unit-id                                | andere Einheiten mitnehmen                             | K           |
| [TREIBE \[betrag\]](./cmd-tax.md)                                          | TAX \[amount\]                               | Steuern eintreiben (max. 20 S/Talentstufe)             | L           |
| [UNTERHALTE \[betrag\]](./cmd-entertain.md)                                | ENTERTAIN \[amount\]                         | verdiene 20 oder mehr Silber                           | L           |
| [URSPRUNG \[x y\]](./cmd-origin.md)                                        | ORIGIN \[x y\]                               | setzt den Koordinaten-Ursprung                         | K           |
| [VERGISS talent](./cmd-forget.md)                                          | FORGET skill                                 | vergißt das Talent                                     | K           |
| [VERKAUFE anzahl luxusgut](./cmd-sell.md)                                  | SELL \[amount\] \[ALL\] luxurygood           | verkaufe Luxusgüter                                    | (L)\*\*\*\* |
| [[bef-verlasse]](./cmd-leave.md)                                           | LEAVE                                        | Schiff oder Gebäude verlassen                          | K           |
| [ZAUBERE \[REGION x y\] \[STUFE n\] "zauberspruch" \[...\]](./cmd-cast.md) | CAST \[REGION x y\] \[level n\] "spell"      | Zaubern                                                | (L)         |
| [ZEIGE "zauberspruch"](./cmd-show.md)                                      | SHOW                                         | Zeige Beschreibung des Zaubers                         | K           |
| [ZERSTÖRE](./cmd-destroy.md)                                               | DESTROY                                      | Gebäude, Schiff oder Straße                            | L           |
| [ZÜCHTE PFERDE](./cmd-grow.md)                                             | GROW HORSES                                  | Pferde züchten - nur in Pferdezucht                    | L           |
| [ZÜCHTE KRÄUTER](./cmd-grow.md)                                            | GROW HERBS                                   | Kräuter züchten                                        | L           |
| [ZÜCHTE BÄUME](./cmd-grow.md)                                              | GROW TREES                                   | Samen pflanzen                                         | L           |

\* siehe [Kampfende]; \*\*bewegt sich die verfolgte Einheit nicht, kann stattdessen ein anderer langer Befehl ausgeführt werden; \*\*\*kann mit VERKAUFE kombiniert werden; \*\*\*\*kann mit KAUFE kombiniert werden

## Siehe auch

- [Befehle]
- [Befehlsreihenfolge]

Weiterlesen: [Der erste Zug](./first-round.md).

<!-- From [https://wiki.eressea.de/index.php?title=Diskussion:Kurzbeschreibung&oldid=8099] -->

[Befehl]: ./commands.md
[Befehle]: ./commands.md
[Befehlsreihenfolge]: ./commands-sequence.md

[Kampfende]: ./war.md#das-ende
