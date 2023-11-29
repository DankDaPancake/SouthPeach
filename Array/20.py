import sys
import math

n = int(input())
a = list(map(int, input().split()))
increasing = True
for i in range(1, n):
    if a[i-1] < a[i]: 
        increasing = False
        break
if increasing: print('YES')
else: print('NO')