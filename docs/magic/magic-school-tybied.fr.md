# Sorts Tybied

Les sorts de l'École de magie **Tybied** sont décrits ci-dessous par ordre de niveau croissant.

## Magie analysieren

**Beschreibung**:  
Mit diesem Spruch kann der Magier versuchen, die Verzauberungen eines einzelnen angegebenen Objekts zu erkennen. Von allen Sprüchen, die seine eigenen Fähigkeiten nicht überschreiten, wird er einen Eindruck ihres Wirkens erhalten können. Bei stärkeren Sprüchen benötigt er ein wenig Glück für eine gelungene Analyse.  
**Art**: sort normal  
**Niveau** : 1  
**Rang**: 5  
**Composants** : 1 Aura X niveau
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST \[LEVEL n\] "Magie analysieren" ( REGION | UNIT &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\] | SCHIFF &lt;Schiff-Nr&gt; | BURG &lt;Gebäude-Nr&gt; )  

## Schleieraura

**Beschreibung**:  
Dieser Zauber wird die gesamte Ausrüstung der Zieleinheit für einige Zeit vor den Blicken anderer verschleiern. Der Zauber schützt nicht vor Dieben und Spionen.  
**Art**: sort normal  
**Niveau** : 1  
**Rang**: 5  
**Composants** : 1 Aura X niveau
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST \[LEVEL n\] "Schleieraura" &lt;Einheit-Nr&gt;  

## Wunderdoktor

**Beschreibung**:  
Wenn einem der Alchemist nicht weiterhelfen kann, geht man zu dem gelehrten Tybiedmagier. Seine Tränke und Tinkturen helfen gegen alles, was man sonst nicht bekommen kann. Ob nun die kryptische Formel unter dem Holzschuh des untreuen Ehemannes wirklich geholfen hat - nun, der des Lesens nicht mächtige Bauer wird es nie wissen. Dem Magier hilft es auf jeden Fall... beim Füllen seines Geldbeutels. 50 Silber pro Stufe lassen sich so in einer Woche verdienen.  
**Art**: sort normal  
**Niveau** : 1  
**Rang**: 5  
**Composants** : 1 Aura X niveau
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST \[LEVEL n\] "Wunderdoktor"  

## Schutz vor Magie

**Beschreibung**:  
Dieser Zauber legt ein antimagisches Feld um die Magier der Feinde und behindert ihre Zauber erheblich. Nur wenige werden die Kraft besitzen, das Feld zu durchdringen und ihren Truppen in der Schlacht zu helfen.  
**Art**: sort de pré-combat  
**Niveau** : 2  
**Rang**: 2  
**Composants** : 3 Aura X niveau
**Modificateurs**: *aucun*
**Syntaxe** : COMBATSPELL \[LEVEL n\] "Schutz vor Magie"  

## Beute Bewahren

**Beschreibung**:  
Dieser Zauber verhindert, dass ein Teil der sonst im Kampf zerstörten Gegenstände beschädigt wird. Die Verluste reduzieren sich um 5% pro Stufe des Zaubers bis zu einem Minimum von 25%.  
**Art**: sort de post-combat  
**Niveau** : 3  
**Rang**: 5  
**Composants** : 1 Aura X niveau
**Modificateurs**: *aucun*
**Syntaxe** : COMBATSPELL \[LEVEL n\] "Beute Bewahren"  

## Schutzzauber

**Beschreibung**:  
Dieser Zauber verstärkt die natürliche Widerstandskraft gegen Magie. Eine so geschützte Einheit ist auch gegen Kampfmagie weniger empfindlich. Pro Stufe reicht die Kraft des Magiers aus, um 5 Personen zu schützen.  
**Art**: sort normal  
**Niveau** : 3  
**Rang**: 2  
**Composants** : 5 Aura X niveau
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST \[LEVEL n\] "Schutzzauber" &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\]  

## Astraler Ausgang

**Beschreibung**:  
Der Magier konzentriert sich auf die Struktur der Realität und kann so die astrale Ebene verlassen. Er kann insgesamt (Stufe-3)\*15 GE durch das kurzzeitig entstehende Tor schicken. Ist der Magier erfahren genug, den Zauber auf Stufen von 11 oder mehr zu zaubern, kann er andere Einheiten auch gegen ihren Willen auf die andere Ebene zwingen.  
**Art**: sort normal  
**Niveau** : 4  
**Rang**: 7  
**Composants** : 2 Aura X niveau
**Modificateurs**: *aucun*
**Syntaxe** : CAST \[LEVEL n\] "Astraler Ausgang" &lt;x&gt; &lt;y&gt; &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\]  

