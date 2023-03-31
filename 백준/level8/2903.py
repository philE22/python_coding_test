N = int(input())

li = [0] * (N+1)
li[1] = 3
for i in range(2, N+1):
    li[i] = li[i-1] * 2 - 1

print(li[N] ** 2)