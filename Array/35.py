import sys
import math

n = int(input())
a = list(map(int, input().split()))
countHN = 0
for x in a:
    countF = 0
    sumF, sumS = 0, 0
    while x > 0:
        if countF < 3: 
            sumF += x % 10
            countF += 1
        else: 
            sumS += x % 10
        x //= 10
    if sumF == sumS and countF == 3: countHN += 1
print(countHN)
