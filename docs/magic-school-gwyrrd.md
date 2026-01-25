---
# cSpell:locale en
alias: gwyrrd-spells
---
# Gwyrrd spells

## Steingolems

| Type      |   Rang | Components           | Modifiers      |
|:----------|-------:|----------------------|----------------|
| normal    |        |                      |                |
| :-------- | -----: | -------------------- | -------------- |
|           |        |                      |                |

**Description**:  
Man befeuchte einen kluftfreien Block aus feinkristallinen Gestein mit einer Phiole des Lebenswassers bis dieses vollständig vom Gestein aufgesogen wurde. Sodann richte man seine Kraft auf die sich bildende feine Aura des Lebens und forme der ungebundenen Kraft ein Gehäuse. Je mehr Kraft der Magier investiert, desto mehr Golems können geschaffen werden, bevor die Aura sich verflüchtigt. Jeder Golem hat jede Runde eine Chance von 10 Prozent zu Staub zu zerfallen. Gibt man den Golems die Befehle MAKE BURG oder MAKE STRASSE, so werden pro Golem 4 Steine verbaut und der Golem löst sich auf.  
**Type**: normal spell  
**Level**: 1  
**Rank**: 4  
**Components**: 2 x L Aura, L [stone], 1 [water of life]  
**Modifiers**:  
**Syntax**: `CAST [LEVEL n] "Erschaffe Steingolems"`  

## Segen der Erde

**Description**:  
Dieses Ernteritual verbessert die Erträge der arbeitenden Bauern in der Region um ein Silberstück. Je mehr Kraft der Druide investiert, desto länger wirkt der Zauber.  
**Type**: normal spell  
**Level**: 1  
**Rank**: 5  
**Components**: L Aura  
**Modifiers**: Fernzauber, Schiffszauber  
**Syntax**: `CAST [REGION x y] [LEVEL n] "Segen der Erde"`  

## Viehheilung

**Description**:  
Die Fähigkeiten der Gwyrrd-Magier in der Viehzucht und Heilung sind bei den Bauern sehr begehrt. Gerade auf Märkten sind ihre Dienste häufig sehr gefragt. Manch einer mag auch sein Talent dazu nutzen, ein Tier für einen besseren Preis zu verkaufen. Pro niveau kann der Magier so 50 Silber verdienen.  
**Type**: normal spell  
**Level**: 1  
**Rank**: 5  
**Components**: L Aura  
**Modifiers**: Schiffszauber  
**Syntax**: `CAST [LEVEL n] "Viehheilung"`  

## Eisengolems

**Description**:  
Je mehr Kraft der Magier investiert, desto mehr Golems können geschaffen werden. Jeder Golem hat jede Runde eine Chance von 15 Prozent zu Staub zu zerfallen. Gibt man den Golems den Befehl MAKE SCHWERT/BIHÄNDER oder MAKE SCHILD/KETTENHEMD/PLATTENPANZER, so werden pro Golem 4 Eisenbarren verbaut und der Golem löst sich auf.  
**Type**: normal spell  
**Level**: 2  
**Rank**: 4  
**Components**: 2 x L Aura, L [iron], 1 [water of life]  
**Modifiers**:  
**Syntax**: `CAST [LEVEL n] "Erschaffe Eisengolems"`  

## Hainzauber

**Description**:  
Wo sonst aus einem Stecken nur ein Baum sprießen konnte, so treibt nun jeder Ast Wurzeln.  
**Type**: normal spell  
**Level**: 2  
**Rank**: 5  
**Components**: 4 x L Aura, L [wood], 1 [water of life]  
**Modifiers**: Fernzauber  
**Syntax**: `CAST [REGION x y] [LEVEL n] "Hainzauber"`  

## Bergwächter

