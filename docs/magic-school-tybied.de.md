---
# cSpell:locale de
alias: tybiedzauber
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Tybiedzauber

## Stufe 1

### Magie analysieren

:   Mit diesem Spruch kann der Magier versuchen, die Verzauberungen eines einzelnen angegebenen Objekts zu erkennen.  
    Von allen Sprüchen, die seine eigenen Fähigkeiten nicht überschreiten, wird er einen Eindruck ihres Wirkens erhalten können.  
    Bei stärkeren Sprüchen benötigt er ein wenig Glück für eine gelungene Analyse.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
|   T aura    |   1   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE [STUFE n] 'Magie analysieren' ( REGION | EINHEIT <Einheit-Nr> [<Einheit-Nr> ...] | SCHIFF <Schiff-Nr> [<Schiff-Nr> ...] | BURG <Gebäude-Nr> [<Gebäude-Nr> ...] )`  

### Schleieraura

:   Dieser Zauber wird die gesamte Ausrüstung der Zieleinheit für einige Zeit vor den Blicken anderer verschleiern.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
|   T aura    |   1   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE [STUFE n] Schleieraura <Einheit-Nr>`  

### Wunderdoktor

:   Wenn einem der Alchemist nicht weiterhelfen kann, geht man zu dem gelehrten Tybiedmagier.  
    Seine Tränke und Tinkturen helfen gegen alles, was man sonst nicht bekommen kann.  
    Ob nun die kryptische Formel unter dem Holzschuh des untreuen Ehemannes wirklich geholfen hat - nun, der des Lesens nicht mächtige Bauer wird es nie wissen.  
    Dem Magier hilft es auf jeden Fall...
    beim Füllen seines Geldbeutels.  
    50 Silber pro Stufe lassen sich so in einer Woche verdienen.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
|   T aura    |   1   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE [STUFE n] Wunderdoktor`  

## Stufe 2

### Schutz vor Magie

:   Dieser Zauber legt ein antimagisches Feld um die Magier der Feinde und behindert ihre Zauber erheblich.  
    Nur wenige werden die Kraft besitzen, das Feld zu durchdringen und ihren Truppen in der Schlacht zu helfen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 3 x T aura  |   2   | Prä-k. |  2   |        |       |

`KAMPFZAUBER [STUFE n] 'Schutz vor Magie'`  

## Stufe 3

### Beute Bewahren

:   Dieser Zauber verhindert, dass ein Teil der sonst im Kampf zerstörten Gegenstände beschädigt wird.  
    Die Verluste reduzieren sich um 5% pro Stufe des Zaubers bis zu einem Minimum von 25%.  

| Komponenten | Stufe |   Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:-------:|:----:|:------:|:-----:|
|   T aura    |   3   | Post-k. |  5   |        |       |

`KAMPFZAUBER [STUFE n] 'Beute Bewahren'`  

### Schutzzauber

:   Dieser Zauber verstärkt die natürliche Widerstandskraft gegen Magie.  
    Eine so geschützte Einheit ist auch gegen Kampfmagie weniger empfindlich.  
    Pro Stufe reicht die Kraft des Magiers aus, um 5 Personen zu schützen.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
| 5 x T aura  |   3   | Normal |  2   | :material-check:{ .success } |       |

`ZAUBERE [STUFE n] Schutzzauber <Einheit-Nr> [<Einheit-Nr> ...]`  

## Stufe 4

### Astraler Ausgang

:   Der Magier konzentriert sich auf die Struktur der Realität und kann so die astrale Ebene verlassen.  
    Er kann insgesamt (Stufe-3) x 15 GE durch das kurzzeitig entstehende Tor schicken.  
    Ist der Magier erfahren genug, den Zauber auf Stufen von 11 oder mehr zu zaubern, kann er andere Einheiten auch gegen ihren Willen auf die andere Ebene zwingen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:-----:|
| 2 x T aura  |   4   | Normal |  7   |        |       |

`ZAUBERE [STUFE n] 'Astraler Ausgang' <x> <y> <Einheit-Nr> [<Einheit-Nr> ...]`  

### Astraler Weg

:   Alte arkane Formeln ermöglichen es dem Magier, sich und andere in die astrale Ebene zu schicken.  
    Der Magier kann (Stufe-3) x 15 GE durch das kurzzeitig entstehende Tor schicken.  
    Ist der Magier erfahren genug, den Zauber auf Stufen von 11 oder mehr zu zaubern, kann er andere Einheiten auch gegen ihren Willen auf die andere Ebene zwingen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:-----:|
| 2 x T aura  |   4   | Normal |  7   |        |       |

`ZAUBERE [STUFE n] 'Astraler Weg' <Einheit-Nr> [<Einheit-Nr> ...]`  

## Stufe 5

### Astrale Schwächezone

:   Mit diesem Zauber kann der Magier eine Zone der astralen Schwächung erzeugen, ein lokales Ungleichgewicht im Astralen Feld.  
    Dieses Zone wird bestrebt sein, wieder in den Gleichgewichtszustand zu gelangen.  
    Dazu wird sie jedem in dieser Region gesprochenen Zauber einen Teil seiner Stärke entziehen, die schwächeren gar ganz absorbieren.  

| Komponenten | Stufe |  Art   | Rang | Schiff |            Fern.             |
|:-----------:|:-----:|:------:|:----:|:------:|:----------------------------:|
| 3 x T aura  |   5   | Normal |  2   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] 'Astrale Schwächezone'`  

