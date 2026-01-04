---
# cSpell:locale en
alias: cmd-plant
---
# PLANT

*[long] order.*  

**`PLANT`**`[`*`number`*`] HERBS`  
**`PLANT`**`[`*`number`*`] TREES`  
**`PLANT`**`[`*`number`*`] MALLORNSEEDS`  
**`PLANT`**`[`*`number`*`] SEEDS`  

This order can be used to restore fresh greenery to a emptied or devastated region or to control natural tree reproduction.  

For `PLANT HERBS` requires at least [Herbalism] 6.  
The unit attempts to plant the specified number of herbs, up to a maximum of one herb per skill level;  
To do this, she needs the appropriate number of herbs of the corresponding type and a vial of [[tables-potions-and-herbs|Water of Life]] (for no matter how many herbs).  
This means that no herb type can be changed; we always try to plant the herb that is native to the region.  

In the region, newly planted herbs multiply very quickly (except in winter) if they are left alone for a few weeks.  
If you have low skill, herbs can also be broken when planting.  
It should only be reasonably safe from level 10 onwards.  
Growing herbs is more intended to reactivate regions where someone has completely harvested all the herbs and nothing can reproduce on their own.  

With`PLANT [`*`number`*`] TREES` or `PLANT [`*`number`*`] SEEDS` the unit attempts to plant the specified number of seeds, up to a maximum of one seed per skill level.  
Only mallorn seeds can be planted in Mallorn regions.  
To do this, she needs at least Herbalism 7.  
To plant normal seeds, she needs at least Herbalism 6.  
In spring, a unit with at least Herbalism 12 will directly plant a sapling for every 10 seeds.  
You should carefully consider whether this is desirable or not.  

Player experience (Solthar):

`PLANT` and `GROW` are synonymous orders.  
You can grow seeds and plant horses. But it is not recommended.  

## See also

- [[cmd-grow|`GROW HORSES`]]
- [[resources]]

<!-- From [https://wiki.eressea.de/index.php?title=PLANT&oldid=16730] -->

[long]: ./commands.md#short-and-long-orders
[Herbalism]: ./skills-list.md#herbalism
