---
# cSpell:locale en
alias: basics
---

# Basics

Just because there is no winner in Eressea doesn't mean you can't lose.  

We often see avoidable mistakes among beginners that lead to one [faction][factions] being eliminated from the game early because a rule was not fully understood, or the player encountering problems unprepared.  

The following basic things every player should understand.  

## The report

There are two reports every week that contain the same data.  
The normal report (NR) is a text file that can be read with any editor.  
The computer report (CR) is a file that is understood by tools such as [Magellan][magellan-id] and [CSMap][csmap-id].  

We recommend that beginners make their first moves with the normal report and a text editor.  
The first few commands are rarely more than a dozen lines, and you don't need a tool like Magellan to create them.  

On the contrary, because these tools are designed for managing large parties with hundreds of [units], they have a lot of features that tend to be confusing at first.
It could distract from the important information that is easier to see in the normal report.  

## Long and short orders

A unit can only perform one [long order][short-and-long-orders] per week, but can perform any number of short ones.  

!!! warning "Danger"
    [Combat] can be a long action, even if you haven't attacked yourself.  

## Battle

Battle in regions that you don't [guard][cmd-guard] are always long, even if your entire faction is attacked by just one scout, he prevents ALL units he [attacked][cmd-attack] from carrying out their long order.  
So you should make sure that you are guarding your regions from the first week in which your faction can be attacked at the latest.  

[](){ #basics-hunger-id }

## Hunger

Avoid [starvation][starvation] at all costs. The effects are catastrophic.  
Each person needs 10 silver maintenance per week in order not to go hungry  

## Finance

Entertainment and taxes are learned quicker than trading, only do [`WORK`][cmd-work] in an emergency to avoid starvation.  

## Mage

Each Magic School has a spell at level 1 that produces 50 silver per caster level.  
If your race does not have a penalty in magic, training magicians early can be worthwhile as an alternative source of income.  
But be careful - spells sometime fail.  

<!-- TODO:
## Use items and silver

`GIVE` and `RESERVE` declare and that `GIVE` reserves the items with the recipient.
When something is used, for example to make an item or to recruit, who uses it and in what order?
-->

## Load capacity

[movement][movement] will fail if the carrier's [load capacity][transport-capacity] is less than the total weight of the people, objects, equipment, etc.

Please check the position of the `MOVE` order in the [order sequence][orders-sequence].  

For example, the `ENTERTAIN` order executes before it; with the potential earnings, a boat or unit could be overloaded.  

## New units

Units that have silver or are given silver always use this silver first before accessing the [[items-pool]].  
If you create a new unit, recruit a cat (costs 90 silver) and let it run into the neighboring region (10 silver maintenance) in order to let it learn entertainment there the following week (another 10 silver maintenance) and then entertain it (from here on it takes care of itself) it is not enough to give it 20 silver for the travel time and the learning week, you also have to give it the 90 silver for your own recruiting.  
Otherwise the unit will arrive in the neighboring region starving.

## Scout

Scouts are a strategic investment.  
Secure important neighboring regions, but only if you can afford it.  
As a rule, it is not enough to place an entertainer unit in the neighboring mountain if it cannot guard it.  

<!-- From [https://wiki.eressea.de/index.php?title=Grundlagen&oldid=17000] -->

[cmd-attack]: [[cmd-attack]]
[cmd-guard]: [[cmd-guard]]
[cmd-work]: [[cmd-work]]
