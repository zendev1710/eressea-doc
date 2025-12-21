---
# cSpell:locale en
alias: description-of-spells
---
# Description of spells

## A

### Acceleration

**Description:**  
This spell speeds up some fighters on your side so that they can attack twice in one combat round throughout the entire combat.
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 5 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Acceleration`  

### Air Shield

**Description:**  
Invoking the Elemental Spirits of Wind conjures up sudden gusts of wind, small gusts of wind, and vents that will hinder opposing archers.
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Air Shield"`  

### Airship

**Description:**  
These magical runes make a boat or longboat fly for a week. This can then also be used to cross land. For the color of the runes, a special ink must be mixed from a cream puff and a snow crystal.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 10 Aura, 1 Windbeutel, 1 snow crystal  
**Modifiers:** Ship spell  
**Syntax:** `CAST Airship <ship-id>`  

### Analyse Dreams

**Description:**  
With this spell, the dream weaver can attempt to detect the enchantments of a single unit. He will be able to get an impression of their effectiveness from all spells that do not exceed his own abilities. With stronger spells he needs a little luck for a successful analysis.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 25 Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Analyse Dreams" <unit-id>`  

### Analyze Magic

**Description:**  
This spell allows the magician to attempt to detect the enchantments of a single specified object. He will be able to get an impression of their effectiveness from all spells that do not exceed his own abilities. With stronger spells he needs a little luck for a successful analysis.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] "Analyze Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Analysis

**Description:**  
Like living things, ships and buildings and even regions have their own song, albeit much fainter and harder to hear. And just as you can tell from a person"s life song whether they are under a spell, this is also possible with castles, ships or regions.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 3 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] "Analysis" ( REGION | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Analyze Song of Life

**Description:**  
All living beings have their own individual life song. No two songs are alike, even if all songs of the same type are similar. Each spell changes this song in one way or another and thus reveals itself. This chant helps to hear those changes in a person"s life song that are magical in nature. You will be able to decipher and unmask all enchantments that are not more masked than your ability.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 10 Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Analyze Song of Life" <unit-id>`  

### Animate Dead

**Description:**  
The black magician has to spend nights wandering through the cemeteries and burial grounds of the region in order to be able to revive the unearthed corpses. The undead will be at his service, but the uninformed be warned that summoning the forces of death can be a double-edged sword.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 5 Aura \* Level  
**Modifiers:** Distance  spell, Ship spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Animate Dead"`  

### Antimagic

**Description:**  
With this spell the magician can create a zone of astral weakening, a local imbalance in the astral field. This zone will strive to return to equilibrium. To do this, it will remove part of the strength of every spell cast in this region and even completely absorb the weaker ones.
**Type:** Normal spell  
**Rank:** 2  
**Components:** 3 Aura \* Level  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Antimagic"`  

### Appeasing Song <!-- Friedenslied -->

**Description:**  
This song tames even the wildest orc and makes him peaceful and gentle. Any thought of harming the singer will disappear. The magician can move to a neighboring region unmolested.
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 2 Aura  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Appeasing Song"`  

### Astral Call

**Description:**  
A magician who is in the astral plane can use this spell to bring other units to him. The magician can (level 3)*Send 15 kg through the briefly created gate. If the magician is experienced enough to cast the spell at levels 13 or more, he can force other units to the other level even against their will.
**Type:** Normal spell  
**Rank:** 7  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Astral Call" <x> <y> <unit-id> [<unit-id> ...]`  

### Astral Chaos

**Description:**  
This ritual, performed before battle, swirls the astral energies on the battlefield, making it more difficult for enemy magicians to cast their spells.
**Type:** Pre-combat spell  
**Rank:** 2  
**Components:** 6 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Astral Chaos"`  

### Astral Exit

**Description:**  
The magician concentrates on the structure of reality and can thus leave the astral plane. He can overall (Level-3)*Send 15 kg through the briefly created gate. If the magician is experienced enough to cast the spell at levels 11 or more, he can force other units to the other level even against their will.
**Type:** Normal spell  
**Rank:** 7  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Astral Exit" <x> <y> <unit-id> [<unit-id> ...]`  

### Astral Guardian Spirits

**Description:**  
This ritual summons some elemental spirits of magic and sends them into the ranks of the enemy mages. These will find it much more difficult to cast spells for the duration of the fight.
**Type:** Pre-combat spell  
**Rank:** 2  
**Components:** 5 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Astral Guardian Spirits"`  

### Astral Leak

**Description:**  
With this dark ritual, the black magician can cause a rift in the fabric of magic, which will tear all magical power from the region. All magically gifted people in the region will lose much of their aura.
**Type:** Normal spell  
**Rank:** 3  
**Components:** 35 Aura, 1 Dragonblood  
**Modifiers:**  
**Syntax:** `CAST "Astral Leak"`  

### Astral Path

**Description:**  
Ancient arcane formulas allow the magician to send himself and others into the astral plane. The magician can (level 3)*Send 15 kg through the briefly created gate. If the magician is experienced enough to cast the spell at levels 11 or more, he can force other units to the other level even against their will.
**Type:** Normal spell  
**Rank:** 7  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Astral Path" <unit-id> [<unit-id> ...]`  

### Aufruhr beschwichtigen <!-- TODO -->

**Description:**  
With the help of this magical chant, the magician can calm a region in turmoil. The hordes of farmers will get lost and return to their fields.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 30 Aura  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] "Aufruhr beschwichtigen"`  

### Aufruhr verursachen <!-- TODO -->

**Description:**  
With the help of this magical song, the magician puts an entire region in turmoil. Rebellious hordes of farmers make any taxation impossible, hardly anyone will donate money to scams anymore and no new people can be recruited. After a few weeks the mob calms down again.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 40 Aura  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] "Aufruhr verursachen"`  

### Awakening of the [Ents]

**Description:**  
With the help of this spell, the druid awakens the Ents slumbering in the forests of the region from their eons-long sleep. The wild tree creatures will join him and assist him, but after a while they will fall back into slumber.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 6 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Awakening of the Ents"`  

## B

### Banish Spirits

**Description:**  
According to the ancient teachings of the Druids, what ordinary beings call magic consists of elemental spirits. The magician conjures and banishes these into a form to achieve the desired effect. This ritual is able to drive away elemental spirits that have been summoned into this world in order to free an object from magic.
**Type:** Normal spell  
**Rank:** 2  
**Components:** 6 Aura \* Level  
**Modifiers:** Distance  spell, Ship spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Banish Spirits" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Belebtes Gestein <!-- TODO -->

