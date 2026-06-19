---
# cSpell:locale de
alias: parteien
---

# Parteien

Spielende führen sogenannte **Parteien** auf Eressea. Eine Partei besteht zunächst aus einer, später dann mitunter aus sehr vielen Einheiten. Diese Einheiten bestehen aus einer, einigen wenigen oder gar Tausenden von Personen der [Rasse][rassen] der Partei. Jede Einheit kann beliebig viele Gegenstände und Silber besitzen, und ebenso alle [Talente][talente] von Eressea erlernen. Den Einheiten kannst du jede Runde [Befehle][befehl] geben, welche sie so gut wie möglich ausführen.

Du scheidest aus dem Spiel aus, wenn deine Partei keine Mitglieder mehr hat - wenn also alle Einheiten zerstört oder aufgelöst worden sind, oder wenn über fünf Runden nacheinander keine Befehle eingetroffen sind (5 NMR).

## Einheiten

Das Spiel beginnt die Partei mit einer **Einheit**, bestehend aus einer Person mit 2500 Silber, 10 Holz, 4 Steinen und einem [rassenspezifischen Startgeschenk][start-der-6-welt]. Ein Tip: Wenn du nicht weißt, was du da hast, probiere mal [`ZEIGE "`*`Gegenstand`*`"`]. Diese erste Person ist in keiner Weise speziell; es ist einfach die erste Person, die zur neuen Partei gehört. Du kannst nun weitere Personen [rekrutieren][rekrutieren], später dann [Gegenstände produzieren][waren], [Gebäude][gebaude-id] und [Schiffe][schiff] bauen, [Pferde][pferd-und-wagen] zähmen, [Waffen][kriegstabellen] schmieden und so weiter.

Neue Einheiten werden gemacht, indem du mit einer bestehenden Einheit eine neue generierst ([`MACHE TEMP`]). Eine neue Einheit enthält noch keine Leute; diese müssen entweder von einer bestehenden in die neue Einheit [transferiert][bef-gib] oder frisch rekrutiert werden, wozu die Einheit dann das notwendige [Geld][ausgaben] bekommen muss. Einheiten, die von Einheiten auf Schiffen oder in Gebäuden gemacht werden, starten dort, also auf dem Schiff bzw. in dem Gebäude.

Eine Partei kann nicht mehr als eine bestimmte Zahl von Einheiten, bekannt als das **Einheitenlimit**, haben. Das liegt derzeit bei 2500 Einheiten und wird auch im Report angezeigt. Das Einheitenmlimit verhindert, dass neue Einheiten erzeugt werden. Es ist dafür unerheblich, ob vielleicht später im Zug Einheiten aufgelöst werden. Unter gewissen Umständen ist es möglich, dass eine Partei mehr Einheiten hat als das Einheitenlimit. Die überzähligen Einheiten werden nicht gelöscht; es können dann nur so lange keine neuen Einheiten mehr erzeugt werden, bis die Einheitenzahl wieder unter das Limit sinkt.

Hier ein Beispiel für Einheiten:

      * Konrad Rabenhelm (tb2), 1 Mensch, vorne, bewacht die Region, Talente:
        Hiebwaffen 1, Steuereintreiben 2, hat: Schwert, 20 Silber, "TREIBEN";
        Konrad Rabenhelm ist ein typischer Ritter seines Ordens. Der Orden der
        Gerechtigkeit ist bekannt für seine düsteren und zurückhaltenden 
        Mitglieder. Sie scheinen alle an einem finsteren Erlebnis zu nagen.
       
      - Botschafter des Clans (2ow), anonym, 1 Zwerg, hat: Pferd,
        Silberbeutel; Der Botschafter ist auf der Suche nach befreundeten Völkern
        und solchen, die es werden wollen.
       
      + Kieselnasen (kies), Gesteinsfreunde (135), 4 Trolle, hat: 1 Wagen, 30
        Juwelen.

Eigene Einheiten sind mit einem '\*' markiert, Einheiten anderer Parteien mit einem '-' oder einem '+', wenn man der Partei [hilft][allianz].

Jede Einheit besitzt eine eindeutige Nummer, die vom Computer vergeben wird und die bei allen Befehlen verwendet wird, im ersten Fall hier die Nummer tb2.  
Der Begriff "Nummer" mutet hier seltsam an, denn in Eressea werden die Einheiten mit "base36"-Zahlen versehen; neben den Ziffern 0-9 sind also die Buchstaben a-z als "Ziffern" gültig.  
Jede Einheit hat zudem einen Namen ("Konrad Rabenhelm") und vielleicht eine Beschreibung (nach dem Semikolon).  
Zudem werden Besitz und, falls die Information verfügbar ist, Talente angezeigt.

