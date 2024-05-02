# swarm
Particule swarm optimization sandbox

Contexte

L'optimisation par essaim de particules (particle swarm optimization - PSO dans la suite du texte) est fondée sur une famille d'algorithmes stochastiques basés sur une population [dite particulaire], et inspirés par le comportement collectif de certains animaux comme les nuées d'oiseaux, les bancs de poissons, les abeilles, etc …
Ces essaims ont un comportement coopératif, par exemple pour la recherche de nourriture, chaque « particule » de l'essaim réagissant à ses propres perceptions, mais également à celles des autres « particules » par communication.

Historiquement, les premiers développements sont relativement récents et remontent à 1987 (Craig Reynolds) et 1995 (James Kennedy et Russel Eberhart).

Les algorithmes PSO sont en général robustes, et convergent le plus souvent très rapidement vers la solution recherchée.
Ils peuvent en outre être facilement parallélisés et hybridés avec d'autres algorithmes.
Ils restent curieusement assez peu utilisés, peut-être parce que le choix des paramètres reste empirique, et qu'ils sont non-déterministes (mais ils sont loin d'être les seuls dans le domaine de l'optimisation ou du « data scientisme ».

Le champ d'étude théorique reste ouvert, notamment pour la détermination a priori des plages de paramètres, et l'application à des problèmes discrets, multi-objectifs, contraints, ou dynamiques.

Présentation d'un algorithme de base

L'algorithme présenté est celui d'Eberhart et Shi (A modified particle swarm optimizer – 1998).

Chaque particule « i » est définie par un vecteur position Xi et un vecteur vitesse de déplacement Vi.
A chaque particule est associée sa dernière meilleure position Pi, relativement à l'objectif.
A l'ensemble des particules est associée la meilleure dernière position absolue G, relativement à l'objectif.

L'évolution de ces vecteurs est calculée comme suit :

Vi = w.Vi + c1.rand1[0 ..1].(Pi – Xi) + c2.rand2[0 ,, 1].(G – Xi)

Xi = Xi + Vi

w, c1, c2 sont des constantes scalaires
rand1[0 ..1] et rand2[0 ,, 1] sont deux scalaires aléatoires prenant leurs valeurs entre 0 et 1

L’intervalle de temps entre mises à jour de Vi et Xi est supposé égal à 1, pour assurer la cohérence entre position et vitesse.

Le premier terme de mise à jour de la vitesse modélise l'inertie de la particule.
Le second terme modélise la perception de la particule par rapport à l'objectif.
Le troisième terme modélise l'influence de l'essaim sur la particule (terme de « communication »).

Test

Pour l'exemple Python, on utilise une fonction de Rastrigin dont on recherche la valeur minimale absolue.
Les coordonnées objectif sont 0, 0.
Sur le graphe animé, G est représenté par une X, les positions des particules par O, et les vitesses par des flèches (direction et module).