**Description**:  
Erschafft einen Wächtergeist, der in Gletschern und Bergen Eisen- und Laenabbau durch nichtalliierte Parteien (HELP GUARD) verhindert, solange er die Region bewacht. Der Bergwächter ist an den Ort der Beschwörung gebunden.  
**Type**: normal spell  
**Level**: 3  
**Rank**: 5  
**Components**: 3 x L Aura  
**Modifiers**: Fernzauber  
**Syntax**: `CAST [REGION x y] [LEVEL n] "Bergwächter"`  

## Firuns Fell

**Description**:  
Dieser Zauber ermöglicht es dem Magier Insekten auf magische Weise vor der lähmenden Kälte der Gletscher zu bewahren. Sie können Gletscher betreten und dort normal agieren. Der Spruch wirkt auf Stufex10 Insekten. Ein Ring der Macht erhöht die Menge der verzauberbaren Insekten zusätzlich um 10.  
**Type**: normal spell  
**Level**: 3  
**Rank**: 5  
**Components**: 2 x L Aura  
**Modifiers**: Schiffszauber  
**Syntax**: `CAST [LEVEL n] "Firuns Fell" <unit-id> [<unit-id> ...]`  

## Hagel

**Description**:  
Im Kampf ruft der Magier die Elementargeister der Kälte an und bindet sie an sich. Sodann kann er ihnen befehlen, den Gegner mit Hagelkörnern und Eisbrocken zuzusetzen.  
**Type**: Kampfzauber  
**Level**: 3  
**Rank**: 5  
**Components**: L Aura  
**Modifiers**:  
**Syntax**: `COMBATSPELL [LEVEL n] "Hagel"`  

## Rostregen

**Description**:  
Mit diesem Ritual wird eine dunkle Gewitterfront beschworen, die sich unheilverkündend über der Region auftürmt. Der magische Regen wird alles Eisenerz rosten lassen. Eisenwaffen und Rüstungen werden schartig und rostig. Die Zerstörungskraft des Regens ist von der investierten Kraft des Magiers abhängig. Für jede niveau können bis zu 10 Gegenstände betroffen werden. Ein Ring der Macht verstärkt die Wirkung wie eine zusätzliche niveau.  
**Type**: normal spell  
**Level**: 3  
**Rank**: 5  
**Components**: 2 x L Aura  
**Modifiers**: Fernzauber  
**Syntax**: `CAST [REGION x y] [LEVEL n] "Rostregen" <unit-id> [<unit-id> ...]`  

## Magischer Pfad

**Description**:  
Durch Ausführung dieser Rituale ist der Magier in der Lage einen mächtigen Erdelementar zu beschwören. Solange dieser in den Boden gebannt ist, wird kein Regen die Wege aufweichen und kein Fluß Brücken zerstören können. Alle Reisende erhalten damit die gleichen Vorteile, die sonst nur ein ausgebautes gepflastertes Straßennetz bietet. Selbst Sümpfe und Gletscher können so verzaubert werden. Je mehr Kraft der Magier in den Bann legt, desto länger bleibt die Straße bestehen.  
**Type**: normal spell  
**Level**: 4  
**Rank**: 5  
**Components**: L Aura, 1 [stone], 1 Holz  
**Modifiers**: Fernzauber, Schiffszauber  
**Syntax**: `CAST [REGION x y] [LEVEL n] "Magischer Pfad"`  

## Segne Mallornstecken

**Description**:  
Diese Ritual verstärkt die Wirkung des magischen Trankes um ein vielfaches. Wo sonst aus einem Stecken nur ein Baum sprießen konnte, so treibt nun jeder Ast Wurzeln.  
**Type**: normal spell  
**Level**: 4  
**Rank**: 5  
**Components**: 6 x L Aura, L [mallorn], 1 [water of life]  
**Modifiers**: Fernzauber  
**Syntax**: `CAST [REGION x y] [LEVEL n] "Segne Mallornstecken"`  

## Wasserelementar

