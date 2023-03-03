import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
result = [list(map(int, input().split())) for _ in range(M)]
dp = [[0] * (N + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + m[i-1][j-1]

for a, b, c, d in result:
    print(dp[c][d] - dp[a - 1][d] - dp[c][b - 1] + dp[a - 1][b - 1])
