import sys
import math

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

ceven = 0
for i in range(m):
    for j in range(n): 
        if a[i][j] % 2 == 0: ceven += 1
print(ceven)