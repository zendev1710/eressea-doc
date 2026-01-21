---
# cSpell:locale fr
alias: sorts-tybied
---
# Sorts Tybied

Les sorts de l'École de magie **Tybied** sont décrits ci-dessous par ordre de niveau croissant.

## Analyze de la Magie

<!-- cspell:disable -->
*Analyze Magic (EN), Magie analysieren (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au mage de tenter de détecter les enchantements d'un seul objet spécifié.
    Il pourra se faire une idée de leur efficacité grâce à tous les sorts qui ne dépassent pas ses propres capacités.
    Avec des sorts plus puissants, il lui faut un peu de chance pour réussir son analyse.

**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Magie analysieren" ( REGION | UNIT <Unit-id> [<Unit-id> ...] | SCHIFF <Schiff-id> | BURG <building-id> )`  

## Dissimulation d'aura

<!-- cspell:disable -->
*Concealing Aura (EN), Schleieraura (DE)*.
<!-- cspell:enable -->

:   Ce sort masquera tout l'équipement de l'unité cible pendant un certain temps.

**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Concealing Aura" <unit-id>`  

## Wunderdoktor

**Description** :  
Wenn einem der Alchemist nicht weiterhelfen kann, geht man zu dem gelehrten Tybiedmagier. Seine Tränke und Tinkturen helfen gegen alles, was man sonst nicht bekommen kann. Ob nun die kryptische Formel unter dem Holzschuh des untreuen Ehemannes wirklich geholfen hat - nun, der des Lesens nicht mächtige Bauer wird es nie wissen. Dem Magier hilft es auf jeden Fall... beim Füllen seines Geldbeutels. 50 Silber pro Stufe lassen sich so in einer Woche verdienen.  
**Type** : sort normal  
**Niveau** : 1  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Wunderdoktor"`  

## Schutz vor Magie

**Description** :  
Dieser Zauber legt ein antimagisches Feld um die Magier der Feinde und behindert ihre Zauber erheblich. Nur wenige werden die Kraft besitzen, das Feld zu durchdringen und ihren Truppen in der Schlacht zu helfen.  
**Type** : sort de pré-combat  
**Niveau** : 2  
**Rang** : 2  
**Composants** : 3 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Schutz vor Magie"`  

## Beute Bewahren

**Description** :  
Dieser Zauber verhindert, dass ein Teil der sonst im Kampf zerstörten Gegenstände beschädigt wird. Die Verluste reduzieren sich um 5% pro Stufe des Zaubers bis zu einem Minimum von 25%.  
**Type** : sort de post-combat  
**Niveau** : 3  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Beute Bewahren"`  

## Schutzzauber

**Description** :  
Dieser Zauber verstärkt die natürliche Widerstandskraft gegen Magie. Eine so geschützte Unit ist auch gegen Kampfmagie weniger empfindlich. Pro Stufe reicht die Kraft des Magiers aus, um 5 Personen zu schützen.  
**Type** : sort normal  
**Niveau** : 3  
**Rang** : 2  
**Composants** : 5 x N Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Schutzzauber" <Unit-id> [<Unit-id> ...]`  

## Sortie de l'Astral

<!-- cspell:disable -->
*Astral Exit (EN), Astraler Ausgang (DE)*.
<!-- cspell:enable -->

:   Le mage se concentre sur la structure de la réalité et peut ainsi quitter le plan Astral.
    Il peut globalement (Niveau-3)*Envoyer 15 kg par la porte brièvement créée.
    Si le mage est suffisamment expérimenté pour lancer le sort aux niveaux 11 ou plus, il peut forcer d'autres unités à passer à l'autre niveau, même contre leur gré.

**Type** : sort normal  
**Niveau** : 4  
**Rang** : 7  
**Composants** : 2 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Astral Exit" <x> <y> <unit-id> [<unit-id> ...]`  

## Voie de l'Astral

<!-- cspell:disable -->
*Astral Path (EN), Astraler Weg (DE)*.
<!-- cspell:enable -->

:   D'anciennes formules arcaniques permettent au mage de s'envoyer lui-même et les autres dans le plan Astral.
    Le mage peut envoyer 15 kg par la porte brièvement créée.
    Si le mage est suffisamment expérimenté pour lancer le sort aux niveaux 11 ou plus, il peut forcer d'autres unités à passer à l'autre niveau, même contre leur gré.

**Type** : sort normal  
**Niveau** : 4  
**Rang** : 7  
**Composants** : 2 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Astral Path" <unit-id> [<unit-id> ...]`  

## Antimagie

<!-- cspell:disable -->
*Antimagic (EN), Astrale Schwächezone (DE)*.
<!-- cspell:enable -->

:   Avec ce sort le mage peut créer une zone d'affaiblissement Astral, un déséquilibre local dans le champ Astral.
    Cette zone s'efforcera de revenir à l'équilibre.
    Pour ce faire, il supprimera une partie de la force de chaque sort lancé dans cette région et même absorbera complètement les plus faibles.

**Type** : sort normal  
**Niveau** : 5  
**Rang** : 2  
**Composants** : 3 x N Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Antimagic"`  

## Auratransfer

**Description** :  
Mit Hilfe dieses Zauber kann der Magier eigene Aura im Verhältnis 2:1 auf einen anderen Magier des gleichen Magiegebietes oder im Verhältnis 3:1 auf einen Magier eines anderen Magiegebietes übertragen.  
**Type** : sort normal  
**Niveau** : 5  
**Rang** : 1  
**Composants** : 1 Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Auratransfer" <Unit-id> <Aura>`  

## Dévoreur de magie

<!-- cspell:disable -->
*Destroy Magic (EN), Magiefresser (DE)*.
<!-- cspell:enable -->

:   Ce sort permet au mage de dissiper les enchantements sur une unité, un bateau, un bâtiment ou même une région.

**Type** : sort normal  
**Niveau** : 5  
**Rang** : 2  
**Composants** : 4 x N Aura  
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Destroy Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> | CASTLE <building-id> )`  

## Schockwelle

**Description** :  
Dieser Zauber läßt eine Welle aus purer Kraft über die gegnerischen Reihen hinwegfegen. Viele Kämpfer wird der Schock so benommen machen, daß sie für einen kurzen Moment nicht angreifen können.  
**Type** : sort de combat  
**Niveau** : 5  
**Rang** : 5  
**Composants** : N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Schockwelle"`  

