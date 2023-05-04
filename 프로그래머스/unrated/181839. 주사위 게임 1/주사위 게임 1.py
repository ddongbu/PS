def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:
        result  = a**2 + b ** 2
    elif a % 2 == 1 or b % 2 == 1:
        result = 2*(a+b)
    else:
        result = abs(a-b)
    return result