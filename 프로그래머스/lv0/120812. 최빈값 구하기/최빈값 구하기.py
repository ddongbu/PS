from collections import Counter

def solution(array):
    counter = Counter(array)
    most = counter.most_common()
    maximum = most[0][1]
    li =[]
    for num in most:
        if num[1] == maximum:
            li.append(num[0])
    if len(li) >= 2:
        return -1
    else:
        return li[0]
   