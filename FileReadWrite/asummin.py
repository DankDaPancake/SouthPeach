import bisect

fi = open('asummin.inp', 'r')
fo = open('asummin.out', 'w')

m, n = map(int, fi.readline().split())
a = list(map(int, fi.readline().split()))
b = list(map(int, fi.readline().split()))

sb = b.copy()
sb.sort()

ida, numb, mins = 0, 0, int(1e10)
for i in range(m):
    j = bisect.bisect_left(sb, -a[i])
    if j >= n: j = n-1
    if abs(a[i] + sb[j]) < mins:
        mins = abs(a[i] + sb[j])
        ida = i
        numb = sb[j]
    if abs(a[i] + sb[j-1]) < mins:
        mins = abs(a[i] + sb[j-1])
        ida = i
        numb = sb[j-1]

for i in range(n): 
    if b[i] == numb:
        fo.write(str(ida+1) + ' ' + str(i+1))
        break
