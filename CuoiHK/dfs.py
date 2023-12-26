
fi = open('dfs.inp', 'r')
fo = open('dfs.out', 'w')

N = int(1e5+5)
g = [[] for _ in range(N)]
st = [False for _ in range(N)]
f = [False for _ in range(N)]
path = []
par = [0 for _ in range(N)]

def dfs(s, t):
    par[s] = -1
    stack = [s]
    while s != t and stack:
        s = stack.pop()
        if not f[s]:
            path.append(s)
        if s == -1: break
        if s == t:
            break
        f[s] = True
        if not g[s]:
            path.pop()
            stack.append(par[s])
            continue
        if not st[s]:
            g[s].sort(reverse = True)
            st[s] = True
        c = 0
        for v in g[s]:
            if f[v]:
                continue
            par[v] = s
            stack.append(v)
            c += 1
        if c == 0:
            path.pop()
            stack.append(par[s])
        

n, m, s, t = map(int, fi.readline().split())
for _ in range(m):
    u, v = map(int, fi.readline().split())
    g[u].append(v)
    
dfs(s,t)
for u in path: fo.write(str(u) + ' ')