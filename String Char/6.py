s=input()
new=''
for i in range(len(s)):
    if((s[i]!=' ' and s[i-1]==' ') or (s[i]!=' ' and i==0)):
        new+=s[i].upper()
    else:
        new+=s[i]
print(new)