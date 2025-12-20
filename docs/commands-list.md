---
# cSpell:locale en
alias:
    name: list-of-orders
    text: List of orders
---
# List of orders

Unter "K/L" ist vermerkt, ob der [Befehl] ein kurzer oder langer Befehl ist. Eine Einheit kann pro Runde nur einen langen Befehl ausführen, aber beliebig viele kurze.

[<sup>(l)</sup>] bezeichnet einen [pseudolangen Befehl][Befehl], der einer Einheit mehrfach gegeben werden kann. Allerdings kann kein weiterer anderer langer Befehl ausgeführt werden. Näheres dazu ist auf der Seite des jeweiligen Befehls nachzulesen.

Kurzliste der Befehle

| Befehl                                         | Beschreibung                                 | K/L     |
|------------------------------------------------|----------------------------------------------|---------|
| [//]                                           | bleibender Kommentar                         | [S]     |
| [[cmd-work]]                                       | verdient 10 Silber oder mehr                 | [L]     |
| [`ATTACK <unit id>`]                           | greift die Einheit an                        | [(l)] 1 |
| [`BANNER "<text>"`]                            | setzt Text für Adressliste                   | [S]     |
| [`CLAIM <number> <item>`]                      | holt Gegenstände aus Parteipool              | [S]     |
| [[cmd-promote]]                                    | macht Einheit zu Helden                      | [S]     |
| [`STEAL <unit id>`]                            | klaut 50 Silber oder mehr                    | [L]     |
| [`NAME UNIT "<name>"`]                         | benennt Objekte                              | [S]     |
| [`NAME FACTION "<name>"`]                      |                                              | [S]     |
| [`NAME BUILDING "<name>"`]                     |                                              | [S]     |
| [`NAME SHIP "<name>"`]                         |                                              | [S]     |
| [`NAME REGION "<name>"`]                       |                                              | [S]     |
| [`NAME FREMDE UNIT einheit "<name>"`]          | benennt fremde und unbenannte Objekte        | [S]     |
| [`NAME FREMDES SHIP schiff "<name>"`]          |                                              | [S]     |
| [`NAME FREMDES BUILDING gebäude "<name>"`]     |                                              | [S]     |
| [`NAME FREMDE FACTION partei "<name>"`]        |                                              | [S]     |
| [`USE [<number>] trank`]                       | benutzt alchemistischen Trank                | [S]     |
| [`DESCRIBE UNIT "<text>"`]                     | beschreibt Objekte                           | [S]     |
| [`DESCRIBE PRIVAT "<text>"`]                   |                                              | [S]     |
| [`DESCRIBE BUILDING "<text>"`]                 |                                              | [S]     |
| [`DESCRIBE SHIP "<text>"`]                     |                                              | [S]     |
| [`DESCRIBE REGION "<text>"`]                   |                                              | [S]     |
| [`ENTER BUILDING <building id>`]               | betritt Gebäude                              | [S]     |
| [`ENTER SHIP <ship id>`]                       | betritt Schiffe                              | [S]     |
| [`GUARD [NOT]`]                                | bewacht die Region                           | [S]     |
| [`PAY NOT [<building id>]`]                    | bezahlt den Unterhalt für ein Gebäude nicht  | [S]     |
| [`MESSAGE REGION "<text>"`]                    | versendet Botschaften                        | [S]     |
| [`MESSAGE SHIP <ship id> "<text>"`]            | versendet Botschaften                        | [S]     |
| [`MESSAGE BUILDING <building id> "<text>"`]    | versendet Botschaften                        | [S]     |
| [`MESSAGE UNIT <unit id> "<text>"`]            |                                              | [S]     |
| [`MESSAGE FACTION <faction id> "<text>"`]      |                                              | [S]     |
| [`DEFAULT "Orders"`]                           | setzt Default-Befehl für die nächste Runde.  | [S]     |
| [`UNIT <unit id>`]                             | beginnt Befehle für eine Einheit             | [S]     |
| [`EMAIL email@adresse`]                        | setzt die E-Mail-Adresse                     | [S]     |
| [[cmd-end]]                                        | beendet MAKE TEMP                            | [S]     |
| [`ERESSEA <faction id> "passwort"`]            | beginnt Befehle für Partei                   | [S]     |
| [`RIDE <unit id>`]                             | sich transportieren lassen                   | [L]     |
| [`FOLLOW UNIT <unit id>`]                      | folgt einer Einheit                          | [(l)] 2 |
| [`FOLLOW SHIP <ship id>`]                      | folgt einem Schiff                           | [(l)] 2 |
| [`RESEARCH HERBS`]                             | sucht Kräuter                                | [L]     |
| [`GIVE <unit id> herb`]                        | gibt einer Einheit alle Kräuter              | [S]     |
| [`GIVE <unit id> KOMMANDO`]                    | übergibt Kommando über Schiff/Gebäude        | [S]     |
| [`GIVE <unit id> UNIT`]                        | übergibt Einheit an fremde Partei            | [S]     |
| [`GIVE <unit id> [JE] <number> PERSONS`]       | übergibt Personen                            | [S]     |
| [`GIVE <unit id> [JE] <number> SHIP`]          | übergibt SHIP zur Bildung von Konvois        | [S]     |
| [`GIVE <unit id> [JE] <number> SILVER`]        | übergibt Silber                              | [S]     |
| [`GIVE <unit id> [JE] <number> <item>`]        | übergibt Gegenstände                         | [S]     |
| [`GIVE 0 <number> SILVER`]                     | gibt Gegenstände an die Bauern               | [S]     |
| [`GIVE 0 <number> PERSONS`]                    |                                              | [S]     |
| [`GIVE 0 <number> <item>`]                     |                                              | [S]     |
| [`GROUP ["<name>"]`]                           | Gruppieren von Einheiten                     | [S]     |
| [`HELP <faction id> ALLES [NOT]`]              | setzt / löscht einseitige Allianz            | [S]     |
| [`HELP <faction id> GIVE [NOT]`]               |                                              | [S]     |
| [`HELP <faction id> COMBAT [NOT]`]             |                                              | [S]     |
| [`HELP <faction id> GUARD [NOT]`]              |                                              | [S]     |
| [`HELP <faction id> SILVER [NOT]`]             |                                              | [S]     |
| [`HELP <faction id> PARTEITARNUNG [NOT]`]      |                                              | [S]     |
| [[cmd-combat]]                                     | setzt Verhalten im Kampf                     | K       |
| [`COMBAT AGGRESSIVE`]                          |                                              | [S]     |
| [`COMBAT DEFENSIVE`]                           |                                              | [S]     |
| [`COMBAT FLEE`]                                |                                              | [S]     |
| [`COMBAT HELP [NOT]`]                          | der Einheit wird im Kampf nicht geholfen     | [S]     |
| [`COMBAT REAR`]                                |                                              | [S]     |
| [`COMBAT NOT`]                                 |                                              | [S]     |
| [`COMBATSPELL [LEVEL n] "zauberspruch" [NOT]`] | setzt Zauber für Kämpfe                      | [S]     |
| [`BUY <number> luxusgut`]                      | kaufe Luxusgüter                             | [(l)] 3 |
| [`CONTACT <unit id>`]                          | kontaktiere fremde Einheiten                 | [S]     |
| [`TEACH <unit id> [<unit id> etc.]`]           | lehre Einheiten                              | [L]     |
| [`LEARN <skill>`]                              | Talent lernen                                | [L]     |
| [`LEARN AUTO <skill>`]                         | Talent lernen oder lehren                    | [L]     |
| [`LOCALE en/de`]                               | zeigt die Sprache der Befehle an             | [S]     |
| [`MAKE TEMP unit-alias-nr ["<name>"]`]         | erschaffe neue Einheit                       | [S]     |
| [`MAKE [stufe] gebäude-typ [<building id>]`]   | erweitere oder baue neues Gebäude            | [L]     |
| [`MAKE [stufe] schiffstyp`]                    | baue neue Schiffe                            | [L]     |
| [`MAKE [stufe] SHIP [<ship id>]`]              | baue weiter am Schiff                        | [L]     |
| [[cmd-make]]                                       | baue weiter an Gebäude/Schiff                | [L]     |
| [`MAKE [stufe] STRASSE richtung`]              | baue Straßen                                 | [L]     |
| [`MAKE [<number>] herb`]                       | suche Kräuter der Region                     | [L]     |
| [`MAKE [<number>] trank`]                      | MAKE einen alchemistischen Trank             | [L]     |
| [`MAKE [<number>] <item>`]                     | MAKE einen Gegenstand oder baue Rohstoffe ab | [L]     |
| [`MOVE richtung [richtung etc.]`]              | reisen                                       | [L]     |
| [`NEXT] | beendet Befehle | [S] |
| [`NUMBER UNIT [neue\_nr]`] | vergibt neue Nummer | [S] |
| [`NUMBER BUILDING [neue\_nr]`] |     | [S] |
| [`NUMBER FACTION [neue\_nr]`] |     | [S] |
| [`NUMBER SHIP [neue\_nr]`] |     | [S] |
| [`OPTION AUSWERTUNG [NOT]`] | verschiedene Einstellungen | [S] |
| [`OPTION COMPUTER [NOT]`] |     | [S] |
| [`OPTION ZIPPED [NOT]`] |     | [S] |
| [`OPTION BZIP2 [NOT]`] |     | [S] |
| [`OPTION SILBERPOOL [NOT]`] |     | [S] |
| [`OPTION MATERIALPOOL [NOT]`] |     | [S] |
| [`OPTION ADRESSEN [NOT]`] |     | [S] |
| [`OPTION ZUGVORLAGE [NOT]`] |     | [S] |
| [`OPTION STATISTIK [NOT]`] |     | [S] |
| [`OPTION TALENTVERSCHIEBUNG [NOT]`] |     | [S] |
| [`OPTION PUNKTE [NOT]`] |     | [S] |
| [`PASSWORD "neues-passwort"`] | setzt neues Passwort | [S] |
| [`PLANT [<number>] herb`] | pflanzt Kräuter | [L] |
| [`PLANT [<number>] BÄUME`] | pflanzt Samen | [L] |
| [`PLANT [<number>] MALLORNSAMEN`] | pflanzt Samen | [L] |
| [`PLANT [<number>] SAMEN`] | pflanzt Samen | [L] |
| [`PIRACY [partei\_1] [partei\_2] [...]`] | Piraterie setzen | [L] |
| [`PREFIX [präfix]`] | gibt der Rassenbezeichnung ein Präfix | [S] |
| [`REGION x,y`] | keine Funktion (nur für Tools) | [S] |
| [`RECRUIT <number>`] | rekrutiert weitere Personen | [S] |
| [`RESERVE <number> "<item>"`] | Gegenstände reservieren | [S] |
| [`RESERVE <number> SILVER`] | Silber reservieren | [S] |
| [`ROUTE richtung [richtung etc.]`] | reisen | [L] |
| [`SORT BEFORE <unit id>`] | Einheit in Report sortieren | [S] |
| [`SORT AFTER <unit id>`] |     | [S] |
| [`SPY <unit id>`] | Einheit ausspionieren | [L] |
| [`LANGUAGE en/de`] | ändert die Sprache der Partei | [S] |
| [`QUIT "passwort" [FACTION <faction id>]`] | aus dem Spiel ausscheiden | [S] |
| [`HIDE [stufe]`] | Tarnstufe setzen | [S] |
| [`HIDE rasse`] | Dämonen: als andere Rasse tarnen | [S] |
| [`HIDE FACTION [NOT]`] | Parteizugehörigkeit verbergen (als "anonym" getarnt) | [S] |
| [`HIDE FACTION NUMBER nummer`] | Parteizugehörigkeit tarnen (als andere Partei getarnt) | [S] |
| [`CARRY <unit id>`] | andere Einheiten mitnehmen | [S] |
| [`TAX [betrag]`] | Steuern eintreiben | [L] |
| [`ENTERTAIN [betrag]`] | verdient 20 oder mehr Silber | [L] |
| [`ORIGIN x y`] | setzt den Koordinaten-Ursprung | [S] |
| [`FORGET <skill>`] | vergisst das Talent | [S] |
| [`SELL anzah`l luxusgut] | verkauft Luxusgüter | [(l)] 3 |
| [`SELL ALLES luxusgut`] |     |     |
| [`LEAVE] | Schiff oder Gebäude verlassen | [S] |
| [`CAST [REGION x y] [LEVEL n] "zauberspruch" [...]`] | Zaubern | [(l)] 4 |
| [`SHOW ALLE ZAUBER`] | zeigt Beschreibung aller bekannten Zauber | [S] |
| [`SHOW ALLE TRÄNKE`] | zeigt Beschreibung aller bekannten Tränke | [S] |
| [`SHOW "Gegenstand"`] | zeigt Beschreibung eines Gegenstands | [S] |
| [`SHOW "Trank"`] | zeigt Beschreibung des Tranks | [S] |
| [`SHOW "Zauberspruch"`] | zeigt Beschreibung des Zaubers | [S] |
| [`SHOW "Rasse"`] | zeigt Beschreibung der Rasse der Einheit | [S] |
| [`DESTROY [stufen]`] | Gebäude oder Schiff verkleinern | [L] |
| [`DESTROY [stufen]`] STRASSE richtung | Straße einreißen | [L] |
| [`GROW PFERDE`] | Pferde züchten - nur in Pferdezucht | L   |

<!-- [//]: ./cmd-comment-slash.md-->
[S]: ./commands.md#short-and-long-orders
[L]: ./commands.md#short-and-long-orders
[`ATTACK <unit id>`]: ./cmd-attack.md
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
[`GIVE <unit id> [JE] <number> PERSONS`]: ./cmd-give.md
[`GIVE <unit id> [JE] <number> SHIP`]: ./cmd-give.md
[`GIVE <unit id> [JE] <number> SILVER`]: ./cmd-give.md
[`GIVE <unit id> [JE] <number> <item>`]: ./cmd-give.md
[`GIVE 0 <number> SILVER`]: ./cmd-give.md
[`GIVE 0 <number> PERSONS`]: ./cmd-give.md
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

<sup>1</sup> der Befehl ist nicht immer lang, siehe [Kampfende]  
<sup>2</sup> bewegt sich die verfolgte Einheit nicht, kann stattdessen ein anderer langer Befehl ausgeführt werden  
<sup>3</sup> ein BUY- und mehrere SELL-Befehle können kombiniert werden  
<sup>4</sup> eine Einheit kann mehrere Zauber ausführen

## See also

- [Befehle]
- [Befehlsreihenfolge]

Continue reading: [Der erste Zug].

[Der erste Zug]: ./first-round.md

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[Befehl]: ./commands.md
[<sup>(l)</sup>]: ./commands.md#short-and-long-orders
[Kampfende]: ./war.md#the-end
[Befehle]: ./commands.md
[Befehlsreihenfolge]: ./commands-sequence.md
