import sys
input = sys.stdin.readline

ans,x,y = -1,0,0
for i in range(9):
    arr = list(map(int,input().split()))
    for j in range(9):
        if arr[j] > ans:
            ans,x,y = arr[j],i,j
print(ans,x+1,y+1,sep="\n")