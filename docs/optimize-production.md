---
# cSpell:locale en
alias: optimize-production
---
# Optimizing production

By optimizing production I mainly mean the economical use of units. I.e. I have a group of units in a region with the same task and should produce a set amount (silver, trade, items, ships and buildings).

It is relatively clear that this is the so-called backpack problem. The aim here is to overload the backpack as little as possible, i.e. to assign the units so that as few people as possible do nothing. In principle, it is also conceivable to set a minimum utilization limit (for the last assigned unit).

When loading a backpack, it is important to load as much weight as possible into the limited space/weight. In our case, space/weight is the quantity to be produced. We don't have any value, but we do have costs. And they are e.g. the better a unit is, the lower it is.

The backpack problem can be solved quite well using Pareto optimal points (intermediate states) for individual, very different objects that you pack in the backpack. Unfortunately, at Eressea we often have to deal with a lot of equally well-trained units. i.e. the costs per person are the same, only the size may be different. However, this means that quite a few states are on the same line, i.e. it is hardly possible to eliminate any of them.

So how do you basically proceed:

1. Sort existing units by cost per person (least first) and then by number of people (most first)
2. Recursive creation of states
    1. Be careful to only assign the same units (cost and size) in a defined order (i.e. if the first one in the group is not there, do not try the second one)
    2. Remove states that cause >= costs with <= production quantity (non-Pareto-optimal points)
    3. Check the additional condition of minimum utilization for the last unit and/or possibly the smallest unit
3. From all target states, choose the one with the highest production and, if necessary, the lowest costs

A method that calculates the result of the optimization only needs a list of the units, their costs and their production quantity. If necessary, additional conditions are given to the method. Such a unit list can be created relatively quickly, regardless of the actual target, and provided with the necessary attributes. When applied to production, the backpack problem can be implemented quite easily in a generalized manner.

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Produktion&oldid=2469] -->
