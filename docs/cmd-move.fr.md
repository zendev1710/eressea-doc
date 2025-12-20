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

## Voir aussi

- [Reisen]
- [[cmd-route]]
- [[cmd-follow]]
- [[cmd-default]][Defaultbefehle]

<!-- From [https://wiki.eressea.de/index.php?title=MOVE&oldid=16729] -->

[<sup>`L`</sup>]: ./commands.md#ordres-courts-et-longs
[Defaultbefehle]: ./cmd-default.md
[Zugvorlage]: ./commands.md
[Reisen]: ./travel.md
[ROUTE]: ./cmd-route.md
[FOLLOW]: ./cmd-follow.md
