---
# cSpell:locale en
alias: sending-orders
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD042 MD052 -->
# Sending orders

## What you need to play Eressea

In addition to your own email access, you don't need much to play Eressea.  

To edit the [[orders]], a simple text editor is sufficient.  
Under UNIX/Linux e.g. VI or EMACS, under Windows Notepad also works.  
The important thing is: the editor should only make a line break where you actually enter one.  
Under no circumstances should lines that are too long be wrapped independently, otherwise orders may not be executed correctly.  

[Notepad++] is a good editor for Windows.

### Examples

Most new players use the [[magellan]] tool.  
Eressea also has various other tools that make life easier for the player.  
Here is a list of the most famous ones:

- [CSMap][csmap-fr-id]
- [[echeck]]
- [[ehmv]]
- [[magellan]]
  - [[extended-commands]]
  - [[fftools]]
- [[vorlage]]

## How to submit orders, and what you get in return

You can send in your orders up to 20 times in each round.  
Submitting provisional orders is therefore possible and recommended.  
You should make sure that the correct time is set on your computer.  
The server uses the send time as the basis for overwriting old orders, not the received time.  

Please note: The trains must appear as normal text (text/plain) in the text of the email (mail body).  
Alternatively, they can be in one `.txt` file can be sent as an attachment, but then the email must otherwise be empty (no text in the email body).  
Otherwise the orders will not be recognized by the game server and will be ignored!  
There are various [tools][how-to-submit-orders-and-what-you-get-in-return] that make entering orders easier, especially for larger factions.  

Be careful when using web interfaces such as GMX or GMail!  
These have proven to be problematic in the past because emails were formatted incorrectly.  

Users of [[magellan]] can most conveniently [[sending-orders-from-magellan|send orders directly from the program]], without having to go through email programs or web mailers.  

The orders must always be sent to [eressea-server@kn-bremen.de] with the subject **ERESSEA 2 ORDERS**.  
If these subjects are not used, the emails will not be recognized by the game server and will be ignored.  
Moves that arrive correctly are automatically checked with the ECheck syntax checker and the result of the check is sent to the player.  

An example:

```text
ECHECK (Version 3.4.2, Jun 12 2000), Zug-Checker für Eressea - Freeware!

Process file `[faroul@beyond.kn-bremen.de](mailto:faroul@beyond.kn-bremen.de)'2'.
Recruitment cost set to 75 Silver, Warning Level 0.
Silver pool activated.

Orders were read for 1 faction and 100 units.
The orders seem fine.
```

This confirmation usually occurs within a few minutes.  
Since the server can unfortunately only send one orders confirmation every 2 minutes for technical reasons, there may be longer waiting times, especially shortly before the evaluation.  
So sending identical orders frequently to get confirmation faster doesn't help anyone, it just makes the problem worse.  
However, if the orders were sent correctly to the server, they are usually processed, even if no orders confirmation has been received before evaluation.  
For technical reasons, no confirmations will be sent on Saturdays between 8:45 p.m. and midnight.  
**It is therefore advisable to send orders as early as possible before the ZAT at 21:00.**  

If the evaluation is delayed due to technical problems or errors in the game, the evaluation in the following week will be canceled if the evaluation is not sent by 11:00 a.m. on Sunday morning at the latest.  

If no orders are received by the game leader over five rounds (so-called "NMR", No Moves Received), the faction automatically dissolves!  

ECheck on the server only does basic syntax testing.  
You can also download ECheck at home and use its options for more advanced testing.  
Magellan has also built in extensive tests that essentially make ECheck unnecessary.  

## Request

### Request the report

Sometimes it can happen that the email with the report is lost somewhere due to technical failures.  
If you still haven't received a report on Monday evening and there was no announcement in the Eressea Announce list, you can request the current evaluation again.  

To do this, send an email with the following subject to [eressea-server@kn-bremen.de], because this is the only place where the data is available:

```text
ERESSEA 2 REPORT <faction-id> "<password>"
```

This means that all files that were sent after the regular evaluation are sent again to the requesting address (which may be different from the address to which the report is normally sent), i.e. possibly also the computer report etc.

!!! warning
    factions with special characters in the password cannot request a report!

Please don't request the report "quickly" because you don't have it to hand at the moment.  
Such requests cause unnecessary traffic.  

Mails an Eressea

| Regarding                      | Notice                              |
|--------------------------------|-------------------------------------|
| ERESSEA 2 ORDERS               | Contains orders for Eressea in text |
| ERESSEA 2 REPORT no "password" | Requests the report for the faction |

## What you need to consider when entering data

Each move must begin with the line [[cmd-eressea|`ERESSEA xxx "password"`]]. xxx is your own faction number, and "password" is the faction's password.  
Each turn must be ended with the [[cmd-next]] keyword.  

All orders are issued per unit, even if they are orders that affect the faction as a whole; someone has to do it.  

If the option has been activated, a template for the next command file is always sent in a separate file.  
Here is an example of such a move:  

```text
ERESSEA 2 "GrofxMoftzg"
; ECHECK -z -w4 -r100
REGION 4,2;     Handan
; ECHECK WAGE 12
UNIT 5;         Horde of Trolls [5,100$]
    LEARN mining