Diese erste Einheit des Beispiels ist die Einheit der Partei, die diesen Report bekam.  
Sie besteht aus einem Menschen der eigenen Partei (wird nicht angezeigt), hat 20 Silber und kann mit Hiebwaffen kämpfen: in diesem Talent hat die Einheit die Stufe 1.  
Das Talent [Steuereintreiben][skill-steuereintreiben-id] beherrscht sie auf Stufe 2 (näheres im Kapitel [zu den Talenten][talente]).  
Wie man sieht, hat Konrad Rabenhelm ein Schwert. "TREIBE" ist der so genannte [Defaultbefehl]. Bekommt diese Einheit keine neuen Befehle für die nächste Runde, so wird sie weiterhin Steuern eintreiben.  
Im NR wird immer nur ein Defaultbefehl angezeigt, aber die Einheit kann unter Umständen mehrere haben, die nur im CR oder in der Zugvorlage sichtbar sind.  
Das wird im Kapitel über [Befehle][befehl] weiter erklärt.

Einheiten haben einen "Kampfstatus", in diesem Fall "vorne". Die Einzelheiten kannst du im Kapital [Krieg][krieg] im Abschnitt [Kampfreihen][die-schlacht] sowie in der Erklärung zum Befehl [KÄMPFE][bef-kampfe-id] nachlesen.

Eine Einheit kann eine Region bewachen (zu den Auswirkungen siehe [`BEWACHE`][bef-bewache]).  
In diesem Fall steht bei ihr zusätzlich "bewacht die Region".

Schlussendlich kann eine Einheit durch einen [Kampf][krieg] oder durch [Hunger][hunger-de-id] verwundet sein.  
In diesem Fall steht bei der Einheit noch "erschöpft", "verwundet" oder gar "schwer verwundet".

Die nächste Einheit hat die Nummer 2ow, besteht aus einem [Zwergen][zwerge] und hat ein Pferd und einen Silberbeutel.  
Das heißt, dass sie mehr als 500 Silber bei sich hat.  
Hätte sie gar mehr als 5000 Silber bei sich, sähe man eine Silberkassette.  
Hätte sie nur 500 Silber oder weniger, würde man bei einer fremden Einheit gar nichts sehen.  
Welcher Partei die fremde Einheit angehört, kann man nicht sehen, denn sie hat sich [parteigetarnt], verbirgt also ihre Parteizugehörigkeit.  
Dies ist bei Botschaftern natürlich keine besonders kluge Wahl, da die anderen Spielenden so auch nicht an die E-Mail-Adresse der Partei kommen. Du kannst einer solchen Einheit höchstens eine [`BOTSCHAFT`][bef-botschaft] zukommen lassen.

Schließlich siehst du ein paar befreundete [Trolle][trolle], die Juwelen geladen haben.  
Neben [Menschen][menschen], [Zwergen][zwerge] und [Trollen][trolle] gibt es noch viele andere Rassen in Eressea.  
Sie werden [diesem Kapitel][rassen] näher behandelt.

Über fremde Einheiten gibt es nur begrenzte Informationen.  
Ihr Kampfstatus, Verletzungen, Talente, Gruppe, Parteitarnung, Rassentarnung, Heldenstatus und Zauber sind verborgen.  
Die meisten Gegenstände sind sichtbar, aber Silber, Kräuter und magische Gegenstände sind nicht alle genau zu erkennen.

### Auflösung von Einheiten

Sollte eine Einheit am [Ende der Runde][befehlsreihenfolge] einmal keine Personen mehr haben (sei es durch Hunger, Übergabe oder weil sie nie welche bekommen hat), wird sie aufgelöst.  
Ihre Gegenstände fallen dann an eine Einheit der eigenen Partei, falls vorhanden, ansonsten an eine befreundete Einheit (zu der sie [`HELFE Silber`][bef-helfe] hat und die zu ihr `HELFE GIB` hat).  
Dabei wird wahrscheinlich die erste Einheit der Reportreihenfolge ausgewählt.  
Falls beides nicht geht, fallen Silber und Pferde an die Region, alle anderen Gegenstände gehen verloren.

Spielererfahrung: SoltharEs soll Fälle geben, bei denen besondere magische Gegenstände eine unheimliche Energie erzeugen, die Einheiten in einem Zustand zwischen Leben und Tod erhalten.  
Diese sind dann aber nicht mehr unter der Kontrolle ihrer ehemaligen Partei.

## Siehe auch

- [Der Parteipool][parteipool]
- [Befehle][befehl]

Weiterlesen: [Rassen][rassen].

<!-- From [https://wiki.eressea.de/index.php?title=Parteien&oldid=16699] -->

[`ZEIGE "`*`Gegenstand`*`"`]: [[bef-zeige]]
[`MACHE TEMP`]: [[bef-mache]]
[Defaultbefehl]: [[bef-default]]
[parteigetarnt]: [[bef-tarne]]
[bef-bewache]: [[bef-bewache]]
[bef-botschaft]: [[bef-botschaft]]
[bef-gib]: [[bef-gib]]
[bef-helfe]: [[bef-helfe]]
