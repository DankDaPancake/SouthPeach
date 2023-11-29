import sys
import math

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

codd = 0
for i in range(m):
    for j in range(n): 
        if a[i][j] % 2 == 1: codd += 1
print(codd)