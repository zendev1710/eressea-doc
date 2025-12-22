---
# cSpell:locale en
alias: resources
---
# Resources

Raw materials can be obtained without other ingredients from the region without further ingredients. However, the deposits are limited and regenerate only slowly or not at all. The necessary skill can be looked up in the section about [[items|goods]].

## Extraction of Raw Materials

When exploiting resources, it is important to consider that units [[cmd-guard|on guard]] prevent non-allied factions - having neither [[cmd-help|`HELP GUARD`]] nor [[cmd-help|`HELP ALL`]] to your faction and not [[cmd-contact|contacting]] your unit or faction - from exploiting them. This does not apply if the guarding faction does not see the producer, for example because they are [[camouflage|cloaked]].

### About Mining

Iron, stone, laen, and, in particularly ancient regions, sometimes even adamantium, can be mined or quarried from mountains, glaciers, and sometimes other types of regions. Laen and adamantium require a mine and particularly high mining skill. These resources can be difficult to extract. In your report you can find out by the number after the  -->/”. For example, if the report says "20 iron/4", this means that 20 iron can still be mined at skill level 4. Once these have been extracted, miners will need to be level 5 to extract iron from the next layer (5). In general, the quantities that can be extracted increase with each new layer.

### Deep in the Forest

The development of Eressea's vegetation is determined by the seasons. As soon as the first rays of sunlight hit the ground in spring, the seeds hidden in the soil germinate and last year's saplings grow into mature trees. If there isn't enough sun (no free working space), the seeds remain dormant in the soil. During the summer and autumn months, mature trees shed their seeds, which can be collected with the [[cmd-make]]`seed / "mallorn seed"` order and the [herbalism] skill (minimum level 3 / 4) and then replanted elsewhere with the [[cmd-plant]]`seed / "mallorn seed"` order (minimum level 6 / 7).

If wood or mallorn is felled, the forest shrinks and only recovers very slowly. As long as there is enough wood, it can be felled in any quantity. The same applies to mallorn, a 'magic' wood found only in a few regions. Mallorn reproduces like wood, but mallorn seeds only grow in regions that are suitable for them. In regions with mallorn, the order [[cmd-make|`MAKE wood`]] can also be used to harvest wood instead of mallorn. The number of mallorn trees is then reduced by the same amount as if mallorn had been felled.

### And Elsewhere

You may capture wild horses as you like with [[cmd-make|`MAKE horse`]] by a unit with the [taming skill][herbalism]. Without help, only wild horses reproduce. They love space and freedom, which is why some of them migrate to neighboring regions when there are fewer horses there. However, it is possible to breed captured horses in a [stable] with the taming skill and the order [[cmd-grow|`BREED HORSES`]].

Player experience: SoltharThe maximal amount of horses in a region equals the number of [[world|jobs]] / 10. In a relatively empty plain they grow at a rate of 4%. As they approach the upper limit, growth slows down. The most new horses are born at about half the maximal population. In a plain with 25 horses, there is 1 birth per week. With 500 horses there are 10 new horses per round. At 1000 horses there is no more growth.

Herbs can also be harvested to make potions. There is a maximum of one herb species in each region. See the [herbs list].

## See also

- [[production]]
- [[items|Goods]]
- [[roads]]
- [[buildings]]

Continue reading: [[items|Goods]].

<!-- From [https://wiki.eressea.de/index.php?title=Rohstoffe/en&oldid=16867] -->

[herbalism]: ./skills-list.md#herbalism
[stable]: ./buildings-others.md#stable
[herbs list]: ./herbs.md#herbs-list #kräuterliste