### Auratransfer

:   Mit Hilfe dieses Zaubers kann der Magier eigene Aura im Verhältnis 2:1 auf einen anderen Magier des gleichen Magiegebietes oder im Verhältnis 3:1 auf einen Magier eines anderen Magiegebietes übertragen.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:-----:|
|   1 aura    |   5   | Normal |  1   | :material-check:{ .success } |       |

`ZAUBERE Auratransfer <Einheit-Nr> <Aura>`  

### Magiefresser

:   Dieser Zauber ermöglicht dem Magier, Verzauberungen einer Einheit, eines Schiffes, Gebäudes oder auch der Region aufzulösen.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern.                        |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:-----------------------------|
| 4 x T aura  |   5   | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] Magiefresser ( REGION | EINHEIT <Einheit-Nr> [<Einheit-Nr> ...] | SCHIFF <Schiff-Nr> [<Schiff-Nr> ...] | BURG <Gebäude-Nr> [<Gebäude-Nr> ...] )`  

### Schockwelle

:   Dieser Zauber läßt eine Welle aus purer Kraft über die gegnerischen Reihen hinwegfegen.  
    Viele Kämpfer wird der Schock so benommen machen, dass sie für einen kurzen Moment nicht angreifen können.  

| Komponenten | Stufe |  Art  | Rang | Schiff | Fern. |
|:-----------:|:-----:|:-----:|:----:|:------:|:------|
|   T aura    |   5   | Kampf |  5   |        |       |

`KAMPFZAUBER [STUFE n] Schockwelle`  

## Stufe 6

### Astraler Ruf

:   Ein Magier, der sich in der astralen Ebene befindet, kann mit Hilfe dieses Zaubers andere Einheiten zu sich holen.  
    Der Magier kann (Stufe-3) x 15 GE durch das kurzzeitig entstehende Tor schicken.  
    Ist der Magier erfahren genug, den Zauber auf Stufen von 13 oder mehr zu zaubern, kann er andere Einheiten auch gegen ihren Willen auf die andere Ebene zwingen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:-----:|
| 2 x T aura  |   6   | Normal |  7   |        |       |

`ZAUBERE [STUFE n] 'Astraler Ruf' <x> <y> <Einheit-Nr> [<Einheit-Nr> ...]`  

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

### Luftschiff

:   Diese magischen Runen bringen ein Boot oder Langboot für eine Woche zum Fliegen.  
    Damit kann dann auch Land überquert werden.  
    Für die Farbe der Runen muss eine spezielle Tinte aus einem Windbeutel und einem Schneekristall angerührt werden.  

|               Komponenten               | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:---------------------------------------:|:-----:|:------:|:----:|:----------------------------:|:------|
| 10 aura, 1 [gousse], 1 [schneekristall] |   6   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE Luftschiff <Schiff-Nr>`  

### Ruf der Realität

:   Ein Magier, welcher sich in der materiellen Welt befindet, kann er mit Hilfe dieses Zaubers Einheiten aus der angrenzenden Astralwelt herbeiholen.  
    Ist der Magier erfahren genug, den Zauber auf Stufen von 13 oder mehr zu zaubern, kann er andere Einheiten auch gegen ihren Willen in die materielle Welt zwingen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 2 x T aura  |   6   | Normal |  7   |        |       |

`ZAUBERE [STUFE n] 'Ruf der Realität' <Einheit-Nr> [<Einheit-Nr> ...]`  

### Stehle Aura

