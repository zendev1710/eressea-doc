---
alias:
    name: optimizing-learning-chains
    text: Optimizing learning chains
---
# Optimierung Lernketten

## Vorüberlegungen

Als allererstes sollte man sich bei der Optimierung von Lernketten im klaren sein, welche Zuordnungen von Lehrern zu Schülern man bevorzugt. Erst dann kann man entweder ein Regelwerk erstellen (sogenanntes Expertenwissen) oder einen Optimierungsalgorithmus schreiben, der den besten oder zumindest einen möglichst guten Zustand (Zuordnungen von Lehrern und Schülern) erzeugt.

Alle anderen Ansätze die ich bisher gesehen habe, gehören eher in die Kategorie Expertenwissen. Zu nennen seien hier das Techer-Plugin von Magellan oder auch die FF-Tools (2). Die Einheiten werden nach einem Kriterium sortiert und anschliessend abgearbeitet. Dabei werden Sukzessive die Zuordnungen erstellt. Eine Bewertung bzw. Vergleich verschiedener Möglichkeiten findet wenn dann nur auf unterster Ebene statt.

Diese Vorgehensweise ist keineswegs schlecht, da sie gute Ergebnisse in einer super Zeit liefert. Ausserdem ist das Regelwerk klar und verständlich und niemand wird sich wundern, warum eine Zuordnung zustande gekommen ist.

Eine andere Möglichkeit möchte ich hier aber auch aufzeigen: Jeder Teilzustand lässt sich ähnlich wie bei der Wegfindung mit einer Kosten- bzw. Gewinn und einer Schätzfunktion bewerten. Somit lässt ein meist nicht erreichbares Optimum definieren, auf welches man versucht die Zuordnungen hin zu trimmen. Das Wichtigste dabei ist also als erstes die Kosten- bzw. Gewinnfunktion und daraus abgeleitet später die Schätzfunktion.

## Kosten- Gewinnfunktion

Lernen verursacht Kosten, soweit ist das denke ich jedem klar. In Eressea ist es das Silber für den Unterhalt oder auch das für die teuren Talente. Wird man gelehrt, bleiben die Kosten zwar absolut gleich, aber der Lerneffekt ist grösser. Also kann man sagen die Kosten pro Lernwoche sinken auf die Hälfte - Richtig, nicht ganz, denn der Lehrer will ja auch bezahlt sein.

Man kann auch anders rum herangehen und den Lerngewinn maximieren und davon ausgehen die Kosten sind konstant (was ja meist stimmt). Dieser Fall kommt uns entgegen, da lehren dann nicht mehr unendliche Kosten bedeutet (da wir ja nichts lernen).

Eine einfache Gewinnfunktion könnte also folgende Werte pro Person zurückgeben (Beispiel 1):

    Lehrer            = 0
    Lernt ohne Lehrer = 1
    Lernt mit Lehrer  = 2

Soviel kann ich bestätigen, diese Funktion tut was man erwartet - Sie sorgt dafür das möglichst viele Schüler einen Lehrer bekommen. Leider bewertet sie nicht die Talente von Lehrern oder Schülern und sorgt damit dafür, dass über kurz oder lang alle Einheiten innerhalb eines Bereiches von 2-3 Talentstufen sind. Es wird ebenfalls passieren, dass ein Lehrer eine 2 Personen Einheit lehrt.

Es ist also wie anfangs erwähnt wichtig, sich über einige Grenzen im klaren zu werden. Dann müssen diese Grenze, die sich leider oft auch gegenteilig auswirken, in die Kostenfunktion integriert werden.

### Grenzfälle für die Kostenfunktion

Als erstes sollte man festlegen wie viele Schüler ein Lehrer mindestens haben soll, selbst wenn der Talentunterschied lediglich 2 Stufen ist. Desweiteren sollte man klären bis zu welcher Stufe Rekruten gelehrt werden dürfen, d.h. ob T20er auch T0er lehren dürfen. Allgemeiner spezifiziert man, bis zu welcher Talentdifferenz in Abhängigkeit vom Talent des Lehrers wie viele Schüler mindestens gelehrt werden müssen, damit diese Zuordnung günstiger ist, als Lehrer und Schüler lernen zu lassen. Am besten erstellt man sich hier ein kleines Diagramm mit der gewünschten Linie/Kurve und entwickelt dann eine Funktion die diese möglichst gut abdeckt.

