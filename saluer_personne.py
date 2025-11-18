def saluer_personne(nom, heure):

    """""Salue une personne selon l'heure de la journée 
    """""
    if 6 <= heure < 12:
        return f"Bonjour {nom}"
    elif 12 <= heure < 18:
        return f"Bon après-midi {nom}"
    elif 18 <= heure < 24:
        return f"Bonsoir {nom}"
    else:
        return f"Bonne nuit {nom}"



print(saluer_personne("Tom", 9))   
print(saluer_personne("Victor", 14))  
print(saluer_personne("Marie", 20))    
print(saluer_personne("Paul", 3))     