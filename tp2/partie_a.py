# Partie A : classe Grille pour le jeu du Morpion


class Grille:
    """
    Représente une grille de Morpion 3x3.
    """

    def __init__(self):
        # Grille 3x3 : liste de 3 lignes, chaque ligne contient 3 cases
        # Une case vide est représentée par une chaîne vide ""
        self.cases = [["" for _ in range(3)] for _ in range(3)]

    def afficher(self):
        """
        Affiche la grille de façon lisible dans le terminal.
        """
        for i, ligne in enumerate(self.cases):
            # On remplace les cases vides par un espace pour l'affichage
            affichage = [c if c != "" else " " for c in ligne]
            print(" " + " | ".join(affichage))
            # On trace un séparateur entre les lignes (pas après la dernière)
            if i < 2:
                print("-----------")

    def jouer(self, x, y, joueur):
        """
        Place le symbole du joueur ("X" ou "O") en (x, y) si la case est libre.
        Renvoie True si le coup a été joué, False sinon.
        """
        # Vérification : les coordonnées doivent être dans la grille
        if not (0 <= x < 3 and 0 <= y < 3):
            print("Coup refusé : hors grille.")
            return False
        # Vérification : la case doit être libre
        if self.cases[x][y] != "":
            print("Coup refusé : case occupée.")
            return False
        # Le coup est valide : on place le symbole
        self.cases[x][y] = joueur
        return True

    def est_gagnant(self, j):
        """
        Renvoie True si le joueur j a aligné 3 symboles.
        """
        # Test des lignes et des colonnes
        for i in range(3):
            if all(self.cases[i][k] == j for k in range(3)):  # ligne i
                return True
            if all(self.cases[k][i] == j for k in range(3)):  # colonne i
                return True
        # Test de la diagonale principale
        if all(self.cases[k][k] == j for k in range(3)):
            return True
        # Test de la diagonale secondaire
        if all(self.cases[k][2 - k] == j for k in range(3)):
            return True
        return False

    def est_plein(self):
        """
        Renvoie True si aucune case n'est libre.
        """
        # On vérifie qu'aucune ligne ne contient de case vide
        return all(c != "" for ligne in self.cases for c in ligne)


# Jeu d'essai
if __name__ == "__main__":
    g = Grille()
    g.jouer(0, 0, "X")
    g.jouer(0, 1, "O")
    g.jouer(1, 1, "X")
    g.afficher()

    g.jouer(0, 0, "O")  # refusé : case occupée
    g.jouer(3, 0, "O")  # refusé : hors grille

    print(g.est_gagnant("X"))  # False
    g.jouer(2, 2, "X")
    print(g.est_gagnant("X"))  # True (diagonale)