import sys
import math

n = int(input())
mind = 10
while n > 0: 
    if n % 10 > 0 and n % 10 < mind: mind = n % 10
    n //= 10
print(mind) 