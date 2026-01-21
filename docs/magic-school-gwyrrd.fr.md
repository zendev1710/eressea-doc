---
# cSpell:locale fr
alias: sorts-gwyrrd
---
# Sorts Gwyrrd

Les sorts de l'École de magie **Gwyrrd** sont décrits ci-dessous par ordre de niveau croissant.

## Créer des [[stone-golem]]

<!-- cspell:disable -->
*Create Stone Golems (EN), Erschaffe Steingolems (DE)*.
<!-- cspell:enable -->

:   "Humidifiez un bloc de fine roche cristalline sans interstice avec une fiole d’eau de vie jusqu’à ce qu’elle soit complètement absorbée par la roche.
    Ensuite, vous dirigez votre force vers la fine aura de vie qui se forme et formez un logement pour la force non liée."
    Plus le mage investit de puissance, plus de golems peuvent être créés avant que l'aura ne se dissipe.
    Chaque golem a 10 pour cent de chances de se transformer en poussière à chaque tour.
    Si vous donnez aux golems l'ordre `MAKE CASTLE` ou `MAKE STREET`, 4 pierres sont utilisées par golem et le golem se dissout.

**Type** : sort normal  
**Niveau** : 1  
**Rang** : 4  
**Composants** : 2 x N Aura, N [pierre], 1 [eau de vie]  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Create Stone Golems"`  

## Bénédiction de la terre

<!-- cspell:disable -->
*Blessed Harvest (EN), Segen der Erde (DE)*.
<!-- cspell:enable -->

<!-- TODO: check description -->
:   Ce rituel de récolte améliore les rendements des agriculteurs qui travaillent dans la région pour un silver de plus.
    Plus le druide investit de puissance, plus le sort dure longtemps.

**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Blessed Harvest"`  

## Guérison du bétail

<!-- cspell:disable -->
*Cattle Healing (EN), Viehheilung (DE)*.
<!-- cspell:enable -->

:   Les compétences d'élevage et de guérison des mages Gwyrrd sont très recherchées par les agriculteurs.
    Leurs services sont souvent très demandés, notamment sur les marchés.
    Certaines personnes peuvent également utiliser leur compétence pour vendre un animal à un meilleur prix.
    Le mage peut gagner 50 silver par niveau.

**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Cattle Healing"`  

## Eisengolems

<!-- cspell:disable -->
*Create Iron Golems (EN), Erschaffe Eisengolems (DE)*.
<!-- cspell:enable -->

:   Plus le mage investit de puissance, plus de golems peuvent être créés.
    Chaque golem a 15 % de chances de se transformer en poussière à chaque tour.
    Si vous donnez aux golems l'ordre `MAKE Sword/BIHANDER` ou `MAKE Shield/CHAIN ​​​​MAIL/PLATE ARMOR`, 4 fer sont consommés par golem et le golem se dissout.

**Type** : sort normal  
**Niveau** : 2  
**Rang** : 4  
**Composants** : 2 x N Aura, N [fer], 1 [eau de vie]  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Create Iron Golems"`  

## Magie du bosquet de chêne

<!-- cspell:disable -->
*Grove of Oak Trees (EN), Hainzauber (DE)*.
<!-- cspell:enable -->

:   Alors qu'auparavant seul un arbre pouvait germer à partir d'un bâton, chaque branche produit désormais des racines.

**Type** : sort normal  
**Niveau** : 2  
**Rang** : 5  
**Composants** : 4 x N Aura, N [bois], 1 [eau de vie]  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Grove of Oak Trees"`  

## Bergwächter

**Description** :  
Erschafft einen Wächtergeist, der in Gletschern und Bergen Eisen- und Laenabbau durch nichtalliierte Parteien (HELP GUARD) verhindert, solange er die Region bewacht. Der Bergwächter ist an den Ort der Beschwörung gebunden.  
**Type** : sort normal  
**Niveau** : 3  
**Rang** : 5  
**Composants** : 3 x N Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Bergwächter"`  

