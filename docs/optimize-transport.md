---
alias:
    name: optimizing-transport
    text: Optimizing transport
---
# Optimizing transport

## Handelsreisender

Da wir bei Eressea nicht mit wenigen sondern mit sehr vielen Einheiten hantieren, stellt sich die Problematik des Handelsreisenden weniger, da Transporte oft nicht mehrere Regionen im Kreis anfahren, sondern Bedarfe eher mit vielen einzelnen Transporten parallel bearbeitet werden.

## Optimale Beladung

Für die Beladung eines Transportes mit Waren liegt es nahe das Rucksackproblem anzuwenden. Allerdings läuft man in Eressea dabei schnell in die Falle zu viele gleichartige Gegenstände verladen zu wollen. Optimierungen des Rucksackproblems kommen damit kaum klar.

Ein einfaches Beispiel:

Zu transportieren sind 10 Steine (je 60 kg) und 100 Juwelen (je 1 kg). Es steht jedoch nur 500GE Kapazität zur Verfügung. Ein Stein wird mit einem Wert von 1200 bemessen, ein Juwel mit einem Wert von 50. Da die Juwelen mehr Wert pro kg bieten (50 je kg) laden wir also zuerst alle Juwelen auf:

    Wert   = 100 * 50 = 5000 
    Ladung = 100 * 1 kg = 100 kg
    frei   = 400 kg

Bei 400 kg gelingt es uns also noch 6 Steine aufzuladen, 40 kg bleiben frei.

    Wert   = 5000 + 6 * 1200 = 12200
    Ladung = 100 kg + 6 * 60 kg = 460 kg
    frei   = 40 kg

Versuchen wir es also mit den Steinen zuerst: 8 Steine, dann bleibt noch Platz für 20 Juwelen:

    Wert   = 20 * 50 + 8 * 1200 = 10600

Das war offenbar nichts. Aber geht es doch noch irgendwie besser? Ja, 7 Steine und 80 Juwelen scheinen offenbar die Kapazität besser auszunutzen:

    Wert   = 80 * 50 + 7 * 1200 = 12400

Der Weg dahin führt z.b. über greedy suche, also das durchsuchen sämtlicher Zustände. In dem Fall also 0 bis 8 Steine und 0 bis 100 Juwelen (manchmal weniger) macht also rund 900 Zustände die zu prüfen wären. Wenn man sich jetzt noch eine 3. oder 4. Ware vorstellt wird schnell klar, so kommen wir nicht zum Ergebnis.

Normalerweise führt hier der schnelle Weg zum Ziel über sogenannte Pareto-optimale Zwischenzustände. Was solche Zwischenzustände sind lässt sich leichter anders rum erklären. Zustände die bei gleicher Beladung weniger Wert sind als ein anderer Zwischenzustand sind nicht Pareto-optimal. Diese braucht man nicht weiter zu verfolgen, da offenbar immer wieder nur nicht Pareto-optimale Zustände erreicht werden können.

Vergleicht man also beispielsweise den Zustand "60 Juwelen" mit "1 Stein" so zeigt sich, das 60 Juwelen offenbar bei gleicher Beladung weit mehr Wert sind. Es lohnt also nicht "1 Stein" weiter zu expandieren. Genau genommen kommt man zu dieser Feststellung bereits wenn man 24 Juwelen expandiert hat.

Problematisch ist diese Art der Optimumsberechnung nun, da offenbar jede Anzahl von Juwelen zwischen 0 und 100 pareto-optimal ist. Schlimmer noch auch jede Kombination aus 1-6 Steinen mit 77 bis 100 Juwelen und 7 Steinen mit 77 bis 80 Juwelen ist pareto-optimal. D.h. trotz Optimierung müssen wir 100 + 6 \* 24 + 4 = 248 Zustände von ca. 900 Zuständen expandieren, bis wir uns der gefundenen Lösung sicher sein können - kein schönes Ergebnis.

Allerdings bietet sich eine andere Optimierung an. Wir können die verwendeten Transportmengen einschränken. Da sich Juwelen so lange lohnen wie sie zusammen eine ganz Anzahl Steine ergeben, liegt die Juwelenzahl zwischen 60 und 100. Die Juwelen können jedoch nie die komplette Kapazität belegen, weshalb mindestens 6 Steine und maximal 8 mitgenommen werden können. Damit reduziert sich die Suche auf 41\*3 oder mit Pareto-optimalen Zwischenzuständen auf 41 + 24 + 4 = 69 Zustände.

