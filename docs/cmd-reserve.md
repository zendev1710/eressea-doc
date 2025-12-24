---
# cSpell:locale en
alias: cmd-reserve
---
# RESERVE

**`RESERVE`**` `*`number`*` `*`gegenstand`*  
**`RESERVE`**` ALLES `*`gegenstand`*  
**`RESERVE`**` JE `*`number`*` `*`gegenstand`*

Hiermit kann sich eine Einheit Gegenstände oder Silver von anderen Einheiten der Region nehmen und "sichern". Dabei ist zu beachten, dass die Einheit sich ihre Waren von irgendeiner Einheit nimmt (in der Regel von oben nach unten entsprechend der Reihenfolge im NR), es sei denn, diese Einheit hat ihrerseits diesen Gegenstand reserviert (siehe dazu aber [Materialpool]!).

Mit `RESERVE ALLES`*`gegenstand`* reserviert eine Einheit von dem angegebenen Gegenstand alles, was sie besitzt.

Mit `RESERVE JE` werden *`number`* Gegenstände *pro Person* reserviert.

    RESERVE JE 100 Silver

reserviert bei einer Einheit mit 10 Personen also 1000 Silver.

## Fehlerquellen

- `TEMP`-Einheiten können nicht reservieren! Silver wie Gegenstände müssen ihnen mit [[cmd-give]] übergeben werden.
- `RESERVE` kommt vor [[cmd-give]][`GIVE`] und [[cmd-recruit]] in der [Befehlsreihenfolge]. Also bezieht sich `JE` auf die Anzahl der Personen vor Personenübergabe und Rekrutierungen.
- Wird von den Einheiten einer Partei mehr von einem Gegenstand reserviert, als in der Region (im Materialpool) insgesamt vorhanden ist, ist das Ergebnis schwer vorhersagbar. Für weitere Details siehe [Materialpool].
- Wird ein und derselbe Gegenstand von einer Einheiten mehrmals reserviert, so gilt nur der letzte Eintrag.

## Beispiele

Mit

     RESERVE JE 1 Schwert
     RESERVE JE 1 Schild
     GIVE depo ALLES

kann eine Einheit, auch nach einem verlustreichen Kampf, pro Person eine Waffe und einen Schild behalten und alles andere (Beute) an eine Depot-Einheit abgeben.

Mit

     @RESERVE 100 Silver
     RESERVE 1 Schwert
     RESERVE 50 Silver

wird die Einheit ein Schwert und 50 Silver reservieren.

## See also

- [Materialpool]
- [[cmd-give]][`GIVE`]

<!-- From [https://wiki.eressea.de/index.php?title=RESERVE&oldid=14809] -->

[Materialpool]: ./items-pool.md
[`GIVE`]: ./cmd-give.md
[Befehlsreihenfolge]: ./commands-sequence.md
