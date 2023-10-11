import sys
import math

n, m = map(int, input().split())
lim_n = int(math.sqrt(n))
lim_m = int(math.sqrt(m))
sum_n, sum_m = 1, 1
for i in range(2, lim_n + 1):
    if i * i == n: sum_n += i
    elif n % i == 0: sum_n += i + n//i
for i in range(2, lim_m + 1):
    if i * i == m: sum_m += i
    elif m % i == 0: sum_m += i + m//i
if sum_n == m and sum_m == n: print('YES')
else: print('NO')