## Astraler Weg

**Beschreibung**:  
Alte arkane Formeln ermöglichen es dem Magier, sich und andere in die astrale Ebene zu schicken. Der Magier kann (Stufe-3)\*15 GE durch das kurzzeitig entstehende Tor schicken. Ist der Magier erfahren genug, den Zauber auf Stufen von 11 oder mehr zu zaubern, kann er andere Einheiten auch gegen ihren Willen auf die andere Ebene zwingen.  
**Art**: sort normal  
**Niveau** : 4  
**Rang**: 7  
**Composants** : 2 Aura X niveau
**Modificateurs**: *aucun*
**Syntaxe** : CAST \[LEVEL n\] "Astraler Weg" &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\]  

## Astrale Schwächezone

**Beschreibung**:  
Mit diesem Zauber kann der Magier eine Zone der astralen Schwächung erzeugen, ein lokales Ungleichgewicht im Astralen Feld. Dieses Zone wird bestrebt sein, wieder in den Gleichgewichtszustand zu gelangen. Dazu wird sie jedem in dieser Region gesprochenen Zauber einen Teil seiner Stärke entziehen, die schwächeren gar ganz absorbieren.  
**Art**: sort normal  
**Niveau** : 5  
**Rang**: 2  
**Composants** : 3 Aura X niveau
**Modificateurs**: sort à distance  
**Syntaxe** : CAST \[REGION x y\] \[LEVEL n\] "Astrale Schwächezone"  

## Auratransfer

**Beschreibung**:  
Mit Hilfe dieses Zauber kann der Magier eigene Aura im Verhältnis 2:1 auf einen anderen Magier des gleichen Magiegebietes oder im Verhältnis 3:1 auf einen Magier eines anderen Magiegebietes übertragen.  
**Art**: sort normal  
**Niveau** : 5  
**Rang**: 1  
**Composants** : 1 Aura  
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST "Auratransfer" &lt;Einheit-Nr&gt; &lt;Aura&gt;  

## Magiefresser

**Beschreibung**:  
Dieser Zauber ermöglicht dem Magier, Verzauberungen einer Einheit, eines Schiffes, Gebäudes oder auch der Region aufzulösen.  
**Art**: sort normal  
**Niveau** : 5  
**Rang**: 2  
**Composants** : 4 Aura X niveau
**Modificateurs**: sort à distance, sort de bateau  
**Syntaxe** : CAST \[REGION x y\] \[LEVEL n\] "Magiefresser" ( REGION | UNIT &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\] | SCHIFF &lt;Schiff-Nr&gt; | BURG &lt;Gebäude-Nr&gt; )  

## Schockwelle

**Beschreibung**:  
Dieser Zauber läßt eine Welle aus purer Kraft über die gegnerischen Reihen hinwegfegen. Viele Kämpfer wird der Schock so benommen machen, daß sie für einen kurzen Moment nicht angreifen können.  
**Art**: sort de combat  
**Niveau** : 5  
**Rang**: 5  
**Composants** : 1 Aura X niveau
**Modificateurs**: *aucun*
**Syntaxe** : COMBATSPELL \[LEVEL n\] "Schockwelle"  

## Astraler Ruf

**Beschreibung**:  
Ein Magier, der sich in der astralen Ebene befindet, kann mit Hilfe dieses Zaubers andere Einheiten zu sich holen. Der Magier kann (Stufe-3)\*15 GE durch das kurzzeitig entstehende Tor schicken. Ist der Magier erfahren genug, den Zauber auf Stufen von 13 oder mehr zu zaubern, kann er andere Einheiten auch gegen ihren Willen auf die andere Ebene zwingen.  
**Art**: sort normal  
**Niveau** : 6  
**Rang**: 7  
**Composants** : 2 Aura X niveau
**Modificateurs**: *aucun*
**Syntaxe** : CAST \[LEVEL n\] "Astraler Ruf" &lt;x&gt; &lt;y&gt; &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\]  

