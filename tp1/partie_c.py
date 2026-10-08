# Partie C - Manipulation des mots

import random

mots = ["papillon", "bonjour", "voiture", "poulet"]

def choisir_mot(mots):
    """
    Choisit un mot au hasard dans la liste et le renvoie en majuscules.

    mots : liste de mots disponibles
    """
    mot = random.choice(mots)

    # Renvoie le mot en majuscules grâce à .upper()
    return mot.upper() 

def masque(mot):
    """
    Crée et retourne un masque composé de caractères "_",
    avec autant de "_" que le mot contient de caractères.

    mot : mot dont on veut créer le masque.
    """

    return ["_"] * len(mot)

print(choisir_mot(mots))
print(masque("POULET"))