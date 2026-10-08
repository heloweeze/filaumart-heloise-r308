# Partie C - Manipulation des mots

import random


# Liste des mots disponibles

mots = ["papillon", "bonjour", "voiture", "poulet"]


# Choix du mot

def choisir_mot(mots):
    """
    Choisit un mot au hasard dans la liste et le renvoie en majuscules.

    Paramètre :
        mots (list) : liste des mots disponibles.

    Retourne :
        str : mot choisi aléatoirement en majuscules.
    """

    # random.choice() choisit un élément au hasard dans la liste.
    mot = random.choice(mots)

    # upper() transforme le mot en majuscules.
    return mot.upper()


# Création du masque

def masque(mot):
    """
    Crée un masque composé de "_" pour chaque caractère du mot.

    Paramètre :
        mot (str) : mot dont on veut créer le masque.

    Retourne :
        list : liste de "_" de même longueur que le mot.
    """

    # len() donne le nombre de caractères du mot.
    # ["_"] * len(mot) répète "_" autant de fois que nécessaire.
    return ["_"] * len(mot)


# Test des fonctions

print(choisir_mot(mots))
print(masque("POULET"))
