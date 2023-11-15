import sys
import math

m, n, x = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

count = 0
for i in range(m):
    for j in range(n): 
        if a[i][j] == x:
            count += 1
            print(i+1, j+1)
if count == 0: print(-1)