import sys
import math

n = int(input())
tn = n
revn = 0
while tn > 0: 
    revn = (revn * 10) + tn % 10
    tn //= 10
if revn == n: print('YES')
else: print('NO')