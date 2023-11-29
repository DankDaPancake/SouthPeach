import math
import sys

x, y, z = map(float, input().split())
a = 2.0 * math.cos(x - math.pi / 6) / (1 / 2 + pow(math.sin(y), 2))
b = 1.0 + pow(z, 2) / (3.0 + pow(0.4, z))
print('%.2f' % a, '%.2f' % b)