**Description**:  
Der Magier zwingt mit diesem Ritual die Elementargeister des Wassers in seinen Dienst und bringt sie dazu, das angegebene Schiff schneller durch das Wasser zu tragen. Zudem wird das Schiff nicht durch ungünstige Winde oder Strömungen beeinträchtigt.  
**Type**: normal spell  
**Level**: 4  
**Rank**: 5  
**Components**: L Aura  
**Modifiers**: Schiffszauber  
**Syntax**: `CAST [LEVEL n] "Beschwörung eines Wasserelementares" <Schiff-id>`  

## Windschild

**Description**:  
Die Anrufung der Elementargeister des Windes beschwört plötzliche Windböen, kleine Windhosen und Luftlöcher herauf, die die gegnerischen Schützen behindern werden.  
**Type**: post-combat spell  
**Level**: 4  
**Rank**: 5  
**Components**: 2 x L Aura  
**Modifiers**:  
**Syntax**: `COMBATSPELL [LEVEL n] "Windschild"`  

## Astralschutzgeister

**Description**:  
Dieses Ritual beschwört einige Elementargeister der Magie und schickt sie in die Reihen der feindlichen Magier. Diesen wird das Zaubern für die Dauer des Kampfes deutlich schwerer fallen.  
**Type**: post-combat spell  
**Level**: 5  
**Rank**: 2  
**Components**: 5 x L Aura  
**Modifiers**:  
**Syntax**: `COMBATSPELL [LEVEL n] "Astralschutzgeister"`  

## Erschaffe einen magischen Kräuterbeutel

**Description**:  
Der Druide nehme etwas präpariertes Leder, welches er in einem großen Ritual der Reinigung von allen unreinen Geistern befreie, und binde dann einige kleine Geister der Luft und des Wassers in das Material. Aus dem so vorbereiteten Leder fertige er nun ein kleines Beutelchen, welches in ihm aufbewahrte Kräuter besser zu konservieren vermag.  
**Type**: normal spell  
**Level**: 5  
**Rank**: 5  
**Components**: 30 Aura, 1 permanente Aura, 1 [water of life]  
**Modifiers**: Schiffszauber  
**Syntax**: `CAST "Erschaffe einen magischen Kräuterbeutel"`  

## Heal

**Description**:  
Nicht nur der Feldscher kann den Verwundeten einer Schlacht helfen. Druiden vermögen mittels einer Beschwörung der Elementargeister des Lebens Wunden zu schließen, gebrochene Knochen zu richten und selbst abgetrennte Glieder wieder zu regenerieren.  
**Type**: Postkampfzauber  
**Level**: 5  
**Rank**: 5  
**Components**: L Aura  
**Modifiers**:  
**Syntax**: `COMBATSPELL [LEVEL n] "Heal"`  

## Wirbelwind

**Description**:  
Diese Beschwörung öffnet ein Tor in die Ebene der Elementargeister des Windes. Sofort erheben sich in der Umgebung des Tors starke Winde oder gar Stürme und behindern alle Schützen einer Schlacht.  
**Type**: post-combat spell  
**Level**: 5  
**Rank**: 5  
**Components**: 15 Aura  
**Modifiers**:  
**Syntax**: `COMBATSPELL [LEVEL n] "Wirbelwind"`  

## Erdelementar

**Description**:  
Der Druide beschwört mit diesem Ritual einen Elementargeist der Erde und bringt ihn dazu, die Erde erbeben zu lassen. Dieses Erdbeben wird alle Gebäude in der Region beschädigen.  
**Type**: normal spell  
**Level**: 6  
**Rank**: 5  
**Components**: 25 Aura, 2 Laen  
**Modifiers**: Fernzauber  
**Syntax**: `CAST [REGION x y] "Beschwöre einen Erdelementar"`  

## Erschaffe ein Amulett des wahren Sehens

**Description**:  
Der Spruch ermöglicht es einem Magier, ein Amulett des Wahren Sehens zu erschaffen. Das Amulett erlaubt es dem Träger, alle Einheiten, die durch einen Ring der Unsichtbarkeit geschützt sind, zu sehen. Einheiten allerdings, die sich mit ihrem Tarnungs-Talent verstecken, bleiben weiterhin unentdeckt.  
**Type**: normal spell  
**Level**: 6  
**Rank**: 5  
**Components**: 50 Aura, 3000 Silber, 1 permanente Aura  
**Modifiers**: Schiffszauber  
**Syntax**: `CAST "Erschaffe ein Amulett des wahren Sehens"`  

