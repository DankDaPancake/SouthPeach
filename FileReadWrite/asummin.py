fi = open('asummin.inp', 'r')
fo = open('asummin.out', 'w')

m, n = map(int, fi.readline().split())
a = list(map(int, fi.readline().split()))
b = list(map(int, fi.readline().split()))
sb = []
for i in range(n): 
    sb.append((b[i], i))
sb.sort()

def bsearch(x):
    if x <= sb[0][0]: return sb[0][1]
    if x >= sb[-1][0]: return sb[-1][1]
    l, r = 0, len(sb) - 1
    while l <= r:
        mid = (l + r) // 2
        if sb[mid][0] == x: return sb[mid][1]
        elif sb[mid][0] < x:
            l = mid + 1
        else:
            r = mid - 1
    if abs(sb[l][0] - x) < abs(sb[r][0] - x):
        return sb[l][1]
    else:
        return sb[r][1]

ida, idb = -1, -1
for i in range(m): 
    if i > 0 and a[i] == a[i-1]: continue
    t = bsearch(-a[i])
    if a[i] + b[t] == 0:
        fo.write(str(i+1) + ' ' + str(t+1))
        exit()
    if ida == -1 or abs(a[i] + b[t]) <= abs(a[ida] + b[idb]):
        ida = i
        idb = t
fo.write(str(ida+1) + ' ' + str(idb+1))
