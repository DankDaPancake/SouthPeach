import sys
import math

n = int(input())
s = 0.0
for i in range(1, n):
    s += i / (i + 1)
print('%.2f' % s)   