import math
import sys

a, b, c = map(float, input().split())
s = a + b + c
if s < 1:
    minv = a
    if b < minv:
        minv = b
    if c < minv:
        minv = c
    if minv == a:
        a = s /3
    elif minv == b:
        b = s /3
    else:
        c = s /3
else:
    if a < b:
        a = (b + c)/2
    else:
        b = (a + c)/2
print("%.2f" % a,"%.2f" % b, "%.2f" % c)

