---
# cSpell:locale en
alias:
    - war
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD042 MD052 -->
# War

Conflict is bound to arise in Eressea.  
There will be quarrels over money, over regions, over taxes, over trade routes and so on.  
That's why you should always look for friends and allies, because "friends come and go, enemies multiply".  

## The sides in a battle

The [`ATTACK`][cmd-attack] order launches an attack against the opponent.  
`ATTACK` orders are executed in random order.  
During an attack, units from all sides gather in the area and fight each other individually (person by person).  
A battle lasts a maximum of six turns: five regular combat turns and possibly also turn 0 (zero), the [tactics turn][tacticians-round].

The attacking side consists of all units that have given `ATTACK` orders against one or more units of the defenders.

<!-- TODO: check links in this sentence in wiki -->
The defenders' camp is made up of the units that have been attacked, on which the opponent has therefore given the order `ATTACK`*`unit-id`*, and with all the units of the attacked faction that are ready to fight.  
Therefore those in [`COMBAT`][cmd-combat], [`COMBAT AGGRESSIVE`][cmd-combat], [`COMBAT REAR`][cmd-combat] or [`COMBAT DEFENSIVE`][cmd-combat].  
In addition, all combat-ready units of factions allied to the factions under attack, i.e. those that have put [`HELP COMBAT`][cmd-help] with the faction under attack, help out.

So there are different reasons why a unit takes part in combat.  
These are, listed in order of priority:

1. The unit ready to fight attacks another unit.
   In this case, it takes part in the combat in any case.
2. The unit is attacked by another unit.
   Then it joins the [combat rows][combat-rows] according to its combat status.
3. A unit whose faction is being attacked.
   The unit then takes part in the combat if it has not set `COMBAT NOT` or `COMBAT FLEE`.
   In the latter case, it does not [flee][fleeing] as it is not directly threatened.
4. A unit from an allied faction (that is, a faction to which `HELP COMBAT` has been set) is attacked by someone.
   The unit then takes part in the combat, unless it has set `COMBAT NOT` or `COMBAT FLEE`.
   Again, a unit with `COMBAT FLEE` will not run away, as it is not exposed to a direct threat.

So allies only automatically help defenders and *only if the defenders have not attacked themselves*.  
Attacked units defend themselves with all the units of the faction, unless they explicitly stay out of the fight.  
For the attacker, combat status is irrelevant for the purpose of joining the battle: apart from defenders, only units that have given an [`ATTACK`][cmd-attack] order are engaged in combat.  
However, units that have set [`COMBAT NOT`][cmd-combat] or [`COMBAT FLEE`][cmd-combat] cannot attack.

So, to jointly attack an enemy, each attacking faction must attack at least one of the enemy's units.  
To defend together against attackers, all the defending factions do is assist each other (HELP).

Basically anyone to whom [`HELP COMBAT`][cmd-help] has been assigned, and who has not attacked anyone to whom [`HELP COMBAT`][cmd-help] has also been assigned is considered an ally.

**Example 1:**

A helps B and C.  
C attacks B, which is why A is involved in the battle: B is an ally.  
Faction C is not considered an ally because it is attacking an ally.

Who's fighting who now?

I fight my enemies.  
My enemies are factions that attack me, that I attack, or that attack an ally (according to the definition just given).

**Example 2:**

A helps B and C.  
B and C attack each other.  
In this situation, A helps neither B nor C, because neither of them is considered an ally and neither is an enemy of A.

**Example 3:**

A attacks B and C.  
If B and C are not allies, they still help each other against A, because A is a common enemy.  
So, if B still has front-line troops and C only has archers, B's troops move in front of C to protect them.  
Exception: If B and C are enemies, e.g. because B is fighting against an additional ally D of C, then they do not help each other, not even against A.

**Example 4:**

A and B attack C.  
In this case they help each other against C (even if they are not allied), since they have a common enemy.

Player experience:In fact, it's even more complicated.

!!! warning
    Badly specified help statuses or ATTACK orders have already led to battles with unexpected outcomes.  
    Allies have stood by and done nothing or have even fought amongst themselves.  

There are a few tips to help you **avoid the biggest blunders**:

- You should regularly check the help statuses for all your allies.
  `HELP ALL` is preferable for anyone you **might** fight.
  Mistrust often does damage here.
