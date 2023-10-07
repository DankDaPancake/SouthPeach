import sys
import math

a, b = map(float, input().split())
c = math.sqrt((a/2)**2 + (b/2)**2)
cv = c * 4
dt = (a * b)/2
print('%.2f' % cv)
print('%.2f' % dt)