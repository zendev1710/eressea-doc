---
# cSpell:locale de
alias: gwyrrdzauber
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Gwyrrdzauber

## Stufe 1

### Erschaffe [Steingolems]

<div class="lore-dialogue">
"Man befeuchte einen kluftfreien Block aus feinkristallinen Gestein mit einer Phiole des Lebenswassers bis dieses vollständig vom Gestein aufgesogen wurde.
Sodann richte man seine Kraft auf die sich bildende feine Aura des Lebens und forme der ungebundenen Kraft ein Gehäuse."
</div>

:   Je mehr Kraft der Magier investiert, desto mehr Golems können geschaffen werden, bevor die Aura sich verflüchtigt.  
    Jeder Golem hat jede Runde eine Chance von 10 Prozent zu Staub zu zerfallen.  
    Gibt man den Golems die Befehle MACHE BURG oder MACHE STRASSE, so werden pro Golem 4 Steine verbaut und der Golem löst sich auf.  

|                               Komponenten                               | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------------------------------------------------------------------:|:-----:|:------:|:----:|:------:|:-----:|
| 2 x T aura, T [steine][stein], 1 [wasser des lebens][wasser-des-lebens] |   1   | Normal |  4   |        |       |

`ZAUBERE [STUFE n] 'Erschaffe Steingolems'`  

### Segen der Erde

:   Dieses Ernteritual verbessert die Erträge der arbeitenden Bauern in der Region um ein Silberstück.  
    Je mehr Kraft der Druide investiert, desto länger wirkt der Zauber.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern.                        |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:-----------------------------|
|   T aura    |   1   | Normal |  5   | :material-check:{ .success } | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] 'Segen der Erde'`  

### Viehheilung

:   Die Fähigkeiten der Gwyrrd-Magier in der Viehzucht und Heilung sind bei den Bauern sehr begehrt.  
    Gerade auf Märkten sind ihre Dienste häufig sehr gefragt.  
    Manch einer mag auch sein Talent dazu nutzen, ein Tier für einen besseren Preis zu verkaufen.  
    Pro Stufe kann der Magier so 50 Silber verdienen.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
|   T aura    |   1   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE [STUFE n] Viehheilung`  

### Erschaffe [Eisengolems]

:   Je mehr Kraft der Magier investiert, desto mehr Golems können geschaffen werden.  
    Jeder Golem hat jede Runde eine Chance von 15 Prozent zu Staub zu zerfallen.  
    Gibt man den Golems den Befehl MACHE SCHWERT/BIHÄNDER oder MACHE SCHILD/KETTENHEMD/PLATTENPANZER, so werden pro Golem 4 Eisenbarren verbaut und der Golem löst sich auf.  

|                              Komponenten                               | Stufe |  Art   | Rang | Schiff | Fern. |
|:----------------------------------------------------------------------:|:-----:|:------:|:----:|:------:|:-----:|
| 2 x T aura, T [eisen][eisen], 1 [wasser des lebens][wasser-des-lebens] |   2   | Normal |  4   |        |       |

`ZAUBERE [STUFE n] 'Erschaffe Eisengolems'`  

### Hainzauber

:   Wo sonst aus einem Stecken nur ein Baum sprießen konnte, so treibt nun jeder Ast Wurzeln.  

|                             Komponenten                              | Stufe |  Art   | Rang | Schiff | Fern.                        |
|:--------------------------------------------------------------------:|:-----:|:------:|:----:|:------:|:-----------------------------|
| 4 x T aura, T [holz][holz], 1 [wasser des lebens][wasser-des-lebens] |   2   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] Hainzauber`  

### [Bergwächter]

:   Erschafft einen Wächtergeist, der in Gletschern und Bergen Eisen- und Laenabbau durch nichtalliierte Parteien (HELFE BEWACHE) verhindert, solange er die Region bewacht.  
    Der Bergwächter ist an den Ort der Beschwörung gebunden.  

| Komponenten | Stufe |  Art   | Rang | Schiff |            Fern.             |
|:-----------:|:-----:|:------:|:----:|:------:|:----------------------------:|
| 3 x T aura  |   3   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] Bergwächter`  

### Firuns Fell

:   Dieser Zauber ermöglicht es dem Magier Insekten auf magische Weise vor der lähmenden Kälte der Gletscher zu bewahren.  
    Sie können Gletscher betreten und dort normal agieren.  
    Der Spruch wirkt auf Stufe x 10 Insekten.  
    Ein Ring der Macht erhöht die Menge der verzauberbaren Insekten zusätzlich um 10.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:-----:|
