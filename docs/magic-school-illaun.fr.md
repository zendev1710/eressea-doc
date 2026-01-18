---
# cSpell:locale fr
alias: sorts-illaun
---
# Sorts Illaun

Les sorts de l'École de magie **Illaun** sont décrits ci-dessous par ordre de niveau croissant.

## Schattenritter

**Description** :  
Dieser Zauber vermag dem Gegner ein geringfügig versetztes Bild der eigenen Truppen vorzuspiegeln. Die Schattenritter haben keinen effektiven Angriff und Verwundungen im Kampf zerstören sie sofort.  
**Art** : sort de pré-combat  
**Niveau** : 1  
**Rang** : 4  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Schattenritter"`  

## Traumsenden

**Description** :  
Der Zauberer sendet dem Ziel des Spruches einen Traum.  
**Art** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Traumsenden" <Unit-id>`  

## Wahrsagen

**Description** :  
Niemand kann so gut die Träume deuten wie ein Magier des Illaun. Auch die Kunst der Wahrsagerei, des Kartenlegens und des Handlesens sind ihm geläufig. Dafür zahlen ihm die Bauern 50 Silber pro Stufe.  
**Art** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Wahrsagen"`  

## Grauen der Schlacht

**Description** :  
Der Traumweber beschwört vor dem Kampf grauenerregende Trugbilder herauf, die viele Gegner in Panik versetzen. Die Betroffenen werden versuchen, vor den Trugbildern zu fliehen.  
**Art** : sort de pré-combat  
**Niveau** : 2  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Grauen der Schlacht"`  

## Seelenfrieden

**Description** :  
Dieses magische Ritual beruhigt die gequälten Seelen der gewaltsam zu Tode gekommenen und ermöglicht es ihnen so, ihre letzte Reise in die Anderlande zu beginnen. Je Stufe des Zaubers werden ungefähr 50 Seelen ihre Ruhe finden. Der Zauber vermag nicht, bereits wieder auferstandene lebende Tote zu erlösen, da deren Bindung an diese Welt zu stark ist.  
**Art** : sort normal  
**Niveau** : 2  
**Rang** : 5  
**Composants** : 3 Aura \* Stufe, 1 Wasser des Lebens  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Seelenfrieden"`  

## Gestaltwandlung

**Description** :  
Mit Hilfe dieses arkanen Rituals vermag der Traumweber die wahre Gestalt einer Gruppe zu verschleiern. Unbedarften Beobachtern erscheint sie dann als einer anderen Rasse zugehörig.  
**Art** : sort normal  
**Niveau** : 3  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Gestaltwandlung" <Unit-id> <Rasse>`  

## Traum der Magie

**Description** :  
Mit Hilfe dieses Zaubers kann der Traumweber eigene Aura im Verhältnis 2:1 auf einen anderen Traumweber übertragen.  
**Art** : sort normal  
**Niveau** : 3  
**Rang** : 1  
**Composants** : 2 Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Traum der Magie" <Unit-id> <Aura>`  

## Traumschlößchen

**Description** :  
Mit Hilfe dieses Zaubers kann der Traumweber die Illusion eines beliebigen Gebäudes erzeugen. Die Illusion kann betreten werden, ist aber ansonsten funktionslos und benötigt auch keinen Unterhalt. Sie wird einige Wochen bestehen bleiben.  
**Art** : sort normal  
**Niveau** : 3  
**Rang** : 5  
**Composants** : 3 Aura  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Traumschlößchen" <Gebäudetyp>`  

## Schwere Glieder

**Description** :  
Dieser sort de combat führt dazu, dass einige Gegner im Kampf unter schwerer Müdigkeit leiden. Die Soldaten verschlafen manchmal ihren Angriff und verteidigen sich schlechter.  
**Art** : sort de pré-combat  
**Niveau** : 4  
**Rang** : 5  
**Composants** : 4 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Schwere Glieder"`  

## Traumlesen

**Description** :  
Dieser Zauber ermöglicht es dem Traumweber, in die Träume einer Unit einzudringen und so einen Bericht über die Umgebung zu erhalten.  
**Art** : sort normal  
**Niveau** : 4  
**Rang** : 5  
**Composants** : 8 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Traumlesen" <Unit-id>`  

## Traumbilder analysieren

**Description** :  
Mit diesem Spruch kann der Traumweber versuchen, die Verzauberungen einer einzelnen Unit zu erkennen. Von allen Sprüchen, die seine eigenen Fähigkeiten nicht überschreiten, wird er einen Eindruck ihres Wirkens erhalten können. Bei stärkeren Sprüchen benötigt er ein wenig Glück für eine gelungene Analyse.  
**Art** : sort normal  
**Niveau** : 5  
**Rang** : 5  
**Composants** : 25 Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Traumbilder analysieren" <Unit-id>`  

## Wiederbelebung

**Description** :  
Stirbt ein Krieger im Kampf so macht sich seine Seele auf die lange Wanderung zu den Sternen. Mit Hilfe eines Rituals kann ein Traumweber versuchen, die Seele wieder einzufangen und in den Körper des Verstorbenen zurückzubringen. Zwar heilt der Zauber keine körperlichen Verwundungen, doch ein Behandelter wird den Kampf überleben.  
**Art** : sort de post-combat  
**Niveau** : 5  
**Rang** : 4  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Wiederbelebung"`  

## Erschaffe ein Amulett des wahren Sehens

**Description** :  
Der Spruch ermöglicht es einem Magier, ein Amulett des Wahren Sehens zu erschaffen. Das Amulett erlaubt es dem Träger, alle Einheiten, die durch einen Ring der Unsichtbarkeit geschützt sind, zu sehen. Einheiten allerdings, die sich mit ihrem Tarnungs-Talent verstecken, bleiben weiterhin unentdeckt.  
**Art** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 50 Aura, 3000 Silber, 1 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe ein Amulett des wahren Sehens"`  

