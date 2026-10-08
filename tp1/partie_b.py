# Partie B - Mini-jeu « Devine le nombre »

import random


# Choix des bornes du jeu

borne_min = int(input("Borne minimale : "))
borne_max = int(input("Borne maximale : "))


# BONUS : Gestion de la rejouabilité

rejouer = "oui"

while rejouer == "oui":

    # Génère un nombre secret entre les deux bornes

    nombre_secret = random.randint(borne_min, borne_max)

    print(f"\nDevinez le nombre entre {borne_min} et {borne_max} !")


    # Gestion des essais

    for i in range(10):

        nombre = int(input("Proposez un nombre : "))

        if nombre < nombre_secret:
            print("Trop petit")

        elif nombre > nombre_secret:
            print("Trop grand")

        else:
            print("Gagné !")
            break

    else:
        print("Perdu ! Le nombre secret était :", nombre_secret)


    # Demande si le joueur souhaite rejouer

    rejouer = input("Voulez-vous rejouer ? (oui/non) : ").strip().lower()


# Fin du programme

print("Merci d'avoir joué !")
