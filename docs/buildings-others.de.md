---
# cSpell:locale de
alias: andere-gebaeude
---
# Andere Gebäude

Gebäude werden mit dem Befehl [MACHE gebäudetyp] gebaut und mit [MACHE gebäudetyp gebäude-nr][MACHE gebäudetyp] wird an einem Gebäude weitergebaut. Beispiele: [[bef-mache|MACHE leuchtturm]] oder [[bef-mache|MACHE hafen]] xyz.
Für diese Gebäude ist ein Mindesttalentwert in Burgenbau erforderlich, der in der Tabelle angegeben ist. Außerdem können einige Gebäude nur bis zu einer bestimmten Größe ausgebaut werden.

Hier zunächst eine zusammenfassende Tabelle, nähere Erklärungen folgen darunter.

Gebäude; siehe auch Tabelle [Burgenbau]

Die Kapazität bezieht sich nur auf die Personen, die von dem Gebäude profitieren können.

\* außerdem 2 Mallorn und 2 Laen pro Größenpunkt

| Gebäude        | Baukosten |      |       |        | Talent | Unterhalt |            | Max.  | Kapazität   |
|----------------|-----------|------|-------|--------|--------|-----------|------------|-------|-------------|
|                | Stein     | Holz | Eisen | Silber |        | Silber    | Ressourcen |       |             |
| [Leuchtturm]   | 2         | 1    | 1     | 100    | 3      | 100       | \-/-       | keins | 4 Einheiten |
| [Bergwerk]     | 5         | 10   | 1     | 250    | 4      | 500       | \-/-       | keins | Größe       |
| [Steinbruch]   | 1         | 5    | 1     | 250    | 2      | 250       | \-/-       | keins | Größe       |
| [Sägewerk]     | 5         | 5    | 3     | 200    | 3      | 250       | \-/-       | keins | Größe       |
| [Schmiede]     | 5         | 5    | 2     | 200    | 3      | 300       | 1 Holz     | keins | Größe       |
| [Pferdezucht]  | 2         | 4    | 1     | 100    | 2      | 150       | \-/-       | keins | Größe       |
| [Hafen]        | 5         | 5    | \-/-  | 250    | 3      | 250       | \-/-       | 25    | Größe       |
| [Karawanserei] | 1         | 5    | 1     | 500    | 2      | 3000      | 2 Pferde   | 10    | Größe       |
| [Akademie]     | 5         | 5    | 1     | 500    | 3      | 1000      | \-/-       | 25    | Größe       |
| [Magierturm]\* | 5         | 3    | 3     | 500    | 5      | 1000      | \-/-       | 50    | 2 Personen  |
| [Damm]         | 5         | 10   | 1     | 500    | 4      | 1000      | 3 Holz     | 50    | Größe       |
| [Tunnel]       | 10        | 5    | 1     | 300    | 6      | 100       | 2 Stein    | 100   | Größe       |
| [Taverne]      | 4         | 3    | 1     | 200    | 2      | 5\*Größe  | \-/-       | keins | Größe       |
| [Monument]     | 1         | 1    | 1     | 400    | 4      | \-/-      | \-/-       | keins | Größe       |
| [Steinkreis]   | 5         | 5    | \-/-  | \-/-   | 2      | \-/-      | \-/-       | 100   | 3 Personen  |

## Leuchtturm

|                            |                                       |
|----------------------------|---------------------------------------|
| Baukosten pro Größenpunkt: | 2 Steine, 1 Holz, 1 Eisen, 100 Silber |
| Mindestbautalent:          | 3                                     |
| Unterhalt pro Runde:       | 100 Silber                            |
| Größenbegrenzung:          | Keine                                 |
| Kapazität:                 | 4 Einheiten                           |

| Größe | Wahrnehmung | Sichtweite |
|-------|-------------|------------|
| 10    | 3           | 1          |
| 10    | 6           | 2          |
| 100   | 9           | 3          |
| 1000  | 12          | 4          |
| etc   |             |            |

- Ab einer Größe von 10 verhindert ein Leuchtturm im Umkreis von log10 (Leuchtturmgröße) + 1 Feldern das Abtreiben von Schiffen durch Stürme.
- Ab einer Größe von 10 gibt ein Leuchtturm den Insassen (nur bis zu 4 Einheiten) Infos über Schiffsichtungen in allen Ozeanfeldern im Umkreis von 1 + log10 (Leuchtturmgröße) Feldern. Die Einheit muss dafür mindestens eine Wahrnehmung von Entfernung \* 3 haben. Einen Report einer drei Felder entfernten Ozeanregion bekommt man also nur, wenn der Leuchtturm mindestens Größe 100 und die Einheit mindestens Wahrnehmung 9 hat.

