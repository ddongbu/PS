def solution(n):
    tmp = 6 / n
    i=1
    while(1):
        if (tmp * i).is_integer():
            return i
        i+=1