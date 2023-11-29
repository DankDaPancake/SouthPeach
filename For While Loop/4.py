import sys
import math

n = int(input())
for i in range(0, n+1, 2):
    x = (int)(i / 2)
    y = n - i
    print(x, y)
