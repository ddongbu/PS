def solution(array, n):
    MAX = 9999
    answer = -1

    array.sort()
    #정렬알고리즘 가동 푸슝푸슝
    for a in array:
        if abs(n - a) < MAX:
            MAX = abs(n - a)
            answer = a

    return answer