## Le manteau de Firun

<!-- cspell:disable -->
*Firun's Coat (EN), Firuns Fell (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au mage de protéger comme par magie les insectes du froid paralysant des glaciers.
    Vous pouvez entrer dans les glaciers et y agir normalement. Le dicton fonctionne au niveau*10 insectes.
    Un anneau de pouvoir augmente le nombre d'insectes enchantables de 10 supplémentaires.

**Type** : sort normal  
**Niveau** : 3  
**Rang** : 5  
**Composants** : 2 x N Aura  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] "Firun's Coat" <unit-id> [<unit-id> ...]`  

## Grêle

<!-- cspell:disable -->
*Hail (EN), Hagel (DE)*.
<!-- cspell:enable -->

:   Au combat, le mage fait appel aux esprits élémentaires du froid et les lie à lui-même.
    Il peut alors leur ordonner d'attaquer l'ennemi avec des grêlons et des morceaux de glace.

**Type** : sort de combat  
**Niveau** : 3  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] Hail`  

## Rostregen

**Description** :  
Mit diesem Ritual wird eine dunkle Gewitterfront beschworen, die sich unheilverkündend über der Region auftürmt. Der magische Regen wird alles Eisenerz rosten lassen. Eisenwaffen und Rüstungen werden schartig und rostig. Die Zerstörungskraft des Regens ist von der investierten Kraft des Magiers abhängig. Für jede Stufe können bis zu 10 Gegenstände betroffen werden. Ein Ring der Macht verstärkt die Wirkung wie eine zusätzliche Stufe.  
**Type** : sort normal  
**Niveau** : 3  
**Rang** : 5  
**Composants** : 2 x N Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Rostregen" <Einheit-id> [<Einheit-id> ...]`  

## Magischer Pfad

**Description** :  
Durch Ausführung dieser Rituale ist der Magier in der Lage einen mächtigen Erdelementar zu beschwören. Solange dieser in den Boden gebannt ist, wird kein Regen die Wege aufweichen und kein Fluß Brücken zerstören können. Alle Reisende erhalten damit die gleichen Vorteile, die sonst nur ein ausgebautes gepflastertes Straßennetz bietet. Selbst Sümpfe und Gletscher können so verzaubert werden. Je mehr Kraft der Magier in den Bann legt, desto länger bleibt die Straße bestehen.  
**Type** : sort normal  
**Niveau** : 4  
**Rang** : 5  
**Composants** : N Aura, 1 [pierre], 1 [bois]  
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Magischer Pfad"`  

## Segne Mallornstecken

**Description** :  
Diese Ritual verstärkt die Wirkung des magischen Trankes um ein vielfaches. Wo sonst aus einem Stecken nur ein Baum sprießen konnte, so treibt nun jeder Ast Wurzeln.  
**Type** : sort normal  
**Niveau** : 4  
**Rang** : 5  
**Composants** : 6 x N Aura, N Mallorn, 1 [eau de vie]  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Segne Mallornstecken"`  

## Wasserelementar

**Description** :  
Der Magier zwingt mit diesem Ritual die Elementargeister des Wassers in seinen Dienst und bringt sie dazu, das angegebene Schiff schneller durch das Wasser zu tragen. Zudem wird das Schiff nicht durch ungünstige Winde oder Strömungen beeinträchtigt.  
**Type** : sort normal  
**Niveau** : 4  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Beschwörung eines Wasserelementares" <Schiff-id>`  

## Bouclier aérien

<!-- cspell:disable -->
*Air Shield (EN), Windschild (DE)*.
<!-- cspell:enable -->

:   Invoque les esprits élémentaires du vent.
    Invoque des rafales de vent soudaines, de petites rafales de vent et des évents qui gêneront les archers adverses.

**Type** : sort de pré-combat  
**Niveau** : 4  
**Rang** : 5  
**Composants** : 2 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Windschild"`  

## Esprits du Gardien de l'Astral

