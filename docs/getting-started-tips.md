---
# cSpell:locale en
alias: beginner-tips
---

# Beginner tips

When entering orders, make sure you have used the correct faction number and unit numbers.
[Set a password][cmd-password] and don't forget it.

It's more interesting for everyone if you name your faction and all units in an original way.
Please keep in mind that Eressea is a fantasy role-playing game – names like "Barney's Remote Control Torturers" (yes, that really existed!) simply don't fit the atmosphere of Eressea.

If you're unsure about anything or have any questions, the best thing to do is contact [Eressea's Discord channel].
You can access it via browser, installed program, or app.
They'll definitely give you tips for your first moves or answer your questions.
You can also ask questions in the [PbEm Games forum].
Eressea has its own subforum there.

Most players use [Magellan][magellan-id], a program that reads the CR (Computer Report), displays it clearly, helps in creating commands, and shows many errors.

Then there's [ECheck][echeck-id], a program that lets you check your moves for correctness.
ECheck is automatically run by the server on incoming moves and the result is sent back.
Use ECheck at home with the -e option to check if your commands are being interpreted as expected.
ECheck only checks the spelling of the commands and the order of the parameters.
ECheck doesn't analyze the semantics (i.e., the meaning and logic of the commands), but it can perform various tests regarding silver when the server's [orders template][orders] is used.

Set yourself several goals you want to achieve.
One of your first goals should be exploring the surrounding area.
This is the only way to find important mountain and forest regions where you can mine ore and harvest timber.
So send out a few single-person units and give them enough silver to sustain themselves for a while.
Note: the silver required for recruitment must be factored in!

Create more units and learn some skills that you expect to need in the next three to four rounds.

[Entertainment][cmd-entertain] is essential for earning money.
Without sufficient silver, your faction won't be able to grow.
[Tax collectors][cmd-tax] are also a good source of income;
for this, you need, for example, metals ([mining][about-mining]) or wood ([logging][deep-in-the-forest]) to craft weapons like swords or spears;
and of course, tax collectors need the appropriate weapon skill ([tax collection][collecting-taxes], [weapon skills][combat-skills]).

[Perception][skill-perception-id] is a very important skill that is often underestimated by beginners.
Only tax collectors are able to see camouflaged units and prevent them from [stealing][stealing-the-dishonest-way]! It's therefore worthwhile to recruit and train at least one Perceiver for each of your home regions right from the start.
It's also advisable to build [castles][castles] early, at least at level 2, and "trading posts" (required skills: [masonry][masonry] and [mining] for the stone and [castles building][buildings-id]) so that [trade][silver-trade-id] can be conducted.
Of course, training the necessary merchants and transports (usually cavalry) and equipping them with [horses and wagons][horse-and-carriage] is also essential.
Understanding trade isn't easy for beginners, but it's worth the effort.

Units with expensive skills like [Tacticians][tactics-id], [Alchemists][list-of-skills], etc., should only be trained later, as their training consumes a great deal of silver (200 silver per turn).
Training [Mages][magic-id] costs even more silver, but a mage with combat spells can provide significant advantages in conflict.
And mages of all schools of magic can cast a spell to earn silver very early on, making an early investment worthwhile (especially for races with +1 in Magic).

It would also be advisable to have some precautions in case the neighbors aren't very peaceful.
In other words, a plan for how to protect your faction from attacks once the initial immunity period ends.

Write plenty of comments in your orders files so you know what each action was for in the following rounds.
It's a good idea to group orders by region so you have a few lines of comments for each region.
A good starting point for your new orders file is the [Round Template][orders] appended to the evaluation for the next round.
For each unit, you can also note what it produces, for whom it produces it, where it's going, or what kind of trade it's engaged in.
Here is an example of these comments:

```text
REGION 4,4 ; Lochinver
; Beware the dark horde
; cut down?

UNIT zbt;         Bow maker Jog'nabat and his clan [4;100$]
    MAKE Swords
    GIVE sjur 5 Swords; He probably only gives the 4 that he
                      ; had last round

UNIT sjur;          Fuhrmann Sjur [2;243$]
    // Capacity: 420 = 7 stones; Silver!
    GIVE 7jht 7 Stones
    ROUTE SW W PAUSE E NE PAUSE
```

