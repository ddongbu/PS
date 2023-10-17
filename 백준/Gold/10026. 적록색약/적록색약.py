import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


n = int(input().rstrip())
square = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

three_cnt, two_cnt = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True
    current_color = square[x][y]


    queue = deque()
    queue.append((x, y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):

            if visited[nx][ny] == False:
                if square[nx][ny] == current_color:
                    dfs(nx, ny)


for i in range(n):
    for j in range(n):
        
        if visited[i][j] == False:
            dfs(i, j)
            three_cnt += 1


for i in range(n):
    for j in range(n):
        if square[i][j] == "R":
            square[i][j] = "G"
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            two_cnt += 1

print(three_cnt, two_cnt)

