import math
import sys

x1, y1, x2, y2, x3, y3 = map(float, input().split())
a = math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
b = math.sqrt(pow(x2-x3, 2) + pow(y2-y3, 2))
c = math.sqrt(pow(x3-x1, 2) + pow(y3-y1, 2))
p = a+b+c
print('%.2f' % p)
p /= 2
s = math.sqrt(p * (p-a) * (p-b) * (p-c))
print('%.2f' % s)