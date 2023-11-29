import sys
import math

n = int(input())
s = 0
for i in range(1, n):
    s += math.sqrt(i)
    if s >= n:
        print(i) 
        break