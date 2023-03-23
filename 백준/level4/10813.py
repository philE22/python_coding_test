N, M = map(int, input().split())
li = [str(i) for i in range(1, N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    tmp = li[b-1]
    li[b-1] = li[a-1]
    li[a-1] = tmp

print(" ".join(li))