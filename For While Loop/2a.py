import sys
import math

n, x = map(float, input().split())
n = int(n)
s = 1.0
for _ in range(n):
    s *= x
print('%.2f' % s)  