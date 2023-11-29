import sys
import math

n = int(input())
p = 1
while n > 0: 
    if n % 2 == 1: p *= n % 10
    n //= 10
print(p)