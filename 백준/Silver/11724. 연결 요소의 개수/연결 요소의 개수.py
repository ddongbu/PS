import sys
sys.setrecursionlimit(2500)

N, M = map(int, sys.stdin.readline().split())
graph = {}

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
    
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

def dfs(u):
    visited[u] = True
    if u in graph:
        for v in graph[u]:
            if visited[v] == False:
                dfs(v)

visited = [False for _ in range(N+1)]
count = 0

for u in range(1, N+1):
    if visited[u] == False:
        dfs(u)
        count += 1

print(count)