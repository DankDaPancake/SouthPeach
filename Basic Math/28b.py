import math
import sys

a, b, c = map(float, input().split())
d = a * a
e = b * b
f = c * c
if d == e + f or e == d + f or f == d + e: print(2)
elif d > e + f or e > d + f or f > d + e: print(3)
elif d < e + f or e < d + f or f < d + e: print(1)