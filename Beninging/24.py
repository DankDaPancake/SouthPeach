import sys
import math

a, b = map(float, input().split())
d = abs(a) - abs(b)
s = abs(a) + abs(b)
print('%.2f' % d)
print('%.2f' % s)