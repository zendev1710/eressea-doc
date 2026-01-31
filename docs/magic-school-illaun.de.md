---
# cSpell:locale de
alias: illaunzauber
---
# Illaunzauber

## Stufe 1

### Schattenritter

:   Dieser Zauber vermag dem Gegner ein 
    Die Schattenritter haben keinen effeztes Bild der eigenen Truppen vorzuspiegeln. Die Schattenritter haben keinen effektiven Angriff und Verwundungen im Kampf zerstören sie sofort.  


| Komponenten | Stufe |  Art   | 
|:-----------:|:-----:|:------:|:
|   T aura    |   1   | Prä-k. | 

`KAMPFZAUBER [STUFE n] Schattenritter`  

### Traumsenden

:   Der Zauberer sendet dem Ziel des Spruches einen Traum.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
|   T aura    |   1   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE [STUFE n] Traumsenden <Einheit-Nr>`  

### Wahrsagen

:   Niemand kann so gut die Träume deuten wie ein Magier des Illaun.  
    Auch die Kunst der Wahrsagerei, des Kartenlegens und des Handlesens sind ihm geläufig.  
    Dafür zahlen ihm die Bauern 50 Silber pro Stufe.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
|   T aura    |   1   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE [STUFE n] Wahrsagen`  

## Stufe 2

### Grauen der Schlacht

:   Der Traumweber beschwört vor dem Kampf grauenerregende Trugbilder herauf, die viele Gegner in Panik versetzen.  
    Die Betroffenen werden versuchen, vor den Trugbildern zu fliehen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
|   T aura    |   2   | Prä-k. |  5   |        |       |

`KAMPFZAUBER [STUFE n] 'Grauen der Schlacht'`  

### Seelenfrieden

:   Dieses magische Ritual beruhigt die gequälten Seelen der gewaltsam zu Tode gekommenen und ermöglicht es ihnen so, ihre letzte Reise in die Anderlande zu beginnen.  
    Je Stufe des Zaubers werden ungefähr 50 Seelen ihre Ruhe finden.  
    Der Zauber vermag nicht, bereits wieder auferstandene lebende Tote zu erlösen, da deren Bindung an diese Welt zu stark ist.  

|            Komponenten            | Stufe |  Art   | Rang | Schiff | Fern. |
|:---------------------------------:|:-----:|:------:|:----:|:------:|:------|
| 3 x T aura, 1 [wasser des lebens] |   2   | Normal |  5   |        |       |

`ZAUBERE [STUFE n] Seelenfrieden`  

## Stufe 3

### Gestaltwandlung

:   Mit Hilfe dieses arkanen Rituals vermag der Traumweber die wahre Gestalt einer Gruppe zu verschleiern.  
    Unbedarften Beobachtern erscheint sie dann als einer anderen Rasse zugehörig.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
|   T aura    |   3   | Normal |  5   |        |       |

`ZAUBERE [STUFE n] Gestaltwandlung <Einheit-Nr> <Rasse>`  

### Traum der Magie

:   Mit Hilfe dieses Zaubers kann der Traumweber eigene Aura im Verhältnis 2:1 auf einen anderen Traumweber übertragen.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
|   2 aura    |   3   | Normal |  1   | :material-check:{ .success } |       |

`ZAUBERE 'Traum der Magie' <Einheit-Nr> <Aura>`  

### Traumschlößchen

:   Mit Hilfe dieses Zaubers kann der Traumweber die Illusion eines beliebigen Gebäudes erzeugen.  
    Die Illusion kann betreten werden, ist aber ansonsten funktionslos und benötigt auch keinen Unterhalt.  
    Sie wird einige Wochen bestehen bleiben.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
|   3 aura    |   3   | Normal |  5   |        |       |

`ZAUBERE Traumschlößchen <Gebäudetyp>`  

## Stufe 4

### Schwere Glieder

:   Dieser Kampfzauber führt dazu, dass einige Gegner im Kampf unter schwerer Müdigkeit leiden.  
    Die Soldaten verschlafen manchmal ihren Angriff und verteidigen sich schlechter.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 4 x T aura  |   4   | Prä-k. |  5   |        |       |

`KAMPFZAUBER [STUFE n] 'Schwere Glieder'`  

### Traumlesen

