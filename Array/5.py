import sys
import math

n = int(input())
a = list(map(int, input().split()))
codd = 0
for i in a:
    if i % 2 == 1: codd += 1
print(codd)