import sys
import math

n = int(input())
a = list(map(int, input().split()))
sumf = [1] * n
for i in range(n):
    for j in range(2, int(math.sqrt(a[i])) + 1):
        if j * j == a[i]: sumf[i] += j
        elif a[i] % j == 0: sumf[i] += j + a[i]//j

found = False
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] == sumf[j] and a[j] == sumf[i]:
            found = True
            print(a[i], a[j])

if not found: print(-1)