## Erschaffe ein Amulett des wahren Sehens

**Beschreibung**:  
Der Spruch ermöglicht es einem Magier, ein Amulett des Wahren Sehens zu erschaffen. Das Amulett erlaubt es dem Träger, alle Einheiten, die durch einen Ring der Unsichtbarkeit geschützt sind, zu sehen. Einheiten allerdings, die sich mit ihrem Tarnungs-Talent verstecken, bleiben weiterhin unentdeckt.  
**Art**: sort normal  
**Niveau** : 6  
**Rang**: 5  
**Composants** : 50 Aura, 3000 Silber, 1 permanente Aura  
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST "Erschaffe ein Amulett des wahren Sehens"  

## Erschaffe einen Ring der Unsichtbarkeit

**Beschreibung**:  
Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer unsichtbaren Einheit muss jede Person einen Ring tragen.  
**Art**: sort normal  
**Niveau** : 6  
**Rang**: 5  
**Composants** : 50 Aura, 3000 Silber, 1 permanente Aura  
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST "Erschaffe einen Ring der Unsichtbarkeit"  

## Luftschiff

**Beschreibung**:  
Diese magischen Runen bringen ein Boot oder Langboot für eine Woche zum Fliegen. Damit kann dann auch Land überquert werden. Für die Farbe der Runen muss eine spezielle Tinte aus einem Windbeutel und einem Schneekristall angerührt werden.  
**Art**: sort normal  
**Niveau** : 6  
**Rang**: 5  
**Composants** : 10 Aura, 1 Windbeutel, 1 Schneekristall  
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST "Luftschiff" &lt;Schiff-Nr&gt;  

## Ruf der Realität

**Beschreibung**:  
Ein Magier, welcher sich in der materiellen Welt befindet, kann er mit Hilfe dieses Zaubers Einheiten aus der angrenzenden Astralwelt herbeiholen. Ist der Magier erfahren genug, den Zauber auf Stufen von 13 oder mehr zu zaubern, kann er andere Einheiten auch gegen ihren Willen in die materielle Welt zwingen.  
**Art**: sort normal  
**Niveau** : 6  
**Rang**: 7  
**Composants** : 2 Aura X niveau
**Modificateurs**: *aucun*
**Syntaxe** : CAST \[LEVEL n\] "Ruf der Realität" &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\]  

## Stehle Aura

**Beschreibung**:  
Mit Hilfe dieses Zaubers kann der Magier einem anderen Magier seine Aura gegen dessen Willen entziehen und sich selber zuführen.  
**Art**: sort normal  
**Niveau** : 6  
**Rang**: 3  
**Composants** : 2 Aura X niveau
**Modificateurs**: sort à distance  
**Syntaxe** : CAST \[REGION x y\] \[LEVEL n\] "Stehle Aura" &lt;Einheit-Nr&gt;  

## Erschaffe Antimagiekristall

**Beschreibung**:  
Mit Hilfe dieses Zauber entzieht der Magier einem Quarzkristall all seine magischen Energien. Der Kristall wird dann, wenn er zu feinem Staub zermahlen und verteilt wird, die beim Zaubern freigesetzten magischen Energien aufsaugen und die Kraft aller Zauber reduzieren, welche in der betreffenden Woche in der Region gezaubert werden.  
**Art**: sort normal  
**Niveau** : 7  
**Rang**: 5  
**Composants** : 50 Aura, 3000 Silber  
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST "Erschaffe Antimagiekristall"  

## Fluch brechen

**Beschreibung**:  
Dieser Zauber ermöglicht dem Magier, gezielt eine bestimmte Verzauberung einer Einheit, eines Schiffes, Gebäudes oder auch der Region aufzulösen.  
**Art**: sort normal  
**Niveau** : 7  
**Rang**: 3  
**Composants** : 3 Aura X niveau
**Modificateurs**: sort à distance, sort de bateau  
**Syntaxe** : CAST \[REGION x y\] \[LEVEL n\] "Fluch brechen" ( REGION | UNIT &lt;Einheit-Nr&gt; | SCHIFF &lt;Schiff-Nr&gt; | BURG &lt;Gebäude-Nr&gt; ) &lt;Zauber-ID&gt;  

## Mauern der Ewigkeit

