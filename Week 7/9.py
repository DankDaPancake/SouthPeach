import sys
import math

n = int(input())
a = list(map(int, input().split()))
for i in a:
    if i >= 0:
        ii = int(math.sqrt(i))
        if ii * ii == i: 
            print(i, end = ' ')
