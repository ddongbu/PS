result_x = int(input())
result_n = int(input())

sum=0

for n in range(result_n):
    a,b = map(int,input().split())
    i = a*b
    sum += i

if result_x == sum:
    print("Yes")
else:
    print("No")
