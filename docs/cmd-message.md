---
# cSpell:locale en
alias: cmd-message
---
# MESSAGE

**`MESSAGE`**` UNIT `*`unit id`*`"`*`text`*`"`  
**`MESSAGE`**` PARTEI `*`faction-id`*`"`*`text`*`"`  
**`MESSAGE`**` SCHIFF `*`ship-id`*`"`*`text`*`"`  
**`MESSAGE`**` GEBÄUDE `*`building-id`*`"`*`text`*`"`  
**`MESSAGE`**`REGION "`*`text`*`"`

Hiermit können Botschaften an andere Einheiten, an andere Parteien, oder an alle Parteien in einer Region geschickt werden. Absender und Empfänger müssen in der selben Region sein. Schickt man eine Botschaft an eine Einheit, dann wird die Botschaft anonymisiert, wenn der Empfänger die absendende Einheit nicht sehen kann.

Mit `MESSAGE GEBÄUDE` und `MESSAGE SCHIFF` geht die Botschaft an alle Einheiten, die in dem Gebäude bzw. auf dem Schiff sind, allerdings nur eine Einheit pro Partei.

Wie alle anderen Texte auch, kann die Botschaft mit dem \\ (Backslash) umgebrochen werden.

       MESSAGE UNIT z14 "Zahlt sofort je 100 Silber an Jonan \
       den Zöllner (9i6), sonst werden unsere Wachen sich \
       um euch kümmern!"

<!-- From [https://wiki.eressea.de/index.php?title=MESSAGE&oldid=5960] -->
