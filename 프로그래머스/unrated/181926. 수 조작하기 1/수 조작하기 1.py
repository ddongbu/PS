def solution(n, control):
    for i in range(len(control)):
        if control[i:i+1] == "w":
            n += 1
        elif control[i:i+1] == "s":
            n -= 1    
        elif control[i:i+1] == "d":
            n += 10
            
        elif control[i:i+1] == "a":
            n -= 10
        else:
            break
    return n