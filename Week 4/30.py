import sys
import math

a1, b1, c1, a2, b2, c2 = map(float, input().split())
t = b1 / b2
a2 *= t
b2 *= t
c2 *= t
if a1 == a2 and b1 == b2:
    if c1 == c2: print('A')
    else: print('E')
else:
    x = (- c1 + c2) / (a1 - a2)
    y = (- a1 * x - c1) / b1
    print('%.2f' % x, '%.2f' % y)
