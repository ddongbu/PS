def solution(n):
    n = str(n)
    n = list(map(int,list(n)))
    n = sorted(n,reverse=True)
    
    return int("".join(map(str,n)))