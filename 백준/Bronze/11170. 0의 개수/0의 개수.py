import sys

T = int(input())

#N 부터 M의 숫자들중 0을 세서 cnt++
for i in range(T):
    N,M = map(int, sys.stdin.readline().split())
    cnt = 0
    for i in range(N,M+1):
        w = str(i)
        cnt += w.count('0')
    print(cnt)

