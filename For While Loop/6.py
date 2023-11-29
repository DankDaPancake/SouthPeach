import sys
import math

n = int(input())
if n <= 2:
    print(n)
else:
    F1, F2 = 1, 2
    for i in range(3, n+1):
        temp = F2
        F2 = 3 * temp - 2 * F1
        F1 = temp
    print(F2)