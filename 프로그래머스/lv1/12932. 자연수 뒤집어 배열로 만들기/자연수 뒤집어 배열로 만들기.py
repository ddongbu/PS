def solution(n):
    n_list = []
    
    n = str(n)
    n_list = list(n)
    n_list = list(map(int, n_list))
    
    n_list.reverse()
    return n_list
    
