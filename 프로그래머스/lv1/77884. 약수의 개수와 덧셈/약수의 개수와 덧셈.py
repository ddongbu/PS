def solution(left, right):
    answer = 0
    # 1부터 5까지의 수 중에서
    for i in range(left,right+1):
        now_count = 0
        for j in range(1, i+1):		#1부터 i까지 증가하며 약수를 찾아냅니다.
            if i % j == 0:		#나누어 떨어지는 수는 약수!
                now_count +=1;		#약수라면 개수를 증가시켜줍니다.
        if now_count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
    # 약수의 개수가 짝인수는 더하고
    # 약수의 갯수가 홀수인수는 빼자
    
    return answer
    