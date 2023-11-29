import sys
import math

x, y = map(float, input().split())
if x < 0 and y < 0:
    x = abs(x)
    y = abs(y)
elif x < 0 or y < 0:
    x += 0.5
    y += 0.5
elif (x < 1 or x > 2) and (y < 1 or y > 2):
    x *= 10
    y *= 10
print('%.2f' % x, '%.2f' % y)