Ich habe für mich folgende Funktion entwickelt:

    A = 1.2
    B = 15
    C = 0.34
    Lehrer            = 0
    Lernt ohne Lehrer = (A^Stufe + B) * (3^C)
    Lernt mit Lehrer  = (A^Stufe + B) * (6^C)

Die Parameter A, B und C sind nach langen Tests und teils durch gleichsetzen diverser Formeln entstanden. Die Formel lässt sich problemlos auch fürGehirnschmalz und Akademienutzung verwenden, indem die 3, bzw. 6 durch die Anzahl der Lernversuche \* 3 ersetzt wird. Lernen mit Gehirnschmalz ergibt also (1 + 1/3) \* 3 = 4.

Wir man sich ausrechnen kann, ist lernen mit Lehrer durch Faktor C nicht doppelt so gewinnbringend wie ohne Lehrer, sondern nur ca. 27% mehr wert. Und dadurch, dass die Stufe als Potenz in die Formel eingeht, gewinnt man weit mehr wenn man 8 hochstufe Leute lehrt statt 10 Neulinge.

## Schätzfunktion

Wie erwähnt sollte diese den Gewinn möglichst gut vorhersagen. Wichtig dabei ist, das Optimum nicht zu unterschätzen. Wo aber liegt unser Optimum? Offenbar können nicht alle Leute gelehrt werden, ohne dass es einen Lehrer gibt. D.h. wir können zwar für jede Einheit annehmen sie wird komplett gelehrt, müssen dann aber gleichzeitig das Minimum dessen abziehen, das ein Lehrer als Gewinn hätte erreichen können. Eine sehr gute Näherung dafür ergibt sich also aus:

    Geschätzter Gewinn = Lernt_mit_Lehrer(Stufe) - 0.1 * Lernt_mit_Lehrer(Stufe+2) + 0.01 * Lernt_mit_Lehrer(Stufe+4)

Damit liegen wir definitiv leicht über dem möglichen Optimum.

## A\*-Suche

Die A\*-Suche ist sicher dem einen oder anderen aus der Wegfindung bekannt. Kurz gesagt gibt es einen oder mehrere Zielzustände viele Zwischenzustände und natürlich irgendwo auch einen Startzustand. Diese Zustände sind durch Kanten verbunden. Geht man eine Kante entlang verursacht man Kosten (oder erwirtschaftet Gewinn - je nach Betrachtung). Es wird also ein Pfad im Zustandsgraphen gesucht, der minimale Kosten verursacht oder maximalen Gewinn.

Die A\*Suche optimiert die Suche im Graphen dadurch, das sie nicht alle möglichen Pfade durchsucht, sondern zielgerichtet solche Pfade beschreitet, die geringe geschätze Kosten / hohen geschätzten Gewinn zum Ziel haben.

Wie gut die A\*-Suche funktioniert, hängt daher stark von der Genauigkeit der Schätzfunktion ab. Genauigkeit mein, wie nah der Schätzwert am tatsächlich optimalen Wert liegt.

### Lernzustände

Schwierig ist es nun für dieses Fall der Lernsystemoptimierung die Zustände zu spezifizieren. Es gilt zu unterscheiden, ob eine Einheit Lernt oder Lehrt, wie viele Schüler sie hat, oder wie viele eigene Personen gelehrt werden. Schwieriger wird schon die Frage, ob es interessiert welche Schüler ein Lehrer hat. Haben die Lehrer die selbe Stufe ist es generell ja egal wer davon welchen Schüler lehrt. Praktisch ist das leider nicht so, da jeder Lehrer nur einen Schüler haben kann der von mehreren Lehrern gelehrt wird (der letzte nämlich), es sei denn man gibt bei jedem Lehrer alle Schüler an, aber das wollen wir ja auch nicht (doch es würde auf Serverseite wohl funktionieren).

Bei der Konstruktion der Zustände muss man also aufpassen, dass man nicht zwei vergleichbare Zustände produziert, da damit der Suchraum viel grösser werden kann. Das kommt aber leider sehr oft vor, da nicht selten mehrere gleich gute und gleich grosse Lehrereinheiten existieren. Hier hilft es solche Lehrer nur in einer definierten Reihenfolge zuzulassen. Lehren sollte man solche Einheiten natürlich genau in der umgekehrten Reihenfolge wenn möglich.

