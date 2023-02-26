n = int(input())

arr = []
for _ in range(n):
    x, y = input().split()
    arr.append([int(x), y])

arr.sort(key=lambda x: x[0])

for a, b in arr:
    print(str(a) + " " + b)