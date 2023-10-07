import sys
import math

n = int(input())
F, sumF = 1, 1
for i in range(2, n+1):
    F = i * sumF
    sumF += F
    print(F)
print(F)