---
# cSpell:locale en
alias: optimize-transport
---
# Optimizing transport

## Traveling salesman

Since we at Eressea don't deal with just a few units but with a lot of them, the problem of traveling salesmen is less of a problem, as transports often do not go to several regions in a circle, but rather requirements are processed in parallel with many individual transports.  

## Optimal loading

It makes sense to use the backpack problem when loading a transport with goods.  
However, in Eressea you quickly fall into the trap of trying to load too many similar items.  
Optimizations of the backpack problem can hardly cope with this.  

A simple example:

You have to transport 10 stones (60 kg each) and 100 jewels (1 kg each).  
However, only 500GE capacity is available.  
A stone is valued at 1200, a jewel at a value of 50.  
Since the jewels offer more value per kg (50 per kg), we load all the jewels first:  

```text
Value  = 100 * 50 = 5000
Charge = 100 * 1 kg = 100 kg
Free   = 400 kg
```

At 400 kg we still manage to load 6 stones, leaving 40 kg free.  

```text
Value  = 5000 + 6 * 1200 = 12200
Charge = 100 kg + 6 * 60 kg = 460 kg
Free   = 40 kg
```

So let's try with the stones first: 8 stones, then there's still room for 20 jewels:

```text
Value  = 20 * 50 + 8 * 1200 = 10600
```

Apparently that was nothing.
But can there be any better way? Yes, 7 stones and 80 jewels seem to make better use of the capacity:

```text
Value  = 80 * 50 + 7 * 1200 = 12400
```

The way there leads, for example, via greedy search, i.e. searching through all states.  
In this case, 0 to 8 stones and 0 to 100 jewels (sometimes less) means around 900 conditions that would have to be checked.  
If you now imagine a 3rd or 4th product, it quickly becomes clear that we won't get the result.  

Normally the quickest way to reach the goal is through so-called Pareto-optimal intermediate states.  
What such intermediate states are can be more easily explained the other way round.  
States that are less valuable than another intermediate state with the same loading are not Pareto optimal.  
There is no need to pursue this any further, as apparently only non-Pareto-optimal states can always be achieved.  

For example, if you compare the condition "60 jewels" with "1 stone", you can see that 60 jewels are obviously worth much more with the same load.  
So it's not worth expanding "1 stone" further.  
Strictly speaking, you come to this conclusion once you have expanded 24 jewels.  

This type of optimum calculation is problematic because apparently any number of jewels between 0 and 100 is Pareto optimal.  
Even worse, any combination of 1-6 stones with 77 to 100 jewels and 7 stones with 77 to 80 jewels is Pareto optimal.  
I.e. despite optimization we have to expand 100 + 6*24 + 4 = 248 states of about 900 states until we can be sure of the solution we have found - not a nice result.  

However, another optimization is possible.  
We can limit the transport quantities used.  
Since jewels are worthwhile as long as they add up to a whole number of stones, the number of jewels is between 60 and 100.  
However, the jewels can never occupy the entire capacity, which is why a minimum of 6 stones and a maximum of 8 can be taken.  
This reduces the search to 41*3 or with Pareto-optimal intermediate states to 41 + 24 + 4 = 69 states.  

!!! warning "Attention"
    If you prioritize the goods instead of evaluating them, then this type of packaging is unlikely to be used.  
    Then the following applies: highest priority first...

### Packages

Often the transport of raw materials only becomes worthwhile when all the raw materials required reach their destination.  
The idea is now to package these raw materials.  
This can mean either sending them all or not at all, or adding a bonus when the package size is reached.  
Since the individual raw materials in Eressea come from different regions, the first option would probably result in nothing being delivered.  
The second variant would be desirable, but unfortunately it torpedoes the optimization with Pareto-optimal intermediate states.  
What remains is the first variant limited to one type of object.  
Whether the effort is worth it remains questionable.  

Regardless of this, it is of course possible and useful to rate items that are missing to complete a goal a little higher.  

It may make sense to differentiate between two or three types of packages:

1. Groups of objects that can only be used as a whole, e.g. individual levels of a building, multiple components for potions or weapons.
   These items cannot be processed individually at the destination, i.e. you have to wait until the last component has arrived
2. Groups of items or subgroups of the upper category are necessary for full utilization in weekly production.
   However, production can also be carried out without full capacity.
   This just reduces the time in which something else can be done if necessary
3. Groups of items or subgroups of the upper categories that are necessary for the full fulfillment of a mission, i.e. completing a ship or building, or fully equipping a unit with its equipment.
   It can be produced, possibly even at full capacity.
   It's just not certain that all components will arrive soon for completion.

The last two groups can probably be grouped together in practice and most likely ignored.  
For the first group, however, a fulfillment bonus is conceivable and could also be planned.  

## Multi-path finding

However, when planning transport, it can happen that a transport already has some cargo and therefore a target region.  
However, there is still capacity available during transport that could be occupied by other goods.  
Simple options now include only giving goods that are needed at the intermediate points on the route.  
Advanced techniques load goods, which bring them a little closer to their goal.  

However, it also seems possible to me to adapt the route so that a route is searched for with the same duration to the first destination, which at the same time leads as close as possible or even over the region of the second destination.  
It is also conceivable to optimize the route by running it via “transshipment points” to ensure that the goods for the second destination can then also find transport in the fork region.  

