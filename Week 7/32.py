import sys
import math

n = int(input())
a = list(map(int, input().split()))
countpal = 0
for x in a:
    revx, tx = 0, x
    while tx > 0: 
        revx = (revx * 10) + tx % 10
        tx //= 10
    if revx == x and x > 0: countpal += 1
print(countpal)
