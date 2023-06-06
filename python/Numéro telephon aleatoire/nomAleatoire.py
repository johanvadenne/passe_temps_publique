import random

#saisie
nombreDeNumero = int(input("Combien de numero voulez-vous?\n"))

#tableau
prefixe = ["06", "07"]
tableauNum = []

#nombre aléatoire
for i in range(nombreDeNumero):
    
    #choisie un préfixe aléatoire
    preRandom = random.choice(prefixe)
    
    #choisie un numéro aléatoire
    numRandom = random.randint(0, 99999999)
    numRandom = str(preRandom) + str(numRandom).zfill(8)
    
    #rajoute dans le tableau
    tableauNum.append(numRandom)
    
    print (numRandom)

#j'écrie dans un fichier texte
fichier = open("mesNuméros.txt", "w+", encoding="utf-8")
for i in tableauNum:
    fichier.write(i + "\n")
fichier.close()