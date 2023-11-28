import sys

s = input()
t = ''
for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90: t += chr(ord(s[i]) + 32)
    else: t += s[i]
print(t)