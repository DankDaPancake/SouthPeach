import sys
import math

n, x = map(float, input().split())
n = int(n)
s, p, f = 0, 1, 1
for i in range(1, n+1):
    p *= x
    f *= i
    if i % 2 == 1: s += p / f
    else: s -= p / f    
print('%.2f' % s)  