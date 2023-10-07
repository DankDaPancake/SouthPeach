import sys
import math

x, y = map(float, input().split())
s = (((3 * y - 7) * y + 2) * x - 3) * x + ((-2 * x - 4) * y + 15 * x + 10) * y + 6
print('%.2f' % s) 

