---
# cSpell:locale fr
alias: commerce-automatise
---
# Commerce automatisé

Le commerce n’a qu’un seul objectif : maximiser le rendement de l’argent.  
Cela signifie que le grand objectif est défini très simplement.  

Le problème à optimiser est donc de maximiser le profit entre l’achat et la vente.  
La condition secondaire est le transport de la marchandise, même si cette condition secondaire peut vite devenir très compliquée.  

## Maximisation du profit commercial

Dans le monde d'Eressea, les régions d'une île proposent généralement l'un des deux biens commerciaux à l'achat.  
Cela rend relativement facile la détermination de la quantité optimale d’achat de marchandises sur l’île, car nous connaissons la quantité maximale que nous pouvons vendre et à quel prix.  
Tant qu’il y a encore une marge entre l’achat et la vente, nous achèterons.  
Habituellement, vous achèterez pour vos propres besoins sur les îles à 1 à 3 fois le prix de base, juste dans la proportion dans laquelle les deux produits de luxe sont proposés.  
Pour des raisons de minimisation des unités, les régions avec un volume d'échanges très faible peuvent également être évitées et doivent donc être exclues du calcul.  

Le besoin de produits de luxe externes est souvent encore plus facile à déterminer.  
C'est à peu près le nombre d'agriculteurs de l'île divisé par 100.  
Cependant, ce besoin sera rarement satisfait car les bateaux ont généralement des choses plus importantes à faire.  

Le problème ici est plutôt ennuyeux ou ne peut pas être décrit comme un problème.  
Ce n'est que pendant le transport que des « décisions » doivent être réellement prises.

## Condition supplémentaire importante : le transport

Restons pour l'instant sur le cas simple de deux marchandises échangées et regardons maintenant le transport.  
Comme nous ne pouvons pas traiter un nombre quelconque d'unités de transport - au contraire, ce nombre doit être minimisé (limite d'unités) - nous pouvons difficilement livrer tous les besoins chaque semaine "juste à temps".  
Nous pouvons ainsi obtenir plus que ce dont nous avons besoin pour une semaine dans une région à la fois.  

Les approches permettant de déterminer les conditions de stockage optimales et la quantité transportée sont aussi différentes que similaires.  
En fin de compte, vous essayez toujours de livrer au moins la quantité actuellement requise, tout en maintenant le transport à pleine capacité.

Une approche est le modèle de priorité : le prix de vente et le délai de livraison des marchandises peuvent être inclus dans la priorité.  
Puisqu’au fil du temps, tous les prix de vente d’un produit atteignent la même valeur, vous pouvez vous limiter dans le temps.  

Si vous attribuez désormais les transports par priorité, un stock minimum peut toujours être garanti si le nombre de transports et la capacité des transports sont suffisants.  

Plus vous contrôlez intelligemment le transport, moins vous aurez besoin de trajets à vide et donc de transport et de capacité de transport.  
Il est donc important d’effectuer le moins de transports possible et le plus court possible.  
Malheureusement, l’optimisation de ce problème est complexe : à mesure que le nombre de régions augmente et surtout le nombre d’agriculteurs très différent et certaines topologies insulaires, le nombre de combinaisons d’itinéraires de livraison possibles augmente de façon exponentielle.  
Cela ne vaut probablement pas la peine de déterminer ici la combinaison optimale (cela revient généralement à rechercher toutes les combinaisons judicieuses).  
Au lieu de cela, essayez simplement de trouver une bonne combinaison  
Cela peut être fait à l’aide de diverses règles ou d’une « recherche ciblée ».  

Les règles seraient, par exemple :

- Vers une région de destination, recherchez un transport dans une région source proche
- Un transport doit atteindre un remplissage d'au moins X %

Une recherche ciblée peut créer des états qui représentent un résultat partiel et, sur cette base, étendre les états suivants les plus prometteurs.  
Puisque, bien entendu, des résultats partiels qui ne sont pas seulement bons à première vue peuvent finalement produire un état final presque optimal, une évaluation est nécessaire.  
Cette évaluation doit à son tour évaluer les connaissances et les estimations à différents degrés afin d'atteindre un état cible presque optimal dans un délai raisonnable, même avec des milliards d'états possibles.  
Bien entendu, les conditions qui ne produisent certainement pas un bon résultat doivent également être éliminées au préalable.  

<!-- From [https://wiki.eressea.de/index.php?title=Automatisierung\_Handel&oldid=2482] -->
