import sys
import math

n = int(input())
s = 1
p = 1
for i in range(2, n+1):
    p = p * i
    if i % 2 == 0: s -= 1.0 / p
    else: s += 1.0 / p
print('%.2f' % s)   