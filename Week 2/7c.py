import math
import sys

a, b, c = map(float, input().split())
sa = b + c
sb = a + c
sc = a + b
lA = math.sqrt(b*c * (sa+a) * (sa-a)) / sa
lB = math.sqrt(a*c * (sb+b) * (sb-b)) / sb
lC = math.sqrt(a*b * (sc+c) * (sc-c)) / sc
print('%.2f' % lA)
print('%.2f' % lB)
print('%.2f' % lC)