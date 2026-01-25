---
# cSpell:locale en
alias: illaun-spells
---
# Illaun spells

## Level 1 spells

### Shadow Knights

:   This spell can give the enemy a slightly different image of their own troops.  
    The Shadow Knights have no effective attack and being wounded in battle will destroy them instantly.

| Sc. | Components | Lvl |   Type | Rank | Ship | Dist. |
|:---:|------------|----:|-------:|:----:|:-----|:------|
|  I  | T auras    |   1 | Pre-c. |  4   |      |       |

`COMBATSPELL [LEVEL n] "Shadow Knights"`  

### Dream

:   The magician sends the target of the spell a dream.

| Sc. | Components | Lvl |   Type | Rank | Ship               | Dist. |
|:---:|------------|----:|-------:|:----:|:-------------------|:------|
|  I  | T auras    |   1 | Normal |  5   | :heavy_check_mark: |       |

`CAST [LEVEL n] Dream <unit-id>`  

### Wahrsagen

**Beschreibung**:  
Niemand kann so gut die Träume deuten wie ein Magier des Illaun. Auch die Kunst der Wahrsagerei, des Kartenlegens und des Handlesens sind ihm geläufig. Dafür zahlen ihm die Bauern 50 Silber pro Stufe.  
**Art**: Normaler Zauber  
**Level**: 1  
**Rank**: 5  
**Components**: 1 Aura \* Stufe  
**Modifikationen**: Schiffszauber  
**Syntax**: CAST \[LEVEL n\] "Wahrsagen"  

## Level 2 spells

### Grauen der Schlacht

**Beschreibung**:  
Der Traumweber beschwört vor dem Kampf grauenerregende Trugbilder herauf, die viele Gegner in Panik versetzen. Die Betroffenen werden versuchen, vor den Trugbildern zu fliehen.  
**Art**: Präkampfzauber  
**Level**: 2  
**Rank**: 5  
**Components**: 1 Aura \* Stufe  
**Modifikationen**:  
**Syntax**: COMBATSPELL \[LEVEL n\] "Grauen der Schlacht"  

### Seelenfrieden

**Beschreibung**:  
Dieses magische Ritual beruhigt die gequälten Seelen der gewaltsam zu Tode gekommenen und ermöglicht es ihnen so, ihre letzte Reise in die Anderlande zu beginnen. Je Stufe des Zaubers werden ungefähr 50 Seelen ihre Ruhe finden. Der Zauber vermag nicht, bereits wieder auferstandene lebende Tote zu erlösen, da deren Bindung an diese Welt zu stark ist.  
**Art**: Normaler Zauber  
**Level**: 2  
**Rank**: 5  
**Components**: 3 Aura \* Stufe, 1 Wasser des Lebens  
**Modifikationen**:  
**Syntax**: CAST \[LEVEL n\] "Seelenfrieden"  

## Level 3 spells

### Gestaltwandlung

**Beschreibung**:  
Mit Hilfe dieses arkanen Rituals vermag der Traumweber die wahre Gestalt einer Gruppe zu verschleiern. Unbedarften Beobachtern erscheint sie dann als einer anderen Rasse zugehörig.  
**Art**: Normaler Zauber  
**Level**: 3  
**Rank**: 5  
**Components**: 1 Aura \* Stufe  
**Modifikationen**:  
**Syntax**: CAST \[LEVEL n\] "Gestaltwandlung" &lt;Einheit-Nr&gt; &lt;Rasse&gt;  

### Traum der Magie

**Beschreibung**:  
Mit Hilfe dieses Zaubers kann der Traumweber eigene Aura im Verhältnis 2:1 auf einen anderen Traumweber übertragen.  
**Art**: Normaler Zauber  
**Level**: 3  
**Rank**: 1  
**Components**: 2 Aura  
**Modifikationen**: Schiffszauber  
**Syntax**: CAST "Traum der Magie" &lt;Einheit-Nr&gt; &lt;Aura&gt;  

### Traumschlößchen

**Beschreibung**:  
Mit Hilfe dieses Zaubers kann der Traumweber die Illusion eines beliebigen Gebäudes erzeugen. Die Illusion kann betreten werden, ist aber ansonsten funktionslos und benötigt auch keinen Unterhalt. Sie wird einige Wochen bestehen bleiben.  
**Art**: Normaler Zauber  
**Level**: 3  
**Rank**: 5  
**Components**: 3 Aura  
**Modifikationen**:  
**Syntax**: CAST "Traumschlößchen" &lt;Gebäudetyp&gt;  

## Level 4 spells

### Schwere Glieder

**Beschreibung**:  
Dieser Kampfzauber führt dazu, dass einige Gegner im Kampf unter schwerer Müdigkeit leiden. Die Soldaten verschlafen manchmal ihren Angriff und verteidigen sich schlechter.  
**Art**: Präkampfzauber  
**Level**: 4  
**Rank**: 5  
**Components**: 4 Aura \* Stufe  
**Modifikationen**:  
**Syntax**: COMBATSPELL \[LEVEL n\] "Schwere Glieder"  

### Traumlesen

