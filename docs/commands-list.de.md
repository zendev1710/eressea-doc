---
# cSpell:locale de
alias: kurzbeschreibung
---
# Kurzbeschreibung

Unter "K/L" ist vermerkt, ob der [Befehl] ein kurzer oder langer Befehl ist. Eine Einheit kann pro Runde nur einen langen Befehl ausführen, aber beliebig viele kurze.

[<sup>(l)</sup>] bezeichnet einen [pseudolangen Befehl][Befehl], der einer Einheit mehrfach gegeben werden kann. Allerdings kann kein weiterer anderer langer Befehl ausgeführt werden. Näheres dazu ist auf der Seite des jeweiligen Befehls nachzulesen.

Kurzliste der Befehle

| Befehl                                                      | Beschreibung                                           | K/L     |
|-------------------------------------------------------------|--------------------------------------------------------|---------|
| [//]                                                        | bleibender Kommentar                                   | [K]     |
| [[bef-arbeite]]                                             | verdient 10 Silber oder mehr                           | [L]     |
| [ATTACKIERE einheit-nr]                                     | greift die Einheit an                                  | [(l)] 1 |
| [BANNER "text"]                                             | setzt Text für Adressliste                             | [K]     |
| [BEANSPRUCHE anzahl gegenstand]                             | holt Gegenstände aus Parteipool                        | [K]     |
| [[bef-befoerdere]]                                          | macht Einheit zu Helden                                | [K]     |
| [BEKLAUE einheit-nr]                                        | klaut 50 Silber oder mehr                              | [L]     |
| [BENENNE EINHEIT "name"]                                    | benennt Objekte                                        | [K]     |
| [BENENNE PARTEI "name"]                                     |                                                        | [K]     |
| [BENENNE GEBÄUDE "name"]                                    |                                                        | [K]     |
| [BENENNE SCHIFF "name"]                                     |                                                        | [K]     |
| [BENENNE REGION "name"]                                     |                                                        | [K]     |
| [BENENNE FREMDE EINHEIT einheit "name"]                     | benennt fremde und unbenannte Objekte                  | [K]     |
| [BENENNE FREMDES SCHIFF schiff "name"]                      |                                                        | [K]     |
| [BENENNE FREMDES GEBÄUDE gebäude "name"]                    |                                                        | [K]     |
| [BENENNE FREMDE PARTEI partei "name"]                       |                                                        | [K]     |
| [BENUTZE \[anzahl\] trank]                                  | benutzt alchemistischen Trank                          | [K]     |
| [BESCHREIBE EINHEIT "text"]                                 | beschreibt Objekte                                     | [K]     |
| [BESCHREIBE PRIVAT "text"]                                  |                                                        | [K]     |
| [BESCHREIBE GEBÄUDE "text"]                                 |                                                        | [K]     |
| [BESCHREIBE SCHIFF "text"]                                  |                                                        | [K]     |
| [BESCHREIBE REGION "text"]                                  |                                                        | [K]     |
| [BETRETE GEBÄUDE gebäude-nr]                                | betritt Gebäude                                        | [K]     |
| [BETRETE SCHIFF schiff-nr]                                  | betritt Schiffe                                        | [K]     |
| [BEWACHE \[NICHT\]]                                         | bewacht die Region                                     | [K]     |
| [BEZAHLE NICHT \[gebäude-nr\]]                              | bezahlt den Unterhalt für ein Gebäude nicht            | [K]     |
| [BOTSCHAFT REGION "text"]                                   | versendet Botschaften                                  | [K]     |
| [BOTSCHAFT SCHIFF schiff-nr "text"]                         | versendet Botschaften                                  | [K]     |
| [BOTSCHAFT GEBÄUDE gebäude-nr "text"]                       | versendet Botschaften                                  | [K]     |
| [BOTSCHAFT EINHEIT einh-nr "text"]                          |                                                        | [K]     |
| [BOTSCHAFT PARTEI partei-nr "text"]                         |                                                        | [K]     |
| [DEFAULT "befehl"]                                          | setzt Default-Befehl für die nächste Runde.            | [K]     |
| [EINHEIT einheit-nr]                                        | beginnt Befehle für eine Einheit                       | [K]     |
| [EMAIL email@adresse]                                       | setzt die E-Mail-Adresse                               | [K]     |
| [[bef-ende]]                                                | beendet MACHE TEMP                                     | [K]     |
| [ERESSEA partei-nr "passwort"]                              | beginnt Befehle für Partei                             | [K]     |
| [FAHRE einheit-nr]                                          | sich transportieren lassen                             | [L]     |
| [FOLGE EINHEIT einheit-nr]                                  | folgt einer Einheit                                    | [(l)] 2 |
| [FOLGE SCHIFF schiff-nr]                                    | folgt einem Schiff                                     | [(l)] 2 |
| [FORSCHE KRÄUTER]                                           | sucht Kräuter                                          | [L]     |
| [GIB einheit-nr KRÄUTER]                                    | gibt einer Einheit alle Kräuter                        | [K]     |
| [GIB einheit-nr KOMMANDO]                                   | übergibt Kommando über Schiff/Gebäude                  | [K]     |
| [GIB einheit-nr EINHEIT]                                    | übergibt Einheit an fremde Partei                      | [K]     |
| [GIB einheit-nr \[JE\] anzahl PERSONEN]                     | übergibt Personen                                      | [K]     |
| [GIB einheit-nr \[JE\] anzahl SCHIFF]                       | übergibt SCHIFF zur Bildung von Konvois                | [K]     |
| [GIB einheit-nr \[JE\] anzahl SILBER]                       | übergibt Silber                                        | [K]     |
| [GIB einheit-nr \[JE\] anzahl gegenstand]                   | übergibt Gegenstände                                   | [K]     |
| [GIB 0 anzahl SILBER]                                       | gibt Gegenstände an die Bauern                         | [K]     |
| [GIB 0 anzahl PERSONEN]                                     |                                                        | [K]     |
| [GIB 0 anzahl gegenstand]                                   |                                                        | [K]     |
| [GRUPPE \["name"\]]                                         | Gruppieren von Einheiten                               | [K]     |
| [HELFE partei-nr ALLES \[NICHT\]]                           | setzt / löscht einseitige Allianz                      | [K]     |
| [HELFE partei-nr GIB \[NICHT\]]                             |                                                        | [K]     |
| [HELFE partei-nr KÄMPFE \[NICHT\]]                          |                                                        | [K]     |
| [HELFE partei-nr BEWACHE \[NICHT\]]                         |                                                        | [K]     |
| [HELFE partei-nr SILBER \[NICHT\]]                          |                                                        | [K]     |
| [HELFE partei-nr PARTEITARNUNG \[NICHT\]]                   |                                                        | [K]     |
| [KÄMPFE]                                                    | setzt Verhalten im Kampf                               | K       |
| [KÄMPFE AGGRESSIV]                                          |                                                        | [K]     |
| [KÄMPFE DEFENSIV]                                           |                                                        | [K]     |
| [KÄMPFE FLIEHE]                                             |                                                        | [K]     |
| [KÄMPFE HELFE \[NICHT\]]                                    | der Einheit wird im Kampf \[nicht\] geholfen           | [K]     |
| [KÄMPFE HINTEN]                                             |                                                        | [K]     |
| [KÄMPFE NICHT]                                              |                                                        | [K]     |
| [KAMPFZAUBER \[STUFE n\] "zauberspruch" \[NICHT\]]          | setzt Zauber für Kämpfe                                | [K]     |
| [KAUFE anzahl luxusgut]                                     | kaufe Luxusgüter                                       | [(l)] 3 |
| [KONTAKTIERE einheit-nr]                                    | kontaktiere fremde Einheiten                           | [K]     |
| [LEHRE einheit-nr \[einheit-nr etc.\]]                      | lehre Einheiten                                        | [L]     |
| [LERNE talent]                                              | Talent lernen                                          | [L]     |
| [LERNE AUTO talent]                                         | Talent lernen oder lehren                              | [L]     |
| [LOCALE en/de]                                              | zeigt die Sprache der Befehle an                       | [K]     |
| [MACHE TEMP unit-alias-nr \["name"\]]                       | erschaffe neue Einheit                                 | [K]     |
| [MACHE \[stufe\] gebäude-typ \[gebäude-nr\]]                | erweitere oder baue neues Gebäude                      | [L]     |
| [MACHE \[stufe\] schiffstyp]                                | baue neue Schiffe                                      | [L]     |
| [MACHE \[stufe\] SCHIFF \[schiff-nr\]]                      | baue weiter am Schiff                                  | [L]     |
| [[bef-mache]]                                               | baue weiter an Gebäude/Schiff                          | [L]     |
| [MACHE \[stufe\] STRASSE richtung]                          | baue Straßen                                           | [L]     |
| [MACHE \[anzahl\] KRÄUTER]                                  | suche Kräuter der Region                               | [L]     |
| [MACHE \[anzahl\] trank]                                    | mache einen alchemistischen Trank                      | [L]     |
| [MACHE \[anzahl\] gegenstand]                               | mache einen Gegenstand oder baue Rohstoffe ab          | [L]     |
| [NACH richtung \[richtung etc.\]]                           | reisen                                                 | [L]     |
| [NÄCHSTER]                                                  | beendet Befehle                                        | [K]     |
| [NUMMER EINHEIT \[neue\_nr\]]                               | vergibt neue Nummer                                    | [K]     |
| [NUMMER GEBÄUDE \[neue\_nr\]]                               |                                                        | [K]     |
| [NUMMER PARTEI \[neue\_nr\]]                                |                                                        | [K]     |
| [NUMMER SCHIFF \[neue\_nr\]]                                |                                                        | [K]     |
| [OPTION AUSWERTUNG \[NICHT\]]                               | verschiedene Einstellungen                             | [K]     |
| [OPTION COMPUTER \[NICHT\]]                                 |                                                        | [K]     |
| [OPTION ZIPPED \[NICHT\]]                                   |                                                        | [K]     |
| [OPTION BZIP2 \[NICHT\]]                                    |                                                        | [K]     |
| [OPTION SILBERPOOL \[NICHT\]]                               |                                                        | [K]     |
| [OPTION MATERIALPOOL \[NICHT\]]                             |                                                        | [K]     |
| [OPTION ADRESSEN \[NICHT\]]                                 |                                                        | [K]     |
| [OPTION ZUGVORLAGE \[NICHT\]]                               |                                                        | [K]     |
| [OPTION STATISTIK \[NICHT\]]                                |                                                        | [K]     |
| [OPTION TALENTVERSCHIEBUNG \[NICHT\]]                       |                                                        | [K]     |
| [OPTION PUNKTE \[NICHT\]]                                   |                                                        | [K]     |
| [PASSWORT "neues-passwort"]                                 | setzt neues Passwort                                   | [K]     |
| [PFLANZE \[anzahl\] KRÄUTER]                                | pflanzt Kräuter                                        | [L]     |
| [PFLANZE \[anzahl\] BÄUME]                                  | pflanzt Samen                                          | [L]     |
| [PFLANZE \[anzahl\] MALLORNSAMEN]                           | pflanzt Samen                                          | [L]     |
| [PFLANZE \[anzahl\] SAMEN]                                  | pflanzt Samen                                          | [L]     |
| [PIRATERIE \[partei\_1\] \[partei\_2\] \[...\]]             | Piraterie setzen                                       | [L]     |
| [PRÄFIX \[präfix\]]                                         | gibt der Rassenbezeichnung ein Präfix                  | [K]     |
| [REGION x,y]                                                | keine Funktion (nur für Tools)                         | [K]     |
| [REKRUTIERE anzahl]                                         | rekrutiert weitere Personen                            | [K]     |
| [RESERVIERE anzahl "gegenstand"]                            | Gegenstände reservieren                                | [K]     |
| [RESERVIERE anzahl SILBER]                                  | Silber reservieren                                     | [K]     |
| [ROUTE richtung \[richtung etc.\]]                          | reisen                                                 | [L]     |
| [SORTIERE VOR einheit-nr]                                   | Einheit in Report sortieren                            | [K]     |
| [SORTIERE HINTER einheit-nr]                                |                                                        | [K]     |
| [SPIONIERE einheit-nr]                                      | Einheit ausspionieren                                  | [L]     |
| [SPRACHE en/de]                                             | ändert die Sprache der Partei                          | [K]     |
| [STIRB "passwort" \[PARTEI partei-nr\]]                     | aus dem Spiel ausscheiden                              | [K]     |
| [TARNE \[stufe\]]                                           | Tarnstufe setzen                                       | [K]     |
| [TARNE rasse]                                               | Dämonen: als andere Rasse tarnen                       | [K]     |
| [TARNE PARTEI \[NICHT\]]                                    | Parteizugehörigkeit verbergen (als "anonym" getarnt)   | [K]     |
| [TARNE PARTEI NUMMER nummer]                                | Parteizugehörigkeit tarnen (als andere Partei getarnt) | [K]     |
| [TRANSPORTIERE einheit-nr]                                  | andere Einheiten mitnehmen                             | [K]     |
| [TREIBE \[betrag\]]                                         | Steuern eintreiben                                     | [L]     |
| [UNTERHALTE \[betrag\]]                                     | verdient 20 oder mehr Silber                           | [L]     |
| [URSPRUNG x y]                                              | setzt den Koordinaten-Ursprung                         | [K]     |
| [VERGISS talent]                                            | vergisst das Talent                                    | [K]     |
| [VERKAUFE anzahl luxusgut]                                  | verkauft Luxusgüter                                    | [(l)] 3 |
| [VERKAUFE ALLES luxusgut]                                   |                                                        |         |
| [[bef-verlasse]]                                            | Schiff oder Gebäude verlassen                          | [K]     |
| [ZAUBERE \[REGION x y\] \[STUFE n\] "zauberspruch" \[...\]] | Zaubern                                                | [(l)] 4 |
| [ZEIGE ALLE ZAUBER]                                         | zeigt Beschreibung aller bekannten Zauber              | [K]     |
| [ZEIGE ALLE TRÄNKE]                                         | zeigt Beschreibung aller bekannten Tränke              | [K]     |
| [ZEIGE "Gegenstand"]                                        | zeigt Beschreibung eines Gegenstands                   | [K]     |
| [ZEIGE "Trank"]                                             | zeigt Beschreibung des Tranks                          | [K]     |
| [ZEIGE "Zauberspruch"]                                      | zeigt Beschreibung des Zaubers                         | [K]     |
| [ZEIGE "Rasse"]                                             | zeigt Beschreibung der Rasse der Einheit               | [K]     |
| [ZERSTÖRE \[stufen\]]                                       | Gebäude oder Schiff verkleinern                        | [L]     |
| [ZERSTÖRE \[stufen\]] STRASSE richtung                      | Straße einreißen                                       | [L]     |
| [ZÜCHTE PFERDE]                                             | Pferde züchten - nur in Pferdezucht                    | L       |

[//]: ./cmd-comment-slash.md
[K]: ./commands.md#kurze-und-lange-befehle
[bef-arbeite]: ./cmd-work.md
[L]: ./commands.md#kurze-und-lange-befehle
[ATTACKIERE einheit-nr]: ./cmd-attack.md
[(l)]: ./commands.md#kurze-und-lange-befehle
[BANNER "text"]: ./cmd-banner.md
[BEANSPRUCHE anzahl gegenstand]: ./cmd-claim.md
[BEFÖRDERE]: ./cmd-promote.md
[BEKLAUE einheit-nr]: ./camouflage.md
[BENENNE EINHEIT "name"]: ./cmd-name.md
[BENENNE PARTEI "name"]: ./cmd-name.md
[BENENNE GEBÄUDE "name"]: ./cmd-name.md
[BENENNE SCHIFF "name"]: ./cmd-name.md
[BENENNE REGION "name"]: ./cmd-name.md
[BENENNE FREMDE EINHEIT einheit "name"]: ./cmd-name.md
[BENENNE FREMDES SCHIFF schiff "name"]: ./cmd-name.md
[BENENNE FREMDES GEBÄUDE gebäude "name"]: ./cmd-name.md
[BENENNE FREMDE PARTEI partei "name"]: ./cmd-name.md
[BENUTZE \[anzahl\] trank]: ./cmd-use.md
[BESCHREIBE EINHEIT "text"]: ./cmd-describe.md
[BESCHREIBE PRIVAT "text"]: ./cmd-describe.md
[BESCHREIBE GEBÄUDE "text"]: ./cmd-describe.md
[BESCHREIBE SCHIFF "text"]: ./cmd-describe.md
[BESCHREIBE REGION "text"]: ./cmd-describe.md
[BETRETE GEBÄUDE gebäude-nr]: ./cmd-enter.md
[BETRETE SCHIFF schiff-nr]: ./cmd-enter.md
[BEWACHE \[NICHT\]]: ./cmd-guard.md
[BEZAHLE NICHT \[gebäude-nr\]]: ./cmd-pay-not.md
[BOTSCHAFT REGION "text"]: ./cmd-message.md
[BOTSCHAFT SCHIFF schiff-nr "text"]: ./cmd-message.md
[BOTSCHAFT GEBÄUDE gebäude-nr "text"]: ./cmd-message.md
[BOTSCHAFT EINHEIT einh-nr "text"]: ./cmd-message.md
[BOTSCHAFT PARTEI partei-nr "text"]: ./cmd-message.md
[DEFAULT "befehl"]: ./cmd-default.md
[EINHEIT einheit-nr]: ./cmd-unit.md
[EMAIL email@adresse]: ./cmd-email.md
[bef-ende]: ./cmd-end.md
[ERESSEA partei-nr "passwort"]: ./cmd-eressea.md
[FAHRE einheit-nr]: ./cmd-ride.md
[FOLGE EINHEIT einheit-nr]: ./cmd-follow.md
[FOLGE SCHIFF schiff-nr]: ./cmd-follow.md
[FORSCHE KRÄUTER]: ./cmd-research.md
[GIB einheit-nr KRÄUTER]: ./cmd-give.md
[GIB einheit-nr KOMMANDO]: ./cmd-give.md
[GIB einheit-nr EINHEIT]: ./cmd-give.md
[GIB einheit-nr \[JE\] anzahl PERSONEN]: ./cmd-give.md
[GIB einheit-nr \[JE\] anzahl SCHIFF]: ./cmd-give.md
[GIB einheit-nr \[JE\] anzahl SILBER]: ./cmd-give.md
[GIB einheit-nr \[JE\] anzahl gegenstand]: ./cmd-give.md
[GIB 0 anzahl SILBER]: ./cmd-give.md
[GIB 0 anzahl PERSONEN]: ./cmd-give.md
[GIB 0 anzahl gegenstand]: ./cmd-give.md
[GRUPPE \["name"\]]: ./cmd-group.md
[HELFE partei-nr ALLES \[NICHT\]]: ./cmd-help.md
[HELFE partei-nr GIB \[NICHT\]]: ./cmd-help.md
[HELFE partei-nr KÄMPFE \[NICHT\]]: ./cmd-help.md
[HELFE partei-nr BEWACHE \[NICHT\]]: ./cmd-help.md
[HELFE partei-nr SILBER \[NICHT\]]: ./cmd-help.md
[HELFE partei-nr PARTEITARNUNG \[NICHT\]]: ./cmd-help.md
[KÄMPFE]: ./cmd-combat.md
[KÄMPFE AGGRESSIV]: ./cmd-combat.md
[KÄMPFE DEFENSIV]: ./cmd-combat.md
[KÄMPFE FLIEHE]: ./cmd-combat.md
[KÄMPFE HELFE \[NICHT\]]: ./cmd-combat.md
[KÄMPFE HINTEN]: ./cmd-combat.md
[KÄMPFE NICHT]: ./cmd-combat.md
[KAMPFZAUBER \[STUFE n\] "zauberspruch" \[NICHT\]]: ./cmd-combatspell.md
[KAUFE anzahl luxusgut]: ./cmd-buy.md
[KONTAKTIERE einheit-nr]: ./cmd-contact.md
[LEHRE einheit-nr \[einheit-nr etc.\]]: ./cmd-teach.md
[LERNE talent]: ./cmd-learn.md
[LERNE AUTO talent]: ./cmd-learn-auto.md
[LOCALE en/de]: ./cmd-locale.md
[MACHE TEMP unit-alias-nr \["name"\]]: ./cmd-make.md
[MACHE \[stufe\] gebäude-typ \[gebäude-nr\]]: ./cmd-make.md
[MACHE \[stufe\] schiffstyp]: ./cmd-make.md
[MACHE \[stufe\] SCHIFF \[schiff-nr\]]: ./cmd-make.md
[bef-mache]: ./cmd-make.md
[MACHE \[stufe\] STRASSE richtung]: ./cmd-make.md
[MACHE \[anzahl\] KRÄUTER]: ./cmd-make.md
[MACHE \[anzahl\] trank]: ./cmd-make.md
[MACHE \[anzahl\] gegenstand]: ./cmd-make.md
[NACH richtung \[richtung etc.\]]: ./cmd-move.md
[NÄCHSTER]: ./cmd-next.md
[NUMMER EINHEIT \[neue\_nr\]]: ./cmd-number.md
[NUMMER GEBÄUDE \[neue\_nr\]]: ./cmd-number.md
[NUMMER PARTEI \[neue\_nr\]]: ./cmd-number.md
[NUMMER SCHIFF \[neue\_nr\]]: ./cmd-number.md
[OPTION AUSWERTUNG \[NICHT\]]: ./cmd-option.md
[OPTION COMPUTER \[NICHT\]]: ./cmd-option.md
[OPTION ZIPPED \[NICHT\]]: ./cmd-option.md
[OPTION BZIP2 \[NICHT\]]: ./cmd-option.md
[OPTION SILBERPOOL \[NICHT\]]: ./cmd-option.md
[OPTION MATERIALPOOL \[NICHT\]]: ./cmd-option.md
[OPTION ADRESSEN \[NICHT\]]: ./cmd-option.md
[OPTION ZUGVORLAGE \[NICHT\]]: ./cmd-option.md
[OPTION STATISTIK \[NICHT\]]: ./cmd-option.md
[OPTION TALENTVERSCHIEBUNG \[NICHT\]]: ./cmd-option.md
[OPTION PUNKTE \[NICHT\]]: ./cmd-option.md
[PASSWORT "neues-passwort"]: ./cmd-password.md
[PFLANZE \[anzahl\] KRÄUTER]: ./cmd-plant.md
[PFLANZE \[anzahl\] BÄUME]: ./cmd-plant.md
[PFLANZE \[anzahl\] MALLORNSAMEN]: ./cmd-plant.md
[PFLANZE \[anzahl\] SAMEN]: ./cmd-plant.md
[PIRATERIE \[partei\_1\] \[partei\_2\] \[...\]]: ./cmd-piracy.md
[PRÄFIX \[präfix\]]: ./cmd-prefix.md
[REGION x,y]: ./cmd-region.md
[REKRUTIERE anzahl]: ./silver.md#rekrutieren
[RESERVIERE anzahl "gegenstand"]: ./cmd-reserve.md
[RESERVIERE anzahl SILBER]: ./cmd-reserve.md
[ROUTE richtung \[richtung etc.\]]: ./cmd-route.md
[SORTIERE VOR einheit-nr]: ./cmd-sort.md
[SORTIERE HINTER einheit-nr]: ./cmd-sort.md
[SPIONIERE einheit-nr]: ./cmd-spy.md
[SPRACHE en/de]: ./cmd-language.md
[STIRB "passwort" \[PARTEI partei-nr\]]: ./cmd-quit.md
[TARNE \[stufe\]]: ./cmd-hide.md
[TARNE rasse]: ./cmd-hide.md
[TARNE PARTEI \[NICHT\]]: ./cmd-hide.md
[TARNE PARTEI NUMMER nummer]: ./cmd-hide.md
[TRANSPORTIERE einheit-nr]: ./cmd-carry.md
[TREIBE \[betrag\]]: ./cmd-tax.md
[UNTERHALTE \[betrag\]]: ./cmd-entertain.md
[URSPRUNG x y]: ./cmd-origin.md
[VERGISS talent]: ./cmd-forget.md
[VERKAUFE anzahl luxusgut]: ./cmd-sell.md
[VERKAUFE ALLES luxusgut]: ./cmd-sell.md
[bef-verlasse]: ./cmd-leave.md
[ZAUBERE \[REGION x y\] \[STUFE n\] "zauberspruch" \[...\]]: ./cmd-cast.md
[ZEIGE ALLE ZAUBER]: ./cmd-show.md
[ZEIGE ALLE TRÄNKE]: ./cmd-show.md
[ZEIGE "Gegenstand"]: ./cmd-show.md
[ZEIGE "Trank"]: ./cmd-show.md
[ZEIGE "Zauberspruch"]: ./cmd-show.md
[ZEIGE "Rasse"]: ./cmd-show.md
[ZERSTÖRE \[stufen\]]: ./cmd-destroy.md
[ZÜCHTE PFERDE]: ./cmd-grow.md

<sup>1</sup> der Befehl ist nicht immer lang, siehe [Kampfende]  
<sup>2</sup> bewegt sich die verfolgte Einheit nicht, kann stattdessen ein anderer langer Befehl ausgeführt werden  
<sup>3</sup> ein KAUFE- und mehrere VERKAUFE-Befehle können kombiniert werden  
<sup>4</sup> eine Einheit kann mehrere Zauber ausführen

## Siehe auch

- [Befehle]
- [Befehlsreihenfolge]

Weiterlesen: [Der erste Zug].

[Der erste Zug]: ./first-round.md

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[Befehl]: ./commands.md
[<sup>(l)</sup>]: ./commands.md#kurze-und-lange-befehle
[Kampfende]: ./war.md#das-ende
[Befehle]: ./commands.md
[Befehlsreihenfolge]: ./commands-sequence.md