<!-- cspell:disable -->
*Astral Guardian Spirits (EN), Astralschutzgeister (DE)*.
<!-- cspell:enable -->

:   Ce rituel invoque des esprits élémentaires de magie et les envoie dans les rangs des mages ennemis.
    Ces derniers auront bien plus de mal à lancer des sorts pendant toute la durée du combat.

**Type** : sort de pré-combat  
**Niveau** : 5  
**Rang** : 2  
**Composants** : 5 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Astral Guardian Spirits"`  

## Erschaffe einen magischen Kräuterbeutel

**Description** :  
Der Druide nehme etwas präpariertes Leder, welches er in einem großen Ritual der Reinigung von allen unreinen Geistern befreie, und binde dann einige kleine Geister der Luft und des Wassers in das Material. Aus dem so vorbereiteten Leder fertige er nun ein kleines Beutelchen, welches in ihm aufbewahrte Kräuter besser zu konservieren vermag.  
**Type** : sort normal  
**Niveau** : 5  
**Rang** : 5  
**Composants** : 30 Aura, 1 Aura permanent, 1 [eau de vie]  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe einen magischen Kräuterbeutel"`  

## Heilung

**Description** :  
Nicht nur der Feldscher kann den Verwundeten einer Schlacht helfen. Druiden vermögen mittels einer Beschwörung der Elementargeister des Lebens Wunden zu schließen, gebrochene Knochen zu richten und selbst abgetrennte Glieder wieder zu regenerieren.  
**Type** : sort de post-combat  
**Niveau** : 5  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Heilung"`  

## Wirbelwind

**Description** :  
Diese Beschwörung öffnet ein Tor in die Ebene der Elementargeister des Windes. Sofort erheben sich in der Umgebung des Tors starke Winde oder gar Stürme und behindern alle Schützen einer Schlacht.  
**Type** : sort de pré-combat  
**Niveau** : 5  
**Rang** : 5  
**Composants** : 15 Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Wirbelwind"`  

## Erdelementar

**Description** :  
Der Druide beschwört mit diesem Ritual einen Elementargeist der Erde und bringt ihn dazu, die Erde erbeben zu lassen. Dieses Erdbeben wird alle Gebäude in der Region beschädigen.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 25 Aura, 2 Laen  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Beschwöre einen Erdelementar"`  

## Erschaffe ein Amulett des wahren Sehens

**Description** :  
Der Spruch ermöglicht es einem Magier, ein Amulett des Wahren Sehens zu erschaffen. Das Amulett erlaubt es dem Träger, alle Einheiten, die durch einen Ring der Unsichtbarkeit geschützt sind, zu sehen. Einheiten allerdings, die sich mit ihrem Tarnungs-Talent verstecken, bleiben weiterhin unentdeckt.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 50 Aura, 3 000 silver, 1 Aura permanent  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe ein Amulett des wahren Sehens"`  

## Erschaffe einen Ring der Unsichtbarkeit

**Description** :  
Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer unsichtbaren Einheit muss jede Person einen Ring tragen.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 50 Aura, 3 000 silver, 1 Aura permanent  
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
**Syntaxe** : `CAST "Meditation" <Einheit-id> <Aura>`  

## Sturmelementar

**Description** :  
Die Beschwörung von Elementargeistern der Stürme ist ein uraltes Ritual. Der Druide bannt die Elementare in die Segel der Schiffe, wo sie helfen, das Schiff mit hoher Geschwindigkeit über die Wellen zu tragen. Je mehr Kraft der Druide in den Zauber investiert, desto größer ist die Zahl der Elementargeister, die sich bannen lassen. Für jedes Schiff wird ein Elementargeist benötigt.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 6 x N Aura
**Modificateurs** : Seezauber, sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Beschwöre einen Sturmelementar" <Schiff-id> [<Schiff-id> ...]`  

## Heimstein

