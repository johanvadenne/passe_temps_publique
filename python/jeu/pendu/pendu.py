#déclaration variable
pilier = ""
piedPendu = ""
poutre = ""
corde = ""
tete = ""
corp = ""
brasGauche = " "
brasDroit = ""
piedGauche = ""
piedDroit = ""
lettreFauce = ""
pendu = 0
lettreManquante = 0


#saisie mot secret
while True:
    motSecret = input("Qu'elle est le mot à trouver:\n")
    demande = input("Etes vous sûr:\n- oui\n- non\n")
    if demande == "oui":
        break
lettreCacher = len(motSecret)
lettreManquante = lettreCacher
motCacher = ["_"] * lettreCacher

#trouve mot
while True:
    
    lettreTrouver = False
    
    #saisie
    trouveMot = input("lettre fauce: {}\nTrouvé le mot cacher: {}\n".format(lettreFauce, motCacher))
    
    #vérifie
    for i in range(lettreCacher):
        if trouveMot == motSecret[i]:
            motCacher[i] = trouveMot
            lettreManquante -= 1
            lettreTrouver = True

    #si lettre trouvé
    if lettreTrouver:
        print("Trouvé")
        
        #si gagné
        if lettreManquante == 0:
            print("Vous avez gagné\n{}".format(motCacher))
            break
        
        continue
    
    #si lettre pas trouvé
    print("Non")
    lettreFauce += trouveMot + " "
    pendu += 1
    
    #affiiche le pendu
    if pendu == 1:
        piedPendu = "______{}______".format(pilier)
    elif pendu == 2:
        pilier = "|"
        piedPendu = "______{}______".format(pilier)
    elif pendu == 3:
        poutre = "      _________"
    elif pendu == 4:
        corde = "|"
    elif pendu == 5:
        tete = "O"
    elif pendu == 6:
        corp = "|"
    elif pendu == 7:
        brasGauche = "/"
    elif pendu == 8:
        brasDroit = "\\"
    elif pendu == 9:
        piedGauche = "/"
    elif pendu == 10:
        piedDroit = "\\"
        
        
    #affiiche le pendu
    print(poutre)
    print("      {}     {}".format(pilier,corde))
    print("      {}     {}".format(pilier,tete))
    print("      {}    {}{}{}".format(pilier,brasGauche,corp,brasDroit))
    print("      {}     {}".format(pilier,corp))
    print("      {}    {} {}".format(pilier,piedGauche,piedDroit))
    print(piedPendu)
    
    #si perdu
    if pendu == 10:
        print("Vous avez perdu")
        break