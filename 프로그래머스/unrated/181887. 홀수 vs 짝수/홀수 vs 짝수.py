def solution(num_list):
    oddsum = 0
    evensum = 0
    for index, value in enumerate(num_list):
        if index % 2 == 0:
            oddsum += value
        else:
            evensum += value
            
    return max(oddsum,evensum)
    