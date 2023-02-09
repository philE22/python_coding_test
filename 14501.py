n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
#답 찾아보고 품
dp = [0] * (n + 1)

for i in range(n):
    for j in range(i + arr[i][0], n+1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]
            
print(dp[-1])

#바텀업 방식
# for i in range(n-1, -1, -1):
#     if i + arr[i][0] > n:
#         dp[i] = dp[i + 1]
#     else:
#         dp[i] = max(arr[i][1] + dp[i+arr[i][0]], dp[i + 1])

# print(dp[0])