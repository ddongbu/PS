input()
l = list(map(int, input().split()))
min, max = 1000000, -1000000

for item in l:
  if item > max:
    max = item
  if item < min:
    min = item

print(min, max)