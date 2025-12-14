---
alias: talente
---
# Talente

Eine der wesentlichen Eigenschaften, die [Einheiten] in Eressea definieren, sind ihre Talente. Alle Mitglieder einer Einheit haben dieselben Talente. Jedes Talent hat eine Stufe. Je höher die Stufe desto besser kann die Einheit das Talent benutzen. Um ein Talent zu lernen, kann eine Einheit mit dem Befehl [[bef-lerne]] pro Zug einen Versuch machen, in eine neue Stufe aufzusteigen.

Manche Talente verbessern sich zudem noch durch Anwendung. Wendet die Einheit das Talent lediglich an, dauert es ungefähr dreimal so lange, eine Stufe aufzusteigen, wie beim Lernen. Zu den Talenten, die sich *nicht* durch Anwendung verbessern, gehören alle Waffentalente, Ausdauer, Wahrnehmung, Taktik und Steuereintreiben.

Für die meisten Belange ist der Talentwert entscheidend, der im Report angezeigt wird. Er schließt Rassenboni, Regionsboni und Dinge wie Hunger oder Magie ein, die den Talentwert verändern. Manchmal wird aber auch der "rohe" Talentwert ohne Boni benötigt, vor allem um die Lernkosten von Magie und die Lernzeiten zu berechnen.

## Talente erlernen

Eine weitere Talentstufe zu erreichen, wird von Stufe zu Stufe schwieriger. Im Mittel dauert der Aufstieg in eine neue Talentstufe mit dem Befehl [[bef-lerne]] in etwa Anzahl von Wochen entsprechend der angepeilten Talentstufe, ohne Berücksichtigung von Modifikationen durch [Rasse] oder Terrain. Die minimale Lernzeit beträgt eine Woche. Die maximale Lernzeit übersteigt (2 x neue Stufe − 1) nicht. Diese Extremwerte kommen weniger häufig vor als die durchschnittliche Dauer.

**Beispiele:** Das Aufsteigen von Stufe 3 nach Stufe 4 dauert im Schnitt 4 Wochen, jedoch manchmal nur eine Woche und manchmal bis zu 7 Wochen. Eine [Zwergeneinheit] mit Bergbau 3 im Report hat "roh" eigentlich Stufe 1, da Zwerge auf Bergbau einen Modifikator von +2 haben. Sie benötigt für den Aufstieg im Talent Bergbau von Stufe 3 nach Stufe 4 im Schnitt zwei Wochen.

Um die Zeit herabzusetzen, die eine Einheit zum Erlernen eines Talentes benötigt, kann eine zweite Einheit, die besser ist, die erste Einheit das Talent [lehren]. Diese lehrende Einheit muss eine Talentstufe haben, die um mindestens 2 größer ist als die Talentstufe der Schüler. Damit lernt die gelehrte Einheit doppelt so schnell, als wenn sie versucht, ein Talent auf eigene Faust zu verbessern. Die lehrende Einheit lernt jedoch gar nicht. Ein Lernen in einer [Akademie] bringt einen weiteren Zeitvorteil.

Eine Lehrperson kann maximal 10 Schüler lehren. Hat die "Schüler-Einheit" mehr Personen, als die Lehreinheit lehren kann, so wird dies trotzdem anteilig auf die Zeit, die neue Stufe zu erreichen, angerechnet. Eine Einheit kann mehrere Einheiten lehren, ebenso kann eine Einheit von mehreren Einheiten gelehrt werden, wobei natürlich jede Person nur maximal einmal profitieren kann.

**Beispiel:**

      Einheit l1; 1 Person, Ausdauer 3
      LEHRE s1
      Einheit l2; 1 Person, Hiebwaffen 3, Ausdauer 3
      LEHRE s1 s2
      Einheit s1; 15 Personen, Ausdauer 1
      LERNE Ausdauer
      Einheit s2; 10 Personen, Hiebwaffen 1
      LERNE Hiebwaffen

Ergebnis: Einheit l1 lehrt 10 Personen von Einheit s1 in Ausdauer. Einheit l2 lehrt die restlichen 5 Personen von s1 in Ausdauer und 5 Personen von Einheit s2 in Hiebwaffen. Einheit s1 wird von l1 und l2 gelehrt und lernt doppelt so schnell wie normal. Einheit s2 wird nur zur Hälfte in Ausdauer gelehrt und lernt deshalb nur 50% schneller.

