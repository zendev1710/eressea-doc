---
# cSpell:locale fr
alias: sorts-illaun
---
# Sorts Illaun

Les sorts de l'École de magie **Illaun** sont décrits ci-dessous par ordre de niveau croissant.

## Schattenritter

**Description** :  
Dieser Zauber vermag dem Gegner ein geringfügig versetztes Bild der eigenen Truppen vorzuspiegeln. Die Schattenritter haben keinen effektiven Angriff und Verwundungen im Kampf zerstören sie sofort.  
**Type** : sort de pré-combat  
**Niveau** : 1  
**Rang** : 4  
**Composants** : N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Schattenritter"`  

## Traumsenden

**Description** :  
Der Zauberer sendet dem Ziel des Spruches einen Traum.  
**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Traumsenden" <Unit-id>`  

## Wahrsagen

**Description** :  
Niemand kann so gut die Träume deuten wie ein Magier des Illaun. Auch die Kunst der Wahrsagerei, des Kartenlegens und des Handlesens sind ihm geläufig. Dafür zahlen ihm die Bauern 50 silver pro Stufe.  
**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Wahrsagen"`  

## Grauen der Schlacht

**Description** :  
Der Traumweber beschwört vor dem Kampf grauenerregende Trugbilder herauf, die viele Gegner in Panik versetzen. Die Betroffenen werden versuchen, vor den Trugbildern zu fliehen.  
**Type** : sort de pré-combat  
**Niveau** : 2  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Grauen der Schlacht"`  

## Repos éternel

<!-- cspell:disable -->
*Eternal Rest (EN), Seelenfrieden (DE)*.
<!-- cspell:enable -->

:   Ce rituel magique apaise les âmes tourmentées de ceux qui sont morts violemment, leur permettant d'entamer leur dernier voyage vers les Autres Terres.
    Environ 50 âmes trouveront la paix par niveau de sort.
    Le sort ne peut pas racheter les morts-vivants déjà ressuscités car leurs liens avec ce monde sont trop forts.

**Type** : sort normal  
**Niveau** : 2  
**Rang** : 5  
**Composants** : 3 x N Aura, 1 [eau de vie]  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Eternal Rest"`  

## Gestaltwandlung

**Description** :  
Mit Hilfe dieses arkanen Rituals vermag der Traumweber die wahre Gestalt einer Gruppe zu verschleiern. Unbedarften Beobachtern erscheint sie dann als einer anderen Rasse zugehörig.  
**Type** : sort normal  
**Niveau** : 3  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Gestaltwandlung" <Unit-id> <Rasse>`  

## Rêve de magie