Was man recht schnell feststellt ist das die Zahl der Zustände (also Kombinationsmöglichkeiten) exponentiell wächst. Ohne A\*-Suche wäre ein Ergebnis gar nicht denkbar. Leider ist aber auch die A\*-Suche bei mehr als 10 Einheiten immer noch recht lange beschäftigt lässt man sie den allerbesten Zielzustand suchen.

Erst durch "Scheuklappen" ist es mir gelungen den Algorithmus in annehmbarer Zeit zu einem sehr guten Ergebnis zu führen. Oft entspricht dieses Ergebnis dem Optimum. In einigen Fällen übersieht der Algorithmus aber Möglichkeiten. Das hängt mit dem Konstruktionsmechanismus der Zustände zusammen. Ich erzeuge für einen Lehrer nicht alle möglichen Kombinationen Schüler zu lehren, sondern nur solche in denen Top-Down die nächsten freien Einheiten gesucht werden. Das funktioniert i.A. recht gut, in Ausnahemfällen wird dadurch + die Scheuklappen aber ein besserer Zustand "übersehen".

## Statische Lernketten

Bisher wurde besprochen, wie man vorhandene Einheiten als Lehrer/Schüler einplant. Nun soll es darum gehen, welche Einheiten-Struktur man bilden sollte, damit Lehren und Lernen möglichst gut aufeinander abgestimmt werden können. Im folgenden werden einige typische Lehrer-Schüler-Ketten vorgestellt und besprochen:

### Typische Lernketten

- **Einfache Lehrer-Schüler-Kette** -- bestehend aus einer Lehrer-Einheit (L) und einer Schüler-Einheit (S) mit 10\*|L|=|S|. Die Lehrer lernen bis sie zwei Talentstufen Vorsprung haben, dann lehren sie die Schüler. Wenn die Schüler nicht lernen, gehen sie anderen Tätigkeiten nach.  
  Nachteil: Geringes Lerntempo, Vorteile: es werden nur zwei Einheiten benötigt, leicht zu automatisieren. Sinnvoll bei Einheiten bei denen das Lernen nicht im Vordergrund steht, z.B. bei Bergleuten, die hauptsächlich nur lernen um tiefere Erzschichten zu erreichen, oder bei Steuereintreibern, die nach und nach ihre Kampffähigkeiten erhöhen, um kleinere Monstergruppen selbständig bekämpfen zu können.
- **Pyramide** -- Weiterentwicklung der einfachen Lehrer-Schüler-Kette, bestehend aus einer Lehrer-Einheit (L) und mehreren Schichten Schüler-Einheiten (S1,S2,...) mit 10\*|L|=|S1|, 10\*|S1|=|S2| ...  
  Geht es darum beim Lernen [teurer Talente] die Kosten zu minimieren, dann lernt der Lehrer und lehrt anschließend die erste Schüler-Einheit (S1). Diese lehren anschließend S2 usw. Schüler lernen dabei nur, wenn sie gelehrt werden. Das minimiert zwar die Kosten, schneller geht es aber, wenn die Schüler der Zwischen-Schichten auch dann lernen, wenn sie keinen Lehrer haben.  
  Nicht sinnvoll hingegen ist es, wenn auch die *unterste* Schülerschicht ohne Lehrer lernt. Dies führt mittelfristig dazu, das so gut wie gar nicht mehr gelehrt wird, weil es keiner Schicht gelingt einen Talentvorsprung vor der nächst tieferen zu erreichen. Wenn man das will, kann man sich die ganze Pyramidenstruktur sparen und einfach eine Einheit ohne Lehrer lernen lassen.  
  Je mehr Schichten eine Pyramide hat, desto schneller lernt sie. Da mit jeder Schicht die Anzahl der benötigten Personen um den Faktor 10 zunimmt, sind der Höhe der Pyramide allerdings Grenzen gesetzt.
- **Pyramide mit Doppelspitze** -- Die Lehrer-Einheit an der Spitze einer Pyramide lernt mindestens zwei Drittel der Zeit und kann höchstens ein Drittel der Zeit lehren. Ideal wäre es hingegen, wenn die erste Schüler-Einheit die Hälfte der Zeit lernt (und in der anderen Hälfte ihr Wissen weitergibt). Das führt zu der Idee an der Spitze nicht nur eine Lehrer-Einheit sondern zwei zu verwenden.  
  Die Hoffnung zwei Lehrer könnten dann abwechselnd zwei Drittel der Zeit lehren, erweißt sich als trügerisch. Aber eine Erhöhung der Lerngeschwindigkeit erreicht man damit schon. Genauere Analysen zeigen, dass eine Pyramide mit Doppelspitze das selbe Lerntempo erreicht, wie eine normale Pyramide, die eine Schicht mehr hat. Die Pyramide mit Doppelspitze ist dabei zwar etwas weniger effizient (d.h. die Personen haben relativ gesehen weniger Zeit etwas anderes außer Lernen zu machen), funktioniert dafür aber mit weniger Personen.
