
prix = float(input("Veuillez entrer un prix en dinars (ex: 12.45) : "))


dinars = int(prix)
centimes = int(round((prix - dinars) * 100))


print(f"Partie en dinars : {dinars}")
print(f"Partie en centimes : {centimes}")
