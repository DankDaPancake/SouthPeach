import sys
import math

n = int(input())
s = 0.0
for i in range(1, n+1):
    if i == 1: s = n - i + 1
    else: s = n - i + 1 + 1.0 / s
print('%.2f' % s)   