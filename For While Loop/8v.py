import sys
import math

n = int(input())
count, carry = 0, 0
while n > 0:
    if n % 10 == 0 and carry > 0:
        count += 1
        carry = 0
    else: carry = (carry * 10) + n % 10
    n //= 10
if carry > 0: count += 1
print(count)