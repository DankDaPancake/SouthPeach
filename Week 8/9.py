import sys
import math

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n): 
        if a[i][j] < 1: continue
        if math.sqrt(a[i][j]) == int(math.sqrt(a[i][j])):
            print(a[i][j], end = ' ')