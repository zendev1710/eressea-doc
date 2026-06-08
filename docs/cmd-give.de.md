---
# cSpell:locale de
alias: bef-gib
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# GIB

` `**`GIB`**` `*`einheit-nr anzahl gegenstand`*  
**`GIB`**` `*`einheit-nr`*` JE `*`anzahl`*` `*`gegenstand`*  
**`GIB`**` `*`einheit-nr`*`ALLES`  
**`GIB`**` `*`einheit-nr`*` ALLES `*`gegenstand`*  
**`GIB`**` `*`einheit-nr`*`KRÄUTER`  
**`GIB`**` `*`einheit-nr anzahl`*`PERSONEN`  
**`GIB`**` `*`einheit-nr`*`ALLES PERSONEN`  
**`GIB`**` `*`einheit-nr`*`EINHEIT`  
**`GIB`**` `*`einheit-nr`*`KOMMANDO`  
**`GIB`**` `*`einheit-nr anzahl SCHIFF`*  
**`GIB`**` 0 `*`anzahl gegenstand`*  
**`GIB`**` 0 `*`anzahl`*`PERSONEN`  
**`GIB`**` 0 `*`anzahl`*`SCHIFF`  

Die Einheit übergibt Gegenstände, das Kommando über Schiffe oder Gebäude, Personen, Schiffe oder gar sich selbst an andere Einheiten.

## Gegenstände

Mit `GIB` können Einheiten alle Waren, die sie haben, an andere Einheiten geben.
Bedingung ist, dass die angegebene Einheit Sachen annimmt.
Dies tut sie nur, wenn sie zur eigenen oder einer alliierten Partei gehört (`HELFE GIB`), oder wenn sie diese Runde den Befehl [[bef-kontaktiere]] für die Gebereinheit gegeben hat.
Einheiten der Monsterpartei und manche Spielereinheiten mit Monsterrassen nehmen ebenfalls nichts an.
Wer Gegenstände einfach nur los werden will, kann diese auch an die Bauern übergeben oder im Ozean versenken (`GIB 0`*`anzahl gegenstand`*).
Personen, Silber und Pferde vergrößern den Bauern-, Silber- bzw. Pferdevorrat einer Landregion.
Alle anderen Gegenstände verschwinden einfach.

Geber- wie Empfängereinheit müssen sich natürlich in der selben Region aufhalten.
Die Übergabe klappt auch auf hoher See, zwischen Schiffen und von Schiffen an Land und umgekehrt.

Statt einer Anzahl kann man auch den Parameter `ALLES` (oder `ALLE`) benutzen.
`GIB`*`einheit-nr`*`ALLE Schwerter` übergibt zum Beispiel alle Schwerter, die die Einheit zu dem Zeitpunkt hat.
`GIB`*`einheit-nr`*`ALLES` übergibt sämtliche Gegenstände, Kräuter, Tränke und Silber, nicht aber die Personen der Einheit.
Mit `GIB`*`einheit-nr`*`KRÄUTER` werden sämtliche Kräuter übergeben, welche die Einheit besitzt.
Gibt man explizit den Befehl `GIB`*`einheit-nr`*`ALLE PERSONEN`, so werden alle Personen übergeben und die Einheit aufgelöst.

!!! warning "Achtung"
    Alle Gegenstände und Silber, die mit `GIB` übergeben wurden, sind automatisch reserviert und können auch vom Materialpool nicht mehr weiter gegeben werden! Auch `GIB` benutzt den [Materialpool], ausgenommen im Kontext von GIB ALLES, wo die Einheit nur eigene, nicht reservierte Gegenstände gibt.

Die Variante `GIB xyz JE` übergibt *anzahl* Gegenstände pro Person der Zieleinheit.
Hat die Einheit xyz also zum Beispiel 10 Personen, so übergibt `GIB xyz JE 20 Silber` ihr 200 Silber.

**Tip:** Mit `@GIB` kann man automatische Übergaben einrichten.
Zum Beispiel wird eine Einheit mit `@GIB abc ALLES Eisen` der Einheit abc jede Woche alles Eisen übergeben.

```text
GIB k3f 300 Silber
; Gibt der Einheit k3f 300 Silber.

GIB 0 5 Steine
; Wirft 5 Steine weg.

GIB TEMP 3 7 PERSONEN
; Gibt 7 Personen an die neu geschaffene Einheit TEMP 3.
```