- **5er-Pyramide** -- Die 5er Pyramide funktioniert wie der Name schon sagt mit einem Faktor 5 bei den Einheitengrössen. Dafür lehrt ein Lehrer immer 2 Einheiten und kommt so auf seine 10-fache Schülerzahl. Dieses System lässt sich über beliebig viele Ebenen staffeln. Die oberste Ebene erhält idealerweise 6 Einheiten gleicher Grösse. Die zweite Ebene 3 Einheiten mit 5-facher Grösse, die dritte Ebene 3 Einheiten 25-facher Grösse. Von den Zwischenebenen lehrt jeweils eine Einheit und 2 werden gelehrt. In der oberste Ebene Lehrt einer und die anderen 5 Einheiten lernen ohne Lehrer, dafür mit Gehirnschmalz und/oder Akademie.
- **Lernen von zwei Talenten** -- Kampfeinheiten (S) lernen in der Regel zwei Talente, ihr [Waffentalent und Ausdauer]. Es erweist sich als sinnvoll dafür auch verschiedene Lehrer (L\_K,L\_A) zu verwenden.  
  Prinzipiell hat man zwei Möglichkeiten: Die Lehrer sind Spezialisten und lernen nur ein Talent. Das ist zwar von der Lerngeschwindigkeit her günstiger, dafür sind solche Spezialisten im Kampffall sehr anfällig (bzw. nicht zu gebrauchen). Alternativ wählt man |S|=9\*|L\_K|=9\*|L\_A|. L\_K lernt das Kampftalent und lehrt dann S und L\_A. L\_A lernt Ausdauer und lehrt dann S und L\_K.
- Pyramiden mit zwei Talenten -- Hier gibt es zahllose Kombinationsmöglichkeiten. Die größten Lerngeschwindigkeiten erzielt man, wenn außer der untersten Schicht alle doppelt besetzt sind, also z.B. L\_K,L\_A,S1\_K,S1\_A,S2\_K,S2\_A,S3. Dafür benötigt man natürlich auch viele Einheiten.

### Lernketten-Analyse

Bei der Beurteilung einer Lernkette spielen vier Faktoren eine Rolle: Mit welcher *Geschwindigkeit* lernt sie (gemessen in Lernversuche/Woche)? Wie *effektiv* ist sie, d.h. wie viel Zeit haben die Personen um etwas anderes zu machen, außer zu lernen? Wie viele *Einheiten* benötigt man? Wie viele *Personen* benötigt man?  
Junge Parteien etwa können keine 5-stufigen Pyramiden aufbauen, weil sie gar nicht so viele Leute haben. Ältere Parteien müssen wegen des Einheiten-Limit ihre Ketten vereinfachen. Produktions-Einheiten wollen viel Zeit zum Arbeiten haben und nur dann lernen, wenn es sich wirklich lohnt usw.  
Mit ein paar Vereinfachungen und etwas Mathematik, kann man Lernketten bezüglich dieser vier Faktoren gut analysieren.

**Vereinfachungen:** 1) Alle Einheiten brauchen gleich lang, um die nächste Stufe zu erreichen. Tatsächlich gibt es zufällige Schwankungen in der Lerndauer bis zur nächsten Stufe und Lehrer müssen etwas mehr lernen als Schüler, weil sie sich auf einer höheren Talent-Stufe befinden.  
2) Die Zeit lässt sich beliebig fein unterteilen. Tatsächlich kann man nur Wochenweise lehren./cmd-learn.md. Praktisch ist diese Unterteilung auch fein genug.  
3) "Lehren" und "gelehrt werden" behindern sich nicht gegenseitig. Denkbar sind Situationen wie: S2 könnte bei S1 lernen, aber auch S3 lehren; S1 kann nicht bei L lernen und S3 kann nicht S4 lehren. Da S2 nicht beides gleichzeitig machen kann, muss entweder S1 oder S3 ohne Lehrer lernen, wobei Zeit verschwendet wird. Tatsächlich können solche Situationen aber (fast) nur in der Startphase auftreten. Damit solch eine Konstellation "von alleine" entsteht, müsste S1 in einer Woche zwei Talentstufen nach oben geklettert sein, was ja doch eher unwahrscheinlich ist.

