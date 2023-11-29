import math
import sys

x, y, z = map(float, input().split())
a = (3.0 + pow(math.e, y-1)) / (1.0 + pow(x, 2) * abs(y - math.tan(z)))
b = (1.0 - abs(y-x) + pow(y-x, 2)/2 + pow(y-x, 3)/3)
print('%.2f' % a, '%.2f' % b)