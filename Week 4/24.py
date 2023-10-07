import sys
import math

x, y, z = map(float, input().split())
if x < 0: x *= x
if y < 0: y *= y
if z < 0: z *= z
print('%.2f' % x, '%.2f' % y, '%.2f' % z)
