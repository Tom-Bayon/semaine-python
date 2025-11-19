import platform
import psutil
from datetime import datetime

def collecter_info_systeme():
    """
    Retourne un dictionnaire avec les infos système
    """
    return {
        'os_nom': platform.system(),
        'version_os': platform.version(),
        'archi': platform.machine(),
        'nom_machine': platform.node()
    }

def collecter_cpu():
    """
    Retourne un dictionnaire avec infos CPU
    """
    return {
        'coeurs_physiques': psutil.cpu_count(logical=False),
        'coeurs_logiques': psutil.cpu_count(logical=True),
        'utilisation': psutil.cpu_percent(interval=1)
    }

def collecter_memoire():
    """
    Retourne un dictionnaire avec infos mémoire
    """
    mem = psutil.virtual_memory()
    return {
        'total_octets': mem.total,
        'disponible_octets': mem.available,
        'pourcentage': mem.percent
    }

def collecter_disques():
    """
    Retourne une liste de dictionnaires pour chaque partition
    """
    partitions = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            partitions.append({
                'nom_partition': part.mountpoint,
                'total_octets': usage.total,
                'utilise_octets': usage.used,
                'pourcentage': usage.percent
            })
        except PermissionError:
            continue
    return partitions

def collecter_tout():
    """
    Retourne un dictionnaire global avec toutes les métriques
    """
    return {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'systeme': collecter_info_systeme(),
        'cpu': collecter_cpu(),
        'memoire': collecter_memoire(),
        'disques': collecter_disques()
    }