Vorsicht! Lehren mehrere Lehrer-Einheiten mehrere Schüler-Einheiten in verschiedenen Talenten oder Talentstufen seitens der Lehrer, kann es passieren, dass einige Schüler keine oder nicht die richtigen Lehrer abbekommen. Dies lässt sich aufgrund der Interna von Eressea nicht anders gestalten. Hier solltest du also ggf. durch Umstrukturieren der Lehrer-Einheiten "klare Verhältnisse" schaffen. Beim Befehl [LERNE AUTO] versucht der Server, das Lernen und Lehren in einer Region zu automatisieren. Da dies allerdings durch eine einfache Heuristik bewirkt wird, ist nicht garantiert, dass hier eine (dauerhaft) optimale Lernkette entsteht.

[Magie], [Alchemie], [Kräuterkunde][Alchemie], [Spionage][Alchemie] und [Taktik] zu erlernen ist besonders schwer und aufwendig. Spionage zu erlernen kostet 100 Silber pro Person und Runde, Alchemie, Kräuterkunde und Taktik sogar 200 Silber pro Person und Woche. Das Erlernen von Magie kostet auf hohen Stufen leicht mehrere Tausend Silber (siehe [Tabelle][Magie]). Die Einheit, welche eines dieser Talente lernt, muss dieses Silber bei sich tragen. Dabei ist es für die Kosten unerheblich, ob die Einheit gelehrt wird oder nicht. Befindet sich die Einheit in einer [Akademie][1], verdoppeln sich die Lernkosten teurer Talente.

Wenn der lernenden Einheit zum Zeitpunkt des Bezahlens nicht der volle Betrag des Geldes zur Verfügung steht, lernt sie anteilig je nach vorhandener Geldmenge, das heißt, wenn sie beispielsweise nur 500 von 550 Silber hat, sinkt ihre Lerngeschwindigkeit um etwa 10%.

In seltenen Fällen will eine Einheit ein Talent auch wieder loswerden. Dies ist mit dem Befehl [[bef-vergiss]] möglich.

## Mischen von Talenten

Werden Personen in eine Einheit transferiert oder rekrutiert, berechnen sich die neuen Talentstufen nach der Anzahl der Lernwochen, die die beiden Einheiten hatten. Dabei kann es dazu kommen, dass Lernwochen durch Rundungseffekte "verloren gehen". Du solltest also unnötiges Zusammenlegen von Einheiten möglichst vermeiden.

**Beispiel:** Eine Einheit mit zwei Personen mit Hiebwaffen 5 rekrutiert einen Bauern. Die zwei Personen haben bis zum Aufstieg auf Stufe 5 ungefähr je 15 Wochen (nämlich 1+2+3+4+5) gelernt. Bauern haben keine Talente, also wird hier 0 dazugerechnet. Die neue Einheit hat also 3 Personen und ca. 30 Lernwochen. Dies entspricht 3 Personen mit Hiebwaffen 4 (1+2+3+4=10 Wochen pro Person). Die neue Einheit hat also Stufe 4.

Bei der Berechnung der Lernwochen kommt es wie beim Lernen auf die "rohen" Talentwerte an, bei denen alle Boni und -mali wie Rassenboni zunächst abgezogen werden.

Spielererfahrung: Solthar Tatsächlich ist die Sache komplizierter. Das kannst du jedoch überspringen, wenn du diese Anleitung zum ersten Mal liest. Jedes Mal, wenn eine Einheit eine Stufe aufsteigt, wird gewürfelt, wie viele Wochen sie zum Aufstieg auf die nächste Stufe brauchen wird. Dabei ergibt sich ein Wert zwischen 1 und (2 x neue Stufe − 1). Eine Einheit kann also ein Talent zwischen (6,1) – diese Schreibweise bedeutet hier Stufe 6 und noch eine Woche bis zum Aufstieg – und (6,13) haben. Dieser Wert ist "geheim": er wird nirgends angezeigt, nur der Server kennt ihn. Er wird beim Mischen aber mit eingerechnet. Mischst du zum Beispiel eine Person mit (5,6) und eine Person mit (1,2) – beides entspricht genau dem Durchschnitt – haben sie zusammen 16 Lernwochen. Zwei Personen mit (3,4) entsprechen aber nur 12 Lernwochen. Die Differenz von zwei Wochen pro Person wird der neuen Einheit "gutgeschrieben". Sie hat deshalb (3,2) – ein bisschen besser als durchschnittlich.

