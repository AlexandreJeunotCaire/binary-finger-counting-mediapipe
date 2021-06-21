# Binary Finger Counting

## Auteur

- [Alexandre Jeunot-Caire](https://github.com/jeunotca)

## Visuel

<img src="./img/demo.gif" alt="Rendu de l'algorithme" style="margin: auto;"/>

## Description

Programme <b>personnel</b> développé en `Python` afin de découvrir la bibliothèque [Mediapipe](https://github.com/google/mediapipe).

Le programme compte simplement le nombre de doigts levés de votre **main droite** en binaire ou en décimal.

### Informations supplémentaires

A l'heure actuelle, le programme ne donne le bon résultat qu'avec la main droite. En effet, la vérification de fermeture du pouce consiste à vérifier des positions horizontales entre l'extrémité du pouce et le milieu du pouce. Cela fait qu'il considèrera un pouce gauche fermé lorsqu'il est ouvert, et réciproquement.

En outre, le calcul en binaire doit se faire avec la main face camera, et non de dos comme on le fait généralement lorsque l'on apprend à compter en binaire. Ce choix d'implémentation était plus facile pour moi. De plus, j'ai décidé de ne pas inverser la valeur des doigts mais de conserver les valeurs que l'on connaît (pouce = 1, auriculaire = 16) pour ne pas "tromper" quelqu'un qui apprendrait à compter ainsi.

A l'avenir, j'implémenterai certainement le calcul sur deux mains.

### Position des doigts

Le moment le plus important est celui-ci :

```python
def fingers_raised(fingers):
    return [fingers[4][1] < fingers[3][1], #true if thumb is open
            fingers[8][2] < fingers[6][2], #true if index is open
            fingers[12][2] < fingers[10][2], #true if middle finger is open
            fingers[16][2] < fingers[14][2], #true if ring finger is open
            fingers[20][2] < fingers[18][2] #true if little finger is open
            ]
```

Ce code réside sur le schéma suivant :

<img src="./img/hand_landmarks.png" alt="Description d'une main" style="magin: auto;"/>

Analysons-le ensemble :
- tout d'abord, le pouce est un cas particulier, qui se ferme horizontalement. C'est la raison pour laquelle on cherche à comparer la composante horizontale du bout du pouce par rapport au milieu du doigt.
- Pour les autres doigts, on cherche à vérifier que le milieu du doigt est au-dessus de son extrémité.

### Calcul en binaire

Le calcul en binaire est tout simplement 2 ** int(le doigt i est levé)

## Comment tester ?

### Récupération des sources

* Depuis l'invité de commandes (HTTP):
```bash
$ git clone https://github.com/jeunotca/binary-finger-counting-mediapipe.git
$ cd binary-finger-counting-mediapipe
```

### Dépendances

Ce programme a été réalisé à l'aide de :
- [Mediapipe](https://github.com/google/mediapipe)

Vous pouvez installer les dépendances avec :
```bash
pip install -r requirements.txt
```

### Exécution

```bash
python main.py
```

Appuyer sur ESC pour quitter, et sur SPACE pour changer de mode de calcul :)
