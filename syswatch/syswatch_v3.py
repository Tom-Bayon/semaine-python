import sys
import time
import csv
import json
from collector import collecter_tout
from traitement import calculer_moyennes, detecter_pics

# ---------------------------
# Export CSV
# ---------------------------
def exporter_csv(metriques, fichier):
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

# ---------------------------
# Export JSON
# ---------------------------
def exporter_json(metriques, fichier):
    with open(fichier, "w") as f:
        json.dump(metriques, f, indent=2)

# ---------------------------
# Collecte unique
# ---------------------------
def collecte_unique():
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

# ---------------------------
# Collecte continue
# ---------------------------
def collecte_continue(intervalle, nombre):
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

# ---------------------------
# Statistiques et pics
# ---------------------------
def afficher_stats():
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
