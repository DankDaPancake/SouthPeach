import sys
import math

n, m = map(int, input().split())
s, f = 0, 1
for i in range(1, n+1):
    f = (f * i) % m
    s = (s + f) % m
print(s)