**Description:**  
This energy-sapping ritual uses a ball of concentrated Laen to summon a massive earth elemental and banish it to a building. The elemental can then be ordered to carry the building and all its inhabitants to a neighboring region. The strength of the summoned elemental depends on the talent of the magician: the elemental can do maximum[Level-12]*Move 250 size units buildings. The building will not survive this procedure unscathed.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 10 Aura \* Level, 1 permanent Aura, 5 Laen  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Belebtes Gestein" <building-id> <Richtung>`  

### Beschwöre Schattenmeister <!-- TODO -->

**Description:**  
Using dark rituals, the magician summons demons from the sphere of shadows. These feared creatures can move almost invisibly among the living, but their dark aura can be felt by everyone. In battle, shadow masters are feared opponents. They are difficult to hit and drain their opponent"s strength and life.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 7 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Beschwöre Schattenmeister"`  

### Blabbermouth

**Description:**  
The enchanted unit begins to babble uninhibitedly, telling you what talents it can do, what kind of objects it carries with it, and if it is magically gifted, even what spells it can use. Unfortunately, this spell does not affect memory, and so in retrospect she will be aware that she has told too much.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 10 Aura  
**Modifiers:**  
**Syntax:** `CAST Blabbermouth <unit-id>`  

### Blick in die Realität <!-- TODO -->

**Description:**  
With the help of this spell, the magician can look from the astral plane into the material plane and recognize the regions and units precisely.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 40 Aura  
**Modifiers:**  
**Syntax:** `CAST "Blick in die Realität"`  

### Blood Frenzy

**Description:**  
In this bloody ritual, the magician sacrifices a newborn baby in front of his army before battle. The blood spirits summoned in this way will take possession of the soldiers and send them into a bloodlust.
**Type:** Pre-combat spell  
**Rank:** 4  
**Components:** 5 Aura \* Level, 1 Bauer  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Blood Frenzy"`  

## C

### Call of Reality

**Description:**  
A magician who is in the material world can use this spell to summon units from the adjacent astral world. If the magician is experienced enough to cast the spell at levels of 13 or more, he can force other units into the material world against their will.
**Type:** Normal spell  
**Rank:** 7  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Call of Reality" <unit-id> [<unit-id> ...]`  

### Calm Monster

**Description:**  
This mellifluous song can tame almost any intelligent monster. It will refrain from attacking the magician and will not touch its companions. But make no mistake, it will still remain an unpredictable creature.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 15 Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Calm Monster" <unit-id>`  

### Castle of Illusion

**Description:**  
With the help of this spell, the dream weaver can create the illusion of any building. The illusion can be entered, but is otherwise non-functional and requires no maintenance. It will last for a few weeks.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 3 Aura  
**Modifiers:**  
**Syntax:** `CAST "Castle of Illusion" <Gebäudetyp>`  

### Cattle Healing

**Description:**  
The Gwyrrd mages" livestock and healing skills are highly sought after by farmers. Their services are often in high demand, especially in markets. Some people may also use their talent to sell an animal for a better price. The magician can earn 50 silver per level.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] "Cattle Healing"`  

### Chaos Curse

**Description:**  
This insidious curse significantly impairs the victim"s magical abilities. A chaos magic zone around the victim reduces his ability to concentrate and makes it very difficult for him to cast spells.
**Type:** Normal spell  
**Rank:** 4  
**Components:** 4 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Chaos Curse" <unit-id>`  

### Chaos Gift

**Description:**  
The magician opens his mind to the spheres of chaos and will thus have more magical power for some time. But the help of the Lords of the Spheres comes at a price, and so the phase of power is replaced by a phase of weakness.
**Type:** Normal spell  
**Rank:** 3  
**Components:** 6 Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Chaos Gift"`  

### Chaossog <!-- TODO -->

**Description:**  
By sacrificing 200 pawns, the chaos magician can open a gate to the astral world. The gate can be used the following week, it dissolves at the end of the following week.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 150 Aura, 200 Bauern  
**Modifiers:**  
**Syntax:** `CAST Chaossog`  

### Concealing Aura

**Description:**  
This spell will obscure all of the target unit"s equipment from view for a period of time.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] "Concealing Aura" <unit-id>`  

### Countersong

**Description:**  
This shrill chant echoes throughout the battlefield. The special dissonances in the melodies make it almost impossible for magicians to concentrate on their spells.
**Type:** Pre-combat spell  
**Rank:** 2  
**Components:** 5 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Countersong`  

### Create a [[belt-of-troll-strength]]

**Description:**  
This magical artifact grants the wearer the strength of a full-grown cave troll. Its carrying capacity increases 50 times and the increased strength and troll-tough skin will also have a positive effect in combat.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 20 Aura, 1 permanent Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Create A Belt of Troll Strength"`  

### Create a [[dreameye]]

**Description:**  
A dragon"s eye cast with this spell and consumed at communion allows the user to enter and read another person"s dreams. For a long time, such an ability was considered useless until the former Wood Elf master of battle magic, Liarana Sundew from the Thall Academy, presented a special application: Generals often dream restlessly before major battles and reveal their plans in dreams. This can give the user a huge advantage in the upcoming battle. But be careful: interpreting dreams is a difficult matter.  
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Drachenkopf, 5 permanent Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Create A DreamEye"`  

### Create a [[flaming-sword]]

**Description:**  
"And so rub the blood of a fierce fighter into the steel of the blade and begin the invocation of the Spheres of Chaos. And if you have done everything to please them, they will send one of their own to imbue the sword with his power..."
**Type:** Normal spell  
**Rank:** 5  
**Components:** 100 Aura, 1 Berserkerblut, 1 Schwert, 1 permanent Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Create A Flaming Sword"`  

### Create [[iron golem|Iron Golems]]

**Description:**  
The more power the magician invests, the more golems can be created. Each golem has a 15 percent chance of turning to dust each round. If you give the golems the command MAKE SWORD/BIHANDER or MAKE SHIELD/CHAIN ​​MAIL/PLATE ARMOR, 4 iron bars are installed per golem and the golem dissolves.
**Type:** Normal spell  
**Rank:** 4  
**Components:** 2 Aura \* Level, 1 Eisen \* Level, 1 Wasser des Lebens  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Create Iron Golems"`  