**Description** :  
Mit dieser Formel bindet der Magier auf ewig die Kräfte der Erde in die Mauern der Burg, in der er sich gerade befindet. Weder magisch noch mit schwerem Geschütz können derartig gestärkte Mauern zerstört werden, und auch das Alter setzt ihnen weniger zu. Das Gebäude bietet sodann auch einen besseren Schutz gegen Angriffe mit dem Schwert wie mit Magie.  
**Type** : sort normal  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 50 Aura, 1 Aura permanent  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Heimstein"`  

## Wolfsgeheul

**Description** :  
Nicht wenige Druiden freunden sich im Laufe ihres Lebens in der Natur mit den ältesten Freunden der großen Völker an. Sie erlernen, mit einem einzigen heulenden Ruf viele ihrer Freunde herbeizurufen, um ihnen im Kampf beizustehen.  
**Type** : sort de pré-combat  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 2 x N Aura
**Modificateurs** : *aucun*
**Syntaxe** : COMBATSPELL [LEVEL n] "Wolfsgeheul"`  

### Regard du Basilic

<!-- cspell:disable -->
*Gaze of the Basilisk (EN), Blick des Basilisken (DE)*.
<!-- cspell:enable -->

:   Ce sort de combat difficile mais efficace utilise les esprits élémentaires de pierre pour transformer un certain nombre d'ennemis en pierre pendant toute la durée de la bataille.
    Les personnes touchées ne combattront plus, mais elles ne pourront pas non plus être blessées.

**Type** : Kampfzauber  
**Niveau** : 8  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** :*aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Gaze of the Basilisk"`  

## Bannissement des Esprits

<!-- cspell:disable -->
*Banish Spirits (EN), Geister bannen (DE)*.
<!-- cspell:enable -->

:   Selon les anciens enseignements des druides, ce que les êtres ordinaires appellent magie est constitué d'esprits élémentaires.
    Le mage les évoque et les bannit sous une forme permettant d'obtenir l'effet souhaité. Ce rituel est capable de chasser les esprits élémentaires invoqués dans ce monde afin de libérer un objet de la magie.

**Type** : sort normal  
**Niveau** : 8  
**Rang** : 2  
**Composants** : 6 x N Aura  
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Banish Spirits" (REGION | UNIT <unit-id>; [<unit-id>]... | SHIP <ship-id> | CASTLE <building-id>)`  

## Starkes Tor und feste Mauer

**Description** :  
Mit dieser Formel bindet der Magier zu Beginn eines Kampfes einige Elementargeister des Fels in die Mauern des Gebäudes, in dem er sich gerade befindet. Das Gebäude bietet sodann einen besseren Schutz gegen Angriffe mit dem Schwert wie mit Magie.  
**Type** : sort de pré-combat  
**Niveau** : 8  
**Rang** : 5  
**Composants** : 2 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Starkes Tor und feste Mauer"`  

## Heiliger Boden

**Description** :  
Dieses Ritual beschwört verschiedene Naturgeister in den Boden der Region, welche diese fortan bewachen. In einer so gesegneten Region werden niemals wieder die Toten ihre Gräber verlassen, und anderswo entstandene Untote werden sie wann immer möglich meiden.  
**Type** : sort normal  
**Niveau** : 9  
**Rang** : 5  
**Composants** : 80 Aura, 3 Aura permanent  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST "Heiliger Boden"`  

## Sog des Lebens

**Description** :  
Ein Druide, den es in die Welt der Geister verschlagen hat, kann mit Hilfe dieses Zaubers Stufe * 5 Gewichtseinheiten in einen Wald auf der materiellen Welt zurückschicken.  
**Type** : sort normal  
**Niveau** : 9  
**Rang** : 7  
**Composants** : 2 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Sog des Lebens" <x> <y> <Einheit-id> [<Einheit-id> ...]`  

## Weg der Bäume

