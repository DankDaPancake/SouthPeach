import sys
import math

a, b, c = map(float, input().split())
if a >= b and b >= c:
    a *= 2
    b *= 2
    c *= 2
else: 
    a = abs(a)
    b = abs(b)
    c = abs(c)
print('%.2f' % a, '%.2f' % b, '%.2f' % c)

