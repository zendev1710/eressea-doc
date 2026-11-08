---
# cSpell:locale de
alias: bef-reserviere
---

# `RESERVIERE`

**`RESERVIERE`**` `*`anzahl`*` `*`gegenstand`*  
**`RESERVIERE`**` ALLES `*`gegenstand`*  
**`RESERVIERE`**` JE `*`anzahl`*` `*`gegenstand`*  

Hiermit kann sich eine Einheit Gegenstände oder Silber von anderen Einheiten der Region nehmen und "sichern". Dabei ist zu beachten, dass die Einheit sich ihre Waren von irgendeiner Einheit nimmt (in der Regel von oben nach unten entsprechend der Reihenfolge im NR), es sei denn, diese Einheit hat ihrerseits diesen Gegenstand reserviert (siehe dazu aber [Materialpool][materialpool]!).

Mit `RESERVIERE ALLES`*`gegenstand`* reserviert eine Einheit von dem angegebenen Gegenstand alles, was sie besitzt.

Mit `RESERVIERE JE` werden *`anzahl`* Gegenstände *pro Person* reserviert.

```text
RESERVIERE JE 100 Silber
```

reserviert bei einer Einheit mit 10 Personen also 1000 Silber.

## Fehlerquellen

- `TEMP`-Einheiten können nicht reservieren! Silber wie Gegenstände müssen ihnen mit [GIB][bef-gib] übergeben werden.
- `RESERVIERE` kommt vor [GIB][bef-gib] und [`REKRUTIERE`][bef-rekrutiere] in der [Befehlsreihenfolge][befehlsreihenfolge]. Also bezieht sich `JE` auf die Anzahl der Personen vor Personenübergabe und Rekrutierungen.
- Wird von den Einheiten einer Partei mehr von einem Gegenstand reserviert, als in der Region (im Materialpool) insgesamt vorhanden ist, ist das Ergebnis schwer vorhersagbar. Für weitere Details siehe [Materialpool][materialpool].
- Wird ein und derselbe Gegenstand von einer Einheiten mehrmals reserviert, so gilt nur der letzte Eintrag.

## Beispiele

Mit

```text
RESERVIERE JE 1 Schwert
RESERVIERE JE 1 Schild
GIB depo ALLES
```

kann eine Einheit, auch nach einem verlustreichen Kampf, pro Person eine Waffe und einen Schild behalten und alles andere (Beute) an eine Depot-Einheit abgeben.

Mit

```text
@RESERVIERE 100 Silber
RESERVIERE 1 Schwert
RESERVIERE 50 Silber
```

wird die Einheit ein Schwert und 50 Silber reservieren.

## Siehe auch

- [Materialpool][materialpool]
- [GIB][bef-gib]

<!-- From [https://wiki.eressea.de/index.php?title=RESERVIERE&oldid=14809] -->

[bef-gib]: [[bef-gib]]
[bef-rekrutiere]: [[bef-rekrutiere]]
