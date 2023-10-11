import sys
import math

k, n, m = map(int, input().split())
s, p = 1, 1 
for _ in range(n):
    p = (p * k) % m
    s = (s + p) % m
print(s) 