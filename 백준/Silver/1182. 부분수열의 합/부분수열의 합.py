import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i) #배열에서 뽑을 수 있는 모든 조합을 구해준다.
    for x in comb:
        if sum(x) == s: #총합이 구해고자 하는 합과 같다면
            cnt += 1 #cnt +

print(cnt)