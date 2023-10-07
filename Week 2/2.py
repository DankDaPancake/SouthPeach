import sys
import math

a, b = map(float, input().split())
c = math.sqrt(pow(a, 2) - pow(b, 2))
S = (b * c) / 2
r = (2.0 * S) / (a + b + c)
print('%.2f' % r)
