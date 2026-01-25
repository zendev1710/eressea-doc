---
# cSpell:locale fr
alias: premier-tour
---
# Premier tour

## Premier rapport

<!-- TODO : find and copy here an english report extract -->
Hier ist ein Beispiel, wie der erste Report (1-37wj.nr) aussehen kann, den du nach der Anmeldung vom Server bekommst:

```text
                Report für E3, Wednesday, 01. July 2009, 19:56
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

Cabyn (0,0), Ebene, 24/6 Bäume, 2308 zufriedene Bauern, 50000 Silber, 52
Pferde. Die Region ist im Besitz von Partei 37wj (37wj). Im Nordwesten der
Region liegt Ozean (-1,1), im Nordosten Ozean (0,1), im Osten die Wüste von
Budesodid (1,0), im Südosten der Sumpf von Bigecod (1,-1), im Südwesten das
Hochland von Tavesrucal (0,-1) und im Westen Ozean (-1,0)

Auf dem Markt werden Juwelen und Flachwurz feilgeboten.

Statistik für Cabyn (0,0):

  Bauerneinnahmen: 11 Silber
  Rekruten: max. 57 Bauern
  Personen: 1
  Holz: 10
  Silber: 5000
  Steine: 10

  Heimat (wvg3), Größe 10, Befestigung.

    * Entdecker (vdko), 1 Goblin, aggressiv, hat: 10 Holz, 5000 Silber, 10
      Steine, "ARBEITEN".

------------------------------------------------------------------------------
                             Liste aller Adressen

  * Partei 37wj (37wj): drac@example.de; (null)

------------------------------------------------------------------------------
```

## Exemple d'un fichier d'ordres

Ce fichier d'ordres, légèrement modifié, a été utilisé lors d'un premier tour d'une partie (pour E3 !).
Je ne sais pas exactement quand elle a commencé.

Note que certains ordres s'étendent sur plusieurs lignes.
Ici, l'ordre `DESCRIBE` avec des commentaires `//` a été utilisé.

Cependant, si tu utilises [Magellan] pour tes ordres, tu n'as pas à t'en soucier.

