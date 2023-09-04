def solution(nums):
    answer = 0
    poncatmon = len(set(nums))
    catch_pon = len(nums) // 2
    answer = min(poncatmon,catch_pon)
    return answer

#n/2 개를 선택가능
#n/2 개 선택 중 종을 가장 다양하게 선택
#그렇다면 n/2가 종의 수보다 크면 종의 수만큼 선택
#아니라면 n/2가 종의 수보다 작다면 n/2를 출력

