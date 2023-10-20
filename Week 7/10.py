import sys
import math

n = int(input())
a = list(map(int, input().split()))
maxval = - 2e9 - 1
for i in a:
    if i > maxval: maxval = i
print(maxval)