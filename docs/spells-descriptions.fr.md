---
# cSpell:locale fr, en
alias: description-des-sorts
---
# Description des sorts

<!-- cspell:disable -->
<!-- TODO: enable cSpell after descriptions translation -->

## A

### Accélération

<!-- cspell:disable -->
*Acceleration (EN), Beschleunigung (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell speeds up some fighters on your side so that they can attack twice in one combat round throughout the entire combat.
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 5 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Acceleration`  

### Bouclier aérien

<!-- cspell:disable -->
*Air Shield (EN), Windschild (DE)*.
<!-- cspell:enable -->

**Description** :  
Invoking the Elemental Spirits of Wind conjures up sudden gusts of wind, small gusts of wind, and vents that will hinder opposing archers.
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Air Shield"`  

### Dirigeable

<!-- cspell:disable -->
*Airship (EN), Luftschiff (DE)*.
<!-- cspell:enable -->

**Description** :  
These magical runes make a boat or longboat fly for a week. This can then also be used to cross land. For the color of the runes, a special ink must be mixed from a cream puff and a snow crystal.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 10 Aura, 1 Windbeutel, 1 snow crystal  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST Airship <ship-id>`  

### Analyses

<!-- cspell:disable -->
*Analysis (EN), Lied des Ortes analysieren (DE)*.
<!-- cspell:enable -->

**Description** :  
Like living things, ships and buildings and even regions have their own song, albeit much fainter and harder to hear. And just as you can tell from a person"s life song whether they are under a spell, this is also possible with castles, ships or regions.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 3 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] "Analysis" ( REGION | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Analyse des rêves

<!-- cspell:disable -->
*Analyse Dreams (EN), Traumbilder analysieren (DE)*.
<!-- cspell:enable -->

**Description** :  
With this spell, the dream weaver can attempt to detect the enchantments of a single unit. He will be able to get an impression of their effectiveness from all spells that do not exceed his own abilities. With stronger spells he needs a little luck for a successful analysis.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 25 Aura  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Analyse Dreams" <unit-id>`  

### Analyze Magic

<!-- cspell:disable -->
*Analyze Magic (EN), Magie analysieren (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell allows the magician to attempt to detect the enchantments of a single specified object. He will be able to get an impression of their effectiveness from all spells that do not exceed his own abilities. With stronger spells he needs a little luck for a successful analysis.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] "Analyze Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Analyse du chant de la Vie

<!-- cspell:disable -->
*Analyze Song of Life (EN), Gesang des Lebens analysieren (DE)*.
<!-- cspell:enable -->

**Description** :  
All living beings have their own individual life song. No two songs are alike, even if all songs of the same type are similar. Each spell changes this song in one way or another and thus reveals itself. This chant helps to hear those changes in a person"s life song that are magical in nature. You will be able to decipher and unmask all enchantments that are not more masked than your ability.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 10 Aura  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Analyze Song of Life" <unit-id>`  

### Pouvoirs des morts

<!-- cspell:disable -->
*Animate Dead (EN), Mächte des Todes (DE)*.
<!-- cspell:enable -->

**Description** :  
The black magician has to spend nights wandering through the cemeteries and burial grounds of the region in order to be able to revive the unearthed corpses. The undead will be at his service, but the uninformed be warned that summoning the forces of death can be a double-edged sword.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 5 Aura x Niveau  
**Modificateurs** : sort à distance, sort sur bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Animate Dead"`  

### Antimagie

<!-- cspell:disable -->
*Antimagic (EN), Astrale Schwächezone (DE)*.
<!-- cspell:enable -->

**Description** :  
With this spell the magician can create a zone of astral weakening, a local imbalance in the astral field. This zone will strive to return to equilibrium. To do this, it will remove part of the strength of every spell cast in this region and even completely absorb the weaker ones.
**Type** : sort normal  
**Rang** : 2  
**Composants** : 3 Aura x Niveau  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Antimagic"`  

### Chant apaisant

<!-- cspell:disable -->
*Appeasing Song (EN), Friedenslied (DE)*.
<!-- cspell:enable -->

**Description** :  
This song tames even the wildest orc and makes him peaceful and gentle. Any thought of harming the singer will disappear. The magician can move to a neighboring region unmolested.
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 2 Aura  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Appeasing Song"`  

### Invocation de l'Astral

<!-- cspell:disable -->
*Astral Call (EN), ;Astraler Ruf (DE)*.
<!-- cspell:enable -->

**Description** :  
A magician who is in the astral plane can use this spell to bring other units to him. The magician can (level 3)*Send 15 kg through the briefly created gate. If the magician is experienced enough to cast the spell at levels 13 or more, he can force other units to the other level even against their will.
**Type** : sort normal  
**Rang** : 7  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Astral Call" <x> <y> <unit-id> [<unit-id> ...]`  

### Chaos de l'Astral

<!-- cspell:disable -->
*Astral Chaos (EN), Astrales Chaos (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual, performed before battle, swirls the Astral energies on the battlefield, making it more difficult for enemy magicians to cast their spells.
**Type** : sort de pré-combat  
**Rang** : 2  
**Composants** : 6 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Astral Chaos"`  

### Sortie de l'Astral

<!-- cspell:disable -->
*Astral Exit (EN), Astraler Ausgang (DE)*.
<!-- cspell:enable -->

**Description** :  
The magician concentrates on the structure of reality and can thus leave the astral plane. He can overall (Niveau-3)*Send 15 kg through the briefly created gate. If the magician is experienced enough to cast the spell at levels 11 or more, he can force other units to the other level even against their will.
**Type** : sort normal  
**Rang** : 7  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Astral Exit" <x> <y> <unit-id> [<unit-id> ...]`  

### Esprits du Gardien de l'Astral

<!-- cspell:disable -->
*Astral Guardian Spirits (EN), Astralschutzgeister (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual summons some elemental spirits of magic and sends them into the ranks of the enemy mages. These will find it much more difficult to cast spells for the duration of the fight.
**Type** : sort de pré-combat  
**Rang** : 2  
**Composants** : 5 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Astral Guardian Spirits"`  

### Fuite de l'Astral

<!-- cspell:disable -->
*Astral Leak (EN), Astraler Riss (DE)*.
<!-- cspell:enable -->

**Description** :  
With this dark ritual, the black magician can cause a rift in the fabric of magic, which will tear all magical power from the region. All magically gifted people in the region will lose much of their aura.
**Type** : sort normal  
**Rang** : 3  
**Composants** : 35 Aura, 1 Dragonblood  
**Modificateurs** :  
**Syntaxe** : `CAST "Astral Leak"`  

### Voie de l'Astral

<!-- cspell:disable -->
*Astral Path (EN), Astraler Weg (DE)*.
<!-- cspell:enable -->

**Description** :  
Ancient arcane formulas allow the magician to send himself and others into the astral plane. The magician can (level 3)*Send 15 kg through the briefly created gate. If the magician is experienced enough to cast the spell at levels 11 or more, he can force other units to the other level even against their will.
**Type** : sort normal  
**Rang** : 7  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Astral Path" <unit-id> [<unit-id> ...]`  

### Aufruhr beschwichtigen <!-- TODO -->

<!-- cspell:disable -->
* (EN),  (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this magical chant, the magician can calm a region in turmoil. The hordes of farmers will get lost and return to their fields.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 30 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Aufruhr beschwichtigen"`  

### Aufruhr verursachen <!-- TODO -->

<!-- cspell:disable -->
* (EN),  (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this magical song, the magician puts an entire region in turmoil. Rebellious hordes of farmers make any taxation impossible, hardly anyone will donate money to scams anymore and no new people can be recruited. After a few weeks the mob calms down again.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 40 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Aufruhr verursachen"`  

### Éveil des [Ents]

<!-- cspell:disable -->
*Awakening of the Ents (EN), Erwecke Ents (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this spell, the druid awakens the Ents slumbering in the forests of the region from their eons-long sleep. The wild tree creatures will join him and assist him, but after a while they will fall back into slumber.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 6 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Awakening of the Ents"`  

## B

### Bannissement des Esprits

<!-- cspell:disable -->
*Banish Spirits (EN), Geister bannen (DE)*.
<!-- cspell:enable -->

**Description** :  
According to the ancient teachings of the Druids, what ordinary beings call magic consists of elemental spirits. The magician conjures and banishes these into a form to achieve the desired effect. This ritual is able to drive away elemental spirits that have been summoned into this world in order to free an object from magic.
**Type** : sort normal  
**Rang** : 2  
**Composants** : 6 Aura x Niveau  
**Modificateurs** : sort à distance, sort sur bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Banish Spirits" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Belebtes Gestein <!-- TODO -->

<!-- cspell:disable -->
* (EN), Belebtes Gestein (DE)*.
<!-- cspell:enable -->

**Description** :  
This energy-sapping ritual uses a ball of concentrated Laen to summon a massive earth elemental and banish it to a building. The elemental can then be ordered to carry the building and all its inhabitants to a neighboring region. The strength of the summoned elemental depends on the talent of the magician: the elemental can do maximum[Niveau-12]*Move 250 size units buildings. The building will not survive this procedure unscathed.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 10 Aura x Niveau, 1 aura permanent, 5 Laen  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Belebtes Gestein" <building-id> <Richtung>`  

### Beschwöre Schattenmeister <!-- TODO -->

<!-- cspell:disable -->
* (EN), Beschwöre Schattenmeister (DE)*.
<!-- cspell:enable -->

**Description** :  
Using dark rituals, the magician summons demons from the sphere of shadows. These feared creatures can move almost invisibly among the living, but their dark aura can be felt by everyone. In battle, shadow masters are feared opponents. They are difficult to hit and drain their opponent"s strength and life.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 7 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Beschwöre Schattenmeister"`  

### Moulin à paroles

<!-- cspell:disable -->
*Blabbermouth (EN), Plappermaul (DE)*.
<!-- cspell:enable -->

**Description** :  
The enchanted unit begins to babble uninhibitedly, telling you what talents it can do, what kind of objects it carries with it, and if it is magically gifted, even what spells it can use. Unfortunately, this spell does not affect memory, and so in retrospect she will be aware that she has told too much.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 10 Aura  
**Modificateurs** :  
**Syntaxe** : `CAST Blabbermouth <unit-id>`  

### Bénédiction de la terre

<!-- cspell:disable -->
*Blessed Harvest (EN), Segen der Erde (DE)*.
<!-- cspell:enable -->

**Description** :  
This harvest ritual improves the yields of working farmers in the region by one piece of silver. The more power the druid invests, the longer the spell lasts.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** : sort à distance, sort sur bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Blessed Harvest"`  

### Blick in die Realität <!-- TODO -->

<!-- cspell:disable -->
* (EN), Blick in die Realität (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this spell, the magician can look from the astral plane into the material plane and recognize the regions and units precisely.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 40 Aura  
**Modificateurs** :  
**Syntaxe** : `CAST "Blick in die Realität"`  

### Soif de sang

<!-- cspell:disable -->
*Blood Frenzy (EN), Blutrausch (DE)*.
<!-- cspell:enable -->

**Description** :  
In this bloody ritual, the magician sacrifices a newborn baby in front of his army before battle. The blood spirits summoned in this way will take possession of the soldiers and send them into a bloodlust.
**Type** : sort de pré-combat  
**Rang** : 4  
**Composants** : 5 Aura x Niveau, 1 Bauer  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Blood Frenzy"`  

## C

### Invocation de la Réalité

<!-- cspell:disable -->
*Call of Reality (EN), Ruf der Realität (DE)*.
<!-- cspell:enable -->

**Description** :  
A magician who is in the material world can use this spell to summon units from the adjacent astral world. If the magician is experienced enough to cast the spell at levels of 13 or more, he can force other units into the material world against their will.
**Type** : sort normal  
**Rang** : 7  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Call of Reality" <unit-id> [<unit-id> ...]`  

### Monstres paisibles

<!-- cspell:disable -->
*Calm Monster (EN), Monster friedlich stimmen (DE)*.
<!-- cspell:enable -->

**Description** :  
This mellifluous song can tame almost any intelligent monster. It will refrain from attacking the magician and will not touch its companions. But make no mistake, it will still remain an unpredictable creature.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 15 Aura  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Calm Monster" <unit-id>`  

### Château d'Illusion

<!-- cspell:disable -->
*Castle of Illusion (EN), Traumschlößchen (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this spell, the dream weaver can create the illusion of any building. The illusion can be entered, but is otherwise non-functional and requires no maintenance. It will last for a few weeks.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 3 Aura  
**Modificateurs** :  
**Syntaxe** : `CAST "Castle of Illusion" <Gebäudetyp>`  

### Guérison du bétail

<!-- cspell:disable -->
*Cattle Healing (EN), Viehheilung (DE)*.
<!-- cspell:enable -->

**Description** :  
The Gwyrrd mages" livestock and healing skills are highly sought after by farmers. Their services are often in high demand, especially in markets. Some people may also use their talent to sell an animal for a better price. The magician can earn 50 silver per level.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] "Cattle Healing"`  

### Malédiction du Chaos

<!-- cspell:disable -->
*Chaos Curse (EN), Chaosfluch (DE)*.
<!-- cspell:enable -->

**Description** :  
This insidious curse significantly impairs the victim"s magical abilities. A chaos magic zone around the victim reduces his ability to concentrate and makes it very difficult for him to cast spells.
**Type** : sort normal  
**Rang** : 4  
**Composants** : 4 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Chaos Curse" <unit-id>`  

### Chaos Gift

<!-- cspell:disable -->
*Don du Chaos (EN), Gabe des Chaos (DE)*.
<!-- cspell:enable -->

**Description** :  
The magician opens his mind to the spheres of chaos and will thus have more magical power for some time. But the help of the Lords of the Spheres comes at a price, and so the phase of power is replaced by a phase of weakness.
**Type** : sort normal  
**Rang** : 3  
**Composants** : 6 Aura  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Chaos Gift"`  

### Chaossog <!-- TODO -->

<!-- cspell:disable -->
* (EN), Chaossog (DE)*.
<!-- cspell:enable -->

**Description** :  
By sacrificing 200 pawns, the chaos magician can open a gate to the astral world. The gate can be used the following week, it dissolves at the end of the following week.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 150 Aura, 200 Bauern  
**Modificateurs** :  
**Syntaxe** : `CAST Chaossog`  

### Dissimulation d'aura

<!-- cspell:disable -->
*Concealing Aura (EN), Schleieraura (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell will obscure all of the target unit"s equipment from view for a period of time.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] "Concealing Aura" <unit-id>`  

### Chant de contre

<!-- cspell:disable -->
*Countersong (EN), Bannlied (DE)*.
<!-- cspell:enable -->

**Description** :  
This shrill chant echoes throughout the battlefield. The special dissonances in the melodies make it almost impossible for magicians to concentrate on their spells.
**Type** : sort de pré-combat  
**Rang** : 2  
**Composants** : 5 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Countersong`  

### Créer un [[negative-weight-bag]] <!-- TODO: check -->

<!-- cspell:disable -->
* (EN),  (DE)*.
<!-- cspell:enable -->

**Description** :  
This bag encloses a small dimensional fold in which up to 200 weight units can be transported without being counted towards the carrying weight. Horses and other living creatures as well as particularly bulky items (chariots and catapults) cannot be transported in the bag. It is also not possible to transport one magic bag in another. The bag itself weighs 1 kg.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 30 Aura, 1 aura permanent, 5000 silver  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Create A Bag of Negative Weight"`   <!-- TODO: check -->

### Créer une [[belt-of-troll-strength]]

<!-- cspell:disable -->
*Create A Belt of Troll Strength (EN), Erschaffe einen Gürtel der Trollstärke (DE)*.
<!-- cspell:enable -->

**Description** :  
This magical artifact grants the wearer the strength of a full-grown cave troll. Its carrying capacity increases 50 times and the increased strength and troll-tough skin will also have a positive effect in combat.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 20 Aura, 1 aura permanent  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Create A Belt of Troll Strength"`  

### Créer un [[dreameye]] <!-- TODO: check -->

<!-- cspell:disable -->
* (EN),  (DE)*.
<!-- cspell:enable -->

**Description** :  
A dragon"s eye cast with this spell and consumed at communion allows the user to enter and read another person"s dreams. For a long time, such an ability was considered useless until the former Wood Elf master of battle magic, Liarana Sundew from the Thall Academy, presented a special application: Generals often dream restlessly before major battles and reveal their plans in dreams. This can give the user a huge advantage in the upcoming battle. But be careful: interpreting dreams is a difficult matter.  
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Drachenkopf, 5 aura permanent  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Create A DreamEye"`  

### Crére une [[flaming-sword]]

<!-- cspell:disable -->
* (EN),  (DE)*.
<!-- cspell:enable -->

**Description** :  
"And so rub the blood of a fierce fighter into the steel of the blade and begin the invocation of the Spheres of Chaos. And if you have done everything to please them, they will send one of their own to imbue the sword with his power..."
**Type** : sort normal  
**Rang** : 5  
**Composants** : 100 Aura, 1 Berserkerblut, 1 Schwert, 1 aura permanent  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Create A Flaming Sword"`  

### Créer un [[magical-herb-pouch]]

<!-- cspell:disable -->
* (EN),  (DE)*.
<!-- cspell:enable -->

**Description** :  
The Druid takes some prepared leather, which he cleanses of all unclean spirits in a great ritual of purification, and then binds some small spirits of air and water into the material. He now uses the leather prepared in this way to make a small bag that can better preserve the herbs stored in it.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 30 Aura, 1 aura permanent, 1 water of lifes  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Create A magical Herb Pouch"`

### Créer un [[ring-of-power]]

<!-- cspell:disable -->
* (EN),  (DE)*.
<!-- cspell:enable -->

**Description** :  
This powerful ritual creates a ring of power. A ring of power increases the power of any spell its wearer casts, as if the mage were one level better.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 100 Aura, 1 aura permanent, 4000 silver  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Create A Ring of Power"`  

### Créer un [[ring-of-invisibility]]

<!-- cspell:disable -->
* (EN),  (DE)*.
<!-- cspell:enable -->

**Description** :  
With this spell the wizard can create a ring of invisibility. The bearer of the ring becomes invisible to all units of other parties, no matter how good their perception may be. In an invisible unit, each person must wear a ring.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 50 Aura, 3000 silver, 1 aura permanent  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Create A Ring of Invisibility"`  

### Créer une [[sphere-of-invisibility]]

<!-- cspell:disable -->
* (EN),  (DE)*.
<!-- cspell:enable -->

**Description** :  
With this spell the magician can create a sphere of invisibility. The sphere renders its wielder and ninety-nine other people in the same unit invisible.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 150 Aura, 30000 silver, 3 aura permanent  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Create A Sphere of Invisibility"`  

### Créer une [[amulet-of-true-vision|Amulet of True Sight]]

<!-- cspell:disable -->
* (EN),  (DE)*.
<!-- cspell:enable -->

**Description** :  
The spell allows a magician to create an Amulet of True Sight. The amulet allows the wearer to see all units protected by a ring of invisibility. However, units that use their camouflage talent to hide still remain undetected.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 50 Aura, 3000 silver, 1 aura permanent  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Create An Amulet of True Sight"`  

### Créer un [[antimagic-crystal|Antimagic Crystal]]

<!-- cspell:disable -->
* (EN),  (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this spell, the magician drains a quartz crystal of all its magical energies. The crystal, when ground into a fine dust and dispersed, will absorb the magical energies released during casting and reduce the power of all spells cast in the region that week.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 50 Aura, 3000 silver  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Create An Antimagic Crystal"`  

### Créer des [[iron-golem|Iron Golems]]

<!-- cspell:disable -->
*Create Iron Golems (EN), Erschaffe Eisenolems (DE)*.
<!-- cspell:enable -->

**Description** :  
The more power the magician invests, the more golems can be created. Each golem has a 15 percent chance of turning to dust each round. If you give the golems the order MAKE SWORD/BIHANDER or MAKE SHIELD/CHAIN ​​MAIL/PLATE ARMOR, 4 iron bars are installed per golem and the golem dissolves.
**Type** : sort normal  
**Rang** : 4  
**Composants** : 2 x N Aura, N [fers], 1 [eau de vie]  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Create Iron Golems"`  

### Créer des [[stone-golem|Stone Golems]]

<!-- cspell:disable -->
*Create Stone Golems (EN), Erschaffe Steingolems (DE)*.
<!-- cspell:enable -->

**Description** :  
Moisten a gap-free block of fine crystalline rock with a vial of the water of life until it has been completely absorbed into the rock. Then you direct your strength towards the fine aura of life that is forming and form a housing for the unbound strength. The more power the magician invests, the more golems can be created before the aura dissipates. Each golem has a 10 percent chance of turning to dust each round. If you give the golems the commands MAKE CASTLE or MAKE ROAD, 4 stones are placed per golem and the golem dissolves.  
**Type** : sort normal  
**Rang** : 4  
**Composants** : 2 x N Aura, N [pierres], 1 [eau de vie]  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Create Stone Golems"`  

### Malédiction de la peste

<!-- cspell:disable -->
*Curse of Pestilence (EN), Fluch der Pestilenz (DE)*.
<!-- cspell:enable -->

**Description** :  
In an elaborate ritual, the black magician sacrifices some peasants and then magically distributes the corpses into the region"s wells.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 30 Aura, 50 Bauern  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Curse of Pestilence"`  

## D

### Dévoreur de magie

<!-- cspell:disable -->
*Destroy Magic (EN), Magiefresser (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell allows the magician to dispel enchantments on a unit, ship, building, or even region.
**Type** : sort normal  
**Rang** : 2  
**Composants** : 4 Aura x Niveau  
**Modificateurs** : sort à distance, sort sur bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Destroy Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Divination

<!-- cspell:disable -->
*Divination (EN), Weissagung (DE)*.
<!-- cspell:enable -->

**Description** :  
No one can interpret dreams as well as an Illaun magician. He is also familiar with the art of fortune telling, card reading and palm reading. In return, the farmers pay him 50 silver per level.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] Divination`  

### Drachenruf <!-- TODO -->

<!-- cspell:disable -->
* (EN), Drachenruf (DE)*.
<!-- cspell:enable -->

**Description** :  
With this dark ritual, the magician creates a lure that smells irresistible to [Dragons]. It has not yet been possible to research whether the dragons come from the surrounding area or from the sphere of chaos. Both are said to have already happened. The bait lasts about 6 weeks, but must be placed in kite-friendly terrain.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 80 Aura, 1 Drachenkopf  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] Drachenruf`  

### Rêve de magie

<!-- cspell:disable -->
*Dream of Magic (EN), Traum der Magie (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this spell, the dream weaver can transfer his own aura to another dream weaver at a ratio of 2:1.
**Type** : sort normal  
**Rang** : 1  
**Composants** : 2 Aura  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Dream of Magic" <unit-id> <Aura>`  

### Rêve

<!-- cspell:disable -->
*Dream (EN), Traum (DE)*.
<!-- cspell:enable -->

**Description** :  
The magician sends the target of the spell a dream.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] Dream <unit-id>`  

## E

### Chant des héros

<!-- cspell:disable -->
*Epic Heroes (EN), Heldengesang (DE)*.
<!-- cspell:enable -->

**Description** :  
This ancient battle song raises the morale of your troops and also helps them to resist the frightening aura of demonic and undead beings. Such a solid warrior will not flee even in difficult situations and his considered behavior will give him many an advantage in defense.
**Type** : sort de pré-combat  
**Rang** : 4  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Epic Heroes"`  

### Repos éternel

<!-- cspell:disable -->
*Eternal Rest (EN), Seelenfrieden (DE)*.
<!-- cspell:enable -->

**Description** :  
This magical ritual soothes the tormented souls of those who died violently, allowing them to begin their final journey to the Otherlands. Approximately 50 souls will find peace per level of the spell. The spell cannot redeem the living dead who have already been resurrected because their ties to this world are too strong.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 3 Aura x Niveau, 1 water of lifes  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Eternal Rest"`  

### Murs d'éternité

<!-- cspell:disable -->
*Eternal Walls (EN), Mauern der Ewigkeit (DE)*.
<!-- cspell:enable -->

**Description** :  
With this formula, the magician binds the forces of the earth into the walls of the building forever. A building enchanted in this way is protected against the ravages of time and no longer requires any maintenance.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 50 Aura, 1 aura permanent  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] "Eternal Walls" <building-id>`  

## F

### Feuerteufel <!-- TODO -->

<!-- cspell:disable -->
* (EN), Feuerteufel (DE)*.
<!-- cspell:enable -->

**Description** :  
This elemental invocation summons a fire devil, a creature from the deepest reaches of the flaming hells. The fire devil will eagerly pounce on the region"s forests and set them ablaze.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 50 Aura, 1 Öl  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] Feuerteufel`  

### Boule de feu

<!-- cspell:disable -->
*Fireball (EN), Feuerball (DE)*.
<!-- cspell:enable -->

**Description** :  
The sorcerer hurls focused chaos into the enemy"s ranks. The ball-shaped chaos will wound anyone it hits.
**Type** : Kampfzauber  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Fireball`  

### Mur de feu

<!-- cspell:disable -->
*Firewall (EN), Feuerwand (DE)*.
<!-- cspell:enable -->

**Description** :  
The wizard creates a wall of fire in the specified direction. It hurts everyone who walks through it.
**Type** : sort normal  
**Rang** : 4  
**Composants** : 6 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] Firewall <directoin>`  

### Le manteau de Firun

<!-- cspell:disable -->
*Firun's Coat (EN), Firuns Fell (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell allows the magician to magically protect insects from the crippling cold of the glaciers. You can enter glaciers and act normally there. The saying works on a level*10 insects. A Ring of Power increases the number of enchantable insects by an additional 10.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 2 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] "Firun's Coat" <unit-id> [<unit-id> ...]`  

## G

### Regard du Basilic

<!-- cspell:disable -->
*Gaze of the Basilisk (EN), Blick des Basilisken (DE)*.
<!-- cspell:enable -->

**Description** :  
This difficult but effective combat spell uses the elemental spirits of stone to turn a number of enemies to stone for the duration of the battle. The affected people will no longer fight, but they cannot be wounded either.
**Type** : Kampfzauber  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Gaze of the Basilisk"`  

### Gesang der Friedfertigkeit <!-- TODO -->

<!-- cspell:disable -->
* (EN), Gesang der Friedfertigkeit (DE)*.
<!-- cspell:enable -->

**Description** :  
This powerful spell prevents any attacks. No one in the entire region is capable of taking up arms against anyone. The effects can last for several weeks.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 20 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Gesang der Friedfertigkeit"`  

### Gesang der Melancholie  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Gesang der Melancholie (DE)*.
<!-- cspell:enable -->

**Description** :  
With this song the bard spreads a melancholic, sad mood among the farmers. For a few weeks they will retreat to their huts and leave no silver in the theaters and taverns.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 40 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Gesang der Melancholie"`  

### Gesang der Versklavung  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Gesang der Versklavung (DE)*.
<!-- cspell:enable -->

**Description** :  
This powerful spell robs the victim of their free will and subjects them to the Bard"s commands. For a time, the victim will turn completely away from his own people and feel that he belongs to the bard"s party.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 40 Aura  
**Modificateurs** :  
**Syntaxe** : `CAST "Gesang der Versklavung" <unit-id>`  

### Gesang des schwachen Geistes  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Gesang des schwachen Geistes (DE)*.
<!-- cspell:enable -->

**Description** :  
Woven into the magical essence of the region, this song weakens one"s natural resistance to an enchantment by 15% once. Only the bard"s allies (HELP GUARD) are immune to the effect of the song.
**Type** : sort normal  
**Rang** : 2  
**Composants** : 2 Aura x Niveau  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Gesang des schwachen Geistes"`  

### Gesang des wachen Geistes  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Gesang des wachen Geistes (DE)*.
<!-- cspell:enable -->

**Description** :  
This magical song, once sung with fervor, will spread throughout the region, jump from mouth to mouth and be heard everywhere for a while. How many weeks the song disappears from the memory of the region depends on the skill of the bard. Until the song has completely faded away, his magic will grant all of the bard"s allies (HELP GUARD), and of course his own people, a one-time bonus of 15% to the natural resistance to an enchantment.  
**Type** : sort normal  
**Rang** : 2  
**Composants** : 2 Aura x Niveau  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Gesang des wachen Geistes"`  

### Magie du bosquet de chêne

<!-- cspell:disable -->
*Grove of Oak Trees (EN), Hainzauber (DE)*.
<!-- cspell:enable -->

**Description** :  
Where previously only a tree could sprout from a stick, every branch now sprouts roots.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 4 Aura x Niveau, 1 Holz \* Niveau, 1 water of lifes  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Grove of Oak Trees"`  

## H

### Grêle

<!-- cspell:disable -->
*Hail (EN), Hagel (DE)*.
<!-- cspell:enable -->

**Description** :  
In battle, the magician calls upon the elemental spirits of cold and binds them to himself. He can then order them to attack the enemy with hailstones and chunks of ice.
**Type** : Kampfzauber  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Hail`  

### Gueule de bois

<!-- cspell:disable -->
*Hangover (EN), Schaler Wein (DE)*.
<!-- cspell:enable -->

**Description** :  
There are more than 512 characters with translation, please reduce the translation content.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 28 Aura, 3 trématode à nœuds, 50 silver  
**Modificateurs** :  
**Syntaxe** : `CAST Hangover <unit-id>`  

### Guérison

<!-- cspell:disable -->
*Heal (EN), Heilung (DE)*.
<!-- cspell:enable -->

**Description** :  
It"s not just the medic who can help the wounded in battle. Druids are able to close wounds, set broken bones and regenerate even severed limbs by summoning the elemental spirits of life.
**Type** : sort de post-combat  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Heal`  

### Imprécation

<!-- cspell:disable -->
*Hex (EN), Verwünschung (DE)*.
<!-- cspell:enable -->

**Description** :  
The magician"s target is afflicted by a harmless curse.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] Hex <unit-id>`  

### Hitzeelementar  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Hitzeelementar (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual summons angry heat elementals. A drought is plaguing the country. Trees wither, animals die, and the harvest fails. There is hardly any work to be found in agriculture for day laborers.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 600 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] Hitzeelementar`  

### Hohe Kunst der Überzeugung  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Hohe Kunst der Überzeugung (DE)*.
<!-- cspell:enable -->

**Description** :  
From "Wanderings" by Firudin the Wise: "In Weilersweide, near the Wythar harbor, there is a small inn that is rarely visited. It is not known to anyone that until a few years ago this farm was the home of the banished itinerant preacher Grauwolf. After recruiting almost the entire peasantry in one of his infamous fiery speeches, he was convicted of sedition and banished. He was only hesitantly willing to teach me the secret of his persuasiveness."
**Type** : sort normal  
**Rang** : 5  
**Composants** : 20 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Hohe Kunst der Überzeugung"`  

### Pierre de maison

<!-- cspell:disable -->
*Homestone (EN), Heimstein (DE)*.
<!-- cspell:enable -->

**Description** :  
With this formula, the magician binds the forces of the earth forever into the walls of the castle in which he currently finds himself. Walls that have been strengthened in this way cannot be destroyed either by magic or with heavy artillery, and age also affects them less. The building also offers better protection against attacks with swords and magic.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 50 Aura, 1 aura permanent  
**Modificateurs** :  
**Syntaxe** : `CAST Homestone`  

### Chant du partage d'aura

<!-- cspell:disable -->
*Hymn of Aura Sharing (EN), Gesang des Auratransfers (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this spell, the magician can transfer his own aura at a ratio of 2:1 to another magician of the same magic area.
**Type** : sort normal  
**Rang** : 1  
**Composants** : 2 Aura  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Hymn of Aura Sharing" <unit-id> <Aura>`  

## I

### Insomnie

<!-- cspell:disable -->
*Insomnia (EN), Schlechter Schlaf (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell causes insomnia and restlessness in the affected area for a few weeks. Those affected find it much more difficult to learn.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 18 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] Insomnia`  

## J

### Jonglerie

<!-- cspell:disable -->
*Jugglery (EN), Gaukeleien (DE)*.
<!-- cspell:enable -->

**Description** :  
Cerddor mages are the leading jugglers among the mages, they love to entertain the people and be the center of attention. Even beginners learn the little tricks and magical tricks that can be used to lure and seduce people into opening their wallets very wide, and at the end of the week the juggler will have earned 50 silver per level.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] Jugglery`  

## L

### Petit sacrifice de sang

<!-- cspell:disable -->
*Lesser Sacrifice (EN), Kleines Blutopfer (DE)*.
<!-- cspell:enable -->

**Description** :  
With this ritual the magician can sacrifice part of his life energy in order to gain magical power. Experienced ritual magicians report that the ritual, once initiated, is difficult to control and the amount of power gained varies greatly. So it is written in the "Book of Blood": "So let He establish the sign of the four elements in the circle of creation and decay and consecrate each one with a drop of blood. Then let He go into the midst of the Eternal Four and let life pass away so that strength can be born."  
**Type** : sort normal  
**Rang** : 1  
**Composants** : 16 Hit points  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Lesser Sacrifice"`  

## M

### Folie de la guerre

<!-- cspell:disable -->
*Madness of War (EN), Wahnsinn des Krieges (DE)*.
<!-- cspell:enable -->

**Description** :  
In front of the enemy soldiers, the black magician sacrifices the ten pawns in a bloody, cruel ritual and in this way summons spirits of madness over the enemy troops. They will react confusedly in battle and be unable to follow the orders of their officers.
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 3 Aura x Niveau, 10 Bauern  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Madness of War"`  

### Voie magique

<!-- cspell:disable -->
*Magic Path (EN), Magischer Pfad (DE)*.
<!-- cspell:enable -->

**Description** :  
By performing these rituals, the magician is able to summon a powerful earth elemental. As long as this is banished into the ground, no rain will soften the paths and no river will be able to destroy bridges. This means that all travelers receive the same advantages that would otherwise only be offered by a developed paved road network. Even swamps and glaciers can be enchanted this way. The more power the magician puts into the spell, the longer the road lasts.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau, 1 Stein, 1 Holz  
**Modificateurs** : sort à distance, sort sur bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Magic Path"`  

### Mahlstrom  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Mahlstrom (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual summons a great water elemental from the depths of the ocean. The elemental creates a massive whirlpool, a maelstrom, which can severely damage any ships that pass through it.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 200 Aura, 1 Seeschlangenkopf  
**Modificateurs** : Seezauber, sort sur bateau  
**Syntaxe** : `CAST Mahlstrom`  

### Méditation

<!-- cspell:disable -->
*Meditate (EN), Meditation (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this spell, the magician can transfer his own aura at a ratio of 2:1 to another magician of the same magic area.
**Type** : sort normal  
**Rang** : 1  
**Composants** : 2 Aura  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST Meditate <unit-id> <Aura>`  

### Intrusion mentale

<!-- cspell:disable -->
*Mind Probe (EN), Traumdeuten (DE)*.
<!-- cspell:enable -->

**Description** :  
With this spell, the dream weaver penetrates the thoughts and dream world of his victim and can thus spy on his most intimate secrets. His abilities, possessions and party affiliation will no longer be uncertain.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 20 Aura  
**Modificateurs** :  
**Syntaxe** : `CAST "Mind Probe" <unit-id>`  

### Petites malédictions

<!-- cspell:disable -->
*Minor Curses (EN), Kleine Flüche (DE)*.
<!-- cspell:enable -->

**Description** :  
In the darker alleys they exist, the curses and hexes made to order. But of course the disciple of Draig also offers counterspells. Whether the neighbor"s son is to be drawn into a love spell or the rival is to get pimples and warts, no one likes to admit that they have resorted to such measures. For this service, the magician earns 50 silver per level.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] "Minor Curses"`  

### Docteur Miracle

<!-- cspell:disable -->
*Miracle Doctor (EN), Wunderdoktor (DE)*.
<!-- cspell:enable -->

**Description** :  
If the alchemist cannot help you, you go to the learned Tybied magician. His potions and tinctures help against everything you can"t get otherwise. Whether the cryptic formula under the wooden shoe of the unfaithful husband really helped -well, the farmer who doesn"t know how to read will never know. It definitely helps the magician... fill his wallet. You can earn 50 silver per level in a week.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] "Miracle Doctor"`  

### Miriams flinke Finger  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Miriams flinke Finger (DE)*.
<!-- cspell:enable -->

**Description** :  
There are more than 512 characters with translation, please reduce the translation content.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 20 Aura, 1000 silver, 1 aura permanent  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Miriams flinke Finger"`  

### Mob aufwiegeln  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Mob aufwiegeln (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this magical song, the magician convinces the farmers of the region to join him. However, the farmers will not leave their homeland and will not give away any of their possessions. Each week some of the farmers will also cast off the spell and return to their fields. How many farmers join the magician depends on the power of his song.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 4 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Mob aufwiegeln"`  

### [[mountain-guard|Gardien de la Montagne]]

<!-- cspell:disable -->
*Mountain Guardian (EN), Bergwächter (DE)*.
<!-- cspell:enable -->

**Description** :  
Creates a guardian spirit that prevents iron and metal mining in glaciers and mountains by non-allied parties (HELP GUARD) as long as it guards the region. The mountain guardian is bound to the location of the summoning.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 3 Aura x Niveau  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] Mountain Guardian`  

## N

### Brise‑malédiction

<!-- cspell:disable -->
*Negate Curse (EN), Fluch brechen (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell allows the magician to specifically dispel a specific enchantment on a unit, ship, building or even the region.
**Type** : sort normal  
**Rang** : 3  
**Composants** : 3 Aura x Niveau  
**Modificateurs** : sort à distance, sort sur bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Negate Curse" ( REGION | UNIT <unit-id> | SHIP <ship-id> | CASTLE <building-id> ) <spell-id>`  

## O

### Opfere Kraft  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Opfere Kraft (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this spell, the magician can permanently transfer part of his magical power to another magician. He can transfer half of the power used to a magician of the same magic area, and a third to other magicians.
**Type** : sort normal  
**Rang** : 1  
**Composants** : 100 Aura  
**Modificateurs** :  
**Syntaxe** : `CAST "Opfere Kraft" <unit-id> <Aura>`  

## P

### Voie des Arbres

<!-- cspell:disable -->
*Path of Trees (EN), Weg der Bäume (DE)*.
<!-- cspell:enable -->

**Description** :  
Great power lies in places where life pulsates. The druid can collect this power and create a gateway into the world of spiritual beings. The druid can then level*Send 5 units of weight through the gate.
**Type** : sort normal  
**Rang** : 7  
**Composants** : 3 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Path of Trees" <unit-id> [<unit-id> ...]`  

### Pentagramm  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Pentagramm (DE)*.
<!-- cspell:enable -->

**Description** :  
Exactly at midnight, when the powers of darkness are at their greatest, a black magician can also use his powers to remove enchantments. To do this, he draws a pentagram on the enchanted object and begins with an invocation to the lords of darkness. The gentlemen will help him, but whether he succeeds in solving the spell depends solely on his own strength.
**Type** : sort normal  
**Rang** : 2  
**Composants** : 10 Aura x Niveau  
**Modificateurs** : sort à distance, sort sur bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] Pentagramm ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Protection contre la magie

<!-- cspell:disable -->
*Protection from Magic (EN), Schutz vor Magie (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell places an antimagic field around enemy mages, significantly hindering their spellcasting. Only a few will have the strength to penetrate the field and aid their troops in battle.
**Type** : sort de pré-combat  
**Rang** : 2  
**Composants** : 3 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Protection from Magic"`  

### Runes de protection

<!-- cspell:disable -->
*Protective Runes (EN), Runen des Schutzes (DE)*.
<!-- cspell:enable -->

**Description** :  
If you draw these runes on the walls of a building or on the planks of a ship, it will be more difficult to influence by magic. Each ritual increases the building or ship"s resistance to enchantment by 20%. If several protective spells are placed on top of each other, their effects are added together, but 100% protection cannot be achieved this way. The spell lasts at least three weeks, but depending on the magician"s talent it can last much longer.
**Type** : sort normal  
**Rang** : 2  
**Composants** : 20 Aura  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Protective Runes" ( SHIP <ship-id> | CASTLE <building-id> )`  

## R

### Danse de la pluie

<!-- cspell:disable -->
*Rain Dance (EN), Regentanz (DE)*.
<!-- cspell:enable -->

**Description** :  
Dieses uralte Tanzritual ruft die Kräfte des Lebens und der Fruchtbarkeit. Die Erträge der Bauern werden für einige Wochen deutlich besser ausfallen.  
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** : sort à distance, sort sur bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] Rain Dance`  

### Pluie de rouille

<!-- cspell:disable -->
*Rain of Rust (EN), Rostregen (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual conjures up a dark storm front that towers ominously over the region. The magical rain will cause all ore to rust. Iron weapons and armor become chipped and rusty. The destructive power of the rain depends on the power invested by the magician. Up to 10 iron weapons can be affected for each level. A ring of power increases the effect like an additional level.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 2 Aura x Niveau  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Rain of Rust" <unit-id> [<unit-id> ...]`  

### Lecture des rêves

<!-- cspell:disable -->
*Read Dreams (EN), Traumlesen (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell allows the Dreamweaver to enter a unit"s dreams to obtain a report on the surrounding area.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 8 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Read Dreams" <unit-id>`  

### Résistance à la magie

<!-- cspell:disable -->
*Resist Magic (EN), Schutzzauber (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell increases your natural resistance to magic. A unit protected in this way is also less vulnerable to combat magic. Per level, the magician"s power is enough to protect 5 people.
**Type** : sort normal  
**Rang** : 2  
**Composants** : 5 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] Resist Magic <unit-id> [<unit-id> ...]`  

### Résurrection

<!-- cspell:disable -->
*Resurrection (EN), Wiederbelebung (DE)*.
<!-- cspell:enable -->

**Description** :  
If a warrior dies in battle, his soul begins the long journey to the stars. With the help of a ritual, a dream weaver can attempt to capture the soul and return it to the body of the deceased. Although the spell does not heal physical injuries, the person treated will survive the fight.
**Type** : sort de post-combat  
**Rang** : 4  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Resurrection`  

### Rindenhaut  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Rindenhaut (DE)*.
<!-- cspell:enable -->

**Description** :  
Dieses vor dem Kampf zu zaubernde Ritual gibt den eigenen Truppen einen zusätzlichen Bonus auf ihre Rüstung. Jeder Treffer reduziert die Kraft des Zaubers, so dass der Schild sich irgendwann im Kampf auflösen wird.  
**Type** : sort de pré-combat  
**Rang** : 2  
**Composants** : 4 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Rindenhaut`  

### Ritual der Aufnahme  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Ritual der Aufnahme (DE)*.
<!-- cspell:enable -->

**Description** :  
Dieses Ritual ermöglicht es, eine Einheit, egal welcher Art, in die eigene Partei aufzunehmen. Der um Aufnahme Bittende muss dazu willig und bereit sein, seiner alten Partei abzuschwören. Dies bezeugt er durch KONTAKTIEREn des Magiers. Auch wird er die Woche über ausschliesslich mit Vorbereitungen auf das Ritual beschäftigt sein. Das Ritual wird fehlschlagen, wenn er zu stark an seine alte Partei gebunden ist, dieser etwa Dienst für seine teuere Ausbildung schuldet. Der das Ritual leitende Magier muss für die permanent Bindung des Aufnahmewilligen an seine Partei naturgemäß auch aura permanent aufwenden. Pro Niveau und pro 1 aura permanent kann er eine Person aufnehmen.  
**Type** : sort normal  
**Rang** : 5  
**Composants** : 3 Aura x Niveau, 1 aura permanent \* Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Ritual der Aufnahme" <unit-id>`  

### Rüstschild  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Rüstschild (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual, which can be cast before battle, gives your troops an additional bonus to their armor. Each hit reduces the spell"s power, so the shield will dissipate at some point in the fight.
**Type** : sort de pré-combat  
**Rang** : 2  
**Composants** : 4 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Rüstschild`  

## S

### Terre Sacrée

<!-- cspell:disable -->
*Sacred Ground (EN), Heiliger Boden (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual summons various natural spirits into the soil of the region, which guard it from then on. In such a blessed region, the dead will never again leave their graves, and undead that have arisen elsewhere will avoid them whenever possible.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 80 Aura, 3 aura permanent  
**Modificateurs** :  
**Syntaxe** : `CAST "Sacred Ground"`  

### Préservation du butin

<!-- cspell:disable -->
*Save Spoils (EN), Beschleunigung (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell prevents some of the objects that would otherwise be destroyed in battle from being damaged. Losses are reduced by 5% per level of the spell, up to a minimum of 25%.
**Type** : sort de post-combat  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Save Spoils"`  

### Schlechte Träume  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Schlechte Träume (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell allows the Dreamer to disrupt the sleep of all non-allied units (HELP GUARD) in the region to such an extent that they temporarily lose some of their memories.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 90 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Schlechte Träume"`  

### Chevaliers de l'Ombre

<!-- cspell:disable -->
*Shadow Knights (EN), Schattenritteren (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell can give the enemy a slightly different image of their own troops. The Shadow Knights have no effective attack and being wounded in battle will destroy them instantly.
**Type** : sort de pré-combat  
**Rang** : 4  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Shadow Knights"`  

### Bouclier du poisson

<!-- cspell:disable -->
*Shield of the Fish (EN), Schild des Fisches (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell can give the enemy a slightly different image of their own troops, just like the fish in the water is not where it seems to be. In this way, half of the damage from each hit can be rendered harmless. But the shield can only withstand a few hundred sword blows, after which it will disintegrate. The stronger the magician, the more damage the shield can withstand.
**Type** : sort de pré-combat  
**Rang** : 2  
**Composants** : 4 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Shield of the Fish"`  

### Endormissement

<!-- cspell:disable -->
*Sleep (EN), Schlaf (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell causes some enemy combatants to fall asleep. Sleeping fighters do not attack and have poorer defenses, but they wake up as soon as they are hit in combat.
**Type** : Kampfzauber  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Sleep`  

### Onde de choc

<!-- cspell:disable -->
*Shockwave (EN), Schockwelle (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell causes a wave of pure power to sweep across the enemy ranks. The shock will leave many fighters so dazed that they will be unable to attack for a brief moment.
**Type** : Kampfzauber  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Shockwave`  

### Schöne Träume  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Schöne Träume (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell allows the Dreamweaver to affect the sleep of all allied units in the region, giving them a bonus in all talents for a period of time.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 80 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Schöne Träume"`  

### Segne Mallornstecken  <!-- TODO -->

<!-- cspell:disable -->
* (EN), Segne Mallornstecken (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual increases the effect of the magical potion many times over. Where previously only a tree could sprout from a stick, every branch now sprouts roots.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 6 Aura x Niveau, 1 Mallorn \* Niveau, 1 water of lifes  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Segne Mallornstecken"`  

### Segne Steinkreis <!-- TODO -->

<!-- cspell:disable -->
* (EN), Segne Steinkreis (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual blesses a stone circle that must first be built from stones and some wood. The Druid"s Blessing turns the circle into a powerful site of magical activity, providing protection from magic and increased aura regeneration. It is said that virgins encountered strange creatures around stone circles.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 350 Aura, 5 aura permanent  
**Modificateurs** :  
**Syntaxe** : `CAST "Segne Steinkreis" <building-id>`  

### Changement de forme

<!-- cspell:disable -->
*Shapeshift (EN), Gestaltwandlung (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this arcane ritual, the dream weaver is able to disguise the true form of a group. To inexperienced observers, she then appears to belong to a different race.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] Shapeshift <unit-id> <race>`  

### Dissonance du silence

<!-- cspell:disable -->
*Silence Dissonance (EN), Lebenslied festigen (DE)*.
<!-- cspell:enable -->

**Description** :  
Each enchantment affects the Life Song, weakening and distorting it. The skilled bard can attempt to capture and amplify the song of life and erase the changes from the song.
**Type** : sort normal  
**Rang** : 2  
**Composants** : 5 Aura x Niveau  
**Modificateurs** : sort à distance, sort sur bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Silence Dissonance" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Sog des Lebens <!-- TODO -->

<!-- cspell:disable -->
* (EN), Sog des Lebens (DE)*.
<!-- cspell:enable -->

**Description** :  
A druid who has fallen into the world of spirits can use this spell to level up*Send 5 units of weight back to a forest on the material world.
**Type** : sort normal  
**Rang** : 7  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Sog des Lebens" <x> <y> <unit-id> [<unit-id> ...]`  

### Chant de confusion

<!-- cspell:disable -->
*Song of Confusion (EN), Gesang der Verwirrung (DE)*.
<!-- cspell:enable -->

**Description** :  
This magical song comes from the ancient songs of cats and, when used before a fight, can bring decisive strategic advantages. Anyone who comes under the influence of this song will not pay attention to the melody of their surroundings, their mind will become confused and give in erratically to sudden inspirations. Well-ordered armies are said to have suddenly found their archers far in front and their cavalry playing cards with the camp guards (or their leader sleeping in the long-abandoned camp, as is actually said to have happened in the Great Wars of the Old World)..  
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Song of Confusion"`  

### Chant de cour

<!-- cspell:disable -->
*Song of Courting (EN), Gesang des Werbens (DE)*.
<!-- cspell:enable -->

**Description** :  
From "The Songs of the Ancients" by Firudin the Wise: "This seductive little melody and a few insinuating words overcome the distrust of the peasants in an instant. They will enthusiastically join you and leave their house and yard in ruins themselves."
**Type** : sort normal  
**Rang** : 5  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Song of Courting"`  

### Chant d'effroi

<!-- cspell:disable -->
*Song of Fear (EN), Gesang der Angst (DE)*.
<!-- cspell:enable -->

**Description** :  
This war song sows panic in the enemy"s front lines and thus significantly weakens their fighting strength. Fear will weaken their sword arm and fear will paralyze their shield arm.
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 5 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Song of Fear"`  

### Chant de générosité

<!-- cspell:disable -->
*Song of Generosity (EN), Hohes Lied der Gaukelei (DE)*.
<!-- cspell:enable -->

**Description** :  
This cheerful song will spread like a rumor throughout the region and put the whole world in a celebratory mood. Taverns and theaters everywhere will be full and even the beggars will be fed.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 2 Aura x Niveau  
**Modificateurs** : sort à distance, sort sur bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Song of Generosity"`  

### Chant de guérison

<!-- cspell:disable -->
*Song of Healing (EN), Lied der Heilung (DE)*.
<!-- cspell:enable -->

**Description** :  
It"s not just the medic who can help the wounded in battle. The bards know various songs that support the body"s self-healing powers. This song can close wounds, set broken bones and regenerate even severed limbs.
**Type** : sort de post-combat  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Song of Healing"`  

### Chant de séduction

<!-- cspell:disable -->
*Song of Seduction (EN), Lied der Verführung (DE)*.
<!-- cspell:enable -->

**Description** :  
This song can be used to charm a unit into giving most of their cash and possessions to the bard. However, she always keeps what she needs to survive.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 12 Aura  
**Modificateurs** :  
**Syntaxe** : `CAST "Song of Seduction" <unit-id>`  

### Chant de terreur

<!-- cspell:disable -->
*Song of Terror (EN), Gesang der Furcht (DE)*.
<!-- cspell:enable -->

**Description** :  
A very powerful song from the traditions of cats that penetrates deep into the hearts of enemies and robs them of courage and hope. Fear will make them tremble and panic will dominate their thoughts. Full of fear, they will try to escape the horrible songs and flee.
**Type** : Kampfzauber  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Song of Terror"`  

### Chant de guerre

<!-- cspell:disable -->
*Song of War (EN), Kriegsgesang (DE)*.
<!-- cspell:enable -->

**Description** :  
Like many magical songs, this one also comes from the ancient knowledge of cats, who have always known about the powerful effects of the voice. This song whips up the mood of the warriors, even driving them into wild frenzy and bloodlust. Regardless of their own pain, they will fight to the death and never flee. While their attack is intensified, they pay little attention to themselves.
**Type** : sort de pré-combat  
**Rang** : 4  
**Composants** : 5 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Song of War"`  

### Écoute clandestine

<!-- cspell:disable -->
*Sound out (EN), Aushorchen (DE)*.
<!-- cspell:enable -->

**Description** :  
If the unit succumbs to the spell, it will tell the magician everything it knows about the region in question. If there is no one from her party in the region, she has nothing to report. She can also only tell what she could see herself.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 4 Aura, 100 silver  
**Modificateurs** :  
**Syntaxe** : `CAST "Sound out" <unit-id> <x> <y>`  

### Vol d'aura

<!-- cspell:disable -->
*Steal Aura (EN), Stehle Aura (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this spell, the magician can withdraw his aura from another magician against his will and supply it to himself.
**Type** : sort normal  
**Rang** : 3  
**Composants** : 2 Aura x Niveau  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Steal Aura" <unit-id>`  

### Portail puissant et Mur robuste

<!-- cspell:disable -->
*Strong Wall And Sturdy Gate (EN), Starkes Tor und feste Mauer (DE)*.
<!-- cspell:enable -->

**Description** :  
With this formula, at the beginning of a fight, the magician binds some elemental spirits of the rock into the walls of the building in which he is currently located. The building then offers better protection against attacks with the sword and magic.
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Strong Wall And Sturdy Gate"`  

### Störe Astrale Integrität <!-- TODO -->

<!-- cspell:disable -->
* (EN), Störe Astrale Integrität (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell causes severe disruption to the astral space. Within an astral radius of level/5 regions, all astral beings who cannot resist the spell are thrown out of the astral plane. Astral contact with all affected regions is disrupted for level/3 weeks.
**Type** : sort normal  
**Rang** : 4  
**Composants** : 140 Aura  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Störe Astrale Integrität"`  

### Invocation de la Terre

<!-- cspell:disable -->
*Summon Earth Elemental (EN), Beschwöre einen Erdelementar (DE)*.
<!-- cspell:enable -->

**Description** :  
With this ritual, the druid summons an elemental spirit of the earth and causes it to cause the earth to tremble. This earthquake will damage all buildings in the region.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 25 Aura, 2 Laen  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Summon Earth Elemental"`  

### Invocation du Familier

<!-- cspell:disable -->
*Summon Familiar (EN), Vertrauten rufen (DE)*.
<!-- cspell:enable -->

**Description** :  
At some point in his wanderings, an experienced magician will encounter an unusual specimen of a species that will join the magician.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 100 Aura, 5 aura permanent  
**Modificateurs** :  
**Syntaxe** : `CAST "Summon Familiar"`  

### Invocation des Démons de l'Ombre

<!-- cspell:disable -->
*Summon Shadowdemons (EN), Beschwöre Schattendämonen (DE)*.
<!-- cspell:enable -->

**Description** :  
Using dark rituals, the magician summons demons from the sphere of shadows. These feared creatures can move almost invisibly among the living, but their dark aura can be felt by everyone. Shadow demons are feared opponents in battle. They are difficult to hit and drain their opponent"s power.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 3 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Summon Shadowdemons"`  

### Invocation de la Tempête

<!-- cspell:disable -->
*Summon Storm Elemental (EN), Beschwöre einen Sturmelementar (DE)*.
<!-- cspell:enable -->

**Description** :  
Summoning elemental spirits of storms is an ancient ritual. The druid banishes the elementals into the sails of the ships, where they help carry the ship over the waves at high speed. The more power the druid invests in the spell, the greater the number of elemental spirits that can be banished. An elemental spirit is required for each ship.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 6 Aura x Niveau  
**Modificateurs** : Seezauber, sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] "Summon Storm Elemental" <ship-id> [<ship-id> ...]`  

### Invocation de l'Eau

<!-- cspell:disable -->
*Summon Water Elemental (EN), Beschwörung eines Wasserelementares (DE)*.
<!-- cspell:enable -->

**Description** :  
With this ritual, the magician forces the elemental spirits of the water into his service and gets them to carry the specified ship through the water more quickly. In addition, the ship is not affected by unfavorable winds or currents.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] Summon Water Elemental <ship-id>`  

### Süße Träume <!-- TODO -->

<!-- cspell:disable -->
* (EN), Süße Träume (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell -the use of which is strictly forbidden in most cultures -triggers an uncontrollable desire for physical love in the victim. The affected individuals will rush headlong into a love affair, too blinded by desire to think of anything else. Most of the time they regret it a few weeks later...
**Type** : sort normal  
**Rang** : 5  
**Composants** : 5 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Süße Träume" <unit-id> [<unit-id> ...]`  

## T

### Hurlement des Loups

<!-- cspell:disable -->
*Timber Wolves (EN), Wolfsgeheul (DE)*.
<!-- cspell:enable -->

**Description** :  
Over the course of their lives in nature, quite a few Druids become friends with the oldest friends of the great peoples. They learn to summon many of their friends to aid them in battle with a single howling call.
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Timber Wolves"`  

### Affaiblissement

<!-- cspell:disable -->
*Tiredness (EN), Schwere Glieder (DE)*.
<!-- cspell:enable -->

**Description** :  
This combat spell causes some enemies to suffer severe fatigue during combat. The soldiers sometimes oversleep their attack and defend themselves poorly.
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 4 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Tiredness`  

### Tod des Geistes <!-- TODO -->

<!-- cspell:disable -->
* (EN), Tod des Geistes (DE)*.
<!-- cspell:enable -->

**Description** :  
With this spell the magician attacks the minds of his opponents directly. A blast of astral and electrical energy hits the opponents; if magic resistance is broken, a victim permanently loses part of their memories. If it falls victim to this spell too often, it can die.
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Tod des Geistes"`  

### Todeswolke <!-- TODO -->

<!-- cspell:disable -->
* (EN), Todeswolke (DE)*.
<!-- cspell:enable -->

**Description** :  
With a dark ritual and sacrificing his own blood, the black magician summons a great spirit from the elemental plane of poisons. The spirit manifests itself as a bright green cloud over the region and will harm all who come into contact with it.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 40 Aura, 15 Trefferpunkte  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] Todeswolke`  

### Tor in die Ebene der Hitze <!-- TODO -->

<!-- cspell:disable -->
* (EN), Tor in die Ebene der Hitze (DE)*.
<!-- cspell:enable -->

**Description** :  
This powerful ritual opens a gateway into the elemental plane of heat. A great drought is coming to the country. Farmers, animals and plants in the region are fighting for survival, but only half of all living things can survive such a drought. The region can be affected by the consequences of such a drought for years to come.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 800 Aura  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Tor in die Ebene der Hitze"`  

### Transfert d'aura

<!-- cspell:disable -->
*Transfer Aura (EN), Auratransfer (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this spell, the magician can transfer his own aura to another magician of the same magic area at a ratio of 2:1 or to a magician of another magic area at a ratio of 3:1.
**Type** : sort normal  
**Rang** : 1  
**Composants** : 1 Aura  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Transfer aura" <unit-id> <Aura>`  

### Transfert de pouvoir

<!-- cspell:disable -->
*Transfer Power (EN), Machtübertragung (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this spell, the magician can transfer his own aura at a ratio of 2:1 to another magician of the same magic area.
**Type** : sort normal  
**Rang** : 1  
**Composants** : 2 Aura  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST "Transfer Power" <unit-id> <Aura>`  

### Traumbilder entwirren

<!-- cspell:disable -->
* (EN), Traumbilder entwirren (DE)*.
<!-- cspell:enable -->

**Description** :  
This spell allows the dream weaver to distinguish and unravel the natural and forced dream images of a person, building, ship, or region.
**Type** : sort normal  
**Rang** : 2  
**Composants** : 6 Aura x Niveau  
**Modificateurs** : sort à distance, sort sur bateau  
**Syntaxe** : `CAST [REGION x y] [LEVEL n] "Traumbilder entwirren" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

## U

### Héros morts‑vivants

<!-- cspell:disable -->
*Undead Heroes (EN), Untote Helden (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual binds the already escaping souls of some battle victims to their dead bodies, resurrecting them to undead life. Whether they previously fought on the enemy"s side or their own is irrelevant to the ritual.
**Type** : sort de post-combat  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Undead Heroes"`  

### Unheilige Kraft <!-- TODO -->

<!-- cspell:disable -->
* (EN), Unheilige Kraft (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual is only passed on to the adepts in the dark academies in whispers, as it is one of the darkest ever written down. By invoking unholy demons, the power of the living dead is amplified and they transform into undead monsters of great power.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 10 Aura x Niveau, 5 Bauern \* Niveau  
**Modificateurs** :  
**Syntaxe** : `CAST [LEVEL n] "Unheilige Kraft" <unit-id> [<unit-id> ...]`  

### Horreurs indicibles

<!-- cspell:disable -->
*Unspeakable Horrors (EN), Grauen der Schlacht (DE)*.
<!-- cspell:enable -->

**Description** :  
Before battle, the dream weaver conjures up terrifying illusions that cause many opponents to panic. Those affected will try to escape from the mirages.
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 1 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Unspeakable Horrors"`  

## V

## W

### Tourbillon

<!-- cspell:disable -->
*Whirlwind (EN), Wirbelwind (DE)*.
<!-- cspell:enable -->

**Description** :  
This incantation opens a gate into the plane of the elemental spirits of the wind. Strong winds or even storms immediately arise in the area around the gate and hinder all archers in a battle.
**Type** : sort de pré-combat  
**Rang** : 5  
**Composants** : 15 Aura  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] Whirlwind`  

### Vents de rouille

<!-- cspell:disable -->
*Winds of Rust (EN), Rosthauch (DE)*.
<!-- cspell:enable -->

**Description** :  
This ritual conjures up a dark storm front that towers ominously over the region. The magical rain will cause all ore to rust, destroying many of the enemy's weapons.
**Type** : Kampfzauber  
**Rang** : 5  
**Composants** : 2 Aura x Niveau  
**Modificateurs** :  
**Syntaxe** : `COMBATSPELL [LEVEL n] "Winds of Rust"`  

### Wurzeln der Magie <!-- TODO -->

<!-- cspell:disable -->
* (EN), Wurzeln der Magie (DE)*.
<!-- cspell:enable -->

**Description** :  
With the help of this elaborate ritual, the druid allows part of his power to flow permanently into the soil and forests of the region. This will change the balance of nature in the region forever, and in the future only the demanding but strong mallornas will thrive in the region.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 250 Aura, 10 aura permanent, 1 pot de bave de crapaud  
**Modificateurs** : sort à distance  
**Syntaxe** : `CAST [REGION x y] "Wurzeln der Magie"`  

## Z

### Zeitdehnung <!-- TODO -->

<!-- cspell:disable -->
* (EN), Zeitdehnung (DE)*.
<!-- cspell:enable -->

**Description** :  
This practical application of theoretical knowledge of space and time makes it possible to change the flow of time for some people. People modified in this way get twice as many movement points and twice as many attacks per round for a few weeks.
**Type** : sort normal  
**Rang** : 5  
**Composants** : 5 Aura x Niveau  
**Modificateurs** : sort sur bateau  
**Syntaxe** : `CAST [LEVEL n] Zeitdehnung <unit-id> [<unit-id> ...]`  

## Voir aussi

- [[list-of-spells]]

<!-- From [https://wiki.eressea.de/index.php?title=Zauberbeschreibungen\_E2&oldid=9278] -->

[Dragons]: ./monsters.md#dragons
[Ents]: ./monsters.md#ents
