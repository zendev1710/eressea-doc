# Resources

Raw materials can be obtained without other ingredients from the region without further ingredients. However, the deposits are limited and regenerate only slowly or not at all. The necessary skill can be looked up in the section about [goods].

## Extraction of Raw Materials

When exploiting resources, it is important to consider that units on [guard] prevent non-allied factions - having neither [`HELP GUARD`] nor [`HELP ALL`][`HELP GUARD`] to your faction and not [CONTACTing] your unit or faction - from exploiting them. This does not apply if the guarding faction does not see the producer, for example because they are [cloaked].

### About Mining

Iron, stone, laen, and, in particularly ancient regions, sometimes even adamantium, can be mined or quarried from mountains, glaciers, and sometimes other types of regions. Laen and adamantium require a mine and particularly high mining skill. These resources can be difficult to extract. In your report you can find out by the number after the  -->/”. For example, if the report says "20 iron/4", this means that 20 iron can still be mined at skill level 4. Once these have been extracted, miners will need to be level 5 to extract iron from the next layer (5). In general, the quantities that can be extracted increase with each new layer.

### Deep in the Forest

The development of Eressea's vegetation is determined by the seasons. As soon as the first rays of sunlight hit the ground in spring, the seeds hidden in the soil germinate and last year's saplings grow into mature trees. If there isn't enough sun (no free working space), the seeds remain dormant in the soil. During the summer and autumn months, mature trees shed their seeds, which can be collected with the [`MAKE`]`seed / "mallorn seed"` order and the [herbalism] skill (minimum level 3 / 4) and then replanted elsewhere with the [`PLANT`]`seed / "mallorn seed"` order (minimum level 6 / 7).

If wood or mallorn is felled, the forest shrinks and only recovers very slowly. As long as there is enough wood, it can be felled in any quantity. The same applies to mallorn, a 'magic' wood found only in a few regions. Mallorn reproduces like wood, but mallorn seeds only grow in regions that are suitable for them. In regions with mallorn, the order [`MAKE wood`][`MAKE`] can also be used to harvest wood instead of mallorn. The number of mallorn trees is then reduced by the same amount as if mallorn had been felled.

### And Elsewhere

You may capture wild horses as you like with [`MAKE horse`][`MAKE`] by a unit with the [taming skill][herbalism]. Without help, only wild horses reproduce. They love space and freedom, which is why some of them migrate to neighboring regions when there are fewer horses there. However, it is possible to breed captured horses in a [stable] with the taming skill and the order [`BREED HORSES`].

Player experience: SoltharThe maximal amount of horses in a region equals the number of [jobs] / 10. In a relatively empty plain they grow at a rate of 4%. As they approach the upper limit, growth slows down. The most new horses are born at about half the maximal population. In a plain with 25 horses, there is 1 birth per week. With 500 horses there are 10 new horses per round. At 1000 horses there is no more growth.

[jobs]: ./world.md "Welt"

Herbs can also be harvested to make potions. There is a maximum of one herb species in each region. See the [herbs list].

## See also

- [Production]
- [Goods]
- [Roads]
- [Buildings]

Continue reading: [Goods].

[Goods]: ./items.md "Waren"

<!-- From [https://wiki.eressea.de/index.php?title=Rohstoffe/en&oldid=16867] -->

[guard]: ./cmd-guard.md "GUARD (to be documented)"
[`HELP GUARD`]: ./cmd-help.md "HELP"
[CONTACTing]: ./cmd-contact.md "CONTACT"
[cloaked]: ./camouflage.md "Tarnung"
[`MAKE`]: ./cmd-make.md "MAKE"
[herbalism]: ./skills-list.md "Skills list"
[`PLANT`]: ./cmd-plant.md "PLANT"
[stable]: ./buildings-others.md#stable "Pferdezucht"
[`BREED HORSES`]: ./cmd-grow.md "GROW"
[herbs list]: ./herbs.md#kräuterliste "Herbs"
[Production]: ./production.md "Produktion"
[Roads]: ./roads.md "Straßen"
[Buildings]: ./buildings.md "Gebäude"
