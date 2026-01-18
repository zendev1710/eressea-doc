---
# cSpell:locale fr
alias: sorts-gwyrrd
---
# Sorts Gwyrrd

Les sorts de l'École de magie **Gwyrrd** sont décrits ci-dessous par ordre de niveau croissant.

## Steingolems

**Description** :  
Man befeuchte einen kluftfreien Block aus feinkristallinen Gestein mit einer Phiole des Lebenswassers bis dieses vollständig vom Gestein aufgesogen wurde. Sodann richte man seine Kraft auf die sich bildende feine Aura des Lebens und forme der ungebundenen Kraft ein Gehäuse. Je mehr Kraft der Magier investiert, desto mehr Golems können geschaffen werden, bevor die Aura sich verflüchtigt. Jeder Golem hat jede Runde eine Chance von 10 Prozent zu Staub zu zerfallen. Gibt man den Golems die Befehle MAKE BURG oder MAKE STRASSE, so werden pro Golem 4 Steine verbaut und der Golem löst sich auf.  
**Type** : sort normal  
**Niveau** : 1  
**Rang** : 4  
**Composants** : 2 Aura \* niveau, 1 Stein \* niveau, 1 Wasser des Lebens  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST \[LEVEL n\] "Erschaffe Steingolems"`  

## Segen der Erde

**Description** :  
Dieses Ernteritual verbessert die Erträge der arbeitenden Bauern in der Region um ein Silberstück. Je mehr Kraft der Druide investiert, desto länger wirkt der Zauber.  
**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST \[REGION x y\] \[LEVEL n\] "Segen der Erde"`  

## Viehheilung

**Description** :  
Die Fähigkeiten der Gwyrrd-Magier in der Viehzucht und Heilung sind bei den Bauern sehr begehrt. Gerade auf Märkten sind ihre Dienste häufig sehr gefragt. Manch einer mag auch sein Talent dazu nutzen, ein Tier für einen besseren Preis zu verkaufen. Pro Stufe kann der Magier so 50 Silber verdienen.  
**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST \[LEVEL n\] "Viehheilung"`  

## Eisengolems

**Description** :  
Je mehr Kraft der Magier investiert, desto mehr Golems können geschaffen werden. Jeder Golem hat jede Runde eine Chance von 15 Prozent zu Staub zu zerfallen. Gibt man den Golems den Befehl MAKE SCHWERT/BIHÄNDER oder MAKE SCHILD/KETTENHEMD/PLATTENPANZER, so werden pro Golem 4 Eisenbarren verbaut und der Golem löst sich auf.  
**Type** : sort normal  
**Niveau** : 2  
**Rang** : 4  
**Composants** : 2 Aura \* niveau, 1 Eisen \* niveau, 1 Wasser des Lebens  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST \[LEVEL n\] "Erschaffe Eisengolems"`  

## Hainzauber

**Description** :  
Wo sonst aus einem Stecken nur ein Baum sprießen konnte, so treibt nun jeder Ast Wurzeln.  
**Type** : sort normal  
**Niveau** : 2  
**Rang** : 5  
**Composants** : 4 Aura \* niveau, 1 Holz \* niveau, 1 Wasser des Lebens  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST \[REGION x y\] \[LEVEL n\] "Hainzauber"`  

## Bergwächter

**Description** :  
Erschafft einen Wächtergeist, der in Gletschern und Bergen Eisen- und Laenabbau durch nichtalliierte Parteien (HELP GUARD) verhindert, solange er die Region bewacht. Der Bergwächter ist an den Ort der Beschwörung gebunden.  
**Type** : sort normal  
**Niveau** : 3  
**Rang** : 5  
**Composants** : 3 Aura X niveau
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST \[REGION x y\] \[LEVEL n\] "Bergwächter"`  

## Firuns Fell