- If possible, there should only be one [`GROUP`][cmd-group].
- In your faction, either all the combat units should have the ATTACK order, or none at all.
  If only some of your units attack, the rest may not take part in the combat if an ally is attacked.
- It is recommended that you attack all enemy units.
  You should attack *at least* one unit from each enemy faction.
- Note also that faction stealth doesn't always make it clear who really belongs to which faction.
  Another strategy might be to attack just one enemy unit at a time, hoping that the opponents' HELP statuses create some confusion.
  We won't judge here whether this approach is honorable.

## The battle

A battle lasts five combat rounds plus a possible tactics round.  
In each combat round, the combatants strike in a random order.

Note that persons taking part in a battle (the persons listed in the battle report, i.e. attacked or attacking) cannot execute other long orders.  
The exceptions are [combat at sea][combat-on-and-with-ships] and combat in regions which, *at the start of combat*, are guarded by at least one unit of its own faction or a unit which has [`HELP GUARD`][cmd-help] towards the combatant's faction.  
In this case, other long orders are possible.

### Combat rows

In battle, there are four combat rows.  
These are only made up of units that are actually participating in combat (see above).  
For more information on combat status, see [`COMBAT`][cmd-combat].

1. row: This is where you'll find all the units that have set [`COMBAT`][cmd-combat] or [`COMBAT AGGRESSIVE`][cmd-combat].
2. row: This is where you'll find all the units that have set [`COMBAT REAR`][cmd-combat] or [`COMBAT DEFENSIVE`][cmd-combat]
3. row: This is where you'll find all the units that have set [`COMBAT NOT`][cmd-combat].
4. row: This is where you'll find all the units that are simply trying to escape.
   So those that have set [`COMBAT FLEE`][cmd-combat] and those that have lost an appropriate number of hit points (see also [fleeing]).

Only the first two combat rows actively take part in the battle, i.e. they can strike, shoot and be hit.  
Units that are not combat ready and are directly attacked only really take part in the battle when one of the front rows is overrun.  
Fleeing units naturally try to escape (see [fleeing][fleeing]).

Units fighting in the 2nd row can only be attacked directly in close combat when they reach the 1st row (this can happen, for example, when the 1st row is overrun, see below).  
Against opposing ranged attacks, they defend with their best combat skill.

Magicians' combat spells can be cast from behind and from the front line; apart from that, they will arm themselves and fight like everyone else.

### Overrun

If a faction and its allies have more than three times as many persons in the front row as their opponents, the 1st row is overrun.  
All opposing 2nd row units must move up to the first row.  
The 3rd row then moves up to the 2nd row and takes part in the fight.  
If there are still not enough people in the 1st row, the following rows move up until there are enough people in the 1st row.  
This distribution is checked before each combat round.

## To arms

Now, the units arm themselves.  
Each person in a unit equips themselves with a melee weapon, a ranged weapon and armor, according to their skills.  
They choose the weapons that give them the highest Attack and Parry scores.  
Mages who have chosen a combat spell use it to attack.  
However, for defense, they will need a weapon (and an appropriate combat skill), otherwise they will be considered [unarmed][bonuses-and-mali].

!!! warning "Beware"
    Unused weapons or armor are not automatically redistributed to unarmed or unequipped units.

During combat, you no longer change weapons, unless it is possible to take a better weapon from someone in the same unit who has already died (the surviving combatants each use the best weapon sets available).

A ranged combatant who suddenly finds himself in the front row must, if attacked, grab a melee weapon (if the have one and if they have the corresponding skill at least at level 1), otherwise they defend themselves [unarmed][bonuses-and-mali].

**Example:**

A unit of 20 persons has 15 swords, 10 shields and 5 chainmails.  
So 5 people will fight with a sword, a shield and a chainmail, 5 others with a sword and a shield, 5 with a sword only and the last 5 fighters will remain unarmed.  
A unit of 10 people with 10 swords and 10 axes will fight with swords, because they have a better bonus, even if they probably inflict less damage!

## Tactician's round

Before the battle, the best [Tactician][tactics] of all participating units is chosen.  
A tactician fighting in the 1st row receives a +1 bonus to his "tactics" skill.  
If he is in the 3rd or 4th row, his level is reduced by 1.  
In order to leave an element of "form of the day" and luck, each tactician also receives a random bonus which starts at 0 and which, in pure theory, can become very significant, the probability being lower and lower as the bonus increases.