Beim Mischen von (5,1) und (1,1), also Personen, die schon fast den nächsten Aufstieg geschafft haben, käme sogar (4,4) heraus. Beim Mischen von (5,11) und (1,3) ergibt sich hingegen (3,5) als neuer Wert. Es ist also nicht möglich, den Talentwert einer gemischten Einheit genau vorherzusagen. Es kann lediglich ein Minimal- und Maximalwert angegeben werden.

## Anwendungen von Talenten

Talente ermöglichen Einheiten erst, bestimmte Dinge zu tun. Dabei kommt es manchmal auf die Talentstufe der Einheit an, ab der eine bestimmte Tätigkeit möglich wird. Manchmal spielt auch das Gesamttalent der Einheit eine Rolle, also Personenzahl \* Talentwert.

Talente lassen sich in einige Gruppen einteilen:

### Produktionstalente

Alchemie, Bergbau, Burgenbau, Holzfällen, Kräuterkunde, Pferdedressur, Rüstungsbau, Schiffbau, Steinbau, Straßenbau, Waffenbau, Wagenbau

Dies ist die größte Gruppe von Talenten. Sie ermöglichen es, bestimmte Gegenstände, Gebäude, Schiffe oder Straßen herzustellen. Sie werden im Kapitel [Produktion] und [Alchemie][5] näher erklärt.

### Silbertalente

Handel, Steuereintreiben und Unterhaltung werden gebraucht, um Silber erzeugen zu können. Mehr dazu im Kapitel über [Geld].

### Heimlich & Co

[Spionage], [Tarnung] und [Wahrnehmung] drehen sich um Heimlichkeiten. Sie haben ihre eigenen Kapitel.

### Fortbewegung

Segeln und Reiten werden im Kapitel über [Reisen] erklärt. Reiten ist zudem auch im [Kampf] nützlich.

### Magie

[Magie] ist ein Talent mit besonders großen Auswirkungen und beansprucht ein Kapitel für sich.

### Kampftalente

Die Waffentalente Armbrustschießen, Bogenschießen, Hiebwaffen, Katapultbedienung, Stangenwaffen und Waffenloser Kampf, sowie die besonderen Talente Ausdauer, Reiten und Taktik sind im [Krieg] besonders relevant, sei es gegen andere Parteien oder Monster.

Weiterlesen: [Liste der Talente].

[Liste der Talente]: ./skills-list.md "Liste der Talente"

<!-- From [https://wiki.eressea.de/index.php?title=Talente&oldid=16985] -->

[Einheiten]: ./cmd-unit.md "Einheiten"
[bef-lerne]: ./cmd-learn.md "LERNE"
[Rasse]: ./races.md "Rassen"
[Zwergeneinheit]: ./races.md#swerg "Zwerg"
[lehren]: ./cmd-teach.md "LEHRE"
[Akademie]: ./buildings-others.md#akademie  "Akademie"
[LERNE AUTO]: ./cmd-learn-auto.md "LERNE AUTO"
[Magie]: ./magic.md "Magic"
[Alchemie]: ./skills-list.md "Liste der Talente"
[Taktik]: ./tactic.md "Taktik"
[1]: ./buildings-others.md#akademie "Andere Gebäude"
[bef-vergiss]: ./cmd-forget.md "VERGISS"
[Produktion]: ./production.md "Produktion"
[5]: ./alchemy.md "Alchemie"
[Geld]: ./silver.md "Geld"
[Spionage]: ./skills-list.md#spionage "Spionage"
[Tarnung]: ./camouflage.md "Tarnung"
[Wahrnehmung]: ./camouflage.md "Wahrnehmung"
[Reisen]: ./travel.md "Reisen"
[Kampf]: ./war-tables.md "Kampf"
[Krieg]: ./war.md "Krieg"
