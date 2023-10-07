import sys
import math

n = int(input())
s = 1
for i in range(2, n+1):
    inv_sqrt = 1.0 / math.sqrt(i)
    if i % 2 == 0: s *= 1 + inv_sqrt
    else: s *= 1 - inv_sqrt
print('%.2f' % s)  