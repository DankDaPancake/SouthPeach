fi = open('dfs.inp', 'r')
fo = open('dfs.out', 'w')

n, m, s, t = map(int, fi.readline().split())
g = [[] for _ in range(n+1)]
par = [-1 for _ in range(n+1)]

def dfs(u, pre):
    par[u] = pre
    for v in g[u]:
        if par[v] == -1:
            dfs(v, u)

for _ in range(m):
    u, v = map(int, fi.readline().split())
    g[u].append(v)
for i in range(1, n+1):
    g[i].sort()

dfs(s, s)
if par[t] == -1:
    fo.write(str(-1))
    exit()

path = []
while t != par[t]:
    path.append(t)
    t = par[t]
path.append(t)

path.reverse()
for u in path: fo.write(str(u) + ' ')