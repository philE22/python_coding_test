"""
n-1번째 창고를 털고 현재 창고를 넘길지,
n-2번째 창고를 털고 현재 창고를 털지,
둘 중 큰 값을 구하는 방식으로 진행
4
1 3 1 5
"""
n = int(input())
arr = list(map(int, input().split()))

d = [0] * 100
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, n):
    d[i] = max(d[i-2] + arr[i], d[i - 1])
    
print(d[n-1])