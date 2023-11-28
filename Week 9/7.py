import sys

s = input()
t = ''
for i in range(len(s)):
    if i % 2 == 0:
        if 97 <= ord(s[i]) <= 122: t += chr(ord(s[i]) - 32)
        else: t += s[i]
    else: 
        if 65 <= ord(s[i]) <= 90: t += chr(ord(s[i]) + 32)
        else: t += s[i]
print(t)