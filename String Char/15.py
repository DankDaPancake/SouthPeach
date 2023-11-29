import sys

a = list(map(str, input().split()))
s = input()
cut = False
for t in a:
    if t == s: cut = True
    if cut: print(t, end = ' ')