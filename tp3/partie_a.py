
# Partie A : Classe de base

class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
        self.emprunteur = None

    def afficher(self):
        if self.disponible:
            etat = "Disponible"
        else:
            etat = f"Emprunté par {self.emprunteur}"

        print(f"{self.titre} - {self.auteur} ({self.annee}) - {etat}")

    def emprunter(self, nom):
        if not self.disponible:
            return False

        self.disponible = False
        self.emprunteur = nom
        return True

    def rendre(self):
        if self.disponible:
            return False

        self.disponible = True
        self.emprunteur = None
        return True


class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []

    def emprunter_livre(self, livre):
        if livre.emprunter(self.nom):
            self.emprunts.append(livre)
            return True

        return False

    def rendre_livre(self, livre):
        if livre not in self.emprunts:
            return False

        if livre.emprunteur != self.nom:
            return False

        if livre.rendre():
            self.emprunts.remove(livre)
            return True

        return False

    def afficher_emprunts(self):
        if not self.emprunts:
            print(f"{self.nom} n'a aucun emprunt.")
            return

        print(f"Emprunts de {self.nom} :")

        for livre in self.emprunts:
            print(f"- {livre.titre}")
