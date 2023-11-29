import sys
import math

n = int(input())
s = 0.0
for i in range(1, n+1):
    s = math.sqrt(s + 2.0)
print('%.2f' % s)   