*Achtung: Priorisiert man die Waren, statt sie zu bewerten, dann lässt sich diese Art der Packung eher nicht anwenden. Dann gilt: Höchste Priorität zuerst ...*

### Pakete

Oftmals lohnt der Transport von Rohstoffen erst, wenn alle benötigten Rohstoffe das Ziel erreichen. Die Idee ist nun diese Rohstoffe zu paketieren. Das kann heissen diese entweder alle oder gar nicht zu verschicken, oder aber bei Erreichen der Paketgrösse einen Bonus aufzuschlagen. Da in Eressea die einzelnen Rohstoffe auf aus unterschiedlichen Regionen kommen, würde erstere Variante wohl dazu führen, dass gar nichts geliefert wird. Die zweite Variante wäre wünschenswert, torpediert aber leider die Optimierung mit Pareto-optimalen Zwischenzuständen. Was bleibt ist die erste Variante eingeschränkt auf einen Typ Gegenstand. Ob der Aufwand lohnt bleibt fraglich.

Unabhängig davon ist es natürlich möglich und sinnvoll Gegenstände die zur Vollendung eines Ziels fehlen ein wenig höher zu bewerten.

Es macht ggf. sinn zwei bzw. drei Arten von Paketen zu unterscheiden:

1. Gruppen von Gegenständen die nur in Summe überhaupt verwendet werden können, also z.b. einzelne Stufen eines Gebäudes, mehrere Komponenten für Tränke oder Waffen. Einzeln können diese Gegenstände am Ziel nicht verarbeitet werden, d.h. es muss gewartet werden, bis die letzte Komponente eingetroffen ist.
2. Gruppen von Gegenständen oder Untergruppen der oberen Kategorie zur vollen Auslastung in der wöchentlichen Produktion nötig sind. Es kann jedoch auch ohne voll Auslastung produziert werden. Das reduziert nur die Zeit in der ggf. etwas anderes getan werden kann.
3. Gruppen von Gegenständen oder Untergruppen der oberen Kategorien, die zur vollen Erfüllung eines Auftrags notwendig sind, d.h. Vollendung eines Schiffes oder Gebäudes, oder volle Ausstattung einer Einheit mit ihrer Ausrüstung. Es kann produziert werden, möglicherweise sogar voll ausgelastet. Es ist nur noch nicht sichergestellt, dass alle Komponenten zur Fertigstellung demnächst eintreffen.

Die letzten beiden Gruppen können in der Praxis wohl zusammengefasst und höchstwahrscheinlich ignoriert werden. Für die erste Gruppe ist ein Erfüllungsbonus jedoch denkbar und liesse sich auch planen.

## Multiwegfindung

Bei der Transportplanung kann es aber durchaus vorkommen, dass ein Transport bereits etwas Ladung und dementsprechend eine Zielregion hat. Es steht aber auf dem Transport noch Kapazität bereit, die durch andere Waren belegt werden könnten. Einfache Möglichkeiten liegen nun darin nur Waren mitzugeben, die in den Zwischenpunkten der Route gebraucht werden. Fortgeschrittene Techniken laden Waren auf, die dadurch dem Ziel ein Stück näher kommen.

Möglich scheint mir aber auch eine Anpassung der Route, dahingehend, dass bei gleicher Dauer zum ersten Ziel eine Route gesucht wird, die gleichzeitig möglichst nah oder sogar über die Region des 2. Zieles führt. Ebenso denkbar ist die Optimierung der Route, das diese über "Umschlagplätze" läuft, um sicherzustellen, dass die Waren für das 2. Ziel dann auch einen Transport in der Gabelregion finden.

Wie also könnte eine solche Multiwegfindung laufen? Die Runden bis zur Ankunft bei Ziel 1 sind bekannt. Es kommen also nur Routen in Frage, die nicht länger dauern. Das erfährt man jedoch erst wenn eine Route gefunden wurde. Die minimale Entfernung zum Ziel 2 ist also zweites Kriterium bei der Routenbewertung und lässt die Routenberechnung ein wenig mehr "greedy" werden, da nun alle Regionen die im Kriterium 1 den gleichen Wert ergeben auf den 2. Wert getestet werden müssen. Glücklicherweise liefert auch hier die Schätzfunktion gute Dienste.

