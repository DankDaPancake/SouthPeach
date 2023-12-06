import sys
import math
from bisect import bisect_left

fi = open('asummin.inp', 'r')
fo = open('asummin.out', 'w')

m, n = map(int, fi.readline().split())
a = list(map(int, fi.readline().split()))
b = list(map(int, fi.readline().split()))
sb = b.copy()
sb.sort()

def binary_search(x):
    i = bisect_left(sb, x)
    if i != len(sb):
        return min(i, len(sb)-1)

ida, idsb = 0, 0 
minsum = 2**32
for i in range(m):
    idsb = binary_search(-a[i])
    idsb = min(idsb, len(sb)-1)
    idsb = max(idsb, 0)
    if abs(a[i] + sb[idsb]) < minsum: 
        ida = i
        minsum = abs(a[i] + sb[idsb])
    if idsb + 1 == len(sb): continue
    if abs(a[i] + sb[idsb+1]) < minsum: 
        ida = i
        minsum = abs(a[i] + sb[idsb+1])
    if idsb - 1 < 0: continue
    if abs(a[i] + sb[idsb-1]) < minsum: 
        ida = i
        minsum = abs(a[i] + sb[idsb-1])
    
for i in range(n): 
    if abs(a[ida] + b[i]) == minsum: 
        fo.write(str(ida+1) + ' ' + str(i+1))
        exit()
    