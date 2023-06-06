from typing import List


def trajets_retour(n: int, redirection: List[int]) -> None:
    
    tableauRedirection = []
    
    for i in range(n):
        
        x = [i]
        w = redirection[i] - 1
        y = redirection[w]
        
        while True:
            for j in x:
                if w == j:
                    tableauRedirection.append(str(len(x)))
                    break
            if w != j:
                x.append(w)
                w = y - 1
                y = redirection[w]
            else:
                break
    
    print(" ".join(tableauRedirection))



if __name__ == "__main__":
    n = int(input())
    redirection = list(map(int, input().split()))
    trajets_retour(n, redirection)