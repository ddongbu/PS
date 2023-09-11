def solution(n, m):
    gcd = 0 # 최대공약수 (greatest common factor)
    lcm = 0 # 최소공배수 (least common multiple)
    #최대공약수
    #둘 중 작은 수 ~ 1 까지 내려가면서 n, m을 i로 나눴을 때 나머지가 0이면 최대공약수!
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break
    #최소공배수 공식( n*m / n와m의 최대공약수)
    lcm = (n*m) // gcd # = int(n*m / gcd)
    # [최대공약수, 최소공배수]
    return [gcd, lcm]

