import math
import sys

a, b, c = map(float, input().split())
if a == 0:
    if b == 0 and c == 0:
        print('A')
    elif b != 0 and c == 0:
        print('0.00')
    elif b == 0 and c != 0:
        print('E')
    else:
        if -c/b >= 0:
            print('%.2f' % (-math.sqrt((-c) / b)), '%.2f' % (math.sqrt((-c) / b)))
        else:
            print('E')
else:
    delta = (b * b / 4) - a * c
    x1 = (-b / 2) / a
    x2 = ((-b / 2 - math.sqrt(delta)) / a)
    x3 = ((-b / 2 + math.sqrt(delta)) / a)
    if delta < 0:
        print('E')
    elif delta == 0:
        if (-b / 2) / a >= 0:
            print('%.2f' % (-math.sqrt(x1)), '%.2f' % (math.sqrt(x1)))
        else:
            print('E')
    else:
        if x2 < 0 and x3 < 0:
            print('E')
        else:
            if x2 >= 0:
                print('%.2f' % (-math.sqrt(x2)), '%.2f' % (math.sqrt(x2)))
            if x3 >= 0:
                print('%.2f' % (-math.sqrt(x3)), '%.2f' % (math.sqrt(x3)))
