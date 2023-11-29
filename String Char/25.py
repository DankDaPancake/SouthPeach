import sys

inp = input()
s = ''.join(sorted(inp))
ct, c = 1, s[0]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        ct += 1
    else: 
        print(c, ct)
        ct = 1
        c = s[i]
print(c, ct)