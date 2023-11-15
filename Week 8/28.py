import sys
import math
    
def isHappy(x):
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

maxhappy = 0
for i in range(m):
    for j in range(n): 
        if isHappy(a[i][j]) and maxhappy < a[i][j]:
            maxhappy = a[i][j]
if maxhappy == 0: print(-1)
else: print(maxhappy)