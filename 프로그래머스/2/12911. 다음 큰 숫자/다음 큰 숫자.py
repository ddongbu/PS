def solution(n):
    
    #c = 매개변수n의 2진수 값의 1의 갯수를 카운트한 값을 삽입
    #(n+1 , 1000001)
    #m = 다음에 올 n보다 큰 자연수 (n+1)부터 시작
    #제한사항 n은 1,000,000 이하의 자연수 입니다
    c = bin(n).count('1')
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m
    return answer