---
# cSpell:locale de
alias: kurzbeschreibung
---

# Kurzbeschreibung

Unter `K`/`L` ist vermerkt, ob der [befehl][befehl] ein [kurzer][kurze-und-lange-befehle] oder [langer][kurze-und-lange-befehle] Befehl ist.
Eine Einheit kann pro Runde nur einen langen Befehl ausführen, aber beliebig viele kurze.

`PL` bezeichnet einen [pseudolangen Befehl][befehl], der einer Einheit mehrfach gegeben werden kann.
Allerdings kann kein weiterer anderer langer Befehl ausgeführt werden.
Näheres dazu ist auf der Seite des jeweiligen Befehls nachzulesen.

Kurzliste der Befehle.  

<!-- A link containing brackets (e.g. [BEWACHE \[NICHT\]) cannot be used as a reference link -->
<!-- instead, replace by HTML escape codes (e.g. [BEWACHE &#91;NICHT&#93;) or use inline link [...](<link>) -->

| Befehl                                                                   | Beschreibung                                           | K/L    |
|--------------------------------------------------------------------------|--------------------------------------------------------|--------|
| [//]                                                                     | bleibender Kommentar                                   | K      |
| [ARBEITE][bef-arbeite]                                                   | verdient 10 Silber oder mehr                           | L      |
| [ATTACKIERE einheit-nr][bef-attackiere]                                  | greift die Einheit an                                  | PL[^1] |
| [BANNER "text"]                                                          | setzt Text für Adressliste                             | K      |
| [BEANSPRUCHE anzahl gegenstand]                                          | holt Gegenstände aus Parteipool                        | K      |
| [BEFOERDERE][bef-befordere-id]                                           | macht Einheit zu Helden                                | K      |
| [BEKLAUE einheit-nr]                                                     | klaut 50 Silber oder mehr                              | L      |
| [BENENNE EINHEIT "name"][bef-benenne]                                    | benennt Objekte                                        | K      |
| [BENENNE PARTEI "name"][bef-benenne]                                     |                                                        | K      |
| [BENENNE GEBÄUDE "name"][bef-benenne]                                    |                                                        | K      |
| [BENENNE SCHIFF "name"][bef-benenne]                                     |                                                        | K      |
| [BENENNE REGION "name"][bef-benenne]                                     |                                                        | K      |
| [BENENNE FREMDE EINHEIT einheit "name"][bef-benenne]                     | benennt fremde und unbenannte Objekte                  | K      |
| [BENENNE FREMDES SCHIFF schiff "name"][bef-benenne]                      |                                                        | K      |
| [BENENNE FREMDES GEBÄUDE gebäude "name"][bef-benenne]                    |                                                        | K      |
| [BENENNE FREMDE PARTEI partei "name"][bef-benenne]                       |                                                        | K      |
| [BENUTZE &#91;anzahl&#93; trank]                                         | benutzt alchemistischen Trank                          | K      |
| [BESCHREIBE EINHEIT "text"][bef-beschreibe]                              | beschreibt Objekte                                     | K      |
| [BESCHREIBE PRIVAT "text"][bef-beschreibe]                               |                                                        | K      |
| [BESCHREIBE GEBÄUDE "text"][bef-beschreibe]                              |                                                        | K      |
| [BESCHREIBE SCHIFF "text"][bef-beschreibe]                               |                                                        | K      |
| [BESCHREIBE REGION "text"][bef-beschreibe]                               |                                                        | K      |
| [BETRETE GEBÄUDE gebäude-nr][bef-betrete]                                | betritt Gebäude                                        | K      |
| [BETRETE SCHIFF schiff-nr][bef-betrete]                                  | betritt Schiffe                                        | K      |
| [BEWACHE &#91;NICHT&#93;][bef-bewache]                                   | bewacht die Region                                     | K      |
| [BEZAHLE NICHT \[gebäude-nr\]][bef-bezahle-nicht]                        | bezahlt den Unterhalt für ein Gebäude nicht            | K      |
| [BOTSCHAFT REGION "text"][bef-botschaft]                                 | versendet Botschaften                                  | K      |
| [BOTSCHAFT SCHIFF schiff-nr "text"][bef-botschaft]                       | versendet Botschaften                                  | K      |
| [BOTSCHAFT GEBÄUDE gebäude-nr "text"][bef-botschaft]                     | versendet Botschaften                                  | K      |
| [BOTSCHAFT EINHEIT einh-nr "text"][bef-botschaft]                        |                                                        | K      |
| [BOTSCHAFT PARTEI partei-nr "text"][bef-botschaft]                       |                                                        | K      |
| [DEFAULT "befehl"]                                                       | setzt Default-Befehl für die nächste Runde.            | K      |
| [EINHEIT einheit-nr]                                                     | beginnt Befehle für eine Einheit                       | K      |
| [EMAIL email@adresse]                                                    | setzt die E-Mail-Adresse                               | K      |
| [ENDE][bef-ende]                                                         | beendet MACHE TEMP                                     | K      |
| [ERESSEA partei-nr "passwort"]                                           | beginnt Befehle für Partei                             | K      |
| [FAHRE einheit-nr][bef-fahre]                                            | sich transportieren lassen                             | L      |
| [FOLGE EINHEIT einheit-nr]                                               | folgt einer Einheit                                    | PL[^2] |
| [FOLGE SCHIFF schiff-nr]                                                 | folgt einem Schiff                                     | PL[^2] |
| [FORSCHE KRÄUTER]                                                        | sucht Kräuter                                          | L      |
| [GIB einheit-nr KRÄUTER][bef-gib]                                        | gibt einer Einheit alle Kräuter                        | K      |
| [GIB einheit-nr KOMMANDO][bef-gib]                                       | übergibt Kommando über Schiff/Gebäude                  | K      |
| [GIB einheit-nr EINHEIT][bef-gib]                                        | übergibt Einheit an fremde Partei                      | K      |
| [GIB einheit-nr \[JE\] anzahl PERSONEN][bef-gib]                         | übergibt Personen                                      | K      |
| [GIB einheit-nr \[JE\] anzahl SCHIFF][bef-gib]                           | übergibt SCHIFF zur Bildung von Konvois                | K      |
| [GIB einheit-nr \[JE\] anzahl SILBER][bef-gib]                           | übergibt Silber                                        | K      |
| [GIB einheit-nr \[JE\] anzahl gegenstand][bef-gib]                       | übergibt Gegenstände                                   | K      |
| [GIB 0 anzahl SILBER][bef-gib]                                           | gibt Gegenstände an die Bauern                         | K      |
| [GIB 0 anzahl PERSONEN][bef-gib]                                         |                                                        | K      |
| [GIB 0 anzahl gegenstand][bef-gib]                                       |                                                        | K      |
| [GRUPPE \["name"\]][bef-gruppe]                                          | Gruppieren von Einheiten                               | K      |
| [HELFE partei-nr ALLES \[NICHT\]][bef-helfe]                             | setzt / löscht einseitige Allianz                      | K      |
| [HELFE partei-nr GIB \[NICHT\]][bef-helfe]                               |                                                        | K      |
| [HELFE partei-nr KÄMPFE \[NICHT\]][bef-helfe]                            |                                                        | K      |
| [HELFE partei-nr BEWACHE \[NICHT\]][bef-helfe]                           |                                                        | K      |
| [HELFE partei-nr SILBER \[NICHT\]][bef-helfe]                            |                                                        | K      |
| [HELFE partei-nr PARTEITARNUNG \[NICHT\]][bef-helfe]                     |                                                        | K      |
| [KÄMPFE][bef-kampfe-id]                                                  | setzt Verhalten im Kampf                               | K      |
| [KÄMPFE AGGRESSIV][bef-kampfe-id]                                        |                                                        | K      |
| [KÄMPFE DEFENSIV][bef-kampfe-id]                                         |                                                        | K      |
| [KÄMPFE FLIEHE][bef-kampfe-id]                                           |                                                        | K      |
| [KÄMPFE HELFE \[NICHT\]][bef-kampfe-id]                                  | der Einheit wird im Kampf \[nicht\] geholfen           | K      |
| [KÄMPFE HINTEN][bef-kampfe-id]                                           |                                                        | K      |
| [KÄMPFE NICHT][bef-kampfe-id]                                            |                                                        | K      |
| [KAMPFZAUBER \[STUFE n\] "zauberspruch" \[NICHT\]][bef-kampfzauber]      | setzt Zauber für Kämpfe                                | K      |
| [KAUFE anzahl luxusgut]                                                  | kaufe Luxusgüter                                       | PL[^3] |
| [KONTAKTIERE einheit-nr]                                                 | kontaktiere fremde Einheiten                           | K      |
| [LEHRE einheit-nr \[einheit-nr etc.\]][bef-lehre]                        | lehre Einheiten                                        | L      |
| [LERNE talent][bef-lerne]                                                | Talent lernen                                          | L      |
| [LERNE AUTO talent][bef-lerne-auto]                                      | Talent lernen oder lehren                              | L      |
| [LOCALE en/de]                                                           | zeigt die Sprache der Befehle an                       | K      |
| [MACHE TEMP unit-alias-nr \["name"\]][bef-mache]                         | erschaffe neue Einheit                                 | K      |
| [MACHE \[stufe\] gebäude-typ \[gebäude-nr\]][bef-mache]                  | erweitere oder baue neues Gebäude                      | L      |
| [MACHE \[stufe\] schiffstyp][bef-mache]                                  | baue neue Schiffe                                      | L      |
| [MACHE \[stufe\] SCHIFF \[schiff-nr\]][bef-mache]                        | baue weiter am Schiff                                  | L      |
| [MACHE TEMP][bef-mache]                                                  | baue weiter an Gebäude/Schiff                          | L      |
| [MACHE \[stufe\] STRASSE richtung][bef-mache]                            | baue Straßen                                           | L      |
| [MACHE \[anzahl\] KRÄUTER][bef-mache]                                    | suche Kräuter der Region                               | L      |
| [MACHE \[anzahl\] trank][bef-mache]                                      | mache einen alchemistischen Trank                      | L      |
| [MACHE \[anzahl\] gegenstand][bef-mache]                                 | mache einen Gegenstand oder baue Rohstoffe ab          | L      |
| [NACH richtung \[richtung etc.\]][bef-mache]                             | reisen                                                 | L      |
| [NÄCHSTER][bef-nachster-id]                                              | beendet Befehle                                        | K      |
| [NUMMER EINHEIT \[neue\_nr\]][bef-nummer]                                | vergibt neue Nummer                                    | K      |
| [NUMMER GEBÄUDE \[neue\_nr\]][bef-nummer]                                |                                                        | K      |
| [NUMMER PARTEI \[neue\_nr\]][bef-nummer]                                 |                                                        | K      |
| [NUMMER SCHIFF \[neue\_nr\]][bef-nummer]                                 |                                                        | K      |
| [OPTION AUSWERTUNG \[NICHT\]][bef-option]                                | verschiedene Einstellungen                             | K      |
| [OPTION COMPUTER \[NICHT\]][bef-option]                                  |                                                        | K      |
| [OPTION ZIPPED \[NICHT\]][bef-option]                                    |                                                        | K      |
| [OPTION BZIP2 \[NICHT\]][bef-option]                                     |                                                        | K      |
| [OPTION SILBERPOOL \[NICHT\]][bef-option]                                |                                                        | K      |
| [OPTION MATERIALPOOL \[NICHT\]][bef-option]                              |                                                        | K      |
| [OPTION ADRESSEN \[NICHT\]][bef-option]                                  |                                                        | K      |
| [OPTION ZUGVORLAGE \[NICHT\]][bef-option]                                |                                                        | K      |
| [OPTION STATISTIK \[NICHT\]][bef-option]                                 |                                                        | K      |
| [OPTION TALENTVERSCHIEBUNG \[NICHT\]][bef-option]                        |                                                        | K      |
| [OPTION PUNKTE \[NICHT\]][bef-option]                                    |                                                        | K      |
| [PASSWORT "neues-passwort"]                                              | setzt neues Passwort                                   | K      |
| [PFLANZE \[anzahl\] KRÄUTER][bef-pflanze]                                | pflanzt Kräuter                                        | L      |
| [PFLANZE \[anzahl\] BÄUME][bef-pflanze]                                  | pflanzt Samen                                          | L      |
| [PFLANZE \[anzahl\] MALLORNSAMEN][bef-pflanze]                           | pflanzt Samen                                          | L      |
| [PFLANZE \[anzahl\] SAMEN][bef-pflanze]                                  | pflanzt Samen                                          | L      |
| [PIRATERIE \[partei\_1\] \[partei\_2\] \[...\]][bef-piraterie]           | Piraterie setzen                                       | L      |
| [PRÄFIX \[präfix\]][bef-prafix-id]                                       | gibt der Rassenbezeichnung ein Präfix                  | K      |
| [REGION x,y]                                                             | keine Funktion (nur für Tools)                         | K      |
| [REKRUTIERE anzahl]                                                      | rekrutiert weitere Personen                            | K      |
| [RESERVIERE anzahl "gegenstand"][bef-reserviere]                         | Gegenstände reservieren                                | K      |
| [RESERVIERE anzahl SILBER][bef-reserviere]                               | Silber reservieren                                     | K      |
| [ROUTE richtung \[richtung etc.\]][bef-route]                            | reisen                                                 | L      |
| [SORTIERE VOR einheit-nr][bef-sortiere]                                  | Einheit in Report sortieren                            | K      |
| [SORTIERE HINTER einheit-nr][bef-sortiere]                               |                                                        | K      |
| [SPIONIERE einheit-nr]                                                   | Einheit ausspionieren                                  | L      |
| [SPRACHE en/de]                                                          | ändert die Sprache der Partei                          | K      |
| [STIRB "passwort" \[PARTEI partei-nr\]][bef-stirb]                       | aus dem Spiel ausscheiden                              | K      |
| [TARNE \[stufe\]][bef-tarne]                                             | Tarnstufe setzen                                       | K      |
| [TARNE rasse][bef-tarne]                                                 | Dämonen: als andere Rasse tarnen                       | K      |
| [TARNE PARTEI \[NICHT\]][bef-tarne]                                      | Parteizugehörigkeit verbergen (als "anonym" getarnt)   | K      |
| [TARNE PARTEI NUMMER nummer][bef-tarne]                                  | Parteizugehörigkeit tarnen (als andere Partei getarnt) | K      |
| [TRANSPORTIERE einheit-nr]                                               | andere Einheiten mitnehmen                             | K      |
| [TREIBE \[betrag\]]                                                      | Steuern eintreiben                                     | L      |
| [UNTERHALTE \[betrag\]][bef-unterhalte]                                  | verdient 20 oder mehr Silber                           | L      |
| [URSPRUNG x y]                                                           | setzt den Koordinaten-Ursprung                         | K      |
| [VERGISS talent]                                                         | vergisst das Talent                                    | K      |
| [VERKAUFE anzahl luxusgut]                                               | verkauft Luxusgüter                                    | PL[^3] |
| [VERKAUFE ALLES luxusgut]                                                |                                                        |        |
| [VERLASSE][bef-verlasse]                                                 | Schiff oder Gebäude verlassen                          | K      |
| [ZAUBERE \[REGION x y\] \[STUFE n\] "zauberspruch" \[...\]][bef-zaubere] | Zaubern                                                | PL[^4] |
| [ZEIGE ALLE ZAUBER][bef-zeige]                                           | zeigt Beschreibung aller bekannten Zauber              | K      |
| [ZEIGE ALLE TRÄNKE][bef-zeige]                                           | zeigt Beschreibung aller bekannten Tränke              | K      |
| [ZEIGE "Gegenstand"][bef-zeige]                                          | zeigt Beschreibung eines Gegenstands                   | K      |
| [ZEIGE "Trank"][bef-zeige]                                               | zeigt Beschreibung des Tranks                          | K      |
| [ZEIGE "Zauberspruch"][bef-zeige]                                        | zeigt Beschreibung des Zaubers                         | K      |
| [ZEIGE "Rasse"][bef-zeige]                                               | zeigt Beschreibung der Rasse der Einheit               | K      |
| [ZERSTÖRE \[stufen\]][bef-zerstore-id]                                   | Gebäude oder Schiff verkleinern                        | L      |
| [ZERSTÖRE \[stufen\] STRASSE richtung][bef-zerstore-id]                  | Straße einreißen                                       | L      |
| [ZÜCHTE PFERDE][bef-zuchte-id]                                           | Pferde züchten - nur in Pferdezucht                    | L      |

[^1]: der Befehl ist nicht immer lang, siehe [Kampfende][das-ende]  
[^2]: bewegt sich die verfolgte Einheit nicht, kann stattdessen ein anderer langer Befehl ausgeführt werden  
[^3]: ein KAUFE- und mehrere VERKAUFE-Befehle können kombiniert werden  
[^4]: eine Einheit kann mehrere Zauber ausführen  

## Siehe auch

- [Befehle][befehl]
- [Befehlsreihenfolge][befehlsreihenfolge]

Weiterlesen: [Der erste Zug][der-erste-zug].

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[//]: [[bef-kommentar-mit-schraegstrichen]]

[BANNER "text"]: [[bef-banner]]
[BEANSPRUCHE anzahl gegenstand]: [[bef-beanspruche]]
[BEKLAUE einheit-nr]: [[bef-beklaue]]
[DEFAULT "befehl"]: [[bef-default]]
[EINHEIT einheit-nr]: [[bef-einheit]]
[EMAIL email@adresse]: [[bef-email]]
[ERESSEA partei-nr "passwort"]: [[bef-eressea]]
[FOLGE EINHEIT einheit-nr]: [[bef-folge]]
[FOLGE SCHIFF schiff-nr]: [[bef-folge]]
[FORSCHE KRÄUTER]: [[bef-forsche]]
[KAUFE anzahl luxusgut]: [[bef-kaufe]]
[KONTAKTIERE einheit-nr]: [[bef-kontaktiere]]
[LOCALE en/de]: [[bef-locale]]
[PASSWORT "neues-passwort"]: [[bef-passwort]]
[REGION x,y]: [[bef-region]]
[REKRUTIERE anzahl]: [[bef-rekrutiere]]
[SPIONIERE einheit-nr]: [[bef-spioniere]]
[SPRACHE en/de]: [[bef-sprache]]
[TRANSPORTIERE einheit-nr]: [[bef-transportiere]]
[TREIBE \[betrag\]]: [[bef-treibe]]
[URSPRUNG x y]: [[bef-ursprung]]
[VERGISS talent]: [[bef-vergiss]]
[VERKAUFE anzahl luxusgut]: [[bef-verkaufe]]
[VERKAUFE ALLES luxusgut]: [[bef-verkaufe]]
[BENUTZE &#91;anzahl&#93; trank]: [[bef-benutze]]

[bef-arbeite]: [[bef-arbeite]]
[bef-attackiere]: [[bef-attackiere]]
[bef-benenne]: [[bef-benenne]]
[bef-beschreibe]: [[bef-beschreibe]]
[bef-betrete]: [[bef-betrete]]
[bef-bewache]: [[bef-bewache]]
[bef-bezahle-nicht]: [[bef-bezahle-nicht]]
[bef-botschaft]: [[bef-botschaft]]
[bef-ende]: [[bef-ende]]
[bef-fahre]: [[bef-fahre]]
[bef-gib]: [[bef-gib]]
[bef-gruppe]: [[bef-gruppe]]
[bef-helfe]: [[bef-helfe]]
[bef-kampfzauber]: [[bef-kampfzauber]]
[bef-lehre]: [[bef-lehre]]
[bef-lerne]: [[bef-lerne]]
[bef-lerne-auto]: [[bef-lerne-auto]]
[bef-mache]: [[bef-mache]]
[bef-nummer]: [[bef-nummer]]
[bef-option]: [[bef-option]]
[bef-pflanze]: [[bef-pflanze]]
[bef-piraterie]: [[bef-piraterie]]
[bef-reserviere]: [[bef-reserviere]]
[bef-route]: [[bef-route]]
[bef-sortiere]: [[bef-sortiere]]
[bef-stirb]: [[bef-stirb]]
[bef-tarne]: [[bef-tarne]]
[bef-verlasse]: [[bef-verlasse]]
[bef-unterhalte]: [[bef-unterhalte]]
[bef-zaubere]: [[bef-zaubere]]
[bef-zeige]: [[bef-zeige]]
