---
# cSpell:locale de
alias: reisen
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Reisen

In Eressea gibt es mehrere Möglichkeiten, sich fortzubewegen: zu Fuß gehen, auf Pferden reiten oder auf Schiffen über Ozeane segeln. Einige wenige können sogar schwimmen oder fliegen. Für alle Varianten wird der Befehl [NACH][bef-nach] oder [[bef-route]] benutzt.

## Reisen: Zu Land und zur See

In jeder Runde kann man zu Land eine Region weit gehen. Hat eine Einheit genug Pferde und hat sie das Talent Reiten, so kommt sie eine Region weiter als zu Fuß. Sind die aneinanderliegenden Regionen durch Straßen verbunden, können sich die Einheiten zu Fuß bis zu 2 Regionen und zu Pferd bis zu 3 Regionen weit bewegen.

Bewegung ist nur in die sechs Richtungen Nordost, Nordwest, Osten, Westen, Südost und Südwest möglich. Eine direkte Bewegung nach Norden oder Süden geht nicht.

Mit dem Befehl [[bef-transportiere]]` `*`fahrgast-einheit`* können Einheiten andere Einheiten mitnehmen. Die zu transportierende Einheit muss dazu den Befehl [`FAHRE transporter-einheit`][bef-fahre] geben. Durch diesen Befehl ist es z.B. möglich, Einheiten, die nicht reiten können, auf Pferden oder Wagen mitzunehmen. Die transportierende Einheit muss dazu natürlich Tragekapazität für die Passagiere und deren Besitztümer haben. Mit [[bef-folge]]` EINHEIT `*`verfolgte-einheit`* oder `FOLGE SCHIFF`*`verfolgtes-schiff`* ist es hingegen so, als hätte die Einheit selber einen NACH-Befehl gegeben, wenn die verfolgte Einheit oder das Schiff einen Bewegungsbefehl haben. Sie muss also ihr Gewicht selber tragen.

Reisende Einheiten können von bewachenden Einheiten in einer Region gestoppt werden (siehe [[bef-bewache]]).

Wenn eine Einheit oder ein Schiff zu schwer beladen ist, können sie sich nicht fortbewegen. Dazu wird das Gesamtgewicht der zu transportierenden Einheit samt mitgeführten Waren und Silber mit der Tragekapazität verglichen (siehe [diese Tabelle][waren] für die Gewichte).

TODO: Katapulte

Gewichte und Kapazitäten

|                                | Gewicht | Kapazität |
|--------------------------------|--------:|----------:|
| Trolle                         |      20 |      10,8 |
| Goblins                        |       6 |       4,4 |
| alle anderen Spielerrassen     |      10 |       5,4 |
| Pferd                          |      50 |        20 |
| Wagen                          |      40 |       100 |
| [Boot][boot]                   |      -- |        50 |
| [Langboot][langboot]           |      -- |       500 |
| [Drachenschiff][drachenschiff] |      -- |      1000 |
| [Karavelle][karavelle]         |      -- |      3000 |
| [Trireme][trireme-de-id]       |      -- |      2000 |
| [Galeone][galeone]             |      -- |     20000 |

## Straßen

Durch den Bau von [Straßen][strassen-id] kann die Reisegeschwindigkeit um eine Region erhöht werden. Dabei müssen alle Regionen, durch die man reist, ein komplettes Straßennetz aufweisen. Will man also zu Fuß in einer Woche zwei Regionen weit nach Osten reisen, benötigt die Startregion eine vollständige Straße nach Osten, die mittlere Region je eine vollständige Straßen nach Osten und Westen und die Zielregion eine vollständige Straße nach Westen.

## Pferd und Wagen

Die **Bewegungsgeschwindigkeit** zu Fuß beträgt ohne [Straße][strassen-id] eine Region pro Runde; mit Straße sind es zwei. Zu Pferd kann man sich ohne Straße zwei Regionen weit bewegen, mit Straßen drei. Pro 2 Pferde wird ein Talentpunkt benötigt um zu reiten. Die Einheit reitet automatisch, wenn für alle Pferde genug Reittalent vorhanden ist und die Einheit nicht überladen ist. Ist die Einheit zu schwer beladen um zu reiten, aber nicht zu schwer beladen um sich zu Fuß zu bewegen, bleibt die Einheit nicht ganz stehen, sondern bewegt sich eine Region weit (ohne Straße).

**Pferde** haben eine Kapazität von 20GE.

**Wagen** haben eine Kapazität von 100GE. Dazu müssen sie von 2 Pferden pro Wagen gezogen werden. Wagen können aber auch als Fracht transportiert werden, zum Beispiel auf einem Schiff oder wenn die Einheit zu wenige Pferde dabei hat; sie haben ein Gewicht von 40GE.

