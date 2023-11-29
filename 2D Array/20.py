import sys
import math

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

for i in range(m):
    dec = True
    for j in range(n-1): 
        if a[i][j] < a[i][j+1]:
            dec = False
    if dec: print('YES')
    else: print('NO')
        