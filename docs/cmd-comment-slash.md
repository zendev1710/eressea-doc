---
alias:
    name: comment-slashes
    text: COMMENT //
---
# COMMENT

**`//`**` `*`Kommentar`*

Im Gegensatz zu einem Kommentar hinter einem [;] (Semikolon) wird dieser Kommentar mit in die Vorlage für den Zug der nächsten Runde mit aufgenommen.

       UNIT 123;     Hundertdreiundzwanzig [20,450$]
            // Unterhalt Magierturm
          @GIVE 234 1000 SILBER
            // Ab und an Stangenwaffen lernen
          TAX Steuern ein

Das `//` muß wie ein Befehl behandelt werden, man darf also nicht

          @GIVE 345 100 SILBER // wegen Sägewerk

machen. Außerdem muß ein Leerzeichen hinter den `//` sein.

<!-- From  [https://wiki.eressea.de/index.php?title=KOMMENTAR&oldid=3993] -->

[;]: ./cmd-comment.md "comment with comment"
