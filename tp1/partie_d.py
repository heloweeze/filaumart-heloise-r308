# Partie D - Jeu du Pendu

import random


# Liste des mots disponibles

mots = ["papillon", "bonjour", "voiture", "poulet", "python"]


# Choix du mot

def choisir_mot(liste):
    """
    Choisit un mot au hasard dans une liste et le renvoie en majuscules.

    Paramètre :
        liste (list) : liste des mots disponibles.

    Retourne :
        str : mot choisi aléatoirement en majuscules.
    """

    # random.choice() choisit un élément au hasard dans la liste.
    # upper() transforme le mot en majuscules.
    return random.choice(liste).upper()


# Création du masque

def creer_masque(mot):
    """
    Crée un masque composé de "_" pour chaque lettre du mot.

    Paramètre :
        mot (str) : mot à masquer.

    Retourne :
        list : liste de "_" de même longueur que le mot.
    """

    # len() donne le nombre de caractères du mot.
    return ["_"] * len(mot)


# Initialisation de la partie

mot_secret = choisir_mot(mots)
masque = creer_masque(mot_secret)

erreurs = 0
lettres_proposees = []


# Boucle du jeu

while erreurs < 7 and "_" in masque:

    print("\nMot :", " ".join(masque))
    print("Erreurs :", erreurs, "/ 7")
    print("Lettres proposées :", ", ".join(lettres_proposees))

    lettre = input("Proposez une lettre : ").strip().upper()

    # strip() supprime les espaces avant et après le texte.
    # upper() transforme la lettre en majuscule.

    # isalpha() vérifie que le texte contient uniquement des lettres.
    # len() vérifie ici que le joueur a entré une seule lettre.
    if len(lettre) != 1 or not lettre.isalpha():
        print("Veuillez entrer une seule lettre.")
        continue

    # Vérifie si la lettre a déjà été proposée.
    if lettre in lettres_proposees:
        print("Vous avez déjà proposé cette lettre.")
        continue

    lettres_proposees.append(lettre)

    # Vérifie si la lettre existe dans le mot secret.
    if lettre in mot_secret:

        for i in range(len(mot_secret)):
            if mot_secret[i] == lettre:
                masque[i] = lettre

        print("Bonne lettre !")

    else:
        erreurs += 1
        print("Lettre absente !")


# Fin de la partie

if "_" not in masque:
    print("\nGagné ! Le mot était :", mot_secret)
else:
    print("\nPerdu ! Le mot était :", mot_secret)