### gleichwertige Ziele

Sind mehrere Ziele gleichwertig, konkurrieren diese natürlich ab einem bestimmten Punkt um die weitere Route. Bis dahin kann man die Route prima auf das Minimum aus beiden Routen optimieren, d.h. man fährt zur näheren Region, und lädt die Waren für die andere Region ab, wenn man möglichst nah dran ist.

Fügt man jedoch mehr und mehr Ziele hinzu, so wird aus dem Transport tatsächlich ein lokaler "Handelsreisender". Ob und wann es sich lohnt hier tatsächlich eine kleine Rundreise zu machen, habe ich noch nicht näher betrachtet. Sicher gibt es aber solche Grenze.

### Umschlagplätze

Die Multiwegfindung kann man sich aber auch wesentlich vereinfachen. Definiert man ausreichend Umschlagplätze, so kann man die Transporte anweisen bei Routen über einer Woche als Zwischenpunkte **immer** Umschlagplätze anzulaufen, oder dies zumindest dann zu tun, wenn eine Kapazitätsgrenze unterschritten ist, oder der Umschlagplatz keinen Umweg bedeutet.

Das Transportsystem der ehemaligen EWG hatte sich diesem Umstand implizit zueigen gemacht, indem es hierarchisch organisiert war. Umschlagplätze sind dort Regionen die untergeordnete Regionen haben. Die Hierarchie bedeutet allerdings oft Umwege. Ob solch ein System gut funktioniert, hängt dann auch von der Topologie der Insel ab. Vor allem Inseln die Ringe bilden, eignen sich wenig für ein streng hierarchisches Transportsystem.

## Bewertungsfunktion

Verschiedene Optimierungsalgorithmen benötigen zur Bewertung von möglichen Zwischen- und Zielzuständen eine Bewertungsfunktion.

Eine solche Funktion für "Logistische Zustände" zu finden, ist auf den ersten Blick nicht einfach.

Was und wie bewertet man nun am besten?

- Befriedigung möglichst vieler Nachfragen?
- Ausnutzung der vorhandenen Transportkapazität?
- Einfluss von Prioritäten und Wertigkeiten?

Am besten stellt man wie auch beim Lernen verschiedene sehr simple Auswahlmöglichkeiten nebeneinander und grenzt sie voneinander ab. Wicht dabei: Alle nicht erwähnten Eigenschaften sind gleich.

Einfache Bewertungsregeln:

- Es ist besser ein nahes Angebot zu verwenden als eine fernes Angebot.
- Es ist besser eine Nachfrage hoher Priorität zu bedienen als eins mit niedriger Priorität.
- Es ist besser eine Nachfrage von einer nahen Quelle zu beliefern, als von einer fernen Quelle.

kompliziertere Bewertungsregeln:

- Es ist besser einen Transport gut auszulasten als diesen mit viel Leerraum fahren zu lassen. Die Abgrenzung von "Gut" und "viel" ist hier die komplizierte Angelegenheit. Gegenstände gleicher Wertigkeit aber unterschiedlichen Gewichts rufen je nach Umgebung andere Herangehensweisen hervor. Kann der Transport mit dem leichten Gegenstand nicht ausgelastet werden und sind keine anderen Güter zu transportieren, dann ist der schwerere Gegenstand vorzuziehen.
- Gruppierte Bedarfe (Pakete) sollen möglichst zur gleichen Zeit (oder zeitnah) am Ziel eintreffen.
- Es ist besser etwas in ein Umschlagzentrum zu bringen als es liegen zu lassen, aber nur wenn das Umschlagzentrum nicht weiter entfernt ist und in einer Woche erreicht werden kann.
- Priorität kann man auch zweidimensional als Dringlichkeit und Wichtigkeit auffassen. Es bedarf aber einer Vergleichsmöglichkeit zweier solcher zweidimensionaler Punkte.
- Es ist besser einen Transport leer in eine Region mit dringend benötigten Angeboten fahren zu lassen, als in eine Umschlagsregion. Letzteres ist aber immer noch besser als nur zu lernen oder nichts zu tun.
- Gibt es in einer nahen Quelle keinen Transport, in einer ferneren Quelle schon, und führt die Route über die nahe Quelle, so soll der Transport genau dann unterbleiben, wenn die ferne Quelle nach Beladung dann weniger von der Ware hätte als die Nahe Quelle nach Beladung.
  - Beipiel:
    - A hat 100 Steine Bedarf.
    - In B, eine Runde von A entfernt, liegen 1000 Steine. Es gibt keinen verfügbaren Transport in B.
    - In C, zwei Runden von A und eine von B entfernt, liegen 500 Steine. Transport verfügbar.
    - -&gt; Transport sollte ggf. leer von C nach B fahren.
    - Liegen in C 2000 Steine, werden die Steine mitgenommen.
    - Liegen in C 1050 Steine, so werden 75 Steine mitgenommen. Beide Quellen haben nach aufladen auf den Transport dann noch 975 Steine.

