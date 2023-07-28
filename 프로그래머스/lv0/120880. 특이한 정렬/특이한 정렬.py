def solution(numlist, n):
    #n과의 거리의 절댓값인 abs(x-n)에 대해 먼저 정렬을 하고 
    #abs(n-x)가 같으면 n-x가 큰 값을 먼저 정렬한다.
    result = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return result