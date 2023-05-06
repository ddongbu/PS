def solution(n):
    answer = 0
    #n이 홀수라면 n이하의 모든 홀수 합
    if n % 2 == 1:
        for i in range(n+1):
            if i % 2 == 1:
                answer += i
     #n이 짝수라면 n이하의 모든 짝수의 제곱의 합
    else:
        for i in range(n+1):
            if i % 2 == 0:
                answer += i ** 2
    return answer