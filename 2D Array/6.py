import sys
import math

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

sumodd = 0
for i in range(m):
    for j in range(n): 
        if a[i][j] % 2 == 1: sumodd += a[i][j]
print(sumodd)