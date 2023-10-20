import sys
import math

n = int(input())
a = list(map(int, input().split()))
pfnum = 0
for i in a:
    if i >= 6:
        lim = int(math.sqrt(i))
        sumf = 1
        for j in range(2, lim + 1):
            if j * j == i: sumf += j
            elif i % j == 0: sumf += j + i//j
        if sumf == i: 
            pfnum += 1
print(pfnum)