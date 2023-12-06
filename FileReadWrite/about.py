import sys
import math

fi = open('about.inp', 'r')
fo = open('about.out', 'w')

def countF(num):
    if num <= 2: return num
    ans = 2
    for i in range(2, math.trunc(math.sqrt(num))+1):
        if i*i == num: ans += 1
        elif num % i == 0: ans += 2
    return ans  

n, k = map(int, fi.readline().split())

num = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        num += 1
        if countF(num) <= k: 
            fo.write('*')
        else: fo.write('.')
    fo.write('\n')
         