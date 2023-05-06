def solution(before, after):
    #글자 요소 갯수만 같으면 return 해주는 문제
    #before의 알파벳순서로 정렬
    before=sorted(before)
    #after의 알파벳순서로 정렬
    after=sorted(after)
    
    #before와 after의 요소 갯수의 조건문
    if before == after:
        return 1
    else:
        return 0