import sys
import math

n = int(input())
k, maxk, maxd = 0, -1, 0
while n > 0: 
    if n % 10 > maxd: 
        maxd = n % 10
        maxk = k
    k += 1
    n //= 10
print(maxk)