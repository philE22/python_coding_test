n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
# #다이나믹 프로그래밍
# #dp[n] : n일까지의 이익
dp = [0] * (n + 1)
# for i in range(n-1, -1, -1):
#     if i + arr[i][0] > n:
#         dp[i] = dp[i + 1]
#     else:
#         dp[i] = max(arr[i][1] + dp[i+arr[i][0]], dp[i + 1])

# print(dp[0])

for i in range(n):
    for j in range(i + arr[i][0], n+1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]
            
print(dp[-1])