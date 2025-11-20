import sys
import time
import csv
import json
from collector import collecter_tout
from traitement import calculer_moyennes, detecter_pics


def exporter_csv(metriques, fichier):
    """ Ajoute une ligne de métriques dans un fichier CSV. 
    Si le fichier n'existe pas, il est créé 

    Args:
        metriques (dict) : dictionnaire contenant les valeurs à écrire, 
        fichier (str) : chemin du fichier CSV à écrire/ajouter
        """

    colonnes = [
        "timestamp",
        "nom_machine",
        "cpu_utilisation",
        "mem_total_octets",
        "mem_disponible_octets",
        "mem_pourcentage",
        "disk_root_pourcentage"
    ]

    try:
        with open(fichier, "x", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=colonnes)
            writer.writeheader()
            writer.writerow(metriques)
    except FileExistsError:
        with open(fichier, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=colonnes)
            writer.writerow(metriques)


def exporter_json(metriques, fichier):
    """Enregistre toutes les métriques dans un fichier JSON.

    Args:
        metriques (dict): Les données complètes collectées
        fichier (str): Le nom du fichier JSON dans lequel sauvegarder les métriques.
    """

    with open(fichier, "w") as f:
        json.dump(metriques, f, indent=2)


def collecte_unique():
    """Effectue une collecte unique des métriques système, affiche les résultats et les exporte.

    """
    data = collecter_tout()

    print("\n=== Collecte unique ===")
    print("Timestamp :", data["timestamp"])
    print("Nom machine :", data["systeme"]["nom_machine"])
    print("CPU :", data["cpu"]["utilisation"], "%")
    print("Mémoire :", data["memoire"]["pourcentage"], "%")
    print("Disque / :", data["disques"][0]["pourcentage"], "%")

    ligne_csv = {
        "timestamp": data["timestamp"],
        "nom_machine": data["systeme"]["nom_machine"],
        "cpu_utilisation": data["cpu"]["utilisation"],
        "mem_total_octets": data["memoire"]["total_octets"],
        "mem_disponible_octets": data["memoire"]["disponible_octets"],
        "mem_pourcentage": data["memoire"]["pourcentage"],
        "disk_root_pourcentage": data["disques"][0]["pourcentage"]
    }

    exporter_csv(ligne_csv, "historique.csv")
    exporter_json(data, "dernier.json")


def collecte_continue(intervalle, nombre):
    """Collecte les métriques en boucle

    Args:
        intervalle (int): Temps en secondes entre chaque collecte.
        nombre (int): Nombre total de collectes à effectuer.
    """
    compteur = 0
    try:
        while True:
            data = collecter_tout()
            print(f"[{data['timestamp']}] CPU={data['cpu']['utilisation']}% | MEM={data['memoire']['pourcentage']}%")

            exporter_csv({
                "timestamp": data["timestamp"],
                "nom_machine": data["systeme"]["nom_machine"],
                "cpu_utilisation": data["cpu"]["utilisation"],
                "mem_total_octets": data["memoire"]["total_octets"],
                "mem_disponible_octets": data["memoire"]["disponible_octets"],
                "mem_pourcentage": data["memoire"]["pourcentage"],
                "disk_root_pourcentage": data["disques"][0]["pourcentage"]
            }, "historique.csv")

            exporter_json(data, "dernier.json")

            compteur += 1
            if nombre != 0 and compteur >= nombre:
                break

            time.sleep(intervalle)
    except KeyboardInterrupt:
        print("\nArrêt manuel par l'utilisateur !")


def afficher_stats():
    """Statistiques et pics"""
    stats = calculer_moyennes("historique.csv")
    if stats is None:
        print("Aucune donnée dans le CSV !")
        return

    print("\n=== STATISTIQUES ===")
    print(f"CPU : moy={stats['cpu']['moyenne']:.2f}  min={stats['cpu']['min']}  max={stats['cpu']['max']}")
    print(f"MEM : moy={stats['mem']['moyenne']:.2f}  min={stats['mem']['min']}  max={stats['mem']['max']}")

    print("\n=== PICS DÉTECTÉS (CPU>80 ou MEM>85) ===")
    pics = detecter_pics("historique.csv", seuil_cpu=80, seuil_mem=85)
    if not pics:
        print("Aucun pic détecté.")
    else:
        for p in pics:
            print(p)

# ---------------------------
# Programme principal
# ---------------------------
if __name__ == "__main__":
    if len(sys.argv) == 1:
        collecte_unique()
        sys.exit()

    if "--continu" in sys.argv:
        intervalle = 5
        nombre = 0
        if "--intervalle" in sys.argv:
            intervalle = int(sys.argv[sys.argv.index("--intervalle") + 1])
        if "--nombre" in sys.argv:
            nombre = int(sys.argv[sys.argv.index("--nombre") + 1])
        collecte_continue(intervalle, nombre)
        sys.exit()

    if "--stats" in sys.argv:
        afficher_stats()
        sys.exit()