### Create a [[magical-herb-bag]]

**Description:**  
The Druid takes some prepared leather, which he cleanses of all unclean spirits in a great ritual of purification, and then binds some small spirits of air and water into the material. He now uses the leather prepared in this way to make a small bag that can better preserve the herbs stored in it.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 30 Aura, 1 permanent Aura, 1 Wasser des Lebens  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Create A magical Herb Bag"`  <!-- TODO: not sure -->

### Create a [[negative-weight-bag]]

**Description:**  
This bag encloses a small dimensional fold in which up to 200 weight units can be transported without being counted towards the carrying weight. Horses and other living creatures as well as particularly bulky items (chariots and catapults) cannot be transported in the bag. It is also not possible to transport one magic bag in another. The bag itself weighs 1 kg.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 30 Aura, 1 permanent Aura, 5000 Silver  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Create A Bag of Negative Weight"`  

### Create a [[ring-of-power]]

**Description:**  
This powerful ritual creates a ring of power. A ring of power increases the power of any spell its wearer casts, as if the mage were one level better.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 100 Aura, 1 permanent Aura, 4000 Silver  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Create A Ring of Power"`  

### Create a [[ring-of-invisibility]]

**Description:**  
With this spell the wizard can create a ring of invisibility. The bearer of the ring becomes invisible to all units of other parties, no matter how good their perception may be. In an invisible unit, each person must wear a ring.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 50 Aura, 3000 Silver, 1 permanent Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Create A Ring of Invisibility"`  

### Create a [[sphere-of-invisibility]]

**Description:**  
With this spell the magician can create a sphere of invisibility. The sphere renders its wielder and ninety-nine other people in the same unit invisible.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 150 Aura, 30000 Silver, 3 permanent Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Create A Sphäre of Invisibility"`  

### Create an [[amulet-of-true-vision|Amulet of True Sight]]

**Description:**  
The spell allows a magician to create an Amulet of True Sight. The amulet allows the wearer to see all units protected by a ring of invisibility. However, units that use their camouflage talent to hide still remain undetected.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 50 Aura, 3000 Silver, 1 permanent Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Create An Amulet of True Sight"`  

### Create an [[antimagic-crystal|Antimagic Crystal]]

**Description:**  
With the help of this spell, the magician drains a quartz crystal of all its magical energies. The crystal, when ground into a fine dust and dispersed, will absorb the magical energies released during casting and reduce the power of all spells cast in the region that week.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 50 Aura, 3000 Silver  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Create An Antimagic Crystal"`  

### Create [[stone golem|Stone Golems]]

**Description:**  
Moisten a gap-free block of fine crystalline rock with a vial of the water of life until it has been completely absorbed into the rock. Then you direct your strength towards the fine aura of life that is forming and form a housing for the unbound strength. The more power the magician invests, the more golems can be created before the aura dissipates. Each golem has a 10 percent chance of turning to dust each round. If you give the golems the commands MAKE CASTLE or MAKE ROAD, 4 stones are placed per golem and the golem dissolves.  
**Type:** Normal spell  
**Rank:** 4  
**Components:** 2 Aura \* Level, 1 Stein \* Level, 1 Wasser des Lebens  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Create Stone Golems"`  

### Curse of Pestilence

**Description:**  
In an elaborate ritual, the black magician sacrifices some peasants and then magically distributes the corpses into the region"s wells.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 30 Aura, 50 Bauern  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] "Curse of Pestilence"`  

## D

### Destroy Magic

**Description:**  
This spell allows the magician to dispel enchantments on a unit, ship, building, or even region.
**Type:** Normal spell  
**Rank:** 2  
**Components:** 4 Aura \* Level  
**Modifiers:** Distance  spell, Ship spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Destroy Magic" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Divination

**Description:**  
No one can interpret dreams as well as an Illaun magician. He is also familiar with the art of fortune telling, card reading and palm reading. In return, the farmers pay him 50 silver per level.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] Divination`  

### Drachenruf <!-- TODO -->

**Description:**  
With this dark ritual, the magician creates a lure that smells irresistible to [Dragons]. It has not yet been possible to research whether the dragons come from the surrounding area or from the sphere of chaos. Both are said to have already happened. The bait lasts about 6 weeks, but must be placed in kite-friendly terrain.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 80 Aura, 1 Drachenkopf  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] Drachenruf`  

### Dream of Magic

**Description:**  
With the help of this spell, the dream weaver can transfer his own aura to another dream weaver at a ratio of 2:1.
**Type:** Normal spell  
**Rank:** 1  
**Components:** 2 Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Dream of Magic" <unit-id> <Aura>`  

### Dream

**Description:**  
The magician sends the target of the spell a dream.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] Dream <unit-id>`  

## E

### Epic Heroes

**Description:**  
This ancient battle song raises the morale of your troops and also helps them to resist the frightening aura of demonic and undead beings. Such a solid warrior will not flee even in difficult situations and his considered behavior will give him many an advantage in defense.
**Type:** Pre-combat spell  
**Rank:** 4  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Epic Heroes"`  

### Eternal Rest

**Description:**  
This magical ritual soothes the tormented souls of those who died violently, allowing them to begin their final journey to the Otherlands. Approximately 50 souls will find peace per level of the spell. The spell cannot redeem the living dead who have already been resurrected because their ties to this world are too strong.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 3 Aura \* Level, 1 Wasser des Lebens  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Eternal Rest"`  

### Eternal Walls

**Description:**  
With this formula, the magician binds the forces of the earth into the walls of the building forever. A building enchanted in this way is protected against the ravages of time and no longer requires any maintenance.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 50 Aura, 1 permanent Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] "Eternal Walls" <building-id>`  

## F

### Feuerteufel <!-- TODO -->

**Description:**  
This elemental invocation summons a fire devil, a creature from the deepest reaches of the flaming hells. The fire devil will eagerly pounce on the region"s forests and set them ablaze.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 50 Aura, 1 Öl  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] Feuerteufel`  

### Fireball

