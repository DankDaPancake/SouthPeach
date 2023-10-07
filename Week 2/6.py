import math
import sys

a, b, c = map(float, input().split())
A = math.acos((pow(b, 2) + pow(c, 2) - pow(a, 2)) / (b * c * 2.0))
B = math.acos((pow(c, 2) + pow(a, 2) - pow(b, 2)) / (c * a * 2.0))
C = math.acos((pow(a, 2) + pow(b, 2) - pow(c, 2)) / (a * b * 2.0))
A = math.degrees(A)
B = math.degrees(B)
C = math.degrees(C)
print('%.2f' % A, '%.2f' % B, '%.2f' % C)