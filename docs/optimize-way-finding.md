---
# cSpell:locale en
alias: optimize-wayfinding
---
# Optimizing way finding

Many people are probably familiar with the general functionality of route calculation.  
Fortunately, not all routes to Rome are sought, but only those that obviously go in the general direction.  

The easiest option (Greedy) would be to first walk all existing paths from the starting point and remember the new intermediate points.  
From there all paths are taken again.  
The shortest route to a point is always remembered (route and distance).  
If you keep expanding like this, you will eventually find the target point (if it can be reached).  
The fact that you not only get closer to the goal, but also actually go in the completely wrong direction on some routes is an extreme disadvantage on long routes, both in terms of processing time and the memory requirement for intermediate states.  

The A*-Search, on the other hand, aims to only expand intermediate points that are actually on the correct route.  
Using a cost function, the costs are calculated for each point (including start and finish), **probably** to the destination.  
This is probably important here, because we don't know the distance to the destination unless we know the route. That means we estimate the distance.  
The straight line on the map is a good estimate that we certainly won't beat (without stargates, wormholes and the like ;-)  

For Eressea and other games on hex maps, the minimum distance can be calculated relatively easily from the coordinates.  

```text
hx = start.x - target.x
hy = start.y - target.y
Distance = max(abs(hx), abs(hy), abs(hx+hy))
```

This estimated distance to the destination is added to the distance already traveled.  
The regions that still need to be expanded are sorted according to this criterion.  
If there are few obstacles on the map, the algorithm can reach its goal very quickly, even over long distances.  

However, every obstacle and every additional condition that is to be built into the cost function quickly causes execution to slow down again.  

Magellan has already built in a route finding function.
In addition to distance, it also supports ships sailing along coasts.  

Further secondary conditions can concern the safety of regions (sea serpents, opponents), the landing direction in the target region or the preferred stopover in land regions at the end of the round.  
However, it is precisely such secondary conditions that are difficult or impossible to calculate using the estimation function, so that the behavior of the algorithm becomes more and more “greedy”.  
The A*-Searching with an estimator that always returns 0 corresponds to the greedy search.  

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Wegfindung&oldid=2478] -->
