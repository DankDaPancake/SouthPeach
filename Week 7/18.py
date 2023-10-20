import sys
import math

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] >= 2:
        lim = int(math.sqrt(a[i]))
        isPrime = True
        for j in range(2, lim + 1):
            if a[i] % j == 0: 
                isPrime = False
                break
        if isPrime: print(i + 1, end = ' ')