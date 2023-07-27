def solution(arr, k):
    answer = []
    #k가 홀수라면 K를 곱하라
    if k % 2 == 0:
        answer = [num + k for num in arr]
    else:
        answer = [num * k for num in arr]
    
    return answer
    #K가 짝수라면 K를 더하라

        
            