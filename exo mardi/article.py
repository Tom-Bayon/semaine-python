def afficher_liste(courses):
    for article in courses:
        print(article)

def ajouter_article(courses, article):
    courses.append(article)

def retirer_article(courses, article):
    if article in courses:
        courses.remove(article)

def compter_articles(courses):
    return len(courses)



ma_liste = []


ajouter_article(ma_liste, "pomme")
print("Après ajout  :", ma_liste)


ajouter_article(ma_liste, "lait")
print("Après ajout   :", ma_liste)


ajouter_article(ma_liste, "pain")
print("Après ajout   :", ma_liste)


retirer_article(ma_liste, "lait")
print("Après suppression  :", ma_liste)


print("Nombre d'articles :", compter_articles(ma_liste))

