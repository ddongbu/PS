def solution(x):
    #하샤드수 = x의 자리수의 합으로 x가 나누어져야 한다.
    if x % sum(map(int, str(x))) == 0 :
        answer = True
    else:
        answer = False
    return answer