| 2 x T aura  |   3   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE [STUFE n] 'Firuns Fell' <Einheit-Nr> [<Einheit-Nr> ...]`  

### Hagel

:   Im Kampf ruft der Magier die Elementargeister der Kälte an und bindet sie an sich.  
    Sodann kann er ihnen befehlen, den Gegner mit Hagelkörnern und Eisbrocken zuzusetzen.  

| Komponenten | Stufe |  Art  | Rang | Schiff | Fern. |
|:-----------:|:-----:|:-----:|:----:|:------:|:------|
|   T aura    |   3   | Kampf |  5   |        |       |

`KAMPFZAUBER [STUFE n] Hagel`  

### Rostregen

:   Mit diesem Ritual wird eine dunkle Gewitterfront beschworen, die sich unheilverkündend über der Region auftürmt.  
    Der magische Regen wird alles Erz rosten lassen.  
    Eisenwaffen und Rüstungen werden schartig und rostig.  
    Die Zerstörungskraft des Regens ist von der investierten Kraft des Magiers abhängig.  
    Für jede Stufe können bis zu 10 Eisenwaffen betroffen werden.  
    Ein Ring der Macht verstärkt die Wirkung wie eine zusätzliche Stufe.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern.                        |
|:-----------:|:-----:|:------:|:----:|:------:|:-----------------------------|
| 2 x T aura  |   3   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] Rostregen <Einheit-Nr> [<Einheit-Nr> ...]`  

### Magischer Pfad

:   Durch Ausführung dieser Rituale ist der Magier in der Lage einen mächtigen Erdelementar zu beschwören.  
    Solange dieser in den Boden gebannt ist, wird kein Regen die Wege aufweichen und kein Fluß Brücken zerstören können.  
    Alle Reisende erhalten damit die gleichen Vorteile, die sonst nur ein ausgebautes gepflastertes Straßennetz bietet.  
    Selbst Sümpfe und Gletscher können so verzaubert werden.  
    Je mehr Kraft der Magier in den Bann legt, desto länger bleibt die Straße bestehen.  

|               Komponenten                | Stufe |  Art   | Rang |            Schiff            | Fern.                        |
|:----------------------------------------:|:-----:|:------:|:----:|:----------------------------:|:-----------------------------|
| T aura, 1 [stein][stein], 1 [holz][holz] |   4   | Normal |  5   | :material-check:{ .success } | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] 'Magischer Pfad'`  

### Segne Mallornstecken

:   Diese Ritual verstärkt die Wirkung des magischen Trankes um ein vielfaches.  
    Wo sonst aus einem Stecken nur ein Baum sprießen konnte, so treibt nun jeder Ast Wurzeln.  

|                                    Komponenten                                    | Stufe |  Art   | Rang | Schiff | Fern.                        |
|:---------------------------------------------------------------------------------:|:-----:|:------:|:----:|:------:|:-----------------------------|
| 6 x T aura, T [mallorns][mallorn-de-id], 1 [wasser des lebens][wasser-des-lebens] |   4   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] 'Segne Mallornstecken'`  

### Wasserelementar

:   Der Magier zwingt mit diesem Ritual die Elementargeister des Wassers in seinen Dienst und bringt sie dazu, das angegebene Schiff schneller durch das Wasser zu tragen.  
    Zudem wird das Schiff nicht durch ungünstige Winde oder Strömungen beeinträchtigt.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
|   T aura    |   4   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE [STUFE n] Wasserelementar <Schiff-Nr>`  

### Windschild

:   Die Anrufung der Elementargeister des Windes beschwört plötzliche Windböen, kleine Windhosen und Luftlöcher herauf, die die gegnerischen Schützen behindern werden.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
| 2 x T aura  |   4   | Prä-k. |  5   | :material-check:{ .success } |       |

`KAMPFZAUBER [STUFE n] Windschild`  

### Astralschutzgeister

:   Dieses Ritual beschwört einige Elementargeister der Magie und schickt sie in die Reihen der feindlichen Magier.  
    Diesen wird das Zaubern für die Dauer des Kampfes deutlich schwerer fallen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:-----:|
| 5 x T aura  |   5   | Prä-k. |  2   |        |       |

`KAMPFZAUBER [STUFE n] Astralschutzgeister`  

### Erschaffe einen [magischen Kräuterbeutel]

:   Der Druide nehme etwas präpariertes Leder, welches er in einem großen Ritual der Reinigung von allen unreinen Geistern befreie, und binde dann einige kleine Geister der Luft und des Wassers in das Material.  
    Aus dem so vorbereiteten Leder fertige er nun ein kleines Beutelchen, welches in ihm aufbewahrte Kräuter besser zu konservieren vermag.  

|                             Komponenten                              | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:--------------------------------------------------------------------:|:-----:|:------:|:----:|:----------------------------:|:-----:|
| 30 aura, 1 permanente aura, 1 [wasser des lebens][wasser-des-lebens] |   5   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE 'Erschaffe einen magischen Kräuterbeutel'`  

