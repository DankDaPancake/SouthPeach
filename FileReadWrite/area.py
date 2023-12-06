import sys
import math

fi = open('area.inp', 'r')
fo = open('area.out', 'w')

m, n = map(int, fi.readline().split())
b, vst = [], [[False for _ in range(0, n)] for _ in range(0, m)]

def bfs(i, j):
    vst[i][j] = True
    if i > 0 and b[i-1][j] == '*' and not vst[i-1][j]: bfs(i-1, j)
    if j > 0 and b[i][j-1] == '*' and not vst[i][j-1]: bfs(i, j-1)
    if i < m-1 and b[i+1][j] == '*' and not vst[i+1][j]: bfs(i+1, j)
    if j < n-1 and b[i][j+1] == '*' and not vst[i][j+1]: bfs(i, j+1)
                
for i in range(m): 
    b.append(fi.readline())

areas = 0
for i in range(m): 
    for j in range(n):
        if not vst[i][j] and b[i][j] == '*':
            bfs(i, j)
            areas += 1
fo.write(str(areas))
