def find_a_factor(n):
    factor_list = []    
    for num in range(1, (n // 2) + 1):
        if n % num == 0:
            factor_list.append(num)
    factor_list.append(n)
    return factor_list

def solution(n):    
    return len(find_a_factor(n=n))