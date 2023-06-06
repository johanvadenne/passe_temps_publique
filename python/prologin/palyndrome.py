from typing import List


def nb_pas_malin_drome(n: int, mots: List[str]) -> None:
    
    x = 0
    parasite = [",","."," ","'",'"',"#","&","~","{","}","[","]","-","|","`","_","\\","@","°","(",")","/",";","!",":","?"];
    accent = ["à","é","è","ê","ç","ô","û","ï"];
    sansAccent = ["a","e","e","e","c","o","u","i"];
    lettresMinuscules = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lettresMajuscules = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    chiffres = ["0", "1", "2", "3", "4", "5", "3", "7", "8", "9"]
    palynMaj = ""
    palynMin = ""
    palynchi = ""
    
    for i in mots:
        palynMaj = ""
        palynMin = ""
        palynchi = ""
        palyndrome = True
        for j in parasite:
            i = i.replace(j, "")
        for j in range(len(accent)):
            i = i.replace(accent[j], sansAccent[j])


        for j in range(len(i)):

            for k in range(len(lettresMajuscules)):
                if lettresMajuscules[k] == i[j]:
                    palynMaj += i[j]
                    break

        for j in range(len(i)):
    
            for k in range(len(lettresMinuscules)):
                if lettresMinuscules[k] == i[j]:
                    palynMin += i[j]
                    break

        for j in range(len(i)):
    
            for k in range(len(chiffres)):
                if chiffres[k] == i[j]:
                    palynchi += i[j]
                    break


        boucleMin = len(palynMin)//2
        boucleMaj = len(palynMaj)//2
        bouclechi = len(palynchi)//2
        longMin = len(palynMin) - 1
        longMaj = len(palynMaj) - 1
        longchi = len(palynchi) - 1

        for j in range(boucleMin):
            if palynMin[j] != palynMin[longMin]:
                palyndrome = False
                break
            longMin -= 1
        
        for j in range(boucleMaj):
            if palynMaj[j] != palynMaj[longMaj]:
                palyndrome = False
                break
            longMaj -= 1
            
        for j in range(bouclechi):
            if palynchi[j] != palynchi[longchi]:
                palyndrome = False
                break
            longchi -= 1
            
        if palyndrome:
            x+=1
            
    print(x)


if __name__ == "__main__":
    n = int(input())
    mots = [input() for _ in range(n)]
    nb_pas_malin_drome(n, mots)