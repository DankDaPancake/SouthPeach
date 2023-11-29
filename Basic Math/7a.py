import sys
import math

a, b, c = map(float, input().split())
A = math.acos((b * b + c * c - a * a)/(2 * b * c))
B = math.acos((a * a + c * c - b * b)/(2 * a * c))
C = math.acos((a * a + b * b - c * c)/(2 * a * b))
ha = b / math.sin(C)
hb = a / math.sin(C)
hc = math.sin(A) * b
print('%.2f' % (ha))
print('%.2f' % (hb))
print('%.2f' % (hc))