!!! warning "Vorsicht"
    Zwischen `MACHE TEMP` und `ENDE` stehen Befehle für die neue Einheit - und diese hat kein Geld.  
    Folgendes funktioniert also nicht:

```text
MACHE TEMP 1
    GIB TEMP 1 200 Silber  ;  sinnlos!
    REKRUTIERE 2
    NACH WESTEN
ENDE
```

Stattdessen muss es so geschrieben werden:

```text
GIB TEMP 1 200 Silber
MACHE TEMP 1
    REKRUTIERE 2
    NACH WESTEN
ENDE
; GIB TEMP 1 200 Silber  ;  oder hier!
```

## Personen und Einheiten

Will man Personen verschiedener Einheiten zusammenführen, so geschieht dies mit `GIB`*`einheit-nr`*`anzahl PERSONEN`.
Dabei werden dann auch die [Talente] vermischt, und man sollte die Gegenstände nicht vergessen, da sie evtl.
den Bauern zufallen, wenn die Einheit keine Personen mehr hat.

Spielererfahrung: Solthar Willst du einer Einheit einer anderen Partei Personen übergeben, reicht ein einfaches HELFE GIB nicht aus, sondern die Empfängereinheit muss die übergebende Einheit KONTAKTIEREN.
Falls die Empfängereinheit eine [Migranteneinheit][menschen] ist, darf sie außerdem zum Zeitpunkt der Übergabe keine Personen haben.
Am besten sollte sie also eine leere TEMP-Einheit sein.

Beispiel:

```text
EINHEIT a; Partei X
GIB TEMP x ALLES PERSONEN
Einheit b; Partei Y
MACHE TEMP x
KONTAKTIERE EINHEIT a
ENDE
```

Mit `GIB`*`einheit-nr`*`EINHEIT` wird die komplette Einheit mit allen Gegenständen einer anderen Partei gegeben, d.h. sie wechselt zur Partei der Empfänger-Einheit, und wird nicht zur Empfängereinheit zugefügt! Die Einheit führt in der Runde keine weiteren Befehle aus!

## Kommando

Hat die Einheit zudem ein Schiff oder ein Gebäude unter ihrem Kommando - ist sie also die erste aufgeführte Einheit im Schiff oder in dem Gebäude - kann sie das Kommando auch an eine andere Einheit übergeben.
Die Einheit mit dem Kommando bestimmt, welche anderen Einheiten das Schiff oder das Gebäude betreten dürfen.

`GIB einheit KOMMANDO` sollte man immer anwenden, auch wenn die Einheit mit dem Kommando das Schiff oder Gebäude verlässt und die folgende Einheit das Kommando erhalten soll.
Die Reihenfolge der Einheiten ist während der Auswertung nicht immer die dem Report entsprechende.
Neue Besitzer eines Gebäudes werden am Ende der Runde an die erste Position im Gebäude gestellt und profitieren somit eventuell erst in der Folgerunde von dem Gebäude (z.B. Bergbaubonus).
Das Kommando kann nicht an Einheiten ohne Personen (z.B. nach einem Kampf oder "leere" TEMP-Einheiten) übergeben werden.

## Konvoi

Mit `GIB`*`einheit-nr`*` `*`anzahl`*`SCHIFF` übergibt der Besitzer eines Schiffes oder Konvois die Anzahl Schiffe.
Die übergebende und empfangende Einheit müssen der selben Partei angehören, HELFE ALLES oder KONTAKTIERE genügt nicht.
Ist die anderen Einheit ebenfalls Besitzer eines Schiffes wird ein [Konvoi][konvoi-id] gebildet.
Konvois bestehen immer aus Schiffen des gleichen Typs.
Boote können keine Konvois bilden und die Schiffe müssen an der gleichen Küste liegen.

## Siehe auch

- [[bef-reserviere]]
- [Materialpool]
- [Schiff][schiff]
- [Gebäude]

<!-- From [https://wiki.eressea.de/index.php?title=GIB&oldid=16897] -->

[bef-kontaktiere]: ./cmd-contact.md
[Materialpool]: ./items-pool.md
[Talente]: ./skills.md
[bef-reserviere]: ./cmd-reserve.md
[Gebäude]: ./buildings.md
