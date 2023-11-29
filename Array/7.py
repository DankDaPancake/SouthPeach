import sys
import math

n = int(input())
a = list(map(int, input().split()))
maxeven = -1
for i in a:
    if i % 2 == 0:
        if maxeven == -1: maxeven = i
        if i > maxeven: maxeven = i
print(maxeven) 