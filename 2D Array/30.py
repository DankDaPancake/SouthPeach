import sys
import math
    
    
m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

b = []
for i in range(m):
    for j in range(n):
        sum = 0
        if i > 0: sum += a[i-1][j]
        if j > 0: sum += a[i][j-1]
        if i < m-1: sum += a[i+1][j]
        if j < n-1: sum += a[i][j+1]
        if i > 0 and j > 0: sum += a[i-1][j-1]
        if i > 0 and j < n-1: sum += a[i-1][j+1]
        if i < m-1 and j > 0: sum += a[i+1][j-1]
        if i < m-1 and j < n-1: sum += a[i+1][j+1]
        print(sum, end = ' ')
    print()