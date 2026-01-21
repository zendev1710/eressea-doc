---
# cSpell:locale fr
alias: sorts-cerddor
---
# Sorts Cerddor

Les sorts de l'École de magie **Cerddor** sont décrits ci-dessous par ordre de niveau croissant.

## Chant apaisant

<!-- cspell:disable -->
*Appeasing Song (EN), Friedenslied (DE)*.
<!-- cspell:enable -->

:   Cette chanson apprivoise même l'orque le plus sauvage et le rend paisible et doux.
    Toute idée de nuire au chanteur disparaîtra.
    Le mage peut se déplacer sans encombre dans une région voisine.

**Type**: sort de pré-combat  
**Niveau** : 1  
**Rang**: 5  
**Composants** : 2 Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Appeasing Song"`  

## Gaukeleien

**Description**:  
Cerddormagier sind \_die\_ Gaukler unter den Magiern, sie lieben es das Volk zu unterhalten und im Mittelpunkt zu stehen. Schon Anfänger lernen die kleinen Kunststücke und magischen Tricks, mit denen man das Volk locken und verführen kann, den Geldbeutel ganz weit zu öffnen, und am Ende der Woche wird der Gaukler 50 silver pro Stufe verdient haben.  
**Type**: sort normal  
**Niveau** : 1  
**Rang**: 5  
**Composants** : N Aura  
**Modificateurs**: sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Gaukeleien"`  

## Hohes Lied der Gaukelei

**Description**:  
Dieser fröhliche Gesang wird sich wie ein Gerücht in der Region ausbreiten und alle Welt in Feierlaune versetzen. Überall werden Tavernen und Theater gut gefüllt sein und selbst die Bettler satt werden.  
**Type**: sort normal  
**Niveau** : 2  
**Rang**: 5  
**Composants** : 2 x N Aura  
**Modificateurs**: sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Hohes Lied der Gaukelei"`  

## Lied der Heilung

**Description**:  
Nicht nur der Feldscher kann den Verwundeten einer Schlacht helfen. Die Barden kennen verschiedene Lieder, die die Selbstheilungskräfte des Körpers unterstützen. Dieses Lied vermag Wunden zu schließen, gebrochene Knochen zu richten und selbst abgetrennte Glieder wieder zu regenerieren.  
**Type**: sort de post-combat  
**Niveau** : 2  
**Rang**: 5  
**Composants** : N Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Lied der Heilung"`  

## Gesang der Furcht

**Description**:  
Ein gar machtvoller Gesang aus den Überlieferungen der Katzen, der tief in die Herzen der Feinde dringt und ihnen Mut und Hoffnung raubt. Furcht wird sie zittern lassen und Panik ihre Gedanken beherrschen. Voller Angst werden sie versuchen, den gräßlichen Gesängen zu entrinnen und fliehen.  
**Type**: sort de combat  
**Niveau** : 3  
**Rang**: 5  
**Composants** : N Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Gesang der Furcht"`  

## Regentanz

**Description**:  
Dieses uralte Tanzritual ruft die Kräfte des Lebens und der Fruchtbarkeit. Die Erträge der Bauern werden für einige Wochen deutlich besser ausfallen.  
**Type**: sort normal  
**Niveau** : 3  
**Rang**: 5  
**Composants** : N Aura  
**Modificateurs**: sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Regentanz"`  

## Gesang der Verwirrung

**Description**:  
Aus den uralten Gesängen der Katzen entstammt dieses magisches Lied, welches vor einem Kampfe eingesetzt, einem entscheidende strategische Vorteile bringen kann. Wer unter den Einfluss dieses Gesangs gelangt, der wird seiner Umgebung nicht achtend der Melodie folgen, sein Geist wird verwirrt und sprunghaft plötzlichen Eingebungen nachgeben. So sollen schon einst wohlgeordnete Heere plötzlich ihre Schützen weit vorne und ihre Kavallerie bei den Lagerwachen kartenspielend wiedergefunden haben (oder ihren Anführer schlafend im lange verlassenen Lager, wie es in den Großen Kriegen der Alten Welt wirklich geschehen sein soll).  
**Type**: sort de pré-combat  
**Niveau** : 4  
**Rang**: 5  
**Composants** : 2 x N Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Gesang der Verwirrung"`  