**Beispielrechnung** für eine Pyramide mit drei Stufen (L,S1,S2): Für jede Einheit ist angegeben, welchen Anteil ihrer Zeit sie damit verbringt gelehrt zu werden / ohne Lehrer zu lernen / zu lehren / etwas anderes zu tun.

- L kann nicht gelehrt werden. Der Anteil der Zeit in der L lernt sei x. Er lehrt also 1-x. Ergibt: \[0 / x / 1-x / 0\].
- S1 wird 1-x von L gelehrt und lernt y ohne Lehrer. Um genauso schnell wie L zu lernen muss 2\*(1-x)+y=x sein. Also ist y=3\*x-2. Die restliche Zeit \[1-(1-x)-(3x-2)=2-2x\] lehrt S1. Ergibt \[1-x / 3x-2 / 2-2x / 0\].
- S2 wird 2-2x von S1 gelehrt die restliche Zeit (1-(2-2x)=2x-1) macht er irgendwas anderes. Ergibt \[2-2x / 0 / 0 / 2x-1\].
- Damit alle gleich schnell lernen, muss x = 2\*(2-2x) sein, also x=4/5. Die Lerngeschwindigkeit ist also 4/5. Die Zeit, die nicht fürs Lernen gebraucht wird (gewichtet mit der Einheitengröße) ist (100\*3/5+10\*0+1\*0)/111=0.540540... Benötigt werden drei Einheiten und 111 Personen. Im folgenden geben wir das als 4-Tupel (0.8000, 0.5405, 3, 111) an.

Im Vergleich dazu die selbe Rechnung unter der Annahme, dass jede Schicht 10% weniger lernen muss, als die nächst-höhere.

- L kann nicht gelehrt werden. Der Anteil der Zeit in der L lernt sei x. Er lehrt also 1-x. Ergibt: \[0 / x / 1-x / 0\].
- S1 wird 1-x von L gelehrt und lernt y ohne Lehrer. Da S1 10% weniger lernen muss als L, gilt: 2\*(1-x)+y= 0.9x . Also ist y=2.9x-2. Die restliche Zeit \[1-(1-x)-(2.9x-2)=2-1.9x\] lehrt S1. Ergibt \[1-x / 2.9x-2 / 2-1.9x / 0\].
- S2 wird 2-1.9x von S1 gelehrt die restliche Zeit (1-(2-1.9x)=1.9x-1) macht er irgendwas anderes. Ergibt \[2-1.9x / 0 / 0 / 1.9x-1\].
- Damit S2 0.9\*0.9=0.81 mal so schnell wie L lernt, muss 0.81x = 2\*(2-1.9x) sein, also x=0.8677. Die Lerngeschwindigkeit von L ist also 0.8677, die von S1 ist 0.7809 und die von S2 ist 0.7028. Im Durchschnitt macht das 0.7113. Die Zeit, die nicht fürs Lernen gebraucht wird (gewichtet mit der Einheitengröße) ist (100\*0.6486+10\*0+1\*0)/111=0.5843.

Man sieht einen deutlichen Unterschied in der errechneten Lerngeschwindigkeit (0.7113 zu 0.8000). Die absolute Größe der im Folgenden angegeben Werte sollte man also nicht auf die Goldwage legen. Interessanter ist der Vergleich untereinander (A ist schneller als B)

Hier nun eine **Übersicht der Lernketten-Analyse** für die oben genannten Beispiele.

