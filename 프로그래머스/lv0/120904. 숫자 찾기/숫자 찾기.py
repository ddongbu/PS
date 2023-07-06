def solution(num, k):
    num = str(num)
    k = str(k)
    if num.find(k) < 0 :
        return -1
    else:
        return num.find(k) + 1
