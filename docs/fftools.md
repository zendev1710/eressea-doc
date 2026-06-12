---
# cSpell:locale en
alias: fftools
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD041 MD042 -->
[](){ #fftools-id }

# FFTools

FFTools2 are a plugin for [Magellan] for automatically creating orders for units.

On the [official site] there is an introduction, installation instructions and complete help for the individual orders.  
Examples of usage are also available on the orders detail pages.  

The tool is aimed at players who have little or no experience with programming languages ​​and want to automate everyday tasks.  
It is not suitable for getting to know Eressea as a newcomer.
Furthermore, issuing orders manually is fundamentally “more intelligent” than a decision made by the script.  

The script is not AI.
But it can quickly create usable orders for a large number of units, making it useful for large factions whose rulers view their available time as a critical resource.  
If you automate training, trade, construction, brewing and logistics, you have time for diplomacy (again).  

The script orders include complete professions (//script Transport mode=auto), targeted orders over several rounds (//script SailTo X,Y) or very specific material flow instructions (//script Request 100 Stein 200).  
As comments in the unit orders, they are sent to the Eressea server and sent back from it and are available for the next script run.  
If necessary, the script orders can be revised and another script run can be started until the desired result is achieved.  
“Normal” Eressea orders can also be used in addition.

FFTools2 creates its own menu structure in Magellan and also integrates into the context menu (right-click menu).  
In addition to the help pages, there is an extra FFTools channel on the Eressea Discord server.

<!-- From [https://wiki.eressea.de/index.php?title=FFTools2&oldid=16883] -->

[Magellan]: http://magellan-client.sf.net
[official site]: http://fftools2.fietefietz.de/
