---
# cSpell:locale fr
alias: sorts-draig
---
# Sorts Draig

Les sorts de l'École de magie **Draig** sont décrits ci-dessous par ordre de niveau croissant.

## Kleine Flüche

**Description** :  
In den dunkleren Gassen gibt es sie, die Flüche und Verhexungen auf Bestellung. Aber auch Gegenzauber hat der Jünger des Draigs natürlich im Angebot. Ob nun der Sohn des Nachbarn in einen Liebesbann gezogen werden soll oder die Nebenbuhlerin Pickel und Warzen bekommen soll, niemand gibt gerne zu, zu solchen Mitteln gegriffen zu haben. Für diese Dienstleistung streicht der Magier 50 silver pro Stufe ein.  
**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Kleine Flüche"`  

## Verwünschung

**Description** :  
Das Ziel des Zauberers wird von einer harmlosen Verwünschung heimgesucht.  
**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Verwünschung" <unit-id>`  

## Feuerball

**Description** :  
Der Zauberer schleudert fokussiertes Chaos in die Reihen der Gegner. Das ballförmige Chaos wird jeden verwunden, den es trifft.  
**Type** : sort de combat  
**Niveau** : 2  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Feuerball"`  

## Gabe des Chaos

**Description** :  
Der Magier öffnet seinen Geist den Sphären des Chaos und wird so für einige Zeit über mehr magische Kraft verfügen. Doch die Hilfe der Herren der Sphären hat seinen Preis, und so wird die Phase der Macht abgelöst von einer Phase der Schwäche.  
**Type** : sort normal  
**Niveau** : 3  
**Rang** : 3  
**Composants** : 6 Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Gabe des Chaos"`  

## Kleines Blutopfer

**Description** :  
Mit diesem Ritual kann der Magier einen Teil seiner Lebensenergie opfern, um dafür an magischer Kraft zu gewinnen. Erfahrene Ritualmagier berichten, das sich das Ritual, einmal initiiert, nur schlecht steuern ließe und die Menge der so gewonnenen Kraft stark schwankt. So steht im 'Buch des Blutes' geschrieben: 'So richte Er aus das Zeichen der vier Elemente im Kreis des Werdens und Vergehens und Weihe ein jedes mit einem Tropfen Blut. Sodann begebe Er in der Mitten der Ewigen Vierer sich und lasse Leben verrinnen, auf das Kraft geboren werde.'  
**Type** : sort normal  
**Niveau** : 4  
**Rang** : 1  
**Composants** : 16 Trefferpunkte  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Kleines Blutopfer"`  

## Blutrausch

**Description** :  
In diesem blutigen Ritual opfert der Magier vor der Schlacht ein Neugeborenes vor den Augen seiner Armee. Die so gerufenen Blutgeister werden von den Soldaten Besitz ergreifen und sie in einen Blutrausch versetzen.  
**Type** : sort de pré-combat  
**Niveau** : 5  
**Rang** : 4  
**Composants** : 5 Aura \* niveau, 1 Bauer  
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Blutrausch"`  

## Chaosfluch

**Description** :  
Dieser heimtückische Fluch beeinträchtigt die magischen Fähigkeiten des Opfers erheblich. Eine chaosmagische Zone um das Opfer vermindert seine Konzentrationsfähigkeit und macht es ihm sehr schwer Zauber zu wirken.  
**Type** : sort normal  
**Niveau** : 5  
**Rang** : 4  
**Composants** : 4 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Chaosfluch" <unit-id>`  

## Erschaffe ein Amulett des wahren Sehens

**Description** :  
Der Spruch ermöglicht es einem Magier, ein Amulett des Wahren Sehens zu erschaffen. Das Amulett erlaubt es dem Träger, alle Einheiten, die durch einen Ring der Unsichtbarkeit geschützt sind, zu sehen. Einheiten allerdings, die sich mit ihrem Tarnungs-Talent verstecken, bleiben weiterhin unentdeckt.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 50 Aura, 3000 silver, 1 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe ein Amulett des wahren Sehens"`  

## Erschaffe einen Ring der Unsichtbarkeit

**Description** :  
Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer unsichtbaren unit muss jede Person einen Ring tragen.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 50 Aura, 3000 silver, 1 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe einen Ring der Unsichtbarkeit"`  

## Mächte des Todes

**Description** :  
Nächtelang muss der Schwarzmagier durch die Friedhöfe und Gräberfelder der Region ziehen um dann die ausgegrabenen Leichen beleben zu können. Die Untoten werden ihm zu Diensten sein, doch sei der Unkundige gewarnt, dass die Beschwörung der Mächte des Todes ein zweischneidiges Schwert sein kann.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 5 Aura X niveau
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Mächte des Todes"`  

