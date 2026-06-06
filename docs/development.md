---
# cSpell:locale en
alias: development
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Development

This page is intended to bring developers of different tools or script developers together or to address questions that arise again and again.

## Newsgroups & mailing lists

A good starting point for discussions is the [E-Client List] and the Magellan Development List.

## Tools

- [Magellan]
- [CSMapFX]
- [Vorlage]
- [crtools]

### Interesting development plugins

- [ExtendedCommands Plugin] for Magellan
- [FFTools 2] for Magellan

## Format

- [[cr-format]]

## Scripts

When automating Eressea factions, the same problems arise again and again.  
Of course, everyone has a slightly different approach, but fundamentally the problem areas are the same.  
So that you don't have to start over again and maybe get some ideas, I would like to create a kind of treasure trove for automation here.
Such questions are independent of the tool used.  

Of course, links to (tool-specific) script collections are also helpful.  

### Script collections

- [Script collection] for [[vorlage]] on the Vorlage homepage

### Recurring questions

- [[auto-trading]]
- [[auto-transport]]
- [[auto-learning-chains]]
- [Production][production-id]
- [[auto-way-finding]]
- [[auto-event-response]]

### Optimization problems

The central questions can often only be solved (almost) optimally by solving complex optimization problems.  
You will encounter many fundamental optimization problems.  

This is exactly the right thing for (prospective) computer scientists to deal with algorithms in practice that solve such optimization problems in a reasonable amount of time.

- [[optimize-wayfinding|Way finding / Route calculation]] ([A* search algorithm])
- [[optimize-learning-chains]] (A* search algorithm, [backpack problem])
- [[optimize-transport|Transportation and trading systems]] (traveling salesman, Backpack problem)
- [[optimize-production]] (backpack problem)

<!-- From [https://wiki.eressea.de/index.php?title=Entwicklung&oldid=8216] -->

[E-Client List]: http://groups.google.com/group/eressea-client
[Magellan]: http://magellan-client.sf.net
[CSMapFX]: https://github.com/ennorehling/csmapfx
[Vorlage]: https://gulrak.de/pbemtools/
[crtools]: http://sourceforge.net/project/showfiles.php?group_id=91825&package_id=128120
[ExtendedCommands Plugin]: http://magellan.log-out.net/extcmds/
[FFTools 2]: http://fftools2.fietefietz.de/
[Script collection]: http://www.gulrak.net/wiki/view/Gulrak/VorlageSkripte
[backpack problem]: https://en.wikipedia.org/wiki/Knapsack_problem
[A* search algorithm]: https://en.wikipedia.org/wiki/A*_search_algorithm
