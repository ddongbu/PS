def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return num_list.index(num_list[i])
    else:
        return -1

