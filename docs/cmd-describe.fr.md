---
# cSpell:locale fr, en
alias: cmd-describe-fr
---
# DESCRIBE

**`DESCRIBE UNIT`**`"`*`text`*`"`  
**`DESCRIBE BUILDING`**`"`*`text`*`"`  
**`DESCRIBE SHIP`**`"`*`text`*`"`  
**`DESCRIBE REGION`**`"`*`text`*`"`  
**`DESCRIBE PRIVATE`**`"`*`text`*`"`  

The description for the listed object is changed. This description is listed by object and can be up to 8191 characters long.
The computer does not assign descriptions when creating objects.

The same restrictions apply to ships, buildings and regions as when naming objects: buildings and ships can only be described if the unit also has command of the building or ship (i.e. it must be the first unit under the building or ship in the evaluation).
A region can only be described by the lord of the most powerful castle in a region.

With `DESCRIBE PRIVATE` You can give the commanding unit a "private" description that only the owner of the unit can see.

Long descriptions must be with done with the `\` (backslash) "extend order" separator.
New lines after that `\` must not begin with spaces.
<!-- TODO: clarify text below -->
```text
    DESCRIBE UNIT "Leaf-cutting ants don't need one\
    Sleep and its workers are always focused on maximum efficiency\
    t. Everything they do and think under their black cover refers to\
    hen it also das Kollektiv des Staates."
```

It is currently not possible to insert paragraphs and breaks themselves into descriptions.

<!-- From [https://wiki.eressea.de/index.php?title=DESCRIBE&oldid=7442] -->
