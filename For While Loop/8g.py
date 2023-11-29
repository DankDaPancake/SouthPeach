import sys
import math

n = int(input())
maxdif = 0
pre = None
while n > 0: 
    if pre != None: 
        if (abs(pre - (n % 10)) > maxdif): 
            maxdif = abs(pre - (n % 10)) 
    pre = n % 10
    n //= 10
print(maxdif)