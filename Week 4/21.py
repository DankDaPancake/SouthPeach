import sys
import math

a, b = map(float, input().split())
if a >= b: a = 0
print('%.2f' % a, '%.2f' % b)