### Bewertungsbasis Warenwert

Grundlage ist hier ein Basis-Warenwert, der für jeden Gegenstand vom Nutzer vorgegeben wird. Ebenso denkbar sind Berechnungen die Global Angebot und Nachfrage berücksichtigen.

Der Warenwert enthält also ein die globale Wichtigkeit des Gegenstandes.

Der Basis-Warenwert kann z.b. in Silber ausgedrückt werden. Eine Handelsware könnte z.b. als Wert den Mittelwert von Einkaufspreis und Verkaufspreis verwenden. Schwerer wird es knappe Rohstoffe in Silber zu bewerten. Eine Überbewertung würde sonst möglicherweise dazu führen, dass Silber für Unterhalt nicht geliefert wird, weil irgendwo ein Laenschwert fehlt und der Transport deshalb eine andere Route einschlägt.

#### Modifizierung durch Dringlichkeit

Es ist daher klar, dass der Basiswert noch modifiziert werden muss. Dabei sollte die Dringlichkeit sich so stark auswirken können, dass selbst Gegenstände mit niedrigem Basiswert interessant genug werden. Eine exponentielle Funktion o.ä. auf die Dringlichkeit ist somit sinnvoll.

    f(runden bis nötig)=?
    f(0)=10000%*Basiswert
    f(1)=1000%*Basiswert
    f(2)=200%*Basiswert
    f(3)=50%*Basiswert
    f(4)=15%*Basiswert
    f(5)=8%*Basiswert
    f(irgendwann)=5%*Basiswert

Dies wären Werte die mir im Moment vorschweben und die entweder in einer Lookup Tabelle abgelegt werden, oder durch eine Funktion modelliert werden. Die Ausdehnung dieser Formel hängt im wesentlichen von der Bandbreite der verwendeten Basiswerte ab. Ein Flammenschwert, dass irgendwann benötig wird, mag einen Basiswert von 10000 haben, die 10 Silber die in einer anderen Region aber für Unterhalt dringend gebraucht werden, müssen dennoch zu einem Höheren Gesamtwert führen. Mit obiger Formel wäre das Flammenschwert 500 und die 10 Silber 100 wert - zu wenig also um geliefert zu werden. Daher sollten die Parameter der Dringlichkeitsfunktion anhand der min und max werte der Basiswerte berechnet werden.

Ebenso kann natürlich die Wichtigkeit eines Gegenstandes lokal verschieden sein, da die Umgebungsbedingungen andere sind.

#### Modifizierung durch Entfernung

Oft wird es vorkommen, dass eine Ware nicht vom Anbieter direkt zur Nachfrage geschafft werden kann, da beide Regionen zu weit auseinander sind. Damit jedoch eine Belieferung von einer möglichst nahegelegenen Quelle erfolgt, bietet es sich an die Teilausführung einer Nachfrage auf den unterschiedlichen Teilstücken auch unterschiedlich stark zu bewerten.

#### Bewertung von Leerfahrten

Leerfahrten sind unter Umständen nötig, um nicht in Regionen hängen zu bleiben die lediglich als Senken funktionieren.

Für Leerfahrten kann es 2 verschieden motivierte Ziele geben:

1. Ansteuern von Regionen mit dringend benötigten Gütern.
2. Ansteuern von Umschlagsregionen - hier ist immer viel zu transportieren.

Es kann ggf. sogar sinnvoll sein, dass eine leerfahrt

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Transport&oldid=2585] -->
