import sys

s = input()
s1 = input()
vt = int(input())
print(s[:vt-1], end ='')
print(s1, end ='')
print(s[vt-1:])
