---
# cSpell:locale fr
alias: premier-tour
---
<!-- disable MD052 because of mkdocs autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Premier tour

## Premier rapport

<!-- TODO : find and copy here an english report extract -->
Hier ist ein Beispiel, wie der erste Report (1-37wj.nr) aussehen kann, den du nach der Anmeldung vom Server bekommst:

```text
                Report für E2, Wednesday, 01. July 2009, 19:56
   Wir schreiben die erste Woche des Monats Feldsegen im Jahre 1 des dritten
                          Zeitalters. Es ist Sommer.

        Partei 37wj (37wj), Gobelins/Kein Magiegebiet (drac@example.de)

                          Dein Passwort lautet pwpw42.

        Bitte denke daran, deine Befehle mit dem Betreff ERESSEA 3 BEFEHLE an
                     eressea-server@eressea.kn-bremen.de zu senden.

   Die ersten beiden Züge mußt du abgeben, sonst wird deine Partei sofort
               wieder gelöscht, um Karteileichen zu vermeiden.

                  Deine Partei hat 1 Personen in 1 Einheiten.

      Optionen: AUSWERTUNG COMPUTER ZUGVORLAGE STATISTIK ZIPPED ADRESSEN
                             TALENTVERSCHIEBUNGEN

                                  Ereignisse

Das Passwort für diese Partei lautet pwpw42.

                               Aktueller Status

------------------------------------------------------------------------------

Cabyn (0,0), Ebene, 24/6 Bäume, 2308 zufriedene Bauern, 50000 Silver, 52
Pferde. Die Region ist im Besitz von Partei 37wj (37wj). Im Nordwesten der
Region liegt Ozean (-1,1), im Nordosten Ozean (0,1), im Osten die Wüste von
Budesodid (1,0), im Südosten der Sumpf von Bigecod (1,-1), im Südwesten das
Hochland von Tavesrucal (0,-1) und im Westen Ozean (-1,0)

Auf dem Markt werden Juwelen und Flachwurz feilgeboten.

Statistik für Cabyn (0,0):

  Bauerneinnahmen: 11 Silver
  Rekruten: max. 57 Bauern
  Personen: 1
  Holz: 10
  Silver: 5000
  Steine: 10

  Heimat (wvg3), Größe 10, Befestigung.

    * Entdecker (vdko), 1 Goblin, aggressiv, hat: 10 Holz, 5000 Silver, 10
      Steine, "ARBEITEN".

------------------------------------------------------------------------------
                             Liste aller Adressen

  * Partei 37wj (37wj): drac@example.de; (null)

------------------------------------------------------------------------------
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
    PREFIX Nebel
    BANNER "C'est toujours agréable d'en avoir un."
    PASSWORD "Ne jamais consigner le mot de passe dans des documents publics"
    ; Nous avons déjà un château !
    NAME BURG "Repaire du Dragon"
    DESCRIBE CASTLE "Au pied d'une falaise surplombant la mer, une \
    grotte creusée dans la roche. Un petit muret avec une tour de guet basse\
    protège l'intérieur. L'étroite entrée est flanquée de deux crânes empalés.\
    Il est écrit à l'entrée : Ici réside le Clan du Dragon !"
    NAME REGION "Vallée du Dragon"
    ;
    ; Ça ne peut pas faire de mal...
    LEARN Pferdedressur
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
    ; Une fois qu'il aura atteint le niveau de compétence minimum, nous espérons déjà avoir commencé la production.
    ; bois ou fer
    GIVE TEMP dr06 66 Silver
    MAKE TEMP dr06
        NAME UNIT "Dragon gris"
        RECRUIT 1
        LEARN Waffenbau
        COMBAT FLEE
    END
    ;
    ; Les châteaux contrôlent des régions, c'est pourquoi ils sont importants dès le début !
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
    ; Souhaitons-nous nous spécialiser le combat au corps à corps ou à distance,
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
        LEARN Mininh
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
    ; Peut-être devrions-nous aussi former de la cavalerie (pour le transport des pierres !), des charrons,
    ; des armuriers, voire davantage de soldats ? Par ailleurs, il ne faut pas
    ; se surestimer au début et veiller scrupuleusement à ne pas se retrouver soudainement en faillite !
NEXT
```

## Voir aussi

- Un autre [Tutoriel Eressea] (actuellement seulement en allemand)

Poursuivre la lecture : [[protection-du-chiot]].

<!-- From [https://wiki.eressea.de/index.php?title=Der\_erste\_Zug&oldid=7430] -->

[Tutoriel Eressea]: https://playeressea.wordpress.com/eressea-tutorium/ "Tutoriel Erressea en allemand (web)"
