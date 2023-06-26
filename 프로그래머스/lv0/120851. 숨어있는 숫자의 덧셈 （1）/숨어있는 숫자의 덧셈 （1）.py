import re  

def solution(my_string):
    answer = re.findall(r'\d',my_string)
    answer = [int(i) for i in answer]
    return sum(answer)
