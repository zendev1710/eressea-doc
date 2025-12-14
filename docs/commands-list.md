---
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

<!-- [//]: ./cmd-comment-slash.md "KOMMENTAR"-->
[S]: ./commands.md#short-and-long-orders "Orders"
[L]: ./commands.md#short-and-long-orders "Orders"
[`ATTACK <unit id>`]: ./cmd-attack.md "ATTACK"
[(l)]: ./commands.md#short-and-long-orders "Orders"
[`BANNER "<text>"`]: ./cmd-banner.md "BANNER"
[`CLAIM <number> <item>`]: ./cmd-claim.md "CLAIM"
[`STEAL <unit id>`]: ./camouflage.md "STEAL"
[`NAME UNIT "<name>"`]: ./cmd-name.md "NAME"
[`NAME FACTION "<name>"`]: ./cmd-name.md "NAME"
[`NAME BUILDING "<name>"`]: ./cmd-name.md "NAME"
[`NAME SHIP "<name>"`]: ./cmd-name.md "NAME"
[`NAME REGION "<name>"`]: ./cmd-name.md "NAME"
[`NAME FREMDE UNIT einheit "<name>"`]: ./cmd-name.md "NAME"
[`NAME FREMDES SHIP schiff "<name>"`]: ./cmd-name.md "NAME"
[`NAME FREMDES BUILDING gebäude "<name>"`]: ./cmd-name.md "NAME"
[`NAME FREMDE FACTION partei "<name>"`]: ./cmd-name.md "NAME"
[`USE [<number>] trank`]: ./cmd-use.md "USE"
[`DESCRIBE UNIT "<text>"`]: ./cmd-describe.md "DESCRIBE"
[`DESCRIBE PRIVAT "<text>"`]: ./cmd-describe.md "DESCRIBE"
[`DESCRIBE BUILDING "<text>"`]: ./cmd-describe.md "DESCRIBE"
[`DESCRIBE SHIP "<text>"`]: ./cmd-]describe.md "DESCRIBE"
[`DESCRIBE REGION "<text>"`]: ./cmd-describe.md "DESCRIBE"
[`ENTER BUILDING <building id>`]: ./cmd-enter.md "ENTER"
[`ENTER SHIP <ship id>`]: ./cmd-enter.md "ENTER"
[`GUARD [NOT]`]: ./cmd-guard.md "GUARD"
[`PAY NOT [<building id>]`]: ./cmd-pay-not.md "PAY"
[`MESSAGE REGION "<text>"`]: ./cmd-message.md "MESSAGE"
[`MESSAGE SHIP <ship id> "<text>"`]: ./cmd-message.md "MESSAGE"
[`MESSAGE BUILDING <building id> "<text>"`]: ./cmd-message.md "MESSAGE"
[`MESSAGE UNIT <unit id> "<text>"`]: ./cmd-message.md "MESSAGE"
[`MESSAGE FACTION <faction id> "<text>"`]: ./cmd-message.md "MESSAGE"
[`DEFAULT "Orders"`]: ./cmd-default.md "DEFAULT"
[`UNIT <unit id>`]: ./cmd-unit.md "UNIT"
[`EMAIL email@adresse`]: ./cmd-email.md "EMAIL"
[`END`]: ./cmd-end.md "END"
[`ERESSEA <faction id> "passwort"`]: ./cmd-eressea.md "ERESSEA"
[`RIDE <unit id>`]: ./cmd-ride.md "RIDE"
[`FOLLOW UNIT <unit id>`]: ./cmd-follow.md "FOLLOW"
[`FOLLOW SHIP <ship id>`]: ./cmd-follow.md "FOLLOW"
[`RESEARCH HERBS`]: ./cmd-research.md "RESEARCH"
[`GIVE <unit id> herb`]: ./cmd-give.md "GIVE"
[`GIVE <unit id> KOMMANDO`]: ./cmd-give.md "GIVE"
[`GIVE <unit id> UNIT`]: ./cmd-give.md "GIVE"
[`GIVE <unit id> [JE] <number> PERSONS`]: ./cmd-give.md "GIVE"
[`GIVE <unit id> [JE] <number> SHIP`]: ./cmd-give.md "GIVE"
[`GIVE <unit id> [JE] <number> SILVER`]: ./cmd-give.md "GIVE"
[`GIVE <unit id> [JE] <number> <item>`]: ./cmd-give.md "GIVE"
[`GIVE 0 <number> SILVER`]: ./cmd-give.md "GIVE"
[`GIVE 0 <number> PERSONS`]: ./cmd-give.md "GIVE"
[`GIVE 0 <number> <item>`]: ./cmd-give.md "GIVE"
[`GROUP ["<name>"]`]: ./cmd-group.md "GROUP"
[`HELP <faction id> ALLES [NOT]`]: ./cmd-help.md "HELP"
[`HELP <faction id> GIVE [NOT]`]: ./cmd-help.md "HELP"
[`HELP <faction id> COMBAT [NOT]`]: ./cmd-help.md "HELP"
[`HELP <faction id> GUARD [NOT]`]: ./cmd-help.md "HELP"
[`HELP <faction id> SILVER [NOT]`]: ./cmd-help.md "HELP"
[`HELP <faction id> PARTEITARNUNG [NOT]`]: ./cmd-help.md "HELP"
[`COMBAT`]: ./cmd-combat.md "COMBAT"
[`COMBAT AGGRESSIVE`]: ./cmd-combat.md "COMBAT"
[`COMBAT DEFENSIVE``]: ./cmd-combat.md "COMBAT"
[`COMBAT FLEE`]: ./cmd-combat.md "COMBAT"
[`COMBAT HELP [NOT]`]: ./cmd-combat.md "COMBAT"
[`COMBAT REAR`]: ./cmd-combat.md "COMBAT"
[`COMBAT NOT`]: ./cmd-combat.md "COMBAT"
[`COMBATSPELL [LEVEL n] "zauberspruch" [NOT]`]: ./cmd-combatspell.md
[`BUY <number> luxusgut`]: ./cmd-buy.md "BUY"
[`CONTACT <unit id>`]: ./cmd-contact.md "CONTACT"
[`TEACH <unit id> [<unit id> etc.]`]: ./cmd-teach.md "TEACH"
[`LEARN <skill>`]: ./cmd-learn.md "LEARN"
[`LEARN AUTO <skill>`]: ./cmd-learn-auto.md "LEARN AUTO"
[`LOCALE en/de`]: ./cmd-locale.md "LOCALE"
[`MAKE TEMP unit-alias-nr ["<name>"]`]: ./cmd-make.md "MAKE"
[`MAKE [stufe] gebäude-typ [<building id>]`]: ./cmd-make.md "MAKE"
[`MAKE [stufe] schiffstyp`]: ./cmd-make.md "MAKE"
[`MAKE [stufe] SHIP [<ship id>]`]: ./cmd-make.md "MAKE"
[`MAKE`]: ./cmd-make.md "MAKE"
[`MAKE [stufe] STRASSE richtung`]: ./cmd-make.md "MAKE"
[`MAKE [<number>] <herb>`]: ./cmd-make.md "MAKE"
[`MAKE [<number>] trank`]: ./cmd-make.md "MAKE"
[`MAKE [<number>] <item>`]: ./cmd-make.md "MAKE"
[`MOVE richtung [richtung etc.]`]: ./cmd-move.md "MOVE"
[`NEXT`]: ./cmd-next.md "NEXT"
[`NUMBER UNIT [neue\_nr]`]: ./cmd-number.md "NUMBER"
[`NUMBER BUILDING [neue\_nr]`]: ./cmd-number.md "NUMBER"
[`NUMBER FACTION [neue\_nr]`]: ./cmd-number.md "NUMBER"
[`NUMBER SHIP [neue\_nr]`]: ./cmd-number.md "NUMBER"
[`OPTION AUSWERTUNG [NOT]`]: ./cmd-option.md "OPTION"
[`OPTION COMPUTER [NOT]`]: ./cmd-option.md "OPTION"
[`OPTION ZIPPED [NOT]`]: ./cmd-option.md "OPTION"
[`OPTION BZIP2 [NOT]`]: ./cmd-option.md "OPTION"
[`OPTION SILBERPOOL [NOT]`]: ./cmd-option.md "OPTION"
[`OPTION MATERIALPOOL [NOT]`]: ./cmd-option.md "OPTION"
[`OPTION ADRESSEN [NOT]`]: ./cmd-option.md "OPTION"
[`OPTION ZUGVORLAGE [NOT]`]: ./cmd-option.md "OPTION"
[`OPTION STATISTIK [NOT]`]: ./cmd-option.md "OPTION"
[`OPTION TALENTVERSCHIEBUNG [NOT]`]: ./cmd-option.md "OPTION"
[`OPTION PUNKTE [NOT]`]: ./cmd-option.md "OPTION"
[`PASSWORD "neues-passwort"`]: ./cmd-password.md "PASSWORD"
[`PLANT [<number>] herb`]: ./cmd-plant.md "PLANT"
[`PLANT [<number>] BÄUME`]: ./cmd-plant.md "PLANT"
[`PLANT [<number>] MALLORNSAMEN`]: ./cmd-plant.md "PLANT"
[`PLANT [<number>] SAMEN`]: ./cmd-plant.md "PLANT"
[`PIRACY [partei\_1] [partei\_2] [...]`]: ./cmd-piracy.md "PIRACY"
[`PREFIX [präfix]`]: ./cmd-prefix.md "PREFIX"
[`REGION x,y`]: ./cmd-region.md "REGION"
[`RECRUIT <number>`]: ./silver.md#recruter "RECRUIT"
[`RESERVE <number> "<item>"`]: ./cmd-reserve.md "RESERVE"
[`RESERVE <number> SILVER`]: ./cmd-reserve.md "RESERVE"
[`ROUTE richtung [richtung etc.]`]: ./cmd-route.md "ROUTE"
[`SORT BEFORE <unit id>`]: ./cmd-sort.md "SORT"
[`SORT AFTER <unit id>`]: ./cmd-sort.md "SORT"
[`SPY <unit id>`]: ./cmd-spy.md "SPY"
[`LANGUAGE en/de`]: ./cmd-language.md "LANGUAGE"
[`QUIT <passwort> [FACTION <faction id>]`]: ./cmd-quit.md "QUIT"
[`HIDE [stufe]`]: ./cmd-hide.md "HIDE"
[`HIDE rasse`]: ./cmd-hide.md "HIDE"
[`HIDE FACTION [NOT]`]: ./cmd-hide.md "HIDE"
[`HIDE FACTION NUMBER nummer`]: ./cmd-hide.md "HIDE"
[`CARRY <unit id>`]: ./cmd-carry.md "CARRY"
[`TAX [betrag]`]: ./cmd-tax.md "TAX"
[`ENTERTAIN [betrag]`]: ./cmd-entertain.md "ENTERTAIN"
[`ORIGIN x y`]: ./cmd-origin.md "ORIGIN"
[`FORGET <skill>`]: ./cmd-forget.md "FORGET"
[`SELL <number> luxusgut`]: ./cmd-sell.md "SELL"
[`SELL ALLES luxusgut`]: ./cmd-sell.md "SELL"
[`LEAVE`]: ./cmd-leave.md "LEAVE"
[`CAST [REGION x y] [LEVEL n] "zauberspruch" [...]`]: ./cmd-cast.md "CAST"
[`SHOW ALLE ZAUBER`]: ./cmd-show.md "SHOW"
[`SHOW ALLE TRÄNKE`]: ./cmd-show.md "SHOW"
[`SHOW "Gegenstand"`]: ./cmd-show.md "SHOW"
[`SHOW "Trank"`]: ./cmd-show.md "SHOW"
[`SHOW "Zauberspruch"`]: ./cmd-show.md "SHOW"
[`SHOW "Rasse"`]: ./cmd-show.md "SHOW"
[`DESTROY [stufen]`]: ./cmd-destroy.md "DESTROY"
[`GROW PFERDE`]: ./cmd-grow.md "GROW"

<sup>1</sup> der Befehl ist nicht immer lang, siehe [Kampfende]  
<sup>2</sup> bewegt sich die verfolgte Einheit nicht, kann stattdessen ein anderer langer Befehl ausgeführt werden  
<sup>3</sup> ein BUY- und mehrere SELL-Befehle können kombiniert werden  
<sup>4</sup> eine Einheit kann mehrere Zauber ausführen

## See also

- [Befehle]
- [Befehlsreihenfolge]

Continue reading: [Der erste Zug].

[Der erste Zug]: ./first-round.md "Der erste Zug"

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[Befehl]: ./commands.md "Orders"
[<sup>(l)</sup>]: ./commands.md#short-and-long-orders "Orders"
[Kampfende]: ./war.md#the-end "Fin de la bataille"
[Befehle]: ./commands.md "Befehle"
[Befehlsreihenfolge]: ./commands-sequence.md "Befehlsreihenfolge"