## Rosthauch

**Description** :  
Mit diesem Ritual wird eine dunkle Gewitterfront beschworen, die sich unheilverkündend über der Region auftürmt. Der magische Regen wird alles Erz rosten lassen und so viele Waffen des Gegners zerstören.  
**Type** : sort de combat  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 2 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Rosthauch"`  

## Feuerwand

**Description** :  
Der Zauberer erschafft eine Wand aus Feuer in der angegebenen Richtung. Sie verletzt jeden, der sie durchschreitet.  
**Type** : sort normal  
**Niveau** : 7  
**Rang** : 4  
**Composants** : 6 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Feuerwand" <Richtung>`  

## Fluch der Pestilenz

**Description** :  
In einem aufwendigen Ritual opfert der Schwarzmagier einige Bauern und verteilt dann die Leichen auf magische Weise in den Brunnen der Region.  
**Type** : sort normal  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 30 Aura, 50 Bauern  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Fluch der Pestilenz"`  

## Machtübertragung

**Description** :  
Mit Hilfe dieses Zaubers kann der Magier eigene Aura im Verhältnis 2:1 auf einen anderen Magier des gleichen Magiegebietes übertragen.  
**Type** : sort normal  
**Niveau** : 7  
**Rang** : 1  
**Composants** : 2 Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Machtübertragung" <unit-id> <Aura>`  

## Beschwöre Schattendämonen

**Description** :  
Mit Hilfe dunkler Rituale beschwört der Zauberer Dämonen aus der Sphäre der Schatten. Diese gefürchteten Wesen können sich fast unsichtbar unter den Lebenden bewegen, ihre finstere Aura ist jedoch für jeden spürbar. Im Kampf sind Schattendämonen gefürchtete Gegner. Sie sind schwer zu treffen und entziehen ihrem Gegner Kraft.  
**Type** : sort normal  
**Niveau** : 8  
**Rang** : 5  
**Composants** : 3 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Beschwöre Schattendämonen"`  

## Wahnsinn des Krieges

**Description** :  
Vor den Augen der feindlichen Soldaten opfert der Schwarzmagier die zehn Bauern in einem blutigen, grausamen Ritual und beschwört auf diese Weise Geister des Wahnsinns über die feindlichen Truppen. Diese werden im Kampf verwirrt reagieren und nicht in der Lage sein, den Anweisungen ihrer Offiziere zu folgen.  
**Type** : sort de pré-combat  
**Niveau** : 8  
**Rang** : 5  
**Composants** : 3 Aura \* niveau, 10 Bauern  
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Wahnsinn des Krieges"`  

## Astraler Riss

**Description** :  
Der Schwarzmagier kann mit diesem dunklen Ritual einen Riss in das Gefüge der Magie bewirken, der alle magische Kraft aus der Region reißen wird. Alle magisch begabten in der Region werden einen Großteil ihrer Aura verlieren.  
**Type** : sort normal  
**Niveau** : 9  
**Rang** : 3  
**Composants** : 35 Aura, 1 Drachenblut  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Astraler Riss"`  

## Astrales Chaos

**Description** :  
Dieses Ritual, ausgeführt vor einem Kampf, verwirbelt die astralen Energien auf dem Schlachtfeld und macht es so feindlichen Magier schwieriger, ihre Zauber zu wirken.  
**Type** : sort de pré-combat  
**Niveau** : 9  
**Rang** : 2  
**Composants** : 6 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Astrales Chaos"`  

## Erschaffe einen Gürtel der Trollstärke

**Description** :  
Dieses magische Artefakt verleiht dem Träger die Stärke eines ausgewachsenen Höhlentrolls. Seine Tragkraft erhöht sich auf das 50fache und auch im Kampf werden sich die erhöhte Kraft und die trollisch zähe Haut positiv auswirken.  
**Type** : sort normal  
**Niveau** : 9  
**Rang** : 5  
**Composants** : 20 Aura, 1 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe einen Gürtel der Trollstärke"`  

## Untote Helden

**Description** :  
Dieses Ritual bindet die bereits entfliehenden Seelen einiger Kampfopfer an ihren toten Körper, wodurch sie zu untoten Leben wiedererweckt werden. Ob sie ehemals auf der Seite des Feindes oder der eigenen kämpften, ist für das Ritual ohne belang.  
**Type** : sort de post-combat  
**Niveau** : 9  
**Rang** : 5  
**Composants** : 1 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Untote Helden"`  

## Feuerteufel

**Description** :  
Diese Elementarbeschwörung ruft einen Feuerteufel herbei, ein Wesen aus den tiefsten Niederungen der Flammenhöllen. Der Feuerteufel wird sich begierig auf die Wälder der Region stürzen und sie in Flammen setzen.  
**Type** : sort normal  
**Niveau** : 10  
**Rang** : 5  
**Composants** : 50 Aura, 1 Öl  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Feuerteufel"`  

