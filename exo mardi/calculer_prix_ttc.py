def calculer_prix_ttc(prix_ht, tva=20):
        """calculer le prix avec la tva """
        return float(round(prix_ht *(1 + tva/100),2))


print("Le prix avec la TVA est :", calculer_prix_ttc(55),"euros")