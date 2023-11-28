import sys

name = list(map(str, input().split()))
for i in range(len(name)-1):
    print(name[i], end = '')
print()
print(name[-1])