## Bergwerk

|                            |                                        |
|----------------------------|----------------------------------------|
| Baukosten pro Größenpunkt: | 5 Steine, 10 Holz, 1 Eisen, 250 Silber |
| Mindestbautalent:          | 4                                      |
| Unterhalt pro Runde:       | 500 Silber                             |
| Größenbegrenzung:          | keine                                  |
| Kapazität:                 | Personen entsprechend Größe            |

- Von Einheiten innerhalb des Bergwerks abgebautes Eisen wird nur zur Hälfte vom Regionsvorrat abgezogen. Dieser Effekt wirkt kumulativ zusammen mit eventuell vorhandenen entsprechenden Rassenvorteilen.
- Die Fördermenge von Erzen erhöht sich, als hätten die Insassen einen Bergbaubonus von +1. Dies gilt jedoch nicht für die Abbautiefe der Erz-Schicht.
- Nur mit einem Bergwerk ist der Laen-Abbau möglich.

**Beispiele:**

- Ein Mensch mit Bergbau 2 kann in einem Bergwerk 3 Eisen in Tiefe 1 oder 2 abbauen. Wegen Rundung werden davon jedoch 2 Eisen vom Regionsvorrat abgezogen. Zwei Menschen können 6 Eisen abbauen, von denen 3 abgezogen werden.
- 10 Zwerge bauen in einer Region 60 Eisen ab. Es werden durch den Zwergenbonus nur 36 Eisen vom Regionsvorrat abgezogen. Befinden sich diese Zwerge auch noch in einem Bergwerk, so werden nur 18 Eisen abgezogen. Sind nur noch 9 Eisen überhaupt in der Region vorhanden, können die Zwerge natürlich nur 15 bzw. 30 Eisen abbauen.

## Steinbruch

|                            |                                      |
|----------------------------|--------------------------------------|
| Baukosten pro Größenpunkt: | 1 Stein, 5 Holz, 1 Eisen, 250 Silber |
| Mindestbautalent:          | 2                                    |
| Unterhalt pro Runde:       | 250 Silber                           |
| Größenbegrenzung:          | keine                                |
| Kapazität:                 | Personen entsprechend Größe          |

- Von Einheiten innerhalb des Steinbruchs abgebaute Steine werden nur zur Hälfte vom Regionslimit abgezogen. Dieser Effekt wirkt kumulativ zusammen mit eventuell vorhandenen entsprechenden Rassenvorteilen.
- Die Fördermenge von Steinen erhöht sich, als hätten die Insassen einen Steinbaubonus von +1. Dies gilt jedoch nicht für die Abbautiefe.

**Beispiel:** 10 Trolle bauen in einer Region 40 Steine ab. Es werden durch den Trollbonus nur 30 Steine vom Regionsvorrat abgezogen. Befinden sich diese Trolle auch noch in einem Steinbruch, so werden nur 15 Steine abgezogen. Sind nur noch 7 Steine überhaupt in der Region vorhanden, können die Trolle natürlich nur 9 bzw. 18 Steine abbauen.

## Sägewerk

|                            |                                       |
|----------------------------|---------------------------------------|
| Baukosten pro Größenpunkt: | 5 Steine, 5 Holz, 3 Eisen, 200 Silber |
| Mindestbautalent:          | 3                                     |
| Unterhalt pro Runde:       | 250 Silber                            |
| Größenbegrenzung:          | keine                                 |
| Kapazität:                 | Personen entsprechend Größe           |

- Von Einheiten innerhalb des Sägewerks abgeholzte Bäume und Mallornbäume und Schösslinge werden nur zur Hälfte vom Regionsvorrat abgezogen.
- Einheiten innerhalb eines Sägewerks fällen mit einem Talentbonus von +1.

**Beispiel:** Mit [Wasser des Lebens] kann mit Hilfe eines Sägewerks Holz erzeugt werden: Mit [BENUTZE 1 Wasser des Lebens] werden unter Einsatz von 10 Holz 10 Schösslinge gepflanzt. Diese können dann abgeholzt werden, womit sich die Holzmenge auf 20 vergrößert hat.

