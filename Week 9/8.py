import sys

s = input()
t = ''
for i in range(len(s)-1, -1, -1):
    t += s[i]
print(t)