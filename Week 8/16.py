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
    
cprime = 0
for i in range(m):
    for j in range(n): 
        if isPrime(a[i][j]): cprime += 1
print(cprime)