## Erschaffe einen Ring der Unsichtbarkeit

**Description**:  
Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer unsichtbaren unit muss jede Person einen Ring tragen.  
**Type**: normal spell  
**Level**: 6  
**Rank**: 5  
**Components**: 50 Aura, 3000 Silber, 1 permanente Aura  
**Modifiers**: Schiffszauber  
**Syntax**: `CAST "Erschaffe einen Ring der Unsichtbarkeit"`  

## Meditation

**Description**:  
Mit Hilfe dieses Zaubers kann der Magier eigene Aura im Verhältnis 2:1 auf einen anderen Magier des gleichen Magiegebietes übertragen.  
**Type**: normal spell  
**Level**: 6  
**Rank**: 1  
**Components**: 2 Aura  
**Modifiers**: Schiffszauber  
**Syntax**: `CAST "Meditation" <unit-id> <Aura>`  

## Sturmelementar

**Description**:  
Die Beschwörung von Elementargeistern der Stürme ist ein uraltes Ritual. Der Druide bannt die Elementare in die Segel der Schiffe, wo sie helfen, das Schiff mit hoher Geschwindigkeit über die Wellen zu tragen. Je mehr Kraft der Druide in den Zauber investiert, desto größer ist die Zahl der Elementargeister, die sich bannen lassen. Für jedes Schiff wird ein Elementargeist benötigt.  
**Type**: normal spell  
**Level**: 6  
**Rank**: 5  
**Components**: 6 x L Aura  
**Modifiers**: Seezauber, Schiffszauber  
**Syntax**: `CAST [LEVEL n] "Beschwöre einen Sturmelementar" <Schiff-id> [<Schiff-id> ...]`  

## Heimstein

**Description**:  
Mit dieser Formel bindet der Magier auf ewig die Kräfte der Erde in die Mauern der Burg, in der er sich gerade befindet. Weder magisch noch mit schwerem Geschütz können derartig gestärkte Mauern zerstört werden, und auch das Alter setzt ihnen weniger zu. Das Gebäude bietet sodann auch einen besseren Schutz gegen Angriffe mit dem Schwert wie mit Magie.  
**Type**: normal spell  
**Level**: 7  
**Rank**: 5  
**Components**: 50 Aura, 1 permanente Aura  
**Modifiers**:  
**Syntax**: `CAST "Heimstein"`  

## Wolfsgeheul

**Description**:  
Nicht wenige Druiden freunden sich im Laufe ihres Lebens in der Natur mit den ältesten Freunden der großen Völker an. Sie erlernen, mit einem einzigen heulenden Ruf viele ihrer Freunde herbeizurufen, um ihnen im Kampf beizustehen.  
**Type**: post-combat spell  
**Level**: 7  
**Rank**: 5  
**Components**: 2 x L Aura  
**Modifiers**:  
**Syntax**: `COMBATSPELL [LEVEL n] "Wolfsgeheul"`  

## Blick des Basilisken

**Description**:  
Dieser schwierige, aber effektive Kampfzauber benutzt die Elementargeister des Steins, um eine Reihe von Gegnern für die Dauer des Kampfes in Stein zu verwandeln. Die betroffenen Personen werden nicht mehr kämpfen, können jedoch auch nicht verwundet werden.  
**Type**: Kampfzauber  
**Level**: 8  
**Rank**: 5  
**Components**: L Aura  
**Modifiers**:  
**Syntax**: `COMBATSPELL [LEVEL n] "Blick des Basilisken"`  

## Geister bannen

