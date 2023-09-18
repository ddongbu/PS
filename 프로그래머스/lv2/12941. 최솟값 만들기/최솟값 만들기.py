def solution(A,B):
    answer = 0
    #각 배열은 자연수, A,B 둘중에 한개의 숫자를 뽑아 두수를 곱한다.
    #이러한 과정을 배열의 길이만큼 반복한다.
    #두수를 곱한 값을 누적하여 더한다.
    #최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표다.
    #작은값 * 큰값은 은 최솟값이다.
    A = sorted(A)
    B.sort(reverse=True)
    
    for a in range(len(A)):
        val = A[a] * B[a]
        answer += val
    return answer

# def solution(A,B):
#     answer = 0
#     A.sort()
#     B.sort(reverse = True)


#     for a in range(len(A)):
#         val = A[a] * B[a]
#         answer += val

#     return answer
