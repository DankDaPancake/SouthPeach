import sys
import math

n = int(input())
a = list(map(int, input().split()))
minpal = 2e9+1
for x in a:
    revx = 0
    tx = x
    while tx > 0: 
        revx = (revx * 10) + tx % 10
        tx //= 10
    if revx == x and 0 < x < minpal: minpal = x
if minpal == 2e9+1: print(-1)
else: print(minpal)
