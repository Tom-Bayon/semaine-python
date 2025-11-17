def calculer_prix_ttc(prix_ht, tva=20):
    return float(round(prix_ht *(1 + tva/100),2))


print(calculer_prix_ttc(55))