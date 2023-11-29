import sys
import math

n, x = map(int, input().split())
a = list(map(int, input().split()))
found = -1
for i in range(n):
    if a[i] == x: 
        found = i + 1
        break
print(found)