import sys
import math

x, y = map(float, input().split())
if x > y:
    temp = x
    x = y
    y = temp
print('%.2f' % x) 
print('%.2f' % y) 