**Description** :  
Dieser Zauber ermöglicht es dem Magier Insekten auf magische Weise vor der lähmenden Kälte der Gletscher zu bewahren. Sie können Gletscher betreten und dort normal agieren. Der Spruch wirkt auf Stufe\*10 Insekten. Ein Ring der Macht erhöht die Menge der verzauberbaren Insekten zusätzlich um 10.  
**Type** : sort normal  
**Niveau** : 3  
**Rang** : 5  
**Composants** : 2 Aura X niveau
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST \[LEVEL n\] "Firuns Fell" &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\]`  

## Hagel

**Description** :  
Im Kampf ruft der Magier die Elementargeister der Kälte an und bindet sie an sich. Sodann kann er ihnen befehlen, den Gegner mit Hagelkörnern und Eisbrocken zuzusetzen.  
**Type** : sort de combat  
**Niveau** : 3  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL \[LEVEL n\] "Hagel"`  

## Rostregen

**Description** :  
Mit diesem Ritual wird eine dunkle Gewitterfront beschworen, die sich unheilverkündend über der Region auftürmt. Der magische Regen wird alles Eisenerz rosten lassen. Eisenwaffen und Rüstungen werden schartig und rostig. Die Zerstörungskraft des Regens ist von der investierten Kraft des Magiers abhängig. Für jede Stufe können bis zu 10 Gegenstände betroffen werden. Ein Ring der Macht verstärkt die Wirkung wie eine zusätzliche Stufe.  
**Type** : sort normal  
**Niveau** : 3  
**Rang** : 5  
**Composants** : 2 Aura X niveau
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST \[REGION x y\] \[LEVEL n\] "Rostregen" &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\]`  

## Magischer Pfad

**Description** :  
Durch Ausführung dieser Rituale ist der Magier in der Lage einen mächtigen Erdelementar zu beschwören. Solange dieser in den Boden gebannt ist, wird kein Regen die Wege aufweichen und kein Fluß Brücken zerstören können. Alle Reisende erhalten damit die gleichen Vorteile, die sonst nur ein ausgebautes gepflastertes Straßennetz bietet. Selbst Sümpfe und Gletscher können so verzaubert werden. Je mehr Kraft der Magier in den Bann legt, desto länger bleibt die Straße bestehen.  
**Type** : sort normal  
**Niveau** : 4  
**Rang** : 5  
**Composants** : 1 Aura \* niveau, 1 Stein, 1 Holz  
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST \[REGION x y\] \[LEVEL n\] "Magischer Pfad"`  

## Segne Mallornstecken

**Description** :  
Diese Ritual verstärkt die Wirkung des magischen Trankes um ein vielfaches. Wo sonst aus einem Stecken nur ein Baum sprießen konnte, so treibt nun jeder Ast Wurzeln.  
**Type** : sort normal  
**Niveau** : 4  
**Rang** : 5  
**Composants** : 6 Aura \* niveau, 1 Mallorn \* niveau, 1 Wasser des Lebens  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST \[REGION x y\] \[LEVEL n\] "Segne Mallornstecken"`  

## Wasserelementar

**Description** :  
Der Magier zwingt mit diesem Ritual die Elementargeister des Wassers in seinen Dienst und bringt sie dazu, das angegebene Schiff schneller durch das Wasser zu tragen. Zudem wird das Schiff nicht durch ungünstige Winde oder Strömungen beeinträchtigt.  
**Type** : sort normal  
**Niveau** : 4  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST \[LEVEL n\] "Beschwörung eines Wasserelementares" &lt;Schiff-Nr&gt;`  

## Windschild

**Description** :  
Die Anrufung der Elementargeister des Windes beschwört plötzliche Windböen, kleine Windhosen und Luftlöcher herauf, die die gegnerischen Schützen behindern werden.  
**Type** : sort de pré-combat  
**Niveau** : 4  
**Rang** : 5  
**Composants** : 2 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : COMBATSPELL \[LEVEL n\] "Windschild"`  

## Astralschutzgeister

**Description** :  
Dieses Ritual beschwört einige Elementargeister der Magie und schickt sie in die Reihen der feindlichen Magier. Diesen wird das Zaubern für die Dauer des Kampfes deutlich schwerer fallen.  
**Type** : sort de pré-combat  
**Niveau** : 5  
**Rang** : 2  
**Composants** : 5 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : COMBATSPELL \[LEVEL n\] "Astralschutzgeister"`  

## Erschaffe einen magischen Kräuterbeutel

