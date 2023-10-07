import sys
import math

x, y = map(float, input().split())
tx, ty = x, y
if x < y: 
    x = (tx + ty)/2
    y = tx * ty
else:
    x = tx * ty
    y = (tx + ty)/2
print('%.2f' % x, '%.2f' % y)

