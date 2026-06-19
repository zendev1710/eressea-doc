---
# cSpell:locale fr
alias: cmd-cast-fr
---

# CAST

*Ordre [court][ordres-courts-et-longs] [^1].*

**`CAST`**` [REGION `*`<x>`*` `*`<y>`*`] [LEVEL`` `*`niveau`*`] "`*`<sort>`*`" [`*`parameter`*`] ...`

Avec cet ordre, une unité de mage tentera de lancer le sort spécifié.  

Veuillez noter que les modificateurs `REGION` et `LEVEL` ne s'appliquent pas à tous les sorts.  

`REGION` ne peut être utilisé qu'avec des [sorts à distance][magie-a-distance], et `LEVEL` n'a de sens qu'avec des sorts à [coût][composants] variable.

!!! note
    Certains sorts ont des paramètres supplémentaires.

L'utilisation des sorts est expliquée plus en détail dans le chapitre [Magie][magie], et peut également être trouvée dans la description du sort elle-même.  
Vous obtenez leur description lorsque vous récupérez le sort, et vous pouvez utiliser l'ordre [`SHOW ALL SPELLS`][cmd-show-fr] pour l'afficher à nouveau.  

Les **sorts de combat** ne peuvent pas simplement être lancés.  
Si vous souhaitez en utiliser un contre une unité, vous devez définir le statut [`COMBATSPELL`][cmd-combatspell-fr] puis [attaquer][cmd-attack-fr] une unité (ou être attaqué).  
Cependant, cela peut déclencher de plus grandes batailles !  

[^1]: bien que `CAST` ne soit pas un ordre long, il exclut les autres ordres longs. Mais vous pouvez lancer d'autres sorts.

<!-- From [https://wiki.eressea.de/index.php?title=CAST&oldid=16737] -->

[cmd-attack-fr]: [[cmd-attack-fr]]
[cmd-show-fr]: [[cmd-show-fr]]
[cmd-combatspell-fr]: [[cmd-combatspell-fr]]
