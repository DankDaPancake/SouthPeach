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
            for j in range(i-maxLen+1, i+1):
                print(a[j], end = ' ')
    else: curLen = 0
