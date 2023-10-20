import sys
import math

n = int(input())
a = list(map(int, input().split()))
countHN = 0
for x in a:
    countD = 0
    sumF, sumS = 0, 0
    while x > 0:
        if countD < 3: 
            sumF += x % 10
            countD += 1
        else: 
            sumS += x % 10
        x //= 10
    if sumF == sumS and countD == 3: countHN += 1
print(countHN)
