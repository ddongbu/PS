def solution(n):
    #n이 x의 제곱인지 판단하기
    num = n ** 0.5
    if num == int(num):
        return (num+1) ** 2
    else:
        return -1
    #n이 제곱이라면 x+1
    #n이 제곱이 아니라면 -1 return