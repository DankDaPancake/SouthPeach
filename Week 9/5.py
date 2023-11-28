import sys

s = input()
t = ''
for i in range(len(s)):
    if 97 <= ord(s[i]) <= 122: t += chr(ord(s[i]) - 32)
    else: t += s[i]
print(t)