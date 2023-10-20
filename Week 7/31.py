import sys
import math

n = int(input())
a = list(map(int, input().split()))
sumf = [-1] * n
for i in range(n):
    if a[i] <= 1: continue
    sumf[i] = 1
    lim = int(math.sqrt(a[i]))
    for j in range(2, lim + 1):
        if j * j == n: sumf[i] += j
        elif a[i] % j == 0: sumf[i] += j + a[i]//j

found = False
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] == sumf[j] and a[j] == sumf[i]:
            found = True
            print(a[i], a[j])

if found == False: print(-1)