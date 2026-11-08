---
# cSpell:locale fr
alias: premier-tour
---

# Premier tour

## Premier rapport

Voici ce à quoi pourrait ressembler un exemple de premier rapport (`1-37wj.nr`) envoyé par le serveur après inscription :

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

## Exemple de fichier d'ordres

Ce fichier d'ordres, légèrement modifié, a été utilisé lors d'un premier tour d'une partie (pour E3).  
Nous ne savons pas exactement quand elle a débuté.  

Notez que certains ordres s'étendent sur plusieurs lignes.  
Ici, l'ordre `DESCRIBE` avec le délimiteur de retour à la ligne `\` a été utilisé.  

Cependant, si vous utilisez [Magellan][magellan-fr-id] pour vos ordres, vous n'avez pas à vous en soucier.  

```text
ERESSEA 37wj "pwpw42"
; Vous devez bien sûr renseigner votre propre mot de passe ci-dessus.
REGION 0,0 ; Cabyn
UNIT vdko;       Explorateur [1,5000$]
    NAME UNIT "Le Chevaucheur du Dragon"
    ;
    ; Il s'agit actuellement de notre premier et unique unité,
    ; Tout d'abord, quelques réglages de base.
    NAME FACTION "Le clan des Dragons"
    NUMBER FACTION drac ; j'espère que l'id sera disponible
    OPTION SCORE; Affiché uniquement à partir du tour 13
    OPTION TALENTVERSCHIEBUNG
    PREFIX Fog
    BANNER "C'est toujours agréable d'en avoir un."
    PASSWORD "Ne jamais consigner le mot de passe dans des documents publics"
    ; Nous avons déjà un château !
    NAME CASTLE "Repaire du Dragon"
    DESCRIBE CASTLE "Au pied d'une falaise surplombant la mer, une \
    grotte creusée dans la roche. Un petit muret avec une tour de guet basse\
    protège l'intérieur. L'étroite entrée est flanquée de deux crânes empalés.\
    Il est écrit à l'entrée : Ici réside le Clan du Dragon !"
    NAME REGION "Vallée du Dragon"
    ;
    ; Ça ne peut pas faire de mal...
    LEARN Taming
    ; j'aime paramétrer les propriétaires de châteaux sur « COMBAT NOT »
    ; pour qu'ils ne quittent pas accidentellement leur château en fuyant...
    COMBAT NOT
    ;
    ; Il est temps de créer notre première nouvelle unité
    ; L'argent du recrutement doit être remis
    ; Si nécessaire, l'unité prendra en charge les frais de formation
    ; et d'entretien du matériel grâce aux fonds communs.
    GIVE TEMP dr01 460 Silver
    MAKE TEMP dr01
        NAME UNIT "Dragon prismatique"
        RECRUIT 1 Demon
        LEARN Magic "Illaun"
        COMBAT FLEE
        // À l'occasion COMBAT REAR
    END
    ;
    ; Il vous faut bien réfléchir avant d'engager trois mages, afin de vous assurer d'en avoir assez dès le premier tour.
    ; Les mages sont généralement toujours un bon investissement, surtout les démons.
    ; Au besoin, ils disposent d'un sort pour gagner de l'argent, et ils apprennent même quelque chose au passage !
    GIVE TEMP dr02 460 Silver
    GIVE TEMP dr03 460 Silver
    MAKE TEMP dr02
        NAME UNIT "Dragon prismatique"
        RECRUIT 1 Demon
        LEARN Magic "Illaun"
        COMBAT FLEE
    END
    ;
    MAKE TEMP dr03
        NAME UNIT "Dragon prismatique"
        RECRUIT 1 Dämon
        LEARN Magic "Illaun"
        COMBAT FLEE
    END
    ;
    ; Investir dans des combattants d'élite (des héros !) aussi tôt sera-t-il judicieux ?
    GIVE TEMP dr05 720 Silver
    MAKE TEMP dr05
        NAME UNIT "Dragon de l'Ombre"
        RECRUIT 2 Demon
        LEARN Polearm
        // Héros ?
        ; Nous sommes toujours désarmés, mais avant d'oublier
        COMBAT AGGRESSIVE
    END
    ;
    ; Une fois qu'il aura atteint le niveau de compétence minimum, espérons que la production aura commencé.
    ; bois ou fer
    GIVE TEMP dr06 66 Silver
    MAKE TEMP dr06
        NAME UNIT "Dragon gris"
        RECRUIT 1
        LEARN Weaponsmithing
        COMBAT FLEE
    END
    ;
    ; Les châteaux contrôlent des régions dans E3, c'est pourquoi ils sont importants dès le début !
    GIVE TEMP dr07 66 Silver
    MAKE TEMP dr07
        NAME UNIT "Dragon gris"
        RECRUIT 1
        LEARN Masonry
        COMBAT FLEE
    END
    ;
    ; Peut-être avons-nous besoin de plus de maçons ici...
    ;
    ; Le bois est extrêmement important au début pour les armes et les postes de garde,
    ; puis pour les bâtiments et les navires.
    GIVE TEMP dr08 180 Silver
    MAKE TEMP dr08
        NAME UNIT "Dragon vert"
        RECRUIT 3
        LEARN Forestry
        COMBAT FLEE
    END
    ;
    ; Souhaitons-nous nous spécialiser dans le combat au corps à corps ou à distance,
    ; les arcs ou les arbalètes ? Il pourrait être dangereux de le faire trop tôt.
    GIVE TEMP dr10 660 Silver
    MAKE TEMP dr10
        NAME UNIT "Ailes de dragon"
        RECRUIT 10
        LEARN Crossbow
        COMBAT FLEE
    END
    ;
    ; Trouver du fer est également important
    GIVE TEMP dr11 180 Silver
    MAKE TEMP dr11
        NAME UNIT "Dragon des cavernes"
        RECRUIT 3
        LEARN Mining
        // comme éclaireurs dans les régions voisines
        COMBAT FLEE
    END
    ;
    ; ...ainsi que des pierres pour les châteaux
    GIVE TEMP dr12 180 Silver
    MAKE TEMP dr12
        NAME UNIT "Dragon des cavernes"
        RECRUIT 3
        LEARN Quarrying
        COMBAT FLEE
    END
    ;
    ; Il nous faut des éclaireurs, probablement au moins un pour chaque point cardinal.
    ; Important : n'oubliez pas l'argent pour l'entretien !
    GIVE TEMP drr1 260 Silver
    MAKE TEMP drr1
        NAME UNIT "petit chevaucheur de dragon"
        RECRUIT 1
        MOVE sw
        // Extraire des pierres et du fer
        COMBAT FLEE
    END
    ;
    GIVE TEMP drr2 260 Silver
    MAKE TEMP drr2
        NAME UNIT "petit chevaucheur de dragon"
        RECRUIT 1
        MOVE so
        //  Extraire des pierres et du fer
        COMBAT FLEE
    END
    ;
    ;
    ; Nous avons absolument besoin de recruter des artistes dès maintenant !
    ; ...
    ; Peut-être devrions-nous aussi former de la cavalerie (pour le transport des pierres !), des chariots,
    ; des armuriers, voire davantage de soldats ? Par ailleurs, il ne faut pas
    ; se surestimer au début et veiller scrupuleusement à ne pas se retrouver soudainement en faillite !
NEXT
```

## Voir aussi

- Un autre [Tutoriel Eressea] (actuellement seulement en allemand)

Poursuivre la lecture : [[protection-du-chiot]].

<!-- From [https://wiki.eressea.de/index.php?title=Der\_erste\_Zug&oldid=7430] -->

[Tutoriel Eressea]: https://playeressea.wordpress.com/eressea-tutorium/ "Tutoriel Erressea en allemand (web)"
