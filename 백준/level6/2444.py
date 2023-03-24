N = int(input())

for i in range(1, N+1):
    s = " " * (N-i)
    s += "*" * (i * 2 - 1)
    print(s)
for i in range(1, N):
    s = " " * (i)
    s += "*" * (N * 2 - 1 - 2*i)
    print(s)