**Beschreibung**:  
Mit dieser Formel bindet der Magier auf ewig die Kräfte der Erde in die Mauern des Gebäudes. Ein solchermaßen verzaubertes Gebäude ist gegen den Zahn der Zeit geschützt und benötigt keinen Unterhalt mehr.  
**Art**: sort normal  
**Niveau** : 7  
**Rang**: 5  
**Composants** : 50 Aura, 1 permanente Aura  
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST \[LEVEL n\] "Mauern der Ewigkeit" &lt;Gebäude-Nr&gt;  

## Runen des Schutzes

**Beschreibung**:  
Zeichnet man diese Runen auf die Wände eines Gebäudes oder auf die Planken eines Schiffes, so wird es schwerer durch Zauber zu beeinflussen sein. Jedes Ritual erhöht die Widerstandskraft des Gebäudes oder Schiffes gegen Verzauberung um 20%. Werden mehrere Schutzzauber übereinander gelegt, so addiert sich ihre Wirkung, doch ein hundertprozentiger Schutz läßt sich so nicht erreichen. Der Zauber hält mindestens drei Wochen an, je nach Talent des Magiers aber auch viel länger.  
**Art**: sort normal  
**Niveau** : 8  
**Rang**: 2  
**Composants** : 20 Aura  
**Modificateurs**: *aucun*
**Syntaxe** : CAST "Runen des Schutzes" ( SCHIFF &lt;Schiff-Nr&gt; | BURG &lt;Gebäude-Nr&gt; )  

## Schild des Fisches

**Beschreibung**:  
Dieser Zauber vermag dem Gegner ein geringfügig versetztes Bild der eigenen Truppen vorzuspiegeln, so wie der Fisch im Wasser auch nicht dort ist wo er zu sein scheint. Von jedem Treffer kann so die Hälfte des Schadens unschädlich abgeleitet werden. Doch hält der Schild nur einige Hundert Schwerthiebe aus, danach wird er sich auflösen. Je stärker der Magier, desto mehr Schaden hält der Schild aus.  
**Art**: sort de pré-combat  
**Niveau** : 8  
**Rang**: 2  
**Composants** : 4 Aura X niveau
**Modificateurs**: *aucun*
**Syntaxe** : COMBATSPELL \[LEVEL n\] "Schild des Fisches"  

## Beschleunigung

**Beschreibung**:  
Dieser Zauber beschleunigt einige Kämpfer auf der eigenen Seite so, dass sie während des gesamten Kampfes in einer Kampfrunde zweimal angreifen können.  
**Art**: sort de pré-combat  
**Niveau** : 9  
**Rang**: 5  
**Composants** : 5 Aura X niveau
**Modificateurs**: *aucun*
**Syntaxe** : COMBATSPELL \[LEVEL n\] "Beschleunigung"  

## Erschaffe einen Ring der Macht

**Beschreibung**:  
Dieses mächtige Ritual erschafft einen Ring der Macht. Ein Ring der Macht erhöht die Stärke jedes Zaubers, den sein Träger zaubert, als wäre der Magier eine Stufe besser.  
**Art**: sort normal  
**Niveau** : 9  
**Rang**: 5  
**Composants** : 100 Aura, 1 permanente Aura, 4000 Silber  
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST "Erschaffe einen Ring der Macht"  

## Blick in die Realität

**Beschreibung**:  
Der Magier kann mit Hilfe dieses Zaubers aus der Astral- in die materielle Ebene blicken und die Regionen und Einheiten genau erkennen.  
**Art**: sort normal  
**Niveau** : 10  
**Rang**: 5  
**Composants** : 40 Aura  
**Modificateurs**: *aucun*
**Syntaxe** : CAST "Blick in die Realität"  

## Erschaffe einen Beutel des Negativen Gewichts

**Beschreibung**:  
Dieser Beutel umschließt eine kleine Dimensionsfalte, in der bis zu 200 Gewichtseinheiten transportiert werden können, ohne dass sie auf das Traggewicht angerechnet werden. Pferde und andere Lebewesen sowie besonders sperrige Dinge (Wagen und Katapulte) können nicht in dem Beutel transportiert werden. Auch ist es nicht möglich, einen Zauberbeutel in einem anderen zu transportieren. Der Beutel selber wiegt 1 GE.  
**Art**: sort normal  
**Niveau** : 10  
**Rang**: 5  
**Composants** : 30 Aura, 1 permanente Aura, 5000 Silber  
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST "Erschaffe einen Beutel des Negativen Gewichts"  

