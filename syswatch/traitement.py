import csv

def calculer_moyennes(fichier_csv):
    """
    Lit le CSV et calcule les moyennes, min et max du CPU et de la mémoire.
    Les colonnes attendues dans le CSV : cpu_utilisation, mem_pourcentage
    """
    cpu_list = []
    mem_list = []

    with open(fichier_csv, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cpu_list.append(float(row['cpu_utilisation']))
            mem_list.append(float(row['mem_pourcentage']))

    if not cpu_list:
        return None

    return {
        'cpu': {
            'moyenne': sum(cpu_list)/len(cpu_list),
            'min': min(cpu_list),
            'max': max(cpu_list)
        },
        'mem': {
            'moyenne': sum(mem_list)/len(mem_list),
            'min': min(mem_list),
            'max': max(mem_list)
        }
    }


def detecter_pics(fichier_csv, seuil_cpu, seuil_mem):
    """
    Retourne une liste des moments où CPU > seuil_cpu ou MEM > seuil_mem
    """
    pics = []

    with open(fichier_csv, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cpu = float(row['cpu_utilisation'])
            mem = float(row['mem_pourcentage'])
            if cpu > seuil_cpu or mem > seuil_mem:
                pics.append({
                    'timestamp': row['timestamp'],
                    'cpu_utilisation': cpu,
                    'mem_pourcentage': mem
                })

    return pics
