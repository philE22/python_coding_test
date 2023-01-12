import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().split()))
    
#이름, 국어, 영어, 수학
arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: int(x[3]), reverse=True)
arr.sort(key=lambda x: int(x[2]))
arr.sort(key=lambda x: int(x[1]), reverse=True)

for i in arr:
    print(i[0])
    