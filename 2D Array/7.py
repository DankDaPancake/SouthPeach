import sys
import math

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

maxeven = -2e9 - 1
for i in range(m):
    for j in range(n): 
        if a[i][j] % 2 == 0 and a[i][j] > maxeven: maxeven = a[i][j]
if maxeven == -2e9-1: print(-1)
else: print(maxeven)