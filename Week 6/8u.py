import sys
import math

n = int(input())
countD = 0
sumF, sumS = 0, 0
while n > 0:
    if countD < 3: 
        sumF += n % 10
        countD += 1
    else: 
        sumS += n % 10
    n //= 10
if sumF == sumS: print('YES')
else: print('NO')
