# Partie B - Mini-jeu « Devine le nombre »

import random

# Choix des brones de jeux.
# L'utilisateur choisit la valeur minimale et maximale entre lesquelles le nombre secret sera choisi.

borne_min = int(input("Borne minimale : "))
borne_max = int(input("Borne maximale : "))


# Bonus : la variable rejouer permet de contrôler la rejouabilité du jeu.
# Tant que sa valeur est "oui", une nouvelle partie commence.

rejouer = "oui"

while rejouer == "oui":

    # Génère aléatoirement un nombre entier compris entre la borne minimale et la borne maximale.
    nombre_secret = random.randint(borne_min, borne_max)

    print(f"\nDevinez le nombre entre {borne_min} et {borne_max} !")

    # La boucle permet au joueur de faire au maximum 10 essais.
    for i in range(10):

        # Demande une proposition au joueur.
        nombre = int(input("Proposez un nombre : "))

        # Si le nombre proposé est inférieur au nombre secret.
        if nombre < nombre_secret:
            print("Trop petit")

        # Si le nombre proposé est supérieur au nombre secret.
        elif nombre > nombre_secret:
            print("Trop grand")

        # Si aucune des conditions précédentes n'est vraie, cela signifie que le joueur a trouvé le nombre.
        else:
            print("Gagné !")

            # Arrête immédiatement la boucle des essais.
            break

    # Le cas où l'utilisateur n'a pas trouvé le nombre secret, alors ce dernier lui est révéler.
    else:
        print("Perdu ! Le nombre secret était :", nombre_secret)

    # Demande au joueur s'il souhaite commencer une nouvelle partie.
    rejouer = input("Voulez-vous rejouer ? (oui/non) : ").lower # le .lower permet d'accepeter les "OUI", "Oui", "oUi", etc.

# Fin du programme
print("Merci d'avoir joué !")