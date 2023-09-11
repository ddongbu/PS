def solution(price, money, count):
    result = 0
    answer = 0
    #price원인데 만약 n번째 이용하면 price * n
    for i in range(count+1):
        result += price * i
        
    if result >= money:
        answer = result - money 
        return abs(answer)
    else:
        return 0
