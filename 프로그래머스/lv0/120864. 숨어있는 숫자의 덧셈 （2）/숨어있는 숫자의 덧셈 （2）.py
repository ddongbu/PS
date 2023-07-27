import re
def solution(my_string):
    sum=0
    numbers = re.findall(r'\d+', my_string)
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
        sum += numbers[i]
    return sum