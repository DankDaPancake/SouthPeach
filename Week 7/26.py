import sys
import math

n, s = map(int, input().split())
a = list(map(int, input().split()))
found = False
for l in range(n):
    sumRange = 0
    if found: break
    for r in range(l, n):
        if found: break
        sumRange += a[r]
        if sumRange == s: 
            for x in range(l, r+1): 
                found = True
                print(x+1, end = ' ')
if found == False: print(-1)            