**Description** :  
Große Macht liegt in Orten, an denen das Leben pulsiert. Der Druide kann diese Kraft sammeln und so ein Tor in die Welt der Geistwesen erschaffen. Der Druide kann dann Stufe * 5 Gewichtseinheiten durch das Tor entsenden.  
**Type** : sort normal  
**Niveau** : 9  
**Rang** : 7  
**Composants** : 3 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Weg der Bäume" <Einheit-id> [<Einheit-id> ...]`  

## Éveil des [Ents]

<!-- cspell:disable -->
*Awakening of the Ents (EN), Erwecke Ents (DE)*.
<!-- cspell:enable -->

:   Avec l'aide de ce sort, le druide réveille les Ents endormis dans les forêts de la région de leur sommeil éternel.
    Les créatures sauvages des arbres le rejoindront et l’assisteront, mais après un certain temps, elles retomberont dans le sommeil.

**Type** : sort normal  
**Niveau** : 10  
**Rang** : 5  
**Composants** : 6 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Awakening of the Ents"`  

## Vertrauten rufen

**Description** :  
Einem erfahrenen Druidem wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Druiden anschließen wird.  
**Type** : sort normal  
**Niveau** : 10  
**Rang** : 5  
**Composants** : 100 Aura, 5 Aura permanent  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Vertrauten rufen"`  

## Segne Steinkreis

**Description** :  
Dieses Ritual segnet einen Steinkreis, der zuvor aus Steinen und etwas Holz gebaut werden muss. Die Segnung des Druiden macht aus dem Kreis eine mächtige Stätte magischen Wirkens, die Schutz vor Magie und erhöhte Aura- Regeneration bewirkt. Man sagt, Jungfrauen seien in der Umgebung von Steinkreisen seltsame Wesen begegnet.  
**Type** : sort normal  
**Niveau** : 11  
**Rang** : 5  
**Composants** : 350 Aura, 5 Aura permanent  
**Modificateurs** : *aucun*
**Syntaxe** : `CAST "Segne Steinkreis" <Gebäude-id>`  

## Rindenhaut

**Description** :  
Dieses vor dem Kampf zu zaubernde Ritual gibt den eigenen Truppen einen zusätzlichen Bonus auf ihre Rüstung. Jeder Treffer reduziert die Kraft des Zaubers, so dass der Schild sich irgendwann im Kampf auflösen wird.  
**Type** : sort de pré-combat  
**Niveau** : 12  
**Rang** : 2  
**Composants** : 4 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Rindenhaut"`  

## Hitzeelementar

**Description** :  
Dieses Ritual beschwört wütende Elementargeister der Hitze. Eine Dürre sucht das Land heim. Bäume verdorren, Tiere verenden, und die Ernte fällt aus. Für Tagelöhner gibt es kaum noch Arbeit in der Landwirtschaft zu finden.  
**Type** : sort normal  
**Niveau** : 13  
**Rang** : 5  
**Composants** : 600 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Beschwörung eines Hitzeelementar"`  

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
**Composants** : 250 Aura, 10 Aura permanent, 1 pot de bave de crapaud  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Wurzeln der Magie"`  

## Tor in die Ebene der Hitze

**Description** :  
Dieses mächtige Ritual öffnet ein Tor in die Elementarebene der Hitze. Eine grosse Dürre kommt über das Land. Bauern, Tiere und Pflanzen der Region kämpfen um das nackte Überleben, aber eine solche Dürre überlebt wohl nur die Hälfte aller Lebewesen. Der Landstrich kann über Jahre hinaus von den Folgen einer solchen Dürre betroffen sein.  
**Type** : sort normal  
**Niveau** : 17  
**Rang** : 5  
**Composants** : 800 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Tor in die Ebene der Hitze"`  

<!-- From [https://wiki.eressea.de/index.php?title=Gwyrrdzauber&oldid=7693] -->

[Ents]: ./monsters.md#ents "Ents"
[eau de vie]: ./alchemy.md#eau-de-vie "Water of life"
[bois]: ./resources.md#bois "Wood"
[fer]: ./resources.md#fer "Iron"
[pierre]: ./resources.md#pierre "Stone"