## Schmiede

|                            |                                       |
|----------------------------|---------------------------------------|
| Baukosten pro Größenpunkt: | 5 Steine, 5 Holz, 2 Eisen, 200 Silber |
| Mindestbautalent:          | 3                                     |
| Unterhalt pro Runde:       | 300 Silber, 1 Holz                    |
| Größenbegrenzung:          | keine                                 |
| Kapazität:                 | Personen entsprechend Größe           |

- Bei Eisenwaffen und -rüstungen wird nur halb so viel Eisen benötigt. Laen wird in einer Schmiede nicht eingespart.
- In Schmieden produzierende Einheiten haben einen Bonus von +1 auf Waffenbau und Rüstungsbau.

## Pferdezucht

|                            |                                       |
|----------------------------|---------------------------------------|
| Baukosten pro Größenpunkt: | 2 Steine, 4 Holz, 1 Eisen, 100 Silber |
| Mindestbautalent:          | 2                                     |
| Unterhalt pro Runde:       | 150 Silber                            |
| Größenbegrenzung:          | keine                                 |
| Kapazität:                 | Personen entsprechend Größe           |

- In einer Pferdezucht können mit dem Befehl [ZÜCHTE] Pferde gezüchtet werden. Hierzu braucht der Pferdezüchter das Talent Pferdezucht und mindestens zwei Pferde.
- Die Chance ein Pferd zu züchten entspricht dem Talent des Pferdezüchters. Zusätzlich hat er entsprechend seinem Talent mehrere Versuche. Hat ein Pferdezüchter T5, so hat er 5 Versuche zu je 5% ein Pferd zu züchten.
- Für jeden Zuchtversuch benötigt der Züchter ein Pferd. Sind nicht genug Pferde vorhanden, verfallen die Versuche.

## Hafen

|                            |                                           |
|----------------------------|-------------------------------------------|
| Baukosten pro Größenpunkt: | 5 Steine, 5 Holz, 250 Silber              |
| Baukosten gesamt:          | 125 Steine, 125 Holz, 6250 Silber         |
| Mindestbautalent:          | 3                                         |
| Unterhalt pro Runde:       | 250 Silber                                |
| Größenbegrenzung:          | 25                                        |
| Kapazität:                 | Personen entsprechend Größe, Schiffe egal |

- Schiffe größer als ein Boot können auch in Nichtebenen anlegen, wenn ein Hafen vorhanden ist.
- Eine Region mit Hafen kann als "Kanalregion" genutzt werden, d.h. ein Schiff in dem Hafen kann in jede beliebige andere Richtung mit Ozean davon segeln.
- Voraussetzung ist in beiden Fällen, dass der Hafeneigner dem Kapitän [HELFE BEWACHE] gesetzt hat oder der selben Partei angehört.
- Der Eigentümer erhält 10% aller Handelseinnahmen, zusätzlich zu eventuellen Einnahmen durch Burgen.
- Der Eigentümer erhält (2 \* Handeln)% aller Luxusgüter, die sich auf einlaufenden Schiffen befinden, es sei denn, die die Gegenstände tragende Einheit ist besser getarnt als die Wahrnehmung des Hafenmeisters (Schmuggel) oder der Schiffskapitän ist mit dem Hafenmeister alliiert.
- In Regionen mit Hafen steigen die Preise für Luxusgüter mit einer Wahrscheinlichkeit von 20% (normalerweise 10%).
- Ein Hafen funktioniert nur, wenn er voll ausgebaut ist. Es kann nur einen Hafen pro Region geben. Wer zuerst fertig ist, hat gewonnen ... Der halbfertige Hafen kann mit dem Befehl [ZERSTÖRE] zerstört werden.

## Akademie

|                            |                                              |
|----------------------------|----------------------------------------------|
| Baukosten pro Größenpunkt: | 5 Steine, 5 Holz, 1 Eisen, 500 Silber        |
| Baukosten gesamt:          | 125 Steine, 125 Holz, 25 Eisen, 12500 Silber |
| Mindestbautalent:          | 3                                            |
| Unterhalt pro Runde:       | 1000 Silber                                  |
| Größenbegrenzung:          | 25                                           |
| Kapazität:                 | Personen entsprechend Größe                  |

