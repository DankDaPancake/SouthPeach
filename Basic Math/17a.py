import sys
import math

x, y, z = map(float, input().split())
if x > y and x > z: 
    temp = x
    x = z
    z = temp
if x > y:
    x = y
print('%.2f' % x)
print('%.2f' % z)
