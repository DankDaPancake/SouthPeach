import sys
import math

n = int(input())
for i in range(2, math.trunc(math.sqrt(n))+1):
    while n % i == 0:
        print(i, end = ' ')
        n //= i
if n > 1: print(n)