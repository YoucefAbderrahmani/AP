
total = float(input("Veuillez entrer le montant total de l'achat : "))
nb_articles = int(input("Veuillez entrer le nombre d'articles : "))
jour_semaine = input("Veuillez entrer le jour de la semaine (ex: lundi, mardi, ...): ").lower()


if jour_semaine in ['samedi', 'dimanche']:
    remise = 0.20  
else:
    remise = 0.10  


if nb_articles > 5:
    remise += 0.05  #

prix_final = total * (1 - remise)

print(f"Le prix total après remise est : {prix_final:.2f} €")