**Description:**  
The sorcerer hurls focused chaos into the enemy"s ranks. The ball-shaped chaos will wound anyone it hits.
**Type:** Kampfzauber  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Fireball`  

### Firewall

**Description:**  
The wizard creates a wall of fire in the specified direction. It hurts everyone who walks through it.
**Type:** Normal spell  
**Rank:** 4  
**Components:** 6 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] Firewall <directoin>`  

### Firun's Coat

**Description:**  
This spell allows the magician to magically protect insects from the crippling cold of the glaciers. You can enter glaciers and act normally there. The saying works on a level*10 insects. A Ring of Power increases the number of enchantable insects by an additional 10.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 2 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] "Firun's Coat" <unit-id> [<unit-id> ...]`  

## G

### Gaze of the Basilisk

**Description:**  
This difficult but effective combat spell uses the elemental spirits of stone to turn a number of enemies to stone for the duration of the battle. The affected people will no longer fight, but they cannot be wounded either.
**Type:** Kampfzauber  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Gaze of the Basilisk"`  

### Gesang der Friedfertigkeit <!-- TODO -->

**Description:**  
This powerful spell prevents any attacks. No one in the entire region is capable of taking up arms against anyone. The effects can last for several weeks.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 20 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Gesang der Friedfertigkeit"`  

### Gesang der Melancholie  <!-- TODO -->

**Description:**  
With this song the bard spreads a melancholic, sad mood among the farmers. For a few weeks they will retreat to their huts and leave no silver in the theaters and taverns.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 40 Aura  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] "Gesang der Melancholie"`  

### Gesang der Versklavung  <!-- TODO -->

**Description:**  
This powerful spell robs the victim of their free will and subjects them to the Bard"s commands. For a time, the victim will turn completely away from his own people and feel that he belongs to the bard"s party.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 40 Aura  
**Modifiers:**  
**Syntax:** `CAST "Gesang der Versklavung" <unit-id>`  

### Gesang des schwachen Geistes  <!-- TODO -->

**Description:**  
Woven into the magical essence of the region, this song weakens one"s natural resistance to an enchantment by 15% once. Only the bard"s allies (HELP GUARD) are immune to the effect of the song.
**Type:** Normal spell  
**Rank:** 2  
**Components:** 2 Aura \* Level  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Gesang des schwachen Geistes"`  

### Gesang des wachen Geistes  <!-- TODO -->

**Description:**  
This magical song, once sung with fervor, will spread throughout the region, jump from mouth to mouth and be heard everywhere for a while. How many weeks the song disappears from the memory of the region depends on the skill of the bard. Until the song has completely faded away, his magic will grant all of the bard"s allies (HELP GUARD), and of course his own people, a one-time bonus of 15% to the natural resistance to an enchantment.  
**Type:** Normal spell  
**Rank:** 2  
**Components:** 2 Aura \* Level  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Gesang des wachen Geistes"`  

### Grove of Oak Trees

**Description:**  
Where previously only a tree could sprout from a stick, every branch now sprouts roots.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 4 Aura \* Level, 1 Holz \* Level, 1 Wasser des Lebens  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Grove of Oak Trees"`  

## H

### Hail

**Description:**  
In battle, the magician calls upon the elemental spirits of cold and binds them to himself. He can then order them to attack the enemy with hailstones and chunks of ice.
**Type:** Kampfzauber  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Hail`  

### Hangover

**Description:**  
There are more than 512 characters with translation, please reduce the translation content.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 28 Aura, 3 Knotige Saugwurze, 50 Silver  
**Modifiers:**  
**Syntax:** `CAST Hangover <unit-id>`  

### Heal

**Description:**  
It"s not just the medic who can help the wounded in battle. Druids are able to close wounds, set broken bones and regenerate even severed limbs by summoning the elemental spirits of life.
**Type:** Postkampfzauber  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Heal`  

### Hex

**Description:**  
The magician"s target is afflicted by a harmless curse.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] Hex <unit-id>`  

### Hitzeelementar  <!-- TODO -->

**Description:**  
This ritual summons angry heat elementals. A drought is plaguing the country. Trees wither, animals die, and the harvest fails. There is hardly any work to be found in agriculture for day laborers.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 600 Aura  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] Hitzeelementar`  

### Hohe Kunst der Überzeugung  <!-- TODO -->

**Description:**  
From "Wanderings" by Firudin the Wise: "In Weilersweide, near the Wythar harbor, there is a small inn that is rarely visited. It is not known to anyone that until a few years ago this farm was the home of the banished itinerant preacher Grauwolf. After recruiting almost the entire peasantry in one of his infamous fiery speeches, he was convicted of sedition and banished. He was only hesitantly willing to teach me the secret of his persuasiveness."
**Type:** Normal spell  
**Rank:** 5  
**Components:** 20 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Hohe Kunst der Überzeugung"`  

### Homestone

**Description:**  
With this formula, the magician binds the forces of the earth forever into the walls of the castle in which he currently finds himself. Walls that have been strengthened in this way cannot be destroyed either by magic or with heavy artillery, and age also affects them less. The building also offers better protection against attacks with swords and magic.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 50 Aura, 1 permanent Aura  
**Modifiers:**  
**Syntax:** `CAST Homestone`  

### Hymn of Aura Sharing

**Description:**  
With the help of this spell, the magician can transfer his own aura at a ratio of 2:1 to another magician of the same magic area.
**Type:** Normal spell  
**Rank:** 1  
**Components:** 2 Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Hymn of Aura Sharing" <unit-id> <Aura>`  

## I

### Insomnia

**Description:**  
This spell causes insomnia and restlessness in the affected area for a few weeks. Those affected find it much more difficult to learn.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 18 Aura  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] Insomnia`  

## J

### Jugglery

**Description:**  
Cerddor mages are the leading jugglers among the mages, they love to entertain the people and be the center of attention. Even beginners learn the little tricks and magical tricks that can be used to lure and seduce people into opening their wallets very wide, and at the end of the week the juggler will have earned 50 silver per level.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] Jugglery`  

## K

## L

### Lesser Sacrifice

**Description:**  
With this ritual the magician can sacrifice part of his life energy in order to gain magical power. Experienced ritual magicians report that the ritual, once initiated, is difficult to control and the amount of power gained varies greatly. So it is written in the "Book of Blood": "So let He establish the sign of the four elements in the circle of creation and decay and consecrate each one with a drop of blood. Then let He go into the midst of the Eternal Four and let life pass away so that strength can be born."  
**Type:** Normal spell  
**Rank:** 1  
**Components:** 16 Hit points  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Lesser Sacrifice"`  