## Gesang des Werbens

**Description**:  
Aus 'Die Gesänge der Alten' von Firudin dem Weisen: 'Diese verführerische kleine Melodie und einige einschmeichelnde Worte überwinden das Misstrauen der Bauern im Nu. Begeistert werden sie sich Euch anschliessen und selbst Haus und Hof in Stich lassen.'  
**Type**: sort normal  
**Niveau** : 4  
**Rang**: 5  
**Composants** : 2 x N Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Gesang des Werbens"`  

### Moulin à paroles

<!-- cspell:disable -->
*Blabbermouth (EN), Plappermaul (DE)*.
<!-- cspell:enable -->

:   L'unité enchantée commence à babiller sans complexe, vous indiquant quelles compétences elle peut exercer, quel type d'objets elle transporte avec elle et si elle est douée en magie, même quels sorts elle peut utiliser.
    Malheureusement, ce sort n'affecte pas la mémoire et, rétrospectivement, elle se rendra compte qu'elle en a trop dit.

**Type**: sort normal  
**Niveau** : 4  
**Rang**: 5  
**Composants** : 10 Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `CAST "Blabbermouth" <unit-id>`  

## Chant de contre

<!-- cspell:disable -->
*Countersong (EN), Bannlied (DE)*.
<!-- cspell:enable -->

:   Ce chant strident résonne sur tout le champ de bataille.
    Les dissonances particulières des mélodies rendent presque impossible aux mages de se concentrer sur leurs sorts.

**Type**: sort de pré-combat  
**Niveau** : 5  
**Rang**: 2  
**Composants** : 5 x N Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Countersong"`  

## Gesang des Auratransfers

**Description**:  
Mit Hilfe dieses Zaubers kann der Magier eigene Aura im Verhältnis 2:1 auf einen anderen Magier des gleichen Magiegebietes übertragen.  
**Type**: sort normal  
**Niveau** : 5  
**Rang**: 1  
**Composants** : 2 Aura  
**Modificateurs**: sort de bateau  
**Syntaxe** : `CAST "Gesang des Auratransfers" <unit-id> <Aura>`  

## Analyse du chant de la Vie

<!-- cspell:disable -->
*Analyze Song of Life (EN), Gesang des Lebens analysieren (DE)*.
<!-- cspell:enable -->

:   Tous les êtres vivants ont leur propre chant de vie.
    Il n’y a pas deux chansons identiques, même si toutes les chansons du même type sont similaires.
    Chaque sort modifie ce chant d'une manière ou d'une autre et se révèle ainsi.
    Ce chant aide à entendre les changements dans le chant de la vie d'une personne qui sont de nature magique.
    Vous pourrez déchiffrer et démasquer tous les enchantements qui ne sont pas plus masqués que vos capacités.

**Type**: sort normal  
**Niveau** : 5  
**Rang**: 5  
**Composants** : 10 Aura  
**Modificateurs**: sort de bateau  
**Syntaxe** : `CAST "Gesang des Lebens analysieren" <unit-id>`  

## Chant des héros

<!-- cspell:disable -->
*Epic Heroes (EN), Heldengesang (DE)*.
<!-- cspell:enable -->

:   Cet ancien chant de bataille remonte le moral de vos troupes et les aide également à résister à l'aura effrayante des êtres démoniaques et morts-vivants.
Un guerrier aussi solide ne fuira pas même dans des situations difficiles et son comportement réfléchi lui donnera de nombreux avantages en défense.

**Type**: sort de pré-combat  
**Niveau** : 5  
**Rang**: 4  
**Composants** : 2 x N Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Epic Heroes"`  

## Créer une [[amulet-of-true-sight|Amulet of True Sight]]

<!-- cspell:disable -->
*Create An Amulet of True Sight (EN), Erschaffe ein Amulett des wahren Sehens (DE)*.
<!-- cspell:enable -->

