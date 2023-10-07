import sys
import math

k, n, m = map(int, input().split())
s, f = 0, 1
for i in range(1, n+1):
    f *= i
    s = (s + f) % m
print(s)
s, p = 1, 1 
for _ in range(n):
    p = (p * k) % m
    s = (s + p) % m
print(s) 