## M

### Madness of War

**Description:**  
In front of the enemy soldiers, the black magician sacrifices the ten pawns in a bloody, cruel ritual and in this way summons spirits of madness over the enemy troops. They will react confusedly in battle and be unable to follow the orders of their officers.
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 3 Aura \* Level, 10 Bauern  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Madness of War"`  

### Magic Path

**Description:**  
By performing these rituals, the magician is able to summon a powerful earth elemental. As long as this is banished into the ground, no rain will soften the paths and no river will be able to destroy bridges. This means that all travelers receive the same advantages that would otherwise only be offered by a developed paved road network. Even swamps and glaciers can be enchanted this way. The more power the magician puts into the spell, the longer the road lasts.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level, 1 Stein, 1 Holz  
**Modifiers:** Distance  spell, Ship spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Magic Path"`  

### Mahlstrom  <!-- TODO -->

**Description:**  
This ritual summons a great water elemental from the depths of the ocean. The elemental creates a massive whirlpool, a maelstrom, which can severely damage any ships that pass through it.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 200 Aura, 1 Seeschlangenkopf  
**Modifiers:** Seezauber, Ship spell  
**Syntax:** `CAST Mahlstrom`  

### Meditate

**Description:**  
With the help of this spell, the magician can transfer his own aura at a ratio of 2:1 to another magician of the same magic area.
**Type:** Normal spell  
**Rank:** 1  
**Components:** 2 Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST Meditate <unit-id> <Aura>`  

### Mind Probe

**Description:**  
With this spell, the dream weaver penetrates the thoughts and dream world of his victim and can thus spy on his most intimate secrets. His abilities, possessions and party affiliation will no longer be uncertain.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 20 Aura  
**Modifiers:**  
**Syntax:** `CAST "Mind Probe" <unit-id>`  

### Minor Curses

**Description:**  
In the darker alleys they exist, the curses and hexes made to order. But of course the disciple of Draig also offers counterspells. Whether the neighbor"s son is to be drawn into a love spell or the rival is to get pimples and warts, no one likes to admit that they have resorted to such measures. For this service, the magician earns 50 silver per level.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] "Minor Curses"`  

### Miracle Doctor

**Description:**  
If the alchemist cannot help you, you go to the learned Tybied magician. His potions and tinctures help against everything you can"t get otherwise. Whether the cryptic formula under the wooden shoe of the unfaithful husband really helped -well, the farmer who doesn"t know how to read will never know. It definitely helps the magician... fill his wallet. You can earn 50 silver per level in a week.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] "Miracle Doctor"`  

### Miriams flinke Finger  <!-- TODO -->

**Description:**  
There are more than 512 characters with translation, please reduce the translation content.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 20 Aura, 1000 Silver, 1 permanent Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Miriams flinke Finger"`  

### Mob aufwiegeln  <!-- TODO -->

**Description:**  
With the help of this magical song, the magician convinces the farmers of the region to join him. However, the farmers will not leave their homeland and will not give away any of their possessions. Each week some of the farmers will also cast off the spell and return to their fields. How many farmers join the magician depends on the power of his song.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 4 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Mob aufwiegeln"`  

### [[mountain-guard|Mountain Guardian]]

**Description:**  
Creates a guardian spirit that prevents iron and metal mining in glaciers and mountains by non-allied parties (HELP GUARD) as long as it guards the region. The mountain guardian is bound to the location of the summoning.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 3 Aura \* Level  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] Mountain Guardian`  

## N

### Negate Curse

**Description:**  
This spell allows the magician to specifically dispel a specific enchantment on a unit, ship, building or even the region.
**Type:** Normal spell  
**Rank:** 3  
**Components:** 3 Aura \* Level  
**Modifiers:** Distance  spell, Ship spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Negate Curse" ( REGION | UNIT <unit-id> | SHIP <ship-id> | CASTLE <building-id> ) <spell-id>`  

## O

### Opfere Kraft  <!-- TODO -->

**Description:**  
With the help of this spell, the magician can permanently transfer part of his magical power to another magician. He can transfer half of the power used to a magician of the same magic area, and a third to other magicians.
**Type:** Normal spell  
**Rank:** 1  
**Components:** 100 Aura  
**Modifiers:**  
**Syntax:** `CAST "Opfere Kraft" <unit-id> <Aura>`  

## P

### Path of Trees

**Description:**  
Great power lies in places where life pulsates. The druid can collect this power and create a gateway into the world of spiritual beings. The druid can then level*Send 5 units of weight through the gate.
**Type:** Normal spell  
**Rank:** 7  
**Components:** 3 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Path of Trees" <unit-id> [<unit-id> ...]`  

### Pentagramm  <!-- TODO -->

**Description:**  
Exactly at midnight, when the powers of darkness are at their greatest, a black magician can also use his powers to remove enchantments. To do this, he draws a pentagram on the enchanted object and begins with an invocation to the lords of darkness. The gentlemen will help him, but whether he succeeds in solving the spell depends solely on his own strength.
**Type:** Normal spell  
**Rank:** 2  
**Components:** 10 Aura \* Level  
**Modifiers:** Distance  spell, Ship spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] Pentagramm ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Protection from Magic

**Description:**  
This spell places an antimagic field around enemy mages, significantly hindering their spellcasting. Only a few will have the strength to penetrate the field and aid their troops in battle.
**Type:** Pre-combat spell  
**Rank:** 2  
**Components:** 3 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Protection from Magic"`  

### Protective Runes

**Description:**  
If you draw these runes on the walls of a building or on the planks of a ship, it will be more difficult to influence by magic. Each ritual increases the building or ship"s resistance to enchantment by 20%. If several protective spells are placed on top of each other, their effects are added together, but 100% protection cannot be achieved this way. The spell lasts at least three weeks, but depending on the magician"s talent it can last much longer.
**Type:** Normal spell  
**Rank:** 2  
**Components:** 20 Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Protective Runes" ( SHIP <ship-id> | CASTLE <building-id> )`  

## R

### Rain Dance

