def solution(arr):
    answer = []
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]
    #arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수
    #조건 -> 
    # 배열이 빈 배열일 경우 -1을 채워서 리턴