The side with the best tactician can attack on turn 0 (called the "tactician's turn") without the enemy being able to react.  
The number of attacks made depends on the difference between the best tactics score of the winning side and that of the losing side: For each point's difference, each person has a 10% chance of attacking on the tactician's turn.

**Example:**

Camp A has one person with tactics 4 in the first row.  
Camp B has 10 people with tactics 4 in the third row.  
Therefore, side A effectively has 5 and side B 3.  
Without the random bonus, each person on side A would have a 20% chance of attacking during the tactician's turn.  
If the person on side A rolls a bonus 0, at least one person on side B must roll a 2.  
Otherwise, side A has the tactician's turn.  
Let's suppose that the best result obtained on the roll by camp B is a 5 (this is unlikely, but quite possible).  
The difference for side B is therefore (3 + 5) - (5 + 0) = 3.  
Each person on side B then has a 30% chance of attacking on turn 0.  
For a group of 10, this can range from 0 to 10 people, but the average is around 3 attacks.

## Heroes

Heroes are particularly powerful fighters.  
They must have been previously designated with the order [`PROMOTE`][cmd-promote].  
Heroes can attack 5 times per combat round.

Warning! This does not apply to magic attacks or to crossbows and catapults.

For more information, see [`PROMOTE`][cmd-promote].

## The fight between two persons

In each battle, armies face each other person by person, regardless of their number.  
The procedure is as follows:

- The attacker's attack and the defender's parry are (initially) as high as their weapon skill level.
- Add bonuses and penalties: Add any [bonuses and penalties][bonuses-and-mali] to the attacker's attack and the defender's parry.
- If the attacker is a ranged fighter, the opponent's modified parry value is halved.
- The basic hit probability (BT) of an attacker is 30%.
- Subtract values from each other: For every point difference between the attacker's attack and the defender's parry, the BT is now increased or decreased by 5%.
  The real chance of hitting is therefore calculated as follows: (Attack(attacker)-Parry(defender)) \* 5% + 30%.
- Beginner's luck: If the attack fails, the attacker has an additional 10% chance of converting his attack after all: He can strike a second time with a 90 to 99% (chance) increased chance of hitting.
  This gives severely disadvantaged fighters the opportunity to get at least a few random hits.

Each person attacks once per combat round (except [Heroes][cmd-promote] and some monsters).

When a fighter manages to hit his opponent, he inflicts damage.  
Different weapons inflict different amounts of damage (damage points, see [Weapon characteristics][weapons-summary-table]).  
It's also worthwhile having high levels of skill in weapon mastery: if you have more skill levels than your opponent, the damage inflicted by a hit increases by one point for every two skill levels difference.  
Only skill levels are considered, and the bonuses provided by horses, castles, etc. do not count.  
This applies to both ranged and close combat.  
In addition, there is a certain chance, depending on the level difference, of receiving a critical hit that can cause up to five times more damage.

If a person has received more damage than he can "take", he dies (see [races-and-their-characteristics] the different hits taken during the fight are added together).

When a fighter wears armor, it can absorb some (or all) of the damage points.  
However, armor makes the fighter less mobile and increases his chances of being hit (see [this armors table][armors-summary]).  
Against crossbows, armor is only half effective (rounded down).

Some creatures or weapons are also able to cause magical damage.  
Normal armor is ineffective against magical damage.  
Only the [Magic Resistance][war-tables-magic-resistance-id] counts, which can be increased by specific items and spells.

[Endurance][skill-endurance-id] skill allows you to harden your body and take more damage before dying (see [this table][table-endurance-id]).

### Ranged combat

Ranged weapons and catapults can be used effectively in the second row.  
There, they will be protected from your opponent's hand-to-hand combatants by your front row.

Ranged fighters can also fire into the opposing second row.  
They choose a target at random from among all the enemies in the first or second row.

Crossbows can also pierce armor: against a crossbow shot, the armor is only half effective (rounded down).

The table below shows the differences between ranged weapons.  
Bows are very difficult to use (offensive bonus -2), but can be used in every round of combat.  
Crossbows are much easier to use (OB 0), but can only fire every third round of combat.  
Catapults always fire in the first round of combat only (either the tactics round or round 1) and inflict heavy damage.

