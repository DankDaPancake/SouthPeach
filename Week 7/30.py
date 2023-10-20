import sys
import math

n = int(input())
a = list(map(int, input().split()))
prime = [True] * n
maxLen, curLen = 0, 0
for i in range(n):
    if a[i] >= 2:
        lim = int(math.sqrt(a[i]))
        for j in range(2, lim + 1):
            if a[i] % j == 0: 
                prime[i] = False
                break
    else: prime[i] = False
    if prime[i]: 
        curLen += 1
        if curLen > maxLen: maxLen = curLen
    else: curLen = 0

curLen = 0
for i in range(n):
    if prime[i]:
        curLen += 1
        if curLen == maxLen:
            for j in range(i-maxLen+1, i+1):
                print(a[j], end = ' ')
    else: curLen = 0