**Beschreibung**:  
Dieser Zauber ermöglicht es dem Traumweber, in die Träume einer Einheit einzudringen und so einen Bericht über die Umgebung zu erhalten.  
**Art**: Normaler Zauber  
**Level**: 4  
**Rank**: 5  
**Components**: 8 Aura  
**Modifikationen**: Fernzauber  
**Syntax**: CAST \[REGION x y\] "Traumlesen" &lt;Einheit-Nr&gt;  

## Level 5 spells

### Traumbilder analysieren

**Beschreibung**:  
Mit diesem Spruch kann der Traumweber versuchen, die Verzauberungen einer einzelnen Einheit zu erkennen. Von allen Sprüchen, die seine eigenen Fähigkeiten nicht überschreiten, wird er einen Eindruck ihres Wirkens erhalten können. Bei stärkeren Sprüchen benötigt er ein wenig Glück für eine gelungene Analyse.  
**Art**: Normaler Zauber  
**Level**: 5  
**Rank**: 5  
**Components**: 25 Aura  
**Modifikationen**: Schiffszauber  
**Syntax**: CAST "Traumbilder analysieren" &lt;Einheit-Nr&gt;  

### Wiederbelebung

**Beschreibung**:  
Stirbt ein Krieger im Kampf so macht sich seine Seele auf die lange Wanderung zu den Sternen. Mit Hilfe eines Rituals kann ein Traumweber versuchen, die Seele wieder einzufangen und in den Körper des Verstorbenen zurückzubringen. Zwar heilt der Zauber keine körperlichen Verwundungen, doch ein Behandelter wird den Kampf überleben.  
**Art**: Postkampfzauber  
**Level**: 5  
**Rank**: 4  
**Components**: 1 Aura \* Stufe  
**Modifikationen**:  
**Syntax**: COMBATSPELL \[LEVEL n\] "Wiederbelebung"  

## Level 6 spells

### Erschaffe ein Amulett des wahren Sehens

**Beschreibung**:  
Der Spruch ermöglicht es einem Magier, ein Amulett des Wahren Sehens zu erschaffen. Das Amulett erlaubt es dem Träger, alle Einheiten, die durch einen Ring der Unsichtbarkeit geschützt sind, zu sehen. Einheiten allerdings, die sich mit ihrem Tarnungs-Talent verstecken, bleiben weiterhin unentdeckt.  
**Art**: Normaler Zauber  
**Level**: 6  
**Rank**: 5  
**Components**: 50 Aura, 3000 Silber, 1 permanente Aura  
**Modifikationen**: Schiffszauber  
**Syntax**: CAST "Erschaffe ein Amulett des wahren Sehens"  

### Erschaffe einen Ring der Unsichtbarkeit

**Beschreibung**:  
Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer unsichtbaren Einheit muss jede Person einen Ring tragen.  
**Art**: Normaler Zauber  
**Level**: 6  
**Rank**: 5  
**Components**: 50 Aura, 3000 Silber, 1 permanente Aura  
**Modifikationen**: Schiffszauber  
**Syntax**: CAST "Erschaffe einen Ring der Unsichtbarkeit"  

### Schlechter Schlaf

**Beschreibung**:  
Dieser Zauber führt in der betroffenen Region für einige Wochen zu Schlaflosigkeit und Unruhe. Den Betroffenen fällt das Lernen deutlich schwerer.  
**Art**: Normaler Zauber  
**Level**: 6  
**Rank**: 5  
**Components**: 18 Aura  
**Modifikationen**: Fernzauber  
**Syntax**: CAST \[REGION x y\] "Schlechter Schlaf"  

## Level 7 spells

### Schlaf

**Beschreibung**:  
Dieser Zauber läßt einige feindliche Kämpfer einschlafen. Schlafende Kämpfer greifen nicht an und verteidigen sich schlechter, sie wachen jedoch auf, sobald sie im Kampf getroffen werden.  
**Art**: Kampfzauber  
**Level**: 7  
**Rank**: 5  
**Components**: 1 Aura \* Stufe  
**Modifikationen**:  
**Syntax**: COMBATSPELL \[LEVEL n\] "Schlaf"  

### Traumdeuten

**Beschreibung**:  
Mit diesem Zauber dringt der Traumweber in die Gedanken und Traumwelt seines Opfers ein und kann so seine intimsten Geheimnisse ausspähen. Seine Fähigkeiten, seinen Besitz und seine Parteizugehörigkeit wird nicht länger ungewiss sein.  
**Art**: Normaler Zauber  
**Level**: 7  
**Rank**: 5  
**Components**: 20 Aura  
**Modifikationen**:  
**Syntax**: CAST "Traumdeuten" &lt;Einheit-Nr&gt;  

## Level 8 spells

### Schöne Träume

**Beschreibung**:  
Dieser Zauber ermöglicht es dem Traumweber, den Schlaf aller aliierten Einheiten in der Region so zu beeinflussen, dass sie für einige Zeit einen Bonus in allen Talenten bekommen.  
**Art**: Normaler Zauber  
**Level**: 8  
**Rank**: 5  
**Components**: 80 Aura  
**Modifikationen**: Fernzauber  
**Syntax**: CAST \[REGION x y\] "Schöne Träume"  

