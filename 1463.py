N = int(input())

dp = [0] * (N + 1)
dp[1] = 0
n = 2

#dp[n] = min(dp[n / 3] + 1, dp[n / 2] + 1, dp[n - 1] + 1)

while n <= N:
    dp[n] = dp[n - 1] + 1
    if n % 3 == 0:
        dp[n] = min(dp[n // 3] + 1, dp[n])
    if n % 2 == 0:
        dp[n] = min(dp[n // 2] + 1, dp[n])
    n += 1

print(dp[N])