import sys

a = list(map(str, input().split()))
x = input()
countx = 0
for i in range(len(a)):
    for c in a[i]:
        if c == x: countx += 1
print(countx)