def solution(a, b):
    resultA = 2*a*b
    resultB = str(a) + str(b)
    
    if resultA > int(resultB):
        return resultA
    else:
        return int(resultB)