```text
ERESSEA 37wj "pwpw42"
; du muss natürlich oben dein eigenes Passwort einsetzen
REGION 0,0 ; Cabyn
UNIT vdko;       Entdecker [1,5000$]
    NAME UNIT "Dracheneinreiter"
    ;
    ; Das ist im Moment unsere erste und einzige Einheit,
    ; erstmal ein paar grundsätzliche Einstellungen
    NAME FACTION "Der Drachenclan"
    NUMBER FACTION drac ; hoffentlich noch frei
    OPTION PUNKTE ; Wird erst ab Runde 13 angezeigt
    OPTION TALENTVERSCHIEBUNG
    PREFIX Nebel
    BANNER "Immer schön eines zu haben"
    PASSWORD "Setze das Passwort nie in öffentliche Dokumente"
    ; wir haben schon eine Burg!
    NAME BURG "Drachenhort"
    DESCRIBE BURG "Am Fuße eines Kliffs, das auf das Meer hinausblickt, ist \
    eine Höhle in den Fels gehauen. Eine kleine Mauer mit einem niedrigen Wacht\
    urm schützt das Innere. Der schmale Eingang ist von zwei aufgespießten Schä\
    deln flankiert. Sie sagen: Hier haust der Drachenclan!"
    NAME REGION "Drachental"
    ;
    ; das kann nicht schaden...
    LEARN Pferdedressur
    ; Burgenbesitzer setze ich gerne auf COMBAT NOT, damit sie die Burg nicht 
    ; aus Versehen bei der Flucht verlassen ...
    COMBAT NOT
    ;
    ; Zeit für die erste neue Einheit
    ; Rekrutierungssilber sollte besser übergeben werden
    ; Lernkosten und Einheitenunterhalt holt sie sich notfalls aus dem Pool
    GIVE TEMP dr01 460 Silber
    MAKE TEMP dr01
        NAME UNIT "prismatischer Drache"
        RECRUIT 1 Dämon
        LEARN Magie "Illaun"
        COMBAT FLEE
        // Bei Gelegenheit COMBAT REAR
    END
    ;
    ; Man muss sich genau überlegen, ob man im ersten Zug schon genug Geld für
    ; drei Magier hat. Eigentlich lohnen sich Magier aber immer, besonders
    ;  Dämonen. Zur Not haben sie einen Zauber, mit dem sie Geld verdienen können
    ; -- und dabei lernen sie sogar noch was dazu!
    GIVE TEMP dr02 460 Silber
    GIVE TEMP dr03 460 Silber
    MAKE TEMP dr02
        NAME UNIT "prismatischer Drache"
        RECRUIT 1 Dämon
        LEARN Magie "Illaun"
        COMBAT FLEE
    END
    ;
    MAKE TEMP dr03
        NAME UNIT "prismatischer Drache"
        RECRUIT 1 Dämon
        LEARN Magie "Illaun"
        COMBAT FLEE
    END
    ;
    ; wird es sich lohnen, sich so früh schon Elitekämpfer (Helden!) zu leisten?
    GIVE TEMP dr05 720 Silber
    MAKE TEMP dr05
        NAME UNIT "Schattendrache"
        RECRUIT 2 Dämon
        LEARN Stangenwaffen
        // Held?
        ; wir sind zwar noch unbewaffnet, aber bevor wir es später vergessen
        COMBAT AGGRESSIVE
    END
    ;
    ; wenn er das Mindesttalent erreicht hat, produzieren wir hoffentlich schon
    ; Holz oder Eisen
    GIVE TEMP dr06 66 Silber
    MAKE TEMP dr06
        NAME UNIT "grauer Drache"
        RECRUIT 1
        LEARN Waffenbau
        COMBAT FLEE
    END
    ;
    ; Burgen kontrollieren in E3 Regionen, deshalb sind sie schon früh wichtig!
    GIVE TEMP dr07 66 Silber
    MAKE TEMP dr07
        NAME UNIT "grauer Drache"
        RECRUIT 1
        LEARN Burgenbau
        COMBAT FLEE
    END
    ;
    ; evtl. wollen wir hier noch mehr Burgenbauer...
    ;
    ; Holz ist am Anfang super wichtig für Waffen und Wachposten,
    ; später für Gebäude, Schiffe
    GIVE TEMP dr08 180 Silber
    MAKE TEMP dr08
        NAME UNIT "grüner Drache"
        RECRUIT 3
        LEARN Holzfällen
        COMBAT FLEE
    END
    ;
    ; Wollen wir uns auf Nahkampf oder Fernkampf, Bögen oder Armbrüste
    ; spezialisieren? Evtl. ist es gefährlich, das zu früh zu tun.
    GIVE TEMP dr10 660 Silber
    MAKE TEMP dr10
        NAME UNIT "Drachenflügel"
        RECRUIT 10
        LEARN Armbrustschießen
        COMBAT FLEE
    END
    ;
    ; Eisen zu finden ist auch wichtig
    GIVE TEMP dr11 180 Silber
    MAKE TEMP dr11
        NAME UNIT "Höhlendrache"
        RECRUIT 3
        LEARN Bergbau
        // als Späher in Nachbarregionen
        COMBAT FLEE
    END
    ;
    ; ...ebenso wie Steine für Burgen
    GIVE TEMP dr12 180 Silber
    MAKE TEMP dr12
        NAME UNIT "Höhlendrache"
        RECRUIT 3
        LEARN Steinbau
        COMBAT FLEE
    END
    ;
    ; Wir brauchen Späher, vermutlich mindestens einen für jede Himmelsrichtung
    ; Wichtig: Unterhaltssilber nicht vergessen!
    GIVE TEMP drr1 260 Silber
    MAKE TEMP drr1
        NAME UNIT "kleiner Drachenreiter"
        RECRUIT 1
        MOVE sw
        // Stein- und Bergbauer machen
        COMBAT FLEE
    END
    ;
    GIVE TEMP drr2 260 Silber
    MAKE TEMP drr2
        NAME UNIT "kleiner Drachenreiter"
        RECRUIT 1
        MOVE so
        // Stein- und Bergbauer machen
        COMBAT FLEE
    END
    ;
    ;
    ;  in E2 müssten wir jetzt noch unbedingt Unterhalter rekrutieren!
    ; ...
    ; Vielleicht sollten wir auch noch Reiter (Steintransport!), Wagenbauer,
    ; Rüstungsbauer oder noch mehr Soldaten ausbilden? Andererseits sollte man 
    ; sich am Anfang nicht übernehmen und sehr genau aufpassen, dass man nicht
    ; plötzlich pleite ist!
NEXT
```

## Voir aussi

- Un autre [Tutoriel Eressea] (actuellement seulement en allemand)

Poursuivre la lecture : [protection du chiot].

[protection du chiot]: ./puppy-protection.md

<!-- From [https://wiki.eressea.de/index.php?title=Der\_erste\_Zug&oldid=7430] -->

[Magellan]: ./magellan.md
[Tutoriel Eressea]: https://playeressea.wordpress.com/eressea-tutorium/ "Tutoriel Erressea en allemand (web)"
