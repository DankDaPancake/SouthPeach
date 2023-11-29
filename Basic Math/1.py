import sys
import math

n, r = map(float, input().split())
alpha = 3.14 / n
a = 2.0 * r * math.sin(alpha)
p = n * a
print('%.2f' % p)
