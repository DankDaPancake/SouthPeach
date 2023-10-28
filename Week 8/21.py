import sys
import math

m, n, x = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n): 
        if a[i][j] == x:
            print(i+1, j+1)