:   Le sort permet à un mage de créer une [amulette de vision décuplée].
    L'amulette permet au porteur de voir toutes les unités protégées par un anneau d'invisibilité.
    Cependant, les unités qui utilisent leur compétence de [camouflage] pour se cacher ne sont toujours pas détectées.

**Type**: sort normal  
**Niveau** : 6  
**Rang**: 5  
**Composants** : 50 Aura, 3 000 silver, 1 Aura permanent  
**Modificateurs**: sort de bateau  
**Syntaxe** : `CAST "Create An Amulet of True Sight"`  

## Erschaffe einen Ring der Unsichtbarkeit

**Description**:  
Mit diesem Spruch kann der Zauberer einen Ring der Unsichtbarkeit erschaffen. Der Träger des Ringes wird für alle Einheiten anderer Parteien unsichtbar, egal wie gut ihre Wahrnehmung auch sein mag. In einer unsichtbaren unit muss jede Person einen Ring tragen.  
**Type**: sort normal  
**Niveau** : 6  
**Rang**: 5  
**Composants** : 50 Aura, 3 000 silver, 1 Aura permanent  
**Modificateurs**: sort de bateau  
**Syntaxe** : `CAST "Erschaffe einen Ring der Unsichtbarkeit"`  

## Lied der Verführung

**Description**:  
Mit diesem Lied kann eine unit derartig betört werden, so dass sie dem Barden den größten Teil ihres Bargelds und ihres Besitzes schenkt. Sie behält jedoch immer soviel, wie sie zum Überleben braucht.  
**Type**: sort normal  
**Niveau** : 6  
**Rang**: 5  
**Composants** : 12 Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `CAST "Lied der Verführung" <unit-id>`  

## Monstres paisibles

<!-- cspell:disable -->
*Calm Monster (EN), Monster friedlich stimmen (DE)*.
<!-- cspell:enable -->

:   Cette chanson mélodieuse peut apprivoiser presque n'importe quel monstre intelligent.
    Il s'abstiendra d'attaquer le mage et ne touchera pas ses compagnons.
    Mais ne vous y trompez pas, il restera toujours une créature imprévisible.

**Type**: sort normal  
**Niveau** : 6  
**Rang**: 5  
**Composants** : 15 Aura  
**Modificateurs**: sort de bateau  
**Syntaxe** : `CAST "Calm Monster" <unit-id>`  

## Aushorchen

**Description**:  
Erliegt die unit dem Zauber, so wird sie dem Magier alles erzählen, was sie über die gefragte Region weiß. Ist in der Region niemand ihrer Partei, so weiß sie nichts zu berichten. Auch kann sie nur das erzählen, was sie selber sehen könnte.  
**Type**: sort normal  
**Niveau** : 7  
**Rang**: 5  
**Composants** : 4 Aura, 100 silver  
**Modificateurs**: *aucun*  
**Syntaxe** : `CAST "Aushorchen" <unit-id> <x> <y>`  

## Kriegsgesang

**Description**:  
Wie viele magischen Gesänge, so entstammt auch dieser den altem Wissen der Katzen, die schon immer um die machtvolle Wirkung der Stimme wussten. Mit diesem Lied wird die Stimmung der Krieger aufgepeitscht, sie gar in wilde Raserrei und Blutrausch versetzt. Ungeachtet eigener Schmerzen werden sie kämpfen bis zum Tode und niemals fliehen. Während ihre Attacke verstärkt ist achten sie kaum auf sich selbst.  
**Type**: sort de pré-combat  
**Niveau** : 7  
**Rang**: 4  
**Composants** : 5 x N Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Kriegsgesang"`  

### Gueule de bois

