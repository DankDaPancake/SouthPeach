import sys
import math

n = int(input())
maxeven = -1
while n > 0: 
    if n % 2 == 0 and n % 10 > maxeven:
        maxeven = n % 10
    n //= 10
print(maxeven)