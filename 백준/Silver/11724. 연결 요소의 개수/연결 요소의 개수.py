from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
# 정점과 간선의 개수
visited = [False] * (N + 1)
# False로 된 리스트 하나 생성 (초기화)
graph = [[] for _ in range(N + 1)]
# 정점의 갯수 만큼의 리스트 생성

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1

print(cnt)
