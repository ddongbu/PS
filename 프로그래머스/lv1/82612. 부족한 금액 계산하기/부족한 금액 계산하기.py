def solution(price, money, count):
    result = 0
    for i in range(count+1):
        result += price * i
        
    if result >= money:
        return abs(result - money)
    else:
        return 0
