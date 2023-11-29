import math
import sys

a, b, alpha = map(float, input().split())
d = alpha * 3.14 / 180.0
h = math.tan(d) * (abs(a-b) / 2.0)
s = ((a + b) * h) / 2.0
print('%.2f' % s)