---
# cSpell:locale fr
alias: cmd-comment-with-slashes-fr
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD052 -->
# Commentaire //

**`//`**` `*`Comment`*  

Contrairement à un commentaire qui suit un [;][cmd-comment-fr] (point-virgule), ce commentaire est inclus dans le modèle **d'évaluation du prochain tour**.  

```text
UNIT 123; Cent vingt-trois [20,450$]
// Entretien de la Tour des mages
@GIVE 234 1000 SILVER
// Apprendre de temps en temps le combat à l'arme d'hast
TAX
```

`//` doit être traité comme un ordre, donc vous ne pouvez **pas** faire :

```text
@GIVE 345 100 SILVER // à cause de la scierie
```

!!! note
    Il doit également y avoir un espace après `//`.

<!-- From  [https://wiki.eressea.de/index.php?title=KOMMENTAR&oldid=3993] -->

[cmd-comment-fr]: [[cmd-comment-fr]]
