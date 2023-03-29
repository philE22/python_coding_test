import sys
input = sys.stdin.readline

N, M = map(int, input().split())

miro = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
before = [(-1, 0), (0, -1)]
dp[0][0] = miro[0][0]

for x in range(N):
    for y in range(M):
        for a, b in before:
            mx = x + a
            my = y + b
            if mx >= 0 and my >= 0:
                dp[x][y] = max(dp[x][y], dp[mx][my] + miro[x][y])
            
print(dp[N-1][M-1])