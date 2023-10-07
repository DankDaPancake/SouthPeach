import sys
import math

n, x = map(float, input().split())
n = int(n)
s, p, f = 0, 1, 1
for i in range(1, n+1): p *= x
for i in range(1, n+1): 
    p /= x
    f *= i
    s += p / f
print('%.2f' % s)  