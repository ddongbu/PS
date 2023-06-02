def solution(sides):
    #가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야한다.
    # 'A'  < B + C
    sides.sort()
    #리스트를 sort하기
    if sides[0] + sides[1] > sides[2]:
        return 1
    else:
        return 2
    # 가장 긴 배열의 요소 와 남은 두 원소 합을 비교하기
    # 조건문으로 return
    
    return answer