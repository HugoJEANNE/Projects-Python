
# Abase (aire de la base) d'un cercle = pi * R²
# volume d'un cylindre = (Abase * h)

from random import _pi

# Recuperation des données
unite = input("Entrez l'unité de vos données (en cm, m, dm...) : ")
R = input("Entrez le rayon de la base du cylindre (diamètre/2) : ")
h = input("Entrez la hauteur du cylindre : ")

# Calcul
result = (_pi * int(R) * int(R) * int(h))

# Affichage du resultat
print("Le volume du cylindre est V= {} {}³".format(result, unite))