- Einheiten, die in einer Akademie lernen, können mit einer Chance von 1/3 in dieser Woche einmal zusätzlich lernen; wenn sie einen Lehrer haben sogar mit einer Chance von 2/3.
- Lernen in einer Akademie kostet bei nicht kostenpflichtigen Talenten 50 Silber pro Person, bei kostenpflichtigen Talenten das Doppelte der normalen Lernkosten.
- Eine Akademie funktioniert nur, wenn sie voll ausgebaut ist!
- Lehrer, die Schüler in einer Akademie lehren, bekommen ebenfalls eine Chance, zu lernen, die je nach Anzahl ihrer Schüler bis zu 1/3 beträgt. Sie müssen dafür nicht selbst in einer Akademie stehen.

## Magierturm

|                            |                                                                      |
|----------------------------|----------------------------------------------------------------------|
| Baukosten pro Größenpunkt: | 5 Steine, 3 Holz, 2 Mallorn, 3 Eisen, 2 Laen, 500 Silber             |
| Baukosten gesamt:          | 250 Steine, 150 Holz, 100 Mallorn, 150 Eisen, 100 Laen, 25000 Silber |
| Mindestbautalent:          | 5                                                                    |
| Unterhalt pro Runde:       | 1000 Silber                                                          |
| Größenbegrenzung:          | 50                                                                   |
| Kapazität:                 | 2 Personen                                                           |

- In einem Magierturm regeneriert ein Magier 75% mehr Aura.
- Die Stärke jedes Zaubers, der von einem Magierturm aus gesprochen wird, erhöht sich, als wäre der Zauber mit einer Stufe mehr gezaubert worden.
- Patzer passieren deutlich seltener.
- Das Gebäude selbst hat 40% erhöhte Magieresistenz.
- Ein Magierturm funktioniert nur, wenn er voll ausgebaut ist!

## Karawanserei

|                            |                                           |
|----------------------------|-------------------------------------------|
| Baukosten pro Größenpunkt: | 1 Stein, 5 Holz, 1 Eisen, 500 Silber      |
| Baukosten gesamt:          | 10 Steine, 50 Holz, 10 Eisen, 5000 Silber |
| Mindestbautalent:          | 2                                         |
| Unterhalt pro Runde:       | 3000 Silber, 2 Pferde                     |
| Größenbegrenzung:          | 10                                        |
| Kapazität:                 | Personen entsprechend Größe               |

- Ermöglicht Straßenbau in Wüsten. Wird die Karawanserei komplett zerstört, wird die Hälfte der Straße vernichtet. Eine fertige Straße bleibt bestehen, wenn der Gebäudeunterhalt nicht bezahlt wird.
- Verdoppelt in Wüsten das dort mögliche Handelsvolumen. Der Besitzer erhält einen Erlösanteil vom Handel entsprechend den Burgen (siehe [Tabelle zu Burgen]).
- Die Karawanserei funktioniert nur, wenn sie voll ausgebaut ist!

## Damm

|                            |                                              |
|----------------------------|----------------------------------------------|
| Baukosten pro Größenpunkt: | 5 Steine, 10 Holz, 1 Eisen, 500 Silber       |
| Baukosten gesamt:          | 250 Steine, 500 Holz, 50 Eisen, 25000 Silber |
| Mindestbautalent:          | 4                                            |
| Unterhalt pro Runde:       | 1000 Silber, 3 Holz                          |
| Größenbegrenzung:          | 50                                           |
| Kapazität:                 | Personen entsprechend Größe                  |

- Ein Damm ermöglicht den Straßenbau in Sümpfen. Wird der Damm zerstört, so wird die Hälfte der Straße vernichtet. Eine fertige Straße bleibt bestehen, wenn der Gebäudeunterhalt nicht bezahlt wird.
- Der Damm funktioniert nur, wenn er voll ausgebaut ist!

## Tunnel

|                            |                                                |
|----------------------------|------------------------------------------------|
| Baukosten pro Größenpunkt: | 10 Steine, 5 Holz, 1 Eisen, 300 Silber         |
| Baukosten gesamt:          | 1000 Steine, 500 Holz, 100 Eisen, 30000 Silber |
| Mindestbautalent:          | 6                                              |
| Unterhalt pro Runde:       | 100 Silber, 2 Steine                           |
| Größenbegrenzung:          | 100                                            |
| Kapazität:                 | Personen entsprechend Größe                    |

