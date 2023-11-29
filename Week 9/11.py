import sys

s1 = input()
s2 = input()
found = s1.find(s2)
if found != -1: print(found+1)
else: print(-1)