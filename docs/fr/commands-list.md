# Kurzbeschreibung

Unter "K/L" ist vermerkt, ob der [Befehl] ein kurzer oder langer Befehl ist. Eine Einheit kann pro Runde nur einen langen Befehl ausführen, aber beliebig viele kurze.

[<sup>(l)</sup>] bezeichnet einen [pseudolangen Befehl][Befehl], der einer Einheit mehrfach gegeben werden kann. Allerdings kann kein weiterer anderer langer Befehl ausgeführt werden. Näheres dazu ist auf der Seite des jeweiligen Befehls nachzulesen.

|     |     |     |
| --- | --- | --- |Kurzliste der Befehle
| Befehl | Beschreibung | K/L |
| [//] | bleibender Kommentar | [K] |
| [ARBEITE] | verdient 10 Silber oder mehr | [L] |
| [ATTACKIERE einheit-nr] | greift die Einheit an | [(l)] 1 |
| [BANNER "text"] | setzt Text für Adressliste | [K] |
| [BEANSPRUCHE anzahl gegenstand] | holt Gegenstände aus Parteipool | [K] |
| [BEFÖRDERE] | macht Einheit zu Helden | [K] |
| [BEKLAUE einheit-nr] | klaut 50 Silber oder mehr | [L] |
| [BENENNE EINHEIT "name"] | benennt Objekte | [K] |
| [BENENNE PARTEI "name"] |     | [K] |
| [BENENNE GEBÄUDE "name"] |     | [K] |
| [BENENNE SCHIFF "name"] |     | [K] |
| [BENENNE REGION "name"] |     | [K] |
| [BENENNE FREMDE EINHEIT einheit "name"] | benennt fremde und unbenannte Objekte | [K] |
| [BENENNE FREMDES SCHIFF schiff "name"] |     | [K] |
| [BENENNE FREMDES GEBÄUDE gebäude "name"] |     | [K] |
| [BENENNE FREMDE PARTEI partei "name"] |     | [K] |
| [BENUTZE \[anzahl\] trank] | benutzt alchemistischen Trank | [K] |
| [BESCHREIBE EINHEIT "text"] | beschreibt Objekte | [K] |
| [BESCHREIBE PRIVAT "text"] |     | [K] |
| [BESCHREIBE GEBÄUDE "text"] |     | [K] |
| [BESCHREIBE SCHIFF "text"] |     | [K] |
| [BESCHREIBE REGION "text"] |     | [K] |
| [BETRETE GEBÄUDE gebäude-nr] | betritt Gebäude | [K] |
| [BETRETE SCHIFF schiff-nr] | betritt Schiffe | [K] |
| [BEWACHE \[NICHT\]] | bewacht die Region | [K] |
| [BEZAHLE NICHT \[gebäude-nr\]] | bezahlt den Unterhalt für ein Gebäude nicht | [K] |
| [BOTSCHAFT REGION "text"] | versendet Botschaften | [K] |
| [BOTSCHAFT SCHIFF schiff-nr "text"] | versendet Botschaften | [K] |
| [BOTSCHAFT GEBÄUDE gebäude-nr "text"] | versendet Botschaften | [K] |
| [BOTSCHAFT EINHEIT einh-nr "text"] |     | [K] |
| [BOTSCHAFT PARTEI partei-nr "text"] |     | [K] |
| [DEFAULT "befehl"] | setzt Default-Befehl für die nächste Runde. | [K] |
| [EINHEIT einheit-nr] | beginnt Befehle für eine Einheit | [K] |
| [EMAIL email@adresse] | setzt die E-Mail-Adresse | [K] |
| [ENDE] | beendet MACHE TEMP | [K] |
| [ERESSEA partei-nr "passwort"] | beginnt Befehle für Partei | [K] |
| [FAHRE einheit-nr] | sich transportieren lassen | [L] |
| [FOLGE EINHEIT einheit-nr] | folgt einer Einheit | [(l)] 2 |
| [FOLGE SCHIFF schiff-nr] | folgt einem Schiff | [(l)] 2 |
| [FORSCHE KRÄUTER] | sucht Kräuter | [L] |
| [GIB einheit-nr KRÄUTER] | gibt einer Einheit alle Kräuter | [K] |
| [GIB einheit-nr KOMMANDO] | übergibt Kommando über Schiff/Gebäude | [K] |
| [GIB einheit-nr EINHEIT] | übergibt Einheit an fremde Partei | [K] |
| [GIB einheit-nr \[JE\] anzahl PERSONEN] | übergibt Personen | [K] |
| [GIB einheit-nr \[JE\] anzahl SCHIFF] | übergibt SCHIFF zur Bildung von Konvois | [K] |
| [GIB einheit-nr \[JE\] anzahl SILBER] | übergibt Silber | [K] |
| [GIB einheit-nr \[JE\] anzahl gegenstand] | übergibt Gegenstände | [K] |
| [GIB 0 anzahl SILBER] | gibt Gegenstände an die Bauern | [K] |
| [GIB 0 anzahl PERSONEN] |     | [K] |
| [GIB 0 anzahl gegenstand] |     | [K] |
| [GRUPPE \["name"\]] | Gruppieren von Einheiten | [K] |
| [HELFE partei-nr ALLES \[NICHT\]] | setzt / löscht einseitige Allianz | [K] |
| [HELFE partei-nr GIB \[NICHT\]] |     | [K] |
| [HELFE partei-nr KÄMPFE \[NICHT\]] |     | [K] |
| [HELFE partei-nr BEWACHE \[NICHT\]] |     | [K] |
| [HELFE partei-nr SILBER \[NICHT\]] |     | [K] |
| [HELFE partei-nr PARTEITARNUNG \[NICHT\]] |     | [K] |
| [KÄMPFE] | setzt Verhalten im Kampf | K   |
| [KÄMPFE AGGRESSIV] |     | [K] |
| [KÄMPFE DEFENSIV] |     | [K] |
| [KÄMPFE FLIEHE] |     | [K] |
| [KÄMPFE HELFE \[NICHT\]] | der Einheit wird im Kampf \[nicht\] geholfen | [K] |
| [KÄMPFE HINTEN] |     | [K] |
| [KÄMPFE NICHT] |     | [K] |
| [KAMPFZAUBER \[STUFE n\] "zauberspruch" \[NICHT\]] | setzt Zauber für Kämpfe | [K] |
| [KAUFE anzahl luxusgut] | kaufe Luxusgüter | [(l)] 3 |
| [KONTAKTIERE einheit-nr] | kontaktiere fremde Einheiten | [K] |
| [LEHRE einheit-nr \[einheit-nr etc.\]] | lehre Einheiten | [L] |
| [LERNE talent] | Talent lernen | [L] |
| [LERNE AUTO talent] | Talent lernen oder lehren | [L] |
| [LOCALE en/de] | zeigt die Sprache der Befehle an | [K] |
| [MACHE TEMP unit-alias-nr \["name"\]] | erschaffe neue Einheit | [K] |
| [MACHE \[stufe\] gebäude-typ \[gebäude-nr\]] | erweitere oder baue neues Gebäude | [L] |
| [MACHE \[stufe\] schiffstyp] | baue neue Schiffe | [L] |
| [MACHE \[stufe\] SCHIFF \[schiff-nr\]] | baue weiter am Schiff | [L] |
| [MACHE] | baue weiter an Gebäude/Schiff | [L] |
| [MACHE \[stufe\] STRASSE richtung] | baue Straßen | [L] |
| [MACHE \[anzahl\] KRÄUTER] | suche Kräuter der Region | [L] |
| [MACHE \[anzahl\] trank] | mache einen alchemistischen Trank | [L] |
| [MACHE \[anzahl\] gegenstand] | mache einen Gegenstand oder baue Rohstoffe ab | [L] |
| [NACH richtung \[richtung etc.\]] | reisen | [L] |
| [NÄCHSTER] | beendet Befehle | [K] |
| [NUMMER EINHEIT \[neue\_nr\]] | vergibt neue Nummer | [K] |
| [NUMMER GEBÄUDE \[neue\_nr\]] |     | [K] |
| [NUMMER PARTEI \[neue\_nr\]] |     | [K] |
| [NUMMER SCHIFF \[neue\_nr\]] |     | [K] |
| [OPTION AUSWERTUNG \[NICHT\]] | verschiedene Einstellungen | [K] |
| [OPTION COMPUTER \[NICHT\]] |     | [K] |
| [OPTION ZIPPED \[NICHT\]] |     | [K] |
| [OPTION BZIP2 \[NICHT\]] |     | [K] |
| [OPTION SILBERPOOL \[NICHT\]] |     | [K] |
| [OPTION MATERIALPOOL \[NICHT\]] |     | [K] |
| [OPTION ADRESSEN \[NICHT\]] |     | [K] |
| [OPTION ZUGVORLAGE \[NICHT\]] |     | [K] |
| [OPTION STATISTIK \[NICHT\]] |     | [K] |
| [OPTION TALENTVERSCHIEBUNG \[NICHT\]] |     | [K] |
| [OPTION PUNKTE \[NICHT\]] |     | [K] |
| [PASSWORT "neues-passwort"] | setzt neues Passwort | [K] |
| [PFLANZE \[anzahl\] KRÄUTER] | pflanzt Kräuter | [L] |
| [PFLANZE \[anzahl\] BÄUME] | pflanzt Samen | [L] |
| [PFLANZE \[anzahl\] MALLORNSAMEN] | pflanzt Samen | [L] |
| [PFLANZE \[anzahl\] SAMEN] | pflanzt Samen | [L] |
| [PIRATERIE \[partei\_1\] \[partei\_2\] \[...\]] | Piraterie setzen | [L] |
| [PRÄFIX \[präfix\]] | gibt der Rassenbezeichnung ein Präfix | [K] |
| [REGION x,y] | keine Funktion (nur für Tools) | [K] |
| [REKRUTIERE anzahl] | rekrutiert weitere Personen | [K] |
| [RESERVIERE anzahl "gegenstand"] | Gegenstände reservieren | [K] |
| [RESERVIERE anzahl SILBER] | Silber reservieren | [K] |
| [ROUTE richtung \[richtung etc.\]] | reisen | [L] |
| [SORTIERE VOR einheit-nr] | Einheit in Report sortieren | [K] |
| [SORTIERE HINTER einheit-nr] |     | [K] |
| [SPIONIERE einheit-nr] | Einheit ausspionieren | [L] |
| [SPRACHE en/de] | ändert die Sprache der Partei | [K] |
| [STIRB "passwort" \[PARTEI partei-nr\]] | aus dem Spiel ausscheiden | [K] |
| [TARNE \[stufe\]] | Tarnstufe setzen | [K] |
| [TARNE rasse] | Dämonen: als andere Rasse tarnen | [K] |
| [TARNE PARTEI \[NICHT\]] | Parteizugehörigkeit verbergen (als "anonym" getarnt) | [K] |
| [TARNE PARTEI NUMMER nummer] | Parteizugehörigkeit tarnen (als andere Partei getarnt) | [K] |
| [TRANSPORTIERE einheit-nr] | andere Einheiten mitnehmen | [K] |
| [TREIBE \[betrag\]] | Steuern eintreiben | [L] |
| [UNTERHALTE \[betrag\]] | verdient 20 oder mehr Silber | [L] |
| [URSPRUNG x y] | setzt den Koordinaten-Ursprung | [K] |
| [VERGISS talent] | vergisst das Talent | [K] |
| [VERKAUFE anzahl luxusgut] | verkauft Luxusgüter | [(l)] 3 |
| [VERKAUFE ALLES luxusgut] |     |     |
| [VERLASSE] | Schiff oder Gebäude verlassen | [K] |
| [ZAUBERE \[REGION x y\] \[STUFE n\] "zauberspruch" \[...\]] | Zaubern | [(l)] 4 |
| [ZEIGE ALLE ZAUBER] | zeigt Beschreibung aller bekannten Zauber | [K] |
| [ZEIGE ALLE TRÄNKE] | zeigt Beschreibung aller bekannten Tränke | [K] |
| [ZEIGE "Gegenstand"] | zeigt Beschreibung eines Gegenstands | [K] |
| [ZEIGE "Trank"] | zeigt Beschreibung des Tranks | [K] |
| [ZEIGE "Zauberspruch"] | zeigt Beschreibung des Zaubers | [K] |
| [ZEIGE "Rasse"] | zeigt Beschreibung der Rasse der Einheit | [K] |
| [ZERSTÖRE \[stufen\]] | Gebäude oder Schiff verkleinern | [L] |
| [ZERSTÖRE \[stufen\]] STRASSE richtung | Straße einreißen | [L] |
| [ZÜCHTE PFERDE] | Pferde züchten - nur in Pferdezucht | L   |

[//]: /Spezial:Meine_Sprache/KOMMENTAR "Spezial:Meine Sprache/KOMMENTAR"
[K]: /Befehl#KurzLang "Befehl"
[ARBEITE]: /Spezial:Meine_Sprache/ARBEITE "Spezial:Meine Sprache/ARBEITE"
[L]: /Befehl#KurzLang "Befehl"
[ATTACKIERE einheit-nr]: /Spezial:Meine_Sprache/ATTACKIERE "Spezial:Meine Sprache/ATTACKIERE"
[(l)]: /Befehl#KurzLang "Befehl"
[BANNER "text"]: /Spezial:Meine_Sprache/BANNER "Spezial:Meine Sprache/BANNER"
[K]: /Befehl#KurzLang "Befehl"
[BEANSPRUCHE anzahl gegenstand]: /Spezial:Meine_Sprache/BEANSPRUCHE "Spezial:Meine Sprache/BEANSPRUCHE"
[K]: /Befehl#KurzLang "Befehl"
[BEFÖRDERE]: /Spezial:Meine_Sprache/BEF%C3%96RDERE "Spezial:Meine Sprache/BEFÖRDERE"
[K]: /Befehl#KurzLang "Befehl"
[BEKLAUE einheit-nr]: ./camouflage.md "Spezial:Meine Sprache/BEKLAUE"
[L]: /Befehl#KurzLang "Befehl"
[BENENNE EINHEIT "name"]: /Spezial:Meine_Sprache/BENENNE "Spezial:Meine Sprache/BENENNE"
[K]: /Befehl#KurzLang "Befehl"
[BENENNE PARTEI "name"]: /Spezial:Meine_Sprache/BENENNE "Spezial:Meine Sprache/BENENNE"
[K]: /Befehl#KurzLang "Befehl"
[BENENNE GEBÄUDE "name"]: /Spezial:Meine_Sprache/BENENNE "Spezial:Meine Sprache/BENENNE"
[K]: /Befehl#KurzLang "Befehl"
[BENENNE SCHIFF "name"]: /Spezial:Meine_Sprache/BENENNE "Spezial:Meine Sprache/BENENNE"
[K]: /Befehl#KurzLang "Befehl"
[BENENNE REGION "name"]: /Spezial:Meine_Sprache/BENENNE "Spezial:Meine Sprache/BENENNE"
[K]: /Befehl#KurzLang "Befehl"
[BENENNE FREMDE EINHEIT einheit "name"]: /Spezial:Meine_Sprache/BENENNE "Spezial:Meine Sprache/BENENNE"
[K]: /Befehl#KurzLang "Befehl"
[BENENNE FREMDES SCHIFF schiff "name"]: /Spezial:Meine_Sprache/BENENNE "Spezial:Meine Sprache/BENENNE"
[K]: /Befehl#KurzLang "Befehl"
[BENENNE FREMDES GEBÄUDE gebäude "name"]: /Spezial:Meine_Sprache/BENENNE "Spezial:Meine Sprache/BENENNE"
[K]: /Befehl#KurzLang "Befehl"
[BENENNE FREMDE PARTEI partei "name"]: /Spezial:Meine_Sprache/BENENNE "Spezial:Meine Sprache/BENENNE"
[K]: /Befehl#KurzLang "Befehl"
[BENUTZE \[anzahl\] trank]: /Spezial:Meine_Sprache/BENUTZE "Spezial:Meine Sprache/BENUTZE"
[K]: /Befehl#KurzLang "Befehl"
[BESCHREIBE EINHEIT "text"]: /Spezial:Meine_Sprache/BESCHREIBE "Spezial:Meine Sprache/BESCHREIBE"
[K]: /Befehl#KurzLang "Befehl"
[BESCHREIBE PRIVAT "text"]: /Spezial:Meine_Sprache/BESCHREIBE "Spezial:Meine Sprache/BESCHREIBE"
[K]: /Befehl#KurzLang "Befehl"
[BESCHREIBE GEBÄUDE "text"]: /Spezial:Meine_Sprache/BESCHREIBE "Spezial:Meine Sprache/BESCHREIBE"
[K]: /Befehl#KurzLang "Befehl"
[BESCHREIBE SCHIFF "text"]: /Spezial:Meine_Sprache/BESCHREIBE "Spezial:Meine Sprache/BESCHREIBE"
[K]: /Befehl#KurzLang "Befehl"
[BESCHREIBE REGION "text"]: /Spezial:Meine_Sprache/BESCHREIBE "Spezial:Meine Sprache/BESCHREIBE"
[K]: /Befehl#KurzLang "Befehl"
[BETRETE GEBÄUDE gebäude-nr]: /Spezial:Meine_Sprache/BETRETE "Spezial:Meine Sprache/BETRETE"
[K]: /Befehl#KurzLang "Befehl"
[BETRETE SCHIFF schiff-nr]: /Spezial:Meine_Sprache/BETRETE "Spezial:Meine Sprache/BETRETE"
[K]: /Befehl#KurzLang "Befehl"
[BEWACHE \[NICHT\]]: /Spezial:Meine_Sprache/BEWACHE "Spezial:Meine Sprache/BEWACHE"
[K]: /Befehl#KurzLang "Befehl"
[BEZAHLE NICHT \[gebäude-nr\]]: /Spezial:Meine_Sprache/BEZAHLE "Spezial:Meine Sprache/BEZAHLE"
[K]: /Befehl#KurzLang "Befehl"
[BOTSCHAFT REGION "text"]: /Spezial:Meine_Sprache/BOTSCHAFT "Spezial:Meine Sprache/BOTSCHAFT"
[K]: /Befehl#KurzLang "Befehl"
[BOTSCHAFT SCHIFF schiff-nr "text"]: /Spezial:Meine_Sprache/BOTSCHAFT "Spezial:Meine Sprache/BOTSCHAFT"
[K]: /Befehl#KurzLang "Befehl"
[BOTSCHAFT GEBÄUDE gebäude-nr "text"]: /Spezial:Meine_Sprache/BOTSCHAFT "Spezial:Meine Sprache/BOTSCHAFT"
[K]: /Befehl#KurzLang "Befehl"
[BOTSCHAFT EINHEIT einh-nr "text"]: /Spezial:Meine_Sprache/BOTSCHAFT "Spezial:Meine Sprache/BOTSCHAFT"
[K]: /Befehl#KurzLang "Befehl"
[BOTSCHAFT PARTEI partei-nr "text"]: /Spezial:Meine_Sprache/BOTSCHAFT "Spezial:Meine Sprache/BOTSCHAFT"
[K]: /Befehl#KurzLang "Befehl"
[DEFAULT "befehl"]: /Spezial:Meine_Sprache/DEFAULT "Spezial:Meine Sprache/DEFAULT"
[K]: /Befehl#KurzLang "Befehl"
[EINHEIT einheit-nr]: /Spezial:Meine_Sprache/EINHEIT "Spezial:Meine Sprache/EINHEIT"
[K]: /Befehl#KurzLang "Befehl"
[EMAIL email@adresse]: /Spezial:Meine_Sprache/EMAIL "Spezial:Meine Sprache/EMAIL"
[K]: /Befehl#KurzLang "Befehl"
[ENDE]: /Spezial:Meine_Sprache/ENDE "Spezial:Meine Sprache/ENDE"
[K]: /Befehl#KurzLang "Befehl"
[ERESSEA partei-nr "passwort"]: /Spezial:Meine_Sprache/ERESSEA "Spezial:Meine Sprache/ERESSEA"
[K]: /Befehl#KurzLang "Befehl"
[FAHRE einheit-nr]: /Spezial:Meine_Sprache/FAHRE "Spezial:Meine Sprache/FAHRE"
[L]: /Befehl#KurzLang "Befehl"
[FOLGE EINHEIT einheit-nr]: /Spezial:Meine_Sprache/FOLGE "Spezial:Meine Sprache/FOLGE"
[(l)]: /Befehl#KurzLang "Befehl"
[FOLGE SCHIFF schiff-nr]: /Spezial:Meine_Sprache/FOLGE "Spezial:Meine Sprache/FOLGE"
[(l)]: /Befehl#KurzLang "Befehl"
[FORSCHE KRÄUTER]: /Spezial:Meine_Sprache/FORSCHE "Spezial:Meine Sprache/FORSCHE"
[L]: /Befehl#KurzLang "Befehl"
[GIB einheit-nr KRÄUTER]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
[K]: /Befehl#KurzLang "Befehl"
[GIB einheit-nr KOMMANDO]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
[K]: /Befehl#KurzLang "Befehl"
[GIB einheit-nr EINHEIT]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
[K]: /Befehl#KurzLang "Befehl"
[GIB einheit-nr \[JE\] anzahl PERSONEN]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
[K]: /Befehl#KurzLang "Befehl"
[GIB einheit-nr \[JE\] anzahl SCHIFF]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
[K]: /Befehl#KurzLang "Befehl"
[GIB einheit-nr \[JE\] anzahl SILBER]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
[K]: /Befehl#KurzLang "Befehl"
[GIB einheit-nr \[JE\] anzahl gegenstand]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
[K]: /Befehl#KurzLang "Befehl"
[GIB 0 anzahl SILBER]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
[K]: /Befehl#KurzLang "Befehl"
[GIB 0 anzahl PERSONEN]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
[K]: /Befehl#KurzLang "Befehl"
[GIB 0 anzahl gegenstand]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
[K]: /Befehl#KurzLang "Befehl"
[GRUPPE \["name"\]]: /Spezial:Meine_Sprache/GRUPPE "Spezial:Meine Sprache/GRUPPE"
[K]: /Befehl#KurzLang "Befehl"
[HELFE partei-nr ALLES \[NICHT\]]: /Spezial:Meine_Sprache/HELFE "Spezial:Meine Sprache/HELFE"
[K]: /Befehl#KurzLang "Befehl"
[HELFE partei-nr GIB \[NICHT\]]: /Spezial:Meine_Sprache/HELFE "Spezial:Meine Sprache/HELFE"
[K]: /Befehl#KurzLang "Befehl"
[HELFE partei-nr KÄMPFE \[NICHT\]]: /Spezial:Meine_Sprache/HELFE "Spezial:Meine Sprache/HELFE"
[K]: /Befehl#KurzLang "Befehl"
[HELFE partei-nr BEWACHE \[NICHT\]]: /Spezial:Meine_Sprache/HELFE "Spezial:Meine Sprache/HELFE"
[K]: /Befehl#KurzLang "Befehl"
[HELFE partei-nr SILBER \[NICHT\]]: /Spezial:Meine_Sprache/HELFE "Spezial:Meine Sprache/HELFE"
[K]: /Befehl#KurzLang "Befehl"
[HELFE partei-nr PARTEITARNUNG \[NICHT\]]: /Spezial:Meine_Sprache/HELFE "Spezial:Meine Sprache/HELFE"
[K]: /Befehl#KurzLang "Befehl"
[KÄMPFE]: /Spezial:Meine_Sprache/K%C3%84MPFE "Spezial:Meine Sprache/KÄMPFE"
[KÄMPFE AGGRESSIV]: /Spezial:Meine_Sprache/K%C3%84MPFE "Spezial:Meine Sprache/KÄMPFE"
[K]: /Befehl#KurzLang "Befehl"
[KÄMPFE DEFENSIV]: /Spezial:Meine_Sprache/K%C3%84MPFE "Spezial:Meine Sprache/KÄMPFE"
[K]: /Befehl#KurzLang "Befehl"
[KÄMPFE FLIEHE]: /Spezial:Meine_Sprache/K%C3%84MPFE "Spezial:Meine Sprache/KÄMPFE"
[K]: /Befehl#KurzLang "Befehl"
[KÄMPFE HELFE \[NICHT\]]: /Spezial:Meine_Sprache/K%C3%84MPFE "Spezial:Meine Sprache/KÄMPFE"
[K]: /Befehl#KurzLang "Befehl"
[KÄMPFE HINTEN]: /Spezial:Meine_Sprache/K%C3%84MPFE "Spezial:Meine Sprache/KÄMPFE"
[K]: /Befehl#KurzLang "Befehl"
[KÄMPFE NICHT]: /Spezial:Meine_Sprache/K%C3%84MPFE "Spezial:Meine Sprache/KÄMPFE"
[K]: /Befehl#KurzLang "Befehl"
[KAMPFZAUBER \[STUFE n\] "zauberspruch" \[NICHT\]]: /Spezial:Meine_Sprache/KAMPFZAUBER "Spezial:Meine Sprache/KAMPFZAUBER"
[K]: /Befehl#KurzLang "Befehl"
[KAUFE anzahl luxusgut]: /Spezial:Meine_Sprache/KAUFE "Spezial:Meine Sprache/KAUFE"
[(l)]: /Befehl#KurzLang "Befehl"
[KONTAKTIERE einheit-nr]: /Spezial:Meine_Sprache/KONTAKTIERE "Spezial:Meine Sprache/KONTAKTIERE"
[K]: /Befehl#KurzLang "Befehl"
[LEHRE einheit-nr \[einheit-nr etc.\]]: /Spezial:Meine_Sprache/LEHRE "Spezial:Meine Sprache/LEHRE"
[L]: /Befehl#KurzLang "Befehl"
[LERNE talent]: /Spezial:Meine_Sprache/LERNE "Spezial:Meine Sprache/LERNE"
[L]: /Befehl#KurzLang "Befehl"
[LERNE AUTO talent]: /Spezial:Meine_Sprache/LERNE_AUTO "Spezial:Meine Sprache/LERNE AUTO"
[L]: /Befehl#KurzLang "Befehl"
[LOCALE en/de]: /Spezial:Meine_Sprache/LOCALE "Spezial:Meine Sprache/LOCALE"
[K]: /Befehl#KurzLang "Befehl"
[MACHE TEMP unit-alias-nr \["name"\]]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
[K]: /Befehl#KurzLang "Befehl"
[MACHE \[stufe\] gebäude-typ \[gebäude-nr\]]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
[L]: /Befehl#KurzLang "Befehl"
[MACHE \[stufe\] schiffstyp]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
[L]: /Befehl#KurzLang "Befehl"
[MACHE \[stufe\] SCHIFF \[schiff-nr\]]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
[L]: /Befehl#KurzLang "Befehl"
[MACHE]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
[L]: /Befehl#KurzLang "Befehl"
[MACHE \[stufe\] STRASSE richtung]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
[L]: /Befehl#KurzLang "Befehl"
[MACHE \[anzahl\] KRÄUTER]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
[L]: /Befehl#KurzLang "Befehl"
[MACHE \[anzahl\] trank]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
[L]: /Befehl#KurzLang "Befehl"
[MACHE \[anzahl\] gegenstand]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
[L]: /Befehl#KurzLang "Befehl"
[NACH richtung \[richtung etc.\]]: /Spezial:Meine_Sprache/NACH "Spezial:Meine Sprache/NACH"
[L]: /Befehl#KurzLang "Befehl"
[NÄCHSTER]: /Spezial:Meine_Sprache/N%C3%84CHSTER "Spezial:Meine Sprache/NÄCHSTER"
[K]: /Befehl#KurzLang "Befehl"
[NUMMER EINHEIT \[neue\_nr\]]: /Spezial:Meine_Sprache/NUMMER "Spezial:Meine Sprache/NUMMER"
[K]: /Befehl#KurzLang "Befehl"
[NUMMER GEBÄUDE \[neue\_nr\]]: /Spezial:Meine_Sprache/NUMMER "Spezial:Meine Sprache/NUMMER"
[K]: /Befehl#KurzLang "Befehl"
[NUMMER PARTEI \[neue\_nr\]]: /Spezial:Meine_Sprache/NUMMER "Spezial:Meine Sprache/NUMMER"
[K]: /Befehl#KurzLang "Befehl"
[NUMMER SCHIFF \[neue\_nr\]]: /Spezial:Meine_Sprache/NUMMER "Spezial:Meine Sprache/NUMMER"
[K]: /Befehl#KurzLang "Befehl"
[OPTION AUSWERTUNG \[NICHT\]]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
[K]: /Befehl#KurzLang "Befehl"
[OPTION COMPUTER \[NICHT\]]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
[K]: /Befehl#KurzLang "Befehl"
[OPTION ZIPPED \[NICHT\]]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
[K]: /Befehl#KurzLang "Befehl"
[OPTION BZIP2 \[NICHT\]]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
[K]: /Befehl#KurzLang "Befehl"
[OPTION SILBERPOOL \[NICHT\]]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
[K]: /Befehl#KurzLang "Befehl"
[OPTION MATERIALPOOL \[NICHT\]]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
[K]: /Befehl#KurzLang "Befehl"
[OPTION ADRESSEN \[NICHT\]]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
[K]: /Befehl#KurzLang "Befehl"
[OPTION ZUGVORLAGE \[NICHT\]]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
[K]: /Befehl#KurzLang "Befehl"
[OPTION STATISTIK \[NICHT\]]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
[K]: /Befehl#KurzLang "Befehl"
[OPTION TALENTVERSCHIEBUNG \[NICHT\]]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
[K]: /Befehl#KurzLang "Befehl"
[OPTION PUNKTE \[NICHT\]]: /Spezial:Meine_Sprache/OPTION "Spezial:Meine Sprache/OPTION"
[K]: /Befehl#KurzLang "Befehl"
[PASSWORT "neues-passwort"]: /Spezial:Meine_Sprache/PASSWORT "Spezial:Meine Sprache/PASSWORT"
[K]: /Befehl#KurzLang "Befehl"
[PFLANZE \[anzahl\] KRÄUTER]: /Spezial:Meine_Sprache/PFLANZE "Spezial:Meine Sprache/PFLANZE"
[L]: /Befehl#KurzLang "Befehl"
[PFLANZE \[anzahl\] BÄUME]: /Spezial:Meine_Sprache/PFLANZE "Spezial:Meine Sprache/PFLANZE"
[L]: /Befehl#KurzLang "Befehl"
[PFLANZE \[anzahl\] MALLORNSAMEN]: /Spezial:Meine_Sprache/PFLANZE "Spezial:Meine Sprache/PFLANZE"
[L]: /Befehl#KurzLang "Befehl"
[PFLANZE \[anzahl\] SAMEN]: /Spezial:Meine_Sprache/PFLANZE "Spezial:Meine Sprache/PFLANZE"
[L]: /Befehl#KurzLang "Befehl"
[PIRATERIE \[partei\_1\] \[partei\_2\] \[...\]]: /Spezial:Meine_Sprache/PIRATERIE "Spezial:Meine Sprache/PIRATERIE"
[L]: /Befehl#KurzLang "Befehl"
[PRÄFIX \[präfix\]]: /Spezial:Meine_Sprache/PR%C3%84FIX "Spezial:Meine Sprache/PRÄFIX"
[K]: /Befehl#KurzLang "Befehl"
[REGION x,y]: /Spezial:Meine_Sprache/REGION "Spezial:Meine Sprache/REGION"
[K]: /Befehl#KurzLang "Befehl"
[REKRUTIERE anzahl]: /Spezial:Meine_Sprache/REKRUTIERE "Spezial:Meine Sprache/REKRUTIERE"
[K]: /Befehl#KurzLang "Befehl"
[RESERVIERE anzahl "gegenstand"]: /Spezial:Meine_Sprache/RESERVIERE "Spezial:Meine Sprache/RESERVIERE"
[K]: /Befehl#KurzLang "Befehl"
[RESERVIERE anzahl SILBER]: /Spezial:Meine_Sprache/RESERVIERE "Spezial:Meine Sprache/RESERVIERE"
[K]: /Befehl#KurzLang "Befehl"
[ROUTE richtung \[richtung etc.\]]: /Spezial:Meine_Sprache/ROUTE "Spezial:Meine Sprache/ROUTE"
[L]: /Befehl#KurzLang "Befehl"
[SORTIERE VOR einheit-nr]: /Spezial:Meine_Sprache/SORTIERE "Spezial:Meine Sprache/SORTIERE"
[K]: /Befehl#KurzLang "Befehl"
[SORTIERE HINTER einheit-nr]: /Spezial:Meine_Sprache/SORTIERE "Spezial:Meine Sprache/SORTIERE"
[K]: /Befehl#KurzLang "Befehl"
[SPIONIERE einheit-nr]: /Spezial:Meine_Sprache/SPIONIERE "Spezial:Meine Sprache/SPIONIERE"
[L]: /Befehl#KurzLang "Befehl"
[SPRACHE en/de]: /Spezial:Meine_Sprache/SPRACHE "Spezial:Meine Sprache/SPRACHE"
[K]: /Befehl#KurzLang "Befehl"
[STIRB "passwort" \[PARTEI partei-nr\]]: /Spezial:Meine_Sprache/STIRB "Spezial:Meine Sprache/STIRB"
[K]: /Befehl#KurzLang "Befehl"
[TARNE \[stufe\]]: /Spezial:Meine_Sprache/TARNE "Spezial:Meine Sprache/TARNE"
[K]: /Befehl#KurzLang "Befehl"
[TARNE rasse]: /Spezial:Meine_Sprache/TARNE "Spezial:Meine Sprache/TARNE"
[K]: /Befehl#KurzLang "Befehl"
[TARNE PARTEI \[NICHT\]]: /Spezial:Meine_Sprache/TARNE "Spezial:Meine Sprache/TARNE"
[K]: /Befehl#KurzLang "Befehl"
[TARNE PARTEI NUMMER nummer]: /Spezial:Meine_Sprache/TARNE "Spezial:Meine Sprache/TARNE"
[K]: /Befehl#KurzLang "Befehl"
[TRANSPORTIERE einheit-nr]: /Spezial:Meine_Sprache/TRANSPORTIERE "Spezial:Meine Sprache/TRANSPORTIERE"
[K]: /Befehl#KurzLang "Befehl"
[TREIBE \[betrag\]]: /Spezial:Meine_Sprache/TREIBE "Spezial:Meine Sprache/TREIBE"
[L]: /Befehl#KurzLang "Befehl"
[UNTERHALTE \[betrag\]]: /Spezial:Meine_Sprache/UNTERHALTE "Spezial:Meine Sprache/UNTERHALTE"
[L]: /Befehl#KurzLang "Befehl"
[URSPRUNG x y]: /Spezial:Meine_Sprache/URSPRUNG "Spezial:Meine Sprache/URSPRUNG"
[K]: /Befehl#KurzLang "Befehl"
[VERGISS talent]: /Spezial:Meine_Sprache/VERGISS "Spezial:Meine Sprache/VERGISS"
[K]: /Befehl#KurzLang "Befehl"
[VERKAUFE anzahl luxusgut]: /Spezial:Meine_Sprache/VERKAUFE "Spezial:Meine Sprache/VERKAUFE"
[(l)]: /Befehl#KurzLang "Befehl"
[VERKAUFE ALLES luxusgut]: /Spezial:Meine_Sprache/VERKAUFE "Spezial:Meine Sprache/VERKAUFE"
[VERLASSE]: /Spezial:Meine_Sprache/VERLASSE "Spezial:Meine Sprache/VERLASSE"
[K]: /Befehl#KurzLang "Befehl"
[ZAUBERE \[REGION x y\] \[STUFE n\] "zauberspruch" \[...\]]: /Spezial:Meine_Sprache/ZAUBERE "Spezial:Meine Sprache/ZAUBERE"
[(l)]: /Befehl#KurzLang "Befehl"
[ZEIGE ALLE ZAUBER]: /Spezial:Meine_Sprache/ZEIGE "Spezial:Meine Sprache/ZEIGE"
[K]: /Befehl#KurzLang "Befehl"
[ZEIGE ALLE TRÄNKE]: /Spezial:Meine_Sprache/ZEIGE "Spezial:Meine Sprache/ZEIGE"
[K]: /Befehl#KurzLang "Befehl"
[ZEIGE "Gegenstand"]: /Spezial:Meine_Sprache/ZEIGE "Spezial:Meine Sprache/ZEIGE"
[K]: /Befehl#KurzLang "Befehl"
[ZEIGE "Trank"]: /Spezial:Meine_Sprache/ZEIGE "Spezial:Meine Sprache/ZEIGE"
[K]: /Befehl#KurzLang "Befehl"
[ZEIGE "Zauberspruch"]: /Spezial:Meine_Sprache/ZEIGE "Spezial:Meine Sprache/ZEIGE"
[K]: /Befehl#KurzLang "Befehl"
[ZEIGE "Rasse"]: /Spezial:Meine_Sprache/ZEIGE "Spezial:Meine Sprache/ZEIGE"
[K]: /Befehl#KurzLang "Befehl"
[ZERSTÖRE \[stufen\]]: /Spezial:Meine_Sprache/ZERST%C3%96RE "Spezial:Meine Sprache/ZERSTÖRE"
[L]: /Befehl#KurzLang "Befehl"
[ZERSTÖRE \[stufen\]]: /Spezial:Meine_Sprache/ZERST%C3%96RE "Spezial:Meine Sprache/ZERSTÖRE"
[L]: /Befehl#KurzLang "Befehl"
[ZÜCHTE PFERDE]: /Spezial:Meine_Sprache/Z%C3%9CCHTE "Spezial:Meine Sprache/ZÜCHTE"

<sup>1</sup> der Befehl ist nicht immer lang, siehe [Kampfende]  
<sup>2</sup> bewegt sich die verfolgte Einheit nicht, kann stattdessen ein anderer langer Befehl ausgeführt werden  
<sup>3</sup> ein KAUFE- und mehrere VERKAUFE-Befehle können kombiniert werden  
<sup>4</sup> eine Einheit kann mehrere Zauber ausführen

## Siehe auch

- [Befehle]
- [Befehlsreihenfolge]

|     |     |
| --- | --- |
| Weiterlesen: | [Der erste Zug] |

[Der erste Zug]: /Spezial:Meine_Sprache/Der_erste_Zug "Spezial:Meine Sprache/Der erste Zug"

Récupérée de « [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] »

[Catégorie] :

- [Befehle][1]

  [Befehl]: /Spezial:Meine_Sprache/Befehl "Spezial:Meine Sprache/Befehl"
  [<sup>(l)</sup>]: /Befehl#KurzLang "Befehl"
  [Kampfende]: /Spezial:Meine_Sprache/Kampfende "Spezial:Meine Sprache/Kampfende"
  [Befehle]: /Spezial:Meine_Sprache/Befehle "Spezial:Meine Sprache/Befehle"
  [Befehlsreihenfolge]: /Spezial:Meine_Sprache/Befehlsreihenfolge "Spezial:Meine Sprache/Befehlsreihenfolge"
  [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741]: https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741
  [Catégorie]: /Spezial:Kategorien "Spezial:Kategorien"
  [1]: /Kategorie:Befehle "Kategorie:Befehle"
