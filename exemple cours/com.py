nombre = int("abc")

try:
    nombre = int("abc")
    print("conversion réussie")
except ValueError:
    print("Erreur: impossible de convertir ")
    nombre = 0

print("Le programme continue...")