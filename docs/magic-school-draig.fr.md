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
**Composants** : N Aura
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Kleine Flüche"`  

## Verwünschung

**Description** :  
Das Ziel des Zauberers wird von einer harmlosen Verwünschung heimgesucht.  
**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : N Aura
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Verwünschung" <unit-id>`  

### Boule de feu

<!-- cspell:disable -->
*Fireball (EN), Feuerball (DE)*.
<!-- cspell:enable -->

:   Le sorcier lance un chaos ciblé dans les rangs ennemis. Le chaos en forme de boule blessera tous ceux qu'il touchera.

**Type** : sort de combat  
**Niveau** : 2  
**Rang** : 5  
**Composants** : N Aura
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Fireball"`  

## Don du Chaos

<!-- cspell:disable -->
*Chaos Gift (EN), Gabe des Chaos (DE)*.
<!-- cspell:enable -->

:   Le mage ouvre son esprit aux sphères du Chaos et disposera ainsi de plus de pouvoir magique pendant un certain temps.
    Mais l’aide des Seigneurs des Sphères a un prix, et la phase de pouvoir est donc remplacée par une phase de faiblesse.

**Type** : sort normal  
**Niveau** : 3  
**Rang** : 3  
**Composants** : 6 Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Chaos Gift"`  

## Kleines Blutopfer

**Description** :  
Mit diesem Ritual kann der Magier einen Teil seiner Lebensenergie opfern, um dafür an magischer Kraft zu gewinnen. Erfahrene Ritualmagier berichten, das sich das Ritual, einmal initiiert, nur schlecht steuern ließe und die Menge der so gewonnenen Kraft stark schwankt. So steht im 'Buch des Blutes' geschrieben: 'So richte Er aus das Zeichen der vier Elemente im Kreis des Werdens und Vergehens und Weihe ein jedes mit einem Tropfen Blut. Sodann begebe Er in der Mitten der Ewigen Vierer sich und lasse Leben verrinnen, auf das Kraft geboren werde.'  
**Type** : sort normal  
**Niveau** : 4  
**Rang** : 1  
**Composants** : 16 Trefferpunkte  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Kleines Blutopfer"`  

## Soif de sang

<!-- cspell:disable -->
*Blood Frenzy (EN), Blutrausch (DE)*.
<!-- cspell:enable -->

:   Dans ce rituel sanglant, le mage sacrifie un nouveau-né devant son armée avant le combat.
    Les esprits du sang ainsi invoqués prendront possession des soldats et les plongeront dans une soif de sang.

**Type** : sort de pré-combat  
**Niveau** : 5  
**Rang** : 4  
**Composants** : 5 x N Aura, 1 paysan  
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Blood Frenzy"`  

## Malédiction du Chaos

<!-- cspell:disable -->
*Chaos Curse (EN), Chaosfluch (DE)*.
<!-- cspell:enable -->

:   Cette malédiction insidieuse altère considérablement les capacités magiques de la victime.
    Une zone magique de chaos autour de la victime réduit sa capacité de concentration et rend très difficile le lancement de sorts.

**Type** : sort normal  
**Niveau** : 5  
**Rang** : 4  
**Composants** : 4 x N Aura
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Chaos Curse" <unit-id>`  

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

## Pouvoirs des morts

<!-- cspell:disable -->
*Animate Dead (EN), Mächte des Todes (DE)*.
<!-- cspell:enable -->

:   Le mage noir doit passer des nuits à errer dans les cimetières et cimetières de la région afin de pouvoir faire revivre les cadavres déterrés.
    Les morts-vivants seront à son service, mais les non-informés doivent savoir qu'invoquer les forces de la mort peut être une arme à double tranchant.

**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 5 x N Aura
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Mächte des Todes"`  

## Rosthauch

**Description** :  
Mit diesem Ritual wird eine dunkle Gewitterfront beschworen, die sich unheilverkündend über der Region auftürmt. Der magische Regen wird alles Erz rosten lassen und so viele Waffen des Gegners zerstören.  
**Type** : sort de combat  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 2 x N Aura
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Rosthauch"`  

### Mur de feu

<!-- cspell:disable -->
*Firewall (EN), Feuerwand (DE)*.
<!-- cspell:enable -->

:   L'assistant crée un mur de feu dans la direction spécifiée.
    Cela fait mal à tous ceux qui le traversent.

**Type** : sort normal  
**Niveau** : 7  
**Rang** : 4  
**Composants** : 6 x N Aura
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Firewall" <direction>`  

## Malédiction de la peste

