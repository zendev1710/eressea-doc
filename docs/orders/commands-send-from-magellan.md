---
alias:
	name: sending-orders-from-magellan
	text: Sending orders from Magellan
---
# Sending orders from Magellan

<!-- TODO: magellan screenshot 400X134 - should be where in the page ? -->
![Befehle mit Magellan Einsenden am Beispiel Gmail](./assets/images/orders-sending-gmail.png "Befehle mit Magellan Einsenden am Beispiel Gmail")
<!--
Befehle mit Magellan Einsenden am Beispiel Gmail</span></a>
<figcaption>Befehle mit Magellan Einsenden am Beispiel Gmail</figcaption>
-->

[Magellan] bietet die Möglichkeit des [E-Mail-Versands] der Befehle direkt aus dem Programm. Vorteil davon ist, dass es keine Fehler durch Kopieren in das E-Mail-Programm oder Webmailer gibt und diese keine automatischen Formatierung vornehmen, die der Eressea Server nicht versteht, zum Beispiel HTML-Formatierung, komische Zeilenumbrüche, automatische Banner oder eine seltsame Buchstabencodierung, insbesondere bei Umlauten. Um eine Kopie der gesendeten E-Mail zu haben, kann man sich die Befehle als Kopie an die eigene Adresse senden. Hierzu muss man in Magellan die entsprechenden Einstellungen vornehmen inklusive der korrekten Daten des SMTP-Servers des Mailanbieters. Die Daten erhält man üblicherweise aus der Hilfe des Anbieters, für einige sind die Daten unten angegeben. Darüber hinaus kann es sein das man beim Anbieter explizit Berechtigung für externe Programme geben muss.

## In Magellan

Die Einstellung finden sich unter `Datei => Befehle Speichern...` im zweiten Reiter `E-Mail`. Wenn die Einstellungen einmal vorgenommen wurden, kann man auch direkt über `Datei => Befehle per E-Mail senden` verschicken.

**Absenderadresse:** Deine E-Mail  
**SMTP-Server:** Vom Mailanbieter (siehe unten)  
**Port:** Vom Mailanbieter  
**Benutzername:** Dein Benutzername beim Mailanbieter  
**Passwort:** Passwort vom Mailanbieter, **nicht** das Eressea-Befehlspasswort  
**Empfängeradresse:** <eressea-server@eressea.kn-bremen.de>  
**Subject:** ERESSEA 2 BEFEHLE  
**CC:** Optional, zum Beispiel die eigene Adresse

**Kopie an Absender:** Sendet die Befehle auch an Absendeadresse  
**Verwende SSL/TLS:** Emailverschlüsselung; sollte möglichst ausgewählt werden, wenn vom Mailanbieter unterstützt (im Zweifel einfach ausprobieren)  

Authentifizierung verwenden  
in der Regel nötig  

**immer nachfragen:** Fragt das Mailanbieter-Passwort bei jedem Senden ab, es muss dann auch nicht in Magellan gespeichert werden  
**Verwende Werte vom CR:** Füllt Empfängeradresse und Subject automatisch, wenn die Daten im CR stehen

Für einige bekannte Mailanbieter folgen hier die benötigten Werte, soweit derzeit bekannt:

## GMX

