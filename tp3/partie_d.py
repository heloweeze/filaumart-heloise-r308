# Partie D : Programme principal

from pathlib import Path

from partie_a import Livre, Utilisateur
from partie_b import Bibliotheque
from partie_c import sauvegarder_csv, charger_csv


def afficher_menu():
    print("\n========== BIBLIOTHÈQUE ==========")
    print("1. Ajouter un livre")
    print("2. Ajouter un utilisateur")
    print("3. Emprunter un livre")
    print("4. Rendre un livre")
    print("5. Afficher les livres")
    print("6. Quitter et sauvegarder")
    print("7. Afficher les statistiques")
    print("==================================")


def ajouter_livre_menu(bibliotheque):
    titre = input("Titre du livre : ").strip()
    auteur = input("Auteur du livre : ").strip()

    if not titre or not auteur:
        print("Le titre et l'auteur sont obligatoires.")
        return

    try:
        annee = int(input("Année de publication : "))
    except ValueError:
        print("Erreur : l'année doit être un nombre.")
        return

    livre = Livre(titre, auteur, annee)

    if bibliotheque.ajouter_livre(livre):
        print("Livre ajouté avec succès.")
    else:
        print("Ce livre existe déjà.")


def ajouter_utilisateur_menu(bibliotheque):
    nom = input("Nom de l'utilisateur : ").strip()

    if not nom:
        print("Le nom est obligatoire.")
        return

    utilisateur = Utilisateur(nom)

    if bibliotheque.ajouter_utilisateur(utilisateur):
        print("Utilisateur ajouté avec succès.")
    else:
        print("Cet utilisateur existe déjà.")


def emprunter_menu(bibliotheque):
    nom = input("Nom de l'utilisateur : ").strip()
    titre = input("Titre du livre : ").strip()

    if bibliotheque.emprunter(nom, titre):
        print(f"{nom} a emprunté le livre {titre}.")
    else:
        print("Emprunt impossible : vérifiez le nom et le titre, ou la disponibilité du livre.")


def rendre_menu(bibliotheque):
    nom = input("Nom de l'utilisateur : ").strip()
    titre = input("Titre du livre : ").strip()

    if bibliotheque.rendre(nom, titre):
        print(f"{nom} a rendu le livre {titre}.")
    else:
        print("Impossible de rendre ce livre.")


def afficher_statistiques(bibliotheque):
    statistiques = bibliotheque.stats()

    print("\n========== STATISTIQUES ==========")
    print("Nombre total de livres :", statistiques["total"])
    print("Nombre de livres empruntés :", statistiques["empruntes"])
    print("Emprunts par utilisateur :")

    for nom, nombre in statistiques["par_utilisateur"].items():
        print(f"- {nom} : {nombre}")

    print("==================================")


def main():
    chemin_csv = Path(__file__).with_name("livres.csv")

    bibliotheque = charger_csv(chemin_csv)

    print("Bienvenue dans votre bibliothèque !")

    while True:
        afficher_menu()

        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_livre_menu(bibliotheque)

        elif choix == "2":
            ajouter_utilisateur_menu(bibliotheque)

        elif choix == "3":
            emprunter_menu(bibliotheque)

        elif choix == "4":
            rendre_menu(bibliotheque)

        elif choix == "5":
            bibliotheque.afficher_livres()

        elif choix == "6":
            sauvegarder_csv(bibliotheque, chemin_csv)
            print("Bibliothèque sauvegardée. Au revoir !")
            break

        elif choix == "7":
            afficher_statistiques(bibliotheque)

        else:
            print("Choix invalide. Veuillez choisir entre 1 et 7.")


if __name__ == "__main__":
    main()
