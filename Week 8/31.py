import sys
import math

n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]

top, left, bot, right = 0, 0, n-1, n-1
num = 1
while left <= right and top <= bot:
    for i in range(left, right + 1):
        a[top][i] = num
        num += 1
    top += 1
    
    for i in range(top, bot + 1):
        a[i][right] = num
        num += 1
    right -= 1
    
    for i in range(right, left - 1, -1):
        a[bot][i] = num
        num += 1
    bot -= 1
    
    for i in range(bot, top - 1, -1):
        a[i][left] = num
        num += 1
    left += 1

for i in range(n):
    for j in range(n): print(a[i][j], end = ' ')
    print()