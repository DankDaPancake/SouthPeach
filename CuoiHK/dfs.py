import math
import sys

fi = open('dfs.inp', 'r')
fo = open('dfs.out', 'w')

n, m, s, t = map(int, fi.readline().split())
par = [i for i in range(n+1)]
vst = [0] * (n+1)
g = [[] for _ in range(n+1)]
res = []

def solve(u):
    if u == par[u]:
        res.append(u)
        return
    res.append(u)
    u = par[u]
    solve(u)

def dfs():
    st = [s]
    while st:
        p = st[-1]
        vst[p] = 1
        if p == t:
            solve(t)
            return
        st.pop()
        for v in g[p]:
            if vst[v] == 1:
                continue
            par[v] = p
            st.append(v)

for _ in range(m):  
    u, v = map(int, fi.readline().split())
    g[u].append(v)

for i in range(1, n+1):
    g[i].sort(reverse= True)

dfs()

res.reverse()
for v in res:
    fo.write(str(v) + ' ')