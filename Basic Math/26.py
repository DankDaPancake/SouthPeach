import sys
import math

a, b, c, d = map(float, input().split())
if a <= b and b <= c and c <= d:
    a = d 
    b = d 
    c = d
elif a > b and b > c and c > d:
    pass 
else: 
    a *= a
    b *= b
    c *= c
    d *= d
print('%.2f' % a, '%.2f' % b, '%.2f' % c, '%.2f' % d)
