N, M = map(int, input().split())
bucket = ["0"] * N
li = []
for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i-1, j):
        bucket[index] = str(k)

print(" ".join(bucket))