:   Dieser Zauber ermöglicht es dem Traumweber, in die Träume einer Einheit einzudringen und so einen Bericht über die Umgebung zu erhalten.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern.                        |
|:-----------:|:-----:|:------:|:----:|:------:|:-----------------------------|
|   8 aura    |   4   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] Traumlesen <Einheit-Nr>`  

## Stufe 5

### Traumbilder analysieren

:   Mit diesem Spruch kann der Traumweber versuchen, die Verzauberungen einer einzelnen Einheit zu erkennen.  
    Von allen Sprüchen, die seine eigenen Fähigkeiten nicht überschreiten, wird er einen Eindruck ihres Wirkens erhalten können.  
    Bei stärkeren Sprüchen benötigt er ein wenig Glück für eine gelungene Analyse.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:------|
|   25 aura   |   5   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE 'Traumbilder analysieren' <Einheit-Nr>`  

### Wiederbelebung

:   Stirbt ein Krieger im Kampf so macht sich seine Seele auf die lange Wanderung zu den Sternen.  
    Mit Hilfe eines Rituals kann ein Traumweber versuchen, die Seele wieder einzufangen und in den Körper des Verstorbenen zurückzubringen.  
    Zwar heilt der Zauber keine körperlichen Verwundungen, doch ein Behandelter wird den Kampf überleben.  

| Komponenten | Stufe |   Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:-------:|:----:|:------:|:------|
|   T aura    |   5   | Post-k. |  4   |        |       |

`KAMPFZAUBER [STUFE n] Wiederbelebung`  

## Stufe 6

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

### Schlechter Schlaf

:   Dieser Zauber führt in der betroffenen Region für einige Wochen zu Schlaflosigkeit und Unruhe.  
    Den Betroffenen fällt das Lernen deutlich schwerer.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern.                        |
|:-----------:|:-----:|:------:|:----:|:------:|:-----------------------------|
|   18 aura   |   6   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] 'Schlechter Schlaf'`  

## Stufe 7

### Schlaf

:   Dieser Zauber läßt einige feindliche Kämpfer einschlafen.  
    Schlafende Kämpfer greifen nicht an und verteidigen sich schlechter, sie wachen jedoch auf, sobald sie im Kampf getroffen werden.  

| Komponenten | Stufe |  Art  | Rang | Schiff | Fern. |
|:-----------:|:-----:|:-----:|:----:|:------:|:------|
|   T aura    |   7   | Kampf |  5   |        |       |

`KAMPFZAUBER [STUFE n] Schlaf`  

### Traumdeuten

:   Mit diesem Zauber dringt der Traumweber in die Gedanken und Traumwelt seines Opfers ein und kann so seine intimsten Geheimnisse ausspähen.  
    Seine Fähigkeiten, seinen Besitz und seine Parteizugehörigkeit wird nicht länger ungewiss sein.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
|   20 aura   |   7   | Normal |  5   |        |       |

`ZAUBERE Traumdeuten <Einheit-Nr>`  

## Stufe 8

### Schöne Träume

:   Dieser Zauber ermöglicht es dem Traumweber, den Schlaf aller aliierten Einheiten in der Region so zu beeinflussen, dass sie für einige Zeit einen Bonus in allen Talenten bekommen.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern.                        |
|:-----------:|:-----:|:------:|:----:|:------:|:-----------------------------|
|   80 aura   |   8   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] 'Schöne Träume'`  

### Traumbilder entwirren

:   Dieser Zauber ermöglicht es dem Traumweber die natürlichen und aufgezwungenen Traumbilder einer Person, eines Gebäudes, Schiffes oder einer Region zu unterscheiden und diese zu entwirren.  

| Komponenten | Stufe |  Art   | Rang |            Schiff            | Fern.                        |
|:-----------:|:-----:|:------:|:----:|:----------------------------:|:-----------------------------|
| 6 x T aura  |   8   | Normal |  2   | :material-check:{ .success } | :material-check:{ .success } |

`ZAUBERE [REGION x y] [STUFE n] 'Traumbilder entwirren' ( REGION | EINHEIT <Einheit-Nr> [<Einheit-Nr> ...] | SCHIFF <Schiff-Nr> [<Schiff-Nr> ...] | BURG <Gebäude-Nr> [<Gebäude-Nr> ...] )`  

