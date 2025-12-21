---
# cSpell:locale fr, en
alias: cmd-teach-fr
---
# TEACH

**`TEACH`**[<sup>`L`</sup>]` `*`unit-id`*`[`*`unit-id`*`]...`

Um die Zeit herabzusetzen, die eine andere Einheit braucht, um ein Talent zu erlernen, kann man sie das Talent lehren. Dazu muss die lehrende Einheit in dem betreffenden Talent mindestens 2 Stufen besser als die lernende Einheit sein, Damit lernt die lernende Einheit doppelt so schnell, als wenn sie versucht, ihr Talent auf eigene Faust zu verbessern.

Mit diesem Befehl lehrt man allen aufgelisteten Einheiten das Talent, das diese gerade lernen. Die Schüler müssen also lernen während der Lehrer lehrt. Es kann mehr als eine Einheit aufgelistet werden. Eine Lehrer-Einheit kann allerdings pro Person und Runde nur 10 Schüler von seinem Wissen profitieren lassen. Es können auch mehrere Lehrer eine große Schüler-Einheit lehren.

Das zu lehrende Talent muss **nicht** angegeben werden - es wird automatisch das Talent gelehrt, welches die lernende Einheit lernt. Dies können auch verschiedene Talente sein, sofern der Lehrer diese Talente ausreichend besser als die Schüler beherrscht.

Will man Einheiten fremder Parteien lehren, muss man von dieser Partei den Befehl [[cmd-help]] GUARD erhalten haben oder die zu lehrende Einheit muss mit [[cmd-contact]] den Lehrer kontaktieren.

**Beispiel**:

     TEACH xxxx yyyy TEMP 2 zzzz

Durch den Befehl [LEARN AUTO] versucht der Server das Lernen und Lehren in einer Region innerhalb einer Partei zu automatisieren. Eine Mischung von `TEACH` und `LEARN AUTO` ist allerdings nicht möglich.

<!-- From [https://wiki.eressea.de/index.php?title=TEACH&oldid=16726] -->

[<sup>`L`</sup>]: ./commands.md#ordres-courts-et-longs
[HELP]: ./cmd-help.md
[CONTACT]: ./cmd-contact.md
[LEARN AUTO]: ./cmd-learn-auto.md
