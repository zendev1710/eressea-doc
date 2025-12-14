---
alias:
    name: magic
    text: Magic
---
# Magic

Magie ist ein mystischer und machtvoller Weg, Dinge zu verändern, zu erschaffen und kann im [[krieg|kampf]] den Feind schwächen oder Verbündete stärken.

## The Study of Magic

Jede Partei muss sich für eines der fünf [Magiegebiete] entscheiden: [Illaun], [Tybied], [Gwyrrd], [Cerddor] oder [Draig]. Das Magiegebiet der Partei wird durch die allererste Einheit bestimmt, die in der Partei Magie lernt. Dies geschieht mit Hilfe des Befehls [LEARN MAGIE "Magiegebiet"]. In Folge heißt der Befehl nur noch [LEARN MAGIE][LEARN MAGIE "Magiegebiet"] und alle Magier einer [Partei] erlernen dann automatisch das von der Partei gewählte Magiegebiet. Es ist jedoch möglich, mehreren Einheiten [LEARN MAGIE "Magiegebiet"] zu befehlen, falls man sich nicht sicher ist, welche Einheit zuerst kommt. Ein einmal gewähltes Magiegebiet kann nicht mehr geändert werden. Deshalb will diese Entscheidung wohl überlegt sein!

Es darf maximal fünf Magiereinheiten pro Partei geben, lediglich Elfenparteien dürfen sechs Magier besitzen. Magiereinheiten dürfen immer nur aus einer Person bestehen. Sie können keine Personen übergeben, auch nicht an leere TEMP-Einheiten.

Das Talent Magie zu erlernen kostet (50 + 25 \* (1 + Stufe) \* Stufe) Silber pro Person und Runde.

Lernkosten

|               |     |     |     |     |     |      |      |      |      |      |      |      |      |      |      |     |       |     |       |     |       |
|---------------|-----|-----|-----|-----|-----|------|------|------|------|------|------|------|------|------|------|-----|-------|-----|-------|-----|-------|
| Nächste Stufe | 1   | 2   | 3   | 4   | 5   | 6    | 7    | 8    | 9    | 10   | 11   | 12   | 13   | 14   | 15   | ... | 20    | ... | 30    | ... | 40    |
| Kosten        | 100 | 200 | 350 | 550 | 800 | 1100 | 1450 | 1850 | 2300 | 2800 | 3350 | 3950 | 4600 | 5300 | 6050 | ... | 10550 | ... | 23300 | ... | 41050 |

Ein ungelernter Magier bezahlt also 100 Silber für seine ersten Lektionen; hat er schon Stufe 5 im Magietalent, so muss er 1100 Silber pro Lernwoche bezahlen.

**Achtung:** Die Lernkosten beziehen sich immer auf die gelernte Stufe vor der Anwendung eventueller Rassenboni oder -mali. Eine Elfe zahlt also für ihren ersten Lernversuch, der sie auf T2 bringt 100 und nicht 200 Silber, ein Goblin mit seinem -1 zahlt für den 2. Lernversuch jedoch bereits 200 Silber obwohl er noch immer auf Stufe 0 ist. (Das System wertet ihn als T1 - 1 = 0).

**Achtung, Zwerge:** Sie haben -2 auf das Magietalent. Eine Einheit, die mit Magie 0 angezeigt wird, kann eigentlich auf T1 oder T2 sein. Die Lernkosten steigen in letzterem Fall jedoch auf 350 Silber! Es gibt keinen Weg herauszufinden, was von beiden zutrifft. Also lieber etwas großzügiger planen.

Lernen in einer [Akademie] kostet das Doppelte. Unterrichtet werden können nur Magier des gleichen Magiegebietes wie der Lehrer. Ein Draig-Magier kann also keinen Illaun-Magier lehren.

