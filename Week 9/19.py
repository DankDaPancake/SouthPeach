import sys

name = list(map(str, input().split()))
for s in name:
    t = s.upper()
    print(t[0], end ='')
    t = t.lower()
    print(t[1:], end =' ')    