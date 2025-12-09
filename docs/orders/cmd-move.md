# MOVE

**`MOVE`**[<sup>`L`</sup>]` `*`himmelsrichtung`*`[`*`himmelsrichtung`*`]...`

Mit dem Befehl `MOVE` bewegt sich die Einheit durch die Welt von Eressea. Die Himmelsrichtungen sind in Eressea Nordosten, Nordwesten, Osten, Westen, Südosten und Südwesten. Die Koordinaten werden nicht verwendet.

| Richtung   | Abkürzungen |
|------------|-------------|
| Nordosten  | NO, Nordo   |
| Osten      | O           |
| Südosten   | SO, Südo    |
| Nordwesten | NW, Nordw   |
| Westen     | W           |
| Südwesten  | SW, Südw    |

Der Befehl hat ein besonderes Verhalten, was [Defaultbefehle] betrifft, also Befehle, die die Einheit in der Folgewoche in der [Zugvorlage] bekommt: Der MOVE-Befehl wird nicht in die Vorlage übernommen. Stattdessen werden die langen Befehle übernommen, die die Einheit in der letzten Woche in der Vorlage hatte.

Vorlage:

     LEARN Reiten
     @GIVE x 100 Silber

Eingeschickte Befehle

     MOVE w

Vorlage nächste Woche:

     LEARN Reiten

## See also

- [Reisen]
- [ROUTE]
- [FOLLOW]
- [DEFAULT][Defaultbefehle]

<!-- From [https://wiki.eressea.de/index.php?title=MOVE&oldid=16729] -->

[<sup>`L`</sup>]: ./commands.md#short-and-long-orders "Orders"
[Defaultbefehle]: ./cmd-default.md "DEFAULT"
[Zugvorlage]: ./commands.md "Orders"
[Reisen]: ./travel.md "Reisen"
[ROUTE]: ./cmd-route.md "ROUTE"
[FOLLOW]: ./cmd-follow.md "FOLLOW"
