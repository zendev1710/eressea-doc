---
# cSpell:locale fr
alias: cmd-comment-with-slashes-fr
---

# `//`

**`//`**` `*`<commentaire>`*  

Contrairement à un commentaire qui suit un [`;`][cmd-comment-fr], ce commentaire est inclus dans le **modèle d'évaluation du prochain tour**.  

```text
UNIT 123; Cent vingt-trois [20,450$]
// Entretien de la Tour des mages
@GIVE 234 1000 silver
// Apprendre de temps en temps le combat à l'arme d'hast
TAX
```

`//` doit être traité comme un ordre; donc vous ne pouvez **pas** faire :

```text
@GIVE 345 100 silver // pour la scierie
```

!!! note
    Un caractère d'espacement doit suivre l'instruction `//`.

<!-- From  [https://wiki.eressea.de/index.php?title=KOMMENTAR&oldid=3993] -->

[cmd-comment-fr]: [[cmd-comment-fr]]
