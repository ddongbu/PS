#최소일수 에서 bfs를 유추
from collections import deque
import sys

input = sys.stdin.readline
m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]
queue = deque([])
res = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i,j])

d = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs():
    while queue:
        x,y = queue.popleft()
        for dx , dy in d:
            nx , ny = x + dx , y + dy
            if 0 <= nx < n and 0<=ny<m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y]+1
                queue.append([nx,ny])

bfs()
for i in tomato:
    for j in i:
        #찾아서 익지 않았다면 -1
        if j== 0:
            print(-1)
            exit(0)
    # 다익혔으면 그게 정답
    res = max(res,max(i))
# 처음시작을 1로 했으니 1을 빼준다.
print(res-1)
