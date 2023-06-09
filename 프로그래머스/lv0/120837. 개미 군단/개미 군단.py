def solution(hp):
    #개미들의 리스트 생성
    ant_list = [5, 3, 1]
    
    total_ant_num, ant_idx= 0, 0
    
    while True:
        if hp <= 0:
            break
        
        ant_ap = ant_list[ant_idx]
        
        ant_num = hp // ant_ap
        
        total_ant_num += ant_num
        
        hp -= ant_num * ant_ap
        
        ant_idx += 1
    
    return total_ant_num