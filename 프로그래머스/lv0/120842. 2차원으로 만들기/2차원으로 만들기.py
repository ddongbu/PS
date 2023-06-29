def solution(num_list, n):
    answer = []
    array=list(range(0,len(num_list),n))
    for i in array:
        answer.append(num_list[0+i:n+i])
        print(answer)
    return answer