<!-- cspell:disable -->
*Dream of Magic (EN), Traum der Magie (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le tisserand de rêves peut transférer sa propre aura à un autre tisserand de rêves dans un rapport de 2:1.

**Type** : sort normal  
**Niveau** : 3  
**Rang** : 1  
**Composants** : 2 Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Dream of Magic" <unit-id> <Aura>`  

## Château d'Illusion

<!-- cspell:disable -->
*Castle of Illusion (EN), Traumschlößchen (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le tisserand de rêves peut créer l'illusion de n'importe quel bâtiment.
    L'illusion peut être saisie, mais elle est par ailleurs non fonctionnelle et ne nécessite aucun entretien.
    Cela durera quelques semaines.

**Type** : sort normal  
**Niveau** : 3  
**Rang** : 5  
**Composants** : 3 Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST "Castle of Illusion" <building-type>`  

## Schwere Glieder

**Description** :  
Dieser sort de combat führt dazu, dass einige Gegner im Kampf unter schwerer Müdigkeit leiden. Die Soldaten verschlafen manchmal ihren Angriff und verteidigen sich schlechter.  
**Type** : sort de pré-combat  
**Niveau** : 4  
**Rang** : 5  
**Composants** : 4 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Schwere Glieder"`  

## Traumlesen

**Description** :  
Dieser Zauber ermöglicht es dem Traumweber, in die Träume einer Unit einzudringen und so einen Bericht über die Umgebung zu erhalten.  
**Type** : sort normal  
**Niveau** : 4  
**Rang** : 5  
**Composants** : 8 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Traumlesen" <Unit-id>`  

## Analyse des rêves

<!-- cspell:disable -->
*Analyse Dreams (EN), Traumbilder analysieren (DE)*.
<!-- cspell:enable -->

:   Avec ce sort, le tisserand de rêves peut tenter de détecter les enchantements d'une seule unité.
    Il pourra se faire une idée de leur efficacité grâce à tous les sorts qui ne dépassent pas ses propres capacités.
    Avec des sorts plus puissants, il lui faut un peu de chance pour réussir son analyse.


**Type** : sort normal  
**Niveau** : 5  
**Rang** : 5  
**Composants** : 25 Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Traumbilder analysieren" <Unit-id>`  

## Wiederbelebung

**Description** :  
Stirbt ein Krieger im Kampf so macht sich seine Seele auf die lange Wanderung zu den Sternen. Mit Hilfe eines Rituals kann ein Traumweber versuchen, die Seele wieder einzufangen und in den Körper des Verstorbenen zurückzubringen. Zwar heilt der Zauber keine körperlichen Verwundungen, doch ein Behandelter wird den Kampf überleben.  
**Type** : sort de post-combat  
**Niveau** : 5  
**Rang** : 4  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Wiederbelebung"`  

## Erschaffe ein Amulett des wahren Sehens

**Description** :  
Der Spruch ermöglicht es einem Magier, ein Amulett des Wahren Sehens zu erschaffen. Das Amulett erlaubt es dem Träger, alle Einheiten, die durch einen Ring der Unsichtbarkeit geschützt sind, zu sehen. Einheiten allerdings, die sich mit ihrem Tarnungs-Talent verstecken, bleiben weiterhin unentdeckt.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 50 Aura, 3000 silver, 1 Aura permanent  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe ein Amulett des wahren Sehens"`  

## Erschaffe einen Ring der Unsichtbarkeit

**Description** :  
Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer unsichtbaren Unit muss jede Person einen Ring tragen.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 50 Aura, 3000 silver, 1 Aura permanent  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe einen Ring der Unsichtbarkeit"`  

## Schlechter Schlaf

**Description** :  
Dieser Zauber führt in der betroffenen Region für einige Wochen zu Schlaflosigkeit und Unruhe. Den Betroffenen fällt das Lernen deutlich schwerer.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 18 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Schlechter Schlaf"`  

## Schlaf

**Description** :  
Dieser Zauber läßt einige feindliche Kämpfer einschlafen. Schlafende Kämpfer greifen nicht an und verteidigen sich schlechter, sie wachen jedoch auf, sobald sie im Kampf getroffen werden.  
**Type** : sort de combat  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Schlaf"`  

## Traumdeuten

**Description** :  
Mit diesem Zauber dringt der Traumweber in die Gedanken und Traumwelt seines Opfers ein und kann so seine intimsten Geheimnisse ausspähen. Seine Fähigkeiten, seinen Besitz und seine Parteizugehörigkeit wird nicht länger ungewiss sein.  
**Type** : sort normal  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 20 Aura  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Traumdeuten" <Unit-id>`  

## Schöne Träume

**Description** :  
Dieser Zauber ermöglicht es dem Traumweber, den Schlaf aller aliierten Einheiten in der Region so zu beeinflussen, dass sie für einige Zeit einen Bonus in allen Talenten bekommen.  
**Type** : sort normal  
**Niveau** : 8  
**Rang** : 5  
**Composants** : 80 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Schöne Träume"`  

## Traumbilder entwirren

**Description** :  
Dieser Zauber ermöglicht es dem Traumweber die natürlichen und aufgezwungenen Traumbilder einer Person, eines Gebäudes, Schiffes oder einer Region zu unterscheiden und diese zu entwirren.  
**Type** : sort normal  
**Niveau** : 8  
**Rang** : 2  
**Composants** : 6 x N Aura  
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Traumbilder entwirren"` ( REGION | UNIT <Unit-id> [<Unit-id> ...] | SCHIFF <Schiff-id> | BURG <Gebäude-id> )  

## Vertrauten rufen

**Description** :  
Einem erfahrenen Magier wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Magier anschließen wird.  
**Type** : sort normal  
**Niveau** : 9  
**Rang** : 5  
**Composants** : 100 Aura, 5 Aura permanent  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST "Vertrauten rufen"`  

## Schlechte Träume

**Description** :  
Dieser Zauber ermöglicht es dem Träumer, den Schlaf aller nichtaliierten Einheiten (HELP GUARD) in der Region so stark zu stören, das sie vorübergehend einen Teil ihrer Erinnerungen verlieren.  
**Type** : sort normal  
**Niveau** : 10  
**Rang** : 5  
**Composants** : 90 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Schlechte Träume"`  

## Tod des Geistes

**Description** :  
Mit diesem Zauber greift der Magier direkt den Geist seiner Gegner an. Ein Schlag aus astraler und elektrischer Energie trifft die Gegner, wird die Magieresistenz durchbrochen, verliert ein Opfer permanent einen Teil seiner Erinnerungen. Wird es zu oft ein Opfer dieses Zaubers kann es daran sterben.  
**Type** : sort de pré-combat  
**Niveau** : 11  
**Rang** : 5  
**Composants** : 2 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Tod des Geistes"`  

## Süße Träume

**Description** :  
Dieser Zauber - dessen Anwendung in den meisten Kulturen streng verboten ist - löst im Opfer ein unkontrollierbares Verlangen nach körperlicher Liebe aus. Die betroffenen Personen werden sich Hals über Kopf in ein Liebesabenteuer stürzen, zu blind vor Verlangen, um an etwas anderes zu denken. Meistens bereuen sie es einige Wochen später...  
**Type** : sort normal  
**Niveau** : 12  
**Rang** : 5  
**Composants** : 5 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Süße Träume" <Unit-id> [<Unit-id> ...]`  

## Erschaffe eine Sphäre der Unsichtbarkeit

**Description** :  
Mit diesem Spruch kann der Zauberer eine Sphäre der Unsichtbarkeit erschaffen. Die Späre macht ihren Träger sowie neunundneunzig weitere Personen in derselben Unit unsichtbar.  
**Type** : sort normal  
**Niveau** : 13  
**Rang** : 5  
**Composants** : 150 Aura, 30 000 silver, 3 Aura permanent  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe eine Sphäre der Unsichtbarkeit"`  

## Créer un [[dreameye]]

<!-- cspell:disable -->
*Create A DreamEye (EN), Erschaffe ein Traumauge (DE)*.
<!-- cspell:enable -->

:   Un œil de dragon lancé avec ce sort est consommé lors de la communion, ce qui permet à l'utilisateur d'entrer et de lire les rêves d'une autre personne.
    Pendant longtemps, une telle capacité a été considérée comme inutile jusqu'à ce que l'ancien maître de la magie de combat des Elfes des bois, Liarana Sundew de l'Académie Thall, présente une application spéciale :
    les généraux rêvent souvent sans relâche avant les batailles majeures et révèlent leurs plans dans leurs rêves.
    Cela peut donner à l'utilisateur un énorme avantage dans la bataille à venir.
    Mais attention : interpréter les rêves est une affaire difficile.

**Type** : sort normal  
**Niveau** : 14  
**Rang** : 5  
**Composants** : 1 tête de dragon, 5 Aura permanent  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Create A DreamEye"`  

<!-- From [https://wiki.eressea.de/index.php?title=Illaunzauber&oldid=7014] -->

[eau de vie]: ./alchemy.md#eau-de-vie "Water of life"