import sys
import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True
    
m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))
    
for i in range(m):
    for j in range(n): 
        if isPrime(a[i][j]): print(a[i][j])