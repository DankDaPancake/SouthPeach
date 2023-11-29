import sys
import math

a, b, c = map(float, input().split())
if a == 0:
    if b == 0 and c == 0:
        print('A')
    elif b == 0:
        print('E') 
    else:
        x1 = -c / b
        print('%.2f' % x1)
else:
    delta = b * b - 4.0 * a * c
    if delta < 0: 
        print('E')
    elif delta == 0:
        x1 = - b / (2.0 * a)
        print('%.2f' % x1)
    else: 
        x1 = (- b - math.sqrt(delta)) / (2.0 * a)
        x2 = (- b + math.sqrt(delta)) / (2.0 * a)
        print('%.2f' % x1, '%.2f' % x2)