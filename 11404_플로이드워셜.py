INF = int(1e9)

n = int(input())
m = int(input())
g = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(1, n+1):
    g[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if g[a][b] == INF:
        g[a][b] = c   
    else:
        g[a][b] = min(c, g[a][b])

for k in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            g[a][b] = min(g[a][b], g[a][k] + g[k][b])
            
for i in range(1, n + 1):
    arr = g[i]
    arr = list(map(str, arr[1:]))
    print(" ".join(arr))