import math
import sys

x1, y1, x2, y2 = map(float, input().split())
d = math.sqrt(pow(abs(x1-x2), 2) + pow(abs(y1-y2), 2))
print('%.2f' % d)