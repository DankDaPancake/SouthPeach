import sys

s = input()
vt, n = map(int, input().split())
print(s[:vt-1], end ='')
print(s[vt+n-1:])