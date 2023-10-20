import sys
import math

n = int(input())
a = list(map(int, input().split()))
minS = 2e12
for l in range(n):
    sumRange = 0
    for r in range(l, n):
        sumRange += a[r]
        if sumRange < minS: minS = sumRange

for l in range(n):
    sumRange = 0
    for r in range(l, n):
        sumRange += a[r]
        if sumRange == minS: 
            for x in range(l, r+1): 
                print(a[x], end = ' ')
            exit()