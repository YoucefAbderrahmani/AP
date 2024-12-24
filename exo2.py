
temperature = int(input("Veuillez entrer la température (en entier) : "))


if temperature < 0:
    print("Il fait très froid !")
elif temperature < 10:
    print("Il fait froid !")
elif temperature < 20:
    print("Il fait frais !")


print("Restez prudent !")
