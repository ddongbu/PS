def solution(arr):
    sum = 0
    answer = 0
    #리스트 안의 요소들의 총합 구하기
    for i in range(len(arr)):
        sum += arr[i]
    return sum / len(arr)
    # 총합 / 나누기 = 평균