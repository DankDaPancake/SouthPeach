import sys
import math

n, x = map(int, input().split())
a = list(map(int, input().split()))
countx = 0
for i in range(n):
    if a[i] == x: 
        countx += 1
print(countx)