from verbeConjuguer import *


texte = ""
for i in table:
    x = 0
    for j in i:
        if x == 0:
            x = 1
            Verbe = j
            continue
        texte += "\"" + j + "\": \"" + Verbe + "\",\n"





fichier = open("verbeConjuguer1.txt", "w+", encoding="utf-8")
fichier.write(str(texte))
fichier.close