Je 4 Trolle können auch ohne Pferde einen Wagen ziehen, allerdings nur eine Region weit. Nur Trolle können Wagen ohne Pferde benutzen.

**Zu Fuß** kann jede Person (auch ohne das Talent Reiten) ein Pferd eine Region weit führen. Zusätzlich kann jede Person pro Talentstufe Reiten vier Pferde führen (eine Person mit Reiten 1 also insgesamt 5 Pferde). Führen Trolle sowohl Pferde als auch Wagen mit sich, so ziehen bevorzugt die Pferde die Wagen.

**Zu Pferd** kann jede Person pro Talentstufe Reiten zwei Pferde mitnehmen. Dabei ist zu beachten, dass die Reiter selbst von der Kapazität des Gespanns abgezogen werden müssen.

Sind zu viele Pferde vorhanden, kann sich die Einheit nicht mehr bewegen.

Sind in einer Einheit mehrere Pferde und Wagen, so wird deren Tragekapazität einfach addiert. So passen z.B. auf drei Wagen sieben Steine, obwohl auf einen Wagen nur ein Stein (abgerundet) passt.

**Beispiele** (wir nehmen hierfür an, dass es keine Straßen gibt)

- Eine Einheit mit 4 Personen und Reiten 1 kann max. 20 Pferde (4 Pferde ohnehin, dazu 4 \* 4 Pferde durch Reiten 1) zu Fuß mitführen. Wenn sie nicht mehr als 8 Pferde dabei hat und nicht zu schwer, kann sie sich zwei Felder weit bewegen.
- Wenn also dieselbe Einheit nur 8 Pferde und 2 Wagen mitnimmt, hat sie zu Pferd eine Kapazität von 320GE (2 \* 100GE für die Wagen + 8 \* 20GE für die Pferde − 4 \* 10GE für die Reiter). Ausnahme hierzu sind Rassen mit anderem Gewicht, wo natürlich das tatsächliche Gewicht des Reiters abgezogen wird.
- Eine Einheit mit 5 Zwergen ohne Talent Reiten kann 5 Pferde eine Region weit führen und dabei 127GE transportieren (5,4GE pro Zwerg und 20GE pro Pferd).
- Wenn die gleiche Einheit zusätzlich noch 3 Wagen hat, kann sie 287GE an anderen Gütern transportieren (5,4GE pro Zwerg, 20GE pro Pferd und 2 \* 100GE für die gezogenen Wagen minus 40GE für den Wagen der transportiert werden muss, weil 5 Pferde nur für 2 Wagen reichen).
- Eine Einheit mit 4 Trollen ohne Talent Reiten und ohne Pferde kann einen Wagen eine Region (mit Straßen zwei Regionen) weit ziehen und dabei 143,2GE transportieren (10,8GE pro Troll und 100GE auf dem Wagen).
- Eine Einheit mit 4 Trollen ohne Talent Reiten kann 4 Pferde und 3 Wagen (zwei hinter den Pferden und einer hinter den 4 Trollen) eine Region weit führen und dabei 423,2GE transportieren (10,8GE pro Troll, 300GE auf dem Wagen und je 20GE auf den 4 Pferden).
- Eine Einheit mit 4 Trollen und Reiten 1 mit 4 Pferden und zwei Wagen kann mit 323.2GE eine Region weit gehen (10,8GE pro Troll, 20GE pro Pferd und 100GE pro Wagen) oder mit 200GE zwei Regionen weit reiten (20GE pro Pferd, 100GE pro Wagen minus 80 GE für die 4 Trolle).
- Eine Einheit mit Reiten 1, einem Wagen und zwei Pferden kann 130 Schwerter zwei Regionen weit transportieren (der Fuhrmann wiegt 10 und muss von der Kapazität abgezogen werden, wenn er auf dem Wagen sitzt). Eine Einheit mit Reiten 1 und 4 Personen könnte 20 Pferde und 10 Wagen eine Region weit und 8 Pferde und vier Wagen zwei Regionen weit bewegen.
- Soll ein leerer Wagen mit zwei Pferden auf einem Schiff transportiert werden, muss das Schiff dafür eine Kapazität von 140GE (40GE für den Wagen und 2 \* 50GE für die Pferde) frei haben.

## Siehe auch

- [Schiffe][schiff]
- [Straße][strassen-id]

Weiterlesen: [Schiffsreise][schiffsreise].

<!-- From [https://wiki.eressea.de/index.php?title=Reisen&oldid=16133] -->

[bef-bewache]: [[bef-bewache]]
[bef-fahre]: [[bef-fahre]]
[bef-folge]: [[bef-folge]]
[bef-nach]: [[bef-nach]]
[bef-route]: [[bef-route]]
[bef-transportiere]: [[bef-transportiere]]