So how could such multi-path finding work?  
The laps until arrival at destination 1 are known.  
So only routes that don't take longer are considered.  
However, you only find out when a route has been found.  
The minimum distance to destination 2 is the second criterion for route evaluation and makes the route calculation a little more "greedy", since all regions that give the same value in criterion 1 are now moved to 2.  
Value must be tested. Fortunately, the estimation function also provides good service here.  

### Equivalent goals

If several destinations are equivalent, they will of course compete for the next route from a certain point onwards.  
Until then, you can easily optimize the route to the minimum of both routes, i.e. you drive to the closer region and unload the goods for the other region when you are as close as possible.  

However, as more and more destinations are added, the transport actually becomes a local "traveling salesman".  
I haven't yet taken a closer look at whether and when it's actually worth taking a short tour here.  
But of course there is such a limit.  

### Transshipment points

However, multi-path finding can also be made much easier.  
If you define enough transshipment points, you can assign the transports as intermediate points for routes longer than a week **always** to go to transshipment points, or at least to do so when a capacity limit is exceeded or the transshipment point does not mean a detour.  

The transport system of the former EEC implicitly acknowledged this fact by being organized hierarchically.  
Transshipment points are regions that have subordinate regions.  
However, the hierarchy often means detours.  
Whether such a system works well also depends on the topology of the island.  
Islands that form rings are particularly unsuitable for a strictly hierarchical transport system.  

## Evaluation function

Various optimization algorithms require an evaluation function to evaluate possible intermediate and target states.  

Finding such a function for “logistical states” is not easy at first glance.  

What and how do you best evaluate it?  

- Satisfying as many requests as possible?
- Utilization of existing transport capacity?
- Influence of priorities and values?

As with learning, it is best to place various very simple choices next to each other and differentiate them from each other.  
Important: All properties not mentioned are the same.  

Simple scoring rules:

- It is better to use a near offer than a far offer
- It is better to serve a high priority demand than a low priority one
- It is better to supply a demand from a nearby source than from a distant source

More complicated evaluation rules:

- It is better to make full use of a transport than to have it travel with a lot of empty space.
  The distinction between “good” and “a lot” is the complicated matter here.
  Objects of the same value but of different weight evoke different approaches depending on the environment.
  If the transport cannot be used to capacity with the light object and there are no other goods to be transported, then the heavier object is preferable
- Grouped requirements (packages) should arrive at their destination at the same time (or as soon as possible)
- It is better to take something to a transshipment center than to leave it lying around, but only if the transshipment center is not further away and can be reached in a week
- Priority can also be understood in two dimensions as urgency and importance.
  However, it is necessary to be able to compare two such two-dimensional points
- It is better to let a transport drive empty to a region with urgently needed supplies than to a transshipment region.
  But the latter is still better than just learning or doing nothing
- If there is no transport in a nearby source, there is in a more distant source and the route leads via the nearby source, the transport should then be stopped if the distant source after loading would have less of the goods than the nearby source after loading
  - Example:
    - A needs 100 stones.
    - In B, one round away from A, there are 1000 stones. There is no available transportation in B
    - In C, two rounds from A and one from B, there are 500 stones. Transportation available
    --> Transport should travel empty from C to B if necessary
    - If there are 2000 stones in C, the stones are taken away
    - If there are 1050 stones in C, 75 stones are taken. After charging for transport, both sources still have 975 stones

### Valuation basis of goods value

The basis here is a basic goods value that is specified by the user for each item.  
Calculations that take global supply and demand into account are also conceivable.  

The value of the goods therefore contains the global importance of the item.  

The basic goods value can e.g. be expressed in silver.  
A commodity could e.g. Use the average of the purchase price and sales price as the value.  
It is becoming more difficult to value scarce raw materials in silver.  
Overvaluation would otherwise possibly lead to silver for maintenance not being delivered because a sword is missing somewhere and the transport therefore takes a different route.  

#### Modification by urgency

It is therefore clear that the underlying value still needs to be modified.  
The urgency should be able to have such a strong effect that even items with a low base value become interesting enough.  
An exponential function or similar on the urgency therefore makes sense.  

```text
f(r
round until necessary) = ?
f(0)=10000% * Underlying value
f(1)=1000% * Underlying value
f(2)=200% * Underlying value
f(3)=50% * Underlying value
f(4)=15% * Underlying value
f(5)=8% * Underlying value
f(sometime)=5% * Underlying value
```

These would be values ​​that I have in mind at the moment and that are either stored in a lookup table or are modeled by a function.  
The extent of this formula essentially depends on the range of underlying assets used.  
A flaming sword that is needed at some point may have a base value of 10,000, but the 10 silver that is urgently needed for maintenance in another region must still result in a higher total value.  
With the above formula, the flaming sword would be worth 500 and the 10 silver would be worth 100 -too little to be delivered.  
Therefore, the parameters of the urgency function should be calculated based on the min and max values ​​of the base values.  

Of course, the importance of an object can also vary locally because the environmental conditions are different.  

#### Modification by removal

It will often happen that a product cannot be delivered directly to demand by the supplier because the two regions are too far apart.  
However, in order to ensure delivery from a source that is as close as possible, it is advisable to evaluate the partial execution of a demand at different levels on the different sections.  

#### Evaluation of empty runs

Empty trips may be necessary in order not to get stuck in regions that only function as sinks.  

There can be 2 different motivated goals for empty trips:

1. Heading to regions with urgently needed goods
2. Heading for transshipment regions -there is always a lot to transport here

It may even make sense to drive empty.  

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Transport&oldid=2585] -->