### Heilung

:   Nicht nur der Feldscher kann den Verwundeten einer Schlacht helfen.  
    Druiden vermögen mittels einer Beschwörung der Elementargeister des Lebens Wunden zu schließen, gebrochene Knochen zu richten und selbst abgetrennte Glieder wieder zu regenerieren.  

| Komponenten | Stufe |   Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:-------:|:----:|:------:|:------|
|   T aura    |   5   | Post-k. |  5   |        |       |

`KAMPFZAUBER [STUFE n] Heilung`  

### Wirbelwind

:   Diese Beschwörung öffnet ein Tor in die Ebene der Elementargeister des Windes.  
    Sofort erheben sich in der Umgebung des Tors starke Winde oder gar Stürme und behindern alle Schützen einer Schlacht.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
|   15 aura   |   5   | Prä-k. |  5   |        |       |

`KAMPFZAUBER [STUFE n] Wirbelwind`  

### Erdelementar

:   Der Druide beschwört mit diesem Ritual einen Elementargeist der Erde und bringt ihn dazu, die Erde erbeben zu lassen.  
    Dieses Erdbeben wird alle Gebäude in der Region beschädigen.  

|          Komponenten          | Stufe |  Art   | Rang | Schiff |            Fern.             |
|:-----------------------------:|:-----:|:------:|:----:|:------:|:----------------------------:|
| 25 aura, 2 [laen][laen-de-id] |   7   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] Erdelementar`  

### Erschaffe ein [Amulett des wahren Sehens]

:   Der Spruch ermöglicht es einem Magier, ein Amulett des Wahren Sehens zu erschaffen.  
    Das Amulett erlaubt es dem Träger, alle Einheiten, die durch einen Ring der Unsichtbarkeit geschützt sind, zu sehen.  
    Einheiten allerdings, die sich mit ihrem Tarnungs-Talent verstecken, bleiben weiterhin unentdeckt.  

|               Komponenten               | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:---------------------------------------:|:-----:|:------:|:----:|:----------------------------:|:-----:|
| 50 aura, 3000 silber, 1 permanente aura |   6   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE 'Erschaffe ein Amulett des wahren Sehens'`  

### Erschaffe einen [Ring der Unsichtbarkeit]

:   Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit erschaffen.  
    Der Träger des Ringes wird für alle Einheiten anderer Parteien unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag.  
    In einer unsichtbaren Einheit muss jede Person einen Ring tragen.  