**Description** :  
Der Druide nehme etwas präpariertes Leder, welches er in einem großen Ritual der Reinigung von allen unreinen Geistern befreie, und binde dann einige kleine Geister der Luft und des Wassers in das Material. Aus dem so vorbereiteten Leder fertige er nun ein kleines Beutelchen, welches in ihm aufbewahrte Kräuter besser zu konservieren vermag.  
**Type** : sort normal  
**Niveau** : 5  
**Rang** : 5  
**Composants** : 30 Aura, 1 permanente Aura, 1 Wasser des Lebens  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe einen magischen Kräuterbeutel"`  

## Heilung

**Description** :  
Nicht nur der Feldscher kann den Verwundeten einer Schlacht helfen. Druiden vermögen mittels einer Beschwörung der Elementargeister des Lebens Wunden zu schließen, gebrochene Knochen zu richten und selbst abgetrennte Glieder wieder zu regenerieren.  
**Type** : sort de post-combat  
**Niveau** : 5  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL \[LEVEL n\] "Heilung"`  

## Wirbelwind

**Description** :  
Diese Beschwörung öffnet ein Tor in die Ebene der Elementargeister des Windes. Sofort erheben sich in der Umgebung des Tors starke Winde oder gar Stürme und behindern alle Schützen einer Schlacht.  
**Type** : sort de pré-combat  
**Niveau** : 5  
**Rang** : 5  
**Composants** : 15 Aura  
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL \[LEVEL n\] "Wirbelwind"`  

## Erdelementar

**Description** :  
Der Druide beschwört mit diesem Ritual einen Elementargeist der Erde und bringt ihn dazu, die Erde erbeben zu lassen. Dieses Erdbeben wird alle Gebäude in der Region beschädigen.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 25 Aura, 2 Laen  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST \[REGION x y\] "Beschwöre einen Erdelementar"`  

## Erschaffe ein Amulett des wahren Sehens

**Description** :  
Der Spruch ermöglicht es einem Magier, ein Amulett des Wahren Sehens zu erschaffen. Das Amulett erlaubt es dem Träger, alle Einheiten, die durch einen Ring der Unsichtbarkeit geschützt sind, zu sehen. Einheiten allerdings, die sich mit ihrem Tarnungs-Talent verstecken, bleiben weiterhin unentdeckt.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 50 Aura, 3000 Silber, 1 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe ein Amulett des wahren Sehens"`  

## Erschaffe einen Ring der Unsichtbarkeit

**Description** :  
Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer unsichtbaren Einheit muss jede Person einen Ring tragen.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 50 Aura, 3000 Silber, 1 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe einen Ring der Unsichtbarkeit"`  

## Meditation

**Description** :  
Mit Hilfe dieses Zaubers kann der Magier eigene Aura im Verhältnis 2:1 auf einen anderen Magier des gleichen Magiegebietes übertragen.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 1  
**Composants** : 2 Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Meditation" &lt;Einheit-Nr&gt; &lt;Aura&gt;`  

## Sturmelementar

**Description** :  
Die Beschwörung von Elementargeistern der Stürme ist ein uraltes Ritual. Der Druide bannt die Elementare in die Segel der Schiffe, wo sie helfen, das Schiff mit hoher Geschwindigkeit über die Wellen zu tragen. Je mehr Kraft der Druide in den Zauber investiert, desto größer ist die Zahl der Elementargeister, die sich bannen lassen. Für jedes Schiff wird ein Elementargeist benötigt.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 6 Aura X niveau
**Modificateurs** : Seezauber, sort de bateau  
**Syntaxe** : `CAST \[LEVEL n\] "Beschwöre einen Sturmelementar" &lt;Schiff-Nr&gt; \[&lt;Schiff-Nr&gt; ...\]`  

## Heimstein

**Description** :  
Mit dieser Formel bindet der Magier auf ewig die Kräfte der Erde in die Mauern der Burg, in der er sich gerade befindet. Weder magisch noch mit schwerem Geschütz können derartig gestärkte Mauern zerstört werden, und auch das Alter setzt ihnen weniger zu. Das Gebäude bietet sodann auch einen besseren Schutz gegen Angriffe mit dem Schwert wie mit Magie.  
**Type** : sort normal  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 50 Aura, 1 permanente Aura  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Heimstein"`  

