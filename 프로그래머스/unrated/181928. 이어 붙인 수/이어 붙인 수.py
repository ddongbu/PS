def solution(num_list):
    odd_sum = 0
    even_sum = 0
    odd_numbers = []
    even_numbers = []

    for num in num_list:
        if num % 2 != 0:  # 홀수인 경우
            odd_sum += num
            odd_numbers.append(str(num))
        else:  # 짝수인 경우
            even_sum += num
            even_numbers.append(str(num))

    odd_concatenated = int(''.join(odd_numbers))
    even_concatenated = int(''.join(even_numbers))

    return odd_concatenated + even_concatenated
