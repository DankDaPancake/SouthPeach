import sys
import math
    
def isPalin(x):
    tx = x
    revx = 0
    while tx > 0: 
        revx = (revx * 10) + tx % 10
        tx //= 10
    if revx == x: return True
    else: return False
    
m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

maxpalin = -2e9-1
for i in range(m):
    for j in range(n): 
        if isPalin(a[i][j]) and maxpalin < a[i][j]: 
            maxpalin = a[i][j]
if maxpalin == -2e9-1: print(-1)
else: print(maxpalin)