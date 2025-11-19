def est_mot_de_passe_valide(mot):
    """verifie si le mot de passe est correct 

    Args:
        mot (stt): _description_


    """
    longueur_ok = len(mot) >= 8
    chiffre_ok = False
    maj_ok = False

    for c in mot:
        
        if c >= "0" and c <= "9":
            chiffre_ok = True

        
        if c >= "A" and c <= "Z":
            maj_ok = True

   
    return longueur_ok and chiffre_ok and maj_ok



print(est_mot_de_passe_valide("MdP12345"))  
print(est_mot_de_passe_valide("ab123456"))  
print(est_mot_de_passe_valide("ABCDEFGH"))  
