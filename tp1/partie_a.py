# Partie A - Dictionnaire d'étudiants

# 1. Création du dictionnaire étudiants
etudiants = {} 

etudiants["Alice"] = 12.0
etudiants["Bob"] = 15.0
etudiants["Claire"] = 9.5

# 2.1 Création de ajouter_etudiant

def ajouter_etudiant(d, nom, note):
    """
    Ajoute ou met à jour un étudiant.

    d : dictionnaire des étudiants
    nom : nom de l'étudiant
    note : note de l'étudiant
    """
    d[nom] = note

# ajouter_etudiant(etudiants, "David", 14.0)

# 2.2 Création de moyenne_classe

def moyenne_classe(d):
    """
    Calcule et retourne la moyenne des notes de la classe.
    """

    # gestion du dictionnaire vide
    if not d:
        return None

    # calcul de la somme
    somme = 0

    for note in d.values():
        somme += note

    # calcul de la moyenne
    moyenne = somme / len(d)

    return moyenne

print("La moyenne de classe est :", moyenne_classe(etudiants))

# 2.3 Création de meilleur_etudiant

def meilleur_etudiant(d):
    """
    Recherche et retourne l'étudiant ayant la meilleure note.
    """
    if not d:
        return None

    meilleur_nom = None
    meilleure_note = None

    # Parcourt les étudiants et leurs notes
    for nom, note in d.items(): 
        if meilleure_note is None or note > meilleure_note:
            meilleur_nom = nom
            meilleure_note = note

    return (meilleur_nom, meilleure_note)

print("Le meilleur étudiant de la classe est :", meilleur_etudiant(etudiants))

# 3. Sauvegarde et rechargement dans un fichier texte
with open("etudiants.txt", "w") as f:
    for nom, note in etudiants.items():
        f.write(f"{nom}:{note}\n")

def charger_etudiants():
    """
    Charge les étudiants depuis le fichier texte.
    """
    etudiants_charges = {}

    try:
        with open("etudiants.txt", "r") as f:
            for ligne in f:
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

etudiants_recharges = charger_etudiants()
print("La liste des étudiants rechargés :", etudiants_recharges)