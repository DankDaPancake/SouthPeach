import sys
import math

n = int(input())
count0 = 0
for i in range(2, n+1):
    num = i
    while num % 5 == 0: 
        num //= 5
        count0 += 1
print(count0)