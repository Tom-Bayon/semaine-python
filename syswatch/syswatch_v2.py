from collector import collecter_tout


def octets_vers_go(octets):
    """Convertit des octets en Go avec 2 décimales"""
    return f"{octets / (1024**3):.2f} GB"


def afficher_systeme(systeme_info):
    """
    Affiche les informations système contenues dans systeme_info
    """
    print("=== Système ===")
    print(f"OS: {systeme_info['os_nom']}")
    print(f"Version: {systeme_info['version_os']}")
    print(f"Architecture: {systeme_info['architecture']}")
    print(f"Nom de la machine: {systeme_info['nom_machine']}\n")

def afficher_cpu(cpu_info):
    """
    Affiche les informations CPU contenues dans cpu_info
    """
    print("=== CPU ===")
    print(f"Cœurs physiques: {cpu_info['coeurs_physiques']}")
    print(f"Cœurs logiques: {cpu_info['coeurs_logiques']}")
    print(f"Utilisation: {cpu_info['utilisation']:.2f}%\n")

def afficher_memoire(mem_info):
    """
    Affiche les informations mémoire contenues dans mem_info
    """
    print("=== Mémoire ===")
    print(f"Total: {octets_vers_go(mem_info['total_octets'])}")
    print(f"Disponible: {octets_vers_go(mem_info['disponible_octets'])}")
    print(f"Utilisation: {mem_info['pourcentage']:.2f}%\n")

def afficher_disques(disques):
    """
    Affiche les informations des partitions disques
    """
    print("=== Disques ===")
    for d in disques:
        print(f"{d['nom_partition']} : {d['pourcentage']:.2f}% utilisé")
    print()

if __name__ == "__main__":
    
    print("=== SysWatch v2.0 ===\n")

    data = collecter_tout()

    print(f"La date et l'heure est : {data['timestamp']}\n")

    afficher_systeme(data['systeme'])
    afficher_cpu(data['cpu'])
    afficher_memoire(data['memoire'])
    afficher_disques(data['disques'])
     
     