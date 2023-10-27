import sys
import math

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

maxval = -2e9 - 1
for i in range(m):
    for j in range(n): 
        if a[i][j] > maxval: maxval = a[i][j]

for i in range(m):
    for j in range(n): 
        if a[i][j] == maxval:
            print(i+1, j+1)
            exit()