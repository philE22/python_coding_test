n = int(input())

arr = list(map(int, input().split()))

print(arr)
count = 0
for i in arr:
    check = True
    if i == 1:
        continue
    for j in range(2, i):
        if i%j == 0:
            check = False
            break
    if check:
        count += 1

print(count)