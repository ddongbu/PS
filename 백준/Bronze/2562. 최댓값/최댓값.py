item = []
for i in range(9):
    item.append(int(input()))

print(max(item))
print(item.index(max(item))+1)