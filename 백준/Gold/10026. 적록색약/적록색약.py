import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


# 무조건 NxN 정사각형
n = int(input().rstrip())
square = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 적록색약이 아닌사람 #적록색약인 사람의 cnt
three_cnt, two_cnt = 0, 0
# (상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True
    current_color = square[x][y]

    # deque 생성
    queue = deque()
    queue.append((x, y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            # 현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
            if visited[nx][ny] == False:
                if square[nx][ny] == current_color:
                    dfs(nx, ny)


for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.
        if visited[i][j] == False:
            dfs(i, j)
            three_cnt += 1

# R을 G로 바꾼다 결국엔 같은 색깔
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
# 카운트 값 도출
