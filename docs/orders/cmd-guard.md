---
alias:
	name: 
	text: 
---
# GUARD

**`GUARD`**`[NOT]`

Einheiten können ihre Region bewachen. Dazu muss die Einheit mit mindestens einer [Waffe][] [bewaffnet] sein und das passende Waffentalent haben. Ozeanregionen können nicht bewacht werden.

Wenn eine Partei eine Region bewacht, gelten für Einheiten, die mit ihr nicht [alliiert] sind ([`HELP GUARD`] oder [`CONTACT`]), folgende Einschränkungen:

- Sie können in dieser Region keine Steuern mehr eintreiben, Rohstoffe abbauen, [HANDELN] oder Bauern rekrutieren.
- Sie werden auf der Durchreise mit einer gewissen Wahrscheinlichkeit gestoppt.
- Befinden sie sich auf einem Schiff, so können sie nicht [`ARBEITEN`]`,`[`UNTERHALTEN`]`,`[`ATTACKIEREN`] oder sofort über Land weiterziehen. Um die Aktionen in der Folgewoche ausführen zu können, müssen sie das Schiff erst [`VERLASSEN`] haben.

Wenn die Einheit nicht gesehen wird, beispielsweise weil sie ein höheres Tarnungstalent hat als das beste Wahrnehmungstalent der bewachenden Partei in der Region ist, so gelten die ersten beiden Beschränkungen nicht.

Es ist aber sehr wohl möglich in einer bewachten Region an Land zu unterhalten, auch wenn der Bewacher kein HELP GUARD gesetzt hat. Allerdings ist es nicht möglich, wenn die Unterhalter Einheit an Bord eines Schiffes steht.

Geben mehrere Parteien gleichzeitig oder nacheinander den GUARD-Befehl, so bewachen sie alle die Region. Nur für Parteien, die mit *allen* bewachenden Parteien alliiert sind, gelten dann die obigen Einschränkungen nicht.

Parteien, die mit *mindestens einer* bewachenden Partei alliiert sind, können trotz Kämpfen noch lange Befehle (evtl. mit den obigen Ausnahmen) ausführen (siehe [Kampfende]).

In der Runde, in der der `GUARD`-Befehl gegeben wurde, gelten all diese Beschränkungen allerdings noch nicht, denn die bewachende Einheit muss erst einmal herausfinden, wo fremde Einheiten überall Silber eintreiben könnten etc. Die bewachende Einheit wird sofort für alle anderen Einheiten in der Region sichtbar, egal wie hoch ihr Tarnungstalent ist.

Mit `GUARD NOT` wird der Bewachungsstatus einer Einheit aufgelöst. Das passiert außerdem, wenn sich die Einheit fortbewegt. Einheiten mit dem Kampfstatus [COMBAT FLIEHE] können nicht bewachen und Einheiten, aus denen im Kampf alle überlebenden Personen fliehen, beenden ebenfalls das Bewachen.

Wenn eine Einheit durch eine Region reist, die von mindestens einer nicht verbündeten Partei bewacht wird, hängt die Chance, dass sie aufgehalten wird von mehreren Faktoren ab: Sie wird vergrößert durch die Anzahl der feindlichen Bewacher, den Regionstyp (es wird schwerer in Sümpfen, Gletschern, Bergen und Vulkanen), das Wahrnehmungstalent der feindlichen Bewacher, Amulette des Wahren Sehens, sowie die Größe der Burg des Regionsbesitzers, falls dieser nicht verbündet ist. Sie wird verringert durch die Anzahl der verbündeten Bewacher und das Tarnungstalent der Einheit, sowie Ringe der Unsichtbarkeit.

Hinweis: [Monster] Einheiten der Partei (ii) gelten durch ihre Klauen, Zähne, Krallen und sonstige Extremitäten prinzipiell als bewaffnet, auch wenn sie keine sichtbare Waffe tragen. Dies gilt auch für von Spielern magisch beschworene Monster.

In den [ersten Wochen] kann deine Partei noch nicht bewachen.

## See also

- [HELP][`HELP GUARD`]
- [Allianz][alliiert]
- [CONTACT][`CONTACT`]

<!-- From [https://wiki.eressea.de/index.php?title=GUARD&oldid=16839] -->

[Waffe]: ./war-tables.md#waffeneigenschaften "Kriegstabellen"
[bewaffnet]: ./armed.md "Bewaffnet"
[alliiert]: ./alliances.md "Allianz"
[`HELP GUARD`]: ./cmd-help.md "HELP"
[`CONTACT`]: ./cmd-contact.md "CONTACT"
[HANDELN]: ./silver.md#trade "Trade"
[`ARBEITEN`]: ./cmd-work.md "WORK"
[`UNTERHALTEN`]: ./cmd-entertain.md "ENTERTAIN"
[`ATTACKIEREN`]: ./cmd-attack.md "ATTACK"
[`VERLASSEN`]: ./cmd-leave.md "LEAVE"
[Kampfende]: ./war.md#the-end "Kampfende"
[COMBAT FLIEHE]: ./cmd-combat.md "COMBAT"
[Monster]: ./monsters.md "Monster"
[ersten Wochen]: ./puppy-protection.md "Welpenschutz"
