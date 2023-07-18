def solution(s):
    answer = []
    
    for num in s.split():
        if num == "Z":
            answer.pop()
            continue
        answer.append(int(num))
        
    return sum(answer)