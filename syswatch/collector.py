import platform
import psutil
from datetime import datetime

def collecter_info_systeme():
    """Retourne un dictionnaire avec les infos système"""
    return {
        'os': platform.system(),
        'version': platform.version(),
        'architecture': platform.machine(),
        'hostname': platform.node()
    }

def collecter_cpu():
    """Retourne un dictionnaire avec les infos CPU"""
    return {
        'coeurs_physiques': psutil.cpu_count(logical=False),
        'coeurs_logiques': psutil.cpu_count(logical=True),
        'utilisation': psutil.cpu_percent(interval=1)
    }

def collecter_memoire():
    """Retourne un dictionnaire avec les infos mémoire"""
    mem = psutil.virtual_memory()
    return {
        'total': mem.total,
        'disponible': mem.available,
        'pourcentage': mem.percent
    }

def collecter_disques():
    """Retourne une liste de dictionnaires pour chaque partition"""
    partitions = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            partitions.append({
                'point_montage': part.mountpoint,
                'total': usage.total,
                'utilise': usage.used,
                'pourcentage': usage.percent
            })
        except PermissionError:
            continue  # Ignore les partitions inaccessibles
    return partitions

def collecter_tout():
    """Retourne toutes les infos dans un dictionnaire global"""
    return {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'systeme': collecter_info_systeme(),
        'cpu': collecter_cpu(),
        'memoire': collecter_memoire(),
        'disques': collecter_disques()
    }