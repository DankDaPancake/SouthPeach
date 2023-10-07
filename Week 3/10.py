import sys
import math

n, a, d = map(float, input().split())
print('%.0f' % ((a + a + (n - 1) * d) * n / 2))