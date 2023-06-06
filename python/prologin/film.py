
from typing import List


def nombre_films(adore: List[str], deteste: List[str]) -> None:
    x = 0
    z = 0
    regarde = []
    
    for i in adore:
        y = True
        for j in deteste:
            if j.lower() == i.lower():
                y = False
                break
        if y:
            regarde.append(i)
    
    for i in range(len(regarde)):
        for j in range(len(regarde)):
            if i == j:
                continue
            elif regarde[i] == regarde[j]:
                x += 1
                break
            
    for i in regarde:
        if i == "" or i == " ":
            z+=1
            break
    
    if x > 0:
        x-=1
    
    x = x + z
    
    print(len(regarde) - x)


if __name__ == "__main__":
    adore = [input() for _ in range(6)]
    deteste = [input() for _ in range(6)]

nombre_films(adore, deteste)