## Wolfsgeheul

**Description** :  
Nicht wenige Druiden freunden sich im Laufe ihres Lebens in der Natur mit den ältesten Freunden der großen Völker an. Sie erlernen, mit einem einzigen heulenden Ruf viele ihrer Freunde herbeizurufen, um ihnen im Kampf beizustehen.  
**Type** : sort de pré-combat  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 2 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : COMBATSPELL \[LEVEL n\] "Wolfsgeheul"`  

## Blick des Basilisken

**Description** :  
Dieser schwierige, aber effektive sort de combat benutzt die Elementargeister des Steins, um eine Reihe von Gegnern für die Dauer des Kampfes in Stein zu verwandeln. Die betroffenen Personen werden nicht mehr kämpfen, können jedoch auch nicht verwundet werden.  
**Type** : sort de combat  
**Niveau** : 8  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL \[LEVEL n\] "Blick des Basilisken"`  

## Geister bannen

**Description** :  
Wie die alten Lehren der Druiden berichten, besteht das, was die normalen Wesen Magie nennen, aus Elementargeistern. Der Magier beschwört und bannt diese in eine Form, um den gewünschten Effekt zu erzielen. Dieses Ritual nun vermag es, in diese Welt gerufene Elementargeister zu vertreiben, um so ein Objekt von Magie zu befreien.  
**Type** : sort normal  
**Niveau** : 8  
**Rang** : 2  
**Composants** : 6 Aura X niveau
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST \[REGION x y\] \[LEVEL n\] "Geister bannen" ( REGION | UNIT &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\] | SCHIFF &lt;Schiff-Nr&gt; | BURG &lt;Gebäude-Nr&gt; )`  

## Starkes Tor und feste Mauer

**Description** :  
Mit dieser Formel bindet der Magier zu Beginn eines Kampfes einige Elementargeister des Fels in die Mauern des Gebäudes, in dem er sich gerade befindet. Das Gebäude bietet sodann einen besseren Schutz gegen Angriffe mit dem Schwert wie mit Magie.  
**Type** : sort de pré-combat  
**Niveau** : 8  
**Rang** : 5  
**Composants** : 2 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL \[LEVEL n\] "Starkes Tor und feste Mauer"`  

## Heiliger Boden

**Description** :  
Dieses Ritual beschwört verschiedene Naturgeister in den Boden der Region, welche diese fortan bewachen. In einer so gesegneten Region werden niemals wieder die Toten ihre Gräber verlassen, und anderswo entstandene Untote werden sie wann immer möglich meiden.  
**Type** : sort normal  
**Niveau** : 9  
**Rang** : 5  
**Composants** : 80 Aura, 3 permanente Aura  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Heiliger Boden"`  

## Sog des Lebens

**Description** :  
Ein Druide, den es in die Welt der Geister verschlagen hat, kann mit Hilfe dieses Zaubers Stufe\*5 Gewichtseinheiten in einen Wald auf der materiellen Welt zurückschicken.  
**Type** : sort normal  
**Niveau** : 9  
**Rang** : 7  
**Composants** : 2 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `CAST \[LEVEL n\] "Sog des Lebens" &lt;x&gt; &lt;y&gt; &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\]`  

## Weg der Bäume

**Description** :  
Große Macht liegt in Orten, an denen das Leben pulsiert. Der Druide kann diese Kraft sammeln und so ein Tor in die Welt der Geistwesen erschaffen. Der Druide kann dann Stufe\*5 Gewichtseinheiten durch das Tor entsenden.  
**Type** : sort normal  
**Niveau** : 9  
**Rang** : 7  
**Composants** : 3 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `CAST \[LEVEL n\] "Weg der Bäume" &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\]`  

## Erwecke Ents

**Description** :  
Mit Hilfe dieses Zaubers weckt der Druide die in den Wälder der Region schlummernden Ents aus ihrem äonenlangen Schlaf. Die wilden Baumwesen werden sich ihm anschließen und ihm beistehen, jedoch nach einiger Zeit wieder in Schlummer verfallen.  
**Type** : sort normal  
**Niveau** : 10  
**Rang** : 5  
**Composants** : 6 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `CAST \[LEVEL n\] "Erwecke Ents"`  

