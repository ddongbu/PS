#은민이는 4, 7 만좋아해서 금민수라는 수를 만들었어
#금민수는 4,7로만 이루어진 수야

#n이 주어졌을때 n보다 작거나 같은 금민수중 가장 큰것
#n은 자연수 4보다 크거나 같고 백만보다 작거나 같아

n = int(input())

while True:
    flag = True
    for i in str(n):
        if i!="4" and i!="7":
            flag = False
            n -=1
    if flag:
        print(n)
        break