## Invocation de l'Astral

<!-- cspell:disable -->
*Astral Call (EN), Astraler Ruf (DE)*.
<!-- cspell:enable -->

:   Un mage qui se trouve dans le plan Astral peut utiliser ce sort pour lui amener d'autres unités.
    Le mage peut (niveau 3)*Envoyer 15 kg par la porte brièvement créée.
    Si le mage est suffisamment expérimenté pour lancer le sort aux niveaux 13 ou plus, il peut forcer d'autres unités à passer à l'autre niveau, même contre leur gré.

**Type** : sort normal  
**Niveau** : 6  
**Rang** : 7  
**Composants** : 2 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Astral Call" <x> <y> <unit-id> [<unit-id> ...]`  

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
Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer unsichtbaren Unit muss jede Person einen Ring tragen.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 50 Aura, 3 000 silver, 1 Aura permanent  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe einen Ring der Unsichtbarkeit"`  

## Dirigeable

<!-- cspell:disable -->
*Airship (EN), Luftschiff (DE)*.
<!-- cspell:enable -->

:   Ces runes magiques font voler un bateau ou une chaloupe pendant une semaine.
    Cela peut alors également être utilisé pour traverser des terres.
    Pour la couleur des runes, une encre spéciale doit être mélangée à partir d'un chou à la crème et d'un cristal de neige.

**Type** : sort normal  
**Niveau** : 6  
**Rang** : 5  
**Composants** : 10 Aura, 1 [gousse], 1 [pétale de cristal de neige]  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Luftschiff" <Schiff-id>`  

## Invocation de la Réalité

<!-- cspell:disable -->
*Call of Reality (EN), Ruf der Realität (DE)*.
<!-- cspell:enable -->

:   Un mage qui se trouve dans le monde matériel peut utiliser ce sort pour invoquer des unités du monde Astral adjacent.
    Si le mage est suffisamment expérimenté pour lancer le sort à des niveaux de 13 ou plus, il peut forcer d'autres unités à entrer dans le monde matériel contre leur gré.

**Type** : sort normal  
**Niveau** : 6  
**Rang** : 7  
**Composants** : 2 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Call of Reality" <unit-id> [<unit-id> ...]`  

## Stehle Aura

**Description** :  
Mit Hilfe dieses Zaubers kann der Magier einem anderen Magier seine Aura gegen dessen Willen entziehen und sich selber zuführen.  
**Type** : sort normal  
**Niveau** : 6  
**Rang** : 3  
**Composants** : 2 x N Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Stehle Aura" <Unit-id>`  

