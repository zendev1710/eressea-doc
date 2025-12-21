---
# cSpell:locale en
alias: orders
---
# Orders

## Conventions

The following conventions apply in these rules:

    ```text
    GIVE unit-id [number|ALL] [item]
    ```

- Keywords like GIVE, MAKE, NOT are in capital letters. This is not mandatory, but we recommend it-Placeholders are in lowercase letters. They should not be adopted literally, but must be replaced by concrete values, for example unit-id by the number of the desired unit. Sometimes we also write this as <unit-id>, in which case the < and > symbols are *not*to be included.
- Words in \[\] brackets are optional. So they can be omitted, but they change the meaning of the order. Alternatives are through | separated. The example above allows `GIVE 123 EVERYTHING` or `GIVE abc 4 sword`

## Syntax

Except for the password and the faction id, the server is case-insensitive.`lerNE armBRUSTschiessen`is completely legal (but not recommended as it is difficult for humans to read).

Items should always be in the*Singular*stand, so`GIVE xyz 100 Schwert`or`MAKE 15 Stein`. Items often appear in the majority in the report and are mostly understood in commands, but you should be aware that the server does not understand natural language, even if the commands look almost like that.

Many commands can be shortened, although you should not overdo it as this is prone to errors: VER matches FORGET, SELL and LEAVE and is therefore noted as an error; So here you should use at least four letters. In addition, overly cryptic abbreviations are not particularly readable when you look through your moves later... It's still safest if you don't abbreviate your orders, especially since there may be orders, items and skills that are intentionally not in the instructions but start out similar to well-known orders, items and skills.

Texts that contain spaces must be enclosed in quotation marks ("") or the spaces must be replaced by ~ (tilde). Furthermore, umlauts may be replaced by the appropriate paraphrase (Ä=AE, etc.):

    ```text
    NAME Ship "Big Blue Bird"
    GIVE unit 5 Spicy~Daring
    COMBAT REAR
    ```

Es ist möglich, einfache Anführungszeichen (') zu benutzen und zu kombinieren. Was dabei genau herauskommt, solltest du lieber ausprobieren, weil sich das genaue Verhalten immer mal verändern kann.

    ```text
    MESSAGE REGION 'Sprich "Freund" und tritt ein'
    NAME BURG xyz "Helm's Deep"
    DEFAULT 'MAKE 1 "Wasser des Lebens"'
    ```

Also called masking (escaping) by the character\are possible, but not necessarily recommended:

    ```text
    MESSAGE REGION "Sprich \"Freund\" und tritt ein"
    NAME BURG xyz 'Helm\'s Deep'
    DEFAULT 'MAKE 1 Wasser\~des\~Lebens'
    ```

By the way, it is not necessary to limit yourself to the Latin alphabet. The full Unicode character set is possible in names and descriptions:

    ```text
    NAME UNIT "Σωκράτης"
    MESSAGE REGION "🨀 شاه مات"
    ```

Of course, you should make sure that you are understood by others.

<!-- TODO: rework ZUGVORLAGE notion-->
## Move template

The easiest way is to use the move template at the end of the evaluation.
All units are listed there so that you don't forget anyone.
If you don't send in any orders, the orders in the move template will still be executed automatically.
Even if you only send orders for some of your units, the orders in the move template will be executed for the remaining units.
If your evaluation does not contain a move template (with the extension `.txt`), you can reactivate it with the command [[cmd-option|`OPTION MOVE TEMPLATE`]].

## Short and long orders

There are short and long orders in Eressea.

The long orders are:

[[cmd-work]], [[cmd-attack]], [[cmd-steal]], [[cmd-ride]], [[cmd-follow]], [[cmd-research]], [[cmd-buy]], [[cmd-teach]], [[cmd-learn]], [[cmd-make]] (Ausnahme: MAKE TEMP), [[cmd-move]], [[cmd-plant]], [[cmd-piracy]], [[cmd-route]], [[cmd-spy]], [[cmd-tax]], [[cmd-entertain]], [[cmd-sell]], [[cmd-cast]], [[cmd-destroy]], [[cmd-grow]].

Alle anderen Befehle sind kurze Befehle ([Kurzbeschreibung] aller Befehle). Du kannst beliebig viele kurze Befehle pro Einheit eingeben. Eine Einheit kann in der Regel nur einen langen Befehl haben. Es gibt ein paar Ausnahmen, die so genannten pseudolangen Befehle (`ATTACK, FOLLOW, BUY, SELL, CAST`), von denen unter Umständen mehrere gegeben werden können. Näheres in der Beschreibung der einzelnen Befehle.

Wird einer Einheit ein langer Befehl gegeben, wird sie diesen als Default-Befehl übernehmen und damit den vorherigen Default-Befehl ersetzen. Der Default-Befehl steht in der [Zugvorlage][3 Die Zugvorlage] immer als Vorschlag für einen langen Befehl. Du brauchst also einem Pferdedresseur nur einmal den Befehl MAKE pferd zu geben und dieser Befehl erscheint solange in der Zugvorlage, bis sie einen anderen langen Befehl erhält (z.B. LEARN Pferdedressur). Sinnvollerweise werden nicht alle langen Befehle als Default-Befehle übernommen. Das betrifft z.B. MOVE, ATTACK und FOLLOW. Weiteres zu Default-Befehlen auf der Seite zum Befehl [[cmd-default]].

Eine Einheit, die eine Runde arbeitete, in der kommenden Runde nach Norden zog und dann keinen Befehl mehr bekam, wird sich in der darauf folgenden Runde niederlassen und wieder arbeiten (es sei denn natürlich, sie erhält in dieser Runde einen anderen langen Befehl).

Bitte beachte, dass pro Einheit nur ein Befehl pro Einheit im normalen Report (NR) angezeigt wird. Die restlichen Default-Befehle werden in der Zugvorlage und im Computerreport angezeigt.

## Execute short commands permanently

Sometimes it makes sense to execute a short command every round, such as GIVE, because the miners should constantly deliver the mined iron to the forge.

To do this, you can put an @ (at sign, spider monkey) before each short command. Such orders are simply copied into the move template for the next round and -unless you delete them again -executed again.

 **An example** :

    ```text
    UNIT berg;         Miners [5,400$,U500]
        MAKE iron
        @GIVE schm ALLES Eisen;   immer an die Schmiede liefern
    UNIT schm;         Wrought [3,1343$,U250]
        MAKE Swords
    ```

 **Note:** There is a cap on the number of commands stored for a unit. This is currently 128 commands, which should easily be enough for most purposes.

## Suppress errors

It may happen that you consciously accept errors when executing a command. By prefixing it with an exclamation mark (!) you can suppress the server messages concerning this command.

**An example**:

    ```text
    UNIT berg;         Miners
        MAKE iron
        !@GIVE tran ALL iron;   The van isn't always there; we don't want an error message about this
    UNIT tran;        Transporter
        ROUTE w PAUSE o PAUSE;   We commute between two regions
        !@GIVE schm ALL iron;   In the west we hand the iron over to the blacksmiths

Das birgt natürlich das Risiko, dass du Fehler übersiehst, mit denen du nicht gerechnet hast.

## See also

- [[orders-sequence]]
- [[orders-list]]
- [[cmd-default]]

Continue reading: [[orders-sequence]].

<!-- From [https://wiki.eressea.de/index.php?title=Befehl&oldid=16787] -->
