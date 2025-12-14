---
alias:
    name: cmd-default
    text: DEFAULT
---
# DEFAULT

**`DEFAULT`**`"`*`befehl`*`"`

`DEFAULT` ändert den [Befehl], den eine Einheit normalerweise *in der nächsten Woche* ausführen würde:

## Zugvorlage und Defaultbefehle

Nachdem ich meine Befehle eingeschickt habe und der Server die Auswertung erstellt hat, kommen für jede Einheit bestimmte Befehle zurück. Das sind die Defaultbefehle. Sie werden in der nächsten Woche ausgeführt, falls du *für diese Einheit* keine Befehle einschickst. Die Defaultbefehle bekommst du mit dem Report als Textdatei (auch Zugvorlage oder Befehlsvorlage genannt) zugeschickt, falls du sie nicht mit [[cmd-option]]`ZUGVORLAGE NOT` abgeschaltet hast. Außerdem sind sie im Computerreport (CR) enthalten. Der Normalreport (NR) enthält immer nur den ersten langen Defaultbefehl. Man kann dort also nicht alle Defaultbefehle sehen.

In die Defaultbefehle einer Einheit werden normalerweise alle [langen Befehle] übernommen. Ausgenommen davon sind ATTACK, FOLLOW und MOVE. Außerdem werden alle [//]-Kommentare und alle Befehle, die mit @ beginnen übernommen. Die Schreibweise wird dabei möglicherweise standardisiert.

Eingeschickte Befehle:

     UNIT abc
     ; diese Woche nur 10
     kAufe 10 Bals
     SELL 100 Öl
     // nächste Woche mehr Balsam kaufen
     @GIVE xyz ALLES Balsam ; Transporter
     GIVE abc 100 Silber
     RECRUIT 1

Defaultbefehle der nächsten Woche

     UNIT abc
     BUY 10 Bals
     SELL 100 Öl
     // nächste Woche mehr Balsam kaufen
     @GIVE xyz ALLES Balsam ; Transporter

Was passiert, wenn die Einheit illegalerweise mehrere lange Befehle bekommen hat (zum Beispiel LEARN und WORK), ist übrigens nicht genau definiert. Das Gleiche gilt für sonstige ungültige Befehle.

## Der Befehl DEFAULT

Der Befehl DEFAULT ändert dieses Verhalten, indem die Defaultbefehle, die vom Server zurückkommen, verändert werden. Wenn die Einheit einen DEFAULT-Befehl bekommen hat, werden ihre **langen** Befehle nicht in die Vorlage übernommen. [Lange Kommentare] (mit `//`) und kurze @-Befehle werden dagegen übernommen. Die gegebenen Befehle werden dabei bis zu einem gewissen Grade validiert. Ungültige Befehle werden also nicht übernommen. Diese Prüfung hat jedoch Grenzen, es ist besser, sich nicht darauf zu verlassen.

Man kann auch kurze Befehle mit dem Befehl DEFAULT einfügen.

Eingeschickte Befehle:

     UNIT abc
     ; diese Woche nur 10
     Kaufe 10 Balsam
     SELL 100 Öl
     // nächste Woche lernen
     @GIVE xyz ALLES Balsam ; Transporter
     GIVE abc 100 Silber
     RECRUIT 1
     DEFAULT "GIVE 123 50 Silber; nicht vergessen"
     DEFAULT "LEARN Handel" ; löscht BUY und SELL
     DEFAULT "XXX" ; kein Befehl, wird nicht übernommen

Defaultbefehle der nächsten Woche

     UNIT abc
     GIVE 123 50 Silber; nicht vergessen
     LEARN Handel
     // nächste Woche lernen
     @GIVE xyz ALLES Balsam ; Transporter

Falls deine Defaultbefehle Anführungszeichen enthalten müssen, gibt es ein paar Wege, das derzeit zu erreichen:

     DEFAULT "CAST 'Erschaffe einen Ring der Unsichtbarkeit'"
     DEFAULT 'CAST "Erschaffe einen Ring der Unsichtbarkeit"'
     DEFAULT "NAME UNIT \"Bob's Builders\""
     DEFAULT "MAKE 1 'Wasser des Lebens'"

## Der Befehl MOVE

Der MOVE-Befehl spielt eine besondere Rolle: Er wird nicht in die Vorlage übernommen. Stattdessen werden die langen Befehle übernommen, die die Einheit in der letzten Woche in der Vorlage hatte, allerdings nur lange Befehle.

Defaultbefehle

     LEARN Reiten
     @GIVE 0 10 Silber
     // no comment

Eingeschickte Befehle

     MOVE o

Defaultbefehle der nächsten Woche

     LEARN Reiten

Was passiert, wenn sowohl MOVE als auch DEFAULT im Spiel ist?

Vorlage:

     WORK
     // jetzt nach westen

Eingeschickte Befehle

     DEFAULT "LEARN Ausdauer"
     // nun lernen
     MOVE w

Defaultbefehle der nächsten Woche

     LEARN Ausdauer
     // nun lernen

DEFAULT löscht also auch hier die *langen* Defaultbefehle (hier WORK) und setzt sie neu.

Es ist möglich, MOVE mit DEFAULT zu setzen. Vorlage:

     WORK
     @GIVE 0 1 Silber

Eingeschickte Befehle

     DEFAULT "MOVE o"
     WORK
     @GIVE 0 2 Silber

Defaultbefehle der nächsten Woche

     MOVE o
     @GIVE 0 2 Silber

Defaultbefehle der übernächsten Woche, wenn sonst keine Befehle für die Einheit eingeschickt werden:

     @GIVE 0 2 Silber

Auch hier würde die Einheit also dann keinen langen Befehl ausführen.

**Hinweis:** Es gibt eine Obergrenze an Befehlen, die für eine Einheit gespeichert werden. Diese liegt derzeit bei 128 Befehlen, was für die meisten Zwecke leicht ausreichen sollte.

Spielererfahrung: Solthar `DEFAULT DEFAULT`???

Ist es möglich, DEFAULT-Befehle zu schachteln, um für mehrere Wochen im Voraus Befehle zu machen? Nun, so etwas wie `DEFAULT "DEFAULT 'LEARN Ausdauer'"` funktioniert anscheinend, wie man es erwarten würde, aber die Spielleitung möchte lieber keine Garantien dafür abgeben. Bitte schicke keine Bugreports ein, falls so etwas nicht so klappt, wie du erwartet hast. Für solche Vorhaben sind Scriptsprachen wie [Vorlage], [ExtendedCommands] oder [FFTools] besser geeignet.

[Vorlage]: ./vorlage.md "Vorlage"
[ExtendedCommands]: ./commands-extended.md "ExtendedCommands"
[FFTools]: ./fftools.md "FFTools"

## See also

- [Befehle][Befehl]
- [Befehle einschicken]

<!-- From [https://wiki.eressea.de/index.php?title=DEFAULT&oldid=16788] -->

[Befehl]: ./commands.md "Orders"
[`OPTION`]: ./cmd-option.md "OPTION"
[langen Befehle]: ./commands.md#kurze-und-lange-befehle "Orders"
[//]: ./cmd-comment-slash.md "Kommentar (to be documented)"
[Lange Kommentare]: ./cmd-comment-slash.md "KOMMENTAR"
[Befehle einschicken]: ./commands-send.md "Befehle einschicken"
