import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0


def bfs(idx, sub_sum):
    global cnt

    if idx >= n:  # 백 트래킹
        return

    sub_sum += arr[idx]

    if sub_sum == s:
        cnt += 1

    # 현재 arr[idx]를 선택한 경우의 가지
    bfs(idx + 1, sub_sum)

    # 현재 arr[idx]를 선택하지 않은 경우의 가지
    bfs(idx + 1, sub_sum - arr[idx])


bfs(0, 0)
print(cnt)
