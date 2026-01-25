---
# cSpell:locale en
alias: comment-with-slashes
---
# // Comment

**`//`**` `*`Comment`*  

In contrast to a comment after a [[cmd-comment|`;`]] (semicolon), this comment is included in the template **for the next round's** evaluation.  

```text
UNIT 123; One hundred and twenty-three [20,450$]
// Upkeep Mage Tower
@GIVE 234 1000 SILVER
// Learn polearms every now and then
TAX
```

The `//` has to be treated like an order, so you **can't** do:

```text
@GIVE 345 100 SILVER // because of sawmill
```

!!! note
    There must also be a space after the `//`.

<!-- From  [https://wiki.eressea.de/index.php?title=KOMMENTAR&oldid=3993] -->
