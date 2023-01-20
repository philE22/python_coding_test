import sys
input = sys.stdin.readline
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
    
# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 0을 출력
        if g[a][b] == INF:
            print(0, end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(g[a][b], end=" ")
    print()