<!-- cspell:disable -->
*Hangover (EN), Schaler Wein (DE)*.
<!-- cspell:enable -->
<!-- TODO: trématode à nœuds ??? c'est quoi ? -->
:   Enregistrement de la conférence de Selen Ard'Ragorn à Bar'Glingal :
« On dit que ce dicton trouve son origine dans les tavernes des rues de l'Ouest, mais il pourrait tout aussi bien provenir de n'importe quel autre quartier peu recommandable.
Son ingrédient le plus important est un tonneau du pire vin; plus l'essence est bon marché et malsaine, plus elle est puissante.
L'art de distiller ce vin jusqu'à son essence pure, bien plus exigeant qu'un simple mélange de recettes d'alchimiste,
et de le lier et de le conserver de telle manière qu'il ne s'évapore pas immédiatement comme c'est sa nature, oui, c'est quelque chose que seul un maître du Cerddor peut accomplir.
Vous possédez désormais une fiole contenant un reflet rouge rubis – enfin, pas liquide, mais pas vraiment de brume non plus – appelons-le simplement un élixir.
Mais ce n’est pas là le véritable défi; comme son effet se dissipe rapidement, il faut le glisser discrètement dans la boisson de la victime au bout de quelques jours.
Vous, maîtres de la tromperie et de la séduction, voici votre chance de véritablement démontrer votre art.
Mais attention, ne goûtez pas vous-même l'élixir de manière imprudente, car celui qui l'a goûté ne pourra jamais renoncer au vin et en boira sûrement pendant une semaine entière.
Cependant, le véritable danger inhérent à l’élixir n’est pas la tentation de boire, mais plutôt le fait que l’ivresse soit suivie aussi sûrement que le jour après la nuit d’un mal de tête vraiment terrible.
Et il aura presque certainement oublié certaines de ses meilleures capacités pendant quelques jours, voire deux semaines d'études.
Un dernier mot d'avertissement : cela prend beaucoup de temps, et si vous souhaitez lancer d'autres sorts dans la même semaine, ils seront plus difficiles pour vous. »

**Type**: sort normal  
**Niveau** : 7  
**Rang**: 5  
**Composants** : 28 Aura, 3 trématode à nœuds, 50 silver  
**Modificateurs**: *aucun*  
**Syntaxe** : `CAST "Hangover" <unit-id>`  

## Gesang der Angst

**Description**:  
Dieser Kriegsgesang sät Panik in der Front der Gegner und schwächt so ihre Kampfkraft erheblich. Angst wird ihren Schwertarm schwächen und Furcht ihren Schildarm lähmen.  
**Type**: sort de pré-combat  
**Niveau** : 8  
**Rang**: 5  
**Composants** : 5 x N Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Gesang der Angst"`  

## Lebenslied festigen

**Description**:  
Jede Verzauberung beeinflußt das Lebenslied, schwächt und verzerrt es. Der kundige Barde kann versuchen, das Lebenslied aufzufangen und zu verstärken und die Veränderungen aus dem Lied zu tilgen.  
**Type**: sort normal  
**Niveau** : 8  
**Rang**: 2  
**Composants** : 5 x N Aura  
**Modificateurs**: sort à distance, sort de bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Lebenslied festigen" ( REGION | UNIT <unit-id> [<unit-id> ...] | SCHIFF <Schiff-id> | BURG <Gebäude-id> )`  

## Analyses

<!-- cspell:disable -->
*Analysis (EN), Lied des Ortes analysieren (DE)*.
<!-- cspell:enable -->

:   Comme les êtres vivants, les bateaux, les bâtiments et même les régions ont leur propre chant, bien que beaucoup plus faible et plus difficile à entendre.
    Et tout comme le chant de la vie d'une personne permet de savoir si elle est sous le charme, cela est également possible pour les châteaux, les bateaux ou les régions.

**Type**: sort normal  
**Niveau** : 8  
**Rang**: 5  
**Composants** : 3 x N Aura  
**Modificateurs**: sort de bateau  
**Syntaxe** : `CAST [LEVEL n] "Lied des Ortes analysieren" ( REGION | UNIT <unit-id> [<unit-id> ...] | SCHIFF <Schiff-id> | BURG <Gebäude-id> )`  

## Ritual der Aufnahme

