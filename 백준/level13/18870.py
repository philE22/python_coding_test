N = int(input())
li = list(map(int, input().split()))

sorted_li = sorted(set(li))
dp = dict()

for index in range(len(sorted_li)):
    dp[sorted_li[index]] = index
print(dp)
for num in li:
    print(dp[num], end=" ")
