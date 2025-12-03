# Kurzbeschreibung

Unter "K/L" ist vermerkt, ob der [Befehl] ein kurzer oder langer Befehl ist. Eine Einheit kann pro Runde nur einen langen Befehl ausführen, aber beliebig viele kurze.

[<sup>(l)</sup>] bezeichnet einen [pseudolangen Befehl][Befehl], der einer Einheit mehrfach gegeben werden kann. Allerdings kann kein weiterer anderer langer Befehl ausgeführt werden. Näheres dazu ist auf der Seite des jeweiligen Befehls nachzulesen.

Kurzliste der Befehle

| Befehl                                         | Beschreibung                                 | K/L     |
|------------------------------------------------|----------------------------------------------|---------|
| [//]                                           | bleibender Kommentar                         | [K]     |
| [`WORK`]                                       | verdient 10 Silber oder mehr                 | [L]     |
| [`ATTACK <unit id>`]                           | greift die Einheit an                        | [(l)] 1 |
| [`BANNER "<text>"`]                            | setzt Text für Adressliste                   | [K]     |
| [`CLAIM <number> <item>`]                      | holt Gegenstände aus Parteipool              | [K]     |
| [`PROMOTE`]                                    | macht Einheit zu Helden                      | [K]     |
| [`STEAL <unit id>`]                            | klaut 50 Silber oder mehr                    | [L]     |
| [`NAME UNIT "<name>"`]                         | benennt Objekte                              | [K]     |
| [`NAME FACTION "<name>"`]                      |                                              | [K]     |
| [`NAME BUILDING "<name>"`]                     |                                              | [K]     |
| [`NAME SHIP "<name>"`]                         |                                              | [K]     |
| [`NAME REGION "<name>"`]                       |                                              | [K]     |
| [`NAME FREMDE UNIT einheit "<name>"`]          | benennt fremde und unbenannte Objekte        | [K]     |
| [`NAME FREMDES SHIP schiff "<name>"`]          |                                              | [K]     |
| [`NAME FREMDES BUILDING gebäude "<name>"`]     |                                              | [K]     |
| [`NAME FREMDE FACTION partei "<name>"`]        |                                              | [K]     |
| [`USE [<number>] trank`]                       | benutzt alchemistischen Trank                | [K]     |
| [`DESCRIBE UNIT "<text>"`]                     | beschreibt Objekte                           | [K]     |
| [`DESCRIBE PRIVAT "<text>"`]                   |                                              | [K]     |
| [`DESCRIBE BUILDING "<text>"`]                 |                                              | [K]     |
| [`DESCRIBE SHIP "<text>"`]                     |                                              | [K]     |
| [`DESCRIBE REGION "<text>"`]                   |                                              | [K]     |
| [`ENTER BUILDING <building id>`]               | betritt Gebäude                              | [K]     |
| [`ENTER SHIP <ship id>`]                       | betritt Schiffe                              | [K]     |
| [`GUARD [NOT]`]                                | bewacht die Region                           | [K]     |
| [`PAY NOT [<building id>]`]                    | bezahlt den Unterhalt für ein Gebäude nicht  | [K]     |
| [`MESSAGE REGION "<text>"`]                    | versendet Botschaften                        | [K]     |
| [`MESSAGE SHIP <ship id> "<text>"`]            | versendet Botschaften                        | [K]     |
| [`MESSAGE BUILDING <building id> "<text>"`]    | versendet Botschaften                        | [K]     |
| [`MESSAGE UNIT <unit id> "<text>"`]            |                                              | [K]     |
| [`MESSAGE FACTION <faction id> "<text>"`]      |                                              | [K]     |
| [`DEFAULT "befehl"`]                           | setzt Default-Befehl für die nächste Runde.  | [K]     |
| [`UNIT <unit id>`]                             | beginnt Befehle für eine Einheit             | [K]     |
| [`EMAIL email@adresse`]                        | setzt die E-Mail-Adresse                     | [K]     |
| [`END`]                                        | beendet MAKE TEMP                            | [K]     |
| [`ERESSEA <faction id> "passwort"`]            | beginnt Befehle für Partei                   | [K]     |
| [`RIDE <unit id>`]                             | sich transportieren lassen                   | [L]     |
| [`FOLLOW UNIT <unit id>`]                      | folgt einer Einheit                          | [(l)] 2 |
| [`FOLLOW SHIP <ship id>`]                      | folgt einem Schiff                           | [(l)] 2 |
| [`RESEARCH HERBS`]                             | sucht Kräuter                                | [L]     |
| [`GIVE <unit id> herb`]                        | gibt einer Einheit alle Kräuter              | [K]     |
| [`GIVE <unit id> KOMMANDO`]                    | übergibt Kommando über Schiff/Gebäude        | [K]     |
| [`GIVE <unit id> UNIT`]                        | übergibt Einheit an fremde Partei            | [K]     |
| [`GIVE <unit id> [JE] <number> PERSONS`]       | übergibt Personen                            | [K]     |
| [`GIVE <unit id> [JE] <number> SHIP`]          | übergibt SHIP zur Bildung von Konvois        | [K]     |
| [`GIVE <unit id> [JE] <number> SILVER`]        | übergibt Silber                              | [K]     |
| [`GIVE <unit id> [JE] <number> <item>`]        | übergibt Gegenstände                         | [K]     |
| [`GIVE 0 <number> SILVER`]                     | gibt Gegenstände an die Bauern               | [K]     |
| [`GIVE 0 <number> PERSONS`]                    |                                              | [K]     |
| [`GIVE 0 <number> <item>`]                     |                                              | [K]     |
| [`GROUP ["<name>"]`]                           | Gruppieren von Einheiten                     | [K]     |
| [`HELP <faction id> ALLES [NOT]`]              | setzt / löscht einseitige Allianz            | [K]     |
| [`HELP <faction id> GIVE [NOT]`]               |                                              | [K]     |
| [`HELP <faction id> COMBAT [NOT]`]             |                                              | [K]     |
| [`HELP <faction id> GUARD [NOT]`]              |                                              | [K]     |
| [`HELP <faction id> SILVER [NOT]`]             |                                              | [K]     |
| [`HELP <faction id> PARTEITARNUNG [NOT]`]      |                                              | [K]     |
| [`COMBAT`]                                     | setzt Verhalten im Kampf                     | K       |
| [`COMBAT AGGRESSIVE`]                          |                                              | [K]     |
| [`COMBAT DEFENSIVE`]                           |                                              | [K]     |
| [`COMBAT FLEE`]                                |                                              | [K]     |
| [`COMBAT HELP [NOT]`]                          | der Einheit wird im Kampf nicht geholfen     | [K]     |
| [`COMBAT REAR`]                                |                                              | [K]     |
| [`COMBAT NOT`]                                 |                                              | [K]     |
| [`COMBATSPELL [STUFE n] "zauberspruch" [NOT]`] | setzt Zauber für Kämpfe                      | [K]     |
| [`BUY <number> luxusgut`]                      | kaufe Luxusgüter                             | [(l)] 3 |
| [`CONTACT <unit id>`]                          | kontaktiere fremde Einheiten                 | [K]     |
| [`TEACH <unit id> [<unit id> etc.]`]           | lehre Einheiten                              | [L]     |
| [`LEARN <skill>`]                              | Talent lernen                                | [L]     |
| [`LEARN AUTO <skill>`]                         | Talent lernen oder lehren                    | [L]     |
| [`LOCALE en/de`]                               | zeigt die Sprache der Befehle an             | [K]     |
| [`MAKE TEMP unit-alias-nr ["<name>"]`]         | erschaffe neue Einheit                       | [K]     |
| [`MAKE [stufe] gebäude-typ [<building id>]`]   | erweitere oder baue neues Gebäude            | [L]     |
| [`MAKE [stufe] schiffstyp`]                    | baue neue Schiffe                            | [L]     |
| [`MAKE [stufe] SHIP [<ship id>]`]              | baue weiter am Schiff                        | [L]     |
| [`MAKE`]                                       | baue weiter an Gebäude/Schiff                | [L]     |
| [`MAKE [stufe] STRASSE richtung`]              | baue Straßen                                 | [L]     |
| [`MAKE [<number>] herb`]                       | suche Kräuter der Region                     | [L]     |
| [`MAKE [<number>] trank`]                      | MAKE einen alchemistischen Trank             | [L]     |
| [`MAKE [<number>] <item>`]                     | MAKE einen Gegenstand oder baue Rohstoffe ab | [L]     |
| [`MOVE richtung [richtung etc.]`]              | reisen                                       | [L]     |
| [`NÄCHSTER] | beendet Befehle | [K] |
| [`NUMBER UNIT [neue\_nr]`] | vergibt neue Nummer | [K] |
| [`NUMBER BUILDING [neue\_nr]`] |     | [K] |
| [`NUMBER FACTION [neue\_nr]`] |     | [K] |
| [`NUMBER SHIP [neue\_nr]`] |     | [K] |
| [`OPTION AUSWERTUNG [NOT]`] | verschiedene Einstellungen | [K] |
| [`OPTION COMPUTER [NOT]`] |     | [K] |
| [`OPTION ZIPPED [NOT]`] |     | [K] |
| [`OPTION BZIP2 [NOT]`] |     | [K] |
| [`OPTION SILBERPOOL [NOT]`] |     | [K] |
| [`OPTION MATERIALPOOL [NOT]`] |     | [K] |
| [`OPTION ADRESSEN [NOT]`] |     | [K] |
| [`OPTION ZUGVORLAGE [NOT]`] |     | [K] |
| [`OPTION STATISTIK [NOT]`] |     | [K] |
| [`OPTION TALENTVERSCHIEBUNG [NOT]`] |     | [K] |
| [`OPTION PUNKTE [NOT]`] |     | [K] |
| [`PASSWORD "neues-passwort"`] | setzt neues Passwort | [K] |
| [`PLANT [<number>] herb`] | pflanzt Kräuter | [L] |
| [`PLANT [<number>] BÄUME`] | pflanzt Samen | [L] |
| [`PLANT [<number>] MALLORNSAMEN`] | pflanzt Samen | [L] |
| [`PLANT [<number>] SAMEN`] | pflanzt Samen | [L] |
| [`PIRATERIE [partei\_1] [partei\_2] [...]`] | Piraterie setzen | [L] |
| [`PRÄFIX [präfix]`] | gibt der Rassenbezeichnung ein Präfix | [K] |
| [`REGION x,y`] | keine Funktion (nur für Tools) | [K] |
| [`RECRUIT <number>`] | rekrutiert weitere Personen | [K] |
| [`RESERVE <number> "<item>"`] | Gegenstände reservieren | [K] |
| [`RESERVE <number> SILVER`] | Silber reservieren | [K] |
| [`ROUTE richtung [richtung etc.]`] | reisen | [L] |
| [`SORT VOR <unit id>`] | Einheit in Report sortieren | [K] |
| [`SORT HINTER <unit id>`] |     | [K] |
| [`SPIONIERE <unit id>`] | Einheit ausspionieren | [L] |
| [`SPRACHE en/de`] | ändert die Sprache der Partei | [K] |
| [`STIRB "passwort" [FACTION <faction id>]`] | aus dem Spiel ausscheiden | [K] |
| [`HIDE [stufe]`] | Tarnstufe setzen | [K] |
| [`HIDE rasse`] | Dämonen: als andere Rasse tarnen | [K] |
| [`HIDE FACTION [NOT]`] | Parteizugehörigkeit verbergen (als "anonym" getarnt) | [K] |
| [`HIDE FACTION NUMBER nummer`] | Parteizugehörigkeit tarnen (als andere Partei getarnt) | [K] |
| [`CARRY <unit id>`] | andere Einheiten mitnehmen | [K] |
| [`TAX [betrag]`] | Steuern eintreiben | [L] |
| [`ENTERTAIN [betrag]`] | verdient 20 oder mehr Silber | [L] |
| [`ORIGIN x y`] | setzt den Koordinaten-Ursprung | [K] |
| [`FORGET <skill>`] | vergisst das Talent | [K] |
| [`SELL anzah`l luxusgut] | verkauft Luxusgüter | [(l)] 3 |
| [`SELL ALLES luxusgut`] |     |     |
| [`LEAVE] | Schiff oder Gebäude verlassen | [K] |
| [`CAST [REGION x y] [STUFE n] "zauberspruch" [...]`] | Zaubern | [(l)] 4 |
| [`SHOW ALLE ZAUBER`] | zeigt Beschreibung aller bekannten Zauber | [K] |
| [`SHOW ALLE TRÄNKE`] | zeigt Beschreibung aller bekannten Tränke | [K] |
| [`SHOW "Gegenstand"`] | zeigt Beschreibung eines Gegenstands | [K] |
| [`SHOW "Trank"`] | zeigt Beschreibung des Tranks | [K] |
| [`SHOW "Zauberspruch"`] | zeigt Beschreibung des Zaubers | [K] |
| [`SHOW "Rasse"`] | zeigt Beschreibung der Rasse der Einheit | [K] |
| [`DESTROY [stufen]`] | Gebäude oder Schiff verkleinern | [L] |
| [`DESTROY [stufen]`] STRASSE richtung | Straße einreißen | [L] |
| [`GROW PFERDE`] | Pferde züchten - nur in Pferdezucht | L   |

<!-- [//]: ./cmd-comment.md "KOMMENTAR"-->
[K]: ./commands.md#kurzlang "Befehl"
[`WORK`]: ./cmd-work.md "WORK"
[L]: ./commands.md#kurzlang "Befehl"
[`ATTACK <unit id>`]: ./cmd-attack.md "ATTACK"
[(l)]: ./commands.md#kurzlang "Befehl"
[`BANNER "<text>"`]: ./cmd-banner.md "BANNER"
[`CLAIM <number> <item>`]: ./cmd-claim.md "CLAIM"
[`PROMOTE`]: ./cmd-promote.md "PROMOTE"
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
[`DEFAULT "befehl"`]: ./cmd-default.md "DEFAULT"
[`UNIT <unit id>`]: /UNIT "UNIT"
[`EMAIL email@adresse`]: ./cmd-email.md "EMAIL"
[`END`]: /END "END"
[`ERESSEA <faction id> "passwort"`]: /ERESSEA "ERESSEA"
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
[`COMBATSPELL [STUFE n] "zauberspruch" [NOT]`]: ./cmd-combatspell.md
[`BUY <number> luxusgut`]: ./cmd-buy.md "BUY"
[`CONTACT <unit id>`]: ./cmd-contact.md "CONTACT"
[`TEACH <unit id> [<unit id> etc.]`]: ./cmd-teach.md "TEACH"
[`LEARN <skill>`]: ./cmd-learn.md "LEARN"
[`LEARN AUTO <skill>`]: ./cmd-learn.md_AUTO "LEARN AUTO"
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
[`NÄCHSTER`]: ./cmd-next.md "NÄCHSTER"
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
[`PIRATERIE [partei\_1] [partei\_2] [...]`]: ./cmd-piracy.md "PIRATERIE"
[`PRÄFIX [präfix]`]: ./cmd-prefix.md "PRÄFIX"
[`REGION x,y`]: ./cmd-region.md "REGION"
[`RECRUIT <number>`]: ./silver.md#recruter "RECRUIT"
[`RESERVE <number> "<item>"`]: ./cmd-reserve.md "RESERVE"
[`RESERVE <number> SILVER`]: ./cmd-reserve.md "RESERVE"
[`ROUTE richtung [richtung etc.]`]: ./cmd-route.md "ROUTE"
[`SORT VOR <unit id>`]: ./cmd-sort.md "SORT"
[`SORT HINTER <unit id>`]: ./cmd-sort.md "SORT"
[`SPIONIERE <unit id>`]: ./cmd-spy.md "SPIONIERE"
[`SPRACHE en/de`]: ./cmd-language.md "SPRACHE"
[`STIRB <passwort> [FACTION <faction id>]`]: ./cmd-quit.md "STIRB"
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
[`CAST [REGION x y] [STUFE n] "zauberspruch" [...]`]: ./cmd-cast.md "CAST"
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

## Siehe auch

- [Befehle]
- [Befehlsreihenfolge]

|--------------|-----------------|
| Continue reading: | [Der erste Zug] |

[Der erste Zug]: ./round-first.md "Der erste Zug"

<!-- From [https://wiki.eressea.de/index.php?title=Kurzbeschreibung&oldid=16741] -->

[Befehl]: ./commands.md "Befehl"
[<sup>(l)</sup>]: ./commands.md#kurzlang "Befehl"
[Kampfende]: ./war.md#fin-de-la-bataille"Fin de la bataille"
[Befehle]: ./commands.md "Befehle"
[Befehlsreihenfolge]: ./commands-sequence.md "Befehlsreihenfolge"
