# ensci_cnn

## Emplacement

Le logiciel est situé dans le dossier `D:\IA\classifier`

## Mise en place

Soit `n` l'index de la base d'apprentissage (on peut donc en mettre en place plusieurs).

L'index `n` étant par exemple égal à `1` (première base d'apprentissage), répartir les images entre deux catégories (soit `a` et `b`) de manière équitable dans les dossiers `dataset\training_set_1\a`, `dataset\training_set_1\b`, `dataset\test_set_1\a` et `dataset\test_set_1\b`.

(Pour une seconde base d'apprentissage d'index `2`, faire de même avec d'autres images dans les dossiers `dataset\training_set_2\a`, `dataset\training_set_2\b`, `dataset\test_set_2\a` et `dataset\test_set_2\b`, etc.)

## Apprentissage

Exécuter l'apprentissage via la commande **`python train.py 1`** (pour l'index de base d'apprentissage `1` – pour une seconde base d'apprentissage d'index `2`, exécuter la commande `python train.py 2`, etc.)

Le processus peut prendre plusieurs heures : **il ne faut pas l'interrompre !**

Une fois que l'apprentissage est terminé sur une base d'images donnée, il n'est plus nécessaire de le refaire.

> Note : il existe déjà une base d'apprentissage `1` capable de classifier une image entre *chat* (catégorie a) et *chien* (catégorie b). 

## Évaluation d'une nouvelle image

Poser les nouvelles images à évaluer dans le dossier `testset`.

Pour évaluer l'image `exemple.jpg` sur la base d'apprentissage d'index `1`, exécuter la commande **`python test.py 1 exemple.jpg`**. Au terme de l'évaluation, le programme affichera soit `FIRST category (A)` ou `SECOND category (B)`.