## Créer un [[antimagic-crystal|Antimagic Crystal]]

<!-- cspell:disable -->
*Create An Antimagic Crystal (EN), Erschaffe Antimagiekristall (DE)*.
<!-- cspell:enable -->

:   À l'aide de ce sort, le mage draine un cristal de quartz de toutes ses énergies magiques.
    Le cristal, une fois broyé en une fine poussière et dispersé, absorbera les énergies magiques libérées lors du lancement et réduira la puissance de tous les sorts lancés dans la région cette semaine-là.

**Type** : sort normal  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 50 Aura, 3 000 silver  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Create An Antimagic Crystal"`  

## Fluch brechen

**Description** :  
Dieser Zauber ermöglicht dem Magier, gezielt eine bestimmte Verzauberung einer Unit, eines Schiffes, Gebäudes oder auch der Region aufzulösen.  
**Type** : sort normal  
**Niveau** : 7  
**Rang** : 3  
**Composants** : 3 x N Aura  
**Modificateurs** : sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Fluch brechen" ( REGION | UNIT <Unit-id> | SCHIFF <Schiff-id> | BURG <building-id> ) <Zauber-ID>`  

## Murs d'éternité

<!-- cspell:disable -->
*Eternal Walls (EN), Mauern der Ewigkeit (DE)*.
<!-- cspell:enable -->

:   Avec cette formule, le mage lie pour toujours les forces de la terre dans les murs du bâtiment.
    Un bâtiment ainsi enchanté est protégé contre les agressions du temps et ne nécessite plus aucun entretien.

**Type** : sort normal  
**Niveau** : 7  
**Rang** : 5  
**Composants** : 50 Aura, 1 Aura permanent  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Eternal Walls" <building-id>`  

## Runen des Schutzes

**Description** :  
Zeichnet man diese Runen auf die Wände eines Gebäudes oder auf die Planken eines Schiffes, so wird es schwerer durch Zauber zu beeinflussen sein. Jedes Ritual erhöht die Widerstandskraft des Gebäudes oder Schiffes gegen Verzauberung um 20%. Werden mehrere Schutzzauber übereinander gelegt, so addiert sich ihre Wirkung, doch ein hundertprozentiger Schutz läßt sich so nicht erreichen. Der Zauber hält mindestens drei Wochen an, je nach Talent des Magiers aber auch viel länger.  
**Type** : sort normal  
**Niveau** : 8  
**Rang** : 2  
**Composants** : 20 Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST "Runen des Schutzes" ( SCHIFF <Schiff-id> | BURG <building-id> )`  

## Schild des Fisches

**Description** :  
Dieser Zauber vermag dem Gegner ein geringfügig versetztes Bild der eigenen Truppen vorzuspiegeln, so wie der Fisch im Wasser auch nicht dort ist wo er zu sein scheint. Von jedem Treffer kann so die Hälfte des Schadens unschädlich abgeleitet werden. Doch hält der Schild nur einige Hundert Schwerthiebe aus, danach wird er sich auflösen. Je stärker der Magier, desto mehr Schaden hält der Schild aus.  
**Type** : sort de pré-combat  
**Niveau** : 8  
**Rang** : 2  
**Composants** : 4 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Schild des Fisches"`  

## Accélération

<!-- cspell:disable -->
*Acceleration (EN), Beschleunigung (DE)*.
<!-- cspell:enable -->

:   Ce sort accélère certains combattants de votre côté afin qu'ils puissent attaquer deux fois en un seul round de combat, tout au long du combat.  

**Type** : sort de pré-combat  
**Niveau** : 9  
**Rang** : 5  
**Composants** : 5 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Beschleunigung"`  

## Erschaffe einen Ring der Macht

**Description** :  
Dieses mächtige Ritual erschafft einen Ring der Macht. Ein Ring der Macht erhöht die Stärke jedes Zaubers, den sein Träger zaubert, als wäre der Magier eine Stufe besser.  
**Type** : sort normal  
**Niveau** : 9  
**Rang** : 5  
**Composants** : 100 Aura, 1 Aura permanent, 4 000 silver  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe einen Ring der Macht"`  

## Blick in die Realität

