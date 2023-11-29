import sys
import math

n = int(input())
count, carry, maxcarry = 0, 0, 0
while n > 0:
    if n % 10 == 0 and carry > 0 :
        count += 1
        if maxcarry < carry: 
            maxcarry = carry
        carry = 0
    else: carry += 1
    n //= 10
if carry > 0: count += 1
print(maxcarry)