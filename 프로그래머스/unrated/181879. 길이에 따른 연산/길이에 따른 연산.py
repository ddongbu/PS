from functools import reduce

def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return reduce(lambda x, y: x * y, num_list)
    
    