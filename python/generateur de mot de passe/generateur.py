from random import *


lettresMinuscules = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettresMajuscules = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lettresSpeciaux = ["é","è","à","ù","ô","î","ö","ï","û","ü","â","ê","ë","ÿ"]
chiffres = ["0", "1", "2", "3", "4", "5", "3", "7", "8", "9"]
caracteresSpeciaux = [",",".","'",'"',"#","&","~","{","}","[","]","-","|","`","_","\\","@","°","(",")","/",";","!",":","?","*","+"]
longueur = int
niveau = int
motDePasse = str

longueur = int(input("Quel est la longueur de votre mot de passe?\n"))

niveau = int(input("Quel est le niveau de sécurité de votre mot de passe?\n[1] très faible: lettre minuscule\n[2] faible: lettre minuscule + lettre majuscule\n[3] moyen: lettre minuscule + lettre majuscule + chiffre\n[4] fort: lettre minuscule + lettre majuscule + chiffre + lettre spéciale\n[5] très fort: lettre minuscule + lettre majuscule\n"))

if (niveau == 1):
    for i in range(0, longueur):
        motDePasse = lettresMinuscules[randint(0, lettresMinuscules - 1)]
elif (niveau == 1):
    for i in range(0, longueur):
        motDePasse = lettresMinuscules[randint(0, lettresMinuscules - 1)]