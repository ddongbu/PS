import re

def solution(number):
    #음이 아닌 정수를 9로 나눈 나머지 = 음이아닌정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같다
    numbers = re.findall(r'\d', number)
    numbers = list(map(int, numbers))
    sum_list = sum(numbers) % 9
    
    return sum_list