**Description**:  
Dieses Ritual ermöglicht es, eine unit, egal welcher Type, in die eigene Partei aufzunehmen. Der um Aufnahme Bittende muss dazu willig und bereit sein, seiner alten Partei abzuschwören. Dies bezeugt er durch KONTAKTIEREN des Magiers. Auch wird er die Woche über ausschliesslich mit Vorbereitungen auf das Ritual beschäftigt sein. Das Ritual wird fehlschlagen, wenn er zu stark an seine alte Partei gebunden ist, dieser etwa Dienst für seine teuere Ausbildung schuldet. Der das Ritual leitende Magier muss für die permanente Bindung des Aufnahmewilligen an seine Partei naturgemäß auch permanente Aura aufwenden. Pro Stufe und pro 1 permanente Aura kann er eine Person aufnehmen.  
**Type**: sort normal  
**Niveau** : 9  
**Rang**: 5  
**Composants** : 3 x N Aura, N Aura permanents  
**Modificateurs**: *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Ritual der Aufnahme" <unit-id>`  

## Vertrauten rufen

**Description**:  
Einem erfahrenen Magier wird irgendwann auf seinen Wanderungen ein ungewöhnliches Exemplar einer Gattung begegnen, welches sich dem Magier anschließen wird.  
**Type**: sort normal  
**Niveau** : 9  
**Rang**: 5  
**Composants** : 100 Aura, 5 Aura permanents  
**Modificateurs**: *aucun*  
**Syntaxe** : `CAST "Vertrauten rufen"`  

## Gesang des wachen Geistes

**Description**:  
Dieses magische Lied wird, einmal mit Inbrunst gesungen, sich in der Region fortpflanzen, von Mund zu Mund springen und eine Zeitlang überall zu vernehmen sein. Nach wie vielen Wochen der Gesang aus dem Gedächnis der Region entschwunden ist, ist von dem Geschick des Barden abhängig. Bis das Lied ganz verklungen ist, wird seine Magie allen Verbündeten des Barden (HELP GUARD), und natürlich auch seinen eigenem Volk, einen einmaligen Bonus von 15% auf die natürliche Widerstandskraft gegen eine Verzauberung verleihen.  
**Type**: sort normal  
**Niveau** : 10  
**Rang**: 2  
**Composants** : 2 x N Aura  
**Modificateurs**: sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Gesang des wachen Geistes"`  

## Mob aufwiegeln

**Description**:  
Mit Hilfe dieses magischen Gesangs überzeugt der Magier die Bauern der Region, sich ihm anzuschließen. Die Bauern werden ihre Heimat jedoch nicht verlassen, und keine ihrer Besitztümer fortgeben. Jede Woche werden zudem einige der Bauern den Bann abwerfen und auf ihre Felder zurückkehren. Wie viele Bauern sich dem Magier anschließen hängt von der Kraft seines Gesangs ab.  
**Type**: sort normal  
**Niveau** : 10  
**Rang**: 5  
**Composants** : 4 x N Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Mob aufwiegeln"`  

## Gesang der Melancholie

**Description**:  
Mit diesem Gesang verbreitet der Barde eine melancholische, traurige Stimmung unter den Bauern. Einige Wochen lang werden sie sich in ihre Hütten zurückziehen und kein silver in den Theatern und Tavernen lassen.  
**Type**: sort normal  
**Niveau** : 11  
**Rang**: 5  
**Composants** : 40 Aura  
**Modificateurs**: sort à distance  
**Syntaxe** : `CAST [REGION x y] "Gesang der Melancholie"`  

## Miriams flinke Finger

**Description**:  
Die berühmte Bardin Miriam bhean'Meddaf war bekannt für ihr außergewöhnliches Geschick mit der Harfe. Ihre Finger sollen sich so schnell über die Saiten bewegt haben, das sie nicht mehr erkennbar waren. Dieser Zauber, der recht einfach in einen Silberring zu bannen ist, bewirkt eine um das zehnfache verbesserte Geschicklichkeit und Gewandheit der Finger. (Das soll sie auch an anderer Stelle ausgenutzt haben, ihr Ruf als Falschspielerin war berüchtigt). Handwerker können somit das zehnfache produzieren, und bei einigen anderen Tätigkeiten könnte dies ebenfalls von Nutzen sein.  
**Type**: sort normal  
**Niveau** : 11  
**Rang**: 5  
**Composants** : 20 Aura, 1 000 silver, 1 Aura permanent  
**Modificateurs**: sort de bateau  
**Syntaxe** : `CAST "Miriams flinke Finger"`  