**Description:**  
Dieses uralte Tanzritual ruft die Kräfte des Lebens und der Fruchtbarkeit. Die Erträge der Bauern werden für einige Wochen deutlich besser ausfallen.  
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:** Distance  spell, Ship spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] Rain Dance`  

### Rain of Rust

**Description:**  
This ritual conjures up a dark storm front that towers ominously over the region. The magical rain will cause all ore to rust. Iron weapons and armor become chipped and rusty. The destructive power of the rain depends on the power invested by the magician. Up to 10 iron weapons can be affected for each level. A ring of power increases the effect like an additional level.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 2 Aura \* Level  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Rain of Rust" <unit-id> [<unit-id> ...]`  

### Read Dreams

**Description:**  
This spell allows the Dreamweaver to enter a unit"s dreams to obtain a report on the surrounding area.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 8 Aura  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] "Read Dreams" <unit-id>`  

### Resist Magic

**Description:**  
This spell increases your natural resistance to magic. A unit protected in this way is also less vulnerable to combat magic. Per level, the magician"s power is enough to protect 5 people.
**Type:** Normal spell  
**Rank:** 2  
**Components:** 5 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] Resist Magic <unit-id> [<unit-id> ...]`  

### Resurrection

**Description:**  
If a warrior dies in battle, his soul begins the long journey to the stars. With the help of a ritual, a dream weaver can attempt to capture the soul and return it to the body of the deceased. Although the spell does not heal physical injuries, the person treated will survive the fight.
**Type:** Postkampfzauber  
**Rank:** 4  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Resurrection`  

### Rindenhaut  <!-- TODO -->

**Description:**  
Dieses vor dem Kampf zu zaubernde Ritual gibt den eigenen Truppen einen zusätzlichen Bonus auf ihre Rüstung. Jeder Treffer reduziert die Kraft des Zaubers, so dass der Schild sich irgendwann im Kampf auflösen wird.  
**Type:** Pre-combat spell  
**Rank:** 2  
**Components:** 4 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Rindenhaut`  

### Ritual der Aufnahme  <!-- TODO -->

**Description:**  
Dieses Ritual ermöglicht es, eine Einheit, egal welcher Art, in die eigene Partei aufzunehmen. Der um Aufnahme Bittende muss dazu willig und bereit sein, seiner alten Partei abzuschwören. Dies bezeugt er durch KONTAKTIEREn des Magiers. Auch wird er die Woche über ausschliesslich mit Vorbereitungen auf das Ritual beschäftigt sein. Das Ritual wird fehlschlagen, wenn er zu stark an seine alte Partei gebunden ist, dieser etwa Dienst für seine teuere Ausbildung schuldet. Der das Ritual leitende Magier muss für die permanent Bindung des Aufnahmewilligen an seine Partei naturgemäß auch permanent Aura aufwenden. Pro Level und pro 1 permanent Aura kann er eine Person aufnehmen.  
**Type:** Normal spell  
**Rank:** 5  
**Components:** 3 Aura \* Level, 1 permanent Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Ritual der Aufnahme" <unit-id>`  

### Rüstschild  <!-- TODO -->

**Description:**  
This ritual, which can be cast before battle, gives your troops an additional bonus to their armor. Each hit reduces the spell"s power, so the shield will dissipate at some point in the fight.
**Type:** Pre-combat spell  
**Rank:** 2  
**Components:** 4 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Rüstschild`  

## S

### Sacred Ground

**Description:**  
This ritual summons various natural spirits into the soil of the region, which guard it from then on. In such a blessed region, the dead will never again leave their graves, and undead that have arisen elsewhere will avoid them whenever possible.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 80 Aura, 3 permanent Aura  
**Modifiers:**  
**Syntax:** `CAST "Sacred Ground"`  

### Save Spoils

**Description:**  
This spell prevents some of the objects that would otherwise be destroyed in battle from being damaged. Losses are reduced by 5% per level of the spell, up to a minimum of 25%.
**Type:** Postkampfzauber  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Save Spoils"`  

### Schlechte Träume  <!-- TODO -->

**Description:**  
This spell allows the Dreamer to disrupt the sleep of all non-allied units (HELP GUARD) in the region to such an extent that they temporarily lose some of their memories.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 90 Aura  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] "Schlechte Träume"`  

### Shadow Knights

**Description:**  
This spell can give the enemy a slightly different image of their own troops. The Shadow Knights have no effective attack and being wounded in battle will destroy them instantly.
**Type:** Pre-combat spell  
**Rank:** 4  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Shadow Knights"`  

### Shield of the Fish

**Description:**  
This spell can give the enemy a slightly different image of their own troops, just like the fish in the water is not where it seems to be. In this way, half of the damage from each hit can be rendered harmless. But the shield can only withstand a few hundred sword blows, after which it will disintegrate. The stronger the magician, the more damage the shield can withstand.
**Type:** Pre-combat spell  
**Rank:** 2  
**Components:** 4 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Shield of the Fish"`  

### Sleep

**Description:**  
This spell causes some enemy combatants to fall asleep. Sleeping fighters do not attack and have poorer defenses, but they wake up as soon as they are hit in combat.
**Type:** Kampfzauber  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Sleep`  

### Shockwave

**Description:**  
This spell causes a wave of pure power to sweep across the enemy ranks. The shock will leave many fighters so dazed that they will be unable to attack for a brief moment.
**Type:** Kampfzauber  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Shockwave`  

### Schöne Träume  <!-- TODO -->

**Description:**  
This spell allows the Dreamweaver to affect the sleep of all allied units in the region, giving them a bonus in all talents for a period of time.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 80 Aura  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] "Schöne Träume"`  

### Segen der Erde  <!-- TODO -->

**Description:**  
This harvest ritual improves the yields of working farmers in the region by one piece of silver. The more power the druid invests, the longer the spell lasts.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:** Distance  spell, Ship spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Segen der Erde"`  

### Segne Mallornstecken  <!-- TODO -->

**Description:**  
This ritual increases the effect of the magical potion many times over. Where previously only a tree could sprout from a stick, every branch now sprouts roots.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 6 Aura \* Level, 1 Mallorn \* Level, 1 Wasser des Lebens  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Segne Mallornstecken"`  

### Segne Steinkreis <!-- TODO -->

**Description:**  
This ritual blesses a stone circle that must first be built from stones and some wood. The Druid"s Blessing turns the circle into a powerful site of magical activity, providing protection from magic and increased aura regeneration. It is said that virgins encountered strange creatures around stone circles.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 350 Aura, 5 permanent Aura  
**Modifiers:**  
**Syntax:** `CAST "Segne Steinkreis" <building-id>`  

