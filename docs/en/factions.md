# Factions

Players lead so-called **factions** on Eressea. A faction initially consists of one, later sometimes many units. These units consist of one, a few or even thousands of people from the [race] of the faction. Each unit can have any number of items and silver, and can also learn all [skills] of Eressea. You can give units [orders] every turn, which they will carry out as well as they can.

You drop out of the game if your faction has no more members, that is, if all units are destroyed or disbanded, or if no orders have been received for five consecutive turns (5 NMR).

## Units

A faction starts a game with one **unit** consisting of one person with 2500 silver, 10 wood, 4 stones and a [race-specific starting gift]. A hint: if you do not know what you have there, try the order [`SHOW "`*`Item`*`"`]. This first person is not special in any way; they are just the first person belonging to your new faction. You can [recruit] new persons, and eventually [produce items], and build [buildings] and [ships], tame [horses], forge [weapons] and so on.

New units are created by generating them with an existing unit using the [MAKE TEMP] order. A new unit has no people, yet: you first have to [transfer] them from another unit or recruit them, which requires [money]. Units created by units on ships or buildings will start inside the same ship or building.

A faction can only have a certain number of units, known as the **unit limit**. It is currently at 2500 units, which is also shown in the report. Da unit limit prevents the creation of new units. It does not matter if units have been disbanded during the turn. Under certain circumstances it may be possible that a faction has more units than the limit allows. The surplus units are not deleted; you merely cannot create new units until the number of units goes below the limit again.

Here is an example for units:

        * Konrad Rabenhelm (tb2), 1 human, front, guard the region, skills:
        melee 1, taxation 2, has: sword, 20 silver, "TAX";
        Konrad Rabenhelm ist ein typischer Ritter seines Ordens. Der Orden der
        Gerechtigkeit ist bekannt für seine düsteren und zurückhaltenden 
        Mitglieder. Sie scheinen alle an einem finsteren Erlebnis zu nagen.
       
      - Botschafter des Clans (2ow), anonymous, 1 dwarf, has: horse,
        silverbag; Der Botschafter ist auf der Suche nach befreundeten Völkern
        und solchen, die es werden wollen.
       
      + Kieselnasen (kies), Gesteinsfreunde (135), 4 trolls, has: 1 cart, 30 gems.

Your own units are marked with a '\*'. Units of other factions are marked with '-', or '+' if you [help] that faction.

Each unit has a unique computer-generated number, which is used as in identifier in all orders, in this example it is tb2. You may find the term "number" strange, but in Eressea units are given "base 36" numbers: along with the digits 0–9, the letters a–z are also valid "digits" here. Every unit also has a name ("Konrad Rabenhelm") and maybe a description (following the semicolon). The belongings and, if available, the skills are also displayed.

Many of the descriptions that you encounter during the game will be in German, because the majority of players is also German. You may use any language you feel comfortable with for naming and describing your units, just bear in mind how that may affect the experience of your co-players.

The first unit in the example is a unit of the faction that received that report. It consists of one human of that faction, which is not explicitly mentioned. It has 20 silver and knows how to wield melee weapons: it has level 1 in this skill. It masters [taxation] at level 2 (for more on [skills] see the corresponding chapter). As you can see, Konrad also has a sword. "`TAX`" is his so-called [default order]. If the unit is not given new orders for the next round, it will continue gathering taxes. Only one default order is ever given in the NR, but units may sometimes have more than one. They will be only listed in the CR or in the template orders. More on this in the chapter on [orders].

Units have a "combat status", which is "front" in this case. The details are explained in the chapter about [war] in the section on [combat rows] and the explanation of the order [`COMBAT`].

A unit may guard a region (for more on the consequences, see [`GUARD`]). This will be noted with "guards the region" in the report.

At last, a unit may be wounded by a [combat][war] or [Hunger]. This will be noted with "exhausted", "wounded", or even "badly wounded".

The next unit has the number 2ow, consists of a dwarf and has a horse and a silver bag. This means that it has at least 500 silver. If it had more than 5000 silver, you would see a "silverchest". With less than 500 you wouldn't see anything for a foreign unit. You cannot see which faction the unit belongs to because it is [cloaked], that is, it does not reveal the faction it belongs to. This is probably not a very smart choice for a "Botschafter" (ambassador), because you do not even get the E-Mail address of the faction now. The only thing you can do is sending it a [`MESSAGE`].

Finally you have some allied [trolls] carrying gems. In addition to [humans], [dwarves], and [trolls][1], there are a lot of other races in Eressea. They are describe in [this chapter][race].

You only get limited information on foreign units. Their combat status, injuries, skills, faction, faction stealth, racial stealth, hero status, and spells are hidden. Most items are visible, but silver, herbs and magic items are not visible in detail.

### Dissolving units

If a unit happens to have no persons at the [end of the round] (be it from hunger, giving away persons or never getting them) it will be disbanded. Her items go to a unit of your faction, if one is there, or to an allied faction otherwise. (It must have [`HELP silver`] towards that faction and that faction must have `HELP GIVE` towards us.) Usually the first such unit in the order of the report will be selected for this. If both options are not possible, silver and horses go to the region and all other items are lost.