<!-- cspell:disable -->
*Curse of Pestilence (EN), Fluch der Pestilenz (DE)*.
<!-- cspell:enable -->

:   Dans un rituel élaboré, le mage noir sacrifie quelques paysans puis distribue comme par magie les cadavres dans les puits de la région.

**Type** : sort normal  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 30 Aura, 50 paysans  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Curse of Pestilence"`  

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
**Composants** : 3 x N Aura
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Beschwöre Schattendämonen"`  

## Wahnsinn des Krieges

**Description** :  
Vor den Augen der feindlichen Soldaten opfert der Schwarzmagier die zehn Bauern in einem blutigen, grausamen Ritual und beschwört auf diese Weise Geister des Wahnsinns über die feindlichen Truppen. Diese werden im Kampf verwirrt reagieren und nicht in der Lage sein, den Anweisungen ihrer Offiziere zu folgen.  
**Type** : sort de pré-combat  
**Niveau** : 8  
**Rang** : 5  
**Composants** : 3 x N Aura, 10 paysans  
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Wahnsinn des Krieges"`  

## Fuite de l'Astral

<!-- cspell:disable -->
*Astral Leak (EN), Astraler Riss (DE)*.
<!-- cspell:enable -->

:   Avec ce sombre rituel, le mage noir peut provoquer une rupture dans le tissu magique, qui arrachera tout pouvoir magique de la région.
    Toutes les personnes douées pour la magie dans la région perdront une grande partie de leur aura.

**Type** : sort normal  
**Niveau** : 9  
**Rang** : 3  
**Composants** : 35 Aura, 1 Drachenblut  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Astral Leak"`  

## Chaos de l'Astral

<!-- cspell:disable -->
*Astral Chaos (EN), Astrales Chaos (DE)*.
<!-- cspell:enable -->

:   Ce rituel, effectué avant la bataille, fait tourbillonner les énergies astrales sur le champ de bataille, rendant plus difficile le lancement de leurs sorts par les mages ennemis.

**Type** : sort de pré-combat  
**Niveau** : 9  
**Rang** : 2  
**Composants** : 6 x N Aura
**Modificateurs** : *aucun*
**Syntaxe** : `COMBATSPELL [LEVEL n] "Astral Chaos"`  

## Créer une [[belt-of-troll-strength]]

<!-- cspell:disable -->
*Create A Belt of Troll Strength (EN), Erschaffe einen Gürtel der Trollstärke (DE)*.
<!-- cspell:enable -->

:   Cet artefact magique confère à son porteur la force d'un Troll des Cavernes adulte.
    Sa capacité de charge est multipliée par 50 et sa force accrue et sa peau résistante aux trolls auront également un effet positif au combat.

**Type** : sort normal  
**Niveau** : 9  
**Rang** : 5  
**Composants** : 20 Aura, 1 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Create A Belt of Troll Strength"`  

## Untote Helden

**Description** :  
Dieses Ritual bindet die bereits entfliehenden Seelen einiger Kampfopfer an ihren toten Körper, wodurch sie zu untoten Leben wiedererweckt werden. Ob sie ehemals auf der Seite des Feindes oder der eigenen kämpften, ist für das Ritual ohne belang.  
**Type** : sort de post-combat  
**Niveau** : 9  
**Rang** : 5  
**Composants** : N Aura
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
**Composants** : 10 x N Aura
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
**Composants** : 7 x N Aura
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Beschwöre Schattenmeister"`  

## Créer une [[flaming-sword]]

<!-- cspell:disable -->
*Create A Flaming Sword (EN), Erschaffe ein Flammenschwert (DE)*.
<!-- cspell:enable -->

:   "Et alors frottez le sang d'un féroce combattant dans l'acier de la lame et commencez l'invocation des Sphères du Chaos.
    Et si vous avez tout fait pour leur plaire, ils enverront l'un des leurs pour imprégner l'épée de son pouvoir..."

**Type** : sort normal  
**Niveau** : 12  
**Rang** : 5  
**Composants** : 100 Aura, 1 [sang de berserker], 1 [épée], 1 permanente Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Create A Flaming Sword"`  

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
**Composants** : 10 x N Aura, 5 x N paysans
**Modificateurs** : *aucun*
**Syntaxe** : `CAST [LEVEL n] "Unheilige Kraft" <unit-id> [<unit-id> ...]`  

<!-- From [https://wiki.eressea.de/index.php?title=Draigzauber&oldid=6510] -->

[sang de berserker]: ./alchemy.fr.md#sang-de-berserker "Berserkers blood"
[épée]: ./war-tables.md#epee "Sword"