## Gesang der Friedfertigkeit

**Description**:  
Dieser mächtige Bann verhindert jegliche Attacken. Niemand in der ganzen Region ist fähig seine Waffe gegen irgendjemanden zu erheben. Die Wirkung kann etliche Wochen andauern.  
**Type**: sort normal  
**Niveau** : 12  
**Rang**: 5  
**Composants** : 20 x N Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Gesang der Friedfertigkeit"`  

## Gesang des schwachen Geistes

**Description**:  
Dieses Lied, das in die magische Essenz der Region gewoben wird, schwächt die natürliche Widerstandskraft gegen eine Verzauberung einmalig um 15%. Nur die Verbündeten des Barden (HELP GUARD) sind gegen die Wirkung des Gesangs gefeit.  
**Type**: sort normal  
**Niveau** : 12  
**Rang**: 2  
**Composants** : 2 x N Aura  
**Modificateurs**: sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Gesang des schwachen Geistes"`  

## Gesang der Versklavung

**Description**:  
Dieser mächtige Bann raubt dem Opfer seinen freien Willen und unterwirft sie den Befehlen des Barden. Für einige Zeit wird das Opfer sich völlig von seinen eigenen Leuten abwenden und der Partei des Barden zugehörig fühlen.  
**Type**: sort normal  
**Niveau** : 13  
**Rang**: 5  
**Composants** : 40 Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `CAST "Gesang der Versklavung" <unit-id>`  

## Hohe Kunst der Überzeugung

**Description**:  
Aus 'Wanderungen' von Firudin dem Weisen: 'In Weilersweide, nahe dem Wytharhafen, liegt ein kleiner Gasthof, der nur wenig besucht ist. Niemanden bekannt ist, das dieser Hof bis vor einigen Jahren die Bleibe des verbannten Wanderpredigers Grauwolf war. Nachdem er bei einer seiner berüchtigten flammenden Reden fast die gesammte Bauernschaft angeworben hatte, wurde er wegen Aufruhr verurteilt und verbannt. Nur zögerlich war er bereit mir das Geheimniss seiner Überzeugungskraft zu lehren.'  
**Type**: sort normal  
**Niveau** : 14  
**Rang**: 5  
**Composants** : 20 x N Aura  
**Modificateurs**: *aucun*  
**Syntaxe** : `CAST [LEVEL n] "Hohe Kunst der Überzeugung"`  

## Aufruhr beschwichtigen

**Description**:  
Mit Hilfe dieses magischen Gesangs kann der Magier eine Region in Aufruhr wieder beruhigen. Die Bauernhorden werden sich verlaufen und wieder auf ihre Felder zurückkehren.  
**Type**: sort normal  
**Niveau** : 15  
**Rang**: 5  
**Composants** : 30 Aura  
**Modificateurs**: sort à distance  
**Syntaxe** : `CAST [REGION x y] "Aufruhr beschwichtigen"`  

## Aufruhr verursachen

**Description**:  
Mit Hilfe dieses magischen Gesangs versetzt der Magier eine ganze Region in Aufruhr. Rebellierende Bauernhorden machen jedes Besteuern unmöglich, kaum jemand wird mehr für Gaukeleien Geld spenden und es können keine neuen Leute angeworben werden. Nach einigen Wochen beruhigt sich der Mob wieder.  
**Type**: sort normal  
**Niveau** : 16  
**Rang**: 5  
**Composants** : 40 Aura  
**Modificateurs**: sort à distance  
**Syntaxe** : `CAST [REGION x y] "Aufruhr verursachen"`  

<!-- From [https://wiki.eressea.de/index.php?title=Cerddorzauber&oldid=7018] -->

[amulette de vision décuplée]: ./amulet-of-true-sight.md
[camouflage]: ./camouflage.md