### Traumbilder entwirren

**Beschreibung**:  
Dieser Zauber ermöglicht es dem Traumweber die natürlichen und aufgezwungenen Traumbilder einer Person, eines Gebäudes, Schiffes oder einer Region zu unterscheiden und diese zu entwirren.  
**Art**: Normaler Zauber  
**Level**: 8  
**Rank**: 2  
**Components**: 6 Aura \* Stufe  
**Modifikationen**: Fernzauber, Schiffszauber  
**Syntax**: CAST \[REGION x y\] \[LEVEL n\] "Traumbilder entwirren" ( REGION | UNIT &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\] | SCHIFF &lt;Schiff-Nr&gt; | BURG &lt;Gebäude-Nr&gt; )  

## Level 9 spell

### Vertrauten rufen

**Beschreibung**:  
Einem erfahrenen Magier wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Magier anschließen wird.  
**Art**: Normaler Zauber  
**Level**: 9  
**Rank**: 5  
**Components**: 100 Aura, 5 permanente Aura  
**Modifikationen**:  
**Syntax**: CAST "Vertrauten rufen"  

## Level 10 spell

### Schlechte Träume

**Beschreibung**:  
Dieser Zauber ermöglicht es dem Träumer, den Schlaf aller nichtaliierten Einheiten (HELP GUARD) in der Region so stark zu stören, das sie vorübergehend einen Teil ihrer Erinnerungen verlieren.  
**Art**: Normaler Zauber  
**Level**: 10  
**Rank**: 5  
**Components**: 90 Aura  
**Modifikationen**: Fernzauber  
**Syntax**: CAST \[REGION x y\] "Schlechte Träume"  

## Level 11 spell

### Tod des Geistes

**Beschreibung**:  
Mit diesem Zauber greift der Magier direkt den Geist seiner Gegner an. Ein Schlag aus astraler und elektrischer Energie trifft die Gegner, wird die Magieresistenz durchbrochen, verliert ein Opfer permanent einen Teil seiner Erinnerungen. Wird es zu oft ein Opfer dieses Zaubers kann es daran sterben.  
**Art**: Präkampfzauber  
**Level**: 11  
**Rank**: 5  
**Components**: 2 Aura \* Stufe  
**Modifikationen**:  
**Syntax**: COMBATSPELL \[LEVEL n\] "Tod des Geistes"  

## Level 12 spell

### Süße Träume

**Beschreibung**:  
Dieser Zauber - dessen Anwendung in den meisten Kulturen streng verboten ist - löst im Opfer ein unkontrollierbares Verlangen nach körperlicher Liebe aus. Die betroffenen Personen werden sich Hals über Kopf in ein Liebesabenteuer stürzen, zu blind vor Verlangen, um an etwas anderes zu denken. Meistens bereuen sie es einige Wochen später...  
**Art**: Normaler Zauber  
**Level**: 12  
**Rank**: 5  
**Components**: 5 Aura \* Stufe  
**Modifikationen**:  
**Syntax**: CAST \[LEVEL n\] "Süße Träume" &lt;Einheit-Nr&gt; \[&lt;Einheit-Nr&gt; ...\]  

## Level 13 spell

### Erschaffe eine Sphäre der Unsichtbarkeit

**Beschreibung**:  
Mit diesem Spruch kann der Zauberer eine Sphäre der Unsichtbarkeit erschaffen. Die Späre macht ihren Träger sowie neunundneunzig weitere Personen in derselben Einheit unsichtbar.  
**Art**: Normaler Zauber  
**Level**: 13  
**Rank**: 5  
**Components**: 150 Aura, 30000 Silber, 3 permanente Aura  
**Modifikationen**: Schiffszauber  
**Syntax**: CAST "Erschaffe eine Sphäre der Unsichtbarkeit"  

## Level 14 spell

### Erschaffe ein Traumauge

**Beschreibung**:  
Ein mit diesem Zauber belegtes Drachenauge, welches zum Abendmahle verzehrt wird, erlaubt es dem Benutzer, in die Träume einer anderen Person einzudringen und diese zu lesen. Lange Zeit wurde eine solche Fähigkeit für nutzlos erachtet, bis die ehemalige waldelfische Magistra für Kampfmagie, Liarana Sonnentau von der Akademie Thall, eine besondere Anwendung vorstellte: Feldherren träumen vor großen Kämpfen oft unruhig und verraten im Traum ihre Pläne. Dies kann dem Anwender einen großen Vorteil im kommenden Kampf geben. Aber Vorsicht: Die Interpretation von Träumen ist eine schwierige Angelegenheit.  
**Art**: Normaler Zauber  
**Level**: 14  
**Rank**: 5  
**Components**: 1 Drachenkopf, 5 permanente Aura  
**Modifikationen**: Schiffszauber  
**Syntax**: CAST "Erschaffe ein Traumauge"  

<!-- From [https://wiki.eressea.de/index.php?title=Illaunzauber&oldid=7014] -->
