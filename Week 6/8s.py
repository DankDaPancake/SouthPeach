import sys
import math

n = int(input())
lim = int(math.sqrt(n))
sumf = 1
for i in range(2, lim + 1):
    if i * i == n: sumf += i
    elif n % i == 0: sumf += i + n//i
if sumf == n: print('YES')
else: print('NO')