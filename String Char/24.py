import sys

inp = input()
s = ''.join(sorted(inp))
ct, maxct = 1, 1
c, maxc = s[0], s[0]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        ct += 1
        if ct > maxct: 
            maxct = ct
            maxc = c
    else: 
        ct = 1
        c = s[i]
print(maxc)