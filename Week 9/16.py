import sys

s = input()
isPalin = True
for i in range(len(s)//2-1):
    if s[i] != s[-i]:
        isPalin = False
        break
if isPalin: print('YES')
else: print('NO')