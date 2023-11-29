import sys
import math

a, b, c = map(float, input().split())
s = a + pow(b, 2) + pow(c, 3)
print('%.2f' % s)