|               Komponenten               | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:---------------------------------------:|:-----:|:------:|:----:|:----------------------------:|:-----:|
| 50 aura, 3000 silber, 1 permanente aura |   6   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE 'Erschaffe einen Ring der Unsichtbarkeit'`  

### Meditation

:   Mit Hilfe dieses Zaubers kann der Magier eigene Aura im Verhältnis 2:1 auf einen anderen Magier des gleichen Magiegebietes übertragen.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
|   2 aura    |   6   | Normal |  1   | :material-check:{ .success } |       |

`ZAUBERE Meditation <Einheit-Nr> <Aura>`  

### Sturmelementar

:   Die Beschwörung von Elementargeistern der Stürme ist ein uraltes Ritual.  
    Der Druide bannt die Elementare in die Segel der Schiffe, wo sie helfen, das Schiff mit hoher Geschwindigkeit über die Wellen zu tragen.  
    Je mehr Kraft der Druide in den Zauber investiert, desto größer ist die Zahl der Elementargeister, die sich bannen lassen.  
    Für jedes Schiff wird ein Elementargeist benötigt.  

| Komponenten | Stufe |  Art   | Rang |              Schiff              | Fern. |
|:-----------:|:-----:|:------:|:----:|:--------------------------------:|:------|
| 6 x T aura  |   6   | Normal |  5   | :material-check:{ .success }[^3] |       |

`ZAUBERE [STUFE n] Sturmelementar <Schiff-Nr> [<Schiff-Nr> ...]`  

### Heimstein

:   Mit dieser Formel bindet der Magier auf ewig die Kräfte der Erde in die Mauern der Burg, in der er sich gerade befindet.  
    Weder magisch noch mit schwerem Geschütz können derartig gestärkte Mauern zerstört werden, und auch das Alter setzt ihnen weniger zu. Das Gebäude bietet sodann auch einen besseren Schutz gegen Angriffe mit dem Schwert wie mit Magie.  

|        Komponenten         | Stufe |  Art   | Rang | Schiff | Fern. |
|:--------------------------:|:-----:|:------:|:----:|:------:|:------|
| 50 aura, 1 permanente aura |   7   | Normal |  5   |        |       |

`ZAUBERE Heimstein`  

### Wolfsgeheul

:   Nicht wenige Druiden freunden sich im Laufe ihres Lebens in der Natur mit den ältesten Freunden der großen Völker an.  
    Sie erlernen, mit einem einzigen heulenden Ruf viele ihrer Freunde herbeizurufen, um ihnen im Kampf beizustehen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 2 x T aura  |   7   | Prä-k. |  5   |        |       |

`KAMPFZAUBER [STUFE n] Wolfsgeheul`  

### Blick des Basilisken

:   Dieser schwierige, aber effektive Kampfzauber benutzt die Elementargeister des Steins, um eine Reihe von Gegnern für die Dauer des Kampfes in Stein zu verwandeln.  
    Die betroffenen Personen werden nicht mehr kämpfen, können jedoch auch nicht verwundet werden.  

| Komponenten | Stufe |  Art  | Rang | Schiff | Fern. |
|:-----------:|:-----:|:-----:|:----:|:------:|:-----:|
|   T aura    |   8   | Kampf |  5   |        |       |

`KAMPFZAUBER [STUFE n] 'Blick des Basilisken'`  

### Geister bannen

:   Wie die alten Lehren der Druiden berichten, besteht das, was die normalen Wesen Magie nennen, aus Elementargeistern.  
    Der Magier beschwört und bannt diese in eine Form, um den gewünschten Effekt zu erzielen.  
    Dieses Ritual nun vermag es, in diese Welt gerufene Elementargeister zu vertreiben, um so ein Objekt von Magie zu befreien.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            |            Fern.             |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:----------------------------:|
| 6 x T aura  |   8   | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] 'Geister bannen' ( REGION | EINHEIT <Einheit-Nr> [<Einheit-Nr> ...] | SCHIFF <Schiff-Nr> [<Schiff-Nr> ...] | BURG <Gebäude-Nr> [<Gebäude-Nr> ...] )`  

### Starkes Tor und feste Mauer

:   Mit dieser Formel bindet der Magier zu Beginn eines Kampfes einige Elementargeister des Fels in die Mauern des Gebäudes, in dem er sich gerade befindet.  
    Das Gebäude bietet sodann einen besseren Schutz gegen Angriffe mit dem Schwert wie mit Magie.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 2 x T aura  |   8   | Prä-k. |  5   |        |       |

`KAMPFZAUBER [STUFE n] 'Starkes Tor und feste Mauer'`  

### Heiliger Boden

:   Dieses Ritual beschwört verschiedene Naturgeister in den Boden der Region, welche diese fortan bewachen.  
    In einer so gesegneten Region werden niemals wieder die Toten ihre Gräber verlassen, und anderswo entstandene Untote werden sie wann immer möglich meiden.  

|        Komponenten         | Stufe |  Art   | Rang | Schiff | Fern. |
|:--------------------------:|:-----:|:------:|:----:|:------:|:------|
| 80 aura, 3 permanente aura |   9   | Normal |  5   |        |       |

`ZAUBERE 'Heiliger Boden'`  

### Sog des Lebens

:   Ein Druide, den es in die Welt der Geister verschlagen hat, kann mit Hilfe dieses Zaubers Stufe x 5 Gewichtseinheiten in einen Wald auf der materiellen Welt zurückschicken.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 2 x T aura  |   9   | Normal |  7   |        |       |

`ZAUBERE [STUFE n] 'Sog des Lebens' <x> <y> <Einheit-Nr> [<Einheit-Nr> ...]`  

### Weg der Bäume

:   Große Macht liegt in Orten, an denen das Leben pulsiert.  
    Der Druide kann diese Kraft sammeln und so ein Tor in die Welt der Geistwesen erschaffen.  
    Der Druide kann dann Stufe x 5 Gewichtseinheiten durch das Tor entsenden.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 3 x T aura  |   9   | Normal |  7   |        |       |

`ZAUBERE [STUFE n] 'Weg der Bäume' <Einheit-Nr> [<Einheit-Nr> ...]`  

### Erwecke [Ents]

:   Mit Hilfe dieses Zaubers weckt der Druide die in den Wälder der Region schlummernden Ents aus ihrem äonenlangen Schlaf.  
    Die wilden Baumwesen werden sich ihm anschließen und ihm beistehen, jedoch nach einiger Zeit wieder in Schlummer verfallen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:-----:|
