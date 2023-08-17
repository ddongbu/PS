n,k = map(int,input().split())
numlist = []
for i in range(1, n + 1):
    if n % i == 0:
        numlist.append(i)
if len(numlist) < k:
    print(0)
else:
    print(numlist[k-1])