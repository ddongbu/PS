def solution(n):
    #n보다 작은 자연수들의 합이 n과 같은 것
    
    result = 1
    #자기자신도 세기 때문에
    for i in range(1, n // 2 + 1):
        #n의 중반까지 순회
        total = 0
        while total < n:
            total += i
            if total == n:
                result += 1
                break
            i += 1
    return result