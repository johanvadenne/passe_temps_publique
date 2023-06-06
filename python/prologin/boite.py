
from typing import List


def mise_en_boite(n: int, restes: List[int], boites: List[int]) -> None:
    
    x = 0
    
    restes = sorted(restes)
    boites = sorted(boites)
    
    for i in restes:
        for j in range(len(boites)):
            if i <= boites[j]:
                boites.pop(j)
                break
    
    print(n - len(boites))

if __name__ == "__main__":
    n = int(input())
    restes = list(map(int, input().split()))
    boites = list(map(int, input().split()))
    mise_en_boite(n, restes, boites)