## Stufe 9

### Vertrauten rufen

:   Einem erfahrenen Magier wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Magier anschließen wird.  

|         Komponenten         | Stufe |  Art   | Rang | Schiff | Fern. |
|:---------------------------:|:-----:|:------:|:----:|:------:|:------|
| 100 aura, 5 permanente aura |   9   | Normal |  5   |        |       |

`ZAUBERE 'Vertrauten rufen'`  

## Stufe 10

### Schlechte Träume

:   Dieser Zauber ermöglicht es dem Träumer, den Schlaf aller nichtaliierten Einheiten (HELFE BEWACHE) in der Region so stark zu stören, das sie vorübergehend einen Teil ihrer Erinnerungen verlieren.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern.                        |
|:-----------:|:-----:|:------:|:----:|:------:|:-----------------------------|
|   90 aura   |  10   | Normal |  5   |        | :material-check:{ .success } |

`ZAUBERE [REGION x y] 'Schlechte Träume'`  

## Stufe 11

### Tod des Geistes

:   Mit diesem Zauber greift der Magier direkt den Geist seiner Gegner an.  
    Ein Schlag aus astraler und elektrischer Energie trifft die Gegner, wird die Magieresistenz durchbrochen, verliert ein Opfer permanent einen Teil seiner Erinnerungen.  
    Wird es zu oft ein Opfer dieses Zaubers kann es daran sterben.  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 2 x T aura  |  11   | Prä-k. |  5   |        |       |

`KAMPFZAUBER [STUFE n] 'Tod des Geistes'`  

## Stufe 12

### Süße Träume

:   Dieser Zauber - dessen Anwendung in den meisten Kulturen streng verboten ist - löst im Opfer ein unkontrollierbares Verlangen nach körperlicher Liebe aus.  
    Die betroffenen Personen werden sich Hals über Kopf in ein Liebesabenteuer stürzen, zu blind vor Verlangen, um an etwas anderes zu denken.  
    Meistens bereuen sie es einige Wochen später...  

| Komponenten | Stufe |  Art   | Rang | Schiff | Fern. |
|:-----------:|:-----:|:------:|:----:|:------:|:------|
| 5 x T aura  |  12   | Normal |  5   |        |       |

`ZAUBERE [STUFE n] 'Süße Träume' <Einheit-Nr> [<Einheit-Nr> ...]`  

## Stufe 13

### Erschaffe eine [Sphäre der Unsichtbarkeit]

:   Mit diesem Spruch kann der Zauberer eine Sphäre der Unsichtbarkeit erschaffen.  
    Die Späre macht ihren Träger sowie neunundneunzig weitere Personen in derselben Einheit unsichtbar.  

|                Komponenten                | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:-----------------------------------------:|:-----:|:------:|:----:|:----------------------------:|:-----:|
| 150 aura, 30000 silber, 3 permanente aura |  13   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE 'Erschaffe eine Sphäre der Unsichtbarkeit'`  

## Stufe 14

### Erschaffe ein [Traumauge]

:   Ein mit diesem Zauber belegtes Drachenauge, welches zum Abendmahle verzehrt wird, erlaubt es dem Benutzer, in die Träume einer anderen Person einzudringen und diese zu lesen.  
    Lange Zeit wurde eine solche Fähigkeit für nutzlos erachtet, bis die ehemalige waldelfische Magistra für Kampfmagie, Liarana Sonnentau von der Akademie Thall, eine besondere Anwendung vorstellte: Feldherren träumen vor großen Kämpfen oft unruhig und verraten im Traum ihre Pläne.  
    Dies kann dem Anwender einen großen Vorteil im kommenden Kampf geben.  
    Aber Vorsicht: Die Interpretation von Träumen ist eine schwierige Angelegenheit.  

|             Komponenten              | Stufe |  Art   | Rang |            Schiff            | Fern. |
|:------------------------------------:|:-----:|:------:|:----:|:----------------------------:|:-----:|
| 1 [[drachenkopf]], 5 permanente aura |  14   | Normal |  5   | :material-check:{ .success } |       |

`ZAUBERE 'Erschaffe ein Traumauge'`  

<!-- From [https://wiki.eressea.de/index.php?title=Illaunzauber&oldid=7014] -->
