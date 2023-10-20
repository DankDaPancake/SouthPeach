import sys
import math

n = int(input())
a = list(map(int, input().split()))
maxpal = -1
for x in a:
    revx, tx = 0, x
    while tx > 0: 
        revx = (revx * 10) + tx % 10
        tx //= 10
    if revx == x and x > maxpal: maxpal = x
print(maxpal)