Against ranged weapons, those being attacked only defend with half their skill level.  
Units in the front row defend with their full skill level if the ranged combatant is also in the front row.

!!! warning "Attention"
    If a ranged fighter gets into the front line (e.g. because it has been [overrun][combat-rows]), they must defend themselves with a melee weapon.  
    If they do not have this or cannot use it (i.e. their corresponding skill is less than 1), they defend themselves [unarmed][bonuses-and-mali]!

Catapults require ammunition.  
This can be produced from stones using [MAKE ammunition][cmd-make] by a mason with quarrying skill 3 and it weighs 10 weight units.  
One unit of ammunition corresponds to one volley.

*Ranged weapons - bonuses and time.*

| Weapon                        | Skill    | Offensive bonus | Reloading |
|-------------------------------|----------|----------------:|-----------|
| crossbow / mallorn crossbow   | crossbow |               0 | 2         |
| catapult                      | catapult |              -4 | 5         |
| bow / mallorn bow / elven bow | bow      |              -2 | 0         |

The time it takes to get the weapon ready to fire again is indicated under reloading.  
A catapult can therefore only be used once in each battle.  
A crossbow can fire every third round, bows even every round.

### Bonuses and mali

Various factors can modify the chance of hitting someone (attack) or deflecting a hit (parry).  
All bonuses and penalties have a direct effect on the skill and are taken into account before any skill halving by ranged fighters.  
The damage points that a person deals are not changed by the bonuses and penalties; the unmodified skill values count here.  
See also [combat tables][war-tables].

Unarmed persons

:   People who do not have a weapon skill that matches their weapon are also considered unarmed.  
    Unarmed persons fight with a skill of -2.  
    Ranged combatants who get into close combat and do not have access to a melee weapon (and a corresponding skill) defend themselves with a skill of -2.  
    However, they can still attack with their ranged weapon.  
    Unarmed goblins defend themselves with +/-0.  
    The skill with which orcs enter unarmed combat is determined by the level of their best melee skill -3.  
    Some races (generally only familiars) can learn the unarmed combat skill and then have no penalty when fighting without a weapon.  

Castle bonus

:   People in castles are additionally protected.  
    Castle occupants receive a parry bonus depending on the size of the castle if they belong to the defending side and the castle is large enough to accommodate them.  
    A fortification gives +1, a tower +2 ... up to the citadel, which gives +5.  
    If the castle occupants attack themselves, they no longer receive the castle bonus for parrying.  
    The castle bonus also applies against ranged fighters!  

Horse bonus

:   In plains, deserts, and highlands, melee fighters can use a horse in the front row on open ground.  
    To ride a horse into battle, you need a riding skill of at least 2.  
    Riders get a +2 bonus to attack and parry because they are faster and more agile.  
    People who are inside a castle, benefit from the castle bonus, and are attacked do not receive a horse bonus.  
    Trolls cannot use horses in combat!  

Lance bonus

:   Mounted spear and lance users get an additional bonus of +1 to attacks.

Pike bonus

:   spear and halberd users not using a horse get a +1 parry bonus against troops on horses.

Weapon modifiers

:   For this purpose, [weapon modifiers][weapons-summary-table] also count as bonuses and penalties.  
    A halberd unit thus has +2 to its parry (in addition to any other bonuses or penalties).  
    If it is not riding and fights against a rider, its parry value is increased by +1 at this moment.  

**Examples:**

- Base chance of the attacker -> BC = 30%.

Attacker with skill 3, defender skill 4 -> hit chance = 25%  
Defender in a citadel -> parry +5 -> hit chance = 0%  
So the attacker has just a chance of 10% ("beginners luck"), to get a second try at all, then a 90% to 99% chance to actually score a hit.  
All in all, there is 9% to 9.9% chance to hit the defender.  
The attacker is, after all, in a really bad spot caused by the citadel.

- This time the defender is not in the citadel:  

Base chance of the attacker -> BC = 30%  
Attacker skill 3, defender skill 4 -> hit chance = 25%  
Attacker with horse bonus -> attack +2 -> hit chance = 35%

