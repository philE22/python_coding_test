N = int(input())


dp = [0] * (N + 1)
dp[1] = 0
n = 3
#dp[n] = min(dp[n / 3] + 1, dp[n / 2] + 1, dp[n - 1] + 1)
arr = []
while n <= N:
    if n % 3 == 0:
        arr.append(dp[n // 3] + 1)
    if n % 2 == 0:
        arr.append(dp[n // 2] + 1)
    arr.append(dp[n - 1] + 1)
    
    dp[n] = min(arr)
    arr.clear()
    n += 1

print(dp[N])