- Ein Tunnel ermöglicht den Straßenbau in Gletschern. Wird der Tunnel zerstört, so wird die Hälfte der Straße vernichtet. Eine fertige Straße bleibt bestehen, wenn der Gebäudeunterhalt nicht bezahlt wird.
- Der Tunnel funktioniert nur, wenn er voll ausgebaut ist!

## Taverne

|                            |                                      |
|----------------------------|--------------------------------------|
| Baukosten pro Größenpunkt: | 4 Stein, 3 Holz, 1 Eisen, 200 Silber |
| Mindestbautalent:          | 2                                    |
| Unterhalt pro Runde:       | 5 Silber pro Größenpunkt             |
| Größenbegrenzung:          | keine                                |
| Kapazität:                 | Personen entsprechend Größe          |

- Einheiten in einer Taverne regenerieren 50% schneller.
- Einheiten in einer Taverne verbrauchen 14 Silber als Unterhalt!

## Monument

|                            |                                      |
|----------------------------|--------------------------------------|
| Baukosten pro Größenpunkt: | 1 Stein, 1 Holz, 1 Eisen, 400 Silber |
| Mindestbautalent:          | 4                                    |
| Unterhalt pro Runde:       | Kein Unterhalt                       |
| Größenbegrenzung:          | keine                                |
| Kapazität:                 | Personen entsprechend Größe          |

- Sind Name und Beschreibung eines Monumentes gesetzt, können sie nicht mehr geändert werden, auch vom Eigentümer nicht.
- Das Monument hat keine Funktion.

## Steinkreis

|                            |                      |
|----------------------------|----------------------|
| Baukosten pro Größenpunkt: | 5 Stein, 5 Holz      |
| Baukosten gesamt:          | 500 Steine, 500 Holz |
| Mindestbautalent:          | 2                    |
| Unterhalt pro Runde:       | Kein Unterhalt       |
| Größenbegrenzung:          | 100                  |
| Kapazität:                 | 3 Personen           |

- Ein Steinkreis kann durch einen mächtigen Zauber [gesegnet werden]. Dieser entfaltet dann einige sonderbare Wirkungen. Unter anderem scheint er die überaus seltenen Elfenpferde anzulocken. Außerdem können Magier in dem Gebäude die Verbindung zwischen Astralraum und Realwelt unterbrechen.
- Ein Steinkreis funktioniert nur, wenn er voll ausgebaut und gesegnet ist!
- In einem gesegneten Steinkreis regeneriert ein Magier 50% mehr Aura.
- Die Stärke jedes Zaubers, der von einem gesegneten Steinkreis aus gesprochen wird, erhöht sich, als wäre der Zauber mit einer Stufe mehr gezaubert worden.
- Insassen haben 30% zusätzliche Magieresistenz.

## Siehe auch

- [Gebäude]
- [Burgen]
- [Produktion]

Weiterlesen: [Parteipool].

[Burgenbau]: ./castles.md "Burgen"
[Leuchtturm]: #leuchtturm
[Bergwerk]: #bergwerk
[Steinbruch]: #steinbruch
[Sägewerk]: #sägewerk
[Schmiede]: #schmiede
[Pferdezucht]: #pferdezucht
[Hafen]: #hafen
[Karawanserei]: #karawanserei
[Akademie]: #akademie
[Magierturm]: #magierturm
[Damm]: #damm
[Tunnel]: #tunnel
[Taverne]: #taverne
[Monument]: #monument
[Steinkreis]: #steinkreis
[Wasser des Lebens]: ./alchemy.md "Tränke"
[BENUTZE 1 Wasser des Lebens]: ./cmd-use.md "BENUTZE"
[ZÜCHTE]: ./cmd-grow.md "ZÜCHTE"
[HELFE BEWACHE]: ./cmd-help.md "HELFE"
[ZERSTÖRE]: ./cmd-destroy.md "ZERSTÖRE"
[Tabelle zu Burgen]: ./castles.md#uebersicht "Burgen"
[gesegnet werden]: ./spells-descriptions.md#segne-steinkreis "Zauberbeschreibungen E2"
[Gebäude]: ./buildings.md "Gebäude"
[Burgen]: ./castles.md "Burgen"
[Produktion]: ./production.md "Produktion"
[Parteipool]: ./faction-pool.md "Parteipool"
[MACHE gebäudetyp]: ./cmd-make.md "MACHE"