The comment following the [UNIT order][cmd-unit] is inserted into the move template by the program;
following the unit name, in \[ \], is how many people are in the unit and how much money it has (here, 4 people with 100 silver and 2 with 243 silver).

Beware of upkeep costs.
Large units need a lot of money, and if they don't have it, people will starve.
It's enough if one of your own units in a region has enough silver to feed all the other units.
Don't forget units that leave the region!

In the first few rounds, you can live off your starting capital, but soon you'll need a steady income.
This nest egg is generally depleted after four to six rounds.
The fastest way to generate income is with tax collectors and entertainers, and [trading][silver-trade-id] luxury goods promises large profits in the long run.

Plan the first few weeks thoroughly.
You can calculate exactly how many entertainers, tax collectors, weapon makers, lumberjacks, etc., you can and need to recruit.

When the game begins, units from multiple factions are sometimes positioned close together.
Coordinate with each other and divide your tasks so you can expand as efficiently as possible.
Maintain contact with many factions; this makes the game exciting and will help you later.
If you get into conflicts, it's good to know you're not alone.
Contacts allow you to exchange information, such as map data; they enable you to share experiences and tips, and mutual learning is especially helpful.

To contact other factions, obtain a list of them in your region using [`OPTION`][cmd-option] ADDRESSES and contact them directly.
Use the [`MESSAGE`][cmd-message] REGION order to alert other factions to your presence.

To achieve your goals, you shouldn't skimp on expenses.
The starting capital is intended for investment.
The first miner produces iron on a large scale, the second forges swords, and the third trains warriors.
In addition, you can take on a number of other tasks: mapping, training mages, ship building, castle construction, establishing a thieves' guild, building a small trade caravan with horses and wagons...
For these tasks, you can create a few new units.

Wars should be avoided, especially in the initial phase – valuable units are lost too quickly, income is too low, or the supply of materials dries up.

If you have contact with a powerful faction, try to sell them something.
Try to cut down trees, quarry stones, or mine iron.
It's worthwhile to locate or build two castles to trade between.
For this, you'll need merchants and wagons.
Buy a wagon and two horses from the lord of the castle or build one yourself.

You don't need to be allied with trading partners.
Use the [`CONTACT`][cmd-contact] command to exchange goods and silver with other factions without being allied.

One of the most important tables in this guide is the [[orders-sequence]], which shows the order in which orders are processed by the server.
It illustrates, for example, that you can certainly give raw materials to a weaponsmith in the same week before he starts production ([[cmd-give]] is at position 14, [`MAKE`][cmd-make] is at position 22), but you cannot give him potions and then use them immediately ([[cmd-use]] is at position 7).

There are no winners in this game.
The game lasts until you despair of yourselves or your enemies have wiped you out.
After that, if the game masters allow it, you must start again as a new faction.

And always remember: the game is just a game! It's meant to be fun for everyone.
Don't let yourselves get annoyed or be carried away by rash decisions – the player portraying the nasty and mean orcs is probably actually a nice person...

## See also

- [Tips and tricks][tips-and-tricks]
- [Hints][hints]
- [The first round][first-round-id]
- [Basics][basics]

Continue reading: [Xontormia Express][xontormia-express-id].

<!-- From [https://wiki.eressea.de/index.php?title=Anfängertipps&oldid=17013] -->

[Eressea's Discord channel]: https://discord.gg/JyAeYJw%7CDiscord
[PbEm Games forum]: http://www.pbem-spiele.de/

[cmd-contact]: [[cmd-contact]]
[cmd-entertain]: [[cmd-entertain]]
[cmd-make]: [[cmd-make]]
[cmd-option]: [[cmd-option]]
[cmd-message]: [[cmd-message]]
[cmd-password]: [[cmd-password]]
[cmd-tax]: [[cmd-tax]]
[cmd-unit]: [[cmd-unit]]
