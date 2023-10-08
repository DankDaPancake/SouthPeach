import sys
import math

n = int(input())
m = 0
tem_n = n
while tem_n > 0: 
    m = (m * 10) + tem_n % 10
    tem_n //= 10
print(n + m)