import sys

s1, s2 = map(str, input().split())
for i in range(len(s1) - len(s2) + 1):
    found = True
    for j in range(len(s2)):
        if s1[i+j] != s2[j]:
            found = False
            break
    if found: print(i+1, end = ' ')