**Description** :  
Der Magier kann mit Hilfe dieses Zaubers aus der Astral- in die materielle Ebene blicken und die Regionen und Einheiten genau erkennen.  
**Type** : sort normal  
**Niveau** : 10  
**Rang** : 5  
**Composants** : 40 Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST "Blick in die Realität"`  

## Erschaffe einen Beutel des Negativen Gewichts

**Description** :  
Dieser Beutel umschließt eine kleine Dimensionsfalte, in der bis zu 200 Gewichtseinheiten transportiert werden können, ohne dass sie auf das Traggewicht angerechnet werden. Pferde und andere Lebewesen sowie besonders sperrige Dinge (Wagen und Katapulte) können nicht in dem Beutel transportiert werden. Auch ist es nicht möglich, einen Zauberbeutel in einem anderen zu transportieren. Der Beutel selber wiegt 1 kg.  
**Type** : sort normal  
**Niveau** : 10  
**Rang** : 5  
**Composants** : 30 Aura, 1 Aura permanent, 5 000 silber  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST "Erschaffe einen Beutel des Negativen Gewichts"`  

## Zeitdehnung

**Description** :  
Diese praktische Anwendung des theoretischen Wissens um Raum und Zeit ermöglicht es, den Zeitfluß für einige Personen zu verändern. Auf diese Weise veränderte Personen bekommen für einige Wochen doppelt soviele Bewegungspunkte und doppelt soviele Angriffe pro Runde.  
**Type** : sort normal  
**Niveau** : 11  
**Rang** : 5  
**Composants** : 5 x N Aura  
**Modificateurs** : sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Zeitdehnung" <Unit-id> [<Unit-id> ...]`  

## Rüstschild

**Description** :  
Diese vor dem Kampf zu zaubernde Ritual gibt den eigenen Truppen einen zusätzlichen Bonus auf ihre Rüstung. Jeder Treffer reduziert die Kraft des Zaubers, so dass der Schild sich irgendwann im Kampf auflösen wird.  
**Type** : sort de pré-combat  
**Niveau** : 12  
**Rang** : 2  
**Composants** : 4 x N Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Rüstschild"`  

## Vertrauten rufen

**Description** :  
Einem erfahrenen Magier wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Magier anschließen wird.  
**Type** : sort normal  
**Niveau** : 12  
**Rang** : 5  
**Composants** : 100 Aura, 5 Aura permanent  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST "Vertrauten rufen"`  

## Belebtes Gestein

**Description** :  
Dieses kräftezehrende Ritual beschwört mit Hilfe einer Kugel aus konzentriertem Laen einen gewaltigen Erdelementar und bannt ihn in ein building. Dem Elementar kann dann befohlen werden, das building mitsamt aller Bewohner in eine Nachbarregion zu tragen. Die Stärke des beschworenen Elementars hängt vom Talent des Magiers ab: Der Elementar kann maximal [Stufe-12]\*250 Größeneinheiten große building versetzen. Das building wird diese Prozedur nicht unbeschädigt überstehen.  
**Type** : sort normal  
**Niveau** : 13  
**Rang** : 5  
**Composants** : 10 x N Aura, 1 Aura permanent, 5 [laen]  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Belebtes Gestein" <building-id> <direction>`  

## Störe Astrale Integrität

**Description** :  
Dieser Zauber bewirkt eine schwere Störung des Astralraums. Innerhalb eines astralen Radius von Stufe/5 Regionen werden alle Astralwesen, die dem Zauber nicht wiederstehen können, aus der astralen Ebene geschleudert. Der astrale Kontakt mit allen betroffenen Regionen ist für Stufe/3 Wochen gestört.  
**Type** : sort normal  
**Niveau** : 14  
**Rang** : 4  
**Composants** : 140 Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Störe Astrale Integrität"`  

## Opfere Kraft

**Description** :  
Mit Hilfe dieses Zaubers kann der Magier einen Teil seiner magischen Kraft permanent auf einen anderen Magier übertragen. Auf einen Tybied-Magier kann er die Hälfte der eingesetzten Kraft übertragen, auf einen Magier eines anderen Gebietes ein Drittel.  
**Type** : sort normal  
**Niveau** : 15  
**Rang** : 1  
**Composants** : 100 Aura  
**Modificateurs** : *aucun*  
**Syntaxe** : `CAST "Opfere Kraft" <Unit-id> <Aura>`  

<!-- From [https://wiki.eressea.de/index.php?title=Tybiedzauber&oldid=7486] -->

[gousse]: ./herbs.fr.md#gousse "Windbag"
[pétale de cristal de neige]: ./herbs.fr.md#petale-de-cristal-de-neige "Snowcrystal petal"
[laen]: ./resources.md#laen "Laen"
