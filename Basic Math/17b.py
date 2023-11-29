import sys
import math

x, y, z = map(float, input().split())
s = x + y + z
p = x * y * z
if s > p:
    print('%.2f' % s)
else: print('%.2f' % p)
