from collections import Counter
def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        answer += Counter(str(num))[str(k)]
    return answer