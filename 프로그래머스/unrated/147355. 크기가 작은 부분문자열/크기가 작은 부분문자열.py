def solution(t, p):
    cnt = 0
    for idx in range(0,len(t) - len(p) + 1):
        if t[idx:idx+len(p)] <= p:
            cnt += 1
    return cnt