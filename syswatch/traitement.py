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



    
    
