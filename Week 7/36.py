import sys
import math

n = int(input())
a = list(map(int, input().split()))
minHN = 2e9+1
for x in a:
    countD, savex = 0, x
    sumF, sumS = 0, 0
    while x > 0:
        if countD < 3: 
            sumF += x % 10
            countD += 1
        else: 
            sumS += x % 10
        x //= 10
    if sumF == sumS and countD == 3 and savex < minHN: minHN = savex
if minHN == 2e9+1: print(-1)
else: print(minHN)
