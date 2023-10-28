import sys
import math
    
m, n, x = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

countx = 0
for i in range(m):
    for j in range(n): 
        if a[i][j] == x: countx += 1
print(countx)