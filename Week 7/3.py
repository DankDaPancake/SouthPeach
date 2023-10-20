import sys
import math

n = int(input())
a = list(map(int, input().split()))
ceven = 0
for i in a:
    if i % 2 == 0: ceven += 1
print(ceven)