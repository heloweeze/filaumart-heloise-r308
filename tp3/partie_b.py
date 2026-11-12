# Partie B : Gestionnaire de bibliothèque

from partie_a import Livre, Utilisateur


class Bibliotheque:
    def __init__(self):
        self.livres = {}
        self.utilisateurs = {}

    def ajouter_livre(self, livre):
        if livre.titre in self.livres:
            return False

        self.livres[livre.titre] = livre
        return True

    def ajouter_utilisateur(self, utilisateur):
        if utilisateur.nom in self.utilisateurs:
            return False

        self.utilisateurs[utilisateur.nom] = utilisateur
        return True

    def emprunter(self, nom, titre):
        if nom not in self.utilisateurs:
            return False

        if titre not in self.livres:
            return False

        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        return utilisateur.emprunter_livre(livre)

    def rendre(self, nom, titre):
        if nom not in self.utilisateurs:
            return False

        if titre not in self.livres:
            return False

        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        return utilisateur.rendre_livre(livre)

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque ne contient aucun livre.")
            return

        print("\n--- LIVRES DE LA BIBLIOTHÈQUE ---")

        for livre in self.livres.values():
            livre.afficher()

    def stats(self):
        total = len(self.livres)

        empruntes = sum(
            1 for livre in self.livres.values()
            if not livre.disponible
        )

        par_utilisateur = {
            nom: len(utilisateur.emprunts)
            for nom, utilisateur in self.utilisateurs.items()
        }

        return {
            "total": total,
            "empruntes": empruntes,
            "par_utilisateur": par_utilisateur
        }
