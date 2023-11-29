import sys
import math

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

for i in range(m):
    inc = True
    for j in range(n-1): 
        if a[i][j] > a[i][j+1]:
            inc = False
    if inc: print('YES')
    else: print('NO')
        