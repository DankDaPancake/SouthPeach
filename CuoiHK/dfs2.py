from collections import deque

fi = open('dfs.inp', 'r')
fo = open('dfs.out', 'w')

n, m, s, t = map(int, fi.readline().split())
graph = [[] for _ in range((int(1e5+5)))]

def bfs(start, end):
    visited = [False] * n
    path = [-1] * n
    queue = [start]
    visited[start] = True
    while queue:
        u = queue.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                path[v] = u
                queue.append(v)
                if v == end:
                    return path
    return None

def get_path(path, start, end):
    if path[end] == -1:
        return None
    p = [end]
    while p[-1] != start:
        p.append(path[p[-1]])
    return list(reversed(p))

def lexicographic_path(start, end):
    path = bfs(start, end)
    if path is None:
        return None
    return get_path(path, start, end)

for i in range(m):
    u, v = map(int, fi.readline().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    
for i in range(1, n+1):
    graph[i].sort()
    
ans = lexicographic_path(s-1, t-1)
print(ans)