Player experience: SoltharThere have been cases where special magic items produced an unholy nergy which kept their bearers in a state between life and death. But they were no longer under the control of their former faction.

## See also

- [The faction pool]
- [Orders]

|     |     |
| --- | --- |
| Continue reading: | [Races] |

[Races]: /Spezial:Meine_Sprache/Rassen "Spezial:Meine Sprache/Rassen"  

Abgerufen von „[https://wiki.eressea.de/index.php?title=Parteien/en&oldid=16635]“

[Kategorie][]:

- [Regeln/en]

  [race]: /Spezial:Meine_Sprache/Rassen "Spezial:Meine Sprache/Rassen"
  [skills]: ./skills.md "Spezial:Meine Sprache/Talente"
  [orders]: /Spezial:Meine_Sprache/Befehl "Spezial:Meine Sprache/Befehl"
  [race-specific starting gift]: /Spezial:Meine_Sprache/Geschichte_von_Eressea#Start_der_6._Welt "Spezial:Meine Sprache/Geschichte von Eressea"
  [`SHOW "`*`Item`*`"`]: /Spezial:Meine_Sprache/ZEIGE "Spezial:Meine Sprache/ZEIGE"
  [recruit]: /Spezial:Meine_Sprache/REKRUTIERE "Spezial:Meine Sprache/REKRUTIERE"
  [produce items]: /Spezial:Meine_Sprache/Gegenst%C3%A4nde "Spezial:Meine Sprache/Gegenstände"
  [buildings]: /Spezial:Meine_Sprache/Geb%C3%A4ude "Spezial:Meine Sprache/Gebäude"
  [ships]: /Spezial:Meine_Sprache/Schiffe "Spezial:Meine Sprache/Schiffe"
  [horses]: /Spezial:Meine_Sprache/Pferd_und_Wagen "Spezial:Meine Sprache/Pferd und Wagen"
  [weapons]: ./war.mdstabellen "Spezial:Meine Sprache/Kriegstabellen"
  [MAKE TEMP]: /Spezial:Meine_Sprache/MACHE "Spezial:Meine Sprache/MACHE"
  [transfer]: /Spezial:Meine_Sprache/GIB "Spezial:Meine Sprache/GIB"
  [money]: /Spezial:Meine_Sprache/Ausgaben "Spezial:Meine Sprache/Ausgaben"
  [help]: /Spezial:Meine_Sprache/Allianz "Spezial:Meine Sprache/Allianz"
  [taxation]: /Spezial:Meine_Sprache/TREIBE "Spezial:Meine Sprache/TREIBE"
  [default order]: /Spezial:Meine_Sprache/DEFAULT "Spezial:Meine Sprache/DEFAULT"
  [war]: ./war.md "Spezial:Meine Sprache/Krieg"
  [combat rows]: /Spezial:Meine_Sprache/Schlacht#Kampfreihen "Spezial:Meine Sprache/Schlacht"
  [`COMBAT`]: /Spezial:Meine_Sprache/K%C3%84MPFE "Spezial:Meine Sprache/KÄMPFE"
  [`GUARD`]: /Spezial:Meine_Sprache/BEWACHE "Spezial:Meine Sprache/BEWACHE"
  [Hunger]: /Spezial:Meine_Sprache/Hunger "Spezial:Meine Sprache/Hunger"
  [cloaked]: /Spezial:Meine_Sprache/TARNE "Spezial:Meine Sprache/TARNE"
  [`MESSAGE`]: /Spezial:Meine_Sprache/BOTSCHAFT "Spezial:Meine Sprache/BOTSCHAFT"
  [trolls]: /Spezial:Meine_Sprache/Trolle "Spezial:Meine Sprache/Trolle"
  [humans]: /Spezial:Meine_Sprache/Mensch "Spezial:Meine Sprache/Mensch"
  [dwarves]: /Spezial:Meine_Sprache/Zwerg "Spezial:Meine Sprache/Zwerg"
  [1]: /Spezial:Meine_Sprache/Troll "Spezial:Meine Sprache/Troll"
  [end of the round]: /Spezial:Meine_Sprache/Befehlsreihenfolge "Spezial:Meine Sprache/Befehlsreihenfolge"
  [`HELP silver`]: /Spezial:Meine_Sprache/HELFE "Spezial:Meine Sprache/HELFE"
  [The faction pool]: /Spezial:Meine_Sprache/Parteipool "Spezial:Meine Sprache/Parteipool"
  [https://wiki.eressea.de/index.php?title=Parteien/en&oldid=16635]: https://wiki.eressea.de/index.php?title=Parteien/en&oldid=16635
  [Kategorie]: /Spezial:Kategorien "Spezial:Kategorien"
  [Regeln/en]: /index.php?title=Kategorie:Regeln/en&action=edit&redlink=1 "Kategorie:Regeln/en (Seite nicht vorhanden)"
