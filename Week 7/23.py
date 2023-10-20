import sys
import math

n, x = map(int, input().split())
a = list(map(int, input().split()))
notfound = True
for i in range(n):
    if a[i] == x: 
        notfound = False
        print(i+1, end = ' ')
if notfound: print(-1)