import csv 

def calculer_moyennes(fichier_csv):
    """ Lit le CSV et calcule CPU et mémoire : moyenne, min, max
    """
    cpu_list = []
    mem_list = []

    with open(fichier_csv, newline = '') as f :
        reader = csv.DictReader(f)
        for row in reader:
            cpu_list.append(float(row['cpu_percent']))
            mem_list.append(float(row['mem_percent']))

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
    Retourne les moments où CPU > seuil_cpu ou mémoire > seuil_mem
    """
    pics = []
    with open(fichier_csv, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cpu = float(row['cpu_percent'])
            mem = float(row['mem_percent'])
            if cpu > seuil_cpu or mem > seuil_mem:
                pics.append({
                    'le jour est l heure est :': row['timestamp'],
                    'cpu_percent': cpu,
                    'mem_percent': mem
                })
    return pics