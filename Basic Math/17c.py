import sys
import math

x, y, z = map(float, input().split())
s = x + y + z/2
p = x * y * z 
if s > p: minv = p
else: minv = s
print('%.2f' % (minv * minv + 1))
