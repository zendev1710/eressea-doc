---
# cSpell:locale en
alias: cmd-learn
---

# LEARN

*[long order][short-and-long-orders].*

**`LEARN`**` `*`skill`*  
**`LEARN`**`Magie "`*`Magic School`*`"`  

With this order, the unit spends one turn [learning][learn-skills] the specified [skill][skills] (see also: [[list-of-skills]]).
On average, advancing to a new skill level through pure learning takes approximately a number of weeks corresponding to the targeted skill level, without taking modifications due to race or terrain into account.
To go from level 2 to 3 takes about 3 weeks. Typically, a skill rating of 2 is twice as effective as a skill rating of 1, a skill rating of 3 is three times as effective, and so on.

The order `LEARN Magic "Magic School"` determines the [magic school][magic] for a faction that does not already have one.

With `LEARN`*`Taktik`*`200` you can tell tools like  [ECheck][echeck-id] how high the [learning costs][skills] are (here 200 silver).
However, this is not evaluated by the server.

## See also

- [Learning][learn-skills]
- By using [teachers][cmd-teach] you can halve the required learning times
- Through the [`LEARN-AUTO`][cmd-learn-auto] order, the server attempts to automate learning and teaching in a region within a faction. A mixture of `TEACH` and `LEARN AUTO` however, is not possible

<!-- From [https://wiki.eressea.de/index.php?title=LEARN&oldid=16727] -->

[cmd-learn-auto]: [[cmd-learn-auto]]
[cmd-teach]: [[cmd-teach]]