**Description**:  
Wie die alten Lehren der Druiden berichten, besteht das, was die normalen Wesen Magie nennen, aus Elementargeistern. Der Magier beschwört und bannt diese in eine Form, um den gewünschten Effekt zu erzielen. Dieses Ritual nun vermag es, in diese Welt gerufene Elementargeister zu vertreiben, um so ein Objekt von Magie zu befreien.  
**Type**: normal spell  
**Level**: 8  
**Rank**: 2  
**Components**: 6 x L Aura  
**Modifiers**: Fernzauber, Schiffszauber  
**Syntax**: `CAST [REGION x y] [LEVEL n] "Geister bannen" ( REGION | UNIT <unit-id> [<unit-id> ...] | SCHIFF <Schiff-id> | BURG <Gebäude-id> )`  

## Starkes Tor und feste Mauer

**Description**:  
Mit dieser Formel bindet der Magier zu Beginn eines Kampfes einige Elementargeister des Fels in die Mauern des Gebäudes, in dem er sich gerade befindet. Das Gebäude bietet sodann einen besseren Schutz gegen Angriffe mit dem Schwert wie mit Magie.  
**Type**: post-combat spell  
**Level**: 8  
**Rank**: 5  
**Components**: 2 x L Aura  
**Modifiers**:  
**Syntax**: `COMBATSPELL [LEVEL n] "Starkes Tor und feste Mauer"`  

## Heiliger Boden

**Description**:  
Dieses Ritual beschwört verschiedene Naturgeister in den Boden der Region, welche diese fortan bewachen. In einer so gesegneten Region werden niemals wieder die Toten ihre Gräber verlassen, und anderswo entstandene Untote werden sie wann immer möglich meiden.  
**Type**: normal spell  
**Level**: 9  
**Rank**: 5  
**Components**: 80 Aura, 3 permanente Aura  
**Modifiers**:  
**Syntax**: `CAST "Heiliger Boden"`  

## Sog des Lebens

**Description**:  
Ein Druide, den es in die Welt der Geister verschlagen hat, kann mit Hilfe dieses Zaubers Stufex5 Gewichtseinheiten in einen Wald auf der materiellen Welt zurückschicken.  
**Type**: normal spell  
**Level**: 9  
**Rank**: 7  
**Components**: 2 x L Aura  
**Modifiers**:  
**Syntax**: `CAST [LEVEL n] "Sog des Lebens" <x> <y> <unit-id> [<unit-id> ...]`  

## Weg der Bäume

**Description**:  
Große Macht liegt in Orten, an denen das Leben pulsiert. Der Druide kann diese Kraft sammeln und so ein Tor in die Welt der Geistwesen erschaffen. Der Druide kann dann Stufex5 Gewichtseinheiten durch das Tor entsenden.  
**Type**: normal spell  
**Level**: 9  
**Rank**: 7  
**Components**: 3 x L Aura  
**Modifiers**:  
**Syntax**: `CAST [LEVEL n] "Weg der Bäume" <unit-id> [<unit-id> ...]`  

## Erwecke Ents

**Description**:  
Mit Hilfe dieses Zaubers weckt der Druide die in den Wälder der Region schlummernden Ents aus ihrem äonenlangen Schlaf. Die wilden Baumwesen werden sich ihm anschließen und ihm beistehen, jedoch nach einiger Zeit wieder in Schlummer verfallen.  
**Type**: normal spell  
**Level**: 10  
**Rank**: 5  
**Components**: 6 x L Aura  
**Modifiers**:  
**Syntax**: `CAST [LEVEL n] "Erwecke Ents"`  

## Vertrauten rufen

**Description**:  
Einem erfahrenen Druidem wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Druiden anschließen wird.  
**Type**: normal spell  
**Level**: 10  
**Rank**: 5  
**Components**: 100 Aura, 5 permanente Aura  
**Modifiers**:  
**Syntax**: `CAST "Vertrauten rufen"`  

## Segne Steinkreis

