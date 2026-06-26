---
# cSpell:locale en
alias: first-round
---

[](){ #first-round-id }

# The first round

## The first report

Here is an example of what the first report (named here `1-37wj.nr`) that you get from the server after subscribing might look like:

```text
            Report for Eressea, Wednesday, 01. July 2026, 19:56
it's the first week of the month of harvest moon in the 1. year of the second
                        age. It's summer.

    Faction 37wj (37wj), goblins/no magic school (drac@example.de)
Remember to send your orders to eressea-server@kn-bremen.de with the subject
                        ERESSEA 2 ORDERS.

            Your faction has 1 person in 1 of 2500 possible units.

        Options: REPORT COMPUTER TEMPLATE STATISTICS ZIPPED ADDRESSES

                                Notifications

Your faction will be protected against attacks for the next 6 weeks.

                                Events

The password of this faction is 'pwpw42'.

                            Economy and Trade

Unit drac (drac) in Rivudrit (0,0) earns 10 silver.

------------------------------------------------------------------------------

Cabyn (0,0), Plain, 24/6 trees, 2308 peasants, 50000 Silver, 52 horses.
To the northwest the ocean (-1,1), to the northeast the ocean (0,1), to the
east the deserts of Budesodid (1,0), to the southeast the swamps of Bigecod
(1,-1), to the southwest the highlands of Tavesrucal (0,-1) to the west the
ocean (-1,0).

The local market offers gem at a price of 5 silver. Traders can sell incense
for 16 silver, silk for 6 silver, oil for 9 silver, myrrh for 10 silver, spice
for 28 silver and balm for 12 silver.

Statistics für Cabyn (0,0):

  entertainment: max. 4198 silver
  worker salary: 11 Silver
  recruits: max. 57 peasants
  people: 1
  wood: 10
  silver: 5000
  stones: 10

  Heimat (wvg3), size 10, Fortification.

    * Unit vdko (vdko), 1 Goblin, aggressiv, has: 10 wood, 5000 silver,
      10 stones, "WORK".
------------------------------------------------------------------------------

                             Political Status

------------------------------------------------------------------------------

                                Addresses

  * Faction 37wj (37wj): drac@example.de;
```

## Example of an orders file

This orders file, in a slightly modified version, was actually used as the first round in a game (for E3!).  
I don't know exactly when it started.

Note that orders spanning more than one line.  
here the `DESCRIBE` order with backslash (//) were used.  
However, if you're using [Magellan][magellan-id] for your orders, you don't need to worry about this.

```text
ERESSEA 37wj "pwpw42"
; Of course you have to enter your own password above
REGION 0,0 ; Cabyn
UNIT vdko;       Explorer [$1,5000]
    NAME UNIT “Dragon Rider”
    ;
    ; This is our first and only unit at the moment,
    ; First a few basic settings
    NAME FACTION "The Dragon Clan"
    NUMBER FACTION drac ; hopefully still free
    OPTION SCORE; Only shown from round 13 onwards
    OPTION TALENTVERSCHIEBUNG
    PREFIX Fog
    BANNER "Always nice to have one"
    PASSWORD "Never put the password in public documents"
    ; we already have a castle!
    NAME CASTLE "Dragon's Lair"
    DESCRIBE CASTLE "At the foot of a cliff overlooking the sea is\
    a cave carved into the rock. A small wall with a low guard\
    urm protects the inside. The narrow entrance is surrounded by two impaled heads.
    flanked by dolphins. They say: The Dragon Clan lives here!"
    NAME REGION "Dragon Valley"
    ;
    ; that can't hurt...
    LEARN Taming
    ; I like to set castle owners to COMBAT NOT so that they can't take the castle
    ; accidentally abandoned while escaping...
    COMBAT NOT
    ;
    ; Time for the first new unit
    ; Recruitment silver should be better handed over
    ; If necessary, takes learning costs and unit maintenance out of the pool
    GIVE TEMP dr01 460 Silver
    MAKE TEMP dr01
        NAME UNIT "Prismatic Dragon"
        RECRUIT 1 Demon
        LEARN Magic "Illaun"
        COMBAT FLEE
        // On occasion COMBAT REAR
    END
    ;
    ; You have to think carefully about whether you have enough money for the first move
    ; has three magicians. Actually, magicians are always worth it, especially Demons.
    ; In a pinch, they have a spell they can use to make money
    ; --and they even learn something new!
    GIVE TEMP dr02 460 Silver
    GIVE TEMP dr03 460 Silver
    MAKE TEMP dr02
        NAME UNIT "Prismatic Dragon"
        RECRUIT 1 Demon
        LEARN Magic "Illaun"
        COMBAT FLEE
    END
    ;
    MAKE TEMP dr03
        NAME UNIT "Prismatic Dragon"
        RECRUIT 1 Demon
        LEARN Magic "Illaun"
        COMBAT FLEE
    END
    ;
    ; Will it be worth it to buy elite fighters (heroes!) so early?
    GIVE TEMP dr05 720 Silver
    MAKE TEMP dr05
        NAME UNIT "Shadow Dragon"
        RECRUIT 2 Demon
        LEARN Polearm
        // Hero?
        ; We are still unarmed, but lest we forget it later
        COMBAT AGGRESSIVE
    END
    ;
    ; If he has reached the minimum talent level, hopefully we will be producing
    ; wood or iron
    GIVE TEMP dr06 66 Silver
    MAKE TEMP dr06
        NAME UNIT "Gray Dragon"
        RECRUIT 1
        LEARN Weaponsmithing
        COMBAT FLEE
    END
    ;
    ; Castles control regions in E3, so they're important early on!
    GIVE TEMP dr07 66 Silver
    MAKE TEMP dr07
        NAME UNIT "Gray Dragon"
        RECRUIT 1
        LEARN Masonry
        COMBAT FLEE
    END
    ;
    ; Maybe we want more castle builders here...
    ;
    ; Wood is super important in the beginning for weapons and guard posts,
    ; later for buildings, ships
    GIVE TEMP dr08 180 Silver
    MAKE TEMP dr08
        NAME UNIT "Green Dragon"
        RECRUIT 3
        LEARN Forestry
        COMBAT FLEE
    END
    ;
    ; Do we want to focus on melee or ranged combat, bows or crossbows
    ; specialize? It may be dangerous to do this too early.
    GIVE TEMP dr10 660 Silver
    MAKE TEMP dr10
        NAME UNIT "Dragon Wings"
        RECRUIT 10
        LEARN Crossbow
        COMBAT FLEE
    END
    ;
    ; Finding iron is also important
    GIVE TEMP dr11 180 Silver
    MAKE TEMP dr11
        NAME UNIT "Cave Dragon"
        RECRUIT 3
        LEARN Mining
        // as a scout in neighboring regions
        COMBAT FLEE
    END
    ;
    ; ...eas well as stones for castles
    GIVE TEMP dr12 180 Silver
    MAKE TEMP dr12
        NAME UNIT "Cave Dragon"
        RECRUIT 3
        LEARN Quarrying
        COMBAT FLEE
    END
    ;
    ; We need scouts, probably at least one for each direction
    ; Important: Don’t forget your maintenance silver!
    GIVE TEMP drr1 260 Silver
    MAKE TEMP drr1
        NAME UNIT "Little Dragon rider"
        RECRUIT 1
        MOVE sw
        // Quarrying and mining
        COMBAT FLEE
    END
    ;
    GIVE TEMP drr2 260 Silver
    MAKE TEMP drr2
        NAME UNIT "Little Dragon rider"
        RECRUIT 1
        MOVE so
        // Quarrying and mining
        COMBAT FLEE
    END
    ;
    ;
    ;  We still have to recruit entertainers!
    ; ...
    ; Maybe we should also add riders (transporting stone!), cartmakers,
    ; Armourers or training more soldiers? On the other hand, you should
    ; Don't overdo it at the beginning and be very careful not to
    ; suddenly broke!
NEXT
```

## See also

- Another one [Eressea Tutorial] (currently only in German)

Continue reading: [puppy protection][puppy-protection].

<!-- From [https://wiki.eressea.de/index.php?title=Der\_erste\_Zug&oldid=7430] -->

[Eressea Tutorial]: https://playeressea.wordpress.com/eressea-tutorium/ "Erressea Tutorial in German (web)"
