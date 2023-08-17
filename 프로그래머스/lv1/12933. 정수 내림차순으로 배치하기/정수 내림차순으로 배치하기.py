def solution(n):
    ls = list(str(int(n))) #정수형 n을 문자열로 변환한뒤 ls의 리스트에 저장
    ls.sort(reverse = True) #리스트를 내림차순으로 정렬
    return int("".join(ls)) #join으로 합친후 정수형 변환