:   Mit Hilfe dieses Zaubers kann der Magier einem anderen Magier seine Aura gegen dessen Willen entziehen und sich selber zuführen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern.                        |
|:-----------:|:-----:|:------:|:----:|:------:|:-----------------------------|
| 2 x T aura  |   6   | Normal |  3   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] 'Stehle Aura' <Einheit-Nr>`  

## Stufe 7

### Erschaffe [Antimagiekristall]

:   Mit Hilfe dieses Zauber entzieht der Magier einem Quarzkristall all seine magischen Energien.  
    Der Kristall wird dann, wenn er zu feinem Staub zermahlen und verteilt wird, die beim Zaubern freigesetzten magischen Energien aufsaugen und die Kraft aller Zauber reduzieren, welche in der betreffenden Woche in der Region gezaubert werden.  

| Mag. |     Komponenten      | Stufe |  Art   | Rang |       Schiff       | Fern. |
|:--------------------:|:-----:|:------:|:----:|:------------------:|:-----:|
| 50 aura, 3000 silber |   7   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE 'Erschaffe Antimagiekristall'`  

### Fluch brechen

:   Dieser Zauber ermöglicht dem Magier, gezielt eine bestimmte Verzauberung einer Einheit, eines Schiffes, Gebäudes oder auch der Region aufzulösen.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            |            Fern.             |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:----------------------------:|
| 3 x T aura  |   7   | Normal |  3   | :material-check:{ .success } | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] 'Fluch brechen' ( REGION | EINHEIT <Einheit-Nr> | SCHIFF <Schiff-Nr> | BURG <Gebäude-Nr> ) <Zauber-ID>`  

### Mauern der Ewigkeit

:   Mit dieser Formel bindet der Magier auf ewig die Kräfte der Erde in die Mauern des Gebäudes.  
    Ein solchermaßen verzaubertes Gebäude ist gegen den Zahn der Zeit geschützt und benötigt keinen Unterhalt mehr.  

|        Komponenten         | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:--------------------------:|:-----:|:------:|:----:|:----------------------------:|:------|
| 50 aura, 1 permanente aura |   7   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE [STUFE n] 'Mauern der Ewigkeit' <Gebäude-Nr>`  

## Stufe 8

### Runen des Schutzes

:   Zeichnet man diese Runen auf die Wände eines Gebäudes oder auf die Planken eines Schiffes, so wird es schwerer durch Zauber zu beeinflussen sein.  
    Jedes Ritual erhöht die Widerstandskraft des Gebäudes oder Schiffes gegen Verzauberung um 20%.  
    Werden mehrere Schutzzauber übereinander gelegt, so addiert sich ihre Wirkung, doch ein hundertprozentiger Schutz läßt sich so nicht erreichen.  
    Der Zauber hält mindestens drei Wochen an, je nach Talent des Magiers aber auch viel länger.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
|   20 aura   |   8   | Normal |  2   | :material-check:{ .success } |       |

`ZAUBERE 'Runen des Schutzes' ( SCHIFF <Schiff-Nr> | BURG <Gebäude-Nr> )`  

### Schild des Fisches

:   Dieser Zauber vermag dem Gegner ein geringfügig versetztes Bild der eigenen Truppen vorzuspiegeln, so wie der Fisch im Wasser auch nicht dort ist wo er zu sein scheint.  
    Von jedem Treffer kann so die Hälfte des Schadens unschädlich abgeleitet werden.  
    Doch hält der Schild nur einige Hundert Schwerthiebe aus, danach wird er sich auflösen.  
    Je stärker der Magier, desto mehr Schaden hält der Schild aus.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 4 x T aura  |   8   | Prä-k. |  2   |        |       |

## Stufe 9

### Beschleunigung

:   Dieser Zauber beschleunigt einige Kämpfer auf der eigenen Seite so, dass sie während des gesamten Kampfes in einer Kampfrunde zweimal angreifen können.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:-----:|
| 5 x T aura  |   9   | Prä-k. |  5   |        |       |

`KAMPFZAUBER [STUFE n] Beschleunigung`  

### Erschaffe einen [Ring der Macht]

:   Dieses mächtige Ritual erschafft einen Ring der Macht.  
    Ein Ring der Macht erhöht die Stärke jedes Zaubers, den sein Träger zaubert, als wäre der Magier eine Stufe besser.  

