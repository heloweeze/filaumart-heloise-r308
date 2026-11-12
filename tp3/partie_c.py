# Partie C : Persistance des données

import csv
from pathlib import Path

from partie_a import Livre, Utilisateur
from partie_b import Bibliotheque


def sauvegarder_csv(bibliotheque, chemin):
    chemin = Path(chemin)

    with chemin.open("w", newline="", encoding="utf-8") as fichier:
        champs = [
            "titre",
            "auteur",
            "annee",
            "disponible",
            "emprunteur"
        ]

        writer = csv.DictWriter(fichier, fieldnames=champs)
        writer.writeheader()

        for livre in bibliotheque.livres.values():
            writer.writerow({
                "titre": livre.titre,
                "auteur": livre.auteur,
                "annee": livre.annee,
                "disponible": livre.disponible,
                "emprunteur": livre.emprunteur or ""
            })


def charger_csv(chemin):
    bibliotheque = Bibliotheque()
    chemin = Path(chemin)

    if not chemin.exists():
        return bibliotheque

    with chemin.open("r", newline="", encoding="utf-8") as fichier:
        reader = csv.DictReader(fichier)

        for ligne in reader:
            try:
                titre = ligne["titre"]
                auteur = ligne["auteur"]
                annee = int(ligne["annee"])
                disponible = ligne["disponible"].strip().lower() == "true"
                emprunteur = ligne.get("emprunteur", "").strip()

                livre = Livre(titre, auteur, annee)
                livre.disponible = disponible

                if emprunteur:
                    livre.disponible = False
                    livre.emprunteur = emprunteur

                    if emprunteur not in bibliotheque.utilisateurs:
                        utilisateur = Utilisateur(emprunteur)
                        bibliotheque.ajouter_utilisateur(utilisateur)

                    utilisateur = bibliotheque.utilisateurs[emprunteur]
                    utilisateur.emprunts.append(livre)

                bibliotheque.ajouter_livre(livre)

            except (ValueError, KeyError, TypeError):
                print("Une ligne invalide a été ignorée.")

    return bibliotheque
