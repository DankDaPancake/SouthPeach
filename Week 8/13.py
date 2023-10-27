import sys
import math

def isPerfect(x):
    sumf = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if i * i == x: sumf += i
        elif x % i == 0: sumf += i + x//i
    if sumf == x: return True
    else: return False   
    
m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

countpn = 0
for i in range(m):
    for j in range(n): 
        if isPerfect(a[i][j]): 
            print(a[i][j])