- L-S-Kette (Pyramide mit 2 Schichten): (0.6667, 0.6061, 2, 11)
- Pyramide mit 3 Schichten, die Zwischenschicht lernt nicht ohne Lehrer: (0.6667, 0.6306, 3, 111). Mit jeder weiteren Schicht nähert sich der Anteil der nicht mit Lernen verbrachten Zeit der Marke 0.6333. Die Lerngeschwindigkeit bleibt gleich.
- Pyramide mit 3 Schichten, die Zwischenschicht lernt auch ohne Lehrer: (0.8000, 0.5405, 3, 111).
- Pyramide mit 4 Schichten, die Zwischenschichten lernen auch ohne Lehrer: (0.8571, 0.5143, 4, 1111).
- Pyramide mit 5 Schichten, die Zwischenschichten lernen auch ohne Lehrer: (0.8889, 0.5000, 5, 11111).
- Pyramide mit 2 Schichten und Doppelspitze: (0.8000, 0.5000, 3, 12). Zusätzliche Spitzen wirken so ähnlich wie zusätzliche Schichten in einer Pyramide. Die Effizienz ist etwas geringer, dafür werden weniger Personen benötigt.
- Zwei Lehrer (für verschiedene Talente) die jeweils den anderen und eine Schüler-Einheit lehren: (1.0000, 0.4091, 3, 11).
- Zwei Lehrer (für verschiedene Talente) die jeweils nur die Schüler-Einheit lehren: (1.2222, 0.2778, 3, 12). Die Schüler lernen dabei mit Geschwindigkeit 4/3, die Lehrer nur mit 2/3.
- Lehren drei Lehrer drei Verschiedene Talente, dann können die Schüler (fast) immer mit Lehrer lernen. Leider gibt es nur wenige Fälle, in denen man drei Talente dauerhaft lernen will.

### Weitere Einflüsse auf die Geschwindigkeit

Die obigen Anaylsen zeigen wie man aus 100% Zeit mehr Zeit rausholen kann, indem man die lehren nutzt und dabei meist eine Reduzierung der Lerngeschwindigkeit in Kauf nimmt. Für bestimmte Talente ist es aber von enormer Wichtigkeit diese möglichst gut zu beherrschen und trotzdem noch ausreichend Schüler lehren zu können. Ziel ist daher die Lerngeschwindigkeit über 100% (= Immer lernen ohne Lehrer) zu heben.

Bekannt sind die Steigerung durch Akademie und Gehirnschmalz. Sie wirken sich beim Lernen ohne Lehrer jeweils zu 1/3 aus, d.h. beide zusammen ergeben eine Lerngeschwindigkeit von 166%.

Weitere Einflussfaktoren die die maximale Lerngeschwindigkeit steigern sind Rassen, Terrain und Vertraute. Hierbei wird sich zu nutzen gemacht, dass je nach "Zustand" das Talent schwankt und damit durch ändern des Zustands eine Einheit vom Lehrer zum Schüler werden kann. Bestes Beispiel dafür sind Insekten, die so in Kombination mit anderen Rassen jedes Talent pushen können.

Ohne zu sehr ins Detail zu gehen, halten wir fest die maximale Lerngeschwindigkeit der besten Einheiten kann über 100% liegen. Damit müssen obige Betrachtungen noch erweitert werden.

#### 5er Pyramide

Gehen wir von einer Akademie und Gehirnschmalz für die 6 Lehrer-Einheiten aus. So erhalten wir 5/3=166%. Beim lehren gibt es keinen Lernfortschritt (Schüler nicht in Akademie) daher 0/3 = 0% in dem Fall. Ein Lehrer lehrt, 5 Lernen -&gt; 1/6 \* 0/3 + 5/6 \* 5/3= 0 + 25/18 = 139%. Die nächste Ebene mit 3 Lehrereinheiten teilt sich in 2 lernende und 1 lehrende auf: 2/3 \* 6/3 + 1/3 \* 0% = 4/3 = 133% Das ist leicht langsamer, aber am Ende doch schneller, da jede Ebene etwa 10% weniger lernen muss, wie oben schon erwähnt. 1-2 weitere solche Zwischenebenen sind möglich und verfünffachen so jeweils die Zahl der möglichen Schüler.

Beginnt man mit 2er Einheiten an der Spitze so füllen diese eine Akademie zur Hälfte - brauchen aber auch viel Gehirnschmalz. Die erste Zwischenebene hat dann 3 Einheiten á 10 Personen, die zweite 3 Einheiten mit je 50 Personen. Die dritte und wohl meist letzte Zwischenebene hat 250 Personen pro Einheit und kann so 2500 Personen auf einmal ausbilden - mit 200%, d.h. die Schüler holen auf. Sonst wären es 3750 die mit 133% hochgelehrt werden können. d.h. nach Abzug einiger Prozente für die Stufenunterschiede sollten 4000 Schüler möglich sein.

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Lernketten&oldid=3553] -->

[teurer Talente]: ./skills.md "Talente"
[Waffentalent und Ausdauer]: ./skills-list.md "Liste der Talente"