UNIT 36;        Dancer of Death [10,630$]
    ENTERTAIN
REGION 4,3;     Carcavelos
; ECHECK WAGE 11
UNIT 35;        Undead slaves [10,110$]
    WORK
REGION 5,3;     Grandola
; ECHECK WAGE 11
UNIT 32;        Les Cavaliers du Destin [5,30$]
    LEARN Entertainment
NEXT
```

The first line with the ECHECK is for the syntax checker.  
It recognizes this line and uses the parameters of the line.  
With the -z, the people and their assets from the comment behind the command [[cmd-unit]] are evaluated.
Income with [[cmd-work]] (usually 11 silver each per person), [[cmd-tax|tax]] and [[cmd-entertain]] (20 silver per person) are also taken into account.  
Expensive skills such as [[cmd-learn|`LEARN MAGIC`]] and units that move silver with [[cmd-move]] are then evaluated and warnings are issued if there is too little silver.  
The `-w4` is the “warning level”, 4 means being particularly picky.  
And finally, the `-r100` says that the recruitment cost of this faction is 100 silver per person.  

The line `; ECHECK WAGE 12` is also for ECheck and sets the wage for work in this region at 12 silver.  

It can be seen that people from Unit 32 will starve: 30 silver is not enough for five people.  
However, with the ECheck parameter `-z -w4` used above, ECheck will notice this and issue a warning.  
The unit should either earn money (e.g. with [[cmd-entertain]] if it already has the entertainment skill, otherwise with [[cmd-work]]) or another unit with enough silver should move to region 5.3.

All [[orders]] can be abbreviated.  
The computer simply takes the first word that corresponds to the order entered:

- `MO S` can mean either `MOVE SOUTHEAST` or `MOVE SOUTHWEST` to the computer, in which case the computer ignores all further orders!
- `TE 5` means `TEMP 5` to the computer, but `TE5` is an unknown word to the computer

If in doubt, you should not take any shortcuts.  
There can only be one order per line.  
If you have an email program that automatically wraps long lines of text, you can spread orders over several short lines;  
But they then have to be “extended” by adding a `\` (backslash) if the following line belongs to it:

```text
DESCRIBE unit "The ancient warrior has been around for a long time \
    put to rest. His scarred face \
    testifies to a long period of service at the front."

Route Northwest West West Northwest Pause \
    Northwest Northeast Northwest Northeast Pause \
    Southwest Southeast Southwest Southeast Pause \
    Southeast East East Southeast Southeast Pause
```

All orders are case-insensitive.  
The only exception to this is the password, which must be **exactly** entered as it was set.  

If character strings are required for the orders (e.g. for the name), they must be enclosed in quotation marks if they contain spaces.  
If necessary, these character strings can span multiple lines as long as they are extended as described above.  
Between the quotation marks, multiple spaces, line breaks and tabs are always compressed to one space each.  

Any text that follows a semicolon (`;`) is considered a [[cmd-comment|comment]].  
Comments can make it much easier to understand the moves you made next time.  
If you write comments using the [[comment-with-slashes|comment order `//`]], the comment is automatically included in the [[orders|move template]] of the next round.  

Multiple trains can be sent in.  
You can certainly send in orders for only a few units and thus save yourself and the server transfer volume.  
The orders of the other units then remain unchanged.  
The date of the email (Date: header) is used as the order.  

## See also

- [[world|The World of Eressea]]
- [[first-round]]
- [[orders]]

Continue reading: [[hints]].

<!-- From [https://wiki.eressea.de/index.php?title=Befehle\_einschicken&oldid=16786] -->

[Notepad++]: http://notepad-plus.sourceforge.net/
[Magellan]: http://magellan-client.sf.net

[eressea-server@kn-bremen.de]: mailto:eressea-server@kn-bremen.de