Hat eine Magiereinheit nicht genug Silber zum Lernen, lernt sie in der Woche nur anteilig entsprechend der Silbermenge, die sie bezahlen kann. Magie kann auch, durch \[\[Special:MyLanguage/Talente|Anwendung (CAST) gelernt werden. Dafür ist es egal ob die Einheit einen oder mehrere Zauber pro Runde spricht. Natürlich kostet Lernen durch Anwendung kein Silber.

## Sayings

Mit jeder Stufe, die die Einheit in Magie erreicht, kann sie neue Sprüche bekommen. Es gibt zur Zeit einen Spruch in jeder Stufe, in Ausnahmefällen auch einmal mehrere oder gar keinen. Hat man eine neue Stufe erreicht, so werden die Sprüche in der Auswertung beschrieben. Hat man die Beschreibung vergessen, kann man sie sich mit dem Befehl [[cmd-show]] nochmals zeigen lassen.

Eine so angezeigte Spruchbeschreibung sieht ungefähr so aus:

                                     Wunderdoktor

    Beschreibung:
      Wenn einem der Alchemist nicht weiterhelfen kann, geht man zu dem gelehrten
      Tybiedmagier. Seine Tränke und Tinkturen helfen gegen alles, was man sonst
      nicht bekommen kann. Ob nun die kryptische Formel unter dem Holzschuh des
      untreuen Ehemannes wirklich geholfen hat - nun, der des Lesens nicht
      mächtige Bauer wird es nie wissen. Dem Magier hilft es auf jeden Fall...
      beim Füllen seines Geldbeutels. 50 Silber pro Stufe lassen sich so in einer
      Woche verdienen.
    Art: Normaler Zauber
    Stufe: 1
    Rang: 5
    Komponenten:
    -   1 Aura  * Stufe
    Modifikationen: Schiffszauber
    Syntax:
      CAST [LEVEL n] Wunderdoktor

oder so

                        Erschaffe einen Ring der Unsichtbarkeit

    Beschreibung:
      Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit
      erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien
      unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer
      unsichtbaren Einheit muss jede Person einen Ring tragen.
    Art: Normaler Zauber
    Stufe: 6
    Rang: 5
    Komponenten:
    - 50 Aura
    - 3000 Silber
    - 1 permanente Aura
    Modifikationen: Schiffszauber
    Syntax:
      CAST 'Erschaffe einen Ring der Unsichtbarkeit'

### Art

Es gibt Normale Zauber, Präkampfzauber, Kampfzauber und Postkampfzauber.

Normale Zauber werden mit dem Befehl [[cmd-cast]] gezaubert. Ihre Wirkung entfaltet sich entweder sofort (siehe [Befehlsreihenfolge]) oder manchmal auch erst zu einem späteren Zeitpunkt zum Beispiel zum Anfang der folgenden Runde.

Die drei Arten von Kampfzaubern können niemals mit CAST gezaubert werden. Stattdessen werden sie gezaubert, wenn die Einheit aktiv in einen Kampf verwickelt wird. Alle drei Arten können mit dem Befehl [COMBATSPELL LEVEL n "Zauber"] gesetzt werden. Löschen kann man einen bestimmten Kampfzauber mit dem Befehl [COMBATSPELL "Zauber" NOT][COMBATSPELL LEVEL n "Zauber"] oder alle gesetzten Kampfzauber mit [COMBATSPELL NOT][COMBATSPELL LEVEL n "Zauber"]. Kampfzauber wirken in etwa wie die [COMBAT-Befehle], d. h. einmal gesetzt, bleiben sie gespeichert. Eine Einheit kann maximal je einen Präkampfzauber, einen Kampfzauber und einen Postkampfzauber haben. Hat die Einheit beispielsweise schon einen Präkampfzauber und setzt einen neuen Präkampfzauber, so wird der alte durch den neuen ersetzt.

                                  Gesang der Furcht

    Beschreibung:
      Ein gar machtvoller Gesang aus den Überlieferungen der Katzen, der tief in
      die Herzen der Feinde dringt und ihnen Mut und Hoffnung raubt. Furcht wird
      sie zittern lassen und Panik ihre Gedanken beherrschen. Voller Angst werden
      sie versuchen, den gräßlichen Gesängen zu entrinnen und fliehen.
    Art: Kampfzauber
    Stufe: 3
    Rang: 5
    Komponenten:
    -   1 Aura  * Stufe
    Modifikationen:
    Syntax:
      COMBATSPELL [LEVEL n] 'Gesang der Furcht'

Hat eine Magiereinheit Kampfzauber gesetzt, zaubert sie automatisch, sobald sie an einem Kampf teilnimmt. Entweder indem sie selber ATTACK befiehlt oder indem sie durch einen Angriff auf ihre Seite in den Kampf gezogen wurde (siehe [Die Seiten in einer Schlacht]). Das kann also auch passieren, wenn sie auf COMBAT NOT oder FLIEHE steht, falls sie explizit mit dem Befehl [[cmd-attack]] angegriffen wird!

Ein Prä- oder Postkampfzauber wird einmal vor Beginn bzw. nach Ende des Kampfes gezaubert. Ein normaler Kampfzauber einmal in jeder Kampfrunde. Selbstverständlich nur unter der Voraussetzung, dass die Einheit noch ausreichend Aura besitzt (siehe unter [Aura]) und dass sie noch lebt.

### Aura

Aura ist die magische Kraft, mit deren Hilfe Zauberer ihre Magie ausüben. Aura wird durch das Zaubern verbraucht und regeneriert sich mit der Zeit wieder. Eine Magiereinheit kann eine bestimmte maximale Menge Aura aufnehmen. Wie viel, wird - ebenso wie die Auraregeneration - durch das Magietalent der Einheit bestimmt. Die genauen Angaben für jede Einheit stehen im Report, als Faustregel gilt aber, dass das Maximum etwa bei Talent<sup>2</sup> Aura liegt und pro Woche im Durchschnitt etwa (Talent - Stufe) Aura regeneriert wird. Das kann aber zwischen fast gar nichts und Talent - Stufe schwanken. Magische Rassen regenerieren Aura schneller, nichtmagische Rassen deutlich langsamer.

Die maximale Aura ist nicht unveränderlich: Zum einen gibt es einen Zauber, mit dessen Hilfe eine Einheit Aura auf eine andere transferieren kann. Die Zieleinheit kann dadurch kurzfristig mehr Aura erhalten, als sie normalerweise maximal aufnehmen kann. Dadurch kann sie Zauber wirken, deren Kosten über ihrer Maximalaura liegen. Überschüssige Aura geht aber am Ende einer Runde wieder verloren.

Außerdem gibt es Zauber (und möglicherweise andere Dinge), die Magier permanente Aura kosten, wie etwa "Erschaffe einen Ring der Unsichtbarkeit". Das heißt, dass die Einheit fortan weniger maximale Aura speichern kann. In der Regel sind das sehr mächtige Zaubersprüche oder Artefaktmagie, die permanente Effekte hervorrufen.

[CAST] ist ein pseudolanger Befehl vergleichbar mit [[cmd-attack]]. Eine Einheit kann also mehrmals pro Runde zaubern, allerdings keinen anderen langen Befehl ausführen. Das ganze hat aber einen Haken: Die Aura-Kosten der Zauber erhöhen sich. Der erste Zauber, den die Einheit in einer Runde zaubert, kostet die normale, beim Zauber angegebene Aura. Der zweite kostet das Doppelte, der dritte das Vierfache, der vierte das Achtfache usw.

Kampfzauber werden davon gesondert behandelt, sie erhöhen die Kosten für normale Zauber oder andere Kampfzauber nicht und kosten immer nur die angegebene Aura. [Fernzauber] erhöhen ebenfalls die Zauberkosten.

### Caster level

Der Wert, der als "Stufe" angegeben wird, ist zunächst einmal das Mindesttalent, bei dem die Einheit den Zauber bekommt.

Manche Zauber haben feste Wirkungen und Kosten. Sie werden immer auf der Stufe des Zaubers gezaubert und sie kann nicht durch Parameter verändert werden. Für Dinge wie [Magieresistenz] kann sie trotzdem wichtig sein. *Ring der Unsichtbarkeit* wird immer auf Stufe 6 gezaubert und produziert genau einen Ring.

Sehr viele Zauber haben stufenabhängige Wirkungen und Kosten. Ihr Effekt leitet sich von der Stufe ab, auf der gezaubert wurde. Die Details hängen vom jeweiligen Zauber ab. Manchmal betrifft es die Wirkungsdauer, manchmal die Anzahl der verzauberten Personen und so weiter.

Bei diesen variablen Zaubern kann eine Stufe angeben werden, auf der der Zauber gesprochen werden soll. Diese muss gleich oder niedriger sein als das Magietalent der Einheit, sie kann aber über oder unter der normalen Stufe des Zaubers liegen. So kann man den Zauber auf einer niedrigeren Stufe als sein eigenes Talent zaubern.

Durch einen [Ring der Macht], [Andere Gebäude#magierturm] oder [gesegneten Steinkreis] kann die Stärke zusätzlich um je einen Punkt erhöht werden. Dieser Bonus wird zur angegebenen Stufe addiert.

Wird die Stufe weggelassen, wird der Zauber auf der maximal möglichen Stufe, also dem Talentwert der Einheit gezaubert (Modifikationen wie Rassenboni oder Sonderboni wie der für Insekten in Wüsten eingerechnet). Dies ist unter anderem deshalb nicht immer wünschenswert, weil die Stufe auch die [Wahrscheinlichkeit für Patzer] beeinflusst.

Diese Modifikation funktioniert auch bei Kampfzaubern:

     COMBATSPELL LEVEL 2 "Gesang der Furcht"

Das ist zum Beispiel sinnvoll, wenn man sich etwas Aura aufsparen will, um für einen Postkampfzauber noch etwas Aura übrig zu haben.

**Example:**

    CAST LEVEL 4 "Wunderdoktor"

Dieser Zauber wird 4 Aura kosten und 200 Silber verdienen. Mit einem Ring der Macht kostet er immer noch 4 Aura, verdient aber 250 Silber.

### Components

Steht dort einfach nur Anzahl Aura, so heißt das, dass die Kosten fix sind: *Ring der Unsichtbarkeit* kostet immer 50 Aura. Steht dort eine Angabe wie etwa `3 Aura * Stufe`, dann heißt das, dass für einmal Zaubern 3 Aura multipliziert mit der Stufe, auf welcher der Zauber gesprochen wird, an Aurakosten anfallen. *Wunderdoktor* kostet 1 Aura, wenn er auf Stufe 1 gezaubert wird und 30 Aura, wenn er auf Stufe 30 gezaubert wird. Erfordert der Spruch permanente Aura, so verringert sich die maximale Aura der Einheit für immer um diesen Wert. Weitere Komponenten können Kräuter, Rohstoffe, Silber, Tränke oder auch seltene Gegenstände und sogar Bauern sein.

### Distance magic

Fernzauber werden zwar in der Region der Magiereinheit gesprochen, wirken aber in einer anderen. Bei diesen Zaubern kann man dann die folgende Syntax benutzen:

    CAST REGION <x> <y> "Zauber"

Der Zauber wird dann in der angegebenen Region gewirkt. Die X- und Y-Koordinaten beziehen sich dabei auf den [[cmd-origin]]. Diese Modifikation erhöht die Kosten aller Komponenten des Zaubers allerdings exponentiell: Die Kosten für Materialkomponenten und Aura werden pro Region Entfernung zwischen dem Ort der Einheit und dem Ziel verdoppelt (Formel: 2<sup>a</sup>, wobei a die Entfernung der Zielregion zur Region der Einheit ist). Folgende Tabellen zur Illustration:

|                                   |                                   |                                     |                                     |                                     |                                       |
|-----------------------------------|-----------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|---------------------------------------|
| Entfernung Regionen (a)           | 0                                 | 1                                   | 2                                   | 3                                   | 4                                     |
| Anzahl der benötigten Komponenten | 1 Stein  <br>5 Eisen  <br>10 Holz | 2 Steine  <br>10 Eisen  <br>20 Holz | 4 Steine  <br>20 Eisen  <br>40 Holz | 8 Steine  <br>40 Eisen  <br>80 Holz | 16 Steine  <br>80 Eisen  <br>160 Holz |

Aurakosten werden auch erhöht, wenn eine Einheit mehrere Zauber in einer Runde zaubert (Formel: 2<sup>b-1</sup>, wobei b die Anzahl der Zauber in dieser Runde ist, siehe [oben][Aura]). Für andere Komponenten gilt dies nicht, sie werden nur durch Fernzauber erhöht.

Fernzauber und Mehrfachzauber können also auch in Kombination die Aurakosten erhöhen:

| Entfernung Regionen (a) | 0               | 1               | 2                | 3                | 4                |
|-------------------------|-----------------|-----------------|------------------|------------------|------------------|
| Aurakosten (1. Spruch)  | Aurakosten \* 1 | Aurakosten \* 2 | Aurakosten \* 4  | Aurakosten \* 8  | Aurakosten \* 16 |
| Aurakosten (2. Spruch)  | Aurakosten \* 2 | Aurakosten \* 4 | Aurakosten \* 8  | Aurakosten \* 16 | Aurakosten \* 32 |
| Aurakosten (3. Spruch)  | Aurakosten \* 4 | Aurakosten \* 8 | Aurakosten \* 16 | Aurakosten \* 32 | Aurakosten \* 64 |

Die beiden Modifikatoren können auch verknüpft werden:

     CAST REGION <x> <y> LEVEL <nr> "Zauber"

Dabei ist wichtig, dass man erst die Region und dann die Stufe angibt.

**Example:**

Eine Einheit in der Region (1,1) zaubert als ersten Zauberspruch der Runde "Segen der Erde" auf Stufe 3 in die östlich gelegene Nachbarregion (a = 1 Feld Entfernung). Das kostet 2 \* 3 = 6 Aura. Der Befehl für diesen Spruch lautet `CAST REGION 2 1 LEVEL 3 "Segen der Erde"`.

### Ship and sea magic

Neben den Fernzaubern gibt es auch noch zwei andere Klassen von besonderen Sprüchen. Generell können Zauber **nicht von ablegenden Schiffen** aus gezaubert werden. Eine Ausnahme bilden nur die als **Schiffszauber** bezeichneten Sprüche. Sprüche, die als **Seezauber** gekennzeichnet sind, können auch von Nicht-Meermenschen auf dem Ozean gezaubert werden.

### Magic with people and objects

Mit einigen Zaubern kann man Personen und Objekte magisch beeinflussen. Hierbei ist zu beachten, dass die allermeisten Zauber, die auf befreundete Einheiten gezaubert werden sollen, erfordern, dass die Zieleinheit mit [[cmd-contact]] den Magier kontaktiert. Teleports und andere Verzauberungen können ja gut gemeint sein, aber oft auch zu Missetaten benutzt werden, und mit [[cmd-contact]] signalisiert das Ziel, dass es mit der Verzauberung einverstanden ist.

### Rank

Die Reihenfolge der normalen Zauber ergibt sich aus dem Rang des Zaubers. Es werden innerhalb einer Runde immer diejenigen Zauber mit einem niedrigeren Rang vor denjenigen mit einem höheren ausgeführt. Dabei ist Rang 1 der niedrigste und Rang 9 der höchste. Die meisten Zauber haben den Standardrang 5, Antimagiezauber aber haben fast alle Rang 2, werden also gegebenenfalls vor den normalen Zaubern gezaubert. Zauber gleichen Rangs werden in der im Zug angegebenen Reihenfolge gezaubert.

**Example:**

Es gäbe drei Zauber, genannt "Aaaa", "Beee" und "Ceee".

"Aaaa" hat Rang 5 und kostet 10 Aura.

"Beee" hat Rang 2 und kostet 20 Aura.

"Ceee" hat Rang 5 und kostet 5 Aura.

Angenommen die Einheit hat die Befehle

       CAST "Ceee"
       CAST "Beee"
       CAST "Aaaa"

in dieser Reihenfolge. Zuerst wird "Beee" gezaubert, denn der Zauber hat Rang 2. Es ist der erste Zauber der Einheit in dieser Woche, daher kostet er 20 Aura. Dann wird "Ceee" gezaubert, denn "Aaaa" und "Ceee" haben den selben Rang und "Ceee" steht vor "Aaaa". "Ceee" ist der zweite Zauber, er kostet also 5\*2^1=10 Aura. Nun kommt noch "Aaaa". "Aaaa" ist der dritte Zauber, er kostet also 10\*2^2=40 Aura.

## Blunder

Es gibt viel Nichtoffensichtliches im Magiesystem und in den Sprüchen. Generell gilt: Viele Sprüche beinhalten direkte oder indirekte Risiken. Zudem kann ein Zauberer einen Spruch auch verpatzen.

Ein Spruch kann also einfach so fehlschlagen, auch wenn eigentlich alle Komponenten vorhanden sind und die Aura der Einheit ausreicht. Das ist kein Bug und gibt auch eine ganz normale Meldung im Report ("Der Zauber schlägt fehl."). Fehlen Komponenten oder Aura wird dies in der Meldung auch erwähnt.

Die Wahrscheinlichkeit für einen Patzer hängt von vielen Faktoren ab, unter anderem von der Stufe, Schwierigkeitsgrad des Spruchs im Verhältnis zur Stufe, auf der der Spruch vom Magier gezaubert wird, dem Magiegebiet, dem Spruch, der Umgebung, dem Ziel usw.

Patzer können äußerst unangenehme Nebenwirkungen haben! Überlebt die Einheit jedoch einen Patzer, sind diese normalerweise nicht permanent.

Spielererfahrung: Solthar Ein Spruch, der auf der maximal möglichen Stufe gezaubert wird, hat ca 20% Patzerchance; auf der halben Stufe sind es 0% Chance. Für Draigmagier sind es 10% mehr. Mögliche Folgen (in absteigender Häufigkeit):

- Der Zauber funktioniert, aber nachfolgende Sprüche werden viel teurer.
- Alle Aura geht verloren, der Zauber funktioniert oder auch nicht.
- Der Zauber funktioniert nicht und du wirst zur [Kröte] für 2 oder mehr Wochen.
- Der Zauber funktioniert nicht und es gibt einen speziellen Effekt.

Spezielle Effekte betreffen vor allem Gwyrrd (wütende Ents entstehen) und Draig (Bauernmobs oder andere Folgen).

[Kröte]: ./toad.md "Kröte"

## Magic resistance

Die Magieresistenz einer Person/Einheit ist die jeder Person innewohnende Fähigkeit, einem gegen sie gerichteten Zauber zu widerstehen, und wie stark eine Person von magischem Schaden im Kampf betroffen wird. Die Magieresistenz einer Einheit ist:

- die natürliche Magieresistenz der [Rassen]
- plus 5% pro Magietalent
- plus 10% \* Einhörner pro Person
- evtl. Bonus oder Abzug durch [Zauber] auf der Einheit oder der Region
- evtl. Bonus durch [Gebäude][gesegneten Steinkreis]
- Diese Werte werden addiert, das Ergebnis kann aber nie höher als 90% sein.

Bei bestimmten direkten Verzauberungen wird sie zusätzlich von der Erfahrung der Einheit beeinflusst:

- 50% + 5% \* (Höchster Talentwert der verzauberten Einheit - Magietalent der zaubernden Einheit)
- nie unter 2%, nie über 98%

Gegen Kampfzauber wie Feuerbälle und als magisch geltende Waffen wirken stattdessen zusätzlich eventuelle Boni durch [Waffen oder Rüstungen]. Gegen magischen Schaden wirken sonst nur magischer Schutz und die natürliche Rüstung.

Auch "unbelebte Materie", also Regionen, Schiffe, Gebäude usw. haben bisweilen eine Magieresistenz. Auch sie kann durch bestimmte Zauber verstärkt werden.

**Beispiele:** Die Basischance ist 0% für Menschen, 10% für [Elfen], für [Goblins][Elfen] ist sie nur -5%.

Eine Einheit mit Bergbau 10 hat eine 50%-ige Chance, einem Zauber wie [Chaosfluch] gezaubert von einer Einheit mit Magie 10 zu widerstehen. Ist das Magietalent 12, sinkt die Chance auf 40%. Besteht die Zieleinheit aus Goblins, sinkt die Chance weiter auf 35%.

Ein Feuerball, der zum Beispiel 50 Schaden verursachen würde (5d10 + 15), macht gegen einen Elf mit [Laenschwert][Waffen oder Rüstungen] nur (90% \* 70%) = 63% davon, also etwa 31 Schaden.

## Mage Tower

Ein [Magierturm][Andere Gebäude#magierturm] erhöht die Aura-Regeneration um 75% und erhöht die effektive Stufe jedes Zaubers, der in ihnen gezaubert wird, um 1 — gegebenenfalls zusätzlich zu einem Ring der Macht — ohne die Kosten zu erhöhen. Außerdem wird die Wahrscheinlichkeit eines Zauberpatzers deutlich verringert.

## Familiar

Erfahrenen Magiern wird irgendwann auf ihren Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich ihnen anschließen wird. Welcher Gattung dieses Wesen angehört, hängt vor allem von Magiegebiet und Rasse ab. Mehr Details zu diesen Vertrauten kann man im Kapitel über [Vertraute] finden.

## The astral space

**Hinweis:** Auch diesen Abschnitt kannst du auslassen, wenn du die Anleitung zum ersten Mal liest – denn es dauert viele Wochen, bis eine Partei den Astralraum bereisen kann – oder wenn du die komplizierten Regeln des Astralraums lieber selbst herausfinden möchtest.

So unterschiedlich wie die Meinungen, worum es sich dabei eigentlich handelt, sind auch die Namen, die dieser zweiten Ebene des Seins verliehen worden sind: Manche nennen sie die *Welt der Geisterwesen*, andere wiederum die *astrale Welt*, am bekanntesten jedoch ist der Begriff *Astralraum*. In dieser anderen Welt herrschen auch völlig andere Naturgesetze. Diese Tatsache mag der einzige Grund sein, dass der Astralraum überhaupt noch ein praktischer Anwendungsbereich der Magie geblieben ist: Wer es schafft, den Übergang zwischen Astralraum und Wirklichkeit durch seine magischen Kräfte zum richtigen Zeitpunkt verwischen zu lassen, kann daraus große Vorteile erlangen - sei es durch die Wahrnehmung von Dingen auf der jeweils anderen Seite, ohne selbst dabei gesehen zu werden, oder durch die schnelle Reise über große Entfernungen.

Wer den Astralraum betritt – dies ist nur durch bestimmte [Zauber] möglich –, verschwindet vollständig aus der realen Welt. Der Astralraum ist wie die reale Welt in Regionen mit den bekannten Himmelsrichtungen unterteilt. Einheiten, die sich an einem Punkt im Astralraum befinden, tauchen wie andere Einheiten im Report auf und werden auch wie diese gespielt. Sie können also Befehle wie [[cmd-move]] und [[cmd-attack]] erhalten und mit anderen Einheiten in der astralen Welt interagieren. Mit der normalen Welt können sie nur durch Zauber in Verbindung treten.

Die Sinne weltlicher Geschöpfe vermögen es nicht, die Umgebung in der astralen Welt konkret wahrzunehmen. Das Auge erblickt die Umgebung bloß als Nebel, und alle Geräusche sind dumpf und gedämpft. Von jedem Punkt im Astralraum lassen sich bis zu 19 realweltliche Regionen schemenhaft erkennen, die höchstens zwei Regionen Abstand von einer bestimmten realen Region haben, die wir hier den "Bezugspunkt" nennen werden (grün im Bild). Einige Zauber vermögen, diese Schemen genauer erscheinen zu lassen. Im Beispielbild sind alle Regionen, die sich von einer Region erkennen lassen, rot umrandet. Sechs Regionen, die von der roten Linien halbiert werden, sind sogar von je zwei Astralregionen sichtbar.

<!-- TODO: astral connection map 488X393 - should be where in the page ? -->
![Astral space connection](../assets/images/astral-space-connection.jpg "Astral space connection")
<!-- Illustration des Astralraums und der Geometrie seiner Verbindungen</span></a>
<figcaption>Astralraumregionen sind die großen schwarzen Sechsecke, der Bezugspunkt ist grün, die Regionen, die mit der roten Astralraumregion in Verbindung stehen, sind gelb.</figcaption>
-->

Besonders verwirrend wird der Astralraum dadurch, dass diese Schemen nicht identisch sind mit den Regionen, die mit der Astralraumregion verbunden sind, von denen aus man also in die Astralregion gelangen kann und umgekehrt. Stattdessen ist jeder Punkt im Astralraum mit einem Bereich in der normalen Welt verbunden, der je 16 Regionen umfasst (im Bild gelb). Dieser Bereich ist wie ein Parallelogramm geformt mit je vier Regionen Ausdehnung in Richtung Ost-West und Südwest-Nordost. Der "Bezugspunkt" ist die südwestliche Ecke davon. Alle Regionen in so einem Bereich führen beim Betreten der astralen Welt zu demselben Punkt. Diese Verbindung ist für die meisten Zauber, die den Astralraum betreffen, eine Voraussetzung. Sie kann aber auch gestört werden, zum Beispiel durch gesegnete Steinkreise, die kürzlich von einem Magier besucht wurden. Je nach benutztem Zauber können noch weitere Einschränkungen gelten.

Darum ist Vorsicht geboten – denn man kann an einen Punkt im Astralraum einerseits die Schemen von realen Regionen erkennen, die nicht mit diesem Punkt im Realraum verbunden sind, andererseits tauchen nicht alle Regionen der wirklichen Welt, zu denen so eine Verbindung besteht, als Schemen auf. Erst, wenn Reisende sich trotz dieser Unterschiede zurechtfinden, werden sie feststellen, dass sie in der astralen Welt um ein Vielfaches schneller vorankommen können. Denn jeder Schritt in der Geisterwelt entspricht 4 Schritten in der realen Welt.

Nur durch Magie kann die Wirklichkeit derart verändert werden, dass Lebewesen in die Welt der Geisterwesen übertreten. Ferner kann man keine Steine, Pferde, Wagen oder Katapulte in die Welt der Geister mitnehmen. Einzig *Elfenpferde* scheinen als magische Reittiere im Astralraum überleben zu können.

Überhaupt sei jeder vor dem unbedachten Übertritt in den Astralraum gewarnt, wird dieser doch von schrecklichen [Wesen] bewohnt, welche durch gewöhnliche Waffen nicht zu besiegen sind, und die ihren Opfern unbarmherzig Willen und Gedächtnis rauben. Nur wer mächtige magische Waffen oder Verbündete mit sich führt oder sich vor unfreundlichen Blicken außerordentlich gut zu verbergen mag, wird vor diesen Schrecken des Astralraums gefeit sein.

## Lists of all spells

Zu den Anfangszeiten von Eressea waren die genauen Spruchlisten geheim, um "das gespannte Zittern haben zu können, ob und welche neuen Sprüche man beim Erreichen einer neuen Stufe erhält". Inzwischen läuft Eressea aber so lange, dass es einen zu großen Nachteil für neue Spieler gegenüber Veteranen bedeuten würde, wenn die Sprüche nicht bekannt wären. Deshalb gibt es nun eine [Liste aller Zauber][Zauber] und [Zauberbeschreibungen].

Continue reading: [Magiegebiete].

[Magiegebiete]: ./magic-schools.md "Magicgebiete"

<!-- From [https://wiki.eressea.de/index.php?title=Magie/de&oldid=16363] -->

[Illaun]: ./magic-school-illaun.md "Illaunzauber"
[Tybied]: ./magic-school-tybied.md "Tybiedzauber"
[Gwyrrd]: ./magic-school-gwyrrd.md "Gwyrrdzauber"
[Cerddor]: ./magic-school-cerddor.md "Cerddorzauber"
[Draig]: ./magic-school-draig.md "Draigzauber"
[LEARN MAGIE "Magiegebiet"]: ./cmd-learn.md "LEARN"
[Partei]: ./factions.md "Partei"
[Akademie]: ./buildings-others.md "Andere Gebäude"
[CAST]: ./cmd-cast.md "CAST"
[Befehlsreihenfolge]: ./commands-sequence.md "Befehlsreihenfolge"
[COMBATSPELL LEVEL n "Zauber"]: ./cmd-combatspell.md "COMBATSPELL"
[COMBAT-Befehle]: ./war.md#kampfreihen "Krieg"
[Die Seiten in einer Schlacht]: ./war.md#die-seiten-in-einer-schlacht "Krieg"
[Aura]: #aura
[Fernzauber]: #distance-magic
[Magieresistenz]: #magic-resistance
[Ring der Macht]: ./ring-of-power.md "Ring der Macht (to be documented)"
[Andere Gebäude#magierturm]: ./buildings-others.md#mage-tower "Andere Gebäude"
[gesegneten Steinkreis]: ./buildings-others.md#stonecircle "Andere Gebäude"
[Wahrscheinlichkeit für Patzer]: #blunder
[Rassen]: ./races.md "Rasse (to be documented)"
[Zauber]: ./spells-list.md "Zauberliste E2"
[Waffen oder Rüstungen]: ./war-tables.md#magieresistenz "Kriegstabellen"
[Elfen]: ./skills-modifiers.md "Talentmodifikatoren"
[Chaosfluch]: ./spells-list.md#chaosfluch "Zauberliste E2"
[Vertraute]: ./familiars.md "Vertraute"
[Wesen]: ./monsters.md#hirntöter "Monster"
[Zauberbeschreibungen]: ./spells-descriptions.md "Zauberbeschreibungen E2"
