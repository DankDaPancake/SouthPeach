import math
import sys

x, y, z = map(float, input().split())
a = math.log(abs((y - math.sqrt(abs(x))) * (x - y/(z + pow(0.5, x)))))
b = x - pow(x, 2) / 6.0 + pow(x, 5) / 24.0
print('%.2f' % a, '%.2f' % b)