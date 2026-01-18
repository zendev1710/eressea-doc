---
# cSpell:locale fr
alias: contribuer-a-eressea
---
# Contribuer à Eressea

<!-- TODO: rewrite because this page describes how to help editing the mediawiki -->

## Inscription

Früher konnte einfach jeder hier Änderungen vornehmen. Leider hatten wir ziemlich Probleme mit Spammern. Deshalb muss man sich jetzt anmelden und die Anmeldeseite ist nicht immer aktiv. Schreibe einfach Enno eine Mail und er wird dich freischalten.

## Règles

Die Regelseiten sollten mit größter Sorgfalt bearbeitet werden. Gerade weil der Server Änderungen unterliegt, gehören hier nur offizielle Regeln hin. In der Spielergemeinde kursieren einige Gerüchte über die Welt von Eressea, die zum Teil schlicht falsch, ungenau oder veraltet sind. Informationen, die hier in den Regeln auftauchen, sollten mit der Spielleitung abgestimmt sein oder direkt vom Server stammen. Falls Ihr dennoch Anmerkungen machen wollt, die aus Eurer Erfahrung stammen, legt dafür bitte eine eigene Seite an und / oder kennzeichnet sie klar als solche, und zwar so:

Spielererfahrung: Nixus MinimusUntote haben furchtbaren Mundgeruch!

## Le Troisième Âge

Im dritten Zeitalter gibt es eine ganze Menge Änderungen. Diese sollen nach und nach auch hier zu den Regeln hinzugefügt werden, wobei natürlich die Regeln für das zweite Zeitalter nicht gelöscht werden. Einstweilen sind die Änderungen aber nicht vollständig. Eine Übersicht über alle Änderung gibt es hier: [Das dritte Zeitalter]

Für das Kennzeichnen von Änderungen auf den eigentlichen Regelseiten gibt es zwei Templates

<!-- exclude E3 from documentation -->
<!--
|---------|------------------------------------------------------------|
| **E3A** | Für kurze Hinweise benutze {{E3Akurz\|Für kurze Hinweise}} |

**[E3A — Das Dritte Zeitalter][Das dritte Zeitalter]**

Für ausführlichere Hinweise benutze {{E3A|Für ausführlichere Hinweise mit langen oder mehreren Sätzen.}}.
-->

## Langues

Wir sind dabei, das englischsprachige Wiki wieder aufzubauen und auch gleich noch eins auf Französisch!

## Conventions

Folgende Konventionen sollten zumindest bei Regelseiten eingehalten werden:

### Ordres

Artikel, die Befehle beschreiben, sollten zunächst die Syntax auflisten:

**`MAKE`**`[`*`stufen`*`] SCHIFF [`*`ship-id`*`]`  

Dabei sollte der Befehl selbst fett und in Großbuchstaben, Schlüsselwörter in Großbuchstaben, variable Teile kursiv und optionale Teile in eckigen Klammern stehen. Alles sollte in &lt;tt&gt;-Tags eingeschlossen werden. Schlüsselwörter sollten auch im Fließtext in &lt;tt&gt;-Tags eingeschlossen werden.

### Exemples

Beispielbefehle und Reportzitate sollten als "präformatierter" Text gesetzt werden:

     MAKE TEMP 123
       RECRUIT 1
     END

Sonstige Beispiele sollten eher nicht als eigener Abschnitt gesetzt werden, sondern als eigener Absatz, der mit dem fettgedrucktem Wort "Beispiel" beginnt.

**Exemple**:

    '''Beispiel''':
       BESCHREIBEN UNIT "Auf dem Schild steht 'Betreten verboten!'"

<!-- From [https://wiki.eressea.de/index.php?title=Eressea:Mitmachen&oldid=16081] -->

[Das dritte Zeitalter]: ./the-third-age.md
