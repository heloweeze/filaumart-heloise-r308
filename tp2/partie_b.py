# Partie B : classes JoueurHumain et JoueurIA
import random

from partie_a import Grille  # utilisé uniquement pour le jeu d'essai


class JoueurHumain:
    """Joueur qui saisit son coup au clavier."""

    def prochain_coup(self, tab, symbole):
        """Demande à l'utilisateur une ligne et une colonne.
        Renvoie le tuple (x, y). Redemande tant que la saisie n'est pas un nombre.
        (La validité du coup, case libre et dans la grille, est vérifiée par la Grille.)"""
        while True:
            try:
                x = int(input(f"Joueur {symbole} - ligne (0 à 2) : "))
                y = int(input(f"Joueur {symbole} - colonne (0 à 2) : "))
                return (x, y)
            except ValueError:
                # int() échoue si la saisie n'est pas un nombre entier
                print("Saisie invalide : entrez des nombres entiers.")


class JoueurIA:
    """Joueur artificiel qui joue un coup aléatoire."""

    def prochain_coup(self, tab, symbole):
        """Choisit au hasard une case libre. Renvoie le tuple (x, y)."""
        # On liste toutes les cases vides de la grille
        libres = [(x, y) for x in range(3) for y in range(3) if tab[x][y] == ""]
        # random.choice tire une case au hasard parmi les cases libres
        return random.choice(libres)


# Jeu d'essai 
if __name__ == "__main__":
    g = Grille()
    g.jouer(0, 0, "X")

    ia = JoueurIA()
    coup = ia.prochain_coup(g.cases, "O")
    print("L'IA joue :", coup)  # jamais (0, 0), car occupée
    g.jouer(coup[0], coup[1], "O")
    g.afficher()

    humain = JoueurHumain()
    print("Coup saisi :", humain.prochain_coup(g.cases, "X"))