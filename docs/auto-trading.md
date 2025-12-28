---
# cSpell:locale en
alias: auto-trading
---
# Automation trading

Trading has only one purpose: maximizing the silver yield. This means that the big goal is defined very simply.

So the problem to be optimized is maximizing the profit between purchasing and selling.
The secondary condition is the transport of the goods, although this secondary condition can quickly become very complicated.

## Trading profit maximization

In the world of Eressea, the regions of an island usually offer one of two trade goods for purchase.
This makes it relatively easy to determine the optimal purchase quantity of merchandise within the island, as we know the maximum quantity we can sell at what price.
As long as there is still a margin between buying and selling, we will buy.
Usually you will buy for your own needs on the islands at 1-3 times the basic price, just in the proportion in which the two luxury goods are offered.
For reasons of unit minimization, regions with a very low trading volume may also be avoided, so these should then be excluded from the calculation.

The need for external luxury goods is often even easier to determine.
It is roughly the number of farmers on the island divided by 100.
However, this need will rarely be met because ships usually have more important things to do.

The problem here is rather boring or cannot be described as a problem.
Only during transport do “decisions” actually have to be made.

## Important additional condition: transport

Let's stay with the simple case of two trade goods for now and now look at the transport.
Since we cannot handle any number of transport units -on the contrary, this number must be minimized (unit limit) -we can hardly deliver all requirements every week "just in time".
So we can get more than we need for a week into one region at once.

The approaches to determining the optimal storage condition and transport quantity are as different as they are similar.
Ultimately, you always try to deliver at least the currently required quantity, but at the same time keep the transport to full capacity.

One approach is the priority model: both the sales price and the time by which the goods are needed can be included in the priority.
Since over time all sales prices of a product reach the same value, you can limit yourself to time.

If you now assign the transports according to priority, a minimum stock can always be guaranteed if there is a sufficient number of transports and the capacity of the transports.

The more cleverly you control transport, the fewer empty trips and therefore less transport and transport capacity you need.
It is therefore important to carry out as few and as short transports as possible.
Unfortunately, the optimization of this problem is complex, i.e. as the number of regions increases and, above all, very different numbers of farmers and certain island topologies, the number of possible delivery route combinations increases exponentially.
It's probably not worth determining the optimal combination here (it usually comes down to searching through all the sensible combinations).
Instead, you just try to find a good combination
This can be done using various rules or a “targeted search”.

Rules would be, for example:

- To a destination region, look for transport in a close source region
- A transport must reach a filling of at least x%

A targeted search can create states that represent a partial result and, based on this, expand the most promising subsequent states.
Since, of course, partial results that are not only good at first glance can ultimately produce an almost optimal final state, an evaluation is required.
This evaluation must in turn evaluate knowledge and estimation to different degrees in order to achieve an almost optimal target state in a reasonable time, even with billions of possible states.
Of course, conditions that definitely do not produce a good result should also be eliminated in advance.

<!-- From [https://wiki.eressea.de/index.php?title=Automatisierung\_Handel&oldid=2482] -->
