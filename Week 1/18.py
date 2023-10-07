import sys
import math

a, b, c = map(float, input().split())
p = (a + b + c)/2
s = math.sqrt(p * (p-a) * (p-b) * (p-c))
print('%.2f' % (p*2))
print('%.2f' % s)