Die Hilfe von GMX zum STMP-Server findet sich unter: [https://hilfe.gmx.net/pop-imap/index.html] und zu den SMTP Einstellungen unter [https://hilfe.gmx.net/pop-imap/pop3/serverdaten.html]. Darüber hinaus ist es notwendig die externe Berechtigung zum Senden zu erteilen. Dies wird (inklusive Video) unter [https://hilfe.gmx.net/pop-imap/einschalten.html] erklärt.

**Absenderadresse:** Deine E-Mail bei GMX  
**SMTP-Server:** mail.gmx.net  
**Port:** 587 (mit TLS) oder 465 (mit SSL)  
**Benutzername:** Dein Benutzername bei GMX (entweder deine Mailadresse oder deine Benutzernummer)  
**Passwort:** Passwort vom GMX, **nicht** das Eressea-Befehlspasswort

**Verwende SSL:** Ja (Mit Port 465, sonst Nein)  
**Verwende TLS:** Ja (Mit Port 587, sonst Nein)  
**Authentifizierung verwenden:** Ja

## Gmail

<!-- TODO: - should be where in the page ? -->
![Befehle mit Magellan Einsenden am Beispiel Gmail](./assets/images/orders-sending-gmail.png "Befehle mit Magellan Einsenden am Beispiel Gmail")
<!--
Befehle mit Magellan Einsenden am Beispiel Gmail</span></a>
<figcaption>Befehle mit Magellan Einsenden am Beispiel Gmail</figcaption>
-->

**Absenderadresse:** Deine E-Mail bei Gmail  
**SMTP-Server:** smtp.googlemail.com  
**Port:** 465  
**Benutzername:** Dein Benutzername bei Gmail  
**Passwort:** Passwort vom Gmail, **nicht** das Eressea-Befehlspasswort

**Verwende SSL:** Ja  
**Verwende TLS:** Egal, geht beides  
**Authentifizierung verwenden:** Ja

*Achtung!* Spätestens ab 30. Mai 2022 funktioniert dies nicht mehr einfach mit dem Gmail-Passwort ([https://support.google.com/accounts/answer/6010255]). Stattdessen muss man ein so genanntes App-Passwort verwenden einrichten. Genaueres verrät die Gmail-Dokumentation: [https://support.google.com/accounts/answer/185833]. Anstelle des Gmail-Passworts gibt man in Magellan dann einfach das App-Passwort an.

## Freenet

**Absenderadresse:** Deine E-Mail bei Freenet  
**SMTP-Server:** mx.freenet.de  
**Port:** 587  
**Benutzername:** Dein Benutzername bei Freenet  
**Passwort:** Passwort vom Freenet, **nicht** das Eressea-Befehlspasswort

**Verwende SSL:** Ja  
**Verwende TLS:** Ja  
**Authentifizierung verwenden:** Ja

## Posteo

<!-- TODO: orders sending with Posteo 400X159 - should be where in the page ? -->
![Befehle mit Magellan Einsenden am Beispiel Posteo](./assets/images/orders-sending-posteo.png "Befehle mit Magellan Einsenden am Beispiel Posteo")
<!--
title=Befehle mit Magellan Einsenden am Beispiel Posteo"Befehle mit Magellan Einsenden am Beispiel Posteo</span></a>
<figcaption>Befehle mit Magellan Einsenden am Beispiel Posteo</figcaption>
-->

**Absenderadresse:** Deine E-Mail bei Posteo  
**SMTP-Server:** posteo.de  
**Port:** 465  
**Benutzername:** Deine E-Mail bei Posteo  
**Passwort:** Passwort vom Posteo, **nicht** das Eressea-Befehlspasswort

**Verwende SSL:** Ja  
**Verwende TLS:** Ja  
**Authentifizierung verwenden:** Ja

<!-- From [https://wiki.eressea.de/index.php?title=Befehle\_von\_Magellan\_verschicken&oldid=7407] -->

[Magellan]: ./magellan.md "Magellan"
[E-Mail-Versands]: ./commands-send.md "Befehle einschicken"
[https://hilfe.gmx.net/pop-imap/index.html]: https://hilfe.gmx.net/pop-imap/index.html
[https://hilfe.gmx.net/pop-imap/pop3/serverdaten.html]: https://hilfe.gmx.net/pop-imap/pop3/serverdaten.html
[https://hilfe.gmx.net/pop-imap/einschalten.html]: https://hilfe.gmx.net/pop-imap/einschalten.html
[https://support.google.com/accounts/answer/6010255]: https://support.google.com/accounts/answer/6010255
[https://support.google.com/accounts/answer/185833]: https://support.google.com/accounts/answer/185833
