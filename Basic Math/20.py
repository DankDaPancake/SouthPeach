import sys
import math

x, y = map(float, input().split())
if x > y: print('%.2f' % (x - y))
else: print('%.2f' % (y - x - 1))

