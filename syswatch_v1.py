import platform
import psutil

def afficher_infos_systeme():
    """Affichage des informations système
    """
    print("=== Système ===")
    print(f"OS: {platform.system()}")
    print(f"Version: {platform.version()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Hostname: {platform.node()}")
    print(f"Python: {platform.python_version()}")
    print()

def afficher_infos_cpu():
    """Affichage du CPU
    """
    print("=== CPU ===")
    print(f"Coeurs physiques: {psutil.cpu_count(logical=False)}")
    print(f"Coeurs logiques: {psutil.cpu_count(logical=True)}")
    print(f"Utilisation: {psutil.cpu_percent(interval=1):.2f}%")
    print()

def afficher_infos_memoire():
    """Affichage de la mémoire
    """
    mem = psutil.virtual_memory()
    total_go = mem.total / (1024 ** 3)
    dispo_go = mem.available / (1024 ** 3)

    print("=== Mémoire ===")
    print(f"Total: {total_go:.2f} GB")
    print(f"Disponible: {dispo_go:.2f} GB")
    print(f"Utilisation: {mem.percent:.2f}%")
    print()

def afficher_infos_disques():
    """Affichage des disques
    """
    print("=== Disques ===")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(f"{part.mountpoint} : {usage.percent:.2f}% utilisé")
        except PermissionError:
            print(f"{part.mountpoint} : Permission refusée")
    print()

if __name__ == "__main__":
    print("=== SysWatch v1.0 ===\n")

    afficher_infos_systeme()
    afficher_infos_cpu()
    afficher_infos_memoire()
    afficher_infos_disques()