- A sword maiden with melee 3 against a rider with riding 1 and polearms 2: She attacks with 3 (skill 3) against a parry of 2 (skill 2, no horse bonus, because the rider's skill is too low).  

The attacker has a hit chance of 35%.

- A bowman with skill 9 attacks from the 2nd row against a lance rider with riding 3 and polearms 9.
  He attacks with 7 (a -2 penalty from the bow) against a parry of 5 (skill halved and rounded down: skill 9, +2 horse bonus -> (9+2) / 2 = 5).  

The attacker has a resulting hit chance of (7 - 5) \* 5% + 30% = 40%

- A lance rider with riding 3 and polearms 9 attacks a bowman with skill 9 in the 1st row.
  - She attacks with 12 (skill 9, +2 horse bonus, +1 lance bonus) against a parade of -2 (ranged fighter without close combat weapon).  

The attacker has a hit chance of 100%, so she will always hit. Ouch ...

- She parries with her full parry value (weapon skill + horse bonus = 11), because they are in direct contact, against a ranged weapon (penalty 2 because of the bow).  

The shooter effectively attacks with a 7 against the rider with 11.  
The resulting hit chance is (7 - 11) \* 5% + 30% = 10%.  

- A spear fighter with polearms 3 in a castle attacks a rider with riding 2 and polearms 3.
  - She attacks with 3 (skill 3, no pike bonus while attacking, no castle bonus either) against 5 (skill 3, +2 horse bonus, no lance bonus while parrying)..  

The attacker has a hit chance of (3 - 5) \* 5% + 30% = 20%.

- She will parry with 4 (skill 3, no castle bonus because she attacked, +1 pike bonus) against 6 (+2 horse bonus and +1 lance bonus).

The rider has a hit chance of (6 - 4) \* 5% + 30% = 40%.

- A rider with riding 2 and melee 2 against a spear fighter with polearms 3:
  - They attack with 4 (skill 2, +2 horse bonus) against 4 (skill 3 and +1 pike bonus).

The attacker has a hit chance of 30%.

- The spear fighter fights back with 3 against 4 (the pike bonus does not apply while attacking).

The spear bearer has a hit chance of 25%.

- A lance rider with riding 2, polearms 3 attacks an equal combatant.
  They fight with 6 (skill 3, +2 for riding, +1 lance bonus) against 5 (skill 3, +2 riding)  

So the attacker has a hit chance of 35%.

It follows from this that you can hold a castle relatively well, but that you should not launch attacks from a castle if possible, as you will lose your defense bonus.  
It also follows that spear fighters are slightly more effective against mounted troops than sword fighters.

## Fleeing

People who have set [`COMBAT FLEE`][cmd-combat] and are [attacked][cmd-attack] try to flee.  
They do this before each round of combat, so they may have to take (more) hits before they can escape.  

Persons with [`COMBAT`][cmd-combat] or [`COMBAT REAR`][cmd-combat] with only 20% of their hit points left, and persons with [`COMBAT DEFENSIVE`][cmd-combat] or [`COMBAT NOT`][cmd-combat] with just 90% of their hit points left also attempt to flee, but only if they have taken a hit in combat.  
Hits whose damage points have been completely absorbed by the armor and failed hit attempts also count.  
This is to prevent units that were already damaged before the battle from fleeing even though they were not actually in danger.

The basic chance of escape is 25% (50% for halflings), plus 10% if you have a horse and 5% per level in stealth skill; the maximum value is 75% (or 90% for halflings).

Fleeing units evade combat, but remain at a safe distance from the fighting in the region.  
If the unit was in a building or on a ship on land, it leaves this as soon as a person from the unit has fled during the battle.

!!! note
    It may therefore be useful to order castle or ship occupants to re-enter their own ship, which they may be able to do after the battle.  
    It should be noted that the command should also be handed back to the correct unit with [`GIVE COMMAND`][cmd-give].

Special rules apply to units with the FLEE status.  
These units can still move after combat, even if they would otherwise not be able to execute a long order.  
Furthermore, these units cannot guard regions.  
Any guarding performed is automatically canceled when the unit assumes the `FLEE` status.  
This happens at the beginning of the turn, which means that all effects of [`GUARD`][cmd-guard] are immediately negated.

## Combat on and with ships

Sea battles are fought like land battles: The [ships][ships-id] board each other and the units come at each other.  
After the battle, it is possible for the units to carry out further long orders.

If a ship is involved in a battle, it takes 5% damage per battle round if at least one person takes damage that is on the ship or was on the ship at the start of the round.  
It therefor does not help to leave the ship before the battle begins.  
The [tactics round][tactics] and the first round are not counted, so the maximum possible damage is 20%.  

More damage can occur if sea serpents are involved in the battle.  
These monsters, like some familiars, have an attack that can cause structural damage to ships every combat round.  

If the ship is undermanned or empty after the battle, it drifts without control in the ocean and takes further [damage][damage-to-ships].

If you want to land in a region [guarded][cmd-guard] by another faction, you must first [`LEAVE`][cmd-leave] the ship and can attack or move only in the following round.  
This gives your enemies some time to prepare.

From land you can attack a ship immediately.  
Units on ships join the battle rows normally according to their `COMBAT` and [`HELP COMBAT`][cmd-help] status if their allies or they themselves are attacked.

[](){ #piracy-id }

## Piracy

Every captain has the chance to win a prize by capturing ships in adjacent regions.

The captain lies in wait for ships that end their movement in a neighboring region.  
Once there, the crew can act as normal in the next round.  
With the help of [`FOLLOW SHIP`][cmd-follow], for example, you could also just track your victims for the time being.

There are a few things to bear in mind with the whole story:

- Only factions with which you are not allied with `HELP FIGHT` are recognized as targets.
- If faction numbers are specified ([`PIRACY`*`<faction-id>`*`...`][cmd-piracy]), only captains of the specified factions are recognized as targets.
- The mechanism also works when the pirate ship is on land.
  It therefore offers an effective means of coastal protection.
- Pirates also sail into land regions, provided the ship can land there.
  If it cannot land, it takes damage.
- Pirate captains are thick as thieves.
  They cannot assess whether a target is possibly superior to them and will happily sail a single ship into an enemy fleet of 100 vessels.
  Being a pirate has its risks.
- If there are several potential targets to choose from, the captain will select one at random.
- Pirate fleets stay together.
  If an allied ship (to which the captain has set [`HELP COMBAT`][cmd-help]) from your own region has already recognized a victim, our ship will also sail to the region in question, provided that the victim recognized by the first ship is also a potential victim for us.

## The End

After the battle, the dead are tallied and all usable material from wiped-out units is collected and distributed among the survivors.

Units that were injured in battle remain injured.  
This is also displayed in the report.  
Injured units will recover over time.  
Units normally regenerate 5% (some [races][skills-modifiers] more) of their maximum hit points per round, but at least one point per person in the unit.  
Undead units do not regenerate.

If the region being fought in was [guarded][alliances] **at the beginning of the battle** by a friendly unit or by a unit that has set a [`HELP GUARD`][cmd-help] to its own faction ‘'at the start of the battle’', all units participating in the battle (i.e. appearing in the battle report) can still execute a long order.  
This works even if enemy troops are also guarding the region.  
It also works if you have attacked yourself (i.e. you have set the `ATTACK` order yourself).

If you have no own or allied units guarding the region at the beginning of the battle, the units participating in the battle can no longer execute long orders after the battle.

The only exception are units with the combat status [`COMBAT FLEE`][cmd-combat] and units at sea.  
Units with the status `COMBAT FLEE` can move after a battle if the have set one of the following orders: [[cmd-move]], [`ROUTE`][cmd-route] or [`FOLLOW SHIP`][cmd-follow].  
After sea battles on oceans you can always execute long orders.

## See also

- [[tactics]]
- [[war-tables]]

Continue reading: [[alliances]].

<!-- From [https://wiki.eressea.de/index.php?title=Krieg/en&oldid=16626] -->

[cmd-attack]: [[cmd-attack]]
[cmd-combat]: [[cmd-combat]]
[cmd-follow]: [[cmd-follow]]
[cmd-give]: [[cmd-give]]
[cmd-group]: [[cmd-group]]
[cmd-guard]: [[cmd-guard]]
[cmd-help]: [[cmd-help]]
[cmd-leave]: [[cmd-leave]]
[cmd-make]: [[cmd-make]]
[cmd-piracy]: [[cmd-piracy]]
[cmd-promote]: [[cmd-promote]]
[cmd-route]: [[cmd-route]]
