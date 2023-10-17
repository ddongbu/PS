# BFS를 이용해 음식물 그룹을 파악함과 동시에 음식물 개수를 반환한다.
from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().strip().split())
graph = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().strip().split())
    graph[r - 1][c - 1] = 1

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0  #방문
    cnt = 0
    while q:
        y, x = q.popleft()
        cnt += 1
        for dy, dx in d:
            Y, X = y + dy, x + dx
            if (0 <= Y < n) and (0 <= X < m) and graph[Y][X] == 1:
                graph[Y][X] = 0
                q.append((Y, X))
    return cnt


result = 1
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            # print(bfs(y, x))
            result = max(result, bfs(y, x))

print(result)
