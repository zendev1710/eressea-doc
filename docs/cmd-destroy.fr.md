---
# cSpell:locale fr
alias: cmd-destroy-fr
---

# DESTROY

*Ordre [long][ordres-courts-et-longs]*.

**`DESTROY`**`[`*`niveau`*`]`  
**`DESTROY`**`[`*`niveau`*`] STREET`*`direction`*  

Une unité commandant un [bateau][bateaux-id] ou un [bâtiment][batiments-id] peut réduire sa taille ou le détruire à tout moment en utilisant cet ordre.  
Elle n'a besoin d'aucune compétence pour cela.  

Pour les **bâtiments**, le paramètre *niveau* indique le **nombre de points de taille** duquel le bâtiment doit être réduit.  
Pour les **bateaux**,  le paramètre *niveau* définit le **pourcentage** de réduction.  

Si *niveau* n'est pas spécifié, la structure sera complètement détruite.  

Cependant, les bateaux ne peuvent être partiellement ou totalement détruits **qu'en zone côtière**.  
L'équipage refuse d'endommager le bateau en haute mer !

Avec `DESTROY [`*`level`*`] STREET`*`direction`* vous pouvez démolir ou endommager une [route][routes-id].  
<!-- TODO: check if the sentence below is related to DESTROY -->
Aucune faction n'est autorisée à garder la région si elle n'a pas défini `HELP GUARD` comme sa propre faction.  
Pour endommager ou détruire une route, une unité a besoin d'être compétent en [construction de routes][construction-de-routes]{title="Roadwork"}.
Vous pouvez détruire un point de taille par point de compétence.

Une unité ne peut détruire qu'une seule structure (bâtiment, bateau ou route) par semaine.

<!-- From [https://wiki.eressea.de/index.php?title=DESTROY&oldid=16738] -->
