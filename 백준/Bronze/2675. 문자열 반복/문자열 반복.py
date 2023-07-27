#몇번 할건지 입력받기

#반복문으로 입력값 받기
#형변환해준후
#반복문으로 문자 찍어주기

Count = int(input())

for i in range(Count):
    R,S = input().split()
    R = int(R)
    for i in range(len(S)):
        print(R*S[i],end="")
    print()
