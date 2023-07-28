#5개의 자연수들중 적어도 3개로 나누어지는 가장 작은 자연수

num = list(map(int,input().split()))
cnt = 0
i = 1
while cnt<3:
    cnt = 0
    for n in num:
        if i % n == 0:
            cnt += 1
        if cnt == 3:
            break
    i += 1
    
print(i-1)
