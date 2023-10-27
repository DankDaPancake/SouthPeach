import sys
import math

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

sum = 0
for i in range(m):
    for j in range(n): 
        sum += a[i][j]
print('%.2f' % (sum / (m * n)))