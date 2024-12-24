import math


personnes = int(input("Combien de personnes ont besoin d'un trajet ? "))
capacite_taxi = int(input("Combien de personnes peuvent entrer dans un taxi ? "))


taxis_necessaires = math.ceil(personnes / capacite_taxi)


print(f"Il vous faudra {taxis_necessaires} taxis pour transporter {personnes} personnes.")