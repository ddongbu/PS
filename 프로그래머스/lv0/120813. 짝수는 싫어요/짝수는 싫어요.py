def solution(n: int) -> list:
    return [x for x in range(1, n+1) if x % 2 == 1]

if __name__ == '__main__':
    print(solution(10))   # [1, 3, 5, 7, 9]
    print(solution(15))   # [1, 3, 5, 7, 9, 11, 13, 15]