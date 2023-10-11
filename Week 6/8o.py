import sys
import math

n = int(input())
lim = int(math.sqrt(n))
sumf = 0
for i in range(1, lim + 1):
    if i * i == n: sumf += i
    elif n % i == 0: sumf += i + n//i
print(sumf)