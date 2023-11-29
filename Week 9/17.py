import sys

s = input()
t, num = '', ''
for c in s:
    if '0' <= c <= '9': num += c
    else: t += c
print(num)