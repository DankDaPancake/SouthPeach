import sys
import math

n = int(input())
a = list(map(int, input().split()))
maxLen, curLen = 0, 0
for i in range(n):
    if a[i] >= 0  and math.sqrt(a[i]) == int(math.sqrt(a[i])):
        curLen += 1
        if curLen > maxLen: maxLen = curLen
    else: curLen = 0

curLen = 0
for i in range(n):
    if math.sqrt(a[i]) == int(math.sqrt(a[i])):
        curLen += 1
        if curLen == maxLen:
            print(i-maxLen+2, i+1)
            exit()
    else: curLen = 0
