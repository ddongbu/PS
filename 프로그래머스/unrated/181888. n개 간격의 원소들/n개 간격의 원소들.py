def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list)+1,n):
        try:
            answer.append(num_list[i])
        except:
            pass
    return answer