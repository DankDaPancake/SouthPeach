import sys

a = list(map(str, input().split()))
x = input()
for i in range(len(a)):
    found = False
    for c in a[i]:
        if c == x: 
            found = True
            break
    if found: 
        print(i+1)
        break