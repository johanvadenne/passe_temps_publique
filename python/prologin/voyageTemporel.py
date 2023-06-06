from typing import List


def stabilite_maximale(n: int, k: int, p: int, accroches: List[int]) -> None:
    accroches.sort()
    x = len(accroches)
    y = []
    z = []
    if x != 0:
        x +=1 
    
    for i in range(x - 5):
        a = p - (accroches[i+3] - accroches[i])**2
        y.append(a)
    y.sort()
    
    c 
    
    if k > 2:
        for i in range(x - 5):
            for j in range(x-5):
                b = y[i] + y[j + 3]
                z.append(b)
    
    print(y[len(y)- 1])
    print(z)


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = list(map(int, input().split()))
    stabilite_maximale(n, k, p, accroches)