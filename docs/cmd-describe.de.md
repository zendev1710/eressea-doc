---
# cSpell:locale de
alias: bef-beschreibe
---
# BESCHREIBE

**`BESCHREIBE EINHEIT`**`"`*`text`*`"`  
**`BESCHREIBE GEBÄUDE`**`"`*`text`*`"`  
**`BESCHREIBE SCHIFF`**`"`*`text`*`"`  
**`BESCHREIBE REGION`**`"`*`text`*`"`  
**`BESCHREIBE PRIVAT`**`"`*`text`*`"`

Die Beschreibung für das aufgeführte Objekt wird geändert. Diese Beschreibung wird jeweils nach dem Objekt aufgelistet und kann bis zu 8191 Zeichen lang sein. Der Computer vergibt bei der Erschaffung von Objekten keine Beschreibungen.

Für Schiffe, Gebäude und Regionen gelten dieselben Einschränkungen wie beim Benennen von Objekten: Gebäude und Schiffe können nur beschrieben werden, wenn die Einheit auch das Kommando über das Gebäude oder das Schiff hat (sie muss also die erste Einheit unter dem Gebäude oder dem Schiff auf der Auswertung sein). Eine Region kann nur vom Burgherr der mächtigsten Burg einer Region beschrieben werden.

Mit `BESCHREIBE PRIVAT` kann man der befehlsgebenden Einheit eine "private" Beschreibung geben, die nur der Besitzer der Einheit sieht.

Lange Beschreibungen müssen mit dem "Befehlsverlängerer" \\ (Backslash) umgebrochen werden. Neue Zeilen nach dem \\ dürfen nicht mit Leerzeichen anfangen.

    BESCHREIBE EINHEIT "Blattschneideameisen benötigen keinen \
    Schlaf und ihre Arbeiter sind immer auf maximale Effizienz fixier\
    t. Alles was sie tun und unter ihrer schwarzen Hülle denken bezie\
    hen sie auf das Kollektiv des Staates."

Es ist derzeit nicht möglich, Absätze und Umbrüche an sich in Beschreibungen einzufügen.

<!-- From [https://wiki.eressea.de/index.php?title=BESCHREIBE&oldid=7442] -->
