---
# cSpell:locale fr
alias: orientation-optimisee
---
# Orientation optimisée

De nombreuses personnes connaissent probablement la fonctionnalité générale du calcul d’itinéraire.  
Heureusement, tous les chemins vers Rome ne sont pas recherchés, mais seulement ceux qui vont évidemment dans la direction générale.  

L'option la plus simple serait de parcourir d'abord tous les chemins existants à partir du point de départ et de mémoriser les nouveaux points intermédiaires.  
De là, tous les chemins sont repris.  
L'itinéraire le plus court vers un point est toujours mémorisé (itinéraire et distance).  
Si vous poursuivez de cette façon, vous finirez par trouver le point cible (s'il peut être atteint).  
Le fait que non seulement vous vous rapprochez de l'objectif, mais que vous prenez également une direction complètement fausse sur certains itinéraires est un inconvénient majeur sur les itinéraires longs, à la fois en termes de temps de traitement et de mémoire requise pour les états intermédiaires.  

L'algorithme de recherche A*, quant à lui, vise à élargir uniquement les points intermédiaires qui se trouvent réellement sur le bon itinéraire.  
À l'aide d'une fonction de coût, les coûts sont calculés pour chaque point (y compris le début et la fin), **probablement** jusqu'à la destination.  
Ceci est probablement important ici, car nous ne connaissons pas la distance jusqu'à la destination à moins de connaître l'itinéraire. Cela signifie que nous estimons la distance.  
La ligne droite sur la carte est une bonne estimation que nous ne parviendrons certainement pas à battre (sans portes des étoiles, trous de ver et autres ;-)  

Pour Eressea et d'autres jeux avec cartes hexagonales, la distance minimale peut être calculée relativement facilement à partir des coordonnées.  

```text
hx = start.x - target.x
hy = start.y - target.y
Distanz = max(abs(hx), abs(hy), abs(hx+hy))
```

Cette distance estimée jusqu'à la destination s'ajoute à la distance déjà parcourue.  
Les régions qui doivent encore être développées sont triées selon ce critère.  
S’il y a peu d’obstacles sur la carte, l’algorithme peut atteindre son objectif très rapidement, même sur de longues distances.  

Cependant, chaque obstacle et chaque condition supplémentaire à intégrer dans la fonction de coût entraîne rapidement un nouveau ralentissement de l'exécution.  

Magellan a déjà intégré une fonction de recherche d'itinéraire.  
En plus de la distance, il supporte également les bateaux naviguant le long des côtes.  

D'autres conditions secondaires peuvent concerner la sécurité des régions (serpents de mer, adversaires), la direction d'atterrissage dans la région cible ou encore l'escale privilégiée dans les régions terrestres en fin de tour.  
Or, ce sont précisément ces conditions secondaires qui sont difficiles voire impossibles à calculer à l'aide de la fonction d'estimation, de sorte que le comportement de l'algorithme devient de plus en plus « gourmand ».
Une recherche A* avec un estimateur qui renvoie toujours 0 correspond à une recherche gloutonne.  

<!-- From [https://wiki.eressea.de/index.php?title=Optimierung\_Wegfindung&oldid=2478] -->
