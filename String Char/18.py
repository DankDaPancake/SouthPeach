import sys

s = input()
x = input()
t = ''
for c in s:
    if c != x: t += c
print(t)