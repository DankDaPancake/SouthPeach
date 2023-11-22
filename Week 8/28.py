import sys
import math
    
def isHappy(x):
    if x < 100000 or x > 999999: 
        return False
    countD = 0
    sumF, sumS = 0, 0
    while x > 0:
        if countD < 3: 
            sumF += x % 10
            countD += 1
        else: 
            sumS += x % 10
        x //= 10
    if sumF == sumS: return True
    else: return False
    
m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

maxhappy = -2e9 -1
for i in range(m):
    for j in range(n): 
        if isHappy(a[i][j]) and maxhappy < a[i][j]:
            maxhappy = a[i][j]
if maxhappy == -2e9-1: print(-1)
else: print(maxhappy)