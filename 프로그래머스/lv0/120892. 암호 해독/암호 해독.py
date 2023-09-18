def solution(cipher, code):
    answer = ''
    #cipher code의 배수 만큼이 진짜 글자
    for i in range(code,len(cipher)+1):
        if i % code == 0:
            answer += cipher[i-1]
    return answer