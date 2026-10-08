# Partie A - Dictionnaire d'étudiants


# Création du dictionnaire

etudiants = {
    "Alice": 12.0,
    "Bob": 15.0,
    "Claire": 9.5
}


# Gestion des étudiants

def ajouter_etudiant(d, nom, note):
    """
    Ajoute un étudiant au dictionnaire ou met à jour sa note.

    Paramètres :
        d (dict) : dictionnaire des étudiants.
        nom (str) : nom de l'étudiant.
        note (float) : note de l'étudiant.
    """
    d[nom] = note


def moyenne_classe(d):
    """
    Calcule la moyenne des notes de la classe.

    Paramètre :
        d (dict) : dictionnaire contenant les étudiants et leurs notes.

    Retourne :
        float : moyenne des notes.
        None : si le dictionnaire est vide.
    """
    if not d:
        return None

    somme = 0

    for note in d.values():
        somme += note

    return somme / len(d)


def meilleur_etudiant(d):
    """
    Recherche l'étudiant ayant obtenu la meilleure note.

    Paramètre :
        d (dict) : dictionnaire contenant les étudiants et leurs notes.

    Retourne :
        tuple : nom et note du meilleur étudiant.
        None : si le dictionnaire est vide.
    """
    if not d:
        return None

    meilleur_nom = None
    meilleure_note = None

    for nom, note in d.items():
        if meilleure_note is None or note > meilleure_note:
            meilleur_nom = nom
            meilleure_note = note

    return meilleur_nom, meilleure_note


# Affichage des résultats

print("Moyenne de la classe :", moyenne_classe(etudiants))
print("Meilleur étudiant :", meilleur_etudiant(etudiants))


# Sauvegarde dans un fichier texte

with open("etudiants.txt", "w") as fichier:
    for nom, note in etudiants.items():
        fichier.write(f"{nom}:{note}\n")


# Chargement des étudiants depuis le fichier

def charger_etudiants():
    """
    Charge les étudiants enregistrés dans le fichier texte.

    Les lignes mal formées ou contenant une note invalide
    sont ignorées afin d'éviter une erreur du programme.

    Retourne :
        dict : dictionnaire des étudiants chargés.
    """
    etudiants_charges = {}

    try:
        with open("etudiants.txt", "r") as fichier:

            for ligne in fichier:
                ligne = ligne.strip()

                if ":" not in ligne:
                    continue

                nom, note = ligne.split(":", 1)

                try:
                    etudiants_charges[nom] = float(note)

                except ValueError:
                    continue

    except FileNotFoundError:
        print("Le fichier etudiants.txt est introuvable.")

    return etudiants_charges


# Vérification du chargement

etudiants_recharges = charger_etudiants()

print("Étudiants rechargés :", etudiants_recharges)
