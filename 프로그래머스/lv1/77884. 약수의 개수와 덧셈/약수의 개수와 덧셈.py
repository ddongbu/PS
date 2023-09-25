def solution(left, right):
    result = 0  # 결과값을 저장할 변수 초기화
    for i in range(left,right+1):
        if int( i ** 0.5) == i ** 0.5:
            result -= i
        else:
            result += i
    return result  # 최종 결과값 반환