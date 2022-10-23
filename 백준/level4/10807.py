times = int(input())

list = list(map(int, input().split()))

num = int(input())
count = 0

for i in list:
    if i == num:
        count += 1

print(count)