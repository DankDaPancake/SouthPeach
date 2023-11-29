import sys
import math

n = int(input())
lim = int(math.sqrt(n))
factors = 0
for i in range(1, lim + 1):
    if i * i == n: factors += 1
    elif n % i == 0: factors += 2
print(factors)