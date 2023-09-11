def solution(phone_number):
    total_phone_number = len(phone_number)
    back_phone_number = phone_number[-4:]
    return '*' * (total_phone_number-4) + back_phone_number