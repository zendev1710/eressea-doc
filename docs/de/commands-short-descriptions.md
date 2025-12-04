# Diskussion:Kurzbeschreibung

Unter "K/L" ist vermerkt, ob der [Befehl] ein kurzer oder langer Befehl ist, d.h., ob er sofort ausgeführt wird (und danach weitere Befehle möglich sind) oder eine ganze Runde zur Ausführung braucht.

\(L\) bezeichnet einen pseudolangen [Befehl], der einer Einheit mehrfach gegeben werden kann. Allerdings kann kein weiterer anderer langer Befehl ausgeführt werden.

Kurzliste der Befehle

| Befehl (Deutsch)                                                                | Command (English)                            | Beschreibung                                           | K/L         |
|---------------------------------------------------------------------------------|----------------------------------------------|--------------------------------------------------------|-------------|
| [//](/KOMMENTAR "KOMMENTAR")                                                    | //                                           | bleibender Kommentar                                   | K           |
| [ARBEITE](/ARBEITE "ARBEITE")                                                   | WORK                                         | verdient 10 Silber oder mehr                           | L           |
| [ATTACKIERE einheit-nr](/ATTACKIERE "ATTACKIERE")                               | ATTACK unit-ID                               | greift die Einheit an                                  | (L)\*       |
| [BANNER "text"](/BANNER "BANNER")                                               | BANNER                                       | Setzt Text für Adress-Liste                            | K           |
| [BEANSPRUCHE anzahl gegenstand](/BEANSPRUCHE "BEANSPRUCHE")                     | CLAIM                                        | holt Gegenstände aus Parteipool                        | K           |
| [BEFÖRDERE](/BEF%C3%96RDERE "BEFÖRDERE")                                        | PROMOTE                                      | macht Einheit zu Helden                                | K           |
| [BEKLAUE einheit-nr](/BEKLAUE "BEKLAUE")                                        | STEAL unit-ID                                | klaut 50 Silber oder mehr                              | L           |
| [BENENNE EINHEIT "name"](/BENENNE "BENENNE")                                    | NAME UNIT "name"                             | benennt Objekte                                        | K           |
| [BENENNE PARTEI "name"](/BENENNE "BENENNE")                                     | NAME FACTION "name"                          |                                                        | K           |
| [BENENNE GEBÄUDE "name"](/BENENNE "BENENNE")                                    | NAME BUILDING "name"                         |                                                        | K           |
| [BENENNE SCHIFF "name"](/BENENNE "BENENNE")                                     | NAME SHIP "name"                             |                                                        | K           |
| [BENENNE REGION "name"](/BENENNE "BENENNE")                                     | NAME REGION "name"                           |                                                        | K           |
| [BENENNE FREMDE EINHEIT einheit-nr "name"](/BENENNE "BENENNE")                  | NAME FOREIGN UNIT unit-no "name"             | benennt fremde und unbenannte Objekte                  | K           |
| [BENENNE FREMDES SCHIFF schiff-nr "name"](/BENENNE "BENENNE")                   | NAME FOREIGN SHIP ship-no "name"             |                                                        | K           |
| [BENENNE FREMDES GEBÄUDE gebäude-nr "name"](/BENENNE "BENENNE")                 | NAME FOREIGN BUILDING building-no "name"     |                                                        | K           |
| [BENENNE FREMDE PARTEI partei-nr "name"](/BENENNE "BENENNE")                    | NAME FOREIGN FACTION?? faction??-no "name"   |                                                        | K           |
| [BENUTZE \[anzahl\] trank](/BENUTZE "BENUTZE")                                  | USE \[amount\] potion                        | benutzt alchemistischen Trank                          | K           |
| [BESCHREIBE EINHEIT "text"](/BESCHREIBE "BESCHREIBE")                           | DESCRIBE UNIT "text"                         | beschreibt Objekte                                     | K           |
| [BESCHREIBE PRIVAT "text"](/BESCHREIBE "BESCHREIBE")                            | DESCRIBE PRIVATE "text"                      |                                                        | K           |
| [BESCHREIBE GEBÄUDE "text"](/BESCHREIBE "BESCHREIBE")                           | DESCRIBE BUILDING "text"                     |                                                        | K           |
| [BESCHREIBE SCHIFF "text"](/BESCHREIBE "BESCHREIBE")                            | DESCRIBE SHIP "text"                         |                                                        | K           |
| [BESCHREIBE REGION "text"](/BESCHREIBE "BESCHREIBE")                            | DESCRIBE REGION "text"                       |                                                        | K           |
| [BETRETE GEBÄUDE gebäude-nr](/BETRETE "BETRETE")                                | ENTER BUILDING building-id                   | betritt Gebäude                                        | K           |
| [BETRETE SCHIFF schiff-nr](/BETRETE "BETRETE")                                  | ENTER SHIP ship-id                           | betritt Schiffe                                        | K           |
| [BEWACHE \[NICHT\]](/BEWACHE "BEWACHE")                                         | GUARD                                        | bewacht die Region                                     | K           |
| [BEZAHLE NICHT \[gebäude-nr\]](/BEZAHLE "BEZAHLE")                              | PAY \[NOT\]                                  | bezahlt den Unterhalt für ein Gebäude nicht            | K           |
| [BOTSCHAFT REGION "text"](/BOTSCHAFT "BOTSCHAFT")                               | MESSAGE REGION "text"                        | versendet Botschaften                                  | K           |
| [BOTSCHAFT SCHIFF schiff-nr "text"](/BOTSCHAFT "BOTSCHAFT")                     | MESSAGE SHIP ship-id "text"                  | versendet Botschaften                                  | K           |
| [BOTSCHAFT GEBÄUDE gebäude-nr "text"](/BOTSCHAFT "BOTSCHAFT")                   | MESSAGE BUILDING building-id "text"          | versendet Botschaften                                  | K           |
| [BOTSCHAFT EINHEIT einh-nr "text"](/BOTSCHAFT "BOTSCHAFT")                      | MESSAGE UNIT unit-id "text"                  |                                                        | K           |
| [BOTSCHAFT PARTEI partei-nr "text"](/BOTSCHAFT "BOTSCHAFT")                     | MESSAGE FACTION faction-id "text"            |                                                        | K           |
| [DEFAULT befehl](/DEFAULT "DEFAULT")                                            | DEFAULT                                      | Setzt Default-Befehl für die nächste Runde.            | K           |
| [EINHEIT einheit-nr](/EINHEIT "EINHEIT")                                        | UNIT unit-ID                                 | beginnt Befehle für eine Einheit                       | K           |
| [EMAIL email@adresse](/EMAIL "EMAIL")                                           | EMAIL email@adresse                          | setzt die eMail-Adresse                                | K           |
| [ENDE](/ENDE "ENDE")                                                            | END                                          | beendet MACHE TEMP                                     | K           |
| [ERESSEA partei-nr "passwort"](/ERESSEA "ERESSEA")                              | ERESSEA faction-id "password"                | beginnt Befehle für Partei                             | K           |
| [FAHRE einheit-nr](/FAHRE "FAHRE")                                              | RIDE unit-id                                 | sich transportieren lassen                             | L           |
| [FOLGE EINHEIT einheit-nr](/FOLGE "FOLGE")                                      | FOLLOW UNIT unit-id                          | folgt einer Einheit                                    | (L)\*\*     |
| [FOLGE SCHIFF schiff-nr](/FOLGE "FOLGE")                                        | FOLLOW SHIP ship-id                          | folgt einem Schiff                                     | (L)\*\*     |
| [FORSCHE KRÄUTER](/FORSCHE "FORSCHE")                                           | RESEARCH herbs                               | sucht Kräuter                                          | L           |
| [GIB einheit-nr KRÄUTER](/GIB "GIB")                                            | GIVE unit-id herbs\_name                     | gibt einer Einheit alle Kräuter                        | K           |
| [GIB einheit-nr KOMMANDO](/GIB "GIB")                                           | GIVE unit-id command                         | übergibt Kommando über Schiff/Gebäude                  | K           |
| [GIB einheit-nr EINHEIT](/GIB "GIB")                                            | GIVE unit-id UNIT                            | übergibt Einheit an fremde Partei                      | K           |
| [GIB einheit-nr \[JE\] anzahl PERSONEN](/GIB "GIB")                             | GIVE unit-id \[each\] amount MEN             | übergibt Personen                                      | K           |
| [GIB einheit-nr \[JE\] anzahl SCHIFF](/GIB "GIB")                               | GIVE unit-id \[each\] amount SHIP            | übergibt SCHIFF zur Bildung von Konvois                | K           |
| [GIB einheit-nr \[JE\] anzahl SILBER](/GIB "GIB")                               | GIVE unit-id \[each\] amount SILVER          | übergibt Silber                                        | K           |
| [GIB einheit-nr \[JE\] anzahl gegenstand](/GIB "GIB")                           | GIVE unit-id \[each\] amount item            | übergibt Gegenstände                                   | K           |
| [GIB 0 anzahl SILBER](/GIB "GIB")                                               | GIVE 0 number SILVER                         | wegwerfen von Gegenständen                             | K           |
| [GIB 0 anzahl PERSONEN](/GIB "GIB")                                             | GIVE 0 number MEN                            |                                                        | K           |
| [GIB 0 anzahl gegenstand](/GIB "GIB")                                           | GIVE 0 number item                           |                                                        | K           |
| [GRUPPE \["name"\]](/GRUPPE "GRUPPE")                                           | GROUP \["name"\]                             | Gruppieren von Einheiten                               | K           |
| [HELFE partei-nr ALLES \[NICHT\]](/HELFE "HELFE")                               | HELP faction-id ALL \[NOT\]                  | setze/lösche einseitige Allianz                        | K           |
| [HELFE partei-nr GIB \[NICHT\]](/HELFE "HELFE")                                 | HELP faction-id GIVE \[NOT\]                 |                                                        | K           |
| [HELFE partei-nr KÄMPFE \[NICHT\]](/HELFE "HELFE")                              | HELP faction-id COMBAT \[NOT\]               |                                                        | K           |
| [HELFE partei-nr BEWACHE \[NICHT\]](/HELFE "HELFE")                             | HELP faction-id GUARD \[NOT\]                |                                                        | K           |
| [HELFE partei-nr SILBER \[NICHT\]](/HELFE "HELFE")                              | HELP faction-id SILVER \[NOT\]               |                                                        | K           |
| [HELFE partei-nr PARTEITARNUNG \[NICHT\]](/HELFE "HELFE")                       | HELP faction-id FACTIONSTEALTH \[NOT\]       |                                                        | K           |
| [KÄMPFE](/K%C3%84MPFE "KÄMPFE")                                                 | COMBAT                                       | setzt Verhalten im Kampf                               | K           |
| [KÄMPFE AGGRESSIV](/K%C3%84MPFE "KÄMPFE")                                       | COMBAT AGGRESSIVE                            |                                                        | K           |
| [KÄMPFE DEFENSIV](/K%C3%84MPFE "KÄMPFE")                                        | COMBAT DEFENSIVE                             |                                                        | K           |
| [KÄMPFE FLIEHE](/K%C3%84MPFE "KÄMPFE")                                          | COMBAT FLEE                                  |                                                        | K           |
| [KÄMPFE HELFE \[NICHT\]](/K%C3%84MPFE "KÄMPFE")                                 | COMBAT HELP \[NOT\]                          | der Einheit wird im Kampf \[nicht\] geholfen           | K           |
| [KÄMPFE HINTEN](/K%C3%84MPFE "KÄMPFE")                                          | COMBAT REAR                                  |                                                        | K           |
| [KÄMPFE NICHT](/K%C3%84MPFE "KÄMPFE")                                           | COMBAT NOT                                   |                                                        | K           |
| [KAMPFZAUBER \[STUFE n\] "zauberspruch" \[NICHT\]](/KAMPFZAUBER "KAMPFZAUBER")  | COMBATSPELL \[level n\] "spell" \[NOT\]      | setzt Zauber für Kämpfe                                | K           |
| [KAUFE anzahl luxusgut](/KAUFE "KAUFE")                                         | BUY amount luxurygood                        | kaufe Luxusgüter                                       | L\*\*\*     |
| [KONTAKTIERE einheit-nr](/KONTAKTIERE "KONTAKTIERE")                            | CONTACT unit-no                              | kontaktiere fremde Einheiten                           | K           |
| [LEHRE einheit-nr \[einheit-nr etc.\]](/LEHRE "LEHRE")                          | TEACH unit-no                                | lehre Einheiten                                        | L           |
| [LERNE talent](/LERNE "LERNE")                                                  | LEARN skill                                  | Talent lernen                                          | L           |
| [LERNE AUTO talent](/LERNE_AUTO "LERNE AUTO")                                   | LEARN AUTO                                   | Talent lernen oder lehren                              | L           |
| [LOCALE en/de](/LOCALE "LOCALE")                                                | LOCALE en/de??                               | Zeigt die Sprache der Befehle an                       | K           |
| [MACHE TEMP unit-alias-nr \["name"\]](/MACHE "MACHE")                           | MAKE TEMP unit-alias-nr \["name"\]           | erschaffe neue Einheit                                 | K           |
| [MACHE \[stufe\] gebäude-typ \[gebäude-nr\]](/MACHE "MACHE")                    | MAKE \[level\] building-type \[building-ID\] | erweitere oder baue neues Gebäude                      | L           |
| [MACHE \[stufe\] SCHIFF \[schiff-nr\]](/MACHE "MACHE")                          | MAKE \[level\] SHIP \[ship-ID\]              | baue weiter am Schiff                                  | L           |
| [MACHE](/MACHE "MACHE")                                                         | MAKE                                         | baue weiter an Gebäude/Schiff                          | L           |
| [MACHE \[stufe\] BOOT](/MACHE "MACHE")                                          | MAKE \[level\] boat                          | baue neue Schiffe                                      | L           |
| [MACHE \[stufe\] LANGBOOT](/MACHE "MACHE")                                      | MAKE \[level\] longboat                      |                                                        | L           |
| [MACHE \[stufe\] DRACHENSCHIFF](/MACHE "MACHE")                                 | MAKE \[level\] dragonship                    |                                                        | L           |
| [MACHE \[stufe\] KARAVELLE](/MACHE "MACHE")                                     | MAKE \[level\] caravel                       |                                                        | L           |
| [MACHE \[stufe\] TRIREME](/MACHE "MACHE")                                       | MAKE \[level\] trireme                       |                                                        | L           |
| [MACHE \[stufe\] GALEONE](/MACHE "MACHE")                                       | MAKE \[level\] galleon                       |                                                        | L           |
| [MACHE \[stufe\] STRASSE richtung](/MACHE "MACHE")                              | MAKE \[level\] ROAD direction                | baue Straßen                                           | L           |
| [MACHE \[anzahl\] KRÄUTER](/MACHE "MACHE")                                      | MAKE \[amount\] HERBS                        | suche Kräuter der Region                               | L           |
| [MACHE \[anzahl\] trank](/MACHE "MACHE")                                        | MAKE \[amount\] POTIONS                      | mache einen alchemistischen Trank                      | L           |
| [MACHE \[anzahl\] gegenstand](/MACHE "MACHE")                                   | MAKE \[amount\] item                         | mache einen Gegenstand                                 | L           |
| [NACH richtung \[richtung etc.\]](/NACH "NACH")                                 | MOVE direction \[direction\]                 | Reisen                                                 | L           |
| [NÄCHSTER](/N%C3%84CHSTER "NÄCHSTER")                                           | NEXT                                         | Beendet Befehle                                        | K           |
| [NUMMER EINHEIT \[neue\_nr\]](/NUMMER "NUMMER")                                 | NUMBER UNIT \[newID\]                        | vergibt neue Nummer                                    | K           |
| [NUMMER GEBÄUDE \[neue\_nr\]](/NUMMER "NUMMER")                                 | NUMBER CASTLE \[newID\]                      |                                                        | K           |
| [NUMMER PARTEI \[neue\_nr\]](/NUMMER "NUMMER")                                  | NUMBER FACTION \[newID\]                     |                                                        | K           |
| [NUMMER SCHIFF \[neue\_nr\]](/NUMMER "NUMMER")                                  | NUMBER SHIP \[newID\]                        |                                                        | K           |
| [OPTION AUSWERTUNG \[NICHT\]](/OPTION "OPTION")                                 | OPTION                                       | verschiedene Optionen                                  | K           |
| [OPTION COMPUTER \[NICHT\]](/OPTION "OPTION")                                   | OPTION                                       |                                                        | K           |
| [OPTION ZIPPED \[NICHT\]](/OPTION "OPTION")                                     | OPTION                                       |                                                        | K           |
| [OPTION BZIP2 \[NICHT\]](/OPTION "OPTION")                                      | OPTION                                       |                                                        | K           |
| [OPTION SILBERPOOL \[NICHT\]](/OPTION "OPTION")                                 | OPTION                                       |                                                        | K           |
| [OPTION MATERIALPOOL \[NICHT\]](/OPTION "OPTION")                               | OPTION                                       |                                                        | K           |
| [OPTION ADRESSEN \[NICHT\]](/OPTION "OPTION")                                   | OPTION                                       |                                                        | K           |
| [OPTION ZUGVORLAGE \[NICHT\]](/OPTION "OPTION")                                 | OPTION                                       |                                                        | K           |
| [OPTION STATISTIK \[NICHT\]](/OPTION "OPTION")                                  | OPTION                                       |                                                        | K           |
| [OPTION TALENTVERSCHIEBUNG \[NICHT\]](/OPTION "OPTION")                         | OPTION                                       |                                                        | K           |
| [OPTION PUNKTE \[NICHT\]](/OPTION "OPTION")                                     | OPTION                                       |                                                        | K           |
| [PASSWORT "neues-passwort"](/PASSWORT "PASSWORT")                               | PASSWORD "new-password"                      | setze neues Passwort                                   | K           |
| [PFLANZE \[anzahl\] KRÄUTER](/PFLANZE "PFLANZE")                                | PLANT \[amount\] HERBS                       | pflanzt Kräuter                                        | L           |
| [PFLANZE \[anzahl\] BÄUME](/PFLANZE "PFLANZE")                                  | PLANT \[amount\] TREES                       | pflanzt Samen                                          | L           |
| [PFLANZE \[anzahl\] MALLORNSAMEN](/PFLANZE "PFLANZE")                           | PLANT \[amount\] "mallorn seeds"             | pflanzt Samen                                          | L           |
| [PFLANZE \[anzahl\] SAMEN](/PFLANZE "PFLANZE")                                  | PLANT \[amount\] SEEDS                       | pflanzt Samen                                          | L           |
| [PIRATERIE \[partei\_1\] \[partei\_2\] \[...\]](/PIRATERIE "PIRATERIE")         | PIRACY \[faction\_1\] \[faction\_2\]         | Piraterie setzen                                       | L           |
| [PRÄFIX \[präfix\]](/PR%C3%84FIX "PRÄFIX")                                      | PREFIX                                       | gibt der Rassenbezeichnung ein Präfix                  | K           |
| [REGION x,y](/REGION "REGION")                                                  | REGION x,y                                   | keine Funktion (nur für Tools)                         | K           |
| [REKRUTIERE anzahl](/REKRUTIERE "REKRUTIERE")                                   | RECRUIT amount                               | rekrutiere weitere Personen                            | K           |
| [RESERVIERE anzahl "gegenstand"](/RESERVIERE "RESERVIERE")                      | RESERVE amount item                          | Gegenstände reservieren                                | K           |
| [RESERVIERE anzahl SILBER](/RESERVIERE "RESERVIERE")                            | RESERVE amount silver                        | Silber reservieren                                     | K           |
| [ROUTE richtung \[richtung etc.\]](/ROUTE "ROUTE")                              | ROUTE direction \[direction etc.\]           | Reisen                                                 | L           |
| [SORTIERE VOR einheit-nr](/SORTIERE "SORTIERE")                                 | SORT BEFORE unit-id                          | Einheit in Report sortieren                            | K           |
| [SORTIERE HINTER einheit-nr](/SORTIERE "SORTIERE")                              | SORT AFTER unit-id                           |                                                        | K           |
| [SPIONIERE einheit-nr](/SPIONIERE "SPIONIERE")                                  | SPY unit-id                                  | Einheit ausspionieren                                  | L           |
| [SPRACHE en/de](/SPRACHE "SPRACHE")                                             | LANGUAGE                                     | Ändert die Sprache der Partei                          | K           |
| [STIRB "passwort" \[PARTEI partei-nr\]](/STIRB "STIRB")                         | QUIT "password"                              | aus dem Spiel ausscheiden                              | K           |
| [TARNE \[stufe\]](/TARNE "TARNE")                                               | HIDE \[level\]                               | Tarnstufe setzen                                       | K           |
| [TARNE rasse](/TARNE "TARNE")                                                   | HIDE \[race\]                                | Dämonen: als andere Rasse tarnen                       | K           |
| [TARNE PARTEI \[NICHT\]](/TARNE "TARNE")                                        | HIDE FACTION \[NOT\]                         | Parteizugehörigkeit verbergen (als "anonym" getarnt)   | K           |
| [TARNE PARTEI NUMMER nummer](/TARNE "TARNE")                                    | HIDE FACTION faction-ID                      | Parteizugehörigkeit tarnen (als andere Partei getarnt) | K           |
| [TRANSPORTIERE einheit-nr](/TRANSPORTIERE "TRANSPORTIERE")                      | CARRY unit-id                                | andere Einheiten mitnehmen                             | K           |
| [TREIBE \[betrag\]](/TREIBE "TREIBE")                                           | TAX \[amount\]                               | Steuern eintreiben (max. 20 S/Talentstufe)             | L           |
| [UNTERHALTE \[betrag\]](/UNTERHALTE "UNTERHALTE")                               | ENTERTAIN \[amount\]                         | verdiene 20 oder mehr Silber                           | L           |
| [URSPRUNG \[x y\]](/URSPRUNG "URSPRUNG")                                        | ORIGIN \[x y\]                               | setzt den Koordinaten-Ursprung                         | K           |
| [VERGISS talent](/VERGISS "VERGISS")                                            | FORGET skill                                 | vergißt das Talent                                     | K           |
| [VERKAUFE anzahl luxusgut](/VERKAUFE "VERKAUFE")                                | SELL \[amount\] \[ALL\] luxurygood           | verkaufe Luxusgüter                                    | (L)\*\*\*\* |
| [VERLASSE](/VERLASSE "VERLASSE")                                                | LEAVE                                        | Schiff oder Gebäude verlassen                          | K           |
| [ZAUBERE \[REGION x y\] \[STUFE n\] "zauberspruch" \[...\]](/ZAUBERE "ZAUBERE") | CAST \[REGION x y\] \[level n\] "spell"      | Zaubern                                                | (L)         |
| [ZEIGE "zauberspruch"](/ZEIGE "ZEIGE")                                          | SHOW                                         | Zeige Beschreibung des Zaubers                         | K           |
| [ZERSTÖRE](/ZERST%C3%96RE "ZERSTÖRE")                                           | DESTROY                                      | Gebäude, Schiff oder Straße                            | L           |
| [ZÜCHTE PFERDE](/Z%C3%9CCHTE "ZÜCHTE")                                          | GROW HORSES                                  | Pferde züchten - nur in Pferdezucht                    | L           |
| [ZÜCHTE KRÄUTER](/Z%C3%9CCHTE "ZÜCHTE")                                         | GROW HERBS                                   | Kräuter züchten                                        | L           |
| [ZÜCHTE BÄUME](/Z%C3%9CCHTE "ZÜCHTE")                                           | GROW TREES                                   | Samen pflanzen                                         | L           |

\* siehe [Kampfende]; \*\*bewegt sich die verfolgte Einheit nicht, kann stattdessen ein anderer langer Befehl ausgeführt werden; \*\*\*kann mit VERKAUFE kombiniert werden; \*\*\*\*kann mit KAUFE kombiniert werden

## Siehe auch

- [Befehle]
- [Befehlsreihenfolge]

|              |                                                 |
|--------------|-------------------------------------------------|
| Weiterlesen: | [Der erste Zug](/Der_erste_Zug "Der erste Zug") |

<!-- From [https://wiki.eressea.de/index.php?title=Diskussion:Kurzbeschreibung&oldid=8099] -->

  [Befehl]: ./commands.md "Befehl"
  [Kampfende]: ./war.md#kampfende "Kampfende"
  [Befehle]: ./commands.md "Befehle"
  [Befehlsreihenfolge]: ./commands-sequence.md "Befehlsreihenfolge"
