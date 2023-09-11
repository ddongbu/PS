def solution(x):
    #자릿수를 나누어 합을 구하고 그 합은 원래 문자열에 나누어 떨어지나 
    X=[int(i) for i in str(x)]
    if x % sum(X) == 0:
        return True
    else:
        return False