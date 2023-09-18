def solution(s):
    # [1, 2, 3, 4] 숫자형
    s = list(map(int,s.split(" ")))
    result = f'{min(s)} {max(s)}'
    return result