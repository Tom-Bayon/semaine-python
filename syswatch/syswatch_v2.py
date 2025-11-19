from collector import collecter_tout


def octets_vers_go(octets):
    """Convertit des octets en Go avec 2 décimales"""
    return f"{octets / (1024**3):.2f} GB"

def afficher_systeme(data):
    """
    Affiche les informations système contenues dans le dictionnaire 'data'
    """
    print("=== Système ===")
    print(f"OS: {data['os']}")                
    print(f"Version: {data['version']}")      
    print(f"Architecture: {data['architecture']}")  
    print(f"Hostname: {data['hostname']}\n")  

def afficher_cpu(data):
    """
    Affiche les informations CPU contenues dans le dictionnaire 'data'
    """
    print("=== CPU ===")
    print(f"Cœurs physiques: {data['coeurs_physiques']}")  
    print(f"Cœurs logiques: {data['coeurs_logiques']}")    
    print(f"Utilisation: {data['utilisation']:.2f}%\n")

def afficher_memoire(data):
    """Affiche les informations mémoire contenues dans le dictionnaire 'data'
    """
    print("=== Mémoire ===")
    print(f"Total: {octets_vers_go(data['total'])}")      
    print(f"Disponible: {octets_vers_go(data['disponible'])}") 
    print(f"Utilisation: {data['pourcentage']:.2f}%\n") 

def afficher_disques(disques):
    """
    Affiche les informations des partitions disques
    cette fois disque car on a deja créer un liste de dictionnaire dans collector.py 
    """
    print("=== Disques ===")
    for d in disques:
        print(f"{d['point_montage']} : {d['pourcentage']:.2f}% utilisé")
    print()

if __name__ == "__main__":
    
    print("=== SysWatch v2.0 ===\n")

    data = collecter_tout()

    print(f"La date et l'heure est : {data['timestamp']}\n")

    afficher_systeme(data['systeme'])
    afficher_cpu(data['cpu'])
    afficher_memoire(data['memoire'])
    afficher_disques(data['disques'])
     
     