|               Komponenten                | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:----------------------------------------:|:-----:|:------:|:----:|:----------------------------:|:-----:|
| 100 aura, 1 permanente aura, 4000 silber |   9   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE 'Erschaffe einen Ring der Macht'`  

## Stufe 10

### Blick in die Realität

:   Der Magier kann mit Hilfe dieses Zaubers aus der Astral- in die materielle Ebene blicken und die Regionen und Einheiten genau erkennen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:-----:|
|   40 aura   |  10   | Normal |  5   |        |       |

`ZAUBERE 'Blick in die Realität'`  

### Erschaffe einen [Beutel des Negativen Gewichts]

:   Dieser Beutel umschließt eine kleine Dimensionsfalte, in der bis zu 200 Gewichtseinheiten transportiert werden können, ohne dass sie auf das Traggewicht angerechnet werden.  
    Pferde und andere Lebewesen sowie besonders sperrige Dinge (Wagen und Katapulte) können nicht in dem Beutel transportiert werden.  
    Auch ist es nicht möglich, einen Zauberbeutel in einem anderen zu transportieren.  
    Der Beutel selber wiegt 1 GE.  

|               Komponenten               | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:---------------------------------------:|:-----:|:------:|:----:|:----------------------------:|:-----:|
| 30 aura, 1 permanente aura, 5000 silber |  10   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE 'Erschaffe einen Beutel des Negativen Gewichts'`  

## Stufe 11

### Zeitdehnung

:   Diese praktische Anwendung des theoretischen Wissens um Raum und Zeit ermöglicht es, den Zeitfluß für einige Personen zu verändern.  
    Auf diese Weise veränderte Personen bekommen für einige Wochen doppelt soviele Bewegungspunkte und doppelt soviele Angriffe pro Runde.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
| 5 x T aura  |  11   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE [STUFE n] Zeitdehnung <Einheit-Nr> [<Einheit-Nr> ...]`  

## Stufe 12

### Rüstschild

:   Diese vor dem Kampf zu zaubernde Ritual gibt den eigenen Truppen einen zusätzlichen Bonus auf ihre Rüstung.  
    Jeder Treffer reduziert die Kraft des Zaubers, so dass der Schild sich irgendwann im Kampf auflösen wird.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 4 x T aura  |  12   | Prä-k. |  2   |        |       |

`KAMPFZAUBER [STUFE n] Rüstschild`  

### Vertrauten rufen

:   Einem erfahrenen Magier wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Magier anschließen wird.  

|         Komponenten         | Stufe |  Art   | Rang | Schiff | Fern. |
|:---------------------------:|:-----:|:------:|:----:|:------:|:------|
| 100 aura, 5 permanente aura |  12   | Normal |  5   |        |       |

## Stufe 13

### Belebtes Gestein

:   Dieses kräftezehrende Ritual beschwört mit Hilfe einer Kugel aus konzentriertem Laen einen gewaltigen Erdelementar und bannt ihn in ein Gebäude.  
    Dem Elementar kann dann befohlen werden, das Gebäude mitsamt aller Bewohner in eine Nachbarregion zu tragen.  
    Die Stärke des beschworenen Elementars hängt vom Talent des Magiers ab: Der Elementar kann maximal \[Stufe-12\] x 250 Größeneinheiten große Gebäude versetzen.  
    Das Gebäude wird diese Prozedur nicht unbeschädigt überstehen.  

|                     Komponenten                      | Stufe |  Art   | Rang | Schiff | Fern. |
|:----------------------------------------------------:|:-----:|:------:|:----:|:------:|:-----:|
| 10 x T aura, 1 permanente aura, 5 [laen][laen-de-id] |  13   | Normal |  5   |        |       |

`ZAUBERE [STUFE n] 'Belebtes Gestein' <Gebäude-Nr> <Richtung>`  

## Stufe 14

### Störe Astrale Integrität

:   Dieser Zauber bewirkt eine schwere Störung des Astralraums.  
    Innerhalb eines astralen Radius von Stufe/5 Regionen werden alle Astralwesen, die dem Zauber nicht wiederstehen können, aus der astralen Ebene geschleudert.  
    Der astrale Kontakt mit allen betroffenen Regionen ist für Stufe/3 Wochen gestört.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
|  140 aura   |  14   | Normal |  4   |        |       |

`ZAUBERE [STUFE n] 'Störe Astrale Integrität'`  

## Stufe 15

### Opfere Kraft

:   Mit Hilfe dieses Zaubers kann der Magier einen Teil seiner magischen Kraft permanent auf einen anderen Magier übertragen.  
    Auf einen Magier des selben Magiegebietes kann er die Hälfte der eingesetzten Kraft übertragen, auf andere Magier ein Drittel.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
|  100 aura   |  15   | Normal |  1   |        |       |

`ZAUBERE 'Opfere Kraft' <Einheit-Nr> <Aura>`  

<!-- From [https://wiki.eressea.de/index.php?title=Tybiedzauber&oldid=7486] -->