## Erschaffe einen Ring der Unsichtbarkeit

**Description** :  
Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer unsichtbaren Unit muss jede Person einen Ring tragen.  
**Art** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 50 Aura, 3000 Silber, 1 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe einen Ring der Unsichtbarkeit"`  

## Schlechter Schlaf

**Description** :  
Dieser Zauber führt in der betroffenen Region für einige Wochen zu Schlaflosigkeit und Unruhe. Den Betroffenen fällt das Lernen deutlich schwerer.  
**Art** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 18 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Schlechter Schlaf"`  

## Schlaf

**Description** :  
Dieser Zauber läßt einige feindliche Kämpfer einschlafen. Schlafende Kämpfer greifen nicht an und verteidigen sich schlechter, sie wachen jedoch auf, sobald sie im Kampf getroffen werden.  
**Art** : sort de combat  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Schlaf"`  

## Traumdeuten

**Description** :  
Mit diesem Zauber dringt der Traumweber in die Gedanken und Traumwelt seines Opfers ein und kann so seine intimsten Geheimnisse ausspähen. Seine Fähigkeiten, seinen Besitz und seine Parteizugehörigkeit wird nicht länger ungewiss sein.  
**Art** : sort normal  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 20 Aura  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Traumdeuten" <Unit-id>`  

## Schöne Träume

**Description** :  
Dieser Zauber ermöglicht es dem Traumweber, den Schlaf aller aliierten Einheiten in der Region so zu beeinflussen, dass sie für einige Zeit einen Bonus in allen Talenten bekommen.  
**Art** : sort normal  
**Niveau** : 8  
**Rang** : 5  
**Composants** : 80 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Schöne Träume"`  

## Traumbilder entwirren

**Description** :  
Dieser Zauber ermöglicht es dem Traumweber die natürlichen und aufgezwungenen Traumbilder einer Person, eines Gebäudes, Schiffes oder einer Region zu unterscheiden und diese zu entwirren.  
**Art** : sort normal  
**Niveau** : 8  
**Rang** : 2  
**Composants** : 6 Aura X niveau
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Traumbilder entwirren"` ( REGION | UNIT <Unit-id> [<Unit-id> ...] | SCHIFF <Schiff-id> | BURG <Gebäude-id> )  

## Vertrauten rufen

**Description** :  
Einem erfahrenen Magier wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Magier anschließen wird.  
**Art** : sort normal  
**Niveau** : 9  
**Rang** : 5  
**Composants** : 100 Aura, 5 permanente Aura  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Vertrauten rufen"`  

## Schlechte Träume

**Description** :  
Dieser Zauber ermöglicht es dem Träumer, den Schlaf aller nichtaliierten Einheiten (HELP GUARD) in der Region so stark zu stören, das sie vorübergehend einen Teil ihrer Erinnerungen verlieren.  
**Art** : sort normal  
**Niveau** : 10  
**Rang** : 5  
**Composants** : 90 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Schlechte Träume"`  

## Tod des Geistes

**Description** :  
Mit diesem Zauber greift der Magier direkt den Geist seiner Gegner an. Ein Schlag aus astraler und elektrischer Energie trifft die Gegner, wird die Magieresistenz durchbrochen, verliert ein Opfer permanent einen Teil seiner Erinnerungen. Wird es zu oft ein Opfer dieses Zaubers kann es daran sterben.  
**Art** : sort de pré-combat  
**Niveau** : 11  
**Rang** : 5  
**Composants** : 2 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Tod des Geistes"`  

## Süße Träume

**Description** :  
Dieser Zauber - dessen Anwendung in den meisten Kulturen streng verboten ist - löst im Opfer ein unkontrollierbares Verlangen nach körperlicher Liebe aus. Die betroffenen Personen werden sich Hals über Kopf in ein Liebesabenteuer stürzen, zu blind vor Verlangen, um an etwas anderes zu denken. Meistens bereuen sie es einige Wochen später...  
**Art** : sort normal  
**Niveau** : 12  
**Rang** : 5  
**Composants** : 5 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Süße Träume" <Unit-id> [<Unit-id> ...]`  

## Erschaffe eine Sphäre der Unsichtbarkeit

**Description** :  
Mit diesem Spruch kann der Zauberer eine Sphäre der Unsichtbarkeit erschaffen. Die Späre macht ihren Träger sowie neunundneunzig weitere Personen in derselben Unit unsichtbar.  
**Art** : sort normal  
**Niveau** : 13  
**Rang** : 5  
**Composants** : 150 Aura, 30000 Silber, 3 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe eine Sphäre der Unsichtbarkeit"`  

## Erschaffe ein Traumauge

**Description** :  
Ein mit diesem Zauber belegtes Drachenauge, welches zum Abendmahle verzehrt wird, erlaubt es dem Benutzer, in die Träume einer anderen Person einzudringen und diese zu lesen. Lange Zeit wurde eine solche Fähigkeit für nutzlos erachtet, bis die ehemalige waldelfische Magistra für Kampfmagie, Liarana Sonnentau von der Akademie Thall, eine besondere Anwendung vorstellte: Feldherren träumen vor großen Kämpfen oft unruhig und verraten im Traum ihre Pläne. Dies kann dem Anwender einen großen Vorteil im kommenden Kampf geben. Aber Vorsicht: Die Interpretation von Träumen ist eine schwierige Angelegenheit.  
**Art** : sort normal  
**Niveau** : 14  
**Rang** : 5  
**Composants** : 1 Drachenkopf, 5 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe ein Traumauge"`  

<!-- From [https://wiki.eressea.de/index.php?title=Illaunzauber&oldid=7014] -->
