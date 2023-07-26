from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 8)
input = stdin.readline

N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]

for _ in range(M):
    u, v = map(lambda x: x - 1, map(int, input().split()))
    adj[u][v] = 1
    adj[v][u] = 1

chk = [False] * N
ans = 0


def dfs(a):
    for b in range(N):
        if adj[a][b] and not chk[b]:
            chk[b] = True
            dfs(b)


for i in range(N):
    if not chk[i]:
        chk[i] = True
        ans += 1
        dfs(i)

print(ans)