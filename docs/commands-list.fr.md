---
# cSpell:locale fr, en
alias: tableau-recapitulatif-des-ordres
---
# Tableau récapitulatif des ordres

Unter "K/L" ist vermerkt, ob der [Befehl] ein kurzer oder langer Befehl ist. Eine Einheit kann pro Runde nur einen langen Befehl ausführen, aber beliebig viele kurze.

[<sup>(l)</sup>] bezeichnet einen [pseudolangen Befehl][Befehl], der einer Einheit mehrfach gegeben werden kann. Allerdings kann kein weiterer anderer langer Befehl ausgeführt werden. Näheres dazu ist auf der Seite des jeweiligen Befehls nachzulesen.

| Ordre                                                | Description                                            | C/L     |
|------------------------------------------------------|--------------------------------------------------------|---------|
| [//]                                                 | bleibender Kommentar                                   | [C]     |
| [[cmd-work]]                                         | verdient 10 Silber oder mehr                           | [L]     |
| [`ATTACK <unit id>`]                                 | greift die Einheit an                                  | [(l)] 1 |
| [`BANNER "<text>"`]                                  | setzt Text für Adressliste                             | [C]     |
| [`CLAIM <number> <item>`]                            | holt Gegenstände aus Parteipool                        | [C]     |
| [[cmd-promote]]                                      | macht Einheit zu Helden                                | [C]     |
| [`STEAL <unit id>`]                                  | klaut 50 Silber oder mehr                              | [L]     |
| [`NAME UNIT "<name>"`]                               | benennt Objekte                                        | [C]     |
| [`NAME FACTION "<name>"`]                            |                                                        | [C]     |
| [`NAME BUILDING "<name>"`]                           |                                                        | [C]     |
| [`NAME SHIP "<name>"`]                               |                                                        | [C]     |
| [`NAME REGION "<name>"`]                             |                                                        | [C]     |
| [`NAME FREMDE UNIT einheit "<name>"`]                | benennt fremde und unbenannte Objekte                  | [C]     |
| [`NAME FREMDES SHIP schiff "<name>"`]                |                                                        | [C]     |
| [`NAME FREMDES BUILDING gebäude "<name>"`]           |                                                        | [C]     |
| [`NAME FREMDE FACTION partei "<name>"`]              |                                                        | [C]     |
| [`USE [<number>] potion`]                            | benutzt alchemistischen Trank                          | [C]     |
| [`DESCRIBE UNIT "<text>"`]                           | beschreibt Objekte                                     | [C]     |
| [`DESCRIBE PRIVAT "<text>"`]                         |                                                        | [C]     |
| [`DESCRIBE BUILDING "<text>"`]                       |                                                        | [C]     |
| [`DESCRIBE SHIP "<text>"`]                           |                                                        | [C]     |
| [`DESCRIBE REGION "<text>"`]                         |                                                        | [C]     |
| [`ENTER BUILDING <building id>`]                     | betritt Gebäude                                        | [C]     |
| [`ENTER SHIP <ship id>`]                             | betritt Schiffe                                        | [C]     |
| [`GUARD [NOT]`]                                      | bewacht die Region                                     | [C]     |
| [`PAY NOT [<building id>]`]                          | bezahlt den Unterhalt für ein Gebäude nicht            | [C]     |
| [`MESSAGE REGION "<text>"`]                          | versendet Botschaften                                  | [C]     |
| [`MESSAGE SHIP <ship id> "<text>"`]                  | versendet Botschaften                                  | [C]     |
| [`MESSAGE BUILDING <building id> "<text>"`]          | versendet Botschaften                                  | [C]     |
| [`MESSAGE UNIT <unit id> "<text>"`]                  |                                                        | [C]     |
| [`MESSAGE FACTION <faction id> "<text>"`]            |                                                        | [C]     |
| [`DEFAULT "Ordres"`]                                 | setzt Default-Befehl für die nächste Runde.            | [C]     |
| [`UNIT <unit id>`]                                   | beginnt Befehle für eine Einheit                       | [C]     |
| [`EMAIL email@adresse`]                              | setzt die E-Mail-Adresse                               | [C]     |
| [[cmd-end]]                                          | beendet MAKE TEMP                                      | [C]     |
| [`ERESSEA <faction id> "passwort"`]                  | beginnt Befehle für Partei                             | [C]     |
| [`RIDE <unit id>`]                                   | sich transportieren lassen                             | [L]     |
| [`FOLLOW UNIT <unit id>`]                            | folgt einer Einheit                                    | [(l)] 2 |
| [`FOLLOW SHIP <ship id>`]                            | folgt einem Schiff                                     | [(l)] 2 |
| [`RESEARCH HERBS`]                                   | sucht Kräuter                                          | [L]     |
| [`GIVE <unit id> herb`]                              | gibt einer Einheit alle Kräuter                        | [C]     |
| [`GIVE <unit id> KOMMANDO`]                          | übergibt Kommando über Schiff/Gebäude                  | [C]     |
| [`GIVE <unit id> UNIT`]                              | übergibt Einheit an fremde Partei                      | [C]     |
| [`GIVE <unit id> [EACH] <number> MEN`]               | übergibt Personen                                      | [C]     |
| [`GIVE <unit id> [EACH] <number> SHIP`]              | übergibt SHIP zur Bildung von Konvois                  | [C]     |
| [`GIVE <unit id> [EACH] <number> SILVER`]            | übergibt Silber                                        | [C]     |
| [`GIVE <unit id> [EACH] <number> <item>`]            | übergibt Gegenstände                                   | [C]     |
| [`GIVE 0 <number> SILVER`]                           | gibt Gegenstände an die Bauern                         | [C]     |
| [`GIVE 0 <number> MEN`]                              |                                                        | [C]     |
| [`GIVE 0 <number> <item>`]                           |                                                        | [C]     |
| [`GROUP ["<name>"]`]                                 | Gruppieren von Einheiten                               | [C]     |
| [`HELP <faction id> ALL [NOT]`]                      | setzt / löscht einseitige Allianz                      | [C]     |
| [`HELP <faction id> GIVE [NOT]`]                     |                                                        | [C]     |
| [`HELP <faction id> COMBAT [NOT]`]                   |                                                        | [C]     |
| [`HELP <faction id> GUARD [NOT]`]                    |                                                        | [C]     |
| [`HELP <faction id> SILVER [NOT]`]                   |                                                        | [C]     |
| [`HELP <faction id> PARTEITARNUNG [NOT]`]            |                                                        | [C]     |
| [[cmd-combat]]                                       | setzt Verhalten im Kampf                               | K       |
| [`COMBAT AGGRESSIVE`]                                |                                                        | [C]     |
| [`COMBAT DEFENSIVE`]                                 |                                                        | [C]     |
| [`COMBAT FLEE`]                                      |                                                        | [C]     |
| [`COMBAT HELP [NOT]`]                                | der Einheit wird im Kampf nicht geholfen               | [C]     |
| [`COMBAT REAR`]                                      |                                                        | [C]     |
| [`COMBAT NOT`]                                       |                                                        | [C]     |
| [`COMBATSPELL [LEVEL n] "zauberspruch" [NOT]`]       | setzt Zauber für Kämpfe                                | [C]     |
| [`BUY <number> luxusgut`]                            | kaufe Luxusgüter                                       | [(l)] 3 |
| [`CONTACT <unit id>`]                                | kontaktiere fremde Einheiten                           | [C]     |
| [`TEACH <unit id> [<unit id> etc.]`]                 | lehre Einheiten                                        | [L]     |
| [`LEARN <skill>`]                                    | Talent lernen                                          | [L]     |
| [`LEARN AUTO <skill>`]                               | Talent lernen oder lehren                              | [L]     |
| [`LOCALE en/de`]                                     | zeigt die Sprache der Befehle an                       | [C]     |
| [`MAKE TEMP unit-alias-nr ["<name>"]`]               | erschaffe neue Einheit                                 | [C]     |
| [`MAKE [stufe] gebäude-typ [<building id>]`]         | erweitere oder baue neues Gebäude                      | [L]     |
| [`MAKE [stufe] schiffstyp`]                          | baue neue Schiffe                                      | [L]     |
| [`MAKE [stufe] SHIP [<ship id>]`]                    | baue weiter am Schiff                                  | [L]     |
| [[cmd-make]]                                         | baue weiter an Gebäude/Schiff                          | [L]     |
| [`MAKE [stufe] STRASSE richtung`]                    | baue Straßen                                           | [L]     |
| [`MAKE [<number>] herb`]                             | suche Kräuter der Region                               | [L]     |
| [`MAKE [<number>] trank`]                            | MAKE einen alchemistischen Trank                       | [L]     |
| [`MAKE [<number>] <item>`]                           | MAKE einen Gegenstand oder baue Rohstoffe ab           | [L]     |
| [`MOVE richtung [richtung etc.]`]                    | reisen                                                 | [L]     |
| [`NEXT`]                                             | beendet Befehle                                        | [C]     |
| [`NUMBER UNIT [neue\_nr]`]                           | vergibt neue Nummer                                    | [C]     |
| [`NUMBER BUILDING [neue\_nr]`]                       |                                                        | [C]     |
| [`NUMBER FACTION [neue\_nr]`]                        |                                                        | [C]     |
| [`NUMBER SHIP [neue\_nr]`]                           |                                                        | [C]     |
| [`OPTION AUSWERTUNG [NOT]`]                          | verschiedene Einstellungen                             | [C]     |
| [`OPTION COMPUTER [NOT]`]                            |                                                        | [C]     |
| [`OPTION ZIPPED [NOT]`]                              |                                                        | [C]     |
| [`OPTION BZIP2 [NOT]`]                               |                                                        | [C]     |
| [`OPTION SILBERPOOL [NOT]`]                          |                                                        | [C]     |
| [`OPTION MATERIALPOOL [NOT]`]                        |                                                        | [C]     |
| [`OPTION ADRESSEN [NOT]`]                            |                                                        | [C]     |
| [`OPTION ZUGVORLAGE [NOT]`]                          |                                                        | [C]     |
| [`OPTION STATISTIK [NOT]`]                           |                                                        | [C]     |
| [`OPTION TALENTVERSCHIEBUNG [NOT]`]                  |                                                        | [C]     |
| [`OPTION PUNKTE [NOT]`]                              |                                                        | [C]     |
| [`PASSWORD "neues-passwort"`]                        | setzt neues Passwort                                   | [C]     |
| [`PLANT [<number>] herb`]                            | pflanzt Kräuter                                        | [L]     |
| [`PLANT [<number>] BÄUME`]                           | pflanzt Samen                                          | [L]     |
| [`PLANT [<number>] MALLORNSAMEN`]                    | pflanzt Samen                                          | [L]     |
| [`PLANT [<number>] SAMEN`]                           | pflanzt Samen                                          | [L]     |
| [`PIRACY [partei\_1] [partei\_2] [...]`]             | Piraterie setzen                                       | [L]     |
| [`PREFIX [präfix]`]                                  | gibt der Rassenbezeichnung ein Präfix                  | [C]     |
| [`REGION x,y`]                                       | keine Funktion (nur für Tools)                         | [C]     |
| [`RECRUIT <number>`]                                 | rekrutiert weitere Personen                            | [C]     |
| [`RESERVE <number> "<item>"`]                        | Gegenstände reservieren                                | [C]     |
| [`RESERVE <number> SILVER`]                          | Silber reservieren                                     | [C]     |
| [`ROUTE richtung [richtung etc.]`]                   | reisen                                                 | [L]     |
| [`SORT BEFORE <unit id>`]                            | Einheit in Report sortieren                            | [C]     |
| [`SORT AFTER <unit id>`]                             |                                                        | [C]     |
| [`SPY <unit id>`]                                    | Einheit ausspionieren                                  | [L]     |
| [`LANGUAGE en/de`]                                   | ändert die Sprache der Partei                          | [C]     |
| [`QUIT "passwort" [FACTION <faction id>]`]           | aus dem Spiel ausscheiden                              | [C]     |
| [`HIDE [stufe]`]                                     | Tarnstufe setzen                                       | [C]     |
| [`HIDE rasse`]                                       | Dämonen: als andere Rasse tarnen                       | [C]     |
| [`HIDE FACTION [NOT]`]                               | Parteizugehörigkeit verbergen (als "anonym" getarnt)   | [C]     |
| [`HIDE FACTION NUMBER nummer`]                       | Parteizugehörigkeit tarnen (als andere Partei getarnt) | [C]     |
| [`CARRY <unit id>`]                                  | andere Einheiten mitnehmen                             | [C]     |
| [`TAX [betrag]`]                                     | Steuern eintreiben                                     | [L]     |
| [`ENTERTAIN [betrag]`]                               | verdient 20 oder mehr Silber                           | [L]     |
| [`ORIGIN x y`]                                       | setzt den Koordinaten-Ursprung                         | [C]     |
| [`FORGET <skill>`]                                   | vergisst das Talent                                    | [C]     |
| [`SELL anzah`l luxusgut]                             | verkauft Luxusgüter                                    | [(l)] 3 |
| [`SELL ALL luxusgut`]                                |                                                        |         |
| [`LEAVE]                                             | Schiff oder Gebäude verlassen                          | [C]     |
| [`CAST [REGION x y] [LEVEL n] "zauberspruch" [...]`] | Zaubern                                                | [(l)] 4 |
| [`SHOW ALL ZAUBER`]                                  | zeigt Beschreibung aller bekannten Zauber              | [C]     |
| [`SHOW ALL TRÄNKE`]                                  | zeigt Beschreibung aller bekannten Tränke              | [C]     |
| [`SHOW "Gegenstand"`]                                | zeigt Beschreibung eines Gegenstands                   | [C]     |
| [`SHOW "Trank"`]                                     | zeigt Beschreibung des Tranks                          | [C]     |
| [`SHOW "Zauberspruch"`]                              | zeigt Beschreibung des Zaubers                         | [C]     |
| [`SHOW "Rasse"`]                                     | zeigt Beschreibung der Rasse der Einheit               | [C]     |
| [`DESTROY [stufen]`]                                 | Gebäude oder Schiff verkleinern                        | [L]     |
| [`DESTROY [stufen]`] STRASSE richtung                | Straße einreißen                                       | [L]     |
| [`GROW PFERDE`]                                      | Pferde züchten - nur in Pferdezucht                    | L       |

<!-- [//]: ./cmd-comment-slash.md-->

<sup>1</sup> der Befehl ist nicht immer lang, siehe [Kampfende]  
<sup>2</sup> bewegt sich die verfolgte Einheit nicht, kann stattdessen ein anderer langer Befehl ausgeführt werden  
<sup>3</sup> ein BUY- und mehrere SELL-Befehle können kombiniert werden  
<sup>4</sup> eine Einheit kann mehrere Zauber ausführen

## Voir aussi

- [Befehle]
- [Befehlsreihenfolge]

Poursuivre la lecture : [Der erste Zug].

[Der erste Zug]: ./first-round.md

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[L]: ./commands.md#ordres-courts-et-longs
[`ATTACK <unit id>`]: ./cmd-attack.md
[(l)]: ./commands.md#ordres-courts-et-longs
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
[`DEFAULT "Ordres"`]: ./cmd-default.md
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
[`GIVE <unit id> [EACH] <number> MEN`]: ./cmd-give.md
[`GIVE <unit id> [EACH] <number> SHIP`]: ./cmd-give.md
[`GIVE <unit id> [EACH] <number> SILVER`]: ./cmd-give.md
[`GIVE <unit id> [EACH] <number> <item>`]: ./cmd-give.md
[`GIVE 0 <number> SILVER`]: ./cmd-give.md
[`GIVE 0 <number> MEN`]: ./cmd-give.md
[`GIVE 0 <number> <item>`]: ./cmd-give.md
[`GROUP ["<name>"]`]: ./cmd-group.md
[`HELP <faction id> ALL [NOT]`]: ./cmd-help.md
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
[`LEARN <skill>`]: ./Learn.md
[`LEARN AUTO <skill>`]: ./Learn-auto.md
[`LOCALE en/de`]: ./Locale.md
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
[`LANGUAGE en/de`]: ./Language.md
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
[`SELL ALL luxusgut`]: ./cmd-sell.md
[`LEAVE`]: ./Leave.md
[`CAST [REGION x y] [LEVEL n] "zauberspruch" [...]`]: ./cmd-cast.md
[`SHOW ALL ZAUBER`]: ./cmd-show.md
[`SHOW ALL TRÄNKE`]: ./cmd-show.md
[`SHOW "Gegenstand"`]: ./cmd-show.md
[`SHOW "Trank"`]: ./cmd-show.md
[`SHOW "Zauberspruch"`]: ./cmd-show.md
[`SHOW "Rasse"`]: ./cmd-show.md
[`DESTROY [stufen]`]: ./cmd-destroy.md
[`GROW PFERDE`]: ./cmd-grow.md

[Befehl]: ./commands.md
[Befehle]: ./commands.md
[Befehlsreihenfolge]: ./commands-sequence.md

[<sup>(l)</sup>]: ./commands.md#ordres-courts-et-longs
[Kampfende]: ./war.md#fin-du-combat
