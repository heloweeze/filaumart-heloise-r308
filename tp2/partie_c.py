# Partie C : jeu complet du Morpion
from partie_a import Grille
from partie_b import JoueurHumain, JoueurIA


def jouer_partie(joueur_x, joueur_o, afficher=True):
    """Joue une partie complète entre deux joueurs.
    Renvoie "X" ou "O" en cas de victoire, None en cas de match nul."""
    grille = Grille()
    # On associe chaque symbole à son joueur
    joueurs = {"X": joueur_x, "O": joueur_o}
    symbole = "X"  # X commence toujours

    while True:
        if afficher:
            grille.afficher()

        # Le joueur courant propose un coup, on redemande tant qu'il est invalide
        while True:
            x, y = joueurs[symbole].prochain_coup(grille.cases, symbole)
            # jouer() renvoie False et affiche un message si le coup est refusé
            if grille.jouer(x, y, symbole):
                break
            # coup invalide : le même joueur rejoue (on reste dans la boucle)

        # Après chaque coup valide, on teste la victoire puis le match nul
        if grille.est_gagnant(symbole):
            if afficher:
                grille.afficher()
                print(f"Le joueur {symbole} gagne !")
            return symbole
        if grille.est_plein():
            if afficher:
                grille.afficher()
                print("Match nul !")
            return None

        # On passe la main à l'autre joueur
        symbole = "O" if symbole == "X" else "X"


def jouer_plusieurs_parties(joueur_x, joueur_o, nombre, afficher=True):
    """Enchaîne plusieurs parties et tient le score. Renvoie le dictionnaire des scores."""
    scores = {"X": 0, "O": 0, "nuls": 0}
    for i in range(nombre):
        gagnant = jouer_partie(joueur_x, joueur_o, afficher)
        # On met à jour le score selon le résultat
        if gagnant is None:
            scores["nuls"] += 1
        else:
            scores[gagnant] += 1
    return scores


# Programme principal
if __name__ == "__main__":
    print("1 : Humain contre IA")
    print("2 : Humain contre Humain")
    print("3 : IA contre IA (20 parties)")
    choix = input("Votre choix : ")

    if choix == "1":
        print(jouer_plusieurs_parties(JoueurHumain(), JoueurIA(), 1))
    elif choix == "2":
        print(jouer_plusieurs_parties(JoueurHumain(), JoueurHumain(), 1))
    elif choix == "3":
        # Pas d'affichage de la grille pour ne montrer que le score final
        print(jouer_plusieurs_parties(JoueurIA(), JoueurIA(), 20, afficher=False))
    else:
        print("Choix invalide.")