## Pentagramm

**Description** :  
Genau um Mitternacht, wenn die Kräfte der Finsternis am größten sind, kann auch ein Schwarzmagier seine Kräfte nutzen um Verzauberungen aufzuheben. Dazu zeichnet er ein Pentagramm in das verzauberte Objekt und beginnt mit einer Anrufung der Herren der Finsternis. Die Herren werden ihm beistehen, doch ob es ihm gelingt, den Zauber zu lösen, hängt allein von seiner eigenen Kraft ab.  
**Type** : sort normal  
**Niveau** : 10  
**Rang** : 2  
**Composants** : 10 Aura X niveau
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Pentagramm" ( REGION | UNIT <unit-id> [<unit-id> ...] | SCHIFF <Schiff-id> | BURG <Gebäude-id> )`  

## Drachenruf

**Description** :  
Mit diesem dunklen Ritual erzeugt der Magier einen Köder, der für Drachen einfach unwiderstehlich riecht. Ob die Drachen aus der Umgebung oder aus der Sphäre des Chaos stammen, konnte noch nicht erforscht werden. Es soll beides bereits vorgekommen sein. Der Köder hält etwa 6 Wochen, muss aber in einem drachengenehmen Terrain platziert werden.  
**Type** : sort normal  
**Niveau** : 11  
**Rang** : 5  
**Composants** : 80 Aura, 1 Drachenkopf  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Drachenruf"`  

## Todeswolke

**Description** :  
Mit einem düsteren Ritual und unter Opferung seines eigenen Blutes beschwört der Schwarzmagier einen großen Geist von der Elementarebene der Gifte. Der Geist manifestiert sich als giftgrüner Schwaden über der Region und wird allen, die mit ihm in Kontakt kommen, Schaden zufügen.  
**Type** : sort normal  
**Niveau** : 11  
**Rang** : 5  
**Composants** : 40 Aura, 15 Trefferpunkte  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Todeswolke"`  

## Beschwöre Schattenmeister

**Description** :  
Mit Hilfe dunkler Rituale beschwört der Zauberer Dämonen aus der Sphäre der Schatten. Diese gefürchteten Wesen können sich fast unsichtbar unter den Lebenden bewegen, ihre finstere Aura ist jedoch für jeden spürbar. Im Kampf sind Schattenmeister gefürchtete Gegner. Sie sind schwer zu treffen und entziehen ihrem Gegner Kraft und Leben.  
**Type** : sort normal  
**Niveau** : 12  
**Rang** : 5  
**Composants** : 7 Aura X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Beschwöre Schattenmeister"`  

## Erschaffe ein Flammenschwert

**Description** :  
'Und so reibe das Blut eines wilden Kämpfers in den Stahl der Klinge und beginne die Anrufung der Sphären des Chaos. Und hast du alles zu ihrem Wohlgefallen getan, so werden sie einen niederen der ihren senden, das Schwert mit seiner Macht zu beseelen...'  
**Type** : sort normal  
**Niveau** : 12  
**Rang** : 5  
**Composants** : 100 Aura, 1 Berserkerblut, 1 Schwert, 1 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe ein Flammenschwert"`  

## Vertrauten rufen

**Description** :  
Einem erfahrenen Magier wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Magier anschließen wird.  
**Type** : sort normal  
**Niveau** : 13  
**Rang** : 5  
**Composants** : 100 Aura, 5 permanente Aura  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Vertrauten rufen"`  

## Chaossog

**Description** :  
Durch das Opfern von 200 Bauern kann der Chaosmagier ein Tor zur astralen Welt öffnen. Das Tor kann in der Folgewoche verwendet werden, es löst sich am Ende der Folgewoche auf.  
**Type** : sort normal  
**Niveau** : 14  
**Rang** : 5  
**Composants** : 150 Aura, 200 Bauern  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Chaossog"`  

## Unheilige Kraft

**Description** :  
Nur geflüstert wird dieses Ritual an den dunklen Akademien an die Adepten weitergegeben, gehört es doch zu den finstersten, die je niedergeschrieben wurden. Durch die Anrufung unheiliger Dämonen wird die Kraft der lebenden Toten verstärkt und sie verwandeln sich in untote Monster großer Kraft.  
**Type** : sort normal  
**Niveau** : 14  
**Rang** : 5  
**Composants** : 10 Aura \* niveau, 5 Bauern X niveau
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Unheilige Kraft" <unit-id> [<unit-id> ...]`  

<!-- From [https://wiki.eressea.de/index.php?title=Draigzauber&oldid=6510] -->