**Description**:  
Dieses Ritual segnet einen Steinkreis, der zuvor aus Steinen und etwas Holz gebaut werden muss. Die Segnung des Druiden macht aus dem Kreis eine mächtige Stätte magischen Wirkens, die Schutz vor Magie und erhöhte Aura- Regeneration bewirkt. Man sagt, Jungfrauen seien in der Umgebung von Steinkreisen seltsame Wesen begegnet.  
**Type**: normal spell  
**Level**: 11  
**Rank**: 5  
**Components**: 350 Aura, 5 permanente Aura  
**Modifiers**:  
**Syntax**: `CAST "Segne Steinkreis" <Gebäude-id>`  

## Rindenhaut

**Description**:  
Dieses vor dem Kampf zu zaubernde Ritual gibt den eigenen Truppen einen zusätzlichen Bonus auf ihre Rüstung. Jeder Treffer reduziert die Kraft des Zaubers, so dass der Schild sich irgendwann im Kampf auflösen wird.  
**Type**: post-combat spell  
**Level**: 12  
**Rank**: 2  
**Components**: 4 x L Aura  
**Modifiers**:  
**Syntax**: `COMBATSPELL [LEVEL n] "Rindenhaut"`  

## Hitzeelementar

**Description**:  
Dieses Ritual beschwört wütende Elementargeister der Hitze. Eine Dürre sucht das Land heim. Bäume verdorren, Tiere verenden, und die Ernte fällt aus. Für Tagelöhner gibt es kaum noch Arbeit in der Landwirtschaft zu finden.  
**Type**: normal spell  
**Level**: 13  
**Rank**: 5  
**Components**: 600 Aura  
**Modifiers**: Fernzauber  
**Syntax**: `CAST [REGION x y] "Beschwörung eines Hitzeelementar"`  

## Mahlstrom

**Description**:  
Dieses Ritual beschwört einen großen Wasserelementar aus den Tiefen des Ozeans. Der Elementar erzeugt einen gewaltigen Strudel, einen Mahlstrom, welcher alle Schiffe, die ihn passieren, schwer beschädigen kann.  
**Type**: normal spell  
**Level**: 15  
**Rank**: 5  
**Components**: 200 Aura, 1 Seeschlangenkopf  
**Modifiers**: Seezauber, Schiffszauber  
**Syntax**: `CAST "Mahlstrom"`  

## Wurzeln der Magie

**Description**:  
Mit Hilfe dieses aufwändigen Rituals läßt der Druide einen Teil seiner Kraft dauerhaft in den Boden und die Wälder der Region fliessen. Dadurch wird das Gleichgewicht der Natur in der Region für immer verändert, und in Zukunft werden nur noch die anspruchsvollen, aber kräftigen Mallorngewächse in der Region gedeihen.  
**Type**: normal spell  
**Level**: 16  
**Rank**: 5  
**Components**: 250 Aura, 10 permanente Aura, 1 Tiegel mit Krötenschleim  
**Modifiers**: Fernzauber  
**Syntax**: `CAST [REGION x y] "Wurzeln der Magie"`  

## Tor in die Ebene der Hitze

**Description**:  
Dieses mächtige Ritual öffnet ein Tor in die Elementarebene der Hitze. Eine grosse Dürre kommt über das Land. Bauern, Tiere und Pflanzen der Region kämpfen um das nackte Überleben, aber eine solche Dürre überlebt wohl nur die Hälfte aller Lebewesen. Der Landstrich kann über Jahre hinaus von den Folgen einer solchen Dürre betroffen sein.  
**Type**: normal spell  
**Level**: 17  
**Rank**: 5  
**Components**: 800 Aura  
**Modifiers**: Fernzauber  
**Syntax**: `CAST [REGION x y] "Tor in die Ebene der Hitze"`  

<!-- From [https://wiki.eressea.de/index.php?title=Gwyrrdzauber&oldid=7693] -->

[water of life]: ./alchemy.md#water-of-life
[wood]: ./resources.md#wood
[iron]: ./resources.md#iron
[stone]: ./resources.md#stone
[mallorn]: ./resources.md#mallorn