| 6 x T aura  |  10   | Normal |  5   |        |       |

`ZAUBERE [STUFE n] 'Erwecke Ents'`  

### Vertrauten rufen

:   Einem erfahrenen Magier wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Magier anschließen wird.  

|         Komponenten         | Stufe |  Art   | Rang | Schiff | Fern. |
|:---------------------------:|:-----:|:------:|:----:|:------:|:------|
| 100 aura, 5 permanente aura |  10   | Normal |  5   |        |       |

`ZAUBERE 'Vertrauten rufen'`  

### Segne Steinkreis

:   Dieses Ritual segnet einen Steinkreis, der zuvor aus Steinen und etwas Holz gebaut werden muss.  
    Die Segnung des Druiden macht aus dem Kreis eine mächtige Stätte magischen Wirkens, die Schutz vor Magie und erhöhte Aura- Regeneration bewirkt.  
    Man sagt, Jungfrauen seien in der Umgebung von Steinkreisen seltsame Wesen begegnet.  

|         Komponenten         | Stufe |  Art   | Rang | Schiff | Fern. |
|:---------------------------:|:-----:|:------:|:----:|:------:|:------|
| 350 aura, 5 permanente aura |  11   | Normal |  5   |        |       |

`ZAUBERE 'Segne Steinkreis' <Gebäude-Nr>`  

### Rindenhaut

:   Dieses vor dem Kampf zu zaubernde Ritual gibt den eigenen Truppen einen zusätzlichen Bonus auf ihre Rüstung.  
    Jeder Treffer reduziert die Kraft des Zaubers, so dass der Schild sich irgendwann im Kampf auflösen wird.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 4 x T aura  |  12   | Prä-k. |  2   |        |       |

`KAMPFZAUBER [STUFE n] Rindenhaut`  

### Hitzeelementar

:   Dieses Ritual beschwört wütende Elementargeister der Hitze.  
    Eine Dürre sucht das Land heim.  
    Bäume verdorren, Tiere verenden, und die Ernte fällt aus.  
    Für Tagelöhner gibt es kaum noch Arbeit in der Landwirtschaft zu finden.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern.                        |
|:-----------:|:-----:|:------:|:----:|:------:|:-----------------------------|
|  600 aura   |  13   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] Hitzeelementar`  

### Mahlstrom

:   Dieses Ritual beschört einen großen Wasserelementar aus den Tiefen des Ozeans.  
    Der Elementar erzeugt einen gewaltigen Strudel, einen Mahlstrom, welcher alle Schiffe, die ihn passieren, schwer beschädigen kann.  

|                   Komponenten                    | Stufe |  Art   | Rang |              Schiff              | Fern. |
|:------------------------------------------------:|:-----:|:------:|:----:|:--------------------------------:|:------|
| 200 aura, 1 [seeschlangenkopf][seeschlangenkopf] |  15   | Normal |  5   | :material-check:{ .success }[^3] |       |

`ZAUBERE Mahlstrom`  

### Wurzeln der Magie

:   Mit Hilfe dieses aufwändigen Rituals läßt der Druide einen Teil seiner Kraft dauerhaft in den Boden und die Wälder der Region fliessen.  
    Dadurch wird das Gleichgewicht der Natur in der Region für immer verändert, und in Zukunft werden nur noch die anspruchsvollen, aber kräftigen Mallorngewächse in der Region gedeihen.  

|                       Komponenten                        | Stufe |  Art   | Rang | Schiff | Fern.                        |
|:--------------------------------------------------------:|:-----:|:------:|:----:|:------:|:-----------------------------|
| 250 aura, 10 permanente aura, 1  [[pot-of-toadslime-de]] |  16   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] 'Wurzeln der Magie'`  

### Tor in die Ebene der Hitze

:   Dieses mächtige Ritual öffnet ein Tor in die Elementarebene der Hitze.  
    Eine grosse Dürre kommt über das Land.  
    Bauern, Tiere und Pflanzen der Region kämpfen um das nackte Überleben, aber eine solche Dürre überlebt wohl nur die Hälfte aller Lebewesen.  
    Der Landstrich kann über Jahre hinaus von den Folgen einer solchen Dürre betroffen sein.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern.                        |
|:-----------:|:-----:|:------:|:----:|:------:|:-----------------------------|
|  800 aura   |  17   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] 'Tor in die Ebene der Hitze'`  

<!-- From [https://wiki.eressea.de/index.php?title=Gwyrrdzauber&oldid=7693] -->
