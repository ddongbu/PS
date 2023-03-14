def solution(numbers):
    numbers.sort(reverse=True)
    return int(numbers[0] * numbers[1])