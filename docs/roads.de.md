---
# cSpell:locale de
alias: strassen
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD041 MD042 MD052 -->

<!-- NOTE: Straßen slugifyied/stringifyied result is straen, not human readable, so a specific id is used -->
[](){ #strassen-id }

# Straßen

**Straßen** erhöhen die Reisegeschwindigkeit über Land. Dazu müssen von der Start- bis zur Zielregion inklusive Straßen existieren. Diese Straßen erlauben ein leichtes Fortkommen, da sie bei Regen nicht versumpfen, nicht vom Wald überwachsen werden und Flüsse und Schluchten von Brücken überspannt werden.

In jeder Region kann man in die sechs Himmelsrichtungen eine Straße errichten. Damit eine Straße komplett ist, muss in der Region der entsprechenden Richtung in der Gegenrichtung auch eine Straße sein. Um Straßen zu bauen, benötigt man ein Mindest-Bautalent von 1, pro Talentstufe Straßenbau kann man einen Stein verbauen.

Die folgende Tabelle gibt an, wie viele Steine pro Richtung benötigt werden. Außerdem sind einige Regionen so ungastlich, dass zuvor ein [Gebäude][andere-gebaude-id] errichtet werden muss. Dieses muss zum Zeitpunkt des Baus funktionieren, d.h., es muss fertig sein und der Unterhalt muss gezahlt werden. Die fertige Straße funktioniert, auch ohne dass der Unterhalt gezahlt wird.

Straßenbau

| Gelände   | Steine | Gebäude                      |
|-----------|--------|------------------------------|
| Ebene     | 50     | --                           |
| Wald      | 50     | --                           |
| Hochland  | 100    | --                           |
| Gebirge   | 250    | --                           |
| Vulkan    | 250    |                              |
| Sumpf     | 75     | [Damm][damm]                 |
| Wüste     | 100    | [Karawanserei][karawanserei] |
| Gletscher | 250    | [Tunnel][tunnel-de-id]       |

**Beispiel:** Um von der Ebene bei (0,0) über den Sumpf bei (1,0) bis zum Berg in (1,1) eine Straße zu bauen, brauchst du

- 50 Steine für `MACHE Straße O` in (0,0)
- einen Damm in (1,0), der während des Baus funktioniert, also pro Runde 1000 Silber und 3 Holz kostet
- 75 Steine für `MACHE Straße W` in (1,0)
- 75 Steine für `MACHE Straße NO` in (1,0)
- 250 Steine für `MACHE Straße SW` in (1,1)

Danach kann eine Einheit mit `NACH O NO` zu Fuß in einer Runde von (0,0) nach (1,1) reisen.

Weiterlesen: [Schiff][schiff].

<!-- From [https://wiki.eressea.de/index.php?title=Straße&oldid=15933] -->
