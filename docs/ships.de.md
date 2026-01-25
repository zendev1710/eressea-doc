---
# cSpell:locale de
alias: schiff
---
# Schiff

Schiffe werden dem Befehl [**`MACHE`**&#91;*`stufen`*&#93;*`Schiffstyp`*][1] gebaut.  
Existierende, unfertige oder beschädigte Schiffe werden mit **`MACHE`**&#91;*`stufen`*&#93;&nbsp;`SCHIFF`&nbsp;&#91;*`schiff-nr`*&#93; weitergebaut. Dafür braucht man Holz. Je komplexer das Schiff, um so schwerer ist es zu erbauen und zu kommandieren. Dies ist in der Tabelle weiter unten zusammengefasst. Um mit dem Bau eines Schiffes zu beginnen oder an einem Schiff weiterzubauen bzw. es zu reparieren, braucht die Einheit mindestens das angegebene Schiffbautalent. In der Tabelle ist aufgeführt, wie viel Holz benötigt wird, um ein Schiff zu bauen.
Eine Einheit kann pro Runde (Talentstufe \* Personen / Mindesttalent) Holz verbauen.

Auch Schiffe haben Nummern, die in Befehlen gebraucht werden.
Hier ein Beispiel für ein Schiff:

```text
Stolz der Sieben Winde (18), Langboot, (254/500). Dieses schöne

    Schiff war das erste, welches die Händlerfamilie Plötzbogen
    einsetzte.  Kapitän Gorm steht auf dem Achterdeck und erteilt
    Befehle an die Matrosen. Er hat alles voll im Griff.
```

Bei eigenen Schiffen steht hinter dem Schiffstyp die Beladung und die Kapazität (hier 254 Gewichtseinheiten von 500 möglichen).

Unter einem Schiff sind die Einheiten eingerückt, die sich auf dem Schiff befinden.
Die erste Einheit ist Kapitänin und hat das Kommando über das Schiff.
Sie bestimmt, welche anderen Einheiten das Schiff betreten dürfen.
Sie darf das Schiff [umbenennen] oder [beschreiben] und sie zählt auch als Besatzung.

Im Gegensatz zu Gebäuden können Schiffe nicht erweitert werden.
Wer also einmal begonnen hat, ein Langboot zu bauen, kann dies später nicht zu einer Karavelle umbauen.

Neu gebaute Schiffe liegen an keiner Küste und können deshalb in jede benachbarte Ozeanregion ablegen.

## Schiffstypen

### Boot

### Langboot

### Drachenschiff

### Karavelle

### Trireme

### Galeone

### Schiffe - Übersichtstabelle

Schiffe - Reichweite, Kapazität, Talente

| Typ           | Reichweite | Kapazität | Kapitän/Besatzung | Bautalent | Bauholz |
|---------------|:----------:|----------:|------------------:|----------:|--------:|
| Boot          |     2      |        50 |               1/2 |         1 |       5 |
| Langboot      |     3      |       500 |              1/10 |         1 |      50 |
| Drachenschiff |   5[^1]    |      1000 |              2/50 |         2 |     100 |
| Karavelle     |     5      |      3000 |              3/30 |         3 |     250 |
| Trireme       |     7      |      2000 |             4/120 |         4 |     200 |
| Galeone       |     5      |     20000 |         5/250[^2] |         5 |    2000 |

[^1]: Drachenschiffgeschwindigkeit abhängig vom Kapitänstalent.
[^2]: Für das Gesamttalent der Galeone werden nur Einheiten ab T2 in Segeln herangezogen.

Drachenschiffgeschwindigkeit

| Kapitän    | 2 | 6 | 18 | 54 | 162 |
|------------|---|---|----|----|:---:|
| Reichweite | 5 | 6 | 7  | 8  |  9  |

## Konvoi

Analog dazu, wie man mehrere Personen in einer Einheit haben kann, bestehen Konvois aus mehreren Schiffen des gleichen Typs, zum Beispiel

```text
Karavelle (2seh), 73 Karavellen, (12776/85410), 61% beschädigt.
```

Dafür [übergibt] man der Besitzereinheit eines Schiffes ein oder mehr Schiffe des gleichen Typs mit dem Befehl `GIB capt 1 SCHIFF`.
Die empfangende Einheit wird Kommandant eines Konvois.
Die übergebende und empfangende Einheit müssen derselben Partei angehören, HELFE ALLES oder KONTAKTIERE genügt nicht.
Die Besitzereinheit eines Konvois kommandiert alle ihre Schiffe gemeinsam und muss dafür das Mindesttalent für den Schiffstyp haben und eine Person pro Schiff.
Das Gesamttalent der Besatzung muss ebenfalls ein Vielfaches entsprechend der Anzahl Schiffe sein.
Die Reichweite entspricht der des Schiffstyps, maximaler Schaden und Traglast vergrößern sich entsprechend der Anzahl Schiffe.

Beispiel:

Ein Konvoi aus 3 Karavellen benötigt einen Kapitän mit mindestens 3 Personen mit Segeln T3 und Besatzung mit 90 Stufen Gesamttalent.
Sie haben wie zuvor eine Reichweite von 5 Feldern, aber eine Kapazität von 9000 GE.
Es ist also z.B. folgende Konstellation erlaubt und seetüchtig:

```text
Karavelle (2seh), 3 Karavellen, (9000/9000).
    * Kapitänsteam (k29), 3 Menschen, Talente: Segeln 3.
    * Besatzung (2ztf), 9 Menschen, Talente: Segeln 9.
    * Horde (770L), 888 Menschen.
```

Wie man sieht, kann man also in einem Konvoi große Einheiten bewegen, ohne sie auf einzelne Schiffe zu verteilen.
Konvois verhalten sich ansonsten wie ein normales Schiff.
Der ganze Konvoi treibt beispielsweise gemeinsam ab, nimmt als Ganzes Schaden und das Kommando kann übergeben werden.

Boote sind von dieser Regel ausgeschlossen und die Schiffe eines Konvois müssen vom gleichen Typ sein, es sind also beispielsweise keine Mischungen aus Triremen und Karavellen erlaubt.

Beschädigte oder unvollständige Schiffe können ebenfalls übergeben werden, der Zustand wirkt sich dann anteilig auf den Konvoi aus.
Wird ein Schiff mit 8% Schaden an einen Konvoi aus 3 Schiffen übergeben, besteht der Konvoi danach aus 4 Schiffen mit 2% Schaden.
Wird auch nur ein im Bau befindliches Schiff übergeben, befindet sich der ganze Konvoi danach im Bau und kann erst nach Fertigstellung segeln.
Ein 50% fertiges Schiff (im Bau) und ein fertiges gibt zwei 75% fertige Schiffe (im Bau).

Mit demselben Befehl kann man auch Schiffe aus einem Konvoi wieder heraus lösen.
Die Schiffe oder Konvois der Geber- und Empfängereinheit müssen an der gleichen Küste liegen oder sich auf dem Ozean befinden.
Die empfangende Einheit muss entweder Kapitänin eines Schiffes sein — dann wird das Schiff zu deren Konvoi hinzugefügt — oder auf dem gleichen Schiff wie die gebende Einheit sein oder nicht in einem Schiff oder in einem Gebäude sein.

Man kann auch Schiffe an die Bauern übergeben: GIB 0 2 SCHIFF erzeugt einen neuen Konvoi mit 2 Schiffen, auf dem keine Personen sind.
Ein Konvoikommandeur kann an Land auch nicht alle seine Schiffe an die Bauern übergeben, er muss immer mindestens eines behalten.

Wenn nach der Übergabe die übergebende Einheit selber keine Schiffe mehr hat, steigen automatisch alle Einheiten, die vorher mit ihr gefahren sind, auf die Schiffe der Zieleinheit um.

Konvois können nicht verzaubert werden, verzauberte Schiffe können nicht übergeben werden und an Besitzer bezauberter Schiffe können keine weiteren Schiffe übergeben werden.

Spielererfahrung (Solthar):

Eine leere Einheit kann nichts übergeben.
Deshalb ist bei folgenden Befehlen die Reihenfolge wichtig:

```text
GIB 123 1 SCHIFF
GIB 123 ALLES PERSONEN
```

## Siehe auch

- [Schiffsreise]
- [[bef-gib]][übergibt]

Weiterlesen: [Gebäude].

<!-- From [https://wiki.eressea.de/index.php?title=Schiff&oldid=16111] -->

[Gebäude]: ./buildings.md
[1]: ./cmd-make.md
[umbenennen]: ./cmd-name.md
[beschreiben]: ./cmd-describe.md
[übergibt]: ./cmd-give.md
[Schiffsreise]: ./travel.md
