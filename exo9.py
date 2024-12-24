
villes = []

while True:
    ville = input("Veuillez entrer le nom d'une ville (ou tapez 'stop' pour terminer) : ")

    if ville.lower() == "stop":
        break
    

    population = len(ville) * 1000000
    

    villes.append((ville, population))


villes.sort(key=lambda x: x[1], reverse=True)


print("\nVilles et leurs populations (triées par ordre décroissant de population) :")
for ville, population in villes:
    print(f"{ville}: {population:,} citoyens")
