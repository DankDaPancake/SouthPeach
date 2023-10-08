import sys
import math

n = int(input())
s = 0
pre = None
while n > 0: 
    if pre != None: 
        s += abs(pre - (n % 10))
    pre = n % 10
    n //= 10
print(s)