### Shapeshift

**Description:**  
With the help of this arcane ritual, the dream weaver is able to disguise the true form of a group. To inexperienced observers, she then appears to belong to a different race.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] Shapeshift <unit-id> <race>`  

### Silence Dissonance

**Description:**  
Each enchantment affects the Life Song, weakening and distorting it. The skilled bard can attempt to capture and amplify the song of life and erase the changes from the song.
**Type:** Normal spell  
**Rank:** 2  
**Components:** 5 Aura \* Level  
**Modifiers:** Distance  spell, Ship spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Silence Dissonance" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

### Sog des Lebens <!-- TODO -->

**Description:**  
A druid who has fallen into the world of spirits can use this spell to level up*Send 5 units of weight back to a forest on the material world.
**Type:** Normal spell  
**Rank:** 7  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Sog des Lebens" <x> <y> <unit-id> [<unit-id> ...]`  

### Song of Confusion

**Description:**  
This magical song comes from the ancient songs of cats and, when used before a fight, can bring decisive strategic advantages. Anyone who comes under the influence of this song will not pay attention to the melody of their surroundings, their mind will become confused and give in erratically to sudden inspirations. Well-ordered armies are said to have suddenly found their archers far in front and their cavalry playing cards with the camp guards (or their leader sleeping in the long-abandoned camp, as is actually said to have happened in the Great Wars of the Old World)..  
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Song of Confusion"`  

### Song of Courting

**Description:**  
From "The Songs of the Ancients" by Firudin the Wise: "This seductive little melody and a few insinuating words overcome the distrust of the peasants in an instant. They will enthusiastically join you and leave their house and yard in ruins themselves."
**Type:** Normal spell  
**Rank:** 5  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Song of Courting"`  

### Song of Fear

**Description:**  
This war song sows panic in the enemy"s front lines and thus significantly weakens their fighting strength. Fear will weaken their sword arm and fear will paralyze their shield arm.
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 5 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Song of Fear"`  

### Song of Generosity

**Description:**  
This cheerful song will spread like a rumor throughout the region and put the whole world in a celebratory mood. Taverns and theaters everywhere will be full and even the beggars will be fed.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 2 Aura \* Level  
**Modifiers:** Distance  spell, Ship spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Song of Generosity"`  

### Song of Healing

**Description:**  
It"s not just the medic who can help the wounded in battle. The bards know various songs that support the body"s self-healing powers. This song can close wounds, set broken bones and regenerate even severed limbs.
**Type:** Postkampfzauber  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Song of Healing"`  

### Song of Seduction

**Description:**  
This song can be used to charm a unit into giving most of their cash and possessions to the bard. However, she always keeps what she needs to survive.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 12 Aura  
**Modifiers:**  
**Syntax:** `CAST "Song of Seduction" <unit-id>`  

### Song of Terror

**Description:**  
A very powerful song from the traditions of cats that penetrates deep into the hearts of enemies and robs them of courage and hope. Fear will make them tremble and panic will dominate their thoughts. Full of fear, they will try to escape the horrible songs and flee.
**Type:** Kampfzauber  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Song of Terror"`  

### Song of War

**Description:**  
Like many magical songs, this one also comes from the ancient knowledge of cats, who have always known about the powerful effects of the voice. This song whips up the mood of the warriors, even driving them into wild frenzy and bloodlust. Regardless of their own pain, they will fight to the death and never flee. While their attack is intensified, they pay little attention to themselves.
**Type:** Pre-combat spell  
**Rank:** 4  
**Components:** 5 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Song of War"`  

### Sound out

**Description:**  
If the unit succumbs to the spell, it will tell the magician everything it knows about the region in question. If there is no one from her party in the region, she has nothing to report. She can also only tell what she could see herself.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 4 Aura, 100 Silver  
**Modifiers:**  
**Syntax:** `CAST "Sound out" <unit-id> <x> <y>`  

### Steal Aura

**Description:**  
With the help of this spell, the magician can withdraw his aura from another magician against his will and supply it to himself.
**Type:** Normal spell  
**Rank:** 3  
**Components:** 2 Aura \* Level  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Steal Aura" <unit-id>`  

### Strong Wall And Sturdy Gate

**Description:**  
With this formula, at the beginning of a fight, the magician binds some elemental spirits of the rock into the walls of the building in which he is currently located. The building then offers better protection against attacks with the sword and magic.
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Strong Wall And Sturdy Gate"`  

### Störe Astrale Integrität <!-- TODO -->

**Description:**  
This spell causes severe disruption to the astral space. Within an astral radius of level/5 regions, all astral beings who cannot resist the spell are thrown out of the astral plane. Astral contact with all affected regions is disrupted for level/3 weeks.
**Type:** Normal spell  
**Rank:** 4  
**Components:** 140 Aura  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Störe Astrale Integrität"`  

### Summon Earth Elemental

**Description:**  
With this ritual, the druid summons an elemental spirit of the earth and causes it to cause the earth to tremble. This earthquake will damage all buildings in the region.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 25 Aura, 2 Laen  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] "Summon Earth Elemental"`  

### Summon Familiar

**Description:**  
At some point in his wanderings, an experienced magician will encounter an unusual specimen of a species that will join the magician.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 100 Aura, 5 permanent Aura  
**Modifiers:**  
**Syntax:** `CAST "Summon Familiar"`  

### Summon Shadowdemons

**Description:**  
Using dark rituals, the magician summons demons from the sphere of shadows. These feared creatures can move almost invisibly among the living, but their dark aura can be felt by everyone. Shadow demons are feared opponents in battle. They are difficult to hit and drain their opponent"s power.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 3 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Summon Shadowdemons"`  

### Summon Storm Elemental

**Description:**  
Summoning elemental spirits of storms is an ancient ritual. The druid banishes the elementals into the sails of the ships, where they help carry the ship over the waves at high speed. The more power the druid invests in the spell, the greater the number of elemental spirits that can be banished. An elemental spirit is required for each ship.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 6 Aura \* Level  
**Modifiers:** Seezauber, Ship spell  
**Syntax:** `CAST [LEVEL n] "Summon Storm Elemental" <ship-id> [<ship-id> ...]`  

