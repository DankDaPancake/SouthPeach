import sys
import math

n = int(input())
lim = int(math.sqrt(n))
isPrime = True
for i in range(2, lim + 1):
    if n % i == 0: 
        isPrime = False
        break        
if isPrime: print('YES')
else: print('NO')