## Zeitdehnung

**Beschreibung**:  
Diese praktische Anwendung des theoretischen Wissens um Raum und Zeit ermöglicht es, den Zeitfluß für einige Personen zu verändern. Auf diese Weise veränderte Personen bekommen für einige Wochen doppelt soviele Bewegungspunkte und doppelt soviele Angriffe pro Runde.  
**Art**: sort normal  
**Niveau** : 11  
**Rang**: 5  
**Composants** : 5 Aura X niveau
**Modificateurs**: sort de bateau  
**Syntaxe** : CAST \[LEVEL n\] "Zeitdehnung" &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\]  

## Rüstschild

**Beschreibung**:  
Diese vor dem Kampf zu zaubernde Ritual gibt den eigenen Truppen einen zusätzlichen Bonus auf ihre Rüstung. Jeder Treffer reduziert die Kraft des Zaubers, so dass der Schild sich irgendwann im Kampf auflösen wird.  
**Art**: sort de pré-combat  
**Niveau** : 12  
**Rang**: 2  
**Composants** : 4 Aura X niveau
**Modificateurs**: *aucun*
**Syntaxe** : COMBATSPELL \[LEVEL n\] "Rüstschild"  

## Vertrauten rufen

**Beschreibung**:  
Einem erfahrenen Magier wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Magier anschließen wird.  
**Art**: sort normal  
**Niveau** : 12  
**Rang**: 5  
**Composants** : 100 Aura, 5 permanente Aura  
**Modificateurs**: *aucun*
**Syntaxe** : CAST "Vertrauten rufen"  

## Belebtes Gestein

**Beschreibung**:  
Dieses kräftezehrende Ritual beschwört mit Hilfe einer Kugel aus konzentriertem Laen einen gewaltigen Erdelementar und bannt ihn in ein Gebäude. Dem Elementar kann dann befohlen werden, das Gebäude mitsamt aller Bewohner in eine Nachbarregion zu tragen. Die Stärke des beschworenen Elementars hängt vom Talent des Magiers ab: Der Elementar kann maximal \[Stufe-12\]\*250 Größeneinheiten große Gebäude versetzen. Das Gebäude wird diese Prozedur nicht unbeschädigt überstehen.  
**Art**: sort normal  
**Niveau** : 13  
**Rang**: 5  
**Composants** : 10 Aura \* Stufe, 1 permanente Aura, 5 Laen  
**Modificateurs**: *aucun*
**Syntaxe** : CAST \[LEVEL n\] "Belebtes Gestein" &lt;Gebäude-Nr&gt; &lt;Richtung&gt;  

## Störe Astrale Integrität

**Beschreibung**:  
Dieser Zauber bewirkt eine schwere Störung des Astralraums. Innerhalb eines astralen Radius von Stufe/5 Regionen werden alle Astralwesen, die dem Zauber nicht wiederstehen können, aus der astralen Ebene geschleudert. Der astrale Kontakt mit allen betroffenen Regionen ist für Stufe/3 Wochen gestört.  
**Art**: sort normal  
**Niveau** : 14  
**Rang**: 4  
**Composants** : 140 Aura  
**Modificateurs**: *aucun*
**Syntaxe** : CAST \[LEVEL n\] "Störe Astrale Integrität"  

## Opfere Kraft

**Beschreibung**:  
Mit Hilfe dieses Zaubers kann der Magier einen Teil seiner magischen Kraft permanent auf einen anderen Magier übertragen. Auf einen Tybied-Magier kann er die Hälfte der eingesetzten Kraft übertragen, auf einen Magier eines anderen Gebietes ein Drittel.  
**Art**: sort normal  
**Niveau** : 15  
**Rang**: 1  
**Composants** : 100 Aura  
**Modificateurs**: *aucun*
**Syntaxe** : CAST "Opfere Kraft" &lt;Einheit-Nr&gt; &lt;Aura&gt;  

<!-- From [https://wiki.eressea.de/index.php?title=Tybiedzauber&oldid=7486] -->
