# Races

As well as humans, there are many other races (faction types) in Eressea. You need to choose one for your faction. Each race has advantages and disadvantages which translate into [bonuses and penalties] in certain skills, and sometimes special abilities; each race has different [recruitment costs][bonuses and penalties]. As a general rule, a person weighs 10 weight units (WU or GE) and can carry 5.4 WU/GE. Trolls, goblins and various monsters are exceptions.

At the start of the game, you must choose the race you want to play. This race is chosen when you register and cannot be changed afterwards. So think carefully before making your choice.

For a quick overview, see the [table of racial modifiers][bonuses and penalties].

## Demons

Demons are cruel and unpredictable. They devour the local peasants and always surprise by acquiring new abilities or losing them.

**Attention!** Demons are extremely unsuitable for inexperienced Eressea players!

- Volatility: All skills with at least one skill level (before racial malus) have a 25% chance of shifting. The skill can lose up to 3 weeks of learning (40%), or rise up to 3 weeks of learning (60%). No skill can ever fall below level 0.
- Infernal Hunger: Demons eat peasants every turn. Demons that do not receive food (not enough peasants) lose hit points and are subject to skill reduction according to the normal [starvation rule].
- Ethereal Creature: Demons are not [recruited] from the peasant population (they aren't deducted from the peasant pool). However, the normal recruitment limits still apply for balance reasons.
- Ethereal Creature: When a demon unit gives away men with [`GIVE 0`], these people are not added to the peasant population in the region.
- Intrinsic Disguise: Demons can [change their appearance] to become that of any other player race.
- Panic: In close combat, taking a hit from a demon causes panic in the victim. The person receives a modifier of −1 to all combat skills (not the unit).
- Regeneration: Wounded demons regenerate 7,5% of their hit points per turn.

## Elves

The magical people of the faery kingdom aren't built for heavy labor, but they have a knack for nature as well as hidden things, and their archers are almost as feared as their magicians.

- Green Thumb: Each elf (up to 1/8 of the [region's maximum] working population, e.g. 250 in a swamp) increases the chance of a tree (including mallorn trees) to drop a seed in a summer or autumn week. This can make quite a difference depending on the number of elves.
- Forest Dwellers: In forest regions, elves have a skill bonus of +1 to stealth and perception, and +2 to tactics.
- Magicians: Elf factions can have 1 additional [magician], allowing them to have a maximum of 6.
- Elf magicians regenerate aura 25% faster.
- Expert Archers: Elves cause 1 additional damage point when using bows.
- Only elves can build [elven bows].

## Goblins

Goblins are small and weak on their own; they prefer to rely on cunning or superior numbers. Their motto is "quantity instead of quality".

- Overpowering: When their numbers are ten times those of the opponent, goblins get a +1 attack bonus.
- Midget: Goblins weigh only 6 WU/GE, but they can carry only 4.4 WU/GE.
- Master Thieves: Goblins with level 4 or higher in stealth will always [steal] at least 50 silver, even if they were discovered.
- Unarmed Defense: Unarmed goblins do not get the usual -2 penalty on defense.
- Stubborn: A wounded goblin will regenerate 10% of their hit points.

## Halflings

Halflings are small fellows with hairy feet. They are good traders and know how to entertain the peasants. They are good builders, but prefer to leave horses and [ships] to others. Weaponry is not one of their strengths.

- Halflings who try to [flee] in a fight have a basic chance of 50% (all other races 25%). The maximum chance for them is 90% (otherwise 75%, see [`COMBAT FLEE`]).
- Dragonslayers: Halflings get a +5 bonus on attack and damage when fighting against [dragons].
- Always Hungry : Halflings suffer more damage from starvation than other races (between 8 and 17 hit points (1d10+7)).

## Insects

Most insectoid warriors live in organized hives. They hate the cold and prefer the swamps and deserts of Eressea. Their hard carapace will protect them in the battlefields, their skills and discipline make them renowned teachers.

**Attention!** Insects not very suitable for inexperienced Eressea players!

- Cold Blooded: In deserts and swamps, insects get +1 on all skills they still have at least at 1, in mountains and glaciers they get -1.
- Summer Creatures: Insects cannot enter glaciers and cannot be recruited there. Insects that nevertheless enter a glacier lose hit points and suffer skill halving according to the normal [starvation][starvation rule] rule.
- Hibernation: During the winter months of hearth fire, icewind and snowbane, insects can only recruit in deserts. However, [alchemists] can produce a [potion] of "nest warmth" that makes recruitment in other terrains possible.
- Carapace Armor: Insects are protected by their natural armor. This natural armour will be halved if the insects are wearing additional armor. (see this [combat table]).
- Tacticians: Insects get a bonus on the [tactics] skill when appearing in large numbers. An insect tactician gets (log<sub>10</sub> (amount of fighters in their army)) - 1 to their tactics skill. This can also result in a penalty if there are very few fighters! Mind that fighters in different [groups] usually appear in different armies!
- Nomad Traders: Insects can [trade] in deserts and swamps without needing castles.

## Cats

Known for their enhanced senses, the cat people are excellent spies and master guards. But, like elves, they do not like heavy labor.

- Seven Lives: When killed, cats have a 1/7 chance of surviving. By some miracle of nature, they will also be restored to full hit points.
- Silent Hunters: Cats cannot use platemail.
- Evasiveness: Cats receive a +1 bonus on defense.

## Aquarians

Aquarians are at home in the water, but they feel uncomfortable in the mountains. They build and drive ships as easily as they were building blocks, while other tasks do not come to them so naturally.

- Expert Sailors: All ships commanded by an aquarian captain belonging to an aquarian faction [move] by 1 extra region per week.
- Sea dwellers: Aquarians can issue [long orders] while on a ship sailing on the ocean. Attention, this has some implicit consequences: for example, aquarians on a ship in an ocean region adjacent to a land region can move to the land region, see [swimming].
- Fishermen: Up to 100 aquarians per ocean region can earn 10 silver each per turn with the [`WORK`] order.

## Humans

Humans can do a bit of everything. They don't have any really bad skills, but they don't really excel at anything either. They can therefore make up for the weaknesses of their allies, even though they have no specialization.

- Migrants: Human factions are the only ones who are allowed to have people of another race in their ranks, although mixing different races in one unit is not possible. However they cannot recruit these themselves, but must [get them][`GIVE 0`] from other factions. There are no migrants with [expensive skills] like magic, alchemy, herbalism, espionage, or tactics.

The number of *migrants* is calculated as 20 × log<sub>10</sub> (persons in the faction ÷ 50). If you have to many migrants, for example after a battle, they are not removed, but you cannot add any more either. The maximum number of migrants is shown in your report. It is almost identical to the number of [heroes] for large factions. The following table has some examples.

Migrants

|                       |   |    |    |    |    |    |    |     |     |      |      |       |        |         |
|-----------------------|---|----|----|----|----|----|----|-----|-----|------|------|-------|--------|---------|
| people in the faction | 1 | 56 | 57 | 63 | 71 | 80 | 89 | 159 | 500 | 1000 | 5000 | 50000 | 500000 | 5000000 |
| migrants              | 0 | 0  | 1  | 2  | 3  | 4  | 5  | 10  | 20  | 26   | 40   | 60    | 80     | 100     |

## Orcs

Orcs start their life as fighters, and usually end it as fighters. They intuitively know how to wield weapons. They like contacting other factions with triple superiority.

- Born Fighters: All newly recruited orcs start out with a level in the melee and polearm skills.
- Laziness: Orcs earn less silver than other races with the [`WORK`] order.
- Easy Recruits: For two recruited orcs only one peasant is subtracted from the peasant pool of the region. Thus you can recruit twice the recruitment limit of a region. Fractions are rounded up.
- Likewise, for every two orcs given to the peasants (see the [`GIVE 0`] order) only one peasant is added to the peasant pool of the region (rounded down this time).
- Dangerous: Unarmed orcs do not fight with a -2 penalty in close combat like other races, but with (best close combat skill - 3). They still need weapons to collect taxes.
- Orcs are slow thinkers and generally learn all non-weapon skills somewhat slower than other races.

## Trolls

These walking boulders are among the strongest creatures of Eressea. They love to work with rocks, horses are afraid of them, and swimming has never been known as one of the troll's favorite pastimes.

- Heavy Weights: Trolls are strong and they can lift up to 10.8 WU/GE, but they also weigh 20 WU/GE, twice as much as other races.
- Foot Soldiers: While technically trolls can ride, there is no troll cavalry, and thus no bonus for riding in combat (This has no effect on the transport of goods and the movement speed of mounted trolls).
- Quarrying: Only 75% of the stones [quarried] by trolls are subtracted from the amount of stones available in a region. This effect is cumulative with a [quarry].
- The enemy's cavalry only gets a +1 bonus against trolls instead of the normal +2.
- Horsepower: Trolls are the only race able to use carts without horses. Four trolls can pull a cart, making them less dependent on horses, but they can only move one region (without a road). This is explained with the [RIDE] order.
- Unarmed Combat: Unarmed trolls cause 2−6 points of damage.
- Regeneration: Wounded trolls regenerate at 7,5% of their hit points.

## Dwarves

Their homes are the mountains, their weapons are famous, and their fortresses are known for their strength. However, they treat magic and horses with equal skepticism, and their sailing skills are among the worst in the world.

- Efficient Miners: Dwarves are efficient miners. Fore every 5 iron mined by them, only 3 are subtracted in a region, or only 60%. This effect can be combined with that of a mine, dramatically increasing the output of a mountain (see [mine] and [mining][quarried]).
- Mountain Dwellers: In mountains, glaciers and ice bergs, dwarves get +1 to their [tactics] skill.
- Dwarves [mages][magician] regenerate aura 50% slower.

Continue reading: [Racial skill modifiers].

[Racial skill modifiers]: ./skills-modifiers.md "Talentmodifikatoren"

<!-- From [https://wiki.eressea.de/index.php?title=Rassen/en&oldid=16644] -->

[bonuses and penalties]: ./skills-modifiers.md "Talentmodifikatoren"
[starvation rule]: ./silver.md#starvation "Starvation"
[recruited]: ./silver.md#recruiting "Recruiting"
[`GIVE 0`]: ./cmd-give.md "GIVE"
[change their appearance]: ./cmd-hide.md "HIDE"
[region's maximum]: ./world.md "Welt"
[magician]: ./magic.md "Magie"
[elven bows]: ./war-tables.md#waffeneigenschaften "Warstabellen"
[steal]: ./camouflage.md "STEAL"
[ships]: ./ships.md "Ships"
[flee]: ./war.md#fleeing "War"
[`COMBAT FLEE`]: ./cmd-combat.md "COMBAT"
[dragons]: ./monsters.md#dragons "Dragons"
[alchemists]: ./skills-list.md "Skills list"
[potion]: ./alchemy.md "Tränke"
[combat table]: ./war-tables.md#rasseneigenschaften "Warstabellen"
[tactics]: ./tactic.md "Taktik"
[groups]: ./cmd-group.md "GROUP"
[trade]: ./silver.md#trade "Silver"
[move]: ./travel.md "Reisen"
[long orders]: ./commands.md "Orders"
[swimming]: ./sailing.md#swimming "Swimming"
[`WORK`]: ./cmd-work.md "WORK"
[expensive skills]: ./skills.md "Skills"
[heroes]: ./cmd-promote.md "PROMOTE"
[quarried]: ./resources.md#about-mining "Resources"
[quarry]: ./buildings-others.md#quarry "Quarry"
[RIDE]: ./cmd-ride.md "RIDE"
[mine]: ./buildings-others.md#mine "Mine"
