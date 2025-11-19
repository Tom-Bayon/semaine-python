def afficher_liste(courses):
    """
    Affiche la liste de courses

    Paramètre:
        courses (list): La liste des articles
    """
    if len(courses) == 0:
        print(" La liste de courses est vide")
        return

    print(" Liste de courses :")
    print("=" * 40)
    for i, article in enumerate(courses, 1):
        print(f"  {i}. {article}")
    print("=" * 40)
    print(f"Total : {len(courses)} article(s)")


def ajouter_article(courses, article):
    """
    Ajoute un article à la liste de courses

    Paramètres:
        courses (list): La liste des articles
        article (str): L'article à ajouter

    Retourne:
        list: La liste modifiée
    """
    # Vérification que l'article n'est pas vide
    if not article or article.strip() == "":
        print("Erreur : l'article ne peut pas être vide")
        return courses

    # Vérification que l'article n'est pas déjà dans la liste
    if article in courses:
        print(f"  '{article}' est déjà dans la liste")
        return courses

    courses.append(article)
    print(f"✓ '{article}' ajouté à la liste")
    return courses


def retirer_article(courses, article):
    """
    Retire un article de la liste de courses

    Paramètres:
        courses (list): La liste des articles
        article (str): L'article à retirer

    Retourne:
        list: La liste modifiée
    """
    if article in courses:
        courses.remove(article)
        print(f" '{article}' retiré de la liste")
    else:
        print(f" '{article}' n'est pas dans la liste")

    return courses


def compter_articles(courses):
    """
    Compte le nombre d'articles dans la liste

    Paramètre:
        courses (list): La liste des articles

    Retourne:
        int: Le nombre d'articles
    """
    return len(courses)


# Programme principal
def main():
    """Fonction principale du programme"""
    # Initialisation de la liste
    ma_liste_courses = []

    print("Bienvenue dans le gestionnaire de liste de courses !")
    print()

    # Ajout d'articles
    ajouter_article(ma_liste_courses, "Pain")
    ajouter_article(ma_liste_courses, "Lait")
    ajouter_article(ma_liste_courses, "Œufs")
    ajouter_article(ma_liste_courses, "Beurre")
    print()

    # Affichage de la liste
    afficher_liste(ma_liste_courses)
    print()

    # Tentative d'ajout d'un doublon
    ajouter_article(ma_liste_courses, "Pain")
    print()

    # Retrait d'un article
    retirer_article(ma_liste_courses, "Lait")
    print()

    # Affichage de la liste mise à jour
    afficher_liste(ma_liste_courses)
    print()

    # Comptage
    nb_articles = compter_articles(ma_liste_courses)
    print(f"Vous avez {nb_articles} article(s) dans votre liste")


# Lancement du programme
if __name__ == "__main__":
    main()