def solution(n):
    sum=0
    for _ in range(n):
        if n%2==0:
            sum+=n
        n -=1
    return sum