import sys
import math

m, n = map(int, input().split())
pre = []
a = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    row = list(map(int, input().split()))
    for j in range(n):
        pre.append(row[j])
    
pre.sort()
top, left, bot, right = 0, 0, m-1, n-1
k = m * n -1
while left <= right and top <= bot:
    for i in range(left, right + 1):
        a[top][i] = pre[k]
        k -= 1
    top += 1
    
    for i in range(top, bot + 1):
        a[i][right] = pre[k]
        k -= 1
    right -= 1
    
    if top <= bot:
        for i in range(right, left - 1, -1):
            a[bot][i] = pre[k]
            k -= 1
        bot -= 1
    
    if left <= right:
        for i in range(bot, top - 1, -1):
            a[i][left] = pre[k]
            k -= 1
        left += 1

for i in range(m):
    for j in range(n): print(a[i][j], end = ' ')
    print()