## Vertrauten rufen

**Description** :  
Einem erfahrenen Druidem wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Druiden anschließen wird.  
**Type** : sort normal  
**Niveau** : 10  
**Rang** : 5  
**Composants** : 100 Aura, 5 permanente Aura  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Vertrauten rufen"`  

## Segne Steinkreis

**Description** :  
Dieses Ritual segnet einen Steinkreis, der zuvor aus Steinen und etwas Holz gebaut werden muss. Die Segnung des Druiden macht aus dem Kreis eine mächtige Stätte magischen Wirkens, die Schutz vor Magie und erhöhte Aura- Regeneration bewirkt. Man sagt, Jungfrauen seien in der Umgebung von Steinkreisen seltsame Wesen begegnet.  
**Type** : sort normal  
**Niveau** : 11  
**Rang** : 5  
**Composants** : 350 Aura, 5 permanente Aura  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Segne Steinkreis" &lt;Gebäude-Nr&gt;`  

## Rindenhaut

**Description** :  
Dieses vor dem Kampf zu zaubernde Ritual gibt den eigenen Truppen einen zusätzlichen Bonus auf ihre Rüstung. Jeder Treffer reduziert die Kraft des Zaubers, so dass der Schild sich irgendwann im Kampf auflösen wird.  
**Type** : sort de pré-combat  
**Niveau** : 12  
**Rang** : 2  
**Composants** : 4 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL \[LEVEL n\] "Rindenhaut"`  

## Hitzeelementar

**Description** :  
Dieses Ritual beschwört wütende Elementargeister der Hitze. Eine Dürre sucht das Land heim. Bäume verdorren, Tiere verenden, und die Ernte fällt aus. Für Tagelöhner gibt es kaum noch Arbeit in der Landwirtschaft zu finden.  
**Type** : sort normal  
**Niveau** : 13  
**Rang** : 5  
**Composants** : 600 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST \[REGION x y\] "Beschwörung eines Hitzeelementar"`  

## Mahlstrom

**Description** :  
Dieses Ritual beschwört einen großen Wasserelementar aus den Tiefen des Ozeans. Der Elementar erzeugt einen gewaltigen Strudel, einen Mahlstrom, welcher alle Schiffe, die ihn passieren, schwer beschädigen kann.  
**Type** : sort normal  
**Niveau** : 15  
**Rang** : 5  
**Composants** : 200 Aura, 1 Seeschlangenkopf  
**Modificateurs** : Seezauber, sort de bateau  
**Syntaxe** : `CAST "Mahlstrom"`  

## Wurzeln der Magie

**Description** :  
Mit Hilfe dieses aufwändigen Rituals läßt der Druide einen Teil seiner Kraft dauerhaft in den Boden und die Wälder der Region fliessen. Dadurch wird das Gleichgewicht der Natur in der Region für immer verändert, und in Zukunft werden nur noch die anspruchsvollen, aber kräftigen Mallorngewächse in der Region gedeihen.  
**Type** : sort normal  
**Niveau** : 16  
**Rang** : 5  
**Composants** : 250 Aura, 10 permanente Aura, 1 pot de bave de crapaud  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST \[REGION x y\] "Wurzeln der Magie"`  

## Tor in die Ebene der Hitze

**Description** :  
Dieses mächtige Ritual öffnet ein Tor in die Elementarebene der Hitze. Eine grosse Dürre kommt über das Land. Bauern, Tiere und Pflanzen der Region kämpfen um das nackte Überleben, aber eine solche Dürre überlebt wohl nur die Hälfte aller Lebewesen. Der Landstrich kann über Jahre hinaus von den Folgen einer solchen Dürre betroffen sein.  
**Type** : sort normal  
**Niveau** : 17  
**Rang** : 5  
**Composants** : 800 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST \[REGION x y\] "Tor in die Ebene der Hitze"`  

<!-- From [https://wiki.eressea.de/index.php?title=Gwyrrdzauber&oldid=7693] -->
