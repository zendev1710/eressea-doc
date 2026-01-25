---
# cSpell:locale en
alias: cmd-learn-auto
---
# LEARN AUTO

**`LEARN AUTO`**` `*`skill`*  

Through the order, the server attempts to automate [[cmd-learn|learning]] and [[cmd-teach|teaching]] in a region for all units in a faction using this order for this skill.  
However, a mixture of TEACH and LEARN AUTO is not possible.  

If several units in a region give the `LEARN AUTO <skill>` order, e.g. `LEARN AUTO sailing`, then the server selects those units from these units that have to teach so that the rest get the maximum learning output.  
As with simple `TEACH`, each person who gets a teacher learns twice as fast.  

There is no need to split units.  
For example, if a unit with 10 people on T7 and a unit with 10 people on T5 both have `LEARN AUTO` ordered, then one person from the T7 unit teaches the ten from the T5 unit, the remaining nine learn normally.  
With the simple orders you would have had to split up the unit, which can be very annoying.  

This effect also applies to fewer than 10 students.  
A person who teaches 6 students using `LEARN AUTO` has a 4/10 chance of learning for a week.  
If no students can be assigned, the unit learns normally.  

`LEARN AUTO` does not work on expensive skills and not in combination with `TEACH`: other units that use ordinary `LEARN` and `TEACH` orders are not involved in the automatic assignment of teachers.  
Units that use `LEARN AUTO` cannot be taught through `TEACH`.  

It can still make sense to use `TEACH` and `LEARN AUTO` in parallel for different units.  

The advantages of `TEACH`/`LEARN` are:

- Units with expensive skills can be taught
- A unit can teach units in different skills
- Teachers and learners do not have to belong to the same faction
- Units that are not allowed to teach (e.g. most familiars) can still be taught

The advantages of `LEARN AUTO` are the folllowing:

- It's less detailed work and can be left alone for several weeks
- Units that are not fully used as teachers use the remaining capacity to learn themselves

Player experience (XolgrimA):

Block for `LEARN AUTO` consists of a maximum of 128 units per region and skill.  
If more units of a faction in a region give the order, a second block is formed that sets up a teaching/learning chain independently of the first.

<!-- From [https://wiki.eressea.de/index.php?title=LEARN\_AUTO&oldid=15393] -->
