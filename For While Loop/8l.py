import sys
import math

n = int(input())
pre = 10
valid = True
while n > 0: 
    if pre < n % 10:
        print('NO')
        valid = False        
        break
    pre = n % 10
    n //= 10
if valid: print('YES')