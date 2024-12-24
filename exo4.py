
age_personne1 = int(input("Veuillez entrer l'âge de la première personne : "))
age_personne2 = int(input("Veuillez entrer l'âge de la deuxième personne : "))


if age_personne1 > age_personne2:
    print("La première personne est plus âgée.")
elif age_personne1 < age_personne2:
    print("La deuxième personne est plus âgée.")
else:
    print("Les deux personnes ont le même âge.")
