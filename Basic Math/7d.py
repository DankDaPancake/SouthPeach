import math
import sys

a, b, c = map(float, input().split())
p = (a + b + c) / 2
s = math.sqrt(p * (p-a) * (p-b) * (p-c))
R = (a*b*c) / (4.0*s)
r = s / p
print('%.2f' % r)
print('%.2f' % R)