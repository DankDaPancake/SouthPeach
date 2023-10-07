import sys
import math

a, b, c = map(float, input().split())
A = math.acos((b * b + c * c - a * a)/(2.0 * b * c))
B = math.acos((a * a + c * c - b * b)/(2.0 * a * c))
C = math.acos((a * a + b * b - c * c)/(2.0 * a * b))
ma = math.sqrt(pow(a / 2, 2) + c * c - a * c * math.cos(B))
mb = math.sqrt(pow(b / 2, 2) + a * a - a * b * math.cos(C))
mc = math.sqrt(pow(c / 2, 2) + b * b - b * c * math.cos(A))
print('%.2f' % ma)
print('%.2f' % mb)
print('%.2f' % mc)