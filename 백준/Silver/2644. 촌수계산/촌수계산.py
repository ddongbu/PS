import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
result = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

    def dfs(v, cnt):
        cnt += 1
        visited[v] = True

        if v == b:
            result.append(cnt)
        for i in graph[v]:
            if not visited[i]:
                dfs(i, cnt)  # 재귀


dfs(a, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
