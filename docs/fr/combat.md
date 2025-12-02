# COMBATS

**`COMBATTRE`**`DE FACE COMBAT`  
**`AGRESSIF`**`COMBATTRE`  
**`PAR`**`RETOUR`  
**`COMBAT`**`DÉFENSIF NE PAS`  
**`COMBATTRE`**  
**`FUIR`**`LES COMBATS`  
**`AIDE`**`[NE PAS]`

Cet ordre détermine la réaction d’une unité en cas de combat (voir également la section sur [les lignes de bataille dans le chapitre][] [Sur la guerre] ). [][les lignes de bataille dans le chapitre]

- `COMBATTEZ AVEC AGRESSION` : Au combat, l’unité est en première ligne et ne fuira jamais, mais se battra jusqu’à la mort. C’est un avantage considérable lorsque chaque once de puissance offensive est cruciale.

- `COMBAT DE FRONTIÈRE` : En combat, l’unité est positionnée en première ligne. Elle tentera de fuir si ses points de vie sont inférieurs ou égaux à 20 %. Cet avantage est particulièrement avantageux pour les épéistes aguerris. Peut également être combiné avec `COMBAT` .

- `COMBAT PAR L'ARRIÈRE` : L'unité combat en deuxième ligne. Même si le front est décimé, ces unités seront toujours engagées au corps à corps ! C'est un avantage pour les fusiliers. L'unité tentera de fuir lorsqu'il lui restera 20 % ou moins de ses points de vie.

- `COMBAT DÉFENSIF` : Similaire à `RIGUER` , mais l’unité fuira lorsqu’il lui restera 90 % de ses points de vie. Ceci est avantageux pour les mages.

- `NE PAS COMBATTRE` : L’unité ne combattra que si elle est elle-même la cible d’un ordre [`d’ATTAQUE`] ennemi . Ceci est avantageux pour les unités qui doivent rester hors de combat sans pour autant fuir, par exemple parce qu’elles occupent un bâtiment. L’unité tentera de fuir lorsqu’il lui restera 90 % de ses points de vie.  

- `FUITE` : Si une unité dotée de ce statut de combat est engagée dans un combat, elle tentera de fuir avant chaque round. Pour plus d'informations sur le comportement de fuite, consultez la section «[Fuite] --> du chapitre « Combat ». Ce statut est avantageux pour la quasi-totalité des civils. Si un seul membre d'une unité parvient à fuir, il quitte automatiquement les bâtiments ou navires où il se trouve. Il est donc important de déterminer si ce statut est utile pour les occupants des bâtiments. Les unités dotées de ce statut ne peuvent ni [ATTAQUER][`d’ATTAQUE`] ni [GARDER] . Si une unité de garde utilise FUITE, sa mission de garde est immédiatement annulée, avec les conséquences qui en découlent. Les unités dotées de ce statut peuvent toujours se déplacer après un combat (en utilisant [les commandes VERS] , [ITINÉRAIRE] et [SUIVRE] ).

*Attention* ! Les unités dotées des compétences COMBATTRE/FUIR ou NE PAS COMBATTRE combattront si elles sont attaquées et que les deux premières lignes sont franchies. Cela signifie que les mages lanceront également des sorts. Les sorts d'avant et d'après-combat sont (actuellement) lancés même si les premières lignes ne sont pas franchies. Pour éviter cela, vous pouvez désactiver [les sorts de combat] .

L'utilisation des catapultes est une tâche qui nécessite beaucoup de préparation ; par conséquent, les unités ayant le statut de combat NE PAS COMBATTRE et COMBATTRE FUIR ne tireront aucune munition, mais auront recours à d'autres armes si elles en possèdent et savent les utiliser.

*Attention* ! Les personnages ayant peu de points de vie et n'ayant pas activé `la capacité COMBATTRE/FUIR` ne fuiront que s'ils sont touchés au combat. Cela inclut les coups dont les points de dégâts ont été entièrement absorbés par l'armure et les tentatives de coup ratées. Les personnages ayant activé `la capacité COMBATTRE/FUIR` fuiront, bien entendu, avant d'être touchés.

- `AIDE AU COMBAT` : Une unité bénéficiant `du statut AIDE AU COMBAT` ne recevra aucune assistance au combat, ni de ses propres troupes ni de ses alliés. Si une telle unité est attaquée, aucune autre unité ne sera appelée en renfort. Ceci n'est valable que si aucune autre unité ne possédant pas ce statut n'est également attaquée.

Votre groupe est toujours impliqué lorsqu'il attaque, ou lorsqu'il est attaqué, lui ou un groupe qu'il aide. Vous trouverez plus de détails dans la [`section AIDE`] et dans les chapitres [Combat][Sur la guerre] et [Alliance] .

<!-- From [https://wiki.eressea.de/index.php?title=COMBAT&oldid=7216] -->

[les lignes de bataille dans le chapitre]: /Schlacht "bataille"
[Sur la guerre]: /Krieg "Guerre"
[`d’ATTAQUE`]: ./cmd-attack.md "ATTAQUE"
[ Fuite]: /Die_Flucht "L'évasion"
[GARDER]: ./cmd-guard.mdN "GARDE"
[les commandes VERS]: /MOVE "APRÈS"
[ITINÉRAIRE]: /ROUTE "ITINÉRAIRE"
[SUIVRE]: /FOLLOW "CONSÉQUENCE"
[les sorts de combat]: /COMBATSPELL "SORTS DE COMBAT"
[`section AIDE`]: /HELP "AIDE"
[Alliance]: /Allianz "Allianz"