### Summon Water Elemental

**Description:**  
With this ritual, the magician forces the elemental spirits of the water into his service and gets them to carry the specified ship through the water more quickly. In addition, the ship is not affected by unfavorable winds or currents.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] Summon Water Elemental <ship-id>`  

### Süße Träume <!-- TODO -->

**Description:**  
This spell -the use of which is strictly forbidden in most cultures -triggers an uncontrollable desire for physical love in the victim. The affected individuals will rush headlong into a love affair, too blinded by desire to think of anything else. Most of the time they regret it a few weeks later...
**Type:** Normal spell  
**Rank:** 5  
**Components:** 5 Aura \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Süße Träume" <unit-id> [<unit-id> ...]`  

## T

### Timber Wolves

**Description:**  
Over the course of their lives in nature, quite a few Druids become friends with the oldest friends of the great peoples. They learn to summon many of their friends to aid them in battle with a single howling call.
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Timber Wolves"`  

### Tiredness

**Description:**  
This combat spell causes some enemies to suffer severe fatigue during combat. The soldiers sometimes oversleep their attack and defend themselves poorly.
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 4 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Tiredness`  

### Tod des Geistes <!-- TODO -->

**Description:**  
With this spell the magician attacks the minds of his opponents directly. A blast of astral and electrical energy hits the opponents; if magic resistance is broken, a victim permanently loses part of their memories. If it falls victim to this spell too often, it can die.
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Tod des Geistes"`  

### Todeswolke <!-- TODO -->

**Description:**  
With a dark ritual and sacrificing his own blood, the black magician summons a great spirit from the elemental plane of poisons. The spirit manifests itself as a bright green cloud over the region and will harm all who come into contact with it.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 40 Aura, 15 Trefferpunkte  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] Todeswolke`  

### Tor in die Ebene der Hitze <!-- TODO -->

**Description:**  
This powerful ritual opens a gateway into the elemental plane of heat. A great drought is coming to the country. Farmers, animals and plants in the region are fighting for survival, but only half of all living things can survive such a drought. The region can be affected by the consequences of such a drought for years to come.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 800 Aura  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] "Tor in die Ebene der Hitze"`  

### Transfer Aura

**Description:**  
With the help of this spell, the magician can transfer his own aura to another magician of the same magic area at a ratio of 2:1 or to a magician of another magic area at a ratio of 3:1.
**Type:** Normal spell  
**Rank:** 1  
**Components:** 1 Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Transfer aura" <unit-id> <Aura>`  

### Transfer Power

**Description:**  
With the help of this spell, the magician can transfer his own aura at a ratio of 2:1 to another magician of the same magic area.
**Type:** Normal spell  
**Rank:** 1  
**Components:** 2 Aura  
**Modifiers:** Ship spell  
**Syntax:** `CAST "Transfer Power" <unit-id> <Aura>`  

### Traumbilder entwirren

**Description:**  
This spell allows the dream weaver to distinguish and unravel the natural and forced dream images of a person, building, ship, or region.
**Type:** Normal spell  
**Rank:** 2  
**Components:** 6 Aura \* Level  
**Modifiers:** Distance  spell, Ship spell  
**Syntax:** `CAST [REGION x y] [LEVEL n] "Traumbilder entwirren" ( REGION | UNIT <unit-id> [<unit-id> ...] | SHIP <ship-id> [<ship-id> ...] | CASTLE <building-id> [<building-id> ...] )`  

## U

### Undead Heroes

**Description:**  
This ritual binds the already escaping souls of some battle victims to their dead bodies, resurrecting them to undead life. Whether they previously fought on the enemy"s side or their own is irrelevant to the ritual.
**Type:** Postkampfzauber  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Undead Heroes"`  

### Unheilige Kraft <!-- TODO -->

**Description:**  
This ritual is only passed on to the adepts in the dark academies in whispers, as it is one of the darkest ever written down. By invoking unholy demons, the power of the living dead is amplified and they transform into undead monsters of great power.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 10 Aura \* Level, 5 Bauern \* Level  
**Modifiers:**  
**Syntax:** `CAST [LEVEL n] "Unheilige Kraft" <unit-id> [<unit-id> ...]`  

### Unspeakable Horrors

**Description:**  
Before battle, the dream weaver conjures up terrifying illusions that cause many opponents to panic. Those affected will try to escape from the mirages.
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 1 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Unspeakable Horrors"`  

## V

## W

### Whirlwind

**Description:**  
This incantation opens a gate into the plane of the elemental spirits of the wind. Strong winds or even storms immediately arise in the area around the gate and hinder all archers in a battle.
**Type:** Pre-combat spell  
**Rank:** 5  
**Components:** 15 Aura  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] Whirlwind`  

### Winds of Rust

**Description:**  
This ritual conjures up a dark storm front that towers ominously over the region. The magical rain will cause all ore to rust, destroying many of the enemy's weapons.
**Type:** Kampfzauber  
**Rank:** 5  
**Components:** 2 Aura \* Level  
**Modifiers:**  
**Syntax:** `COMBATSPELL [LEVEL n] "Winds of Rust"`  

### Wurzeln der Magie <!-- TODO -->

**Description:**  
With the help of this elaborate ritual, the druid allows part of his power to flow permanently into the soil and forests of the region. This will change the balance of nature in the region forever, and in the future only the demanding but strong mallornas will thrive in the region.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 250 Aura, 10 permanent Aura, 1 Tiegel mit Krötenschleim  
**Modifiers:** Distance  spell  
**Syntax:** `CAST [REGION x y] "Wurzeln der Magie"`  

## Z

### Zeitdehnung <!-- TODO -->

**Description:**  
This practical application of theoretical knowledge of space and time makes it possible to change the flow of time for some people. People modified in this way get twice as many movement points and twice as many attacks per round for a few weeks.
**Type:** Normal spell  
**Rank:** 5  
**Components:** 5 Aura \* Level  
**Modifiers:** Ship spell  
**Syntax:** `CAST [LEVEL n] Zeitdehnung <unit-id> [<unit-id> ...]`  

## See also

- [[list-of-spells]]

<!-- From [https://wiki.eressea.de/index.php?title=Zauberbeschreibungen\_E2&oldid=9278] -->

[Dragons]: ./monsters.md#dragons
[Ents]: ./monsters.md#ents
