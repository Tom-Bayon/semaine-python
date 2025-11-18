import os

def sauvegarder_liste(courses, chemin_fichier):
    with open(chemin_fichier, "w", encoding="utf-8") as f:
        for article in courses:
            f.write(article + "\n")

def afficher_liste(courses):
    for article in courses:
        print(article)

def ajouter_article(courses, article, chemin_fichier):
    courses.append(article)
    sauvegarder_liste(courses, chemin_fichier)

def retirer_article(courses, article, chemin_fichier):
    if article in courses:
        courses.remove(article)
        sauvegarder_liste(courses, chemin_fichier)

def compter_articles(courses):
    return len(courses)



chemin_dossier = r"C:\Users\bayon\Documents\BAC+3\formation_python"
chemin_fichier = os.path.join(chemin_dossier, "liste_courses.txt")


os.makedirs(chemin_dossier, exist_ok=True)

ma_liste = []

ajouter_article(ma_liste, "pomme", chemin_fichier)
print("Après ajout  :", ma_liste)

ajouter_article(ma_liste, "lait", chemin_fichier)
print("Après ajout   :", ma_liste)

ajouter_article(ma_liste, "pain", chemin_fichier)
print("Après ajout   :", ma_liste)

retirer_article(ma_liste, "lait", chemin_fichier)
print("Après suppression  :", ma_liste)

print("Nombre d'articles :", compter_articles(ma_liste))
