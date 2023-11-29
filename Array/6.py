import sys
import math

n = int(input())
a = list(map(int